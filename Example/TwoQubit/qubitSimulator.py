import sys
from pathlib import Path
import subprocess
import os

computeLocation = "Cluster"  # Edit this based on where the QSM is being run. Users at NIST should use "68707Max"
QSMSourceFolder = Path("/beegfs/scratch/joelhoward/QSMSimulations/QSMSource/src")
sys.path.append(str(QSMSourceFolder))
import qubitSimulationModule as QSM
from simulations import *

projectFolder = Path(os.path.dirname(os.path.abspath(__file__)))
copyDir = projectFolder / ".." / "TwoQubit_filesToCopy"

#-----------------------------------------------------------------------------------------------


# QSM.generateSystemParametersFile(projectFolder)  # Run this command only once generate the systemParameters file.
qSys = QSM.initialize(projectFolder, computeLocation, QSMSourceFolder)#Always run this once systemParams is populated.


# qSys.generateComponentParams()
# qSys.generateGeometries()
qSys.loadDesignFiles()

# qSys.generateGDS()

# CapMatSimulation(qSys).initialize()
# CapMatSimulation(qSys).run()
# CapMatSimulation(qSys).postProcess()

# for readoutResonatorIndex,readoutResonator in qSys.allReadoutResonatorsDict.items():
#     LumpedRSimulation(qSys,readoutResonatorIndex).initialize()
#     LumpedRSimulation(qSys,readoutResonatorIndex).run()
#     LumpedRSimulation(qSys,readoutResonatorIndex).postProcess()

# CapMatGESimulation(qSys).initialize()
# CapMatGESimulation(qSys).postProcess()

# for qubitIndex,qubit in qSys.allQubitsDict.items():
#     ECQSimulation(qSys,qubitIndex).initialize()
#     ECQSimulation(qSys,qubitIndex).postProcess()

# for readoutResonatorIndex,readoutResonator in qSys.allReadoutResonatorsDict.items():
#     ECRSimulation(qSys,readoutResonatorIndex).initialize()
#     ECRSimulation(qSys,readoutResonatorIndex).postProcess()

Quantize(qSys).initialize()
Quantize(qSys).postProcess()

# ZZQSimulation(qSys,0,1).initialize()
# ZZQSimulation(qSys,0,1).postProcess()