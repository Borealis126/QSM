import numpy as np
import os
import time
from dataIO import jsonRead, jsonWrite, csvRead, arrayNoBlanks, readY11Data
from ansysAPI import *
import subprocess
from q3dSimulations import Q3DExtractor
from hfssSimulations import *
from circuitSimulations import *
from sympy import symbols
from constants import *
from misc import *
from quantumState import stateFromHeader, baseRepresentation, H_Header
from scipy.misc import derivative
from sympy import Matrix, zeros, sin
from qSysObjects import ReadoutResonator, Qubit
from qutip import state_number_index, qzero, ket, bra, tensor, destroy, qeye
from qubitDesigns import FloatingRectangularTransmonSingleJJ, GroundedRectangularTransmonSingleJJ
from controlLineDesigns import FeedLine

"""Simulations are anything that is saved to a folder. 
These are anything requiring Ansys and anything with a non-trivial calculation time (matrix inversion, etc.)"""


class Simulation:
    def __init__(self, qArch, simName):
        qArch.loadDesignFiles()  # Every time a Simulation instance is made, the design files are loaded.
        self.qArch = qArch
        self.simName = simName
        self.q3dSims = dict()
        self.hfssSims = dict()
        self.circuitSims = dict()

        self.directoryPath = self.qArch.sysParams["Project Folder"] / self.simName

        self.paramsPath = self.directoryPath / "SimulationParameters.json"
        self.resultsFilePath = self.directoryPath / "Results.json"

        self.simParams = dict()
        self.resultsDict = dict()
        if os.path.exists(self.paramsPath):
            self.simParams = jsonRead(self.paramsPath)
        if os.path.exists(self.resultsFilePath):
            self.resultsDict = jsonRead(self.resultsFilePath)

    def runAnsysSimulator(self, aedtFile, simulatorFile, maxRunTime):
        simulateCommand = ""
        if self.qArch.sysParams["Compute Location"] == "Windows":
            ansysExecutableFile = "\"%ProgramFiles%/AnsysEM/v221/Win64/ansysedt.exe\""
            simulateCommand = (str(ansysExecutableFile) + ' -features=beta -ng -runscriptandexit '
                               + str(simulatorFile) + ' ' + str(aedtFile))
        elif self.qArch.sysParams["Compute Location"] == "Cluster":
            simulateCommand = (str(self.qArch.sysParams["QSM Source Folder"] / "helperFiles" / "ansysBatch") + " ansys "
                               + str(simulatorFile) + " " + str(aedtFile) + " "
                               + str(self.directoryPath) + " " + str(maxRunTime))
        subprocess.call(simulateCommand, shell=True)

    def createDirectory(self):
        # Create the directory if it doesn't yet exist.
        if self.qArch.sysParams["Compute Location"] == "Windows":
            bashCommand = "if not exist " + str(self.directoryPath) + " mkdir " + str(self.directoryPath)
            subprocess.call(bashCommand, shell=True)
        elif self.qArch.sysParams["Compute Location"] == "Cluster":
            subprocess.call("rm -rf " + str(self.directoryPath), shell=True)
            bashCommand = "mkdir -p " + str(self.directoryPath)
            subprocess.call(bashCommand, shell=True)

    def generateParams(self, simParamsDict):
        self.createDirectory()
        jsonWrite(self.paramsPath, simParamsDict)

    def runAllSims(self):  # Specifically reserved for Ansys simulations.
        # Delete previous run files
        if self.qArch.sysParams["Compute Location"] == "Cluster":
            subprocess.call("rm -f " + str(self.directoryPath / "/*slurm*"), shell=True)
            subprocess.call("rm -f " + str(self.directoryPath / "/*script.*"), shell=True)
            subprocess.call("rm -f " + str(self.directoryPath / "/nodes"), shell=True)
            subprocess.call("rm -f " + str(self.directoryPath / "/*.log*"), shell=True)
            subprocess.call("rm -f " + str(self.directoryPath / "/*Results*"), shell=True)
        for q3dSimName, q3dSim in self.q3dSims.items():
            """Run all Q3D simulations for the given simulation. 
            Assumes they were initialized when the Ansys file was created."""
            self.copyAnsysFile(q3dSim.aedtPath)
            simulatorFileInstance = open(q3dSim.simulatorPath, "w+", newline='')
            simulatorFileInstance.writelines(q3dSim.lines)
            simulatorFileInstance.close()
            self.runAnsysSimulator(q3dSim.aedtPath, q3dSim.simulatorPath, 60)
        for hfssSimName, hfssSim in self.hfssSims.items():
            self.copyAnsysFile(hfssSim.aedtPath)
            simulatorFileInstance = open(hfssSim.simulatorPath, "w+", newline='')
            simulatorFileInstance.writelines(hfssSim.lines)
            simulatorFileInstance.close()
            self.runAnsysSimulator(hfssSim.aedtPath, hfssSim.simulatorPath, 60)

        for circuitSimName, circuitSim in self.circuitSims.items():
            """"Initialize all circuit simulations for the given simulation."""
            self.copyAnsysFile(circuitSim.aedtPath)
            # Generate the netlist file and load it into the AEDT
            writeFile = open(circuitSim.netlistPath, "w")
            writeFile.writelines(netlistHeaderLines)
            writeFile.write("\n")
            writeFile.writelines(circuitSim.netlistComponentsLines)
            writeFile.writelines(circuitSim.netlistPortsLines)
            writeFile.write("\n")
            writeFile.writelines(circuitSim.netlistSimulationLines(self.simParams))
            writeFile.write("\n")
            writeFile.write(".end")
            writeFile.close()
            loadNetlistFile(circuitSim.aedtPath, circuitSim.netlistPath)
            # Generate and run the ansysRunSimulator file
            lines = ansysSimulatorPreamb.copy()
            lines += [
                "oProject = oDesktop.SetActiveProject(\"" + circuitSim.name + "\")\n",
                "oDesign = oProject.SetActiveDesign(\"" + "Netlist" + "\")\n",
                "oModuleReport = oDesign.GetModule(\"ReportSetup\")\n",
                "oDesign.AnalyzeAll()\n"
            ]
            lines += circuitSim.reportLines
            lines.append(ansysSaveLine)

            simulatorFileInstance = open(circuitSim.ansysRunSimulatorPath, "w+", newline='')
            simulatorFileInstance.writelines(lines)
            simulatorFileInstance.close()
            self.runAnsysSimulator(circuitSim.aedtPath, circuitSim.ansysRunSimulatorPath, 3)  # CircuitSims are fast.

    def deleteUnneededFiles(self):
        # Check if all simulations have completed. Delete Ansys folders.
        if self.qArch.sysParams["Compute Location"] == "Cluster":
            proceed = False
            while not proceed:
                proceed = True
                for q3dSimName, q3dSim in self.q3dSims.items():
                    if not os.path.exists(q3dSim.resultsFilePath):
                        proceed = False
                for hfssSimName, hfssSim in self.hfssSims.items():
                    if not os.path.exists(hfssSim.resultsFilePath):
                        proceed = False
                for circuitSimName, circuitSim in self.circuitSims.items():
                    if not os.path.exists(circuitSim.resultsFilePath):
                        proceed = False
        time.sleep(1)
        # Delete all Ansys results folders (~90MB for capMat)
        for q3dSimName, q3dSim in self.q3dSims.items():
            self.qArch.deleteFolder(str(q3dSim.aedtFolderPath))
        for circuitSimName, circuitSim in self.circuitSims.items():
            resultsFolder = str(circuitSim.aedtFolderPath)
            if os.path.exists(resultsFolder):
                self.qArch.deleteFolder(resultsFolder)

    def copyAnsysFile(self, ansysPath):
        if os.path.exists(str(ansysPath)):
            self.qArch.deleteFile(str(ansysPath))
        copyAEDTTemplateCommand = ""
        if self.qArch.sysParams["Compute Location"] == "Windows":
            copyAEDTTemplateCommand = (
                    "copy "
                    + str(self.qArch.sysParams["QSM Source Folder"] / "helperFiles" / "template.aedt")
                    + " " + str(ansysPath)
            )
        if self.qArch.sysParams["Compute Location"] == "Cluster":
            copyAEDTTemplateCommand = (
                    "cp " + str(self.qArch.sysParams["QSM Source Folder"] / "helperFiles" / "template.aedt")
                    + " " + str(ansysPath)
            )
        subprocess.call(copyAEDTTemplateCommand, shell=True)


