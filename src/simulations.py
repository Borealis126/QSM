import numpy as np
import os
import time
from csvFunctions import csvRead, csvWrite, arrayNoBlanks, returnCorrectType
from ansysFunctions import *
import subprocess
from q3dSimulations import q3dExtractor
from circuitSimulations import S21_params,Y11RSimulation


class Simulation:
    def __init__(self, qSys, simName):
        qSys.loadDesignFiles()  # Every time a Simulation instance is made, the design files are loaded.
        self.qSys = qSys
        self.simName = simName
        self.q3dSims = dict()
        self.hfssSims = dict()
        self.circuitSims = dict()

        self.directoryPath = self.qSys.sysParams["Project Folder"] / self.simName

        self.paramsPath = self.directoryPath / "SimulationParameters.csv"
        self.resultsFilePath = self.directoryPath / "Results.csv"

        self.simParamsLines = []

    def loadSimulationParametersFile(self):
        simParamsFileLines = csvRead(self.paramsPath)
        simParams = dict()
        for line in simParamsFileLines:
            simParams[line[0]] = returnCorrectType(line[1])
        return simParams

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

    def initialize(self):
        # Create the directory if it doesn't yet exist.
        if self.qSys.sysParams["Compute Location"] == "Windows":
            bashCommand = "if not exist " + str(self.directoryPath) + " mkdir " + str(
                self.directory)
            subprocess.call(bashCommand, shell=True)
        elif self.qSys.sysParams["Compute Location"] == "Cluster":
            subprocess.call("rm -rf " + str(self.directoryPath), shell=True)
            bashCommand = "mkdir -p " + str(self.directoryPath)
            subprocess.call(bashCommand, shell=True)
        csvWrite(self.paramsPath, self.simParamsLines)

    def run(self):  # Specifically reserved for Ansys simulations.
        simParams = self.loadSimulationParametersFile()
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
            self.qSys.copyAnsysFile(q3dSim.aedtPath)
            simulatorFileInstance = open(q3dSim.simulatorPath, "w+", newline='')
            simulatorFileInstance.writelines(q3dSim.lines)
            simulatorFileInstance.close()
            self.runAnsysSimulator(q3dSim.aedtPath, q3dSim.simulatorPath, 60)
        for circuitSimName, circuitSim in self.circuitSims.items():
            """"Initialize all circuit simulations for the given simulation."""
            self.qSys.copyAnsysFile(circuitSim["Ansys"])
            # Generate the netlist file and load it into the AEDT
            netlistComponents = circuitSim.netlistComponents
            writeFile = open(circuitSim.netlistPath, "w")
            writeFile.writelines(netlistHeaderLines())
            writeFile.write("\n")
            writeFile.writelines(netlistCircuitLines(netlistComponents))
            writeFile.writelines(self.netlistPortsLines(circuitSimName))
            writeFile.write("\n")
            writeFile.writelines(netlistSimulationLines(simType, simParams))
            writeFile.write("\n")
            writeFile.write(".end")
            writeFile.close()
            loadNetlistFile(circuitSim["Ansys"], circuitSim["Netlist"])
            # Generate and run the ansysRunSimulator file
            lines = ansysSimulatorPreamb.copy()
            lines += [
                "oProject = oDesktop.SetActiveProject(\"" + str(circuitSim["Ansys"]).split("/")[-1][0:-5] + "\")\n",
                "oDesign = oProject.SetActiveDesign(\"" + "Netlist" + "\")\n",
                "oModuleReport = oDesign.GetModule(\"ReportSetup\")\n",
                "oDesign.AnalyzeAll()\n"
            ]

            # S21 circuit simulations
            if circuitSimName == "fullS21":
                lines += [
                    "oModuleReport.CreateReport(\"S Parameter Table 1\", \"Standard\", \"Data Table\", \"LNA\",\n",
                    "    [\n",
                    "        \"NAME:Context\",\n",
                    "        \"SimValueContext:=\"	, [3,0,2,0,False,False,-1,1,0,1,1,\"\",0,0]\n",
                    "    ],\n",
                    "    [\n",
                    "        \"F:=\"			, [\"All\"]\n",
                    "    ],\n",
                    "    [\n",
                    "        \"X Component:=\"		, \"F\",\n",
                    "        \"Y Component:=\"		, [\"S(2,1)\"]\n",
                    "    ], [])\n",
                    "oModuleReport.ExportToFile(\"S Parameter Table 1\", \"" + str(
                        circuitSim["ResultsFile"]) + "\", False)\n"
                ]
            # Y11 circuit simulations
            elif (circuitSimName[0:4] in ["Y11R", "Y11Q"]
                  or circuitSimName[0:5] == "Y11BC"
                  or circuitSimName[0:6] == "YRestR" or circuitSimName[0:10] == "Y11LumpedR"):
                lines += [
                    "oModuleReport.CreateReport(\"Y Parameter Table 1\", \"Standard\", \"Data Table\", \"LNA\",\n",
                    "    [\n",
                    "        \"NAME:Context\",\n",
                    "        \"SimValueContext:=\"	, [3,0,2,0,False,False,-1,1,0,1,1,\"\",0,0]\n",
                    "    ],\n",
                    "    [\n",
                    "        \"F:=\"			, [\"All\"]\n",
                    "    ],\n",
                    "    [\n",
                    "        \"X Component:=\"		, \"F\",\n",
                    "        \"Y Component:=\"		, [\"Y(1,1)\"]\n",
                    "    ], [])\n",
                    (
                            "oModuleReport.ExportToFile(\"Y Parameter Table 1\", \""
                            + str(circuitSim["ResultsFile"])
                            + "\", False)\n"
                    )
                ]
            elif circuitSimName[0:4] == "Z21Q":
                lines += [
                    "oModuleReport.CreateReport(\"Z Parameter Table 1\", \"Standard\", \"Data Table\", \"LNA\",\n",
                    "    [\n",
                    "        \"NAME:Context\",\n",
                    "        \"SimValueContext:=\"	, [3,0,2,0,False,False,-1,1,0,1,1,\"\",0,0]\n",
                    "    ],\n",
                    "    [\n",
                    "        \"F:=\"			, [\"All\"]\n",
                    "    ],\n",
                    "    [\n",
                    "        \"X Component:=\"		, \"F\",\n",
                    "        \"Y Component:=\"		, [\"Z(2,1)\"]\n",
                    "    ], [])\n",
                    (
                            "oModuleReport.ExportToFile(\"Z Parameter Table 1\", \""
                            + str(circuitSim["ResultsFile"])
                            + "\", False)\n"
                    )
                ]
            lines.append(ansysSaveLine)
            simulatorFileInstance = open(circuitSim["ansysRunSimulator"], "w+", newline='')
            simulatorFileInstance.writelines(lines)
            simulatorFileInstance.close()
            self.runAnsysSimulator(circuitSim["Ansys"], circuitSim["ansysRunSimulator"],
                                   self.simFiles[simType]["Directory"], 3)  # Circuit simulations are quite fast

    def postProcess(self):
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
                for circuitSim in self.circuitSims:
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


