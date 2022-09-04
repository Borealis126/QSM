import sys
from pathlib import Path
computeLocation = "Windows"  # Edit this based on where the QSM is being run. Should be "Windows" for most users.
QSMParentFolder = Path(r"C:\Users\jhoward\Desktop")
sys.path.append(str(QSMParentFolder))

import QSM.src.qubitSimulationModule as QSM_init
from QSM.src.simulations import *
from QSM.src.calculations import *
projectFolder = Path(__file__).parent.absolute()
import subprocess
import pytest
from QSM.tests.helpers import copyFile

QSMFolder = QSMParentFolder / 'QSM'
QSMSourceFolder = QSMFolder / 'src'

def test_example():
    copyDir = QSMFolder / "Example" / "TwoQubit"
    QSM_init.generateSystemParams(projectFolder)  # First, run just this command to generate the systemParameters file.
    copyFile(copyDir / "systemParameters_reference.json", projectFolder / "systemParameters.json")

    qArch = QSM_init.initialize(projectFolder, computeLocation, QSMSourceFolder, layoutCompleted=False)
    qArch.generateComponentParams()
    copyFile(copyDir / "componentParameters_reference.json", projectFolder / "componentParameters.json")
#
    qArch = QSM_init.initialize(projectFolder, computeLocation, QSMSourceFolder, layoutCompleted=False)
    qArch.generateGeometries()
    copyFile(copyDir / "componentGeometries_reference.json", projectFolder / "componentGeometries.json")

    qArch = QSM_init.initialize(projectFolder, computeLocation, QSMSourceFolder, layoutCompleted=True)
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
