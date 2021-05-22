import sys
from pathlib import Path
computeLocation = "Windows"  # Edit this based on where the QSM is being run. Should be "Windows" for most users.
QSMSourceFolder = Path("/beegfs/scratch/joelhoward/QSMSimulations/QSMSource/src")
sys.path.append(str(QSMSourceFolder))
import qubitSimulationModule as QSM
from simulations import *
from calculations import *
projectFolder = Path(__file__).parent.absolute()

# QSM.generateSystemParams(projectFolder)  # First, run just this command to generate the systemParameters file.

# qSys = QSM.initialize(projectFolder, computeLocation, QSMSourceFolder, layoutCompleted=False)

# qSys.generateComponentParams()
# qSys.generateGeometries()
# qSys.generateGDS(addMesh=False)

# HFSSModel(qSys).initialize()
# HFSSModel(qSys).run()

# CapMat(qSys).initialize()
# CapMat(qSys).run()
# CapMat(qSys).postProcess()

# for readoutResonatorIndex, readoutResonator in qSys.allReadoutResonatorsDict.items():
#     LumpedR(readoutResonatorIndex)(qSys).initialize()
# for readoutResonatorIndex, readoutResonator in qSys.allReadoutResonatorsDict.items():
#     LumpedR(readoutResonatorIndex)(qSys).run()
# for readoutResonatorIndex, readoutResonator in qSys.allReadoutResonatorsDict.items():
#     LumpedR(readoutResonatorIndex)(qSys).postProcess()

# CapMatGE(qSys).initialize()
# CapMatGE(qSys).postProcess()

# for qubitIndex, qubit in qSys.allQubitsDict.items():
#     ECQ(qubitIndex)(qSys).initialize()
#     ECQ(qubitIndex)(qSys).postProcess()

# for readoutResonatorIndex,readoutResonator in qSys.allReadoutResonatorsDict.items():
#     ECR(readoutResonatorIndex)(qSys).initialize()
#     ECR(readoutResonatorIndex)(qSys).postProcess()

# Quantize(qSys).initialize()
# Quantize(qSys).postProcess()

# print(ZZQ(qSys, 0, 1))
# print(L_iQ(qSys, 0))
# print(anharmonicityQ(qSys, 0))
# print(dispersiveShiftR(qSys, 0))
