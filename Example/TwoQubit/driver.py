import sys
from pathlib import Path
computeLocation = "Windows"  # Edit this based on where the QSM is being run. Should be "Windows" for most users.
QSMSourceFolder = Path(r"O:\68707\JoelHoward\ChipDesign\QSMSource_v2\QSM\src")
sys.path.append(str(QSMSourceFolder))
import qubitSimulationModule as QSM
from simulations import *
from calculations import *
projectFolder = Path(__file__).parent.absolute()

"""Start here. Uncomment the following line and run this file."""
# QSM.generateSystemParams(projectFolder)  # First, run just this command to generate the systemParameters file.

"""Now populate the system parameters (see reference jsons)"""

"""Next run the following two lines (re-commenting previous commands):"""
# qSys = QSM.initialize(projectFolder, computeLocation, QSMSourceFolder, layoutCompleted=False)
# qSys.generateComponentParams()

"""Populate the component parameters"""

"""Next run the following two lines"""
# qSys = QSM.initialize(projectFolder, computeLocation, QSMSourceFolder, layoutCompleted=False)
# qSys.generateGeometries()

"""Populate the geometries"""

"""Check out the GDS:"""
# qSys = QSM.initialize(projectFolder, computeLocation, QSMSourceFolder, layoutCompleted=True)
# qSys.generateGDS(addMesh=False)

"""Generate the HFSS model"""
# qSys = QSM.initialize(projectFolder, computeLocation, QSMSourceFolder, layoutCompleted=True)
# HFSSModel(qSys).initialize()
# HFSSModel(qSys).run()

"""Populate the generated file. The layout phase is now done and analyses can be performed."""
"""You may notice that we keep calling QSM.initialize. This is because after systemParameters is populated, this
needs to be run before every command. Once geometries are completed (i.e., now) switch layoutCompleted to True"""

"""Now uncomment this and leave it uncommented."""
# qSys = QSM.initialize(projectFolder, computeLocation, QSMSourceFolder, layoutCompleted=True)

"""Run the following analyses"""

# CapMat(qSys).initialize() # -> Normally populate, but use the default values for now.
# CapMat(qSys).run()
# CapMat(qSys).postProcess()

# for readoutResonatorIndex, readoutResonator in qSys.allReadoutResonatorsDict.items():
    # LumpedR(readoutResonatorIndex)(qSys).initialize() # -> Populate the simParams inside the LumpedR folder.

# for readoutResonatorIndex, readoutResonator in qSys.allReadoutResonatorsDict.items():
    # LumpedR(readoutResonatorIndex)(qSys).run()

"""From here through Quantize initialize everything can be run at once since there is no
json populating or ansys simulations."""
# for readoutResonatorIndex, readoutResonator in qSys.allReadoutResonatorsDict.items():
    # LumpedR(readoutResonatorIndex)(qSys).postProcess()

# CapMatGE(qSys).initialize()
# CapMatGE(qSys).postProcess()

# for qubitIndex, qubit in qSys.allQubitsDict.items():
    # ECQ(qubitIndex)(qSys).initialize()  # Only creates directory, no simParams file.
    # ECQ(qubitIndex)(qSys).postProcess()

# for readoutResonatorIndex,readoutResonator in qSys.allReadoutResonatorsDict.items():
    # ECR(readoutResonatorIndex)(qSys).initialize()
    # ECR(readoutResonatorIndex)(qSys).postProcess()

# Quantize(qSys).initialize() # -> Populate
# Quantize(qSys).postProcess()

# print(ZZQ(qSys, 0, 1))

# print(L_iQ(qSys, 0))

# print(anharmonicityQ(qSys, 0))

# print(dispersiveShiftR(qSys, 0))

"""Congrats! You have simulated a 2-qubit system. If you don't like any calculated values, you can go back and
tweak any of your layout files and restart the process. """
