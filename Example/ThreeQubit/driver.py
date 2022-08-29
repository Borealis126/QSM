import sys
from pathlib import Path
computeLocation = "Windows"  # Edit this based on where the QSM is being run. Should be "Windows" for most users.
QSMSourceFolder = Path(r"C:\Users\jhoward\Desktop\QSM\src")
sys.path.append(str(QSMSourceFolder))
import qubitSimulationModule as QSM
from simulations import *
from calculations import *
projectFolder = Path(__file__).parent.absolute()

"""Start here. Uncomment the following line and run this file."""
# QSM.generateSystemParams(projectFolder)  # First, run just this command to generate the systemParameters file.

"""Now populate the system parameters (see reference jsons)"""

"""Next run the following two lines (re-commenting previous commands):"""
# qArch = QSM.initialize(projectFolder, computeLocation, QSMSourceFolder, layoutCompleted=False)
# qArch.generateComponentParams()

"""Populate the component parameters"""

"""Next run the following two lines"""
# qArch = QSM.initialize(projectFolder, computeLocation, QSMSourceFolder, layoutCompleted=False)
# qArch.generateGeometries()

"""Populate the geometries. Once finished the architecture is fully specified."""

"""Check out the GDS:"""
qArch = QSM.initialize(projectFolder, computeLocation, QSMSourceFolder, layoutCompleted=True)
qArch.generateGDS(addMesh=False)

"""Generate the HFSS model"""
# qArch = QSM.initialize(projectFolder, computeLocation, QSMSourceFolder, layoutCompleted=True)
# HFSSModel(qArch).initialize()
# HFSSModel(qArch).run()

"""You may notice that we keep calling QSM.initialize. This is because after systemParameters is populated, this
needs to be run before every command. Once geometries are completed (i.e., now) switch layoutCompleted to True"""

"""Now uncomment this and leave it uncommented."""
# qArch = QSM.initialize(projectFolder, computeLocation, QSMSourceFolder, layoutCompleted=True)

"""Run the following analyses"""

# CapMat(qArch).initialize() # -> Normally populate, but use the default values for now.
# CapMat(qArch).run()
# CapMat(qArch).postProcess()
# #
# for readoutResonatorIndex, readoutResonator in qArch.allReadoutResonatorsDict.items():
#     LumpedR(readoutResonatorIndex)(qArch).initialize() # -> Populate simParams inside LumpedR folder (defaults are good)
#
# for readoutResonatorIndex, readoutResonator in qArch.allReadoutResonatorsDict.items():
#     LumpedR(readoutResonatorIndex)(qArch).run()

"""From here through Quantize initialize everything can be run at once since there is no
json populating or ansys simulations."""
# for readoutResonatorIndex, readoutResonator in qArch.allReadoutResonatorsDict.items():
#     LumpedR(readoutResonatorIndex)(qArch).postProcess()
#
# CapMatGE(qArch).initialize()
# CapMatGE(qArch).postProcess()
# #
# for qubitIndex, qubit in qArch.allQubitsDict.items():
#     ECQ(qubitIndex)(qArch).initialize()  # Only creates directory, no simParams file.
#     ECQ(qubitIndex)(qArch).postProcess()
#
# for readoutResonatorIndex,readoutResonator in qArch.allReadoutResonatorsDict.items():
#     ECR(readoutResonatorIndex)(qArch).initialize()
#     ECR(readoutResonatorIndex)(qArch).postProcess()
# #
# Quantize(qArch).initialize() # -> Populate
# Quantize(qArch).postProcess()
#
# print('ZZ (MHz):'+str(round(ZZQ(qArch, 0, 1), 3)))
#
# print('L_iQ0 (nH):'+str(round(L_iQ(qArch, 0)*1e9, 3)))
# print('L_iQ1 (nH):'+str(round(L_iQ(qArch, 1)*1e9, 3)))
#
# print('alpha_Q0 (MHz):'+str(round(anharmonicityQ(qArch, 0), 3)))
# print('alpha_Q1 (MHz):'+str(round(anharmonicityQ(qArch, 1), 3)))
#
# print('Chi_R0 (MHz):'+str(round(dispersiveShiftR(qArch, 0)*1e3, 3)))
# print('Chi_R1 (MHz):'+str(round(dispersiveShiftR(qArch, 1)*1e3, 3)))

"""Congrats! You have simulated a 2-qubit system. If you don't like any calculated values, you can go back and
tweak any of your layout files and restart the process. """
