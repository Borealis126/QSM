from .circuitSimulations import CircuitSim, S21_params, YReportLines
from .simulations import Simulation, CapMat
from copy import deepcopy
from itertools import product
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from .ansysAPI import ansysOutputToComplex
from scipy.interpolate import interp1d
from scipy.optimize import fsolve
from .dataIO import jsonWrite

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
        df = pd.read_csv(self.circuitSims[self.Y_BBQ_SimName].resultsFilePath)
        fig, ax = plt.subplots(1)

        resultsDict = dict()

        for qubitIndex, qubit in self.qArch.allQubitsDict.items():
            freq_data = df['Freq [GHz]']
            y_data = np.imag(df['Y('+str(qubitIndex+1)+','+str(qubitIndex+1)+') [mSie]'].apply(ansysOutputToComplex).astype(complex))
            ax.plot(freq_data, y_data)
            resultsDict['Q'+str(qubitIndex)+"Freq (GHz)"] = fsolve(interp1d(freq_data, y_data), freq_data[0])[0]
        N = len(self.qArch.allQubitsDict)
        for resonatorIndex, resonator in self.qArch.allReadoutResonatorsDict.items():
            freq_data = df['Freq [GHz]']
            y_data = np.imag(df['Y('+str(resonatorIndex+N+1)+','+str(resonatorIndex+N+1)+') [mSie]'].apply(ansysOutputToComplex).astype(complex))
            ax.plot(freq_data, y_data)
            resultsDict['R'+str(resonatorIndex)+"Freq (GHz)"] = fsolve(interp1d(freq_data, y_data), freq_data[0])[0]
        plt.savefig(self.directoryPath / 'Yplots.png')
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
        N = len(self.qArch.allQubitsDict.items())
        for resonatorIndex, resonator in self.qArch.allReadoutResonatorsDict.items():
            node_1 = self.netlistName(resonator.design.pad1.node.name)
            node_2 = self.netlistName(resonator.design.pad2.node.name)
            portsLines += [
                "RPort" + str(resonatorIndex + N) + " " + node_1 + " " + node_2 + " PORTNUM=" + str(
                    resonatorIndex+N) + " RZ=50\n",
                ".PORT " + node_1 + " " + node_2 + " " + str(resonatorIndex+N) + " RPort" + str(
                    resonatorIndex+N) + "\n"]
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
        N=len(self.qArch.allQubitsDict) + len(self.qArch.allReadoutResonatorsDict)
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
            "        \"Y Component:=\"		, ["+    ",".join(["\"Y("+str(i[0]+1)+","+str(i[1]+1)+")\""
                                                                 for i in product(range(N),range(N))])  +"]\n",
            "    ], [])\n",
            (
                    "oModuleReport.ExportToFile(\"Y Parameter Table 1\", r\""
                    + str(self.resultsFilePath)
                    + "\", False)\n"
            )
        ]