class HFSSModel(Simulation):
    def __init__(self, qArch):
        super().__init__(qArch, "HFSSModel")
        hfssSimName = "HFSSModel"
        self.hfssSims = {hfssSimName: HFSSModeler(hfssSimName, self.directoryPath)}

    def initialize(self):
        self.createDirectory()

    def run(self):
        self.hfssSims["HFSSModel"].updateLines(ansysDrawNodes(self.qArch, "3D"))
        self.runAllSims()


class CapMat(Simulation):
    def __init__(self, qArch):
        super().__init__(qArch, "capMat")
        q3dSimName = "capMatExtractor"
        self.q3dSims = {q3dSimName: Q3DExtractor(q3dSimName, self.directoryPath)}

    def initialize(self):
        simParamsDict = {"Dimension": "2D", "PerRefine": "100", "MaxPass": "99"}
        self.generateParams(simParamsDict)

    def run(self):
        self.q3dSims["capMatExtractor"].updateLines(self.simParams, self.capMatLayout_Lines())
        self.runAllSims()

    def postProcess(self):
        # Converts Ansys output data to JSON
        self.deleteUnneededFiles()
        capMatResultsFileLines = csvRead(self.q3dSims["capMatExtractor"].resultsFilePath)
        capMatHeaderLineIndex = 0
        for index, line in enumerate(capMatResultsFileLines):
            if line != [] and line[0] == "Capacitance Matrix":
                capMatHeaderLineIndex = index + 1
        unitsMultiplier = self.capMatUnitsToF
        ansysCapMatHeaders = arrayNoBlanks(capMatResultsFileLines[capMatHeaderLineIndex])
        numNodes = len(ansysCapMatHeaders)
        capMat = np.zeros((numNodes, numNodes))
        capMatStartLineIndex = capMatHeaderLineIndex + 1
        for index1, header1 in enumerate(ansysCapMatHeaders):
            for index2, header2 in enumerate(ansysCapMatHeaders):
                matRow = capMatStartLineIndex + index1
                matCol = 1 + index2
                capacitanceValue = float(capMatResultsFileLines[matRow][matCol]) * unitsMultiplier
                capMat[index1, index2] = capacitanceValue

        resultsDict = {"Header": ansysCapMatHeaders, "capMat (F)": capMat.tolist()}
        jsonWrite(self.resultsFilePath, resultsDict)

    def getChipNSignalNodes(self, N):
        allNodes = []
        for qubitIndex, qubit in self.qArch.chipDict[N].qubitDict.items():
            allNodes += [pad.node for pad in qubit.design.padList]
        for readoutResonatorIndex, readoutResonator in self.qArch.chipDict[N].readoutResonatorDict.items():
            allNodes += [readoutResonator.design.pad1.node, readoutResonator.design.pad2.node]
        for controlLineIndex, controlLine in self.qArch.chipDict[N].controlLineDict.items():
            if isinstance(controlLine.design, FeedLine) and self.qArch.sysParams["Simulate Feedline?"] == "Yes":
                allNodes.append(controlLine.design.lineNode)
        return allNodes

    def capMatLayout_Lines(self):
        lines = ansysDrawNodes(self.qArch, self.simParams["Dimension"])
        # for chipIndex, chip in self.qArch.chipDict.items():
        #     for thisNode in self.getChipNSignalNodes(chip.index):
        #         lines += ansysSignalLine_Lines(thisNode)
        # Assign ground signal line (independent of flip chip)
        # lines += ansysGroundSignalLine_Lines(self.qArch.chipDict[0].ground)

        return lines

    @property
    def capMatUnitsToF(self):
        return self.q3dSims["capMatExtractor"].capMatUnitsToF

    @property
    def ansysCapMatHeaders(self):
        return jsonRead(self.resultsFilePath)["Header"]

    @property
    def capMat(self):
        numNodes = len(self.ansysCapMatHeaders)
        capMat = self.resultsDict["capMat (F)"]
        """If the feedline is not simulated, add in the capacitance to the resonators."""
        if self.qArch.sysParams["Simulate Feedline?"] == "No" and self.qArch.allControlLinesDict != {}:
            newCapMat = [i+[0] for i in capMat.copy()]  # Add a dimension for the feedline, the highest index.
            newCapMat.append([0]*(len(capMat)+1))

            feedlineIndex = numNodes
            self.ansysCapMatHeaders.append(self.qArch.allControlLinesDict[0].design.lineNode.name)

            # Add resonator capacitances
            for readoutResonatorIndex, readoutResonator in self.qArch.allReadoutResonatorsDict.items():
                componentParams = readoutResonator.componentParams
                pad1Index = self.ansysCapMatHeaders.index(readoutResonator.design.pad1.node.name)
                # Capacitance to the feedline
                newCapMat[pad1Index][feedlineIndex] = -componentParams["Capacitance to Feedline (F)"]
                newCapMat[feedlineIndex][pad1Index] = -componentParams["Capacitance to Feedline (F)"]
                # Fix capacitance to ground
                wrongCapToGround = sum(capMat[pad1Index])
                correctCapToGround = componentParams["Feedline Pad Capacitance to Ground (F)"]
                newCapMat[pad1Index][pad1Index] = capMat[pad1Index][pad1Index] - wrongCapToGround + correctCapToGround
            capMat = newCapMat
        return np.array(capMat)


