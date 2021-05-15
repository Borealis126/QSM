import numpy as np
import os
import time
from csvFunctions import jsonRead, jsonWrite, csvRead, arrayNoBlanks, readY11Data
from ansysFunctions import *
import subprocess
from q3dSimulations import Q3DExtractor
from circuitSimulations import *
from sympy import symbols
from constants import *
from analysisFunctions import *
from quantumStateFunctions import stateFromHeader, baseRepresentation, H_Header
from scipy.misc import derivative
from sympy import zeros, Matrix, zeros, sin
from qSysObjects import GroundedQubit, FloatingQubit, ReadoutResonator
from qutip import state_number_index, qzero, ket, bra

class Simulation:
    def __init__(self, qSys, simName):
        qSys.loadDesignFiles()  # Every time a Simulation instance is made, the design files are loaded.
        self.qSys = qSys
        self.simName = simName
        self.q3dSims = dict()
        self.hfssSims = dict()
        self.circuitSims = dict()

        self.directoryPath = self.qSys.sysParams["Project Folder"] / self.simName

        self.paramsPath = self.directoryPath / "SimulationParameters.json"
        self.resultsFilePath = self.directoryPath / "Results.json"

    @property
    def simParams(self):
        return jsonRead(self.paramsPath)

    def runAnsysSimulator(self, aedtFile, simulatorFile, maxRunTime):
        simulateCommand = ""
        if self.qSys.sysParams["Compute Location"] == "Windows":
            ansysExecutableFile = "\"%ProgramFiles%/AnsysEM/AnsysEM19.5/Win64/ansysedt.exe\""
            simulateCommand = (str(ansysExecutableFile) + ' -features=beta -ng -runscriptandexit '
                               + str(simulatorFile) + ' ' + str(aedtFile))
        elif self.qSys.sysParams["Compute Location"] == "Cluster":
            simulateCommand = (str(self.qSys.sysParams["QSM Source Folder"] / "helperFiles" / "ansysBatch") + " ansys "
                               + str(simulatorFile) + " " + str(aedtFile) + " "
                               + str(self.directoryPath) + " " + str(maxRunTime))
        subprocess.call(simulateCommand, shell=True)

    def createDirectory(self):
        # Create the directory if it doesn't yet exist.
        if self.qSys.sysParams["Compute Location"] == "Windows":
            bashCommand = "if not exist " + str(self.directoryPath) + " mkdir " + str(
                self.directory)
            subprocess.call(bashCommand, shell=True)
        elif self.qSys.sysParams["Compute Location"] == "Cluster":
            subprocess.call("rm -rf " + str(self.directoryPath), shell=True)
            bashCommand = "mkdir -p " + str(self.directoryPath)
            subprocess.call(bashCommand, shell=True)

    def generateParams(self, simParamsDict):
        self.createDirectory()
        jsonWrite(self.paramsPath, simParamsDict)

    def runAllSims(self):  # Specifically reserved for Ansys simulations.
        # Delete previous run files
        if self.qSys.sysParams["Compute Location"] == "Cluster":
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
        if self.qSys.sysParams["Compute Location"] == "Cluster":
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
            self.qSys.deleteFolder(str(q3dSim.aedtFolderPath))
        for circuitSimName, circuitSim in self.circuitSims.items():
            resultsFolder = str(circuitSim.aedtFolderPath)
            if os.path.exists(resultsFolder):
                self.qSys.deleteFolder(resultsFolder)

    def copyAnsysFile(self, ansysPath):
        if os.path.exists(str(ansysPath)):
            self.qSys.deleteFile(str(ansysPath))
        copyAEDTTemplateCommand = ""
        if self.qSys.sysParams["Compute Location"] == "Windows":
            copyAEDTTemplateCommand = (
                    "copy "
                    + str(self.qSys.sysParams["QSM Source Folder"] / "helperFiles" / "template.aedt")
                    + " " + str(ansysPath)
            )
        if self.qSys.sysParams["Compute Location"] == "Cluster":
            copyAEDTTemplateCommand = (
                    "cp " + str(self.qSys.sysParams["QSM Source Folder"] / "helperFiles" / "template.aedt")
                    + " " + str(ansysPath)
            )
        subprocess.call(copyAEDTTemplateCommand, shell=True)

    @property
    def resultsDict(self):
        return jsonRead(self.resultsFilePath)


