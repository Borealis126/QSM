from simulations import *


def L_iQ(qSys, qubitIndex):
    qubit = qSys.allQubitsDict[qubitIndex]
    EC = ECQ(qubitIndex)(qSys).EC
    return 1 / (qubit.omega_i(EC) ** 2 * eConst ** 2 / (2 * EC))


def ZZQ(qSys, q1Index, q2Index):
    QuantizeObj = Quantize(qSys)
    q1QuantizeIndex = QuantizeObj.quantizeIndex(qSys.allQubitsDict[q1Index])
    q2QuantizeIndex = QuantizeObj.quantizeIndex(qSys.allQubitsDict[q2Index])

    stateListFunc = QuantizeObj.stateList

    stateList01 = stateListFunc([[q2QuantizeIndex, 1]])
    stateList10 = stateListFunc([[q1QuantizeIndex, 1]])
    stateList11 = stateListFunc([[q1QuantizeIndex, 1], [q2QuantizeIndex, 1]])

    E11 = QuantizeObj.HEval(stateList11)
    E10 = QuantizeObj.HEval(stateList10)
    E01 = QuantizeObj.HEval(stateList01)

    gz = E11 - E01 - E10

    return gz * 1000  # In MHz


def anharmonicityQ(qSys, qubitIndex):
    QuantizeObj = Quantize(qSys)
    qubit = qSys.allQubitsDict[qubitIndex]

    quantizeIndex = QuantizeObj.quantizeIndex(qubit)

    stateList1 = QuantizeObj.stateList([[quantizeIndex, 1]])
    stateList2 = QuantizeObj.stateList([[quantizeIndex, 2]])

    E1 = QuantizeObj.HEval(stateList1)
    E2 = QuantizeObj.HEval(stateList2)

    return (E2-2*E1)*1000  # In MHz


def quantizedFreqQ(qSys, qubitIndex):
    QuantizeObj = Quantize(qSys)
    return QuantizeObj.HEval(QuantizeObj.stateList([[QuantizeObj.quantizeIndex(qSys.allQubitsDict[qubitIndex]), 1]]))


def quantizedFreqR(qSys, qubitIndex):
    QuantizeObj = Quantize(qSys)
    return QuantizeObj.HEval(QuantizeObj.stateList([
        [QuantizeObj.quantizeIndex(qSys.allReadoutResonatorsDict[qubitIndex]), 1]
    ]))


def dispersiveShiftR(qSys, resonatorIndex):
    QuantizeObj = Quantize(qSys)
    readoutResonator = qSys.allReadoutResonatorsDict[resonatorIndex]
    qubitIndex = resonatorIndex  # Dependent on qubit/resonator pair convention!!!!
    qubit = qSys.allQubitsDict[qubitIndex]

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