class CapMatGE(Simulation):
    def __init__(self, qArch):
        super().__init__(qArch, "capMatGE")
        # Components ordering
        nonGECapMatIndex = 0
        self.preGECapMatHeaders = []
        self.postGEComponentList = []
        for qubitIndex, qubit in self.qArch.allQubitsDict.items():
            qubit.design.pad1.quantCapMatIndex = nonGECapMatIndex
            self.preGECapMatHeaders.append(qubit.design.pad1.name)
            nonGECapMatIndex += 1
            if isinstance(qubit.design, FloatingRectangularTransmonSingleJJ):
                qubit.design.pad2.quantCapMatIndex = nonGECapMatIndex
                nonGECapMatIndex += 1
                self.preGECapMatHeaders.append(qubit.design.pad2.name)
            self.postGEComponentList.append(qubit)
        for readoutResonatorIndex, readoutResonator in self.qArch.allReadoutResonatorsDict.items():
            readoutResonator.design.pad2.quantCapMatIndex = nonGECapMatIndex  # Only pad2 is included in quantization
            self.preGECapMatHeaders.append(readoutResonator.design.pad2.node.name)
            self.postGEComponentList.append(readoutResonator)
            nonGECapMatIndex += 1

    def initialize(self):
        self.createDirectory()

    def postProcess(self):
        self.deleteUnneededFiles()
        header = [component.name for component in self.postGEComponentList]

        capMat_GE, phiMat, RHS = self.gaussianElimination()
        capMat_GE_np = np.array(capMat_GE).astype(np.float64)
        resultsDict = {"Header": header, "capMatGE (F)": capMat_GE_np.tolist()}

        jsonWrite(self.resultsFilePath, resultsDict)

    @property
    def capMatForGE(self):
        dimPreGEQuant = len(self.preGECapMatHeaders)
        capMat_preGE = zeros(dimPreGEQuant, dimPreGEQuant)
        capMatReduced = Matrix(CapMat(self.qArch).capMat)
        ansysCapMatHeaders = CapMat(self.qArch).ansysCapMatHeaders

        # Alter the resonator pad 2 capacitance to ground according to the lumped resonator model.
        for readoutResonatorIndex, readoutResonator in self.qArch.allReadoutResonatorsDict.items():
            lumpedRSim = LumpedR(readoutResonatorIndex)(self.qArch)
            index = ansysCapMatHeaders.index(readoutResonator.design.pad2.node.name)
            capMatReduced[index, index] = (capMatReduced[index, index]
                                           - sum(capMatReduced.row(index)) + lumpedRSim.equivC)
        """Remove all control lines and resonator pad1 from the capacitance matrix. This is under the assumption that
        the resonator pad1 only has a non-negligible capacitance to the feedline, 
        thereby not affecting the system Hamiltonian."""
        indicesToRemove = []
        for nodeName in ansysCapMatHeaders:
            if nodeName in [controlLine.design.lineNode.name for controlLine in self.qArch.allControlLinesDict.values()]:
                index = ansysCapMatHeaders.index(nodeName)
                indicesToRemove.append(index)
        for readoutResonatorIndex, readoutResonator in self.qArch.allReadoutResonatorsDict.items():
            index = ansysCapMatHeaders.index(readoutResonator.design.pad1.node.name)
            indicesToRemove.append(index)
        indicesToRemove.sort(reverse=True)

        ansysCapMatHeadersReduced = [i for i in ansysCapMatHeaders]  # Simple copy
        for i in indicesToRemove:
            capMatReduced.row_del(i)
            capMatReduced.col_del(i)
            del ansysCapMatHeadersReduced[i]
            # Now reorder quantCapMat to align with self.preGECapMatHeaders
        for node1Index, node1Name in enumerate(self.preGECapMatHeaders):
            for node2Index, node2Name in enumerate(self.preGECapMatHeaders):
                capMat_preGE[node1Index, node2Index] = capMatReduced[ansysCapMatHeadersReduced.index(node1Name),
                                                                     ansysCapMatHeadersReduced.index(node2Name)]
        return capMat_preGE

    def gaussianElimination(self):
        I_c = symbols('I_c')
        dimPreGEQuant = len(self.preGECapMatHeaders)
        # Assemble the RHS and PhiMat
        RHS = zeros(dimPreGEQuant, 1)
        phiMat = zeros(dimPreGEQuant, 1)
        t = symbols('t')
        for component in self.postGEComponentList:
            if isinstance(component.design, FloatingRectangularTransmonSingleJJ):
                RHS[component.design.pad1.quantCapMatIndex, 0] = I_c * sin((component.design.pad1.phiSym - component.design.pad2.phiSym)
                                                                    / Phi_0Const)
                RHS[component.design.pad2.quantCapMatIndex, 0] = -RHS[component.design.pad1.quantCapMatIndex, 0]
                phiMat[component.design.pad1.quantCapMatIndex, 0] = component.design.pad1.phiSym.diff(t, 2)
                phiMat[component.design.pad2.quantCapMatIndex, 0] = component.design.pad2.phiSym.diff(t, 2)
            elif isinstance(component.design, GroundedRectangularTransmonSingleJJ):
                RHS[component.design.pad1.quantCapMatIndex, 0] = I_c * sin(component.design.pad1.phiSym / Phi_0Const)
                phiMat[component.design.pad1.quantCapMatIndex, 0] = component.design.pad1.phiSym.diff(t, 2)
            elif isinstance(component, ReadoutResonator):
                RHS[component.design.pad2.quantCapMatIndex, 0] = component.design.pad2.phiSym / Phi_0Const
                phiMat[component.design.pad2.quantCapMatIndex, 0] = component.design.pad2.phiSym.diff(t, 2)
        capMat_GE = self.capMatForGE
        # Perform the gaussian elimination on just the qubits.
        for componentIndex, component in enumerate(self.postGEComponentList):
            if isinstance(component.design, FloatingRectangularTransmonSingleJJ):
                component.padToEliminate = component.design.pad1
                component.padToKeep = component.design.pad2
                k = component.padToEliminate.quantCapMatIndex
                s = component.padToKeep.quantCapMatIndex
                O_c = zeros(dimPreGEQuant, dimPreGEQuant)
                for i in range(dimPreGEQuant):
                    for j in range(dimPreGEQuant):
                        if i == s and j == s:
                            O_c[i, j] = -1
                        elif i == j:
                            O_c[i, j] = 1
                        elif (i == s and j == k) or (i == k and j == s):
                            O_c[i, j] = 1
                        else:
                            O_c[i, j] = 0
                O_e = zeros(dimPreGEQuant, dimPreGEQuant)
                for i in range(dimPreGEQuant):
                    for j in range(dimPreGEQuant):
                        if i == s and j == s:
                            O_e[i, j] = -1
                        elif i == k and j == s:
                            O_e[i, j] = 1
                        elif i == j and i != s:
                            O_e[i, j] = 1
                        else:
                            O_e[i, j] = 0
                capMatPrime = O_e * capMat_GE * O_c ** -1
                O_GE = zeros(dimPreGEQuant, dimPreGEQuant)
                for i in range(dimPreGEQuant):
                    for j in range(dimPreGEQuant):
                        if i == j:
                            O_GE[i, j] = 1
                        elif j == k and i != k:
                            O_GE[i, j] = -capMatPrime[i, j] / capMatPrime[j, j]
                        else:
                            O_GE[i, j] = 0
                capMat_GE = O_GE * capMatPrime
                RHS = O_e * RHS
                phiMat = O_c * phiMat
        dimGE = len(self.postGEComponentList)
        """Here we go through and remove the kth rows and columns by adding the non-k elements to a new matrix, 
        first by column then by row."""
        kList = []
        for component in self.postGEComponentList:
            if isinstance(component.design, FloatingRectangularTransmonSingleJJ):
                kList.append(component.padToEliminate.quantCapMatIndex)
        """By nature of how we performed GE it's the qubit pad1 that gets eliminated, 
        but the resulting pad is not really "pad2" anymore, it's just the single qubit pad."""
        kListReverse = [i for i in kList]
        kListReverse.sort(reverse=True)

        colMatIter = 0
        colMat = zeros(dimPreGEQuant, dimGE)
        for i in range(dimPreGEQuant):
            if i not in kList:
                colMat[:, colMatIter] = capMat_GE[:, i]
                colMatIter += 1
        RHSReduced = zeros(dimGE, 1)
        phiMatReduced = zeros(dimGE, 1)
        rowMatIter = 0
        rowMat = zeros(dimGE, dimGE)
        for i in range(dimPreGEQuant):
            if i not in kList:
                rowMat[rowMatIter, :] = colMat[i, :]
                RHSReduced[rowMatIter, 0] = RHS[i, 0]
                phiMatReduced[rowMatIter, 0] = phiMat[i, 0]
                rowMatIter += 1
        capMat_GE_Reduced = rowMat
        # We now perform a change-of-variables (COV) and take phi1-phi2 to be our new phi1, etc.
        # RHS_COV=RHSReduced
        # for component in self.postGEComponentList:
        #    if isinstance(component,FloatingQubit):
        #        RHS_COV=RHS_COV.subs(component.pad1.phiSym-component.pad2.phiSym,component.Phi)

        return capMat_GE_Reduced, phiMatReduced, RHSReduced

    @property
    def capMatGE(self):
        return np.array(self.resultsDict["capMatGE (F)"])