class CapMatSimulation(Simulation):
    def __init__(self, qSys):
        super().__init__(qSys, "capMat")
        q3dSimName = "capMatExtractor"
        self.q3dSims = {q3dSimName: q3dExtractor(q3dSimName, self.directoryPath, qSys)}

    def initialize(self):
        self.simParamsLines = [["PerRefine", "100"], ["MaxPass", "99"]]
        super(CapMatSimulation, self).initialize()

    def run(self):
        simParams = self.loadSimulationParametersFile()

        self.q3dSims["capMatExtractor"].updateLines(simParams)

        super(CapMatSimulation, self).run()

    def postProcess(self):
        super(CapMatSimulation, self).postProcess()
        capMatResultsFileLines = csvRead(self.q3dSims["q3dExtractor"].resultsFilePath)
        capMatHeaderLineIndex = 0
        for index, line in enumerate(capMatResultsFileLines):
            if line != [] and line[0] == "Capacitance Matrix":
                capMatHeaderLineIndex = index + 1
        unitsMultiplier = self.capMatUnitsToF
        numNodes = len(self.ansysCapMatHeaders)
        capMat = np.zeros((numNodes, numNodes))
        capMatStartLineIndex = capMatHeaderLineIndex + 1
        for index1, header1 in enumerate(self.ansysCapMatHeaders):
            for index2, header2 in enumerate(self.ansysCapMatHeaders):
                matRow = capMatStartLineIndex + index1
                matCol = 1 + index2
                capacitanceValue = float(capMatResultsFileLines[matRow][matCol]) * unitsMultiplier
                capMat[index1, index2] = capacitanceValue

        lines = [["Capacitance (F)"], [""] + self.ansysCapMatHeaders]
        for rowIndex in range(numNodes):
            lines.append([self.ansysCapMatHeaders[rowIndex]] + list(capMat[rowIndex, :]))
        lines.append([""])
        lines.append(["Capacitance To Ground (F)"])
        for rowIndex in range(numNodes):
            lines.append([self.ansysCapMatHeaders[rowIndex]] + [str(sum(capMat[rowIndex, :]))])

        csvWrite(self.resultsFilePath, lines)

    @property
    def capMatResultsFileLines(self):
        return csvRead(self.q3dSims["capMatExtractor"].resultsFilePath)

    @property
    def ansysCapMatHeaders(self):
        capMatHeaderLineIndex = 0
        for index, line in enumerate(self.capMatResultsFileLines):
            if line != [] and line[0] == "Capacitance Matrix":
                capMatHeaderLineIndex = index + 1
        return arrayNoBlanks(self.capMatResultsFileLines[capMatHeaderLineIndex])

    @property
    def capMat(self):
        capMatHeaderLineIndex = self.capMatResultsFileLines.index(
            [i for i in self.capMatResultsFileLines if i[0] == "Capacitance (F)"][0]) + 1
        numNodes = len(self.ansysCapMatHeaders)

        capMat = np.zeros((numNodes, numNodes))
        capMatStartLineIndex = capMatHeaderLineIndex + 1
        for index1 in range(numNodes):
            for index2 in range(numNodes):
                matRow = capMatStartLineIndex + index1
                matCol = 1 + index2
                capacitanceValue = float(self.capMatResultsFileLines[matRow][matCol])  # Already in units of F
                capMat[index1, index2] = capacitanceValue

        """If the feedline is not simulated, add in the capacitance to the resonators."""
        if self.qSys.sysParams["Simulate Feedline?"] == "No" and self.qSys.allControlLinesDict != {}:
            newCapMat = np.zeros((numNodes + 1, numNodes + 1))  # The feedline will be the highest index.
            feedlineIndex = numNodes
            self.ansysCapMatHeaders.append(self.qSys.allControlLinesDict[0].lineNode.name)
            # Copy capMat
            for index1 in range(numNodes):
                for index2 in range(numNodes):
                    newCapMat[index1, index2] = capMat[index1, index2]
            # Add resonator capacitances
            for readoutResonatorIndex, readoutResonator in self.qSys.allReadoutResonatorsDict.items():
                genParams = readoutResonator.generalParamsDict
                pad1Index = self.ansysCapMatHeaders.index(readoutResonator.pad1.node.name)
                # Capacitance to the feedline
                newCapMat[pad1Index, feedlineIndex] = -genParams["Capacitance to Feedline (F)"]
                newCapMat[feedlineIndex, pad1Index] = -genParams["Capacitance to Feedline (F)"]
                # Fix capacitance to ground
                wrongCapToGround = sum(capMat[pad1Index, :])
                correctCapToGround = genParams["Feedline Pad Capacitance to Ground (F)"]
                newCapMat[pad1Index, pad1Index] = (capMat[pad1Index, pad1Index]
                                                   - wrongCapToGround + correctCapToGround)
            capMat = newCapMat
        return capMat

    @property
    def capMatUnitsToF(self):
        capMatResultsFileLines = csvRead(self.q3dSims["q3dExtractor"].resultsFilePath)
        reportedUnits = capMatResultsFileLines[2][0][8:]  # "C Units:pF"->"pF"
        unitsMultiplier = 1
        if reportedUnits == "pF":
            unitsMultiplier = 1e-12
        return unitsMultiplier


