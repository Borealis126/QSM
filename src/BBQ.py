from .circuitSimulations import CircuitSim, S21_params
from .simulations import Simulation, CapMat
from copy import deepcopy
from itertools import product
import pandas as pd
import numpy as np
from .ansysAPI import ansysOutputToComplex
from scipy.interpolate import interp1d
from scipy.optimize import fsolve
import qutip as qt
from .constants import hbarConst, GHzToOmega, Joules_To_GHz, Phi_0Const
from scipy.misc import derivative


class BBQ(Simulation):
    def __init__(self, qArch):
        super().__init__(qArch, "BBQ")
        self.Y_BBQ_SimName = "Y_BBQ"
        CapMatObj = CapMat(self.qArch)
        self.circuitSims = {self.Y_BBQ_SimName: Y_BBQ_Simulation(self.directoryPath, qArch, CapMatObj)}

    def initialize(self):
        simParamsDict = S21_params

        quantizeList = "["
        for qubitIndex, qubit in self.qArch.allQubitsDict.items():
            quantizeList += qubit.name + ":"
        for resonatorIndex, resonator in self.qArch.allReadoutResonatorsDict.items():
            quantizeList += resonator.name + ":"
        quantizeList = quantizeList[0:-1] + "]"
        simParamsDict.update({"QuantizeList": quantizeList, "NumResonatorPhotons": 5, "NumQubitPhotons": 5})
        self.generateParams(simParamsDict)

    def run(self):
        self.runAllSims()

    def postProcess(self):
        self.deleteUnneededFiles()
        df = pd.read_csv(self.circuitSims[self.Y_BBQ_SimName].resultsFilePath,
                         dtype=str).applymap(ansysOutputToComplex).astype(complex)
        omegas = df['Freq [GHz]'].astype(float) * GHzToOmega
        num_qubits_all = len(self.qArch.allQubitsDict)
        num_resonators_all = len(self.qArch.allReadoutResonatorsDict)
        num_components_all = num_qubits_all + num_resonators_all

        quantize_list = [str(i) for i in self.simParams["QuantizeList"][1:-1].split(":")]
        qubits_dict = {key: val for key, val in self.qArch.allQubitsDict.items() if val.name in quantize_list}
        resonators_dict = {key: val for key, val in self.qArch.allReadoutResonatorsDict.items() if val.name in quantize_list}
        num_qubits = len(qubits_dict)
        num_resonators = len(resonators_dict)
        num_components = num_qubits + num_resonators

        qubit_indices = {key: {"tensor": len([q for q in qubits_dict.values() if q.index < val.index]),
                               "component": val.index}
                                   for key, val in qubits_dict.items()}
        resonator_indices = {key: {"tensor": len([r for r in resonators_dict.values() if r.index < val.index]) + num_qubits,
                                   "component": val.index + num_qubits_all}
                                       for key, val in resonators_dict.items()}
        component_indices = deepcopy(qubit_indices)
        component_indices.update(resonator_indices)

        Y = np.empty((len(omegas), num_components_all, num_components_all), dtype=complex)
        for w in range(len(omegas)):
            for i in range(num_components_all):
                for j in range(num_components_all):
                    Y[w, i, j] = df['Y(' + str(i + 1) + ',' + str(j + 1) + ') [mSie]'][w] * 1e-3  # Convert to Sie
        Z = np.array([np.linalg.inv(Y[w, :, :]) for w in range(len(omegas))])

        Y_interp = np.array(
            [[interp1d(omegas, Y[:, i, j]) for i in range(num_components_all)] for j in range(num_components_all)])
        Z_interp = np.array(
            [[interp1d(omegas, Z[:, i, j]) for i in range(num_components_all)] for j in range(num_components_all)])

        N_Q = self.simParams["NumQubitPhotons"]
        N_R = self.simParams["NumResonatorPhotons"]
        k = 1
        print("Calculating omegas")
        omega_ps = [fsolve(lambda x: np.imag(Y_interp[i, i](x)), omegas[0])[0] for i in range(num_components_all)]

        print("Calculating Z_kp_effs")
        Z_kp_effs = [2 / (omega_ps[p] * np.imag(derivative(Y_interp[k, k], omega_ps[p], omegas[1] - omegas[0])))
                     for p in range(num_components_all)]

        #Now we only consider the components in QuantizeList
        a_s = [qt.tensor([qt.qeye(N_Q)] * val["tensor"] + [qt.destroy(N_Q)] + [qt.qeye(N_Q)] * (num_qubits - val["tensor"] - 1) + [
            qt.qeye(N_R)] * num_resonators)
               for key, val in qubit_indices.items()] + \
              [qt.tensor([qt.qeye(N_Q)] * num_qubits + [qt.qeye(N_R)] * (val["tensor"]-num_qubits) + [qt.destroy(N_R)] + [qt.qeye(N_R)] * (
                          num_resonators + num_qubits - val["tensor"] - 1))
               for key, val in resonator_indices.items()]

        phi_ells = [sum([Z_interp[val2["component"], k](omega_ps[val["component"]]) / Z_interp[k, k](omega_ps[val["component"]]) * np.sqrt(1 / 2 * Z_kp_effs[val["component"]]) * (
                a_s[val["tensor"]] + a_s[val["tensor"]].dag())
                         for key, val in component_indices.items()])
                    for key2, val2 in qubit_indices.items()]

        print("Calculating H")
        H_0 = sum([omega_ps[val["component"]] * Joules_To_GHz * a_s[val["tensor"]].dag() * a_s[val["tensor"]]
                   for key, val in component_indices.items()]) * hbarConst

        H_nl = sum([-phi_ells[val["tensor"]] ** 4 / (24 * Phi_0Const ** 2 * self.qArch.allQubitsDict[key].LJ)
                    for key, val in qubit_indices.items()]) * Joules_To_GHz * hbarConst ** 2
        H = H_0 + H_nl

        print("Calculating eigenenergies")

        print("H0 eigenenergies:")
        print(H_0.eigenenergies()[0:10])

        eigs = H.eigenenergies()
        eigs_zeroed = np.real(eigs - eigs[0])
        print("H eigenenergies:")
        print(eigs_zeroed[0:10])
        qt.qsave(H, self.directoryPath / 'hamiltonian')
        np.savetxt(self.directoryPath / "eigenvalues.csv", eigs_zeroed, delimiter=",")


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
            if len(qubit.design.padList) == 1:  # if grounded
                node_2 = self.netlistName("G")
            else:
                node_2 = self.netlistName(qubit.design.pad2.node.name)
            port_index = qubitIndex + 1
            portsLines += [
                "RPort" + str(port_index) + " " + node_1 + " " + node_2 + " PORTNUM=" + str(
                    port_index) + " RZ=50\n",
                ".PORT " + node_1 + " " + node_2 + " " + str(port_index) + " RPort" + str(
                    port_index) + "\n"]
        N = len(self.qArch.allQubitsDict.items())
        for resonatorIndex, resonator in self.qArch.allReadoutResonatorsDict.items():
            node_1 = self.netlistName(resonator.design.pad1.node.name)
            node_2 = self.netlistName(resonator.design.pad2.node.name)
            port_index = resonatorIndex + N + 1
            portsLines += [
                "RPort" + str(port_index) + " " + node_1 + " " + node_2 + " PORTNUM=" + str(
                    port_index) + " RZ=50\n",
                ".PORT " + node_1 + " " + node_2 + " " + str(port_index) + " RPort" + str(
                    port_index) + "\n"]
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
        N = len(self.qArch.allQubitsDict) + len(self.qArch.allReadoutResonatorsDict)
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
            "        \"Y Component:=\"		, [" + ",".join(["\"Y(" + str(i[0] + 1) + "," + str(i[1] + 1) + ")\""
                                                               for i in product(range(N), range(N))]) + "]\n",
            "    ], [])\n",
            (
                    "oModuleReport.ExportToFile(\"Y Parameter Table 1\", r\""
                    + str(self.resultsFilePath)
                    + "\", False)\n"
            )
        ]