class Quantize(Simulation):
    def __init__(self, qArch):
        super().__init__(qArch, "quantize")
        self.CapMatGESim = CapMatGE(self.qArch)

    def initialize(self):
        quantizeList = "["
        for component in CapMatGE(self.qArch).postGEComponentList:
            quantizeList += component.name + ":"
        quantizeList = quantizeList[0:-1] + "]"
        simParamsDict = {"QuantizeList": quantizeList, "NumResonatorPhotons": 5, "NumQubitPhotons": 5,
                         "TrigOrder": 10}
        self.generateParams(simParamsDict)

    def postProcess(self):
        self.deleteUnneededFiles()
        self.quantizeSimulation()

    @property
    def numComponents(self):
        return len(self.HComponentOrder)

    @property
    def maxDim(self):
        return max(self.simParams["NumQubitPhotons"], self.simParams["NumResonatorPhotons"])+2

    def a(self, component):
        tensorState = [qeye(self.maxDim)] * self.numComponents
        tensorState[self.quantizeIndex(component)] = destroy(N=self.maxDim)
        return tensor(tensorState)

    def aDagger(self, component):
        return self.a(component).dag()

    def QSecondQuant(self, component):
        QSecondQuant = None
        if issubclass(type(component), Qubit):
            EC = ECQ(component.index)(self.qArch).EC
            QSecondQuant = 1j * np.sqrt(1 / (2 * component.Z(EC))) * (self.aDagger(component) - self.a(component))
        elif isinstance(component, ReadoutResonator):
            equivL = LumpedR(component.index)(self.qArch).equivL
            EC = ECR(component.index)(self.qArch).EC
            QSecondQuant = 1j * np.sqrt(1 / (2 * component.Z(equivL, EC))) * (self.aDagger(component)
                                                                              - self.a(component))
        return QSecondQuant

    def PhiSecondQuant(self, component):
        PhiSecondQuant = None
        if issubclass(type(component), Qubit):
            EC = ECQ(component.index)(self.qArch).EC
            PhiSecondQuant = np.sqrt(1 * component.Z(EC) / 2) * (self.aDagger(component) + self.a(component))
        elif isinstance(component, ReadoutResonator):
            equivL = LumpedR(component.index)(self.qArch).equivL
            EC = ECR(component.index)(self.qArch).EC
            PhiSecondQuant = np.sqrt(1 * component.Z(equivL, EC) / 2) * (self.aDagger(component) + self.a(component))
        return PhiSecondQuant

    def quantizeSimulation(self):
        print("started quantize")
        quantizeStartTime = time.time()

        capMatGE = self.CapMatGESim.capMatGE
        postGEComponentList = self.CapMatGESim.postGEComponentList

        numQubitPhotons = self.simParams["NumQubitPhotons"]
        numResonatorPhotons = self.simParams["NumResonatorPhotons"]
        # self.capMatGE needs to be reduced based on the requested components to quantize.

        capMatGEIndicesToKeep = [[i.name for i in postGEComponentList].index(i)
                                 for i in [j.name for j in self.HComponentOrder]]

        rows = np.array(capMatGEIndicesToKeep, dtype=np.intp)
        columns = np.array(capMatGEIndicesToKeep, dtype=np.intp)
        capMatGE_quant = capMatGE[rows[:, np.newaxis], columns]

        qObjDim = [self.maxDim] * self.numComponents
        Cinv = np.linalg.inv(capMatGE_quant)

        # Assemble the Hamiltonian. H is in units of radians (H/hbar). Calculates 1/2*Q.T*Cinv*Q.
        print("Start assembling H")
        startTime = time.time()
        resolveLHSSum = qzero(qObjDim)
        for Cinv_rowIndex, Cinv_row in enumerate(Cinv):
            resolveRHSSum = qzero(qObjDim)
            for componentIndex, component in enumerate(self.HComponentOrder):
                resolveRHSSum += Cinv_row[componentIndex] * self.QSecondQuant(component)
            LHSComponent = self.HComponentOrder[Cinv_rowIndex]
            resolveLHSSum += 1 / 2 * self.QSecondQuant(LHSComponent) * resolveRHSSum
        H = resolveLHSSum
        endTime = time.time()
        print("Finished assembling H", (endTime - startTime) / 60)
        print("Initial matrix dimension:", H.shape[0])

        print("Start adding inductance")
        startTime = time.time()
        # Add inductance terms
        for component in self.HComponentOrder:
            print(component.name)
            if issubclass(type(component), Qubit):
                x = ((2 * np.pi * np.sqrt(hbarConst) / Phi_0Const) * self.PhiSecondQuant(component))
                for i in range(int(self.simParams["TrigOrder"] / 2) + 1):
                    cosTerm = (-1) ** i * x ** (2 * i) / np.math.factorial(2 * i)
                    H -= (component.EJ / hbarConst) * cosTerm
                    print("cos x^" + str(2 * i) + " term Frobenius norm: ", cosTerm.norm(norm="fro"))
            elif isinstance(component, ReadoutResonator):
                lumpedRSim = LumpedR(component.index)(self.qArch)
                term = self.PhiSecondQuant(component) ** 2 / (2 * lumpedRSim.equivL)
                H += term
        endTime = time.time()
        print("Finished adding inductance", (endTime - startTime) / 60)

        # Truncate H based on maxNumPhotons
        print("Truncating H")
        startTime = time.time()
        numAllStates = H.shape[0]
        # Compile a list of all the states in H
        allStatesList = [0] * numAllStates
        base = self.maxDim
        for i in range(numAllStates):
            stateList = baseRepresentation(i, base, self.numComponents)
            H_index = state_number_index(H.dims[0], stateList)
            allStatesList[
                H_index] = stateList  # The order of allStatesList now corresponds to the order of rows/columns in H.
        # Compile a list of all the states to keep based on the maxNumPhotons parameters.
        keepStatesList = []
        qubitIndices = [i for i in range(self.numComponents) if issubclass(type(self.HComponentOrder[i]), Qubit)]
        readoutResonatorIndices = [i for i in range(self.numComponents) if
                                   isinstance(self.HComponentOrder[i], ReadoutResonator)]
        for stateList in allStatesList:
            qubitExcitations = [stateList[i] for i in range(self.numComponents) if i in qubitIndices]
            readoutResonatorExcitations = [stateList[i]
                                           for i in range(self.numComponents) if i in readoutResonatorIndices]
            if all(i <= numQubitPhotons for i in qubitExcitations) and all(
                    i <= numResonatorPhotons for i in readoutResonatorExcitations):
                keepStatesList.append(stateList)
        # Reduce H to only the states in keepStatesList
        indicesToKeep = [state_number_index(H.dims[0], stateList) for stateList in keepStatesList]
        """This next step is crucial. 
        Because the indices are sorted, state_number_index will still work after extract_states is called."""
        indicesToKeep.sort()
        H = H.extract_states(indicesToKeep)
        # Update the dimension of H to reflect the truncation.
        newHDim = []
        for component in self.HComponentOrder:
            if issubclass(type(component), Qubit):
                newHDim.append(numQubitPhotons + 1)
            elif isinstance(component, ReadoutResonator):
                newHDim.append(numResonatorPhotons + 1)
        H.dims = [newHDim, newHDim]
        stateListHIndices = {str(stateList): state_number_index(H.dims[0], stateList) for stateList in keepStatesList}
        H = H * omegaToGHz
        endTime = time.time()
        print("Finished truncating H", (endTime - startTime) / 60)

        # Extract the bare hamiltonian for each component.
        print("Extracting subspaces")
        startTime = time.time()
        """Each element is a list of the eigenstates in fock ordering for a particular component."""
        subspaceEigenstates = []
        for component in self.HComponentOrder:
            fockStates = [[n if i == self.quantizeIndex(component) else 0 for i in range(self.numComponents)] for n in
                          range(newHDim[self.quantizeIndex(component)])]
            subspaceStateIndices = [stateListHIndices[str(i)] for i in fockStates]
            componentH = H.extract_states(subspaceStateIndices)
            subspaceEigenstates.append(componentH.eigenstates()[1])
        endTime = time.time()
        print("Finished calculating subspaces", (endTime - startTime) / 60)

        # Assemble output states in order of manifold.
        outputStatesList = []
        for photonManifold in [0, 1, 2]:
            base = photonManifold + 1
            allNumsBase = [baseRepresentation(i, base, self.numComponents)
                           for i in range(1, base ** (self.numComponents - 1) * photonManifold + 1)]
            manifoldNums = [i for i in allNumsBase if sum(i) == photonManifold]  # Remove numbers outside the manifold
            manifoldNums.reverse()
            outputStatesList = outputStatesList + manifoldNums
        zeroStateList = [0] * self.numComponents
        outputStatesList = [zeroStateList] + outputStatesList

        H_output_headers = [H_Header(i) for i in outputStatesList]

        print("Starting matrix element")
        startTime = time.time()
        numOutputStates = len(outputStatesList)
        H_output = np.zeros((numOutputStates, numOutputStates), dtype=complex)
        for i in range(numOutputStates):
            for j in range(numOutputStates):
                H_output[i, j] = H.matrix_element(bra(outputStatesList[i], newHDim), ket(outputStatesList[j], newHDim))
        endTime = time.time()
        print("Finished matrix element", (endTime - startTime) / 60)

        print("Final matrix dimension:", H.dims)

        # Eigenvalues
        print("Calculating eigenvalues")
        startTime = time.time()
        eigsComplex = H.eigenenergies()
        eigsReal = [np.real(i) for i in eigsComplex]
        eigsReal.sort()
        eigsRealNorm = [i - eigsReal[0] for i in eigsReal]  # Normalize to the ground state being zero energy.
        endTime = time.time()
        print("Finished calculating eigenvalues", (endTime - startTime) / 60)

        # Output
        print("Starting output")

        resultsDict = {"Index Order": [i.name for i in self.HComponentOrder], "Headers": H_output_headers,
                       "H_output (GHz)": H_output.astype(str).tolist(), "Evals (GHz)": eigsRealNorm}
        jsonWrite(self.resultsFilePath, resultsDict)

        quantizeEndTime = time.time()
        print("Total time:", (quantizeEndTime - quantizeStartTime) / 60)

    @staticmethod
    def readQuantizeList(quantizeList):
        return [str(i) for i in quantizeList[1:-1].split(":")]

    @property
    def HComponentOrder(self):
        quantizeComponentListNames = self.readQuantizeList(self.simParams["QuantizeList"])
        quantizeComponentList = [self.qArch.componentFromName(i) for i in quantizeComponentListNames]
        return quantizeComponentList

    def quantizeIndex(self, component):
        return [self.HComponentOrder.index(i) for i in self.HComponentOrder if i.name == component.name][0]

    @property
    def HStateOrder(self):
        HStateOrder = [stateFromHeader(i) for i in self.Headers]
        return HStateOrder

    @property
    def H(self):
        return np.array(jsonRead(self.resultsFilePath)["H_output (GHz)"]).astype(complex)

    @property
    def HEvals(self):
        return jsonRead(self.resultsFilePath)["Evals (GHz)"]

    @property
    def Headers(self):
        return jsonRead(self.resultsFilePath)["Headers"]

    def HEval(self, stateList):
        """Find the eigenvalue corresponding to the undressed energy.
        Only valid if the dressed states are close to the undressed states!"""
        diagonalComp = []

        HStateOrder = self.HStateOrder
        H = self.H
        for index, state in enumerate(HStateOrder):
            diagonalComp.append([state, H[index, index]])  # Pairs each state up with its diagonal element.
        diagonalCompSorted = sorted(diagonalComp, key=lambda l: l[1])  # Diagonal elements in ascending order.

        stateIndex = diagonalCompSorted.index([i for i in diagonalCompSorted if i[0] == stateList][0])

        return self.HEvals[stateIndex]

    def stateList(self, excitationList):
        """Excitation list is of the form [[i,n],[j,m],...]
        where i,j are component indices, and m,n are the excitations."""
        numComponents = len(self.HComponentOrder)
        s = [0] * numComponents
        for i in excitationList:
            s[i[0]] = i[1]
        return s


