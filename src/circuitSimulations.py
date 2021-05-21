import qSysObjects
from copy import deepcopy


class CircuitSim:  # Y11R, YRest are CircuitSims.
    def __init__(self, circuitSimName, simDirectory, qSys, CapMatObj):
        self.name = circuitSimName
        self.qSys = qSys
        self.capMatObj=CapMatObj
        self.aedtPath = simDirectory / (circuitSimName + ".aedt")
        self.netlistPath = simDirectory / (circuitSimName + "_" + "Netlist.txt")
        self.ansysRunSimulatorPath = simDirectory / (circuitSimName + "_" + "ansysRunSimulator.py")
        self.logPath = simDirectory / (circuitSimName + "_" + "Simulator.log")
        self.resultsFilePath = simDirectory / (circuitSimName + "_" + "Results.csv")
        self.aedtFolderPath = simDirectory / (circuitSimName + ".aedtresults")

    # Takes as argument a netlistName function of one of its children.
    @property
    def generalNetlistComponents(self):
        netlistComponents = {
            "Capacitances": dict(),
            "Inductors": dict(),
            "Resistors": dict(),
            "Transmission Lines": dict(),
            "Feedline Sections": dict()
        }
        # Everything that doesn't involve the feedline.
        ansysCapMatHeaders = self.capMatObj.ansysCapMatHeaders
        capMat = self.capMatObj.capMat
        for index1, node1Name in enumerate(ansysCapMatHeaders):  # Iterate through the capacitance matrix
            for node2Name in ansysCapMatHeaders[index1:]:  # So it's like (0,0),(0,1),(0,2),(1,1),(1,2),(2,2).
                if "CL0" not in node1Name and "CL0" not in node2Name:
                    node1NetlistName = self.netlistName(node1Name)
                    if node1Name == node2Name:  # Capacitance to ground
                        capVal = sum(capMat[index1])
                        node2Name = "G"
                        node2NetlistName = self.netlistName(node2Name)
                    else:
                        capVal = -capMat[index1][ansysCapMatHeaders.index(node2Name)]
                        node2NetlistName = self.netlistName(node2Name)
                    capacitanceName = "C" + node1Name + "_" + node2Name
                    netlistComponents["Capacitances"][capacitanceName] = {
                        "node1NetlistName": node1NetlistName,
                        "node2NetlistName": node2NetlistName,
                        "C": capVal
                    }
        # Feedline capacitance to resonator pad 1
        for readoutResonatorIndex, readoutResonator in self.qSys.allReadoutResonatorsDict.items():
            capVal = 0
            node1Name = readoutResonator.pad1.node.name
            node1NetlistName = self.netlistName(node1Name)
            node2Name = "F" + str(readoutResonatorIndex)
            node2NetlistName = self.netlistName(node2Name)
            if self.qSys.sysParams["Simulate Feedline?"] == "Yes":
                index1 = ansysCapMatHeaders.index(node1Name)
                index2 = ansysCapMatHeaders.index(self.qSys.allControlLinesDict[0].lineNode.name)
                capVal = -capMat[index1][index2]
            elif self.qSys.sysParams["Simulate Feedline?"] == "No":
                capVal = readoutResonator.componentParams["Capacitance to Feedline (F)"]
            capacitanceName = "C" + node1Name + "_" + node2Name
            netlistComponents["Capacitances"][capacitanceName] = {
                "node1NetlistName": node1NetlistName,
                "node2NetlistName": node2NetlistName,
                "C": capVal
            }
        # Qubit inductances
        for qubitIndex, qubit in self.qSys.allQubitsDict.items():
            node1Name = qubit.pad1.node.name
            node1NetlistName = self.netlistName(node1Name)
            node2Name = qubit.pad2.node.name
            node2NetlistName = self.netlistName(node2Name)
            if isinstance(qubit, qSysObjects.GroundedQubit):
                node2Name = "G"
                node2NetlistName = self.netlistName(node2Name)

            inductorName = "L" + node1Name + "_" + node2Name

            netlistComponents["Inductors"][inductorName] = {
                "node1NetlistName": node1NetlistName,
                "node2NetlistName": node2NetlistName,
                "L": qubit.L_i_fixed
            }
        # Readout Resonators
        for readoutResonatorIndex, readoutResonator in self.qSys.allReadoutResonatorsDict.items():
            node1Name = readoutResonator.pad1.node.name
            node1NetlistName = self.netlistName(node1Name)
            node2Name = readoutResonator.pad2.node.name
            node2NetlistName = self.netlistName(node2Name)
            resonatorName = "T" + node1Name + "_" + node2Name
            netlistComponents["Transmission Lines"][resonatorName] = {
                "node1NetlistName": node1NetlistName,
                "node2NetlistName": node2NetlistName,
                "TD": self.qSys.CPW.TD(readoutResonator.geometryParams["Length"])
            }
        # Feedline--------------------------------------------------------------------------------------------------------------------
        """There are always N+1 feedline sections corresponding to segments between the nodes FL,F1,F2,...FN,FR"""
        feedlineNodes = ["FL"]  # Note that the order defines the segments!
        for i in range(self.qSys.sysParams["Number of Readout Resonators"]):
            feedlineNodes.append("F" + str(i))  # Must agree with the naming convention in the capacitances section!
        feedlineNodes.append("FR")
        """-1 since there are one fewer segments than nodes. Should be number of qubits+1"""
        for index, node1Name in enumerate(feedlineNodes[:-1]):
            node1Name = feedlineNodes[index]
            node1NetlistName = self.netlistName(node1Name)
            node2Name = feedlineNodes[index + 1]
            node2NetlistName = self.netlistName(node2Name)
            feedlineSectionName = "T" + node1Name + "_" + node2Name
            feedline = self.qSys.chipDict[0].controlLineDict[0]
            firstResonator = self.qSys.allReadoutResonatorsDict[0]
            lastResonator = self.qSys.allReadoutResonatorsDict[self.qSys.sysParams["Number of Readout Resonators"] - 1]
            if index == 0:  # If the first segment
                length = feedline.pathLengthFromStartToPoint(
                    [firstResonator.pad1.node.centerX, firstResonator.pad1.node.centerY])
            elif index == len(feedlineNodes) - 2:  # If the last segment...
                length = feedline.pathLengthFromEndToPoint(
                    [lastResonator.pad1.node.centerX, lastResonator.pad1.node.centerY])
            else:
                length = feedline.pathLengthPointToPoint(
                    [self.qSys.allReadoutResonatorsDict[index - 1].pad1.node.centerX,
                     self.qSys.allReadoutResonatorsDict[index - 1].pad1.node.centerY],
                    [self.qSys.allReadoutResonatorsDict[index].pad1.node.centerX,
                     self.qSys.allReadoutResonatorsDict[index].pad1.node.centerY]
                )
            netlistComponents["Transmission Lines"][feedlineSectionName] = {
                "node1NetlistName": node1NetlistName,
                "node2NetlistName": node2NetlistName,
                "TD": self.qSys.CPW.TD(length)
            }
        return netlistComponents

    @property
    def netlistComponentsLines(self):
        return netlistCircuitLines(self.netlistComponents)


