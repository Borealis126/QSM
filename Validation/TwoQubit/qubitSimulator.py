#Import modules
import sys
import os
computeLocation="Wendian"#Edit this based on where the QSM is being run. Users at NIST should use "68707Max"
QSMSourceFolder=""
if computeLocation=="68707Max":
    QSMSourceFolder="O:/68707/JoelHoward/ChipDesign/QSMSource/"
elif computeLocation=="Wendian":
    QSMSourceFolder="/beegfs/scratch/joelhoward/QSMSimulations/QSMSource/"
sys.path.append(QSMSourceFolder)
import qubitSimulationModule as QSM

projectPath=os.path.dirname(os.path.abspath( __file__ ))
projectFolder=projectPath.replace("\\","/")

#QSM.generateSystemParametersFile(projectFolder)#Run this command to generate the systemParameters file.

#qSys=QSM.initialize(projectFolder,computeLocation,QSMSourceFolder)#Once systemParameters is available and filled out, ALWAYS run this command first.
#qSys.generateFile("GDS")#Run this command to generate layout files. "componentParams" --> "geometries" --> "GDS"
#qSys.simulationCommand(["simulation","ECQ0","postProcess"])#All "simulations" require completed layout files. 


#SIMULATION COMMANDS
#-----------------------------------------------------------------------------------------------------------
#CAPACITANCE MATRIX
#["simulation","capMat",{"init","run","postProcess"}]
#-----------------------------------------------------------------------------------------------------------
#CIRCUIT SIMULATIONS
#["simulation","fullS21",{"init","run","postProcess"}]

#["simulation","freqQ[N]",{"init","run","postProcess"}]
#["simulation","decayQ[N]",{"init","run","postProcess"}]
#["simulation","exchQ[N1]-[N2]",{"init","run"}] e.g. ["simulation","exchQ0-2","run"]

#["simulation","freqR[N]",{"init","run","postProcess"}]
#["simulation","lumpedR[N]",{"init","run","postProcess"}]
#["simulation","feedlineCouplingR[N]",{"init","run","postProcess"}]#Depends on results of freqQ[N]

#Helper commands:
#"initAllSims"
#"runAllSims"
#"postProcessAllSims"
#-----------------------------------------------------------------------------------------------------------
#AFTER CIRCUIT SIMULATIONS
#["simulation","capMatGE",{"init","postProcess"}]
#["simulation","ECQ[N]",{"init","postProcess"}]#Depends on results of capMatGE
#["simulation","L_iQ[N]",{"init","postProcess"}]#Check how closely this agrees with L_i in the component parameters file. Depends on EC

#Helper commands:
#"GEPlusAllEC": runs init/postprocess for capMatGE and all ECQ
#"AllL_i"
#-----------------------------------------------------------------------------------------------------------
#QUANTIZATION
#["simulation","quantize",{"init","postProcess"}]#Depends on results of all lumpedR
#-----------------------------------------------------------------------------------------------------------
#POST-QUANTIZATION
#["simulation","zzQ[m]-[n]",{"init","postProcess"}]# i.e. zzQ0-1
#["simulation","anharmonicityQ[N]",{"init","postProcess"}]
#["simulation","dispersiveShiftR[N]",{"init","postProcess"}]

#Helper commands:
#"Allzz"
#"AllAnharmonicityQ"
#-----------------------------------------------------------------------------------------------------------