def LumpedR(index):
    class LumpedRSimulation(Simulation):
        def __init__(self, qArch):
            super(LumpedRSimulation, self).__init__(qArch, "lumpedR" + str(index))
            self.index = index
            self.Y11RSimName = "Y11R" + str(self.index)
            self.YRestRSimName = "YRestR" + str(self.index)
            CapMatObj = CapMat(self.qArch)
            self.circuitSims = {
                self.Y11RSimName: Y11RSimulation(self.index, self.Y11RSimName, self.directoryPath, qArch, CapMatObj),
                self.YRestRSimName: YRestRSimulation(self.index, self.YRestRSimName,
                                                     self.directoryPath, qArch, CapMatObj)}

        def initialize(self):
            simParamsDict = S21_params
            self.generateParams(simParamsDict)

        def run(self):
            self.runAllSims()

        def postProcess(self):
            self.deleteUnneededFiles()
            equivL_val, equivC_val = self.calculateLumpedResonator()
            resultsDict = {"equivL(H):": equivL_val, "equivC(F):": equivC_val}
            jsonWrite(self.resultsFilePath, resultsDict)
            print("equivL(H):" + str(equivL_val))
            print("equivC(F):" + str(equivC_val))

        def calculateLumpedResonator(self):  # Calculates from lumpedR files
            # Load Y11,YRest data
            Y11Freq, Y11_Y11, Y11InterpFunc = readY11Data(self.circuitSims[self.Y11RSimName].resultsFilePath)
            YRestFreq, YRest_Y11, YRestInterpFunc = readY11Data(self.circuitSims[self.YRestRSimName].resultsFilePath)
            derivativeResolution = np.abs(Y11Freq[1] - Y11Freq[0])
            dressedFreq = calculateDressedFrequency(Y11Freq, Y11InterpFunc)
            # See Junling's thesis equations 4.19
            equivC = 1 / 2 * (np.imag(derivative(Y11InterpFunc, dressedFreq, derivativeResolution))
                              - np.imag(derivative(YRestInterpFunc, dressedFreq, derivativeResolution))
                              - np.imag(YRestInterpFunc(dressedFreq)) / dressedFreq)
            equivL = 2 / (dressedFreq ** 2 * (np.imag(derivative(Y11InterpFunc, dressedFreq, derivativeResolution))
                                              - np.imag(derivative(YRestInterpFunc, dressedFreq, derivativeResolution)))
                          + dressedFreq * np.imag(YRestInterpFunc(dressedFreq)))
            return equivL, equivC

        @property
        def equivC(self):
            return self.resultsDict["equivC(F):"]

        @property
        def equivL(self):
            return self.resultsDict["equivL(H):"]
    return LumpedRSimulation