class Y11RSimulation(CircuitSim):
    def __init__(self, index, circuitSimName, simDirectory, qSys, CapMatObj):
        super(Y11RSimulation, self).__init__(circuitSimName, simDirectory, qSys, CapMatObj)
        self.index = index

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
        if nodeName == self.qSys.allReadoutResonatorsDict[self.index].pad2.node.name:
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


class YRestRSimulation(CircuitSim):
    def __init__(self, index, circuitSimName, simDirectory, qSys, CapMatObj):
        super(YRestRSimulation, self).__init__(circuitSimName, simDirectory, qSys, CapMatObj)
        self.index = index

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

        readoutResonator = self.qSys.allReadoutResonatorsDict[self.index]
        node1Name = readoutResonator.pad1.node.name
        node2Name = readoutResonator.pad2.node.name
        resonatorName = "T" + node1Name + "_" + node2Name
        netlistComponents["Transmission Lines"].pop(resonatorName)  # Remove the resonator as per Junling's procedure.
        netlistComponents["Capacitances"]["CR" + str(self.index) + "Pad1_G"]["C"] = 0
        netlistComponents["Capacitances"]["CR" + str(self.index) + "Pad2_G"]["C"] = 0
        netlistComponents["Capacitances"]["CR" + str(self.index) + "Pad1_F" + str(self.index)]["C"] = 0

        """Short the two ends of the resonator together. This is functionally accomplished by removing all elements
        of the netlist containing R[N]Pad[N} nodes."""

        for netlistName, component in deepcopy(netlistComponents["Capacitances"]).items():
            if (component["node1NetlistName"] == self.netlistName(node1Name)
                    or component["node2NetlistName"] == self.netlistName(node1Name)):
                netlistComponents["Capacitances"].pop(netlistName)

        return netlistComponents

    def netlistName(self, nodeName):
        if nodeName == self.qSys.allReadoutResonatorsDict[self.index].pad2.node.name:
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