class CapMatSimulation(Simulation):
    def __init__(self, qSys):
        super().__init__(qSys, "capMat")
        q3dSimName = "capMatExtractor"
        self.q3dSims = {q3dSimName: Q3DExtractor(q3dSimName, self.directoryPath)}
    def initialize(self):
        simParamsDict = {"PerRefine": "100", "MaxPass": "99"}
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

    def getChipNNodes_CapMat(self, N):
        allNodes = []
        for qubitIndex, qubit in self.qSys.chipDict[N].qubitDict.items():
            allNodes += [pad.node for pad in qubit.padListGeom]
        for readoutResonatorIndex, readoutResonator in self.qSys.chipDict[N].readoutResonatorDict.items():
            allNodes += [readoutResonator.pad1.node, readoutResonator.pad2.node]
        for controlLineIndex, controlLine in self.qSys.chipDict[N].controlLineDict.items():
            if controlLine.lineType == "feedline" and self.qSys.sysParams["Simulate Feedline?"] == "Yes":
                allNodes.append(controlLine.lineNode)
                for launchPadName, launchPad in controlLine.launchPadNodeDict.items():
                    allNodes.append(launchPad)
        return allNodes

    def capMatLayout_Lines(self):
        lines = ["oEditor = oDesign.SetActiveEditor(\"3D Modeler\")\n",
                 "oModuleBoundary = oDesign.GetModule(\"BoundarySetup\")\n"]
        for chipIndex, chip in self.qSys.chipDict.items():
            # Draw substrate
            lines += ansysPolyline_Lines(
                name=chip.substrate.name,
                color=chip.substrate.node.color,
                material=chip.substrate.node.material,
                polyline3D=[[point[0], point[1], chip.substrate.node.Z]
                            for point in chip.substrate.node.polyline]
            )
            lines += ansysSweepAlongVector_Lines(chip.substrate.node)
            # Draw ground(s)
            lines += ansysPolyline_Lines(
                name=chip.ground.outlineNode.name,
                color=chip.ground.outlineNode.color,
                material=chip.ground.outlineNode.material,
                polyline3D=[[point[0], point[1], chip.ground.outlineNode.Z]
                            for point in chip.ground.outlineNode.polyline]
            )
            # Draw qubits,resonators,controlLines,launchpads

            for thisNode in self.getChipNNodes_CapMat(chip.index):
                lines += ansysPolyline_Lines(
                    name=thisNode.name,
                    color=thisNode.color,
                    material=thisNode.material,
                    polyline3D=[[point[0], point[1], thisNode.Z] for point in
                                thisNode.polyline]
                )
                lines += ansysQ3DMake3D(self.qSys.sysParams["Simulation"], thisNode)
                # Trench round 1
                addTrenchNodeLines, subtractTrenchPeripheryLines, makeTrenchComponent3DLines = ansysTrench(
                    componentNode=thisNode, trench=self.qSys.CPW.geometryParams["Trench"], chip=chip)
                lines += addTrenchNodeLines + subtractTrenchPeripheryLines  # Trench

                lines += ansysSignalLine_Lines(thisNode)
                """Subtract the periphery from the ground. 
                Still subtract the launchpad peripheries so the control lines aren't shorted to ground."""
                for index, peripheryPolyline in enumerate(thisNode.peripheryPolylines):
                    peripheryName = thisNode.name + "periphery" + str(index)
                    lines += ansysPolyline_Lines(
                        name=peripheryName,
                        color=thisNode.color,
                        material=thisNode.material,
                        polyline3D=[[point[0], point[1], thisNode.Z]
                                    for point in peripheryPolyline]
                    )  # First make the boundary
                    """Then subtract it from ground"""
                    lines += ansysSubtract_Lines(chip.ground.outlineNode.name, peripheryName)
            for thisNode in self.getChipNNodes_CapMat(chip.index):  # Trench round 2.
                addTrenchNodeLines, subtractTrenchPeripheryLines, makeTrenchComponent3DLines = ansysTrench(
                    componentNode=thisNode, trench=self.qSys.CPW.geometryParams["Trench"], chip=chip)
                lines += makeTrenchComponent3DLines
            # For grounded qubits unite pad 2 with ground.
            for qubitIndex, qubit in self.qSys.allQubitsDict.items():
                if isinstance(qubit, qSysObjects.GroundedQubit):
                    lines += ansysUniteNodes([chip.ground.outlineNode, qubit.pad2.node])
            # For control lines unite trace and launchpads, also unite flux bias if applicable.
            for controlLineIndex, controlLine in self.qSys.chipDict[chip.index].controlLineDict.items():
                if (controlLine.lineType == "feedline"
                        and self.qSys.sysParams["Simulate Feedline?"] == "Yes"):
                    uniteNodeList = [controlLine.lineNode]
                    for launchPadName, launchPadNode in controlLine.launchPadNodeDict.items():
                        uniteNodeList.append(launchPadNode)
                    lines += ansysUniteNodes(uniteNodeList)
                    if controlLine.lineType == "fluxBias":
                        lines += ansysUniteNodes([self.chipDict[0].ground.outlineNode, controlLine.lineNode])
            # Make the ground 3D
            lines += ansysQ3DMake3D(self.qSys.sysParams["Simulation"], chip.ground.outlineNode)
        # Draw bumps if flip chip, and join the ground nodes via the bumps
        if self.qSys.sysParams["Flip Chip?"] == "Yes":
            uniteNodeList = [self.qSys.chipDict[0].ground.outlineNode, self.qSys.chipDict[1].ground.outlineNode]
            for thisBump in self.bumpsDict["Bumps"]:
                for thisNode in [
                    thisBump.underBumpBottomNode,
                    thisBump.bumpMetalBottomNode,
                    thisBump.bumpMetalTopNode,
                    thisBump.underBumpTopNode
                ]:
                    lines += ansysPolyline_Lines(
                        name=thisNode.name,
                        color=thisNode.color,
                        material=thisNode.material,
                        polyline3D=[[point[0], point[1], thisNode.Z] for point in
                                    thisNode.polyline]
                    )
                    lines += ansysSweepAlongVector_Lines(thisNode)
                    uniteNodeList.append(thisNode)
            lines += ansysUniteNodes(uniteNodeList)  # Resulting single node is ground1
        # Assign ground signal line (independent of flip chip)
        lines += ansysGroundSignalLine_Lines(self.qSys.chipDict[0].ground)

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
        capMat = jsonRead(self.resultsFilePath)["capMat (F)"]
        """If the feedline is not simulated, add in the capacitance to the resonators."""
        if self.qSys.sysParams["Simulate Feedline?"] == "No" and self.qSys.allControlLinesDict != {}:
            newCapMat = [i+[0] for i in capMat.copy()]  # Add a dimension for the feedline, the highest index.
            newCapMat.append([0]*(len(capMat)+1))

            feedlineIndex = numNodes
            self.ansysCapMatHeaders.append(self.qSys.allControlLinesDict[0].lineNode.name)

            # Add resonator capacitances
            for readoutResonatorIndex, readoutResonator in self.qSys.allReadoutResonatorsDict.items():
                componentParams = readoutResonator.componentParams
                pad1Index = self.ansysCapMatHeaders.index(readoutResonator.pad1.node.name)
                # Capacitance to the feedline
                newCapMat[pad1Index][feedlineIndex] = -componentParams["Capacitance to Feedline (F)"]
                newCapMat[feedlineIndex][pad1Index] = -componentParams["Capacitance to Feedline (F)"]
                # Fix capacitance to ground
                wrongCapToGround = sum(capMat[pad1Index])
                correctCapToGround = componentParams["Feedline Pad Capacitance to Ground (F)"]
                newCapMat[pad1Index][pad1Index] = capMat[pad1Index][pad1Index] - wrongCapToGround + correctCapToGround
            capMat = newCapMat
        return capMat


