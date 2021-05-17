from simulations import *


def ZZQCalc(qSys, q1Index, q2Index):
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

    print("E11 (GHz):", E11)
    print("E10 (GHz):", E10)
    print("E01 (GHz):", E01)

    gz = E11 - E01 - E10

    print("gz" + str(q1Index) + "-" + str(q2Index) + "(MHz): ", gz * 1000)
