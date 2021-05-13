class CircuitSim:  # Y11R, YRest are CircuitSims.
    def __init__(self, circuitSimName, simDirectory, qSys):
        qSys.loadDesignFiles()
        self.name = circuitSimName
        self.qSys = qSys
        self.aedtPath = simDirectory / (circuitSimName + ".aedt")
        self.netlistPath = simDirectory / (circuitSimName + "_" + "Netlist.txt")
        self.ansysInitSimulatorPath = simDirectory / (circuitSimName + "_" + "ansysInitSimulator.py")
        self.ansysRunSimulatorPath = simDirectory / (circuitSimName + "_" + "ansysRunSimulator.py")
        self.logPath = simDirectory / (circuitSimName + "_" + "Simulator.log")
        self.resultsFilePath = simDirectory / (circuitSimName + "_" + "Results.csv")
        self.aedtFolderPath = simDirectory / (circuitSimName + ".aedtresults")

    # Takes as argument a netlistName function of one of its children.
    def generateNetlistComponents(self, netlistName):
        netlistComponents = {
            "Capacitances": dict(),
            "Inductors": dict(),
            "Resistors": dict(),
            "Transmission Lines": dict(),
            "PTCs": dict(),
            "Feedline Sections": dict()
        }
        # Everything that doesn't involve the feedline.
        ansysCapMatHeaders = CapMatSimulation(self.qSys).ansysCapMatHeaders
        capMat = CapMatSimulation(self.qSys).capMat
        for index1, node1Name in enumerate(ansysCapMatHeaders):  # Iterate through the capacitance matrix
            for index2, node2Name in enumerate(ansysCapMatHeaders):  # So it's like (0,0),(0,1),(0,2),(1,1),(1,2),(2,2).
                if "CL0" not in node1Name and "CL0" not in node2Name:
                    node1NetlistName = netlistName(node1Name, circuitSim)
                    if index1 == index2:  # Capacitance to ground
                        capVal = sum(capMat[index1])
                        node2Name = "G"
                        node2NetlistName = netlistName(node2Name, circuitSim)
                    else:
                        capVal = -capMat[index1][index2]
                        node2Name = ansysCapMatHeaders[index2]
                        node2NetlistName = netlistName(node2Name, circuitSim)
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
            node1NetlistName = netlistName(node1Name, circuitSim)
            node2Name = "F" + str(readoutResonatorIndex)
            node2NetlistName = netlistName(node2Name, circuitSim)
            if self.qSys.sysParams["Simulate Feedline?"] == "Yes":
                index1 = ansysCapMatHeaders.index(node1Name)
                index2 = ansysCapMatHeaders.index(self.qSys.allControlLinesDict[0].lineNode.name)
                capVal = -capMat[index1][index2]
            elif self.qSys.sysParams["Simulate Feedline?"] == "No":
                capVal = readoutResonator.generalParamsDict["Capacitance to Feedline (F)"]
            capacitanceName = "C" + node1Name + "_" + node2Name
            netlistComponents["Capacitances"][capacitanceName] = {
                "node1NetlistName": node1NetlistName,
                "node2NetlistName": node2NetlistName,
                "C": capVal
            }
        # Qubit inductances
        for qubitIndex, qubit in self.qSys.allQubitsDict.items():
            node1Name = qubit.pad1.node.name
            node1NetlistName = netlistName(node1Name, circuitSim)
            node2Name = qubit.pad2.node.name
            node2NetlistName = netlistName(node2Name, circuitSim)
            if isinstance(qubit, GroundedQubit):
                node2Name = "G"
                node2NetlistName = netlistName(node2Name, circuitSim)

            inductorName = "L" + node1Name + "_" + node2Name

            netlistComponents["Inductors"][inductorName] = {
                "node1NetlistName": node1NetlistName,
                "node2NetlistName": node2NetlistName,
                "L": qubit.L_i_fixed
            }
        # Readout Resonators
        for readoutResonatorIndex, readoutResonator in self.qSys.allReadoutResonatorsDict.items():
            node1Name = readoutResonator.pad1.node.name
            node1NetlistName = netlistName(node1Name, circuitSim)
            node2Name = readoutResonator.pad2.node.name
            node2NetlistName = netlistName(node2Name, circuitSim)
            resonatorName = "T" + node1Name + "_" + node2Name
            netlistComponents["Transmission Lines"][resonatorName] = {
                "node1NetlistName": node1NetlistName,
                "node2NetlistName": node2NetlistName,
                "TD": self.qSys.CPW.TD(readoutResonator.geometryParamsDict["Length"])
            }
        # PTCs
        for PTCIndex, PTC in self.qSys.allPTCsDict.items():
            node1Name = PTC.pad1.node.name
            node1NetlistName = netlistName(node1Name, circuitSim)
            node2Name = PTC.pad2.node.name
            node2NetlistName = netlistName(node2Name, circuitSim)
            inductorName = "L" + node1Name + "_" + node2Name

            netlistComponents["Transmission Lines"]["T" + node1Name + "_G"] = {
                "node1NetlistName": node1NetlistName,
                "node2NetlistName": "G",
                "TD": PTC.TD
            }

            netlistComponents["Inductors"][inductorName] = {
                "node1NetlistName": node1NetlistName,
                "node2NetlistName": node2NetlistName,
                "L": PTC.generalParamsDict["SQUID Inductance(H)"]
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
            node1NetlistName = netlistName(node1Name, circuitSim)
            node2Name = feedlineNodes[index + 1]
            node2NetlistName = netlistName(node2Name, circuitSim)
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

class Y11RSimulation(CircuitSim):
    def __init__(self, circuitSimName, simDirectory, qSys, index):
        super(Y11RSimulation, self).__init__(circuitSimName, simDirectory, qSys)
        self.index = index

    @property
    def netlistComponents(self):
        netlistComponents = super(Y11RSimulation, self).generateNetlistComponents(self.netlistName)

        # Add matching resistors to feedline if there are no ports on either end
        netlistComponents["Resistors"]["RFL"] = {
            "node1NetlistName": self.netlistName("G", circuitSim),
            "node2NetlistName": self.netlistName("FL", circuitSim),
            "R": 50  # 50 ohm
        }
        netlistComponents["Resistors"]["RFR"] = {
            "node1NetlistName": self.netlistName("G", circuitSim),
            "node2NetlistName": self.netlistName("FR", circuitSim),
            "R": 50
        }

    def netlistName(self, nodeName):
        readoutResonatorIndex = int(circuitSim[4:])
        if nodeName == self.qSys.allReadoutResonatorsDict[readoutResonatorIndex].pad2.node.name:
            return "Port1"
        if nodeName == "G":
            return "0"
        return "net_" + nodeName


class YRestRSimulation(CircuitSim):
    def __init__(self, circuitSimName, simDirectory, qSys, index):
        super(Y11RSimulation, self).__init__(circuitSimName, simDirectory, qSys)
        self.index = index

    @property
    def netlistComponents(self):
        netlistComponents = super(Y11RSimulation, self).generateNetlistComponents(self.netlistName)

        # Add matching resistors to feedline if there are no ports on either end
        netlistComponents["Resistors"]["RFL"] = {
            "node1NetlistName": self.netlistName("G", circuitSim),
            "node2NetlistName": self.netlistName("FL", circuitSim),
            "R": 50  # 50 ohm
        }
        netlistComponents["Resistors"]["RFR"] = {
            "node1NetlistName": self.netlistName("G", circuitSim),
            "node2NetlistName": self.netlistName("FR", circuitSim),
            "R": 50
        }

    def netlistName(self, nodeName):
        readoutResonatorIndex = int(circuitSim[4:])
        if nodeName == self.qSys.allReadoutResonatorsDict[readoutResonatorIndex].pad2.node.name:
            return "Port1"
        if nodeName == "G":
            return "0"
        return "net_" + nodeName





def S21_params(simName):
    return [
        ["Type", simName],
        ["LNA_start (GHz)", "4"],
        ["LNA_stop (GHz)", "7"],
        ["LNA_counts", "200"]
    ]