class LumpedRSimulation(Simulation):
    def __init__(self, qSys, readoutResonatorIndex):
        super(LumpedRSimulation, self).__init__(qSys, "lumpedR" + str(readoutResonatorIndex))
        self.index = readoutResonatorIndex
        self.Y11RSimName = "Y11R" + str(readoutResonatorIndex)
        self.YRestRSimName = "YRestR" + str(readoutResonatorIndex)
        self.circuitSims = {
            self.Y11RSimName: Y11RSimulation(self.Y11RSimName, self.directoryPath, qSys, readoutResonatorIndex),
            self.YRestRSimName: YRestRSimulation(self.YRestRSimName, self.directoryPath, qSys,
                                                 readoutResonatorIndex)}

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
        print("equivL(H):" + str(self.equivL))
        print("equivC(F):" + str(self.equivC))

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


class CapMatGESimulation(Simulation):
    def __init__(self, qSys):
        super().__init__(qSys, "capMatGE")
        # Components ordering
        nonGECapMatIndex = 0
        self.preGECapMatHeaders = []
        self.postGEComponentList = []
        for qubitIndex, qubit in self.qSys.allQubitsDict.items():
            qubit.pad1.quantCapMatIndex = nonGECapMatIndex
            self.preGECapMatHeaders.append(qubit.pad1.name)
            nonGECapMatIndex += 1
            if isinstance(qubit, FloatingQubit):
                qubit.pad2.quantCapMatIndex = nonGECapMatIndex
                nonGECapMatIndex += 1
                self.preGECapMatHeaders.append(qubit.pad2.name)
            self.postGEComponentList.append(qubit)
        for readoutResonatorIndex, readoutResonator in self.qSys.allReadoutResonatorsDict.items():
            readoutResonator.pad2.quantCapMatIndex = nonGECapMatIndex  # Only pad2 is included in quantization
            self.preGECapMatHeaders.append(readoutResonator.pad2.node.name)
            self.postGEComponentList.append(readoutResonator)
            nonGECapMatIndex += 1

    def postProcess(self):
        self.deleteUnneededFiles()
        header = [component.name for component in self.postGEComponentList]

        capMat_GE, phiMat, RHS = self.gaussianElimination()
        resultsDict = {"Header": header, "capMat (F)": capMat_GE.tolist()}
        jsonWrite(self.resultsFilePath, resultsDict)

    @property
    def capMatForGE(self):
        dimPreGEQuant = len(self.preGECapMatHeaders)
        capMat_preGE = zeros(dimPreGEQuant, dimPreGEQuant)
        capMatReduced = Matrix(CapMatSimulation(self.qSys).capMat)
        ansysCapMatHeaders = CapMatSimulation(self.qSys).ansysCapMatHeaders

        # Alter the resonator pad 2 capacitance to ground according to the lumped resonator model.
        for readoutResonatorIndex, readoutResonator in self.qSys.allReadoutResonatorsDict.items():
            lumpedRSim = LumpedRSimulation(self.qSys, readoutResonatorIndex)
            index = ansysCapMatHeaders.index(readoutResonator.pad2.node.name)
            capMatReduced[index, index] = capMatReduced[index, index] - sum(
                capMatReduced.row(index)) + lumpedRSim.equivC
        """Remove all control lines and resonator pad1 from the capacitance matrix. This is under the assumption that
        the resonator pad1 only has a non-negligible capacitance to the feedline, 
        thereby not affecting the system Hamiltonian."""
        indicesToRemove = []
        for nodeName in ansysCapMatHeaders:
            if nodeName in [controlLine.lineNode.name for controlLine in self.qSys.allControlLinesDict.values()]:
                index = ansysCapMatHeaders.index(nodeName)
                indicesToRemove.append(index)
        for readoutResonatorIndex, readoutResonator in self.qSys.allReadoutResonatorsDict.items():
            index = ansysCapMatHeaders.index(readoutResonator.pad1.node.name)
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
            if isinstance(component, FloatingQubit):
                RHS[component.pad1.quantCapMatIndex, 0] = I_c * sin((component.pad1.phiSym - component.pad2.phiSym)
                                                                    / Phi_0Const)
                RHS[component.pad2.quantCapMatIndex, 0] = -RHS[component.pad1.quantCapMatIndex, 0]
                phiMat[component.pad1.quantCapMatIndex, 0] = component.pad1.phiSym.diff(t, 2)
                phiMat[component.pad2.quantCapMatIndex, 0] = component.pad2.phiSym.diff(t, 2)
            elif isinstance(component, GroundedQubit):
                RHS[component.pad1.quantCapMatIndex, 0] = I_c * sin(component.pad1.phiSym / Phi_0Const)
                phiMat[component.pad1.quantCapMatIndex, 0] = component.pad1.phiSym.diff(t, 2)
            elif isinstance(component, ReadoutResonator):
                RHS[component.pad2.quantCapMatIndex, 0] = component.pad2.phiSym / Phi_0Const
                phiMat[component.pad2.quantCapMatIndex, 0] = component.pad2.phiSym.diff(t, 2)
        capMat_GE = self.capMatForGE
        # Perform the gaussian elimination on just the qubits.
        for componentIndex, component in enumerate(self.postGEComponentList):
            if isinstance(component, FloatingQubit):
                component.padToEliminate = component.pad1
                component.padToKeep = component.pad2
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
            if isinstance(component, FloatingQubit):
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
        headerLineIndex = 1
        numNodes = len(self.postGEComponentList)
        capMatGE = np.zeros((numNodes, numNodes))
        capMatGEStartLineIndex = headerLineIndex + 1
        for index1 in range(numNodes):
            for index2 in range(numNodes):
                matRow = capMatGEStartLineIndex + index1
                matCol = 1 + index2
                capacitanceValue = float(self.resultsFileLines[matRow][matCol])
                capMatGE[index1, index2] = capacitanceValue
        return capMatGE


