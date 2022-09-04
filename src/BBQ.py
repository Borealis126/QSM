from .circuitSimulations import CircuitSim, S21_params, YReportLines
from .simulations import Simulation, CapMat
from .dataIO import jsonWrite
from copy import deepcopy

class BBQ(Simulation):
    def __init__(self, qArch):
        super().__init__(qArch, "BBQ")
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
        if nodeName == "G":
            return "0"
        return "net_" + nodeName

    @property
    def netlistPortsLines(self):
        portsLines = []
        for qubitIndex, qubit in self.qArch.allQubitsDict.items():
            node_1 = self.netlistName(qubit.design.pad1.node.name)
            node_2 = self.netlistName(qubit.design.pad2.node.name)
            portsLines += [
                "RPort" + str(qubitIndex) + " " + node_1 + " " + node_2 + " PORTNUM=" + str(
                    qubitIndex) + " RZ=50\n",
                ".PORT " + node_1 + " " + node_2 + " " + str(qubitIndex) + " RPort" + str(
                    qubitIndex) + "\n"]
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

        super().__init__(qArch, "capMat")