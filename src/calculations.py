from .simulations import *


def L_iQ(qArch, qubitIndex):
    qubit = qArch.allQubitsDict[qubitIndex]
    EC = ECQ(qubitIndex)(qArch).EC
    return 1 / (qubit.omega_i(EC) ** 2 * eConst ** 2 / (2 * EC))


def ZZQ(qArch, q1Index, q2Index):
    QuantizeObj = Quantize(qArch)
    q1QuantizeIndex = QuantizeObj.quantizeIndex(qArch.allQubitsDict[q1Index])
    q2QuantizeIndex = QuantizeObj.quantizeIndex(qArch.allQubitsDict[q2Index])

    stateListFunc = QuantizeObj.stateList

    stateList01 = stateListFunc([[q2QuantizeIndex, 1]])
    stateList10 = stateListFunc([[q1QuantizeIndex, 1]])
    stateList11 = stateListFunc([[q1QuantizeIndex, 1], [q2QuantizeIndex, 1]])

    E11 = QuantizeObj.HEval(stateList11)
    E10 = QuantizeObj.HEval(stateList10)
    E01 = QuantizeObj.HEval(stateList01)

    gz = E11 - E01 - E10

    return gz * 1000  # In MHz


def anharmonicityQ(qArch, qubitIndex):
    QuantizeObj = Quantize(qArch)
    qubit = qArch.allQubitsDict[qubitIndex]

    quantizeIndex = QuantizeObj.quantizeIndex(qubit)

    stateList1 = QuantizeObj.stateList([[quantizeIndex, 1]])
    stateList2 = QuantizeObj.stateList([[quantizeIndex, 2]])

    E1 = QuantizeObj.HEval(stateList1)
    E2 = QuantizeObj.HEval(stateList2)

    return (E2-2*E1)*1000  # In MHz


def quantizedFreqQ(qArch, qubitIndex):
    QuantizeObj = Quantize(qArch)
    return QuantizeObj.HEval(QuantizeObj.stateList([[QuantizeObj.quantizeIndex(qArch.allQubitsDict[qubitIndex]), 1]]))


def quantizedFreqR(qArch, qubitIndex):
    QuantizeObj = Quantize(qArch)
    return QuantizeObj.HEval(QuantizeObj.stateList([
        [QuantizeObj.quantizeIndex(qArch.allReadoutResonatorsDict[qubitIndex]), 1]
    ]))


def dispersiveShiftR(qArch, resonatorIndex):
    QuantizeObj = Quantize(qArch)
    readoutResonator = qArch.allReadoutResonatorsDict[resonatorIndex]
    qubitIndex = resonatorIndex  # Dependent on qubit/resonator pair convention!!!!
    qubit = qArch.allQubitsDict[qubitIndex]

    resonatorQuantizeIndex = QuantizeObj.quantizeIndex(readoutResonator)
    qubitQuantizeIndex = QuantizeObj.quantizeIndex(qubit)

    stateList01 = QuantizeObj.stateList([[qubitQuantizeIndex, 0], [resonatorQuantizeIndex, 1]])
    stateList10 = QuantizeObj.stateList([[qubitQuantizeIndex, 1], [resonatorQuantizeIndex, 0]])
    stateList11 = QuantizeObj.stateList([[qubitQuantizeIndex, 1], [resonatorQuantizeIndex, 1]])

    E00 = 0
    E01 = QuantizeObj.HEval(stateList01)
    E10 = QuantizeObj.HEval(stateList10)
    E11 = QuantizeObj.HEval(stateList11)

    return ((E11 - E10) - (E01 - E00)) * 1000  # In MHz
