import sys
from pathlib import Path
computeLocation = "Windows"  # Edit this based on where the QSM is being run. Should be "Windows" for most users.
QSMParentFolder = Path(r"C:\Users\jhoward\Desktop")
sys.path.append(str(QSMParentFolder))

import QSM.src.qubitSimulationModule as QSM_init
from QSM.src.simulations import *
from QSM.src.calculations import *
projectFolder = Path(__file__).parent.absolute()
import pytest
from QSM.tests.helpers import copyFile

QSMFolder = QSMParentFolder / 'QSM'
QSMSourceFolder = QSMFolder / 'src'

def test_grounded():
    QSM_init.generateSystemParams(projectFolder)  # First, run just this command to generate the systemParameters file.
    copyFile("systemParameters_reference.json", "systemParameters.json")

    qArch = QSM_init.initialize(projectFolder, computeLocation, QSMSourceFolder, layoutCompleted=False)
    qArch.generateComponentParams()
    copyFile(Path(".") / "componentParameters_reference.json", projectFolder / "componentParameters.json")

    qArch = QSM_init.initialize(projectFolder, computeLocation, QSMSourceFolder, layoutCompleted=False)
    qArch.generateGeometries()
    copyFile(Path(".") / "componentGeometries_reference.json", projectFolder / "componentGeometries.json")
# #
    qArch = QSM_init.initialize(projectFolder, computeLocation, QSMSourceFolder, layoutCompleted=True)
    qArch.generateGDS(addMesh=False)
#
    HFSSModel(qArch).initialize()
    HFSSModel(qArch).run()

    CapMat(qArch).initialize() # -> Normally populate, but use the default values for now.
    CapMat(qArch).run()
    CapMat(qArch).postProcess()

    for readoutResonatorIndex, readoutResonator in qArch.allReadoutResonatorsDict.items():
        LumpedR(readoutResonatorIndex)(qArch).initialize() # -> Populate simParams inside LumpedR folder (defaults are good)

    for readoutResonatorIndex, readoutResonator in qArch.allReadoutResonatorsDict.items():
        LumpedR(readoutResonatorIndex)(qArch).run()
#
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
#
    eta=anharmonicityQ(qArch, 0)
    assert pytest.approx(eta,0.01) == -189.215
