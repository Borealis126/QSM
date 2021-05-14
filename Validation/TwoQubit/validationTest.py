import sys
from pathlib import Path
import subprocess
import os


computeLocation = "Cluster"  # Edit this based on where the QSM is being run. Users at NIST should use "68707Max"
QSMSourceFolder = ""
if computeLocation == "Windows":
    QSMSourceFolder = Path("O:/68707/JoelHoward/ChipDesign/QSMSource/src")
elif computeLocation == "Cluster":
    QSMSourceFolder = Path("/beegfs/scratch/joelhoward/QSMSimulations/QSMSource/src")
sys.path.append(str(QSMSourceFolder))
import qubitSimulationModule as QSM
from simulations import *

projectFolder = Path(os.path.dirname(os.path.abspath(__file__)))
copyDir = projectFolder / ".." / "TwoQubit_filesToCopy"

def copyFile(sourceFile, destinationFile):
    copyCommand = ""
    if computeLocation == "Windows":
        copyCommand = "copy " + str(Path(sourceFile)) + " " + str(Path(destinationFile))
    if computeLocation == "Cluster":
        copyCommand = "cp " + str(Path(sourceFile)) + " " + str(Path(destinationFile))
    subprocess.call(copyCommand, shell=True)

# QSM.generateSystemParametersFile(projectFolder)  # Run this command to generate the systemParameters file.
# copyFile(copyDir / "systemParametersFile.csv", projectFolder / "systemParametersFile.csv")
#
qSys = QSM.initialize(projectFolder, computeLocation, QSMSourceFolder)  # Once systemParameters is available and filled out, ALWAYS run this command first.
# qSys.loadGeometries()

# qSys.generateComponentParams()
# copyFile(copyDir/"componentParametersFile.csv",projectFolder/"componentParametersFile.csv")
#
# qSys.generateGeometries()
# copyFile(copyDir/"componentGeometriesFile.csv",projectFolder/"componentGeometriesFile.csv")


qSys.generateGDS()
# #
# CapMatSimulation(qSys).initialize()
# CapMatSimulation(qSys).run()

# CapMatSimulation(qSys).postProcess()

# copyFile(copyDir/"capMat"/"SimulationParameters.csv",projectFolder/"capMat"/"SimulationParameters.csv")


# qSys.loadDesignFiles()
# for readoutResonatorIndex,readoutResonator in qSys.allReadoutResonatorsDict.items():
    # LumpedRSimulation(qSys,readoutResonatorIndex).initialize()
    # LumpedRSimulation(qSys,readoutResonatorIndex).run()
    # LumpedRSimulation(qSys,readoutResonatorIndex).postProcess()

# CapMatGESimulation(qSys).initialize()
# CapMatGESimulation(qSys).postProcess()


# qSys.loadDesignFiles()
# for qubitIndex,qubit in qSys.allQubitsDict.items():
#     ECQSimulation(qSys,qubitIndex).initialize()
#     ECQSimulation(qSys,qubitIndex).postProcess()

# qSys.loadDesignFiles()
# for readoutResonatorIndex,readoutResonator in qSys.allReadoutResonatorsDict.items():
#     ECRSimulation(qSys,readoutResonatorIndex).initialize()
#     ECRSimulation(qSys,readoutResonatorIndex).postProcess()



# Quantize(qSys).initialize()
# Quantize(qSys).postProcess()

# ZZQSimulation(qSys,0,1).initialize()

# ZZQSimulation(qSys,0,1).postProcess()

# qSys.simulationCommand(["simulation","quantize","postProcess"])
# qSys.simulationCommand(["simulation","zzQ0-1","postProcess"])

# for qubitIndex,qubit in qSys.allQubitsDict.items():
# qSys.simulationCommand(["simulation","anharmonicityQ"+str(qubitIndex),"init"])
# qSys.simulationCommand(["simulation","anharmonicityQ"+str(qubitIndex),"postProcess"])

# for readoutResonatorIndex, readoutResonator in qSys.allReadoutResonatorsDict.items():
#     qSys.simulationCommand(["simulation", "dispersiveShiftR" + str(readoutResonatorIndex), "init"])
#     qSys.simulationCommand(["simulation", "dispersiveShiftR" + str(readoutResonatorIndex), "postProcess"])

# SIMULATION COMMANDS
# -----------------------------------------------------------------------------------------------------------
# CAPACITANCE MATRIX
# ["simulation","capMat",{"init","run","postProcess"}]
# -----------------------------------------------------------------------------------------------------------
# CIRCUIT SIMULATIONS
# ["simulation","fullS21",{"init","run","postProcess"}]

# ["simulation","freqQ[N]",{"init","run","postProcess"}]
# ["simulation","decayQ[N]",{"init","run","postProcess"}]
# ["simulation","exchQ[N1]-[N2]",{"init","run"}] e.g. ["simulation","exchQ0-2","run"]

# ["simulation","freqR[N]",{"init","run","postProcess"}]
# ["simulation","lumpedR[N]",{"init","run","postProcess"}]
# ["simulation","feedlineCouplingR[N]",{"init","run","postProcess"}]#Depends on results of freqQ[N]

# Helper commands:
# "initAllSims"
# "runAllSims"
# "postProcessAllSims"
# -----------------------------------------------------------------------------------------------------------
# AFTER CIRCUIT SIMULATIONS
# ["simulation","capMatGE",{"init","postProcess"}]
# ["simulation","ECQ[N]",{"init","postProcess"}]#Depends on results of capMatGE
# ["simulation","L_iQ[N]",{"init","postProcess"}]#Check how closely this agrees with L_i in the component parameters file. Depends on EC

# Helper commands:
# "GEPlusAllEC": runs init/postprocess for capMatGE and all ECQ
# "AllL_i"
# -----------------------------------------------------------------------------------------------------------
# QUANTIZATION
# ["simulation","quantize",{"init","postProcess"}]#Depends on results of all lumpedR
# -----------------------------------------------------------------------------------------------------------
# POST-QUANTIZATION
# ["simulation","zzQ[m]-[n]",{"init","postProcess"}]# i.e. zzQ0-1
# ["simulation","anharmonicityQ[N]",{"init","postProcess"}]
# ["simulation","dispersiveShiftR[N]",{"init","postProcess"}]

# Helper commands:
# "Allzz"
# "AllAnharmonicityQ"
# -----------------------------------------------------------------------------------------------------------
