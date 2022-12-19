import sys
from pathlib import Path
computeLocation = "Windows"  # Edit this based on where the QSM is being run. Should be "Windows" for most users.
QSMParentFolder = Path(r"C:\Users\jhoward\Desktop")
sys.path.append(str(QSMParentFolder))

import QSM.src.qubitSimulationModule as QSM_init
from QSM.src.simulations import *
from QSM.src.calculations import *
from QSM.src.BBQ import BBQ
projectFolder = Path(__file__).parent.absolute()
import subprocess

QSMFolder = QSMParentFolder / 'QSM'
QSMSourceFolder = QSMFolder / 'src'

"""Start here. Uncomment the following line and run this file."""
# QSM_init.generateSystemParams(projectFolder)  # First, run just this command to generate the systemParameters file.

"""Now populate the system parameters (see reference jsons)"""

"""Next run the following two lines (re-commenting previous commands):"""
# qArch = QSM_init.initialize(projectFolder, computeLocation, QSMSourceFolder, layoutCompleted=False)
# qArch.generateComponentParams()

"""Populate the component parameters"""

"""Next run the following two lines"""
# qArch = QSM_init.initialize(projectFolder, computeLocation, QSMSourceFolder, layoutCompleted=False)
# qArch.generateGeometries()

"""Populate the geometries. Once finished the architecture is fully specified."""

"""Check out the GDS:"""
# qArch = QSM_init.initialize(projectFolder, computeLocation, QSMSourceFolder, layoutCompleted=True)
# qArch.generateGDS(addMesh=False)

"""Generate the HFSS model"""
# qArch = QSM_init.initialize(projectFolder, computeLocation, QSMSourceFolder, layoutCompleted=True)
# HFSSModel(qArch).initialize()
# HFSSModel(qArch).run()

"""You may notice that we keep calling QSM.initialize. This is because after systemParameters is populated, this
needs to be run before every command. Once geometries are completed (i.e., now) switch layoutCompleted to True"""

"""Now uncomment this and leave it uncommented."""
# qArch = QSM_init.initialize(projectFolder, computeLocation, QSMSourceFolder, layoutCompleted=True)

"""Run the following analyses"""

# CapMat(qArch).initialize() # -> Normally populate, but use the default values for now.
# CapMat(qArch).run()
# CapMat(qArch).postProcess()

# BBQ(qArch).initialize()
# BBQ(qArch).run()
# BBQ(qArch).postProcess()

"""Congrats! You have simulated a 2-qubit system. If you don't like any calculated values, you can go back and
tweak any of your layout files and restart the process. """