S21_params = {"LNA_start (GHz)": 4, "LNA_stop (GHz)": 7, "LNA_counts": 200}


netlistHeaderLines = [
    ".option PARHIER=\'local\'\n",
    ".option max_messages=1\n",
    ".option num_threads=4\n"
]


def netlistCircuitLines(netlistComponents):
    lines = []
    # Capacitors
    for capacitanceName, capacitance in netlistComponents["Capacitances"].items():
        lines.append(capacitanceName + " " + capacitance["node1NetlistName"] + " "
                     + capacitance["node2NetlistName"] + " " + str(capacitance["C"]) + "\n")
    # Inductors
    for inductorName, inductor in netlistComponents["Inductors"].items():
        lines.append(inductorName + " " + inductor["node1NetlistName"] + " "
                     + inductor["node2NetlistName"] + " " + str(inductor["L"]) + "\n")
    # Resistors
    for resistorName, resistor in netlistComponents["Resistors"].items():
        lines.append(resistorName + " " + resistor["node1NetlistName"] + " "
                     + resistor["node2NetlistName"] + " " + str(resistor["R"]) + "\n")
    # Transmission Lines
    for transmissionLineName, transmissionLine in netlistComponents["Transmission Lines"].items():
        lines.append(transmissionLineName + " " + transmissionLine["node1NetlistName"] + " 0 "
                     + transmissionLine["node2NetlistName"] + " 0 "
                     + "Z0=50 TD=" + str(transmissionLine["TD"]) + "\n")
    return lines


def loadNetlistFile(ansysFile, netlistFile):
    """I hate this method, but it's the only way I know of to load the netlist into the aedt project."""
    netlistFile = open(netlistFile, 'r')
    netlistFileLines = netlistFile.readlines()
    netlistFileLinesAedtEdit = [aedtEdit(i) for i in netlistFileLines]

    ansysProjectFile = open(ansysFile, 'r')
    ansysProjectFileLines = ansysProjectFile.readlines()

    startLineIndex = ansysProjectFileLines.index("\t\t$begin \'Netlist\'\n")
    endLineIndex = ansysProjectFileLines.index("\t\t$end \'Netlist\'\n")

    beforeLines = ansysProjectFileLines[0:startLineIndex + 1]
    afterLines = ansysProjectFileLines[endLineIndex:]
    betweenLines = ["\t\t\tText=\'" + netlistFileLinesAedtEdit[0][0:-1] + "\\\n"]
    for line in netlistFileLinesAedtEdit[1:-1]:
        betweenLines.append(line[0:-1] + "\\\n")
    betweenLines.append(netlistFileLinesAedtEdit[-1] + "\'\n")  # No \n to remove at end of line!

    ansysProjectFileInstance = open(ansysFile, "w+", newline='')  # Overwrites aedt file to insert netlist
    ansysProjectFileInstance.writelines(beforeLines + betweenLines + afterLines)  # Initialization lines.
    ansysProjectFileInstance.close()


def YReportLines(resultsFile):
    return [
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
                + str(resultsFile)
                + "\", False)\n"
        )
    ]


def aedtEdit(line):
    """This function edits the aedt file lines to add a backslash before each single quote.
    Needed for loading in the netlist"""
    returnLine = ""
    for char in line:
        if char == "\'":
            returnLine = returnLine + "\\" + char
        else:
            returnLine = returnLine + char
    return returnLine