class LumpedRSimulation(Simulation):
    def __init__(self, qSys, readoutResonatorIndex):
        super(LumpedRSimulation, self).__init__(qSys, "lumpedR" + str(readoutResonatorIndex))

        Y11RSimName = "Y11R" + str(readoutResonatorIndex)
        YRestRSimName = "YRestR" + str(readoutResonatorIndex)
        self.circuitSims = {Y11RSimName: Y11RSimulation(Y11RSimName, self.directoryPath, qSys, readoutResonatorIndex),
                            YRestRSimName: YRestRSimulation(YRestRSimName, self.directoryPath, qSys,
                                                            readoutResonatorIndex)}

    def initialize(self):
        self.simParamsLines = S21_params(self.simName)
        super(LumpedRSimulation, self).initialize()



class Quantize(Simulation):
    def __init__(self, qSys):
        super().__init__(qSys, "quantize")

    def initialize(self):
        quantizeList = "["
        for component in self.qSys.postGEComponentList:
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
        simParams = self.loadSimulationParametersFile()
        print("started quantize")
        quantizeStartTime = time.time()

        numQubitPhotons = simParams["NumQubitPhotons"]
        numResonatorPhotons = simParams["NumResonatorPhotons"]
        numPhotons = max(numQubitPhotons, numResonatorPhotons)

        # self.capMatGE needs to be reduced based on the requested components to quantize.
        quantizeComponentListNames = readQuantizeList(simParams["QuantizeList"])
        quantizeComponentList = [self.qSys.componentFromName(i) for i in
                                 quantizeComponentListNames]  # Determines the index ordering in capMatGE_quant!
        for index, component in enumerate(quantizeComponentList):
            component.quantizeIndex = index

        numComponents = len(quantizeComponentList)
        capMatGEIndicesToKeep = [self.qSys.postGEComponentList.index(i) for i in quantizeComponentList]

        rows = np.array(capMatGEIndicesToKeep, dtype=np.intp)
        columns = np.array(capMatGEIndicesToKeep, dtype=np.intp)
        capMatGE_quant = self.capMatGE[rows[:, np.newaxis], columns]

        dim = numPhotons + 2
        qObjDim = [dim] * numComponents
        Cinv = np.linalg.inv(capMatGE_quant)

        # Assemble the Hamiltonian. H is in units of radians (H/hbar). Calculates 1/2*Q.T*Cinv*Q.
        print("Start assembling H")
        startTime = time.time()
        resolveLHSSum = qzero(qObjDim)
        for Cinv_rowIndex, Cinv_row in enumerate(Cinv):
            resolveRHSSum = qzero(qObjDim)
            for componentIndex, component in enumerate(quantizeComponentList):
                resolveRHSSum += Cinv_row[componentIndex] * component.QsecondQuant(dim, numComponents)
            LHSComponent = quantizeComponentList[Cinv_rowIndex]
            resolveLHSSum += 1 / 2 * LHSComponent.QsecondQuant(dim, numComponents) * resolveRHSSum
        H = resolveLHSSum
        endTime = time.time()
        print("Finished assembling H", (endTime - startTime) / 60)
        print("Initial matrix dimension:", H.shape[0])

        print("Start adding inductance")
        startTime = time.time()
        # Add inductance terms
        for component in quantizeComponentList:
            print(component.name)
            if issubclass(type(component), Qubit) or isinstance(component, StraightBusCoupler):
                x = ((2 * np.pi * np.sqrt(hbarConst) / Phi_0Const) * component.PhisecondQuant(dim, numComponents))
                for i in range(int(simParams["TrigOrder"] / 2) + 1):
                    cosTerm = (-1) ** i * x ** (2 * i) / np.math.factorial(2 * i)
                    H -= (component.EJ / hbarConst) * cosTerm
                    print("cos x^" + str(2 * i) + " term Frobenius norm: ", cosTerm.norm(norm="fro"))
            elif isinstance(component, ReadoutResonator):
                term = component.PhisecondQuant(dim, numComponents) ** 2 / (2 * component.equivL)
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
        qubitIndices = [i for i in range(numComponents) if issubclass(type(quantizeComponentList[i]), Qubit)]
        readoutResonatorIndices = [i for i in range(numComponents) if
                                   isinstance(quantizeComponentList[i], ReadoutResonator)]
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
        for component in quantizeComponentList:
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
        for component in quantizeComponentList:
            fockStates = [[n if i == component.quantizeIndex else 0 for i in range(numComponents)] for n in
                          range(newHDim[component.quantizeIndex])]
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
            [i.name for i in quantizeComponentList],
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
        csvWrite(self.simFiles["quantize"]["ResultsFile"], lines)
        quantizeEndTime = time.time()
        print("Total time:", (quantizeEndTime - quantizeStartTime) / 60)

        for component in quantizeComponentList:
            if isinstance(component, ReadoutResonator):
                print(component.equivL)
