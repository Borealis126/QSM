import sys
from pathlib import Path
computeLocation = "Windows"  # Edit this based on where the QSM is being run. Should be "Windows" for most users.
QSMSourceFolder = Path(r"C:\Users\jhoward\Desktop\QSM\src")
sys.path.append(str(QSMSourceFolder))
import qubitSimulationModule as QSM
from simulations import *
from calculations import *
from BBQ import *
projectFolder = Path(__file__).parent.absolute()
import subprocess
import pytest

"""Start here. Uncomment the following line and run this file."""
def copyFile(sourceFile, destinationFile):
    copyCommand = ""
    if computeLocation == "Windows":
        copyCommand = "copy " + str(Path(sourceFile)) + " " + str(Path(destinationFile))
    if computeLocation == "Cluster":
        copyCommand = "cp " + str(Path(sourceFile)) + " " + str(Path(destinationFile))
    subprocess.call(copyCommand, shell=True)

def test_example():
    copyDir = projectFolder / ".." / "Example" / "TwoQubit"
    QSM.generateSystemParams(projectFolder)  # First, run just this command to generate the systemParameters file.
    copyFile(copyDir / "systemParameters_reference.json", projectFolder / "systemParameters.json")

    qArch = QSM.initialize(projectFolder, computeLocation, QSMSourceFolder, layoutCompleted=False)
    qArch.generateComponentParams()
    copyFile(copyDir / "componentParameters_reference.json", projectFolder / "componentParameters.json")

    qArch = QSM.initialize(projectFolder, computeLocation, QSMSourceFolder, layoutCompleted=False)
    qArch.generateGeometries()
    copyFile(copyDir / "componentGeometries_reference.json", projectFolder / "componentGeometries.json")

    qArch = QSM.initialize(projectFolder, computeLocation, QSMSourceFolder, layoutCompleted=True)
    qArch.generateGDS(addMesh=False)

    HFSSModel(qArch).initialize()
    HFSSModel(qArch).run()

    CapMat(qArch).initialize() # -> Normally populate, but use the default values for now.
    CapMat(qArch).run()
    CapMat(qArch).postProcess()

    for readoutResonatorIndex, readoutResonator in qArch.allReadoutResonatorsDict.items():
        LumpedR(readoutResonatorIndex)(qArch).initialize() # -> Populate simParams inside LumpedR folder (defaults are good)

    for readoutResonatorIndex, readoutResonator in qArch.allReadoutResonatorsDict.items():
        LumpedR(readoutResonatorIndex)(qArch).run()

    for readoutResonatorIndex, readoutResonator in qArch.allReadoutResonatorsDict.items():
        LumpedR(readoutResonatorIndex)(qArch).postProcess()
#
    CapMatGE(qArch).initialize()
    CapMatGE(qArch).postProcess()
# #
    for qubitIndex, qubit in qArch.allQubitsDict.items():
        ECQ(qubitIndex)(qArch).initialize()  # Only creates directory, no simParams file.
        ECQ(qubitIndex)(qArch).postProcess()

    for readoutResonatorIndex,readoutResonator in qArch.allReadoutResonatorsDict.items():
        ECR(readoutResonatorIndex)(qArch).initialize()
        ECR(readoutResonatorIndex)(qArch).postProcess()
# #
    Quantize(qArch).initialize() # -> Populate
    Quantize(qArch).postProcess()

    ZZ = ZZQ(qArch, 0, 1)
    assert pytest.approx(ZZ,0.01) == -3.0337461563902934

"""Congrats! You have simulated a 2-qubit system. If you don't like any calculated values, you can go back and
tweak any of your layout files and restart the process. """