class Quantize(Simulation):
    def __init__(self, qSys):
        super().__init__(qSys, "quantize")
        self.HStateOrder_calculated = None

    def initialize(self):
        quantizeList = "["
        for component in CapMatGESimulation(self.qSys).postGEComponentList:
            quantizeList += component.name + ":"
        quantizeList = quantizeList[0:-1] + "]"
        self.simParamsLines = [
            ["QuantizeList", quantizeList],
            ["NumResonatorPhotons", "5"],
            ["NumQubitPhotons", "5"],
            ["TrigOrder", "10"]
        ]

        super(Quantize, self).initialize()

    def postProcess(self):
        super(Quantize, self).postProcess()
        self.quantizeSimulation()

    def quantizeSimulation(self):
        print("started quantize")
        quantizeStartTime = time.time()

        HComponentOrder = self.HComponentOrder  # So it's not reading from the CSV every time.
        CapMatGESim = CapMatGESimulation(self.qSys)
        capMatGE = CapMatGESim.capMatGE
        postGEComponentList = CapMatGESim.postGEComponentList

        numQubitPhotons = self.simParamsDict["NumQubitPhotons"]
        numResonatorPhotons = self.simParamsDict["NumResonatorPhotons"]
        numPhotons = max(numQubitPhotons, numResonatorPhotons)

        # self.capMatGE needs to be reduced based on the requested components to quantize.

        numComponents = len(HComponentOrder)
        capMatGEIndicesToKeep = [[i.name for i in postGEComponentList].index(i)
                                 for i in [j.name for j in HComponentOrder]]

        rows = np.array(capMatGEIndicesToKeep, dtype=np.intp)
        columns = np.array(capMatGEIndicesToKeep, dtype=np.intp)
        capMatGE_quant = capMatGE[rows[:, np.newaxis], columns]

        dim = numPhotons + 2
        qObjDim = [dim] * numComponents
        Cinv = np.linalg.inv(capMatGE_quant)

        # Assemble the Hamiltonian. H is in units of radians (H/hbar). Calculates 1/2*Q.T*Cinv*Q.
        print("Start assembling H")
        startTime = time.time()
        resolveLHSSum = qzero(qObjDim)
        for Cinv_rowIndex, Cinv_row in enumerate(Cinv):
            resolveRHSSum = qzero(qObjDim)
            for componentIndex, component in enumerate(HComponentOrder):
                resolveRHSSum += Cinv_row[componentIndex] * component.QsecondQuant(dim, numComponents)
            LHSComponent = HComponentOrder[Cinv_rowIndex]
            resolveLHSSum += 1 / 2 * LHSComponent.QsecondQuant(dim, numComponents) * resolveRHSSum
        H = resolveLHSSum
        endTime = time.time()
        print("Finished assembling H", (endTime - startTime) / 60)
        print("Initial matrix dimension:", H.shape[0])

        print("Start adding inductance")
        startTime = time.time()
        # Add inductance terms
        for component in HComponentOrder:
            print(component.name)
            if issubclass(type(component), qSysObjects.Qubit) or isinstance(component, qSysObjects.StraightBusCoupler):
                x = ((2 * np.pi * np.sqrt(hbarConst) / Phi_0Const) * component.PhisecondQuant(dim, numComponents))
                for i in range(int(self.simParamsDict["TrigOrder"] / 2) + 1):
                    cosTerm = (-1) ** i * x ** (2 * i) / np.math.factorial(2 * i)
                    H -= (component.EJ / hbarConst) * cosTerm
                    print("cos x^" + str(2 * i) + " term Frobenius norm: ", cosTerm.norm(norm="fro"))
            elif isinstance(component, qSysObjects.ReadoutResonator):
                lumpedRSim=LumpedRSimulation(self.qSys,component.index)
                term = component.PhisecondQuant(dim, numComponents) ** 2 / (2 * component.equivL(lumpedRSim))
                H += term
        endTime = time.time()
        print("Finished adding inductance", (endTime - startTime) / 60)

        # Truncate H based on numPhotons
        print("Truncating H")
        startTime = time.time()
        numAllStates = H.shape[0]
        # Compile a list of all the states in H
        allStatesList = [0] * numAllStates
        base = dim
        for i in range(numAllStates):
            stateList = baseRepresentation(i, base, numComponents)
            H_index = state_number_index(H.dims[0], stateList)
            allStatesList[
                H_index] = stateList  # The order of allStatesList now corresponds to the order of rows/columns in H.
        # Compile a list of all the states to keep based on the numPhotons parameters.
        keepStatesList = []
        qubitIndices = [i for i in range(numComponents) if issubclass(type(HComponentOrder[i]), qSysObjects.Qubit)]
        readoutResonatorIndices = [i for i in range(numComponents) if
                                   isinstance(HComponentOrder[i], qSysObjects.ReadoutResonator)]
        for stateList in allStatesList:
            qubitExcitations = [stateList[i] for i in range(numComponents) if i in qubitIndices]
            readoutResonatorExcitations = [stateList[i] for i in range(numComponents) if i in readoutResonatorIndices]
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
        for component in HComponentOrder:
            if issubclass(type(component), qSysObjects.Qubit):
                newHDim.append(numQubitPhotons + 1)
            elif isinstance(component, qSysObjects.ReadoutResonator):
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
        for component in HComponentOrder:
            fockStates = [[n if i == self.quantizeIndex(component.name) else 0 for i in range(numComponents)] for n in
                          range(newHDim[self.quantizeIndex(component.name)])]
            subspaceStateIndices = [stateListHIndices[str(i)] for i in fockStates]
            componentH = H.extract_states(subspaceStateIndices)
            subspaceEigenstates.append(componentH.eigenstates()[1])
        endTime = time.time()
        print("Finished calculating subspaces", (endTime - startTime) / 60)

        # Assemble output states in order of manifold.
        outputStatesList = []
        for photonManifold in [0, 1, 2]:
            base = photonManifold + 1
            allNumsBase = [baseRepresentation(i, base, numComponents)
                           for i in range(1, base ** (numComponents - 1) * photonManifold + 1)]
            manifoldNums = [i for i in allNumsBase if sum(i) == photonManifold]  # Remove numbers outside the manifold
            manifoldNums.reverse()
            outputStatesList = outputStatesList + manifoldNums
        zeroStateList = [0] * numComponents
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
        lines = [
            ["Index Order"],
            [i.name for i in HComponentOrder],
            [""],
            ["H (GHz)"],
            [""] + H_output_headers
        ]
        for index, H_output_line in enumerate(H_output):
            matRow = [H_output_headers[index]] + [np.real(j) for j in list(H_output_line)]
            lines.append(matRow)
        lines.append([""])
        lines.append(["H_evals"])
        lines.append(eigsRealNorm)
        lines.append([""])
        csvWrite(self.resultsFilePath, lines)
        quantizeEndTime = time.time()
        print("Total time:", (quantizeEndTime - quantizeStartTime) / 60)

    def readQuantizeList(quantizeList):
        return [str(i) for i in quantizeList[1:-1].split(":")]

    @property
    def HIndexLineIndex(self):
        return self.resultsFileLines.index([i for i in self.resultsFileLines if i[0] == "Index Order"][0]) + 1

    @property
    def HComponentOrder(self):
        quantizeComponentListNames = self.readQuantizeList(self.simParamsDict["QuantizeList"])
        quantizeComponentList = [self.qSys.componentFromName(i) for i in quantizeComponentListNames]
        return quantizeComponentList

    @property
    def headerLineIndex(self):
        return self.resultsFileLines.index([i for i in self.resultsFileLines if i[0] == "H (GHz)"][0]) + 1

    def quantizeIndex(self, componentName):
        return [self.HComponentOrder.index(i) for i in self.HComponentOrder if i.name == componentName][0]

    @property
    def HStateOrder(self):
        resultsFileLines = self.resultsFileLines
        HStateOrder = [stateFromHeader(i) for i in arrayNoBlanks(resultsFileLines[self.headerLineIndex][1:])]
        return HStateOrder

    @property
    def H(self):
        HStartLineIndex = self.headerLineIndex + 1

        numStates = len(self.HStateOrder)
        H = np.zeros((numStates, numStates))
        for index1 in range(numStates):
            for index2 in range(numStates):
                matRow = HStartLineIndex + index1
                matCol = 1 + index2
                matElem = float(self.resultsFileLines[matRow][matCol])
                H[index1, index2] = matElem
        return H

    @property
    def HEvals(self):
        HEvalsIndex = self.resultsFileLines.index([i for i in self.resultsFileLines if i[0] == "H_evals"][0]) + 1
        return [float(i) for i in arrayNoBlanks(self.resultsFileLines[HEvalsIndex])]

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


