from circuitSimulations import CircuitSim, S21_params
from simulations import Simulation, CapMat
from dataIO import jsonWrite
from copy import deepcopy

class LumpedRSimulation(Simulation):
    def __init__(self, qArch):
        super().__init__(qArch, "Y_BBQ")
        self.Y_BBQ_SimName = "Y_BBQ"
        CapMatObj = CapMat(self.qArch)
        self.circuitSims = {self.Y_BBQ_SimName: Y_BBQ_Simulation(self.directoryPath, qArch, CapMatObj)}

    def initialize(self):
        simParamsDict = S21_params
        self.generateParams(simParamsDict)

    def run(self):
        self.runAllSims()

    def postProcess(self):
        self.deleteUnneededFiles()
        resultsDict = {"equivL(H):": 1, "equivC(F):": 1}
        jsonWrite(self.resultsFilePath, resultsDict)



class Y_BBQ_Simulation(CircuitSim):

    def __init__(self, simDirectory, qArch, CapMatObj):
        super().__init__("Y_BBQ", simDirectory, qArch, CapMatObj)

    @property
    def netlistComponents(self):
        netlistComponents = deepcopy(self.generalNetlistComponents)

        # Add matching resistors to feedline if there are no ports on either end
        netlistComponents["Resistors"]["RFL"] = {
            "node1NetlistName": self.netlistName("G"),
            "node2NetlistName": self.netlistName("FL"),
            "R": 50  # 50 ohm
        }
        netlistComponents["Resistors"]["RFR"] = {
            "node1NetlistName": self.netlistName("G"),
            "node2NetlistName": self.netlistName("FR"),
            "R": 50
        }
        return netlistComponents

    def netlistName(self, nodeName):
        if nodeName == self.qArch.allReadoutResonatorsDict[self.index].design.pad2.node.name:
            return "Port1"
        if nodeName == "G":
            return "0"
        return "net_" + nodeName

    @property
    def netlistPortsLines(self):
        portNet2Dict = dict()
        """One grounded port on one node"""
        portNet2Dict[1] = self.netlistName("G")
        portsLines = []
        for portIndex, portNet2 in portNet2Dict.items():
            portsLines += [("RPort" + str(portIndex) + " Port" + str(portIndex)
                            + " " + portNet2 + " PORTNUM=" + str(portIndex) + " RZ=50\n"),
                           (".PORT Port" + str(portIndex) + " " + portNet2
                            + " " + str(portIndex) + " RPort" + str(portIndex) + "\n")]
        return portsLines

    @staticmethod
    def netlistSimulationLines(simParams):  # Contains simulation-specific info
        return [
            ".LNA\n",
            "+ LIN " + str(simParams["LNA_counts"]) + " " + str(simParams["LNA_start (GHz)"] * 1e9)
            + " " + str(simParams["LNA_stop (GHz)"] * 1e9) + "\n",
            "+ FLAG=\'LNA\'\n"
        ]

    @property
    def reportLines(self):
        return YReportLines(self.resultsFilePath)


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