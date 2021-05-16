#Import modules
import sys
import os
computeLocation="Windows" # Edit this based on where the QSM is being run. Users at NIST should use "68707Max"
QSMSourceFolder="O:/68707/JoelHoward/ChipDesign/QSMSource/"
sys.path.append(QSMSourceFolder)
import qubitSimulationModule as QSM
projectFolder = Path(os.path.dirname(os.path.abspath( __file__ )))

# QSM.generateSystemParams(projectFolder)#Run this command to generate the systemParameters file.

# Once systemParameters is available and filled out, ALWAYS run this command first.
qSys = QSM.initialize(projectFolder,computeLocation,QSMSourceFolder)

# Generate and populate these sequentially.
# qSys.generateComponentParams()
# qSys.generateGeometries()

# qSys.loadDesignFiles() # Once geometries is populated ALWAYS run this after QSM.initialize

# qSys.generateGDS() #Optional to view layout.

# Run these sequentially. Populate simParams file after initialize().
# CapMatSimulation(qSys).initialize()
# CapMatSimulation(qSys).run()
# CapMatSimulation(qSys).postProcess()

# for readoutResonatorIndex, readoutResonator in qSys.allReadoutResonatorsDict.items():
    # LumpedRSim(readoutResonatorIndex)(qSys).initialize()
    # LumpedRSim(readoutResonatorIndex)(qSys).run()
    # LumpedRSim(readoutResonatorIndex)(qSys).postProcess()

# CapMatGESimulation(qSys).postProcess()

# for qubitIndex, qubit in qSys.allQubitsDict.items():
#     ECQSim(qubitIndex)(qSys).postProcess()
# for readoutResonatorIndex,readoutResonator in qSys.allReadoutResonatorsDict.items():
#     ECRSim(readoutResonatorIndex)(qSys).postProcess()

# Quantize(qSys).initialize()
# Quantize(qSys).postProcess()

# ZZQCalc(qSys, 0, 1)