def ECQSim(index):
    class ECQSimulation(Simulation):
        def __init__(self, qSys):
            super(ECQSimulation, self).__init__(qSys, "ECQ" + str(index))
            self.index = index

        def postProcess(self):
            CapMatGESim = CapMatGESimulation(self.qSys)
            postGEComponentList = CapMatGESim.postGEComponentList
            super(ECQSimulation, self).postProcess()
            qubitObj = self.qSys.allQubitsDict[self.index]
            qubitColumnIndex = postGEComponentList.index(qubitObj)
            cInv = np.linalg.inv(CapMatGESim.capMatGE)
            cSum = 1 / cInv[qubitColumnIndex, qubitColumnIndex]

            E_C = eConst ** 2 / (2 * cSum)  # In Joules
            EJ = self.qSys.allQubitsDict[self.index].EJ
            print(qubitObj.name + "EC (GHz): " + str(E_C * Joules_To_GHz))
            print(qubitObj.name + "EJ (GHz): " + str(EJ * Joules_To_GHz))
            print(qubitObj.name + "EJ/EC: " + str(EJ / E_C))
            lines = [["EC", str(E_C)], ["EJ/EC", str(EJ / E_C)]]
            csvWrite(self.resultsFilePath, lines)

        @property
        def EC(self):
            return self.resultsDict["EC"]

        def updateqSys(self):
            qSys.allQubitsDict[self.index].EcVal = self.EC

    return ECQSimulation


