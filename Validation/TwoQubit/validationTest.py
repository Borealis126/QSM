import sys
from pathlib import Path
import subprocess

computeLocation = "Windows"  # Edit this based on where the QSM is being run. Users at NIST should use "68707Max"
QSMSourceFolder = ""
if computeLocation == "Windows":
    QSMSourceFolder = Path("../../src")
elif computeLocation == "Cluster":
    QSMSourceFolder = Path("/beegfs/scratch/joelhoward/QSMSimulations/QSMSource/src")
sys.path.append(str(QSMSourceFolder))
import qubitSimulationModule as QSM
from simulations import *
from calculations import *

projectFolder = Path(__file__).parent.absolute()
copyDir = projectFolder / ".." / ".." / "Example" / "TwoQubit"


def copyFile(sourceFile, destinationFile):
    copyCommand = ""
    if computeLocation == "Windows":
        copyCommand = "copy " + str(Path(sourceFile)) + " " + str(Path(destinationFile))
    if computeLocation == "Cluster":
        copyCommand = "cp " + str(Path(sourceFile)) + " " + str(Path(destinationFile))
    subprocess.call(copyCommand, shell=True)


# QSM.generateSystemParams(projectFolder)  # Run this command to generate the systemParameters file.
# copyFile(copyDir / "systemParameters.csv", projectFolder / "systemParameters.csv")

# Once systemParameters is available and filled out, ALWAYS run this command first.
qSys = QSM.initialize(projectFolder, computeLocation, QSMSourceFolder, layoutCompleted=True)

# qSys.generateComponentParams()
# copyFile(copyDir/"componentParameters.json", projectFolder/"componentParameters.json")
#
# qSys.generateGeometries()
# copyFile(copyDir/"componentGeometries.json", projectFolder/"componentGeometries.json")

# qSys.generateGDS(addMesh=False)

# HFSSModel(qSys).initialize()
# HFSSModel(qSys).run()


# CapMat(qSys).initialize()
# CapMat(qSys).run()
# CapMat(qSys).postProcess()

# for readoutResonatorIndex, readoutResonator in qSys.allReadoutResonatorsDict.items():
#     LumpedR(readoutResonatorIndex)(qSys).initialize()
#     LumpedR(readoutResonatorIndex)(qSys).run()
#     LumpedR(readoutResonatorIndex)(qSys).postProcess()

CapMatGE(qSys).initialize()
CapMatGE(qSys).postProcess()
#
for qubitIndex, qubit in qSys.allQubitsDict.items():
    ECQ(qubitIndex)(qSys).initialize()
    ECQ(qubitIndex)(qSys).postProcess()

for readoutResonatorIndex,readoutResonator in qSys.allReadoutResonatorsDict.items():
    ECR(readoutResonatorIndex)(qSys).initialize()
    ECR(readoutResonatorIndex)(qSys).postProcess()
#

Quantize(qSys).initialize()
Quantize(qSys).postProcess()

print(ZZQ(qSys, 0, 1))
#
# print(L_iQ(qSys, 0))
#
# print(anharmonicityQ(qSys, 0))
#
# print(dispersiveShiftR(qSys, 0))