def DecayQ(index):
    class DecayQSimulation(Simulation):
        def __init__(self, qArch):
            super(DecayQSimulation, self).__init__(qArch, "DecayQ" + str(index))
            self.index = index
            self.Y11QSimName = "Y11Q" + str(self.index)
            CapMatObj = CapMat(self.qArch)
            self.circuitSims = {
                self.Y11QSimName: Y11QSimulation(self.index, self.Y11QSimName, self.directoryPath, qArch, CapMatObj)}

        def initialize(self):
            simParamsDict = S21_params
            self.generateParams(simParamsDict)

        def run(self):
            self.runAllSims()

        def postProcess(self):
            self.deleteUnneededFiles()
            freq, Y11, Y11InterpFunc = readY11Data(self.circuitSims[self.Y11QSimName].resultsFilePath)
            dressedFreq = calculateDressedFrequency(freq, Y11InterpFunc)
            print(dressedFreq*omegaToGHz)
            derivativeResolution = np.abs(freq[1] - freq[0])
            T1 = np.imag(derivative(Y11InterpFunc, dressedFreq, derivativeResolution)) / \
                 (2 * np.real(Y11InterpFunc(dressedFreq)))
            print("T1(us):", T1*1e6)
            jsonWrite(self.resultsFilePath, {"T1 (s):": T1})

        @property
        def T1(self):
            return self.resultsDict["T1 (s):"]

    return DecayQSimulation


def ECQ(index):
    class ECQSimulation(Simulation):
        def __init__(self, qArch):
            super(ECQSimulation, self).__init__(qArch, "ECQ" + str(index))
            self.index = index

        def initialize(self):
            self.createDirectory()

        def postProcess(self):
            self.deleteUnneededFiles()

            CapMatGESim = CapMatGE(self.qArch)
            postGEComponentList = CapMatGESim.postGEComponentList

            qubitObj = self.qArch.allQubitsDict[self.index]
            qubitColumnIndex = postGEComponentList.index(qubitObj)
            cInv = np.linalg.inv(CapMatGESim.capMatGE)
            cSum = 1 / cInv[qubitColumnIndex, qubitColumnIndex]

            E_C = eConst ** 2 / (2 * cSum)  # In Joules
            EJ = self.qArch.allQubitsDict[self.index].EJ
            print(qubitObj.name + "EC (GHz): " + str(E_C * Joules_To_GHz))
            print(qubitObj.name + "EJ (GHz): " + str(EJ * Joules_To_GHz))
            print(qubitObj.name + "EJ/EC: " + str(EJ / E_C))

            resultsDict = {"EC": E_C, "EJ/EC": EJ / E_C}

            jsonWrite(self.resultsFilePath, resultsDict)

        @property
        def EC(self):
            return self.resultsDict["EC"]
    return ECQSimulation


def ECR(index):
    class ECRSimulation(Simulation):
        def __init__(self, qArch):
            super(ECRSimulation, self).__init__(qArch, "ECR" + str(index))
            self.index = index

        def initialize(self):
            self.createDirectory()

        def postProcess(self):
            CapMatGESim = CapMatGE(self.qArch)
            postGEComponentList = CapMatGESim.postGEComponentList
            readoutResonatorObj = self.qArch.allReadoutResonatorsDict[self.index]
            resonatorColumnIndex = postGEComponentList.index(readoutResonatorObj)
            cInv = np.linalg.inv(CapMatGESim.capMatGE)
            cSum = 1 / cInv[resonatorColumnIndex, resonatorColumnIndex]

            E_C = eConst ** 2 / (2 * cSum)  # In Joules

            resultsDict = {"EC": E_C}
            jsonWrite(self.resultsFilePath, resultsDict)

        @property
        def EC(self):
            return self.resultsDict["EC"]
    return ECRSimulation