def ECRSim(index):
    class ECRSimulation(Simulation):
        def __init__(self, qSys):
            super(ECRSimulation, self).__init__(qSys, "ECR" + str(index))
            self.index = index

        def postProcess(self):
            CapMatGESim = CapMatGESimulation(self.qSys)
            postGEComponentList = CapMatGESim.postGEComponentList
            readoutResonatorObj = self.qSys.allReadoutResonatorsDict[self.index]
            resonatorColumnIndex = postGEComponentList.index(readoutResonatorObj)
            cInv = np.linalg.inv(CapMatGESim.capMatGE)
            cSum = 1 / cInv[resonatorColumnIndex, resonatorColumnIndex]

            E_C = eConst ** 2 / (2 * cSum)  # In Joules
            lines = [["EC", str(E_C)]]
            csvWrite(self.resultsFilePath, lines)

        @property
        def EC(self):
            return self.resultsDict["EC"]
    return ECRSimulation


def ZZQSim(q1Index,q2Index):
    class ZZQSimulation(Simulation):
        def __init__(self, qSys):
            super(ZZQSimulation, self).__init__(qSys, "zzQ" + str(q1Index) + "-" + str(q2Index))
            self.q1Index = q1Index
            self.q2Index = q2Index

        def postProcess(self):
            qubitIndices = [self.q1Index, self.q2Index]
            quantizeIndices = [self.qSys.allQubitsDict[i].quantizeIndex for i in qubitIndices]
            QuantizeObj = Quantize(self.qSys)
            stateListFunc = QuantizeObj.stateList

            stateList01 = stateListFunc([[quantizeIndices[1], 1]])
            stateList10 = stateListFunc([[quantizeIndices[0], 1]])
            stateList11 = stateListFunc([[quantizeIndices[0], 1], [quantizeIndices[1], 1]])

            E11 = QuantizeObj.HEval(stateList11)
            E10 = QuantizeObj.HEval(stateList10)
            E01 = QuantizeObj.HEval(stateList01)

            print("E11 (GHz):", E11)
            print("E10 (GHz):", E10)
            print("E01 (GHz):", E01)

            gz = E11 - E01 - E10

            print("gz" + str(qubitIndices[0]) + "-" + str(qubitIndices[1]) + "(MHz): ", gz * 1000)

            lines = [["g_z (MHz):", str(gz * 1000)]]
            csvWrite(self.resultsFilePath, lines)

        @property
        def gz(self):
            return self.resultsDict["g_z (MHz):"]
    return ZZQSimulation