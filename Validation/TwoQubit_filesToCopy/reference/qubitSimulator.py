#Import modules
import sys
import os
computeLocation="68707Max"
QSMSourceFolder=""
if computeLocation=="68707Max":
    QSMSourceFolder="O:/68707/JoelHoward/ChipDesign/QSMSource/"
    #QSMSourceFolder="O:/68707/RZ/ChipDesign/QSMSource"
elif computeLocation=="Wendian":
    QSMSourceFolder="/beegfs/scratch/joelhoward/QSMSimulations/QSMSource/"
sys.path.append(QSMSourceFolder)
import qubitSimulationModule

projectPath=os.path.dirname(os.path.abspath( __file__ ))
projectName=os.path.basename(projectPath)
projectFolder=projectPath.replace("\\","/")
#-------------Capacitance Matrix,CPW Simulation, and generateGDS------------


#command=["generateFile","GDS"]
#qubitSimulationModule.executeCommand(command,projectFolder,computeLocation,QSMSourceFolder)  

command=["simulation","capMat","init"]
qubitSimulationModule.executeCommand(command,projectFolder,computeLocation,QSMSourceFolder)  
command=["simulation","capMat","run"]
qubitSimulationModule.executeCommand(command,projectFolder,computeLocation,QSMSourceFolder) 
command=["simulation","capMat","postProcess"]
qubitSimulationModule.executeCommand(command,projectFolder,computeLocation,QSMSourceFolder) 

command="GEPlusAllEC"
qubitSimulationModule.executeCommand(command,projectFolder,computeLocation,QSMSourceFolder)  



'''
command=["simulation","fullS21","init"]
qubitSimulationModule.executeCommand(command,projectFolder,computeLocation,QSMSourceFolder)  
command=["simulation","fullS21","run"]
qubitSimulationModule.executeCommand(command,projectFolder,computeLocation,QSMSourceFolder) 
command=["simulation","fullS21","postProcess"]
qubitSimulationModule.executeCommand(command,projectFolder,computeLocation,QSMSourceFolder)
'''

'''
command=["simulation","freqQ0","init"]
qubitSimulationModule.executeCommand(command,projectFolder,computeLocation,QSMSourceFolder)  
command=["simulation","freqQ1","init"]
qubitSimulationModule.executeCommand(command,projectFolder,computeLocation,QSMSourceFolder) 
command=["simulation","freqR0","init"]
qubitSimulationModule.executeCommand(command,projectFolder,computeLocation,QSMSourceFolder) 
command=["simulation","freqR1","init"]
qubitSimulationModule.executeCommand(command,projectFolder,computeLocation,QSMSourceFolder) 
command=["simulation","feedlineCouplingR0","init"]
qubitSimulationModule.executeCommand(command,projectFolder,computeLocation,QSMSourceFolder) 
command=["simulation","feedlineCouplingR1","init"]
qubitSimulationModule.executeCommand(command,projectFolder,computeLocation,QSMSourceFolder) 


command=["simulation","freqQ0","run"]
qubitSimulationModule.executeCommand(command,projectFolder,computeLocation,QSMSourceFolder)  
command=["simulation","freqQ1","run"]
qubitSimulationModule.executeCommand(command,projectFolder,computeLocation,QSMSourceFolder) 
command=["simulation","freqR0","run"]
qubitSimulationModule.executeCommand(command,projectFolder,computeLocation,QSMSourceFolder) 
command=["simulation","freqR1","run"]
qubitSimulationModule.executeCommand(command,projectFolder,computeLocation,QSMSourceFolder) 
command=["simulation","feedlineCouplingR0","run"]
qubitSimulationModule.executeCommand(command,projectFolder,computeLocation,QSMSourceFolder) 
command=["simulation","feedlineCouplingR1","run"]
qubitSimulationModule.executeCommand(command,projectFolder,computeLocation,QSMSourceFolder) 
 
 
command=["simulation","freqQ0","postProcess"]
qubitSimulationModule.executeCommand(command,projectFolder,computeLocation,QSMSourceFolder)  
command=["simulation","freqQ1","postProcess"]
qubitSimulationModule.executeCommand(command,projectFolder,computeLocation,QSMSourceFolder) 
command=["simulation","freqR0","postProcess"]
qubitSimulationModule.executeCommand(command,projectFolder,computeLocation,QSMSourceFolder) 
command=["simulation","freqR1","postProcess"]
qubitSimulationModule.executeCommand(command,projectFolder,computeLocation,QSMSourceFolder)
command=["simulation","feedlineCouplingR0","postProcess"]
qubitSimulationModule.executeCommand(command,projectFolder,computeLocation,QSMSourceFolder) 
command=["simulation","feedlineCouplingR1","postProcess"]
qubitSimulationModule.executeCommand(command,projectFolder,computeLocation,QSMSourceFolder)
'''



command="initAllSims"
qubitSimulationModule.executeCommand(command,projectFolder,computeLocation,QSMSourceFolder)  


command="runAllSims"
qubitSimulationModule.executeCommand(command,projectFolder,computeLocation,QSMSourceFolder)  

command="postProcessAllSims"
qubitSimulationModule.executeCommand(command,projectFolder,computeLocation,QSMSourceFolder) 
 

command=["simulation","quantize","init"]
qubitSimulationModule.executeCommand(command,projectFolder,computeLocation,QSMSourceFolder)  
command=["simulation","quantize","run"]
qubitSimulationModule.executeCommand(command,projectFolder,computeLocation,QSMSourceFolder) 
command=["simulation","quantize","postProcess"]
qubitSimulationModule.executeCommand(command,projectFolder,computeLocation,QSMSourceFolder)


'''
command=["simulation","freqR0","run"]
qubitSimulationModule.executeCommand(command,projectFolder,computeLocation,QSMSourceFolder)
command=["simulation","freqR1","run"]
qubitSimulationModule.executeCommand(command,projectFolder,computeLocation,QSMSourceFolder)

command=["simulation","freqR0","postProcess"]
qubitSimulationModule.executeCommand(command,projectFolder,computeLocation,QSMSourceFolder)
command=["simulation","freqR1","postProcess"]
qubitSimulationModule.executeCommand(command,projectFolder,computeLocation,QSMSourceFolder)
'''
'''
command=["simulation","feedlineCouplingR0","run"]
qubitSimulationModule.executeCommand(command,projectFolder,computeLocation,QSMSourceFolder)
command=["simulation","feedlineCouplingR1","run"]
qubitSimulationModule.executeCommand(command,projectFolder,computeLocation,QSMSourceFolder)

command=["simulation","feedlineCouplingR0","postProcess"]
qubitSimulationModule.executeCommand(command,projectFolder,computeLocation,QSMSourceFolder)
command=["simulation","feedlineCouplingR1","postProcess"]
qubitSimulationModule.executeCommand(command,projectFolder,computeLocation,QSMSourceFolder)
'''
#command="runAllSims"
#qubitSimulationModule.executeCommand(command,projectFolder,computeLocation,QSMSourceFolder)


#command=["generateFile","GDS"]
#command=["simulation","capMat","postProcess"]["simulation","capMatGE",{"init","postProcess"}]


#command="GEPlusAllEC"
#qubitSimulationModule.executeCommand(command,projectFolder,computeLocation,QSMSourceFolder)  

#command=["simulation","exchQ0-1","run"]
#["generateFile",{"sysParams","componentParams","geometries","GDS"}]
#["simulation","capMat",{"init","run"}]
#["simulation","CPW",{"init","run"}]
#["simulation","fullS21",{"init","run"}]
#["simulation","freqR[N]",{"init","run"}]
#["simulation","freqQ[N]",{"init","run"}]
#["simulation","decayQ[N]",{"init","run"}]
#["simulation","lumpedR[N]",{"init","run"}]
#["simulation","quantize",{"init","run"}]

#"initAllSims"
#"runAllSims"
#qubitSimulationModule.executeCommand(command,projectName,projectFolder,computeLocation,QSMSourceFolder)
