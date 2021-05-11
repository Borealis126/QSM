import subprocess
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
import os
from math import factorial
from scipy.misc import derivative
import numpy as np
import gdspy
import time
from ChipElements import OtherComponents
from sympy import symbols,Matrix,zeros,sin
from qutip import tensor,state_number_index,qzero,ket,bra

from analysisFunctions import S21TodB,calculateDressedFrequency
from ansysFunctions import ansysSignalLine_Lines,netlistHeaderLines,ansysSaveLine,ansysUniteNodes,aedtEdit,netlistSimulationLines
from basicGeometryFunctions import pointInPolyline,rotate,translate
from csvFunctions import *

from polylineFunctions import rectanglePolyline,multiplyPolyline
from qSysObjects import *
from quantumStateFunctions import stateFromHeader,baseRepresentation,H_Header
from constants import *
 
def generateSystemParametersFile(folder):
    file=folder/"systemParametersFile.csv"
    lines=[["Chip Description","description"],\
           ["Number of Qubits",1],\
           ["Number of Readout Resonators",1],\
           ["Number of Bus Coupler Resonators",1],\
           ["Number of PTCs",0],\
           ["Number of Straight Bus Couplers",0],\
           ["Number of Control Lines",1],\
           ["Material","perfect conductor"],\
           ["Flip Chip?","No"],\
           ["Chip Markers","Pappas"],\
           ["Simulation","2D"],\
           ["Simulate Feedline?","No"],\
           ["Add Mesh to GDS?","No"],\
           ["Invert GDS?","No"],\
           ["Anti-Vortex Mesh Boundary",40],\
           ["Anti-Vortex Mesh Spacing",50],\
           ["Anti-Vortex Mesh Size",5]]#This is how far the holes in the substrate are from any given component. 
    csvWrite(file,lines)  
def initialize(projectFolder,computeLocation,QSMSourceFolder):
    qSys=loadSystemParametersFile(projectFolder=projectFolder,computeLocation=computeLocation,QSMSourceFolder=QSMSourceFolder)
    return qSys
def loadSystemParametersFile(projectFolder,computeLocation,QSMSourceFolder): #returns qubitSystem object based on data in systemParametersFile
    systemParametersFileLines=csvRead(projectFolder/"systemParametersFile.csv")
    systemParams=dict()
    for line in systemParametersFileLines:
        systemParams[line[0]]=returnCorrectType(line[1]) 
    systemParams["Project Folder"]=projectFolder
    systemParams["Compute Location"]=computeLocation
    systemParams["QSM Source Folder"]=QSMSourceFolder
    return qubitSystem(sysParams=systemParams)
class qubitSystem:
    def __init__(self,sysParams):
        #---independent of flip chip
        self.sysParams=sysParams
        self.projectFolder=self.sysParams["Project Folder"]
        self.componentParametersFile=self.projectFolder/"componentParametersFile.csv"
        self.componentGeometriesFile=self.projectFolder/"componentGeometriesFile.csv"
        self.gdspyFile=self.projectFolder/"layout.gds"
        
        #Dictionaries that are only used until the components are assigned to their respective chips
        self.chipDict=dict()
        
        self.capMat=[]#Overwritten by loadCapMatSimulationResults
        self.ansysCapMatHeaders=[]#Index names of self.capMat
        
        self.capMatGE=[]
        
        self.H=[]
        self.HComponentOrder=[]#List of objects defining the order of components in the state lists. Should agree with quantize simulation parameters file.
        self.HStateOrder=[]#List of states in the order of self.H
        self.HEvals=[]
        
        self.preGECapMatHeaders=[]#After removing the control lines and one resonator pad (and anything else per the model)
        self.postGEComponentList=[]#List of components according to their order in the GE capMat. 
        #------------------------------------
        if self.sysParams["Flip Chip?"]=="Yes":
            self.chipDict={0:Chip(0),1:Chip(1)}
            self.bumpsDict=dict()#Not clearly tied to a single chip.
            self.chipSpacing=0#Not clearly tied to a single chip.
        elif self.sysParams["Flip Chip?"]=="No":
            self.chipDict={0:Chip(0)}
        self.CPW=CPW()#Substantiated in loadGeometries. 
        
        #---Simulation files---
        self.simFiles=dict()#circuit simulation files are added in loadComponentParametersFile once the qubits are defined. 
        self.addToSimFiles(simType="quantize",q3dSims=[],hfssSims=[],circuitSims=[])
        self.addToSimFiles(simType="CPW",q3dSims=[],hfssSims=["portSweep"],circuitSims=[])
        self.addToSimFiles(simType="capMat",q3dSims=["q3dExtractor"],hfssSims=[],circuitSims=[])
        self.addToSimFiles(simType="capMatGE",q3dSims=[],hfssSims=[],circuitSims=[])
        #Populate the available circuit simulation types. 
        self.addToSimFiles(simType="fullS21",q3dSims=[],hfssSims=[],circuitSims=["fullS21"])
        for qubit1Index in range(self.sysParams["Number of Qubits"]):
            self.addToSimFiles(simType="circFreqQ"+str(qubit1Index),q3dSims=[],hfssSims=[],circuitSims=["Y11Q"+str(qubit1Index)])#Qubit frequency simulations
            self.addToSimFiles(simType="decayQ"+str(qubit1Index),q3dSims=[],hfssSims=[],circuitSims=["Y11Q"+str(qubit1Index)])
            self.addToSimFiles(simType="ECQ"+str(qubit1Index),q3dSims=[],hfssSims=[],circuitSims=[])#E_C calculated from the capacitance matrix.
            self.addToSimFiles(simType="anharmonicityQ"+str(qubit1Index),q3dSims=[],hfssSims=[],circuitSims=[])
            self.addToSimFiles(simType="quantFreqQ"+str(qubit1Index),q3dSims=[],hfssSims=[],circuitSims=[])
            self.addToSimFiles(simType="L_iQ"+str(qubit1Index),q3dSims=[],hfssSims=[],circuitSims=[])
            for qubit2Index in range(self.sysParams["Number of Qubits"]):
                if qubit2Index>qubit1Index:
                    self.addToSimFiles(simType="exchQ"+str(qubit1Index)+"-"+str(qubit2Index),q3dSims=[],hfssSims=[],circuitSims=["Z21Q"+str(qubit1Index)+"-"+str(qubit2Index)])
                    self.addToSimFiles(simType="zzQ"+str(qubit1Index)+"-"+str(qubit2Index),q3dSims=[],hfssSims=[],circuitSims=[])
        for readoutResonatorIndex in range(self.sysParams["Number of Readout Resonators"]):
            self.addToSimFiles(simType="ECR"+str(readoutResonatorIndex),q3dSims=[],hfssSims=[],circuitSims=[])#E_C calculated from the capacitance matrix.
            self.addToSimFiles(simType="circFreqR"+str(readoutResonatorIndex),q3dSims=[],hfssSims=[],circuitSims=["Y11R"+str(readoutResonatorIndex)])#Resonator frequency simulations
            self.addToSimFiles(simType="lumpedR"+str(readoutResonatorIndex),q3dSims=[],hfssSims=[],circuitSims=["Y11R"+str(readoutResonatorIndex),"YRestR"+str(readoutResonatorIndex)])#Lumped resonator simulations
            self.addToSimFiles(simType="freqLumpedR"+str(readoutResonatorIndex),q3dSims=[],hfssSims=[],circuitSims=["Y11LumpedR"+str(readoutResonatorIndex)])#Calculates frequency after substituting lumped elements in. 
            self.addToSimFiles(simType="quantFreqR"+str(readoutResonatorIndex),q3dSims=[],hfssSims=[],circuitSims=[])
            self.addToSimFiles(simType="feedlineCouplingR"+str(readoutResonatorIndex),q3dSims=[],hfssSims=[],circuitSims=["Y11R"+str(readoutResonatorIndex)])
            self.addToSimFiles(simType="dispersiveShiftR"+str(readoutResonatorIndex),q3dSims=[],hfssSims=[],circuitSims=[])
        for PTCIndex in range(self.sysParams["Number of PTCs"]):
            self.addToSimFiles(simType="freqPTC"+str(PTCIndex),q3dSims=[],hfssSims=[],circuitSims=["Y11PTC"+str(PTCIndex)])#Resonator frequency simulations
        for straightBusCouplerIndex in range(self.sysParams["Number of Straight Bus Couplers"]):
            self.addToSimFiles(simType="freqBC"+str(straightBusCouplerIndex),q3dSims=[],hfssSims=[],circuitSims=["Y11BC"+str(straightBusCouplerIndex)])#Qubit frequency simulations
    def generateFile(self,fileType):
        if fileType=="componentParams":
            self.generateComponentParametersFile() 
        elif fileType=="geometries":
            self.loadComponentParametersFile()
            self.generateGeometriesFile()
        elif fileType=="GDS":
            self.loadComponentParametersFile()
            self.loadGeometriesFile()
            self.generateGDS() 
    def generateComponentParametersFile(self):
        lines=[]
        qubitRow=["Qubits","Index","Type","L_J(H)","L_I(H)"]
        readoutResonatorRow=["Readout Resonators","Index","Pad 1 Type","Pad 2 Type"]
        busCouplerResonatorRow=["Bus Coupler Resonators","Index","Pad 1 Type","Pad 2 Type"]
        PTCRow=["PTCs","Index","SQUID Inductance(H)","Phase Velocity (um/s)"]
        straightBusCouplerRow=["Straight Bus Couplers","Index","L_J(H)","L_I(H)"]
        controlLineRow=["Control Lines","Index","Type"]#SectionsCode is a string of S and R, where S corresponds to segment and R corresponds to turn
        if self.sysParams["Flip Chip?"]=="Yes":
            qubitRow=qubitRow+["Chip"]
            readoutResonatorRow=readoutResonatorRow+["Chip"]
            PTCRow=PTCRow+["Chip"]
            controlLineRow=controlLineRow+["Chip"]
            bumpsRow=["Bumps","Spacing","Bump Metal Width","Under Bump Width"]
        if self.sysParams["Number of Qubits"]!=0:
            lines.append(qubitRow)
            for qubitIndex in range(self.sysParams["Number of Qubits"]):
                lines.append(["",qubitIndex])        
            lines.append([""])
        if self.sysParams["Number of Readout Resonators"]!=0:
            if self.sysParams["Simulate Feedline?"]=="No":
                readoutResonatorRow=readoutResonatorRow+["Capacitance to Feedline (F)","Feedline Pad Capacitance to Ground (F)"]
            lines.append(readoutResonatorRow)
            for readoutResonatorIndex in range(self.sysParams["Number of Readout Resonators"]):
                lines.append(["",readoutResonatorIndex])        
            lines.append([""])
        if self.sysParams["Number of Bus Coupler Resonators"]!=0:
            lines.append(busCouplerResonatorRow)
            for busCouplerResonatorIndex in range(self.sysParams["Number of Bus Coupler Resonators"]):
                lines.append(["",busCouplerResonatorIndex])        
            lines.append([""])
        if self.sysParams["Number of PTCs"]!=0:
            lines.append(PTCRow)
            for PTCIndex in range(self.sysParams["Number of PTCs"]):
                lines.append(["",PTCIndex])        
            lines.append([""])
        if self.sysParams["Number of Straight Bus Couplers"]!=0:
            lines.append(straightBusCouplerRow)
            for straightBusCouplerIndex in range(self.sysParams["Number of Straight Bus Couplers"]):
                lines.append(["",straightBusCouplerIndex])        
            lines.append([""])   
        if self.sysParams["Number of Control Lines"]!=0:
            lines.append(controlLineRow)
            for controlLineIndex in range(self.sysParams["Number of Control Lines"]):
                lines.append(["",controlLineIndex])
            lines.append([""])
        
        lines.append(["CPW","Phase Velocity(um/s)"])  
        lines.append([""])
        lines.append([""])
        
        if self.sysParams["Flip Chip?"]=="Yes":
            lines.append(bumpsRow) 
        
        csvWrite(self.componentParametersFile,lines)  
    def loadComponentParametersFile(self):
        fileLines=csvRead(self.componentParametersFile)
        #Qubits
        if self.sysParams["Number of Qubits"]!=0:
            qubitComponentsDict=readComponentRowData(fileLines,"Qubits")
            for qubitIndex,params in qubitComponentsDict.items():
                if self.sysParams["Flip Chip?"]=="Yes":
                    qubitChipIndex=returnCorrectType(qubitComponentsDict[qubitIndex]["Chip"])
                elif self.sysParams["Flip Chip?"]=="No":
                    qubitChipIndex=0
                qubit=dict()
                if "Floating" in params["Type"]:
                    qubit=floatingQubit(index=qubitIndex)
                elif "Grounded" in params["Type"]:
                    qubit=groundedQubit(index=qubitIndex)
                qubit.generalParamsDict=params
                #Interpret the qubit type
                fingersStrings=[i for i in qubit.generalParamsDict["Type"].split("-") if "Fingers" in i]
                for fingersString in fingersStrings:#Allowing both pads to have fingers
                    padIndex=returnCorrectType([i for i in fingersString.split("_") if "Pad" in i][0][3:])
                    numFingers=returnCorrectType([i for i in fingersString.split("_") if "Num" in i][0][3:])
                    qubit.fingers["Pad "+str(padIndex)]=numFingers
                self.chipDict[qubitChipIndex].qubitDict[qubitIndex]=qubit#Copy the qubit object to the chip's qubit dictionary
        #Resonators
        if self.sysParams["Number of Readout Resonators"]!=0:
            resonatorComponentsDict=readComponentRowData(fileLines,"Readout Resonators")
            for index,params in resonatorComponentsDict.items():
                if self.sysParams["Flip Chip?"]=="Yes":
                    resonatorChipIndex=resonatorComponentsDict[index]["Chip"]
                elif self.sysParams["Flip Chip?"]=="No":
                    resonatorChipIndex=0
                readoutResonator=ReadoutResonator(index)
                self.chipDict[resonatorChipIndex].readoutResonatorDict[index]=readoutResonator
                readoutResonator.generalParamsDict=params
        #PTCs
        if self.sysParams["Number of PTCs"]!=0:
            PTCComponentsDict=readComponentRowData(fileLines,"PTCs")
            for index,params in PTCComponentsDict.items():
                if self.sysParams["Flip Chip?"]=="Yes":
                    PTCChipIndex=PTCComponentsDict[index]["Chip"]
                elif self.sysParams["Flip Chip?"]=="No":
                    PTCChipIndex=0
                PTC=PTCClass(index)
                PTC.generalParamsDict=params
                self.chipDict[PTCChipIndex].PTCDict[index]=PTC#Copy the qubit object to the chip's qubit dictionary
        #Straight Bus Couplers
        if self.sysParams["Number of Straight Bus Couplers"]!=0:
            componentsDict=readComponentRowData(fileLines,"Straight Bus Couplers")
            for index,params in componentsDict.items():
                chipIndex=0
                if self.sysParams["Flip Chip?"]=="Yes":
                    chipIndex=componentsDict[index]["Chip"]
                straightBusCoupler=StraightBusCoupler(index)
                straightBusCoupler.generalParamsDict=params
                self.chipDict[chipIndex].straightBusCouplerDict[index]=straightBusCoupler#Copy the qubit object to the chip's qubit dictionary
        #Control Lines
        if self.sysParams["Number of Control Lines"]!=0:
            controlLineComponentsDict=readComponentRowData(fileLines,"Control Lines")
            for index,params in controlLineComponentsDict.items():
                if self.sysParams["Flip Chip?"]=="Yes":
                    controlLineChipIndex=controlLineComponentsDict[index]["Chip"]
                elif self.sysParams["Flip Chip?"]=="No":
                    controlLineChipIndex=0
                controlLine=ControlLine(index)
                controlLine.generalParamsDict=params
                self.chipDict[controlLineChipIndex].controlLineDict[index]=controlLine#Copy the qubit object to the chip's qubit dictionary
        #Load CPW info
        self.CPW.generalParamsDict=readSingleRowData(fileLines,"CPW")
        #Load bumps info
        if self.sysParams["Flip Chip?"]=="Yes":
            self.bumpsDict=readSingleRowData(fileLines,"Bumps")
            
        #Components ordering
        nonGECapMatIndex=0
        self.preGECapMatHeaders=[]
        self.postGEComponentList=[]
        for qubitIndex,qubit in self.allQubitsDict.items():
            qubit.pad1.quantCapMatIndex=nonGECapMatIndex
            self.preGECapMatHeaders.append(qubit.pad1.name)
            nonGECapMatIndex+=1
            if isinstance(qubit,floatingQubit):
                qubit.pad2.quantCapMatIndex=nonGECapMatIndex
                nonGECapMatIndex+=1
                self.preGECapMatHeaders.append(qubit.pad2.name)
            self.postGEComponentList.append(qubit)
        for straightBusCouplerIndex,straightBusCoupler in self.allStraightBusCouplersDict.items():
            straightBusCoupler.pad1.quantCapMatIndex=nonGECapMatIndex
            self.preGECapMatHeaders.append(straightBusCoupler.pad1.name)
            straightBusCoupler.pad2.quantCapMatIndex=nonGECapMatIndex+1
            self.preGECapMatHeaders.append(straightBusCoupler.pad2.name)
            self.postGEComponentList.append(straightBusCoupler)
            nonGECapMatIndex+=2
        for readoutResonatorIndex,readoutResonator in self.allReadoutResonatorsDict.items():
            readoutResonator.pad2.quantCapMatIndex=nonGECapMatIndex#Only pad2 is included in quantization
            self.preGECapMatHeaders.append(readoutResonator.pad2.node.name)
            self.postGEComponentList.append(readoutResonator)
            nonGECapMatIndex+=1              
    def generateGeometriesFile(self):
        #For flip chip the polylines for the nodes, substrate, etc. are relative to looking top-down on the assembly, which is centered on the origin. 
        #The chip furthest from the viewer is chip 1. 
        lines=[]
        #Prompt for the qubits
        for qubitIndex,qubit in self.allQubitsDict.items():
            properties=[]
            if "rectangularPads" in qubit.generalParamsDict["Type"]:
                if isinstance(qubit,floatingQubit):
                    properties+=["Angle",\
                                 "Center X",\
                                 "Center Y",\
                                 "Pad Spacing",\
                                 "Pad 1 Width",\
                                 "Pad 1 Length",\
                                 "Pad 1 Height",\
                                 "Pad 1 Side 1 Boundary",\
                                 "Pad 1 Side 2 Boundary",\
                                 "Pad 1 Side 3 Boundary",\
                                 "Pad 1 Side 4 Boundary",\
                                 "Pad 2 Width",\
                                 "Pad 2 Length",\
                                 "Pad 2 Height",\
                                 "Pad 2 Side 1 Boundary",\
                                 "Pad 2 Side 2 Boundary",\
                                 "Pad 2 Side 3 Boundary",\
                                 "Pad 2 Side 4 Boundary",\
                                 "JJ Location"]#JJ location is any number between 0 and 100 representing the location of the JJ relative to the pads. 0 is on the left, 100 is on the right, 50 is in the middle. 
                elif isinstance(qubit,groundedQubit):
                    properties+=["Angle",\
                                 "Center X",\
                                 "Center Y",\
                                 "Pad 1 Width",\
                                 "Pad 1 Length",\
                                 "Pad 1 Height",\
                                 "Pad 1 Side 1 Boundary",\
                                 "Pad 1 Side 2 Boundary",\
                                 "Pad 1 Side 3 Boundary",\
                                 "Pad 1 Side 4 Boundary",\
                                 "JJ Location"]#JJ location is any number between 0 and 100 representing the location of the JJ relative to the pads. 0 is on the left, 100 is on the right, 50 is in the middle. 
                if "doubleJJ" in qubit.generalParamsDict["Type"]:
                    properties+=["SQUID Stem Separation",\
                                 "SQUID T Stem Width",\
                                 "SQUID T Head Width",\
                                 "SQUID T Head Length",\
                                 "JJ Patch Length",\
                                 "JJ Patch Width",\
                                 "JJ Boundary",\
                                 "SQUID Stem Width",\
                                 "SQUID Stem Length"]
                elif "singleJJ" in qubit.generalParamsDict["Type"]:#Otherwise assumed to be along the line of symmetry of the rectangular pads. 
                    properties+=["JJ Stem Boundary",\
                                 "JJ Stem Width",\
                                 "JJ Patch Width",\
                                 "JJ Patch Length"]
                properties+=["JJ Top Electrode Width",\
                             "JJ Bottom Electrode Width"]
                for padName,numFingers in qubit.fingers.items():
                    if numFingers>1:
                        properties+=[padName+" Finger Spacing"]
                    for fingerIndex in range(numFingers):
                        properties+=[padName+" Finger "+str(fingerIndex)+" Stem Length",\
                                     padName+" Finger "+str(fingerIndex)+" Stem Width",\
                                     padName+" Finger Stem Boundary",\
                                     padName+" Finger "+str(fingerIndex)+" T Head Length",\
                                     padName+" Finger "+str(fingerIndex)+" T Width",\
                                     padName+" Finger "+str(fingerIndex)+" T Side 1 Boundary",\
                                     padName+" Finger "+str(fingerIndex)+" T Side 2 Boundary",\
                                     padName+" Finger "+str(fingerIndex)+" T Side 3 Boundary",\
                                     padName+" Finger "+str(fingerIndex)+" T Side 4 Boundary"]  
            lines.append([qubit.name]+properties)
            lines+=[[""],[""]]                   
        #Prompt for resonators
        for readoutResonatorIndex,readoutResonator in self.allReadoutResonatorsDict.items():
            properties=["Length",\
                        "Angle",\
                        "Center X",\
                        "Center Y",\
                        "Pad Separation",\
                        "Meander Turn Radius",\
                        "Pad T Stem Length",\
                        "Meander To Pad Minimum Distance",\
                        "Pad 1 Curve Angle",\
                        "Pad 2 Curve Angle"]
            for padIndex in ["1","2"]:
                if "T" in readoutResonator.generalParamsDict["Pad "+padIndex+" Type"].split("-"):
                    properties=properties+["Pad "+padIndex+" Width",\
                                           "Pad "+padIndex+" Length",\
                                           "Pad "+padIndex+" Height",\
                                           "Pad "+padIndex+" Side 1 Boundary",\
                                           "Pad "+padIndex+" Side 2 Boundary",\
                                           "Pad "+padIndex+" Side 3 Boundary",\
                                           "Pad "+padIndex+" Side 4 Boundary"]
            lines.append([readoutResonator.name]+properties)
            lines+=[[""],[""]]
        #Prompt for PTCs
        for PTCIndex,PTC in self.allPTCsDict.items():
            properties=["Length",\
                        "Angle",\
                        "Center X",\
                        "Center Y",\
                        "End Separation",\
                        "Meander Turn Radius",\
                        "Meander To End Minimum Distance",\
                        "Height",\
                        "CPW Width",\
                        "CPW Gap",\
                        "SQUID Stem Separation",\
                        "SQUID T Stem Length",\
                        "SQUID T Head Width",\
                        "SQUID T Head Length",\
                        "SQUID Patch Length",\
                        "SQUID Patch Width",\
                        "SQUID Boundary",\
                        "SQUID Stem Width",\
                        "SQUID Stem Length",\
                        "SQUID Bar Width",\
                        "SQUID Bar Boundary",\
                        "SQUID Bar Length",\
                        "SQUID Bar T Length",\
                        "SQUID Bar T Width",\
                        "SQUID Bar T Boundary",\
                        "JJ Top Electrode Width",\
                        "JJ Bottom Electrode Width"]
            lines.append([PTC.name]+properties)
            lines+=[[""],[""]]
        #Prompt for the bus couplers
        for straightBusCouplerIndex,straightBusCoupler in self.allStraightBusCouplersDict.items():
            properties=["Total Length",\
                        "Angle",\
                        "Center X",\
                        "Center Y",\
                        "Height",\
                        "Body Width",\
                        "Body Boundary",\
                        "End Width",\
                        "End Length",\
                        "End Boundary",\
                        "SQUID Stem Separation",\
                        "SQUID T Stem Width",\
                        "SQUID T Stem Length",\
                        "SQUID T Head Width",\
                        "SQUID T Head Length",\
                        "SQUID Patch Length",\
                        "SQUID Patch Width",\
                        "SQUID Boundary",\
                        "SQUID Stem Width",\
                        "SQUID Stem Length",\
                        "JJ Top Electrode Width",\
                        "JJ Bottom Electrode Width"]
            lines.append([straightBusCoupler.name]+properties)
            lines+=[[""],[""]]
        #Prompt for the control lines.
        for controlLineIndex,controlLine in self.allControlLinesDict.items():
            properties=["Start X",\
                        "Start Y",\
                        "Start Angle",\
                        "Section Code"]
            if controlLine.generalParamsDict["Type"]=="fluxBias":
                properties=properties+["loopThickness","loopSeg1Length","loopSeg2Length","loopSeg3Length","loopSeg1Boundary","loopSeg2Boundary","loopSeg3Boundary"]
            if controlLine.generalParamsDict["Type"]=="drive":
                properties=properties+["End Gap"]
            lines.append([controlLine.name]+properties)
            lines+=[[""],[""]]
        #Prompt for the CPW. 
        CPWParams=["CPW","Width","Gap","Trench","Height"]
        lines.append(CPWParams)
        lines.append(["","10","6","0.1","0.1"])
        lines.append([""])
        
        #Prompt for the ground(s).
        lines.append(["Ground(s)","Index","Height"])
        for chipIndex,chip in self.chipDict.items():
            lines.append(["",chip.ground.index,0.1])
        lines.append([""])
        
        #Prompt for the substrate(s).
        lines.append(["Substrate(s)","Index","Material","Thickness","Width","Length"])
        for chipIndex,chip in self.chipDict.items():
            lines.append(["",chip.substrate.index,"silicon",500,9500,7500])
        lines.append([""])
        
        #Prompt for NIST logo location
        lines.append(["NIST Logo","Center X","Center Y"])
        lines.append(["",2000,-3000])
        lines.append([""])
        
        #Prompt for Chip Description location
        lines.append(["Chip Description","Start X","Start Y"])
        lines.append(["",1500,-2500])
        lines.append([""])
        #If flip chip, prompt for chip spacing
        if self.sysParams["Flip Chip?"]=="Yes":
            lines.append(["Flip Chip","Chip Spacing"])
            lines.append(["",1000])
            lines.append([""])          
        csvWrite(self.componentGeometriesFile,lines)
    def loadGeometriesFile(self):#The qubit geometry specific parts are shifted into the qubit updateNodes method, a function of the qubitPadParametersDict loaded here. 
        fileLines=csvRead(self.componentGeometriesFile)
        #Load CPW info
        self.CPW.geometryParamsDict=readSingleRowData(fileLines,"CPW")
        #Load NIST Logo info
        NISTLogoParams=readSingleRowData(fileLines,"NIST Logo")
        self.chipDict[0].nistLogoCenter=[NISTLogoParams["Center X"],NISTLogoParams["Center Y"]]#Logo always on the first chip. 
        #Load Chip Description info
        chipDescriptionParams=readSingleRowData(fileLines,"Chip Description")
        self.chipDict[0].chipDescriptionStart=[chipDescriptionParams["Start X"],chipDescriptionParams["Start Y"]]#Logo always on the first chip. 
        #If flip chip, load chip spacing
        if self.sysParams["Flip Chip?"]=="Yes":
            self.chipSpacing=readSingleRowData(fileLines,"Flip Chip")["Chip Spacing"]
        substrateParamsDict=readComponentRowData(fileLines,"Substrate(s)")
        groundComponentsDict=readComponentRowData(fileLines,"Ground(s)")
        #Load geometries
        for chipIndex,chip in self.chipDict.items():
            #Substrates
            chip.substrate.geometryParamsDict=substrateParamsDict[chipIndex]
            chip.substrate.node.height=chip.substrate.geometryParamsDict["Thickness"]
            chip.substrate.node.material=chip.substrate.geometryParamsDict["Material"]
            chip.substrate.node.polyline=rectanglePolyline(centerX=0,\
                                                           centerY=0,\
                                                           width=chip.substrate.geometryParamsDict["Width"],\
                                                           length=chip.substrate.geometryParamsDict["Length"],\
                                                           angle=0)
            if chipIndex==0:
                chip.substrate.node.Z=0#Always 0 for substrate 0, convention
            elif chipIndex==1:
                chip.substrate.node.Z=self.chipDict[0].substrate.node.height+self.chipSpacing
            #Ground
            chip.ground.geometryParamsDict=groundComponentsDict[chipIndex]
            chip.ground.outlineNode.height=chip.ground.geometryParamsDict["Height"]
            chip.ground.outlineNode.polyline=chip.substrate.node.polyline#Ground covers the full substrate
            if chipIndex==0:
                chip.ground.outlineNode.Z=self.chipDict[0].substrate.node.height
            elif chipIndex==1:
                chip.ground.outlineNode.Z=self.chipDict[1].substrate.node.Z-chip.ground.outlineNode.height
            #Qubits
            for qubitIndex,qubit in chip.qubitDict.items():
                qubit.geometryParamsDict=readSingleRowData(fileLines,qubit.name)
                JJLoc_x,JJLoc_y=readJJLocation(qubit.geometryParamsDict["JJ Location"])
                #Polylines
                if "rectangularPads" in qubit.generalParamsDict["Type"]:
                    padSpacing=0
                    centerX=0#X,Y coordinates of the symmetric center of the two-pad structure. 
                    centerY=0
                    pad1NormalizedCenterPoint=[0,0]
                    pad2NormalizedCenterPoint=[0,0]
                    if isinstance(qubit,floatingQubit):
                        padSpacing=qubit.geometryParamsDict["Pad Spacing"]
                        centerX=qubit.geometryParamsDict["Center X"]
                        centerY=qubit.geometryParamsDict["Center Y"]
                        pad1NormalizedCenterPoint=[0,padSpacing/2+qubit.geometryParamsDict["Pad 1 Length"]/2]
                        pad2NormalizedCenterPoint=[0,-padSpacing/2-qubit.geometryParamsDict["Pad 2 Length"]/2]
                        qubit.pad2.node.polylineShapeParams["JJ Stem X"]=-JJLoc_x
                    if isinstance(qubit,groundedQubit):
                        #Pad 2 is a sliver that will be shorted to ground.
                        qubit.pad2.node.polylineShape="rectangle"
                        qubit.geometryParamsDict["Pad 2 Length"]=0.01
                        qubit.geometryParamsDict["Pad 2 Height"]=qubit.geometryParamsDict["Pad 1 Height"]
                        qubit.geometryParamsDict["Pad 2 Side 1 Boundary"]=0
                        qubit.geometryParamsDict["Pad 2 Side 2 Boundary"]=0
                        qubit.geometryParamsDict["Pad 2 Side 3 Boundary"]=0
                        qubit.geometryParamsDict["Pad 2 Side 4 Boundary"]=0
                        
                        padSpacing=qubit.geometryParamsDict["Pad 1 Side 4 Boundary"]-qubit.geometryParamsDict["Pad 2 Length"]
                        centerX=qubit.geometryParamsDict["Center X"]
                        centerY=qubit.geometryParamsDict["Center Y"]\
                                -qubit.geometryParamsDict["Pad 1 Length"]/2\
                                -padSpacing/2
                        pad1NormalizedCenterPoint=[0,padSpacing/2+qubit.geometryParamsDict["Pad 1 Length"]/2]
                        pad2NormalizedCenterPoint=[JJLoc_x,-padSpacing/2-qubit.geometryParamsDict["Pad 2 Length"]/2]
                        qubit.pad2.node.polylineShapeParams["JJ Stem X"]=0
                    for pad in qubit.padListGeom:
                        pad.node.polylineShape="rectangle"
                    #Top pad   
                    pad1CenterPoint=translate(rotate(pad1NormalizedCenterPoint,\
                                                     qubit.geometryParamsDict["Angle"]),\
                                              centerX,\
                                              centerY)
                    qubit.pad1.node.polylineShapeParams["Body Center X"]=pad1CenterPoint[0]
                    qubit.pad1.node.polylineShapeParams["Body Center Y"]=pad1CenterPoint[1]
                    qubit.pad1.node.polylineShapeParams["Angle"]=qubit.geometryParamsDict["Angle"]
                    qubit.pad1.node.polylineShapeParams["JJ Stem X"]=JJLoc_x
                    
                    #Bottom pad
                    pad2CenterPoint=translate(rotate(pad2NormalizedCenterPoint,\
                                                     qubit.geometryParamsDict["Angle"]),\
                                              centerX,\
                                              centerY)
                    qubit.pad2.node.polylineShapeParams["Body Center X"]=pad2CenterPoint[0]
                    qubit.pad2.node.polylineShapeParams["Body Center Y"]=pad2CenterPoint[1]
                    qubit.pad2.node.polylineShapeParams["Angle"]=qubit.geometryParamsDict["Angle"]+np.pi#Addition of pi is so the stem points the right way.
                    
                    #Add fingers if applicable
                    if qubit.fingers!={}: #If fingers for either pad 1 or pad 2 are specified:
                        if "Pad 1" in qubit.fingers:
                            qubit.pad1.node.polylineShape+="PlusFinger(s)"
                            qubit.pad1.node.polylineShapeParams["Number of Fingers"]=qubit.fingers["Pad 1"]
                        if "Pad 2" in qubit.fingers:
                            qubit.pad2.node.polylineShape+="PlusFinger(s)"
                            qubit.pad2.node.polylineShapeParams["Number of Fingers"]=qubit.fingers["Pad 2"]
                        for padName,numFingers in qubit.fingers.items():
                            if padName=="Pad 1":
                                thisNode=qubit.pad1.node
                            elif padName=="Pad 2":
                                thisNode=qubit.pad2.node
                            for fingerIndex in range(numFingers):
                                if numFingers>1:
                                    thisNode.polylineShapeParams["Finger Spacing"]=qubit.geometryParamsDict[padName+" Finger Spacing"]
                                else:
                                    thisNode.polylineShapeParams["Finger Spacing"]=0
                                thisNode.polylineShapeParams["Finger "+str(fingerIndex)+" Stem Length"]=qubit.geometryParamsDict[padName+" Finger "+str(fingerIndex)+" Stem Length"]
                                thisNode.polylineShapeParams["Finger "+str(fingerIndex)+" Stem Width"]=qubit.geometryParamsDict[padName+" Finger "+str(fingerIndex)+" Stem Width"]
                                thisNode.polylineShapeParams["Finger Stem Boundary"]=qubit.geometryParamsDict[padName+" Finger Stem Boundary"]
                                thisNode.polylineShapeParams["Finger "+str(fingerIndex)+" T Head Length"]=qubit.geometryParamsDict[padName+" Finger "+str(fingerIndex)+" T Head Length"]
                                thisNode.polylineShapeParams["Finger "+str(fingerIndex)+" T Width"]=qubit.geometryParamsDict[padName+" Finger "+str(fingerIndex)+" T Width"]
                                thisNode.polylineShapeParams["Finger "+str(fingerIndex)+" T Side 1 Boundary"]=qubit.geometryParamsDict[padName+" Finger "+str(fingerIndex)+" T Side 1 Boundary"]
                                thisNode.polylineShapeParams["Finger "+str(fingerIndex)+" T Side 2 Boundary"]=qubit.geometryParamsDict[padName+" Finger "+str(fingerIndex)+" T Side 2 Boundary"]
                                thisNode.polylineShapeParams["Finger "+str(fingerIndex)+" T Side 3 Boundary"]=qubit.geometryParamsDict[padName+" Finger "+str(fingerIndex)+" T Side 3 Boundary"]
                                thisNode.polylineShapeParams["Finger "+str(fingerIndex)+" T Side 4 Boundary"]=qubit.geometryParamsDict[padName+" Finger "+str(fingerIndex)+" T Side 4 Boundary"]
                    #JJ additions
                    if "singleJJ" in qubit.generalParamsDict["Type"]:
                        for pad in qubit.padListGeom:
                            pad.node.polylineShape+="PlusSingleJJ"
                        for i in [pad.node for pad in qubit.padListGeom]:
                            i.polylineShapeParams["JJ Stem Width"]=qubit.geometryParamsDict["JJ Stem Width"]
                            i.polylineShapeParams["JJ Stem End Boundary"]=qubit.geometryParamsDict["JJ Patch Length"]/2
                            i.polylineShapeParams["JJ Stem Side Boundary"]=qubit.geometryParamsDict["JJ Stem Boundary"]
                        
                        qubit.pad1.node.polylineShapeParams["JJ Stem Length"]=(padSpacing-qubit.geometryParamsDict["JJ Patch Length"])/2-JJLoc_y
                        qubit.pad2.node.polylineShapeParams["JJ Stem Length"]=(padSpacing-qubit.geometryParamsDict["JJ Patch Length"])/2+JJLoc_y                        
                        
                        if isinstance(qubit,groundedQubit):
                            qubit.geometryParamsDict["Pad 2 Width"]=qubit.geometryParamsDict["JJ Stem Width"]
                        
                        unrotatedCenter=[JJLoc_x,JJLoc_y]
                        rotatedCenter=rotate(unrotatedCenter,qubit.geometryParamsDict["Angle"]) 
                        bottomElectrodeGDS,topElectrodeGDS,connectionsGDS,patchGDS=OtherComponents.JJGDSComponents(top_electrode_width=qubit.geometryParamsDict["JJ Top Electrode Width"],\
                                                                                                                   bot_electrode_width=qubit.geometryParamsDict["JJ Bottom Electrode Width"],\
                                                                                                                   rotate=qubit.geometryParamsDict["Angle"],\
                                                                                                                   dx=rotatedCenter[0]+centerX,\
                                                                                                                   dy=rotatedCenter[1]+centerY,\
                                                                                                                   chip=chip.index,\
                                                                                                                   patchLength=qubit.geometryParamsDict["JJ Patch Length"])
                        qubit.JJGDSs.append(JJGDS(patchGDS,topElectrodeGDS,bottomElectrodeGDS,connectionsGDS))
                    elif "doubleJJ" in qubit.generalParamsDict["Type"]:
                        for pad in qubit.padListGeom:
                            pad.node.polylineShape+="PlusDoubleJJ"   
                        qubit.pad1.node.polylineShapeParams["SQUID T Stem Length"]=padSpacing/2-\
                                                                                   qubit.geometryParamsDict["JJ Patch Length"]/2-\
                                                                                   qubit.geometryParamsDict["SQUID Stem Length"]-\
                                                                                   qubit.geometryParamsDict["SQUID T Head Length"]-\
                                                                                   JJLoc_y
                        qubit.pad2.node.polylineShapeParams["SQUID T Stem Length"]=padSpacing/2-\
                                                                                   qubit.geometryParamsDict["JJ Patch Length"]/2-\
                                                                                   qubit.geometryParamsDict["SQUID Stem Length"]-\
                                                                                   qubit.geometryParamsDict["SQUID T Head Length"]+\
                                                                                   JJLoc_y
                        if isinstance(qubit,groundedQubit):
                            qubit.geometryParamsDict["Pad 2 Width"]=qubit.geometryParamsDict["SQUID T Stem Width"]
                        for i in [pad.node for pad in qubit.padListGeom]:
                            i.polylineShapeParams["SQUID Stem Separation"]=qubit.geometryParamsDict["SQUID Stem Separation"]
                            i.polylineShapeParams["SQUID T Head Width"]=qubit.geometryParamsDict["SQUID T Head Width"]
                            i.polylineShapeParams["SQUID T Head Length"]=qubit.geometryParamsDict["SQUID T Head Length"]
                            i.polylineShapeParams["JJ Boundary"]=qubit.geometryParamsDict["JJ Boundary"]
                            i.polylineShapeParams["SQUID Stem Width"]=qubit.geometryParamsDict["SQUID Stem Width"]
                            i.polylineShapeParams["SQUID Stem Length"]=qubit.geometryParamsDict["SQUID Stem Length"]
                            i.polylineShapeParams["SQUID T Stem Width"]=qubit.geometryParamsDict["SQUID T Stem Width"]
                            
                            #Left. Takes advantage of symmetry. May need to be generalized if an off-symmetric JJ is needed. 
                            unrotatedCenter=[JJLoc_x+qubit.geometryParamsDict["SQUID Stem Separation"]/2,JJLoc_y]
                            rotatedCenter=rotate(unrotatedCenter,qubit.geometryParamsDict["Angle"]) 
                            bottomElectrodeGDS,topElectrodeGDS,connectionsGDS,patchGDS=OtherComponents.JJGDSComponents(top_electrode_width=qubit.geometryParamsDict["JJ Top Electrode Width"],\
                                                                                                                       bot_electrode_width=qubit.geometryParamsDict["JJ Bottom Electrode Width"],\
                                                                                                                       rotate=qubit.geometryParamsDict["Angle"],\
                                                                                                                       dx=rotatedCenter[0]+centerX,\
                                                                                                                       dy=rotatedCenter[1]+centerY,\
                                                                                                                       chip=chip.index,\
                                                                                                                       patchLength=qubit.geometryParamsDict["JJ Patch Length"])
                            qubit.JJGDSs.append(JJGDS(patchGDS,topElectrodeGDS,bottomElectrodeGDS,connectionsGDS))
                            #Right
                            unrotatedCenter=[JJLoc_x-qubit.geometryParamsDict["SQUID Stem Separation"]/2,JJLoc_y]
                            rotatedCenter=rotate(unrotatedCenter,qubit.geometryParamsDict["Angle"]) 
                            bottomElectrodeGDS,topElectrodeGDS,connectionsGDS,patchGDS=OtherComponents.JJGDSComponents(top_electrode_width=qubit.geometryParamsDict["JJ Top Electrode Width"],\
                                                                                                                       bot_electrode_width=qubit.geometryParamsDict["JJ Bottom Electrode Width"],\
                                                                                                                       rotate=qubit.geometryParamsDict["Angle"],\
                                                                                                                       dx=rotatedCenter[0]+centerX,\
                                                                                                                       dy=rotatedCenter[1]+centerY,\
                                                                                                                       chip=chip.index,\
                                                                                                                       patchLength=qubit.geometryParamsDict["JJ Patch Length"])
                            qubit.JJGDSs.append(JJGDS(patchGDS,topElectrodeGDS,bottomElectrodeGDS,connectionsGDS))
                    for pad in qubit.padListGeom:
                        pad.node.polylineShapeParams["Body Width"]=qubit.geometryParamsDict["Pad "+str(pad.index)+" Width"]
                        pad.node.polylineShapeParams["Body Length"]=qubit.geometryParamsDict["Pad "+str(pad.index)+" Length"]
                        pad.node.height=qubit.geometryParamsDict["Pad "+str(pad.index)+" Height"]
                        for side in [1,2,3,4]:
                            pad.node.polylineShapeParams["Side "+str(side)+" Boundary"]=qubit.geometryParamsDict["Pad "+str(pad.index)+" Side "+str(side)+" Boundary"]
                #Common to all qubit geometries
                for qubitPad in qubit.padListGeom:
                    qubitPad.node.polylineShapeParams["Mesh Boundary"]=self.sysParams["Anti-Vortex Mesh Boundary"]
                    qubitPad.node.updatePolylines()
                    #Z values
                    if chipIndex==0:
                        qubitPad.node.Z=self.chipDict[0].substrate.node.height
                    elif chipIndex==1:
                        qubitPad.node.Z=self.chipDict[1].substrate.node.Z-qubitPad.node.height
            #Readout Resonators
            for readoutResonatorIndex,readoutResonator in chip.readoutResonatorDict.items():
                readoutResonator.geometryParamsDict=readSingleRowData(fileLines,readoutResonator.name)
                #Z values 
                for resonatorPadNode in [readoutResonator.pad1.node,readoutResonator.pad2.node]:
                    if chipIndex==0:
                        resonatorPadNode.Z=self.chipDict[0].substrate.node.height
                    elif chipIndex==1:
                        resonatorPadNode.Z=self.chipDict[1].substrate.node.Z-resonatorPadNode.height 
                #Mesh boundary
                readoutResonator.pad1.node.polylineShapeParams["Mesh Boundary"]=self.sysParams["Anti-Vortex Mesh Boundary"]
                readoutResonator.pad2.node.polylineShapeParams["Mesh Boundary"]=self.sysParams["Anti-Vortex Mesh Boundary"]
                #Meanders
                readoutResonator.updateMeanderNode(self.CPW)
                #Height
                readoutResonator.pad1.node.height=readoutResonator.geometryParamsDict["Pad 1 Height"]
                readoutResonator.pad2.node.height=readoutResonator.geometryParamsDict["Pad 2 Height"]
                #Pad Polylines
                readoutResonator.pad1.node.polylineShape="rectangle-PlusFinger(s)"
                readoutResonator.pad2.node.polylineShape="rectangle-PlusFinger(s)"
                readoutResonator.pad1.node.polylineShapeParams["Number of Fingers"]=1
                readoutResonator.pad2.node.polylineShapeParams["Number of Fingers"]=1
                
                #pad1NormalizedCenterPoint=[0,readoutResonator.geometryParamsDict["Pad Separation"]/2]#"Normalized" here means where the resonator is oriented along the y-axis with its center coordinates at the origin. 
                #pad2NormalizedCenterPoint=[0,-readoutResonator.geometryParamsDict["Pad Separation"]/2]
                #pad1RealCenterPoint=translate(rotate(pad1NormalizedCenterPoint,readoutResonator.geometryParamsDict["Angle"]),readoutResonator.geometryParamsDict["Center X"],readoutResonator.geometryParamsDict["Center Y"])
                #pad2RealCenterPoint=translate(rotate(pad2NormalizedCenterPoint,readoutResonator.geometryParamsDict["Angle"]),readoutResonator.geometryParamsDict["Center X"],readoutResonator.geometryParamsDict["Center Y"])
                
                pad1RealCenterPoint=translate(rotate([0,readoutResonator.geometryParamsDict["Pad 1 Length"]/2+readoutResonator.geometryParamsDict["Pad T Stem Length"]],readoutResonator.meanderStartAngle+np.pi/2),\
                                              readoutResonator.meanderStartPoint[0],\
                                              readoutResonator.meanderStartPoint[1])
                pad2RealCenterPoint=translate(rotate([0,readoutResonator.geometryParamsDict["Pad 2 Length"]/2+readoutResonator.geometryParamsDict["Pad T Stem Length"]],readoutResonator.meanderEndAngle+3*np.pi/2),\
                                              readoutResonator.meanderEndPoint[0],\
                                              readoutResonator.meanderEndPoint[1])
                
                readoutResonator.pad1.node.polylineShapeParams["Body Center X"]=pad1RealCenterPoint[0]
                readoutResonator.pad1.node.polylineShapeParams["Body Center Y"]=pad1RealCenterPoint[1]
                readoutResonator.pad1.node.polylineShapeParams["Angle"]=readoutResonator.meanderStartAngle+3*np.pi/2
                readoutResonator.pad2.node.polylineShapeParams["Body Center X"]=pad2RealCenterPoint[0]
                readoutResonator.pad2.node.polylineShapeParams["Body Center Y"]=pad2RealCenterPoint[1]
                readoutResonator.pad2.node.polylineShapeParams["Angle"]=readoutResonator.meanderEndAngle+np.pi/2
                
                #pad1Params=[param for param in readoutResonator.geometryParamsDict if param[0:5]=="Pad 1"]
                readoutResonator.pad1.node.polylineShapeParams["Body Width"]=readoutResonator.geometryParamsDict["Pad 1 Width"]
                readoutResonator.pad1.node.polylineShapeParams["Body Length"]=readoutResonator.geometryParamsDict["Pad 1 Length"]
                readoutResonator.pad1.node.polylineShapeParams["Body Height"]=readoutResonator.geometryParamsDict["Pad 1 Height"]
                readoutResonator.pad1.node.polylineShapeParams["Side 1 Boundary"]=readoutResonator.geometryParamsDict["Pad 1 Side 1 Boundary"]
                readoutResonator.pad1.node.polylineShapeParams["Side 2 Boundary"]=readoutResonator.geometryParamsDict["Pad 1 Side 2 Boundary"]
                readoutResonator.pad1.node.polylineShapeParams["Side 3 Boundary"]=readoutResonator.geometryParamsDict["Pad 1 Side 3 Boundary"]
                readoutResonator.pad1.node.polylineShapeParams["Side 4 Boundary"]=readoutResonator.geometryParamsDict["Pad 1 Side 4 Boundary"]
                
                #pad2Params=[param for param in readoutResonator.geometryParamsDict if param[0:5]=="Pad 2"]
                readoutResonator.pad2.node.polylineShapeParams["Body Width"]=readoutResonator.geometryParamsDict["Pad 2 Width"]
                readoutResonator.pad2.node.polylineShapeParams["Body Length"]=readoutResonator.geometryParamsDict["Pad 2 Length"]
                readoutResonator.pad2.node.polylineShapeParams["Body Height"]=readoutResonator.geometryParamsDict["Pad 2 Height"]
                readoutResonator.pad2.node.polylineShapeParams["Side 1 Boundary"]=readoutResonator.geometryParamsDict["Pad 2 Side 1 Boundary"]
                readoutResonator.pad2.node.polylineShapeParams["Side 2 Boundary"]=readoutResonator.geometryParamsDict["Pad 2 Side 2 Boundary"]
                readoutResonator.pad2.node.polylineShapeParams["Side 3 Boundary"]=readoutResonator.geometryParamsDict["Pad 2 Side 3 Boundary"]
                readoutResonator.pad2.node.polylineShapeParams["Side 4 Boundary"]=readoutResonator.geometryParamsDict["Pad 2 Side 4 Boundary"]
                
                #Pad T
                for padName in ["Pad 1","Pad 2"]:
                    if padName=="Pad 1":
                        thisNode=readoutResonator.pad1.node
                    elif padName=="Pad 2":
                        thisNode=readoutResonator.pad2.node
                    thisNode.polylineShapeParams["Finger Spacing"]=0
                    thisNode.polylineShapeParams["Finger 0 Stem Length"]=readoutResonator.geometryParamsDict["Pad T Stem Length"]/2
                    thisNode.polylineShapeParams["Finger 0 Stem Width"]=self.CPW.geometryParamsDict["Width"]
                    thisNode.polylineShapeParams["Finger Stem Boundary"]=self.CPW.geometryParamsDict["Gap"]
                    thisNode.polylineShapeParams["Finger 0 T Head Length"]=readoutResonator.geometryParamsDict["Pad T Stem Length"]/2
                    thisNode.polylineShapeParams["Finger 0 T Width"]=self.CPW.geometryParamsDict["Width"]
                    thisNode.polylineShapeParams["Finger 0 T Side 1 Boundary"]=self.CPW.geometryParamsDict["Gap"]
                    thisNode.polylineShapeParams["Finger 0 T Side 2 Boundary"]=1
                    thisNode.polylineShapeParams["Finger 0 T Side 3 Boundary"]=self.CPW.geometryParamsDict["Gap"]
                    thisNode.polylineShapeParams["Finger 0 T Side 4 Boundary"]=1
  
                readoutResonator.pad1.node.updatePolylines()
                readoutResonator.pad2.node.updatePolylines()              
            #PTCs
            for PTCIndex,PTC in chip.PTCDict.items():
                PTC.geometryParamsDict=readSingleRowData(fileLines,PTC.name)
                #Height
                PTC.pad1.node.height=PTC.geometryParamsDict["Height"]
                PTC.pad2.node.height=PTC.geometryParamsDict["Height"]
                #Polylines
                PTC.pad1.node.polylineShape="rectangle-PlusDoubleJJ"
                PTC.pad2.node.polylineShape="rectangle-PlusDoubleJJ-sideT"
                pad1BodyLength=0.0001#The "body" here is just an artifact of the rectangle-plusDoubleJJ shape.
                squidTStemLength=PTC.geometryParamsDict["SQUID T Stem Length"]
                padSpacing=2*PTC.geometryParamsDict["SQUID Stem Length"]+\
                           PTC.geometryParamsDict["SQUID Patch Length"]+\
                           2*PTC.geometryParamsDict["SQUID T Head Length"]+\
                           2*squidTStemLength
                PTCNormalizedSquidCenter=[0,-PTC.geometryParamsDict["End Separation"]/2-pad1BodyLength-padSpacing/2]
                PTCSQUIDCenter=translate(rotate(PTCNormalizedSquidCenter,PTC.geometryParamsDict["Angle"]),\
                                         PTC.geometryParamsDict["Center X"],\
                                         PTC.geometryParamsDict["Center Y"])
                #For SQUIDPad[N]NormalizedCenterPoint, the center is at the center of the squid. 
                SQUIDPad1NormalizedCenterPoint=[0,padSpacing/2+pad1BodyLength/2]
                pad1CenterPoint=translate(rotate(SQUIDPad1NormalizedCenterPoint,\
                                                 PTC.geometryParamsDict["Angle"]),\
                                          PTCSQUIDCenter[0],\
                                          PTCSQUIDCenter[1])
                
                PTC.pad1.node.polylineShapeParams["Body Center X"]=pad1CenterPoint[0]
                PTC.pad1.node.polylineShapeParams["Body Center Y"]=pad1CenterPoint[1]
                PTC.pad1.node.polylineShapeParams["Angle"]=PTC.geometryParamsDict["Angle"]
                PTC.pad1.node.polylineShapeParams["Body Width"]=self.CPW.geometryParamsDict["Width"]
                PTC.pad1.node.polylineShapeParams["Body Length"]=pad1BodyLength
                PTC.pad1.node.polylineShapeParams["Body Height"]=PTC.geometryParamsDict["Height"]
                PTC.pad1.node.polylineShapeParams["Side 1 Boundary"]=self.CPW.geometryParamsDict["Gap"]
                PTC.pad1.node.polylineShapeParams["Side 2 Boundary"]=0
                PTC.pad1.node.polylineShapeParams["Side 3 Boundary"]=self.CPW.geometryParamsDict["Gap"]
                PTC.pad1.node.polylineShapeParams["Side 4 Boundary"]=0
                PTC.pad1.node.polylineShapeParams["JJ Stem X"]=0
                
                SQUIDPad2NormalizedCenterPoint=[0,-padSpacing/2-PTC.geometryParamsDict["SQUID Bar Length"]/2]
                pad2CenterPoint=translate(rotate(SQUIDPad2NormalizedCenterPoint,\
                                                 PTC.geometryParamsDict["Angle"]),\
                                          PTCSQUIDCenter[0],\
                                          PTCSQUIDCenter[1])
                PTC.pad2.node.polylineShapeParams["Body Center X"]=pad2CenterPoint[0]
                PTC.pad2.node.polylineShapeParams["Body Center Y"]=pad2CenterPoint[1]
                PTC.pad2.node.polylineShapeParams["Angle"]=PTC.geometryParamsDict["Angle"]+np.pi#Addition of pi is so the stem points the right way.
                PTC.pad2.node.polylineShapeParams["Body Width"]=PTC.geometryParamsDict["SQUID Bar Width"]
                PTC.pad2.node.polylineShapeParams["Body Length"]=PTC.geometryParamsDict["SQUID Bar Length"]
                PTC.pad2.node.polylineShapeParams["Body Height"]=PTC.geometryParamsDict["Height"]
                PTC.pad2.node.polylineShapeParams["Side 1 Boundary"]=PTC.geometryParamsDict["SQUID Bar Boundary"]
                PTC.pad2.node.polylineShapeParams["Side 2 Boundary"]=PTC.geometryParamsDict["SQUID Bar Boundary"]
                PTC.pad2.node.polylineShapeParams["Side 3 Boundary"]=PTC.geometryParamsDict["SQUID Bar Boundary"]
                PTC.pad2.node.polylineShapeParams["Side 4 Boundary"]=PTC.geometryParamsDict["SQUID Bar Boundary"]
                PTC.pad2.node.polylineShapeParams["JJ Stem X"]=0
                PTC.pad2.node.polylineShapeParams["Side T Width"]=PTC.geometryParamsDict["SQUID Bar T Width"]
                PTC.pad2.node.polylineShapeParams["Side T Length"]=PTC.geometryParamsDict["SQUID Bar T Length"]
                PTC.pad2.node.polylineShapeParams["Side T Boundary"]=PTC.geometryParamsDict["SQUID Bar T Boundary"]
                for i in [PTC.pad1.node,PTC.pad2.node]:
                    i.polylineShapeParams["SQUID Stem Separation"]=PTC.geometryParamsDict["SQUID Stem Separation"]
                    i.polylineShapeParams["SQUID T Head Width"]=PTC.geometryParamsDict["SQUID T Head Width"]
                    i.polylineShapeParams["SQUID T Head Length"]=PTC.geometryParamsDict["SQUID T Head Length"]
                    i.polylineShapeParams["JJ Boundary"]=PTC.geometryParamsDict["SQUID Boundary"]
                    i.polylineShapeParams["SQUID Stem Width"]=PTC.geometryParamsDict["SQUID Stem Width"]
                    i.polylineShapeParams["SQUID Stem Length"]=PTC.geometryParamsDict["SQUID Stem Length"]
                    i.polylineShapeParams["SQUID T Stem Width"]=self.CPW.geometryParamsDict["Width"]
                    i.polylineShapeParams["SQUID T Stem Length"]=squidTStemLength
                #Left.
                unrotatedCenter=[-PTC.geometryParamsDict["SQUID Stem Separation"]/2,0]
                rotatedCenter=rotate(unrotatedCenter,PTC.geometryParamsDict["Angle"]) 
                bottomElectrodeGDS,topElectrodeGDS,connectionsGDS,patchGDS=OtherComponents.JJGDSComponents(top_electrode_width=PTC.geometryParamsDict["JJ Top Electrode Width"],\
                                                                                                           bot_electrode_width=PTC.geometryParamsDict["JJ Bottom Electrode Width"],\
                                                                                                           rotate=PTC.geometryParamsDict["Angle"],\
                                                                                                           dx=rotatedCenter[0]+PTCSQUIDCenter[0],\
                                                                                                           dy=rotatedCenter[1]+PTCSQUIDCenter[1],\
                                                                                                           chip=chip.index,\
                                                                                                           patchLength=PTC.geometryParamsDict["SQUID Patch Length"])
                PTC.JJGDSs.append(JJGDS(patchGDS,topElectrodeGDS,bottomElectrodeGDS,connectionsGDS))
                #Right
                unrotatedCenter=[+PTC.geometryParamsDict["SQUID Stem Separation"]/2,0]
                rotatedCenter=rotate(unrotatedCenter,PTC.geometryParamsDict["Angle"]) 
                bottomElectrodeGDS,topElectrodeGDS,connectionsGDS,patchGDS=OtherComponents.JJGDSComponents(top_electrode_width=PTC.geometryParamsDict["JJ Top Electrode Width"],\
                                                                                                           bot_electrode_width=PTC.geometryParamsDict["JJ Bottom Electrode Width"],\
                                                                                                           rotate=PTC.geometryParamsDict["Angle"],\
                                                                                                           dx=rotatedCenter[0]+PTCSQUIDCenter[0],\
                                                                                                           dy=rotatedCenter[1]+PTCSQUIDCenter[1],\
                                                                                                           chip=chip.index,\
                                                                                                           patchLength=PTC.geometryParamsDict["SQUID Patch Length"])
                PTC.JJGDSs.append(JJGDS(patchGDS,topElectrodeGDS,bottomElectrodeGDS,connectionsGDS))
                
                
                #Mesh
                PTC.pad1.node.polylineShapeParams["Mesh Boundary"]=self.sysParams["Anti-Vortex Mesh Boundary"]
                PTC.pad2.node.polylineShapeParams["Mesh Boundary"]=self.sysParams["Anti-Vortex Mesh Boundary"]
                PTC.pad1.node.updatePolylines()
                PTC.pad2.node.updatePolylines()  
                #Z values 
                for PTCPadNode in [PTC.pad1.node,PTC.pad2.node]:
                    if chipIndex==0:
                        PTCPadNode.Z=self.chipDict[0].substrate.node.height
                    elif chipIndex==1:
                        PTCPadNode.Z=self.chipDict[1].substrate.node.Z-PTCPadNode.height 
                
                #Meanders
                PTC_CPW=CPW()
                PTC_CPW.geometryParamsDict["Width"]=PTC.geometryParamsDict["CPW Width"]
                PTC_CPW.geometryParamsDict["Gap"]=PTC.geometryParamsDict["CPW Gap"]
                
                PTC.updateMeanderNode(PTC_CPW)
            #Straight Bus Couplers
            for straightBusCouplerIndex,straightBusCoupler in chip.straightBusCouplerDict.items():
                straightBusCoupler.geometryParamsDict=readSingleRowData(fileLines,straightBusCoupler.name)
                geom=straightBusCoupler.geometryParamsDict
                #Height
                straightBusCoupler.pad1.node.height=geom["Height"]
                straightBusCoupler.pad2.node.height=geom["Height"]
                #Polyline Shape
                straightBusCoupler.pad1.node.polylineShape="rectangle-PlusFinger(s)"
                straightBusCoupler.pad2.node.polylineShape="rectangle-PlusFinger(s)"
                straightBusCoupler.pad1.node.polylineShapeParams["Number of Fingers"]=1
                straightBusCoupler.pad2.node.polylineShapeParams["Number of Fingers"]=1
                #Base Rectangle 
                pad1NormalizedCenterPoint=[0,+geom["SQUID Patch Length"]/2+geom["SQUID Stem Length"]+geom["SQUID T Head Length"]+geom["SQUID T Stem Length"]+geom["End Length"]/2]
                pad1CenterPoint=translate(rotate(pad1NormalizedCenterPoint,\
                                                 geom["Angle"]),\
                                          geom["Center X"],\
                                          geom["Center Y"])
                
                straightBusCoupler.pad1.node.polylineShapeParams["Body Center X"]=pad1CenterPoint[0]
                straightBusCoupler.pad1.node.polylineShapeParams["Body Center Y"]=pad1CenterPoint[1]
                straightBusCoupler.pad1.node.polylineShapeParams["Angle"]=geom["Angle"]
                straightBusCoupler.pad1.node.polylineShapeParams["Body Width"]=geom["End Width"]
                straightBusCoupler.pad1.node.polylineShapeParams["Body Length"]=geom["End Length"]
                straightBusCoupler.pad1.node.polylineShapeParams["Body Height"]=geom["Height"]
                straightBusCoupler.pad1.node.polylineShapeParams["Side 1 Boundary"]=geom["End Boundary"]
                straightBusCoupler.pad1.node.polylineShapeParams["Side 2 Boundary"]=0
                straightBusCoupler.pad1.node.polylineShapeParams["Side 3 Boundary"]=geom["End Boundary"]
                straightBusCoupler.pad1.node.polylineShapeParams["Side 4 Boundary"]=0
                straightBusCoupler.pad1.node.polylineShapeParams["JJ Stem X"]=0
                
                pad2NormalizedCenterPoint=[0,-geom["SQUID Patch Length"]/2-geom["SQUID Stem Length"]-geom["SQUID T Head Length"]-geom["SQUID T Stem Length"]-geom["End Length"]/2]
                pad2CenterPoint=translate(rotate(pad2NormalizedCenterPoint,\
                                                 geom["Angle"]),\
                                          geom["Center X"],\
                                          geom["Center Y"])
                straightBusCoupler.pad2.node.polylineShapeParams["Body Center X"]=pad2CenterPoint[0]
                straightBusCoupler.pad2.node.polylineShapeParams["Body Center Y"]=pad2CenterPoint[1]
                straightBusCoupler.pad2.node.polylineShapeParams["Angle"]=geom["Angle"]+np.pi
                straightBusCoupler.pad2.node.polylineShapeParams["Body Width"]=geom["End Width"]
                straightBusCoupler.pad2.node.polylineShapeParams["Body Length"]=geom["End Length"]
                straightBusCoupler.pad2.node.polylineShapeParams["Body Height"]=geom["Height"]
                straightBusCoupler.pad2.node.polylineShapeParams["Side 1 Boundary"]=geom["End Boundary"]
                straightBusCoupler.pad2.node.polylineShapeParams["Side 2 Boundary"]=0
                straightBusCoupler.pad2.node.polylineShapeParams["Side 3 Boundary"]=geom["End Boundary"]
                straightBusCoupler.pad2.node.polylineShapeParams["Side 4 Boundary"]=0
                straightBusCoupler.pad2.node.polylineShapeParams["JJ Stem X"]=0
                
                fingerStemLength=(geom["Total Length"]\
                                  -4*geom["End Length"]\
                                  -geom["SQUID Patch Length"]\
                                  -2*geom["SQUID Stem Length"]\
                                  -2*geom["SQUID T Head Length"]\
                                  -2*geom["SQUID T Stem Length"])/2
                
                
                for padName in ["Pad 1","Pad 2"]:
                    if padName=="Pad 1":
                        thisNode=straightBusCoupler.pad1.node
                    elif padName=="Pad 2":
                        thisNode=straightBusCoupler.pad2.node
                    thisNode.polylineShapeParams["Finger Spacing"]=0
                    thisNode.polylineShapeParams["Finger 0 Stem Length"]=fingerStemLength
                    thisNode.polylineShapeParams["Finger 0 Stem Width"]=geom["Body Width"]
                    thisNode.polylineShapeParams["Finger Stem Boundary"]=geom["Body Boundary"]
                    thisNode.polylineShapeParams["Finger 0 T Head Length"]=geom["End Length"]
                    thisNode.polylineShapeParams["Finger 0 T Width"]=geom["End Width"]
                    thisNode.polylineShapeParams["Finger 0 T Side 1 Boundary"]=0
                    thisNode.polylineShapeParams["Finger 0 T Side 2 Boundary"]=0
                    thisNode.polylineShapeParams["Finger 0 T Side 3 Boundary"]=0
                    thisNode.polylineShapeParams["Finger 0 T Side 4 Boundary"]=0
                #JJ additions
                straightBusCoupler.pad1.node.polylineShape+="PlusDoubleJJ"
                straightBusCoupler.pad2.node.polylineShape+="PlusDoubleJJ"
                for i in [straightBusCoupler.pad1.node,straightBusCoupler.pad2.node]:
                    i.polylineShapeParams["SQUID Stem Separation"]=geom["SQUID Stem Separation"]
                    i.polylineShapeParams["SQUID T Head Width"]=geom["SQUID T Head Width"]
                    i.polylineShapeParams["SQUID T Head Length"]=geom["SQUID T Head Length"]
                    i.polylineShapeParams["JJ Boundary"]=geom["SQUID Boundary"]
                    i.polylineShapeParams["SQUID Stem Width"]=geom["SQUID Stem Width"]
                    i.polylineShapeParams["SQUID Stem Length"]=geom["SQUID Stem Length"]
                    i.polylineShapeParams["SQUID T Stem Width"]=geom["SQUID T Stem Width"]
                    i.polylineShapeParams["SQUID T Stem Length"]=geom["SQUID T Stem Length"]
                #Left. Takes advantage of symmetry. May need to be generalized if an off-symmetric JJ is needed. 
                unrotatedCenter=[geom["SQUID Stem Separation"]/2,0]
                rotatedCenter=rotate(unrotatedCenter,geom["Angle"]) 
                bottomElectrodeGDS,topElectrodeGDS,connectionsGDS,patchGDS=OtherComponents.JJGDSComponents(top_electrode_width=geom["JJ Top Electrode Width"],\
                                                                                                           bot_electrode_width=geom["JJ Bottom Electrode Width"],\
                                                                                                           rotate=geom["Angle"],\
                                                                                                           dx=rotatedCenter[0]+geom["Center X"],\
                                                                                                           dy=rotatedCenter[1]+geom["Center Y"],\
                                                                                                           chip=chip.index,\
                                                                                                           patchLength=geom["SQUID Patch Length"])
                straightBusCoupler.JJGDSs.append(JJGDS(patchGDS,topElectrodeGDS,bottomElectrodeGDS,connectionsGDS))
                #Right
                unrotatedCenter=[-geom["SQUID Stem Separation"]/2,0]
                rotatedCenter=rotate(unrotatedCenter,geom["Angle"]) 
                bottomElectrodeGDS,topElectrodeGDS,connectionsGDS,patchGDS=OtherComponents.JJGDSComponents(top_electrode_width=geom["JJ Top Electrode Width"],\
                                                                                                           bot_electrode_width=geom["JJ Bottom Electrode Width"],\
                                                                                                           rotate=geom["Angle"],\
                                                                                                           dx=rotatedCenter[0]+geom["Center X"],\
                                                                                                           dy=rotatedCenter[1]+geom["Center Y"],\
                                                                                                           chip=chip.index,\
                                                                                                           patchLength=geom["SQUID Patch Length"])
                straightBusCoupler.JJGDSs.append(JJGDS(patchGDS,topElectrodeGDS,bottomElectrodeGDS,connectionsGDS))
                #Common to all straightBusCoupler geometries
                for straightBusCouplerNode in [straightBusCoupler.pad1.node,straightBusCoupler.pad2.node]:
                    straightBusCouplerNode.polylineShapeParams["Mesh Boundary"]=self.sysParams["Anti-Vortex Mesh Boundary"]
                    
                straightBusCoupler.pad1.node.updatePolylines()
                straightBusCoupler.pad2.node.updatePolylines()
                #Z values
                for straightBusCouplerNode in [straightBusCoupler.pad1.node,straightBusCoupler.pad2.node]:
                    if chipIndex==0:
                        straightBusCouplerNode.Z=self.chipDict[0].substrate.node.height
                    elif chipIndex==1:
                        straightBusCouplerNode.Z=self.chipDict[1].substrate.node.Z-straightBusCouplerNode.height
            #Control Lines  
            for controlLineIndex,controlLine in chip.controlLineDict.items():
                controlLine.geometryParamsDict=readSingleRowData(fileLines,controlLine.name)
                #Height
                controlLine.lineNode.height=self.CPW.geometryParamsDict["Height"]
                #Path Polyline
                controlLine.lineNode.polylineShape="path"
                controlLine.lineNode.polylineShapeParams["CPW"]=self.CPW
                controlLine.lineNode.polylineShapeParams["Mesh Boundary"]=self.sysParams["Anti-Vortex Mesh Boundary"]
                for param in controlLine.geometryParamsDict:
                    controlLine.lineNode.polylineShapeParams[param]=controlLine.geometryParamsDict[param]
                controlLine.lineNode.updatePolylines()         
                #Drive line option
                if controlLine.generalParamsDict["Type"]=="drive":
                    loopCutout1Width=controlLine.geometryParamsDict["End Gap"]
                    loopCutout1Length=self.CPW.geometryParamsDict["Width"]+2*self.CPW.geometryParamsDict["Gap"]
                    loopCutout1RawCenter=[loopCutout1Width/2-traceBuffer,0]#Raw=assuming path endpoint is at [0,0]
                    loopCutout1RawPolyline=rectanglePolyline(centerX=loopCutout1RawCenter[0],\
                                                             centerY=loopCutout1RawCenter[1],\
                                                             width=loopCutout1Width,\
                                                             length=loopCutout1Length,\
                                                             angle=0)
                    loopCutout1RotatedPolyline=[rotate(point,controlLine.lineNode.endAngle) for point in loopCutout1RawPolyline]
                    loopCutout1TranslatedPolyline=[translate(point,controlLine.lineNode.endPoint[0],controlLine.lineNode.endPoint[1]) for point in loopCutout1RotatedPolyline]
                    controlLine.lineNode.peripheryPolylines.append(loopCutout1TranslatedPolyline)
                #Flux bias option
                if controlLine.generalParamsDict["Type"]=="fluxBias":
                    loopThickness=controlLine.geometryParamsDict["loopThickness"]
                    loopSeg1Length=controlLine.geometryParamsDict["loopSeg1Length"]
                    loopSeg2Length=controlLine.geometryParamsDict["loopSeg2Length"]
                    loopSeg3Length=controlLine.geometryParamsDict["loopSeg3Length"] 
                    loopSeg1Boundary=controlLine.geometryParamsDict["loopSeg1Boundary"]
                    loopSeg2Boundary=controlLine.geometryParamsDict["loopSeg2Boundary"]
                    loopSeg3Boundary=controlLine.geometryParamsDict["loopSeg3Boundary"]
                    
                    loopCutout1Width=loopSeg1Length
                    loopCutout1Length=loopSeg1Boundary+loopSeg2Length-loopThickness
                    loopCutout1RawCenter=[loopCutout1Width/2-traceBuffer,\
                                          -(loopSeg2Length-loopThickness-loopCutout1Length/2-self.CPW.geometryParamsDict["Width"]/2)]#Raw=assuming path endpoint is at [0,0]
                    loopCutout1RawPolyline=rectanglePolyline(centerX=loopCutout1RawCenter[0],\
                                                             centerY=loopCutout1RawCenter[1],\
                                                             width=loopCutout1Width,\
                                                             length=loopCutout1Length,\
                                                             angle=0)
                    loopCutout1RotatedPolyline=[rotate(point,controlLine.lineNode.endAngle) for point in loopCutout1RawPolyline]
                    loopCutout1TranslatedPolyline=[translate(point,controlLine.lineNode.endPoint[0],controlLine.lineNode.endPoint[1]) for point in loopCutout1RotatedPolyline]
                    controlLine.lineNode.peripheryPolylines.append(loopCutout1TranslatedPolyline)
                    
                    loopCutout2Width=loopSeg3Length+loopSeg2Boundary
                    loopCutout2Length=loopSeg2Length+loopSeg1Boundary+loopSeg3Boundary
                    loopCutout2RawCenter=[loopSeg1Length-loopSeg3Length+loopCutout2Width/2,
                                          -loopCutout2Length/2+self.CPW.geometryParamsDict["Width"]/2+loopSeg1Boundary]#Raw=assuming path endpoint is at [0,0]
                    loopCutout2RawPolyline=rectanglePolyline(centerX=loopCutout2RawCenter[0],\
                                                             centerY=loopCutout2RawCenter[1],\
                                                             width=loopCutout2Width,\
                                                             length=loopCutout2Length,\
                                                             angle=0)
                    loopCutout2RotatedPolyline=[rotate(point,controlLine.lineNode.endAngle) for point in loopCutout2RawPolyline]
                    loopCutout2TranslatedPolyline=[translate(point,controlLine.lineNode.endPoint[0],controlLine.lineNode.endPoint[1]) for point in loopCutout2RotatedPolyline]
                    controlLine.lineNode.peripheryPolylines.append(loopCutout2TranslatedPolyline)
                    #Loop
                    insertIndex=int(len(controlLine.lineNode.polyline)/2-1) #Minus one is so we can insert the short to ground
                    seg3Buffer=0#May be needed when generating GDS
                    loopSeg3Length+=seg3Buffer

                    point1=controlLine.lineNode.polyline[insertIndex]
                    point2=controlLine.lineNode.polyline[insertIndex]
                    shortThickness=loopThickness
                    shortLength=self.CPW.geometryParamsDict["Gap"]
                    shortPoint=[point2[0]-shortThickness*np.cos(controlLine.lineNode.endAngle),point2[1]-shortThickness*np.sin(controlLine.lineNode.endAngle)]
                    
                    
                    loopPolylineRaw=[[-shortThickness,0],\
                                     [-shortThickness,shortLength],\
                                     [0,shortLength],\
                                     [0,0],\
                                     [loopSeg1Length,0],\
                                     [loopSeg1Length,-loopSeg2Length],\
                                     [loopSeg1Length-loopSeg3Length,-loopSeg2Length],
                                     [loopSeg1Length-loopSeg3Length,-loopSeg2Length+loopThickness],\
                                     [loopSeg1Length-loopThickness,-loopSeg2Length+loopThickness],\
                                     [loopSeg1Length-loopThickness,-loopThickness],\
                                     [0,-loopThickness]]
                    loopPolylineRotated=[rotate(point,controlLine.lineNode.endAngle) for point in loopPolylineRaw]
                    traceEdgePoint=translate(rotate([0,self.CPW.geometryParamsDict["Width"]/2],controlLine.lineNode.endAngle),controlLine.lineNode.endPoint[0],controlLine.lineNode.endPoint[1])
                    loopPolylineTranslated=[translate(point,traceEdgePoint[0],traceEdgePoint[1]) for point in loopPolylineRotated]
                    controlLine.lineNode.polyline=controlLine.lineNode.polyline[0:insertIndex]+loopPolylineTranslated+controlLine.lineNode.polyline[insertIndex+1:]#Plus one is because the corner point is included in loopPolylineRaw

                #Z values 
                if chipIndex==0:
                    controlLine.lineNode.Z=self.chipDict[0].substrate.node.height
                elif chipIndex==1:
                    controlLine.lineNode.Z=self.chipDict[1].substrate.node.Z-straightBusCouplerPadNode.height
                #Launch pads
                controlLine.updateLaunchPadNodes()
        #If flip chip update bump nodes
        if self.sysParams["Flip Chip?"]=="Yes":
            self.updateBumpsDict()  
    def generateNetlistComponents(self,circuitSim):#Contains the feedline model. Adds 50ohm resistors to feedline if simulation doesn't call for ports there, but otherwise simulation-independent.
        netlistComponents={"Capacitances":dict(),\
                           "Inductors":dict(),\
                           "Resistors":dict(),\
                           "Transmission Lines":dict(),\
                           "PTCs":dict(),\
                           "Feedline Sections":dict()}
        #Capacitances--------------------------------------------------------------------------------------------------- 
        #Everything that doesn't involve the feedline.
        for index1,node1Name in enumerate(self.ansysCapMatHeaders):#Iterate through the capacitance matrix
            for index2,node2Name in enumerate(self.ansysCapMatHeaders):#So it's like (0,0),(0,1),(0,2),(1,1),(1,2),(2,2).
                if "CL0" not in node1Name and "CL0" not in node2Name:
                    node1NetlistName=self.netlistName(node1Name,circuitSim)  
                    if index1==index2:#Capacitance to ground
                        capVal=sum(self.capMat[index1])
                        node2Name="G"
                        node2NetlistName=self.netlistName(node2Name,circuitSim)  
                    else:
                        capVal=-self.capMat[index1][index2]
                        node2Name=self.ansysCapMatHeaders[index2]
                        node2NetlistName=self.netlistName(node2Name,circuitSim)
                    capacitanceName="C"+node1Name+"_"+node2Name    
                    netlistComponents["Capacitances"][capacitanceName]={"node1NetlistName":node1NetlistName,\
                                                                        "node2NetlistName":node2NetlistName,\
                                                                        "C":capVal}
        #Feedline capacitance to resonator pad 1
        for readoutResonatorIndex,readoutResonator in self.allReadoutResonatorsDict.items():
            capVal=0
            node1Name=readoutResonator.pad1.node.name
            node1NetlistName=self.netlistName(node1Name,circuitSim)
            node2Name="F"+str(readoutResonatorIndex)
            node2NetlistName=self.netlistName(node2Name,circuitSim)
            if self.sysParams["Simulate Feedline?"]=="Yes":
                index1=self.ansysCapMatHeaders.index(node1Name)
                index2=self.ansysCapMatHeaders.index(self.allControlLinesDict[0].lineNode.name)
                capVal=-self.capMat[index1][index2]   
            elif self.sysParams["Simulate Feedline?"]=="No":
                capVal=readoutResonator.generalParamsDict["Capacitance to Feedline (F)"]
            capacitanceName="C"+node1Name+"_"+node2Name  
            netlistComponents["Capacitances"][capacitanceName]={"node1NetlistName":node1NetlistName,\
                                                                        "node2NetlistName":node2NetlistName,\
                                                                        "C":capVal}
        #Qubit inductances
        for qubitIndex,qubit in self.allQubitsDict.items():
            node1Name=qubit.pad1.node.name
            node1NetlistName=self.netlistName(node1Name,circuitSim)
            node2Name=qubit.pad2.node.name
            node2NetlistName=self.netlistName(node2Name,circuitSim)
            if isinstance(qubit,groundedQubit):
                node2Name="G"
                node2NetlistName
                node2NetlistName=self.netlistName(node2Name,circuitSim)
            
            
            inductorName="L"+node1Name+"_"+node2Name
            
            netlistComponents["Inductors"][inductorName]={"node1NetlistName":node1NetlistName,\
                                                          "node2NetlistName":node2NetlistName,\
                                                          "L":qubit.L_i_fixed}
        #Readout Resonators
        for readoutResonatorIndex,readoutResonator in self.allReadoutResonatorsDict.items():        
            node1Name=readoutResonator.pad1.node.name
            node1NetlistName=self.netlistName(node1Name,circuitSim)
            node2Name=readoutResonator.pad2.node.name
            node2NetlistName=self.netlistName(node2Name,circuitSim)
            resonatorName="T"+node1Name+"_"+node2Name
            netlistComponents["Transmission Lines"][resonatorName]={"node1NetlistName":node1NetlistName,\
                                                                    "node2NetlistName":node2NetlistName,\
                                                                    "TD":self.CPW.TD(readoutResonator.geometryParamsDict["Length"])}    
        #PTCs
        for PTCIndex,PTC in self.allPTCsDict.items():
            node1Name=PTC.pad1.node.name
            node1NetlistName=self.netlistName(node1Name,circuitSim)
            node2Name=PTC.pad2.node.name
            node2NetlistName=self.netlistName(node2Name,circuitSim)
            inductorName="L"+node1Name+"_"+node2Name
            
            
            netlistComponents["Transmission Lines"]["T"+node1Name+"_G"]={"node1NetlistName":node1NetlistName,\
                                                                         "node2NetlistName":"G",\
                                                                         "TD":PTC.TD}
            
            netlistComponents["Inductors"][inductorName]={"node1NetlistName":node1NetlistName,\
                                                          "node2NetlistName":node2NetlistName,\
                                                          "L":PTC.generalParamsDict["SQUID Inductance(H)"]}
                        
        #Feedline--------------------------------------------------------------------------------------------------------------------
        #There are always N+1 feedline sections corresponding to segments between the nodes FL,F1,F2,...FN,FR
        feedlineNodes=["FL"]#Note that the order defines the segments!
        for i in range(self.sysParams["Number of Readout Resonators"]):
            feedlineNodes.append("F"+str(i))#Must agree with the naming convention in the capacitances section!
        feedlineNodes.append("FR")
        for index,node1Name in enumerate(feedlineNodes[:-1]):#-1 since there are are one fewer segments than nodes. Should be number of qubits+1
            node1Name=feedlineNodes[index]
            node1NetlistName=self.netlistName(node1Name,circuitSim)
            node2Name=feedlineNodes[index+1]
            node2NetlistName=self.netlistName(node2Name,circuitSim)
            feedlineSectionName="T"+node1Name+"_"+node2Name
            if index==0:#If the first segment
                length=self.chipDict[0].controlLineDict[0].pathLengthFromStartToPoint([self.allReadoutResonatorsDict[0].pad1.node.centerX,\
                                                                                       self.allReadoutResonatorsDict[0].pad1.node.centerY])
                #print("Length Left:"+str(length))
            elif index==len(feedlineNodes)-2:#If the last segment...
                length=self.chipDict[0].controlLineDict[0].pathLengthFromEndToPoint([self.allReadoutResonatorsDict[self.sysParams["Number of Readout Resonators"]-1].pad1.node.centerX,\
                                                                                     self.allReadoutResonatorsDict[self.sysParams["Number of Readout Resonators"]-1].pad1.node.centerY])
                #print("Length Right:"+str(length))
            else:
                length=self.chipDict[0].controlLineDict[0].pathLengthPointToPoint([self.allReadoutResonatorsDict[index-1].pad1.node.centerX,\
                                                                                   self.allReadoutResonatorsDict[index-1].pad1.node.centerY],\
                                                                                  [self.allReadoutResonatorsDict[index].pad1.node.centerX,\
                                                                                   self.allReadoutResonatorsDict[index].pad1.node.centerY])
            netlistComponents["Transmission Lines"][feedlineSectionName]={"node1NetlistName":node1NetlistName,\
                                                                          "node2NetlistName":node2NetlistName,\
                                                                          "TD":self.CPW.TD(length)} 
        
        #Circuit simulation - specific modifications
        #Add matching resistors to feedline if there are no ports on either end
        if circuitSim[0:4]=="Y11Q" or \
            circuitSim[0:5]=="Y11BC" or \
            circuitSim[0:4]=="Z21Q" or \
            circuitSim[0:4]=="Y11R" or \
            circuitSim[0:6]=="YRestR" or \
            circuitSim[0:10]=="Y11LumpedR":
           
            netlistComponents["Resistors"]["RFL"]={"node1NetlistName":self.netlistName("G",circuitSim),\
                                                   "node2NetlistName":self.netlistName("FL",circuitSim),\
                                                   "R":50}#50 ohm
            netlistComponents["Resistors"]["RFR"]={"node1NetlistName":self.netlistName("G",circuitSim),\
                                                   "node2NetlistName":self.netlistName("FR",circuitSim),\
                                                   "R":50}#50 ohm
        if circuitSim[0:6]=="YRestR":#If YRestR circuitSim of lumpedR simulation, set shunt capacitances to 0 and short transmission line. See Junling's thesis Fig.4.13 and surrounding discussion.
            readoutResonatorIndex=int(circuitSim[6:])
            readoutResonator=self.allReadoutResonatorsDict[readoutResonatorIndex]
            node1Name=readoutResonator.pad1.node.name
            node1NetlistName=self.netlistName(node1Name,circuitSim)
            node2Name=readoutResonator.pad2.node.name
            node2NetlistName=self.netlistName(node2Name,circuitSim)
            resonatorName="T"+node1Name+"_"+node2Name
            netlistComponents["Transmission Lines"].pop(resonatorName)#Remove the resonator as per Junling's procedure. 
            netlistComponents["Capacitances"]["CR"+str(readoutResonatorIndex)+"Pad1_G"]["C"]=0
            netlistComponents["Capacitances"]["CR"+str(readoutResonatorIndex)+"Pad2_G"]["C"]=0
            netlistComponents["Capacitances"]["CR"+str(readoutResonatorIndex)+"Pad1_F"+str(readoutResonatorIndex)]["C"]=0#Remove capacitance to feedline. 
            
            netlistComponents["Resistors"]["RR"+str(readoutResonatorIndex)+"Pad1_R"+str(readoutResonatorIndex)+"Pad2"]={"node1NetlistName":self.netlistName(self.allReadoutResonatorsDict[readoutResonatorIndex].pad1.node.name,circuitSim),\
                                                                                                          "node2NetlistName":self.netlistName(self.allReadoutResonatorsDict[readoutResonatorIndex].pad2.node.name,circuitSim),\
                                                                                                          "R":0}#Short the two resonator fingers
        if circuitSim[0:10]=="Y11LumpedR":
            #Remove transmission line resonator
            readoutResonatorIndex=int(circuitSim[10:])
            readoutResonator=self.allReadoutResonatorsDict[readoutResonatorIndex]
            node1Name=readoutResonator.pad1.node.name
            node1NetlistName=self.netlistName(node1Name,circuitSim)
            node2Name=readoutResonator.pad2.node.name
            node2NetlistName=self.netlistName(node2Name,circuitSim)
            resonatorName="T"+node1Name+"_"+node2Name
            netlistComponents["Transmission Lines"].pop(resonatorName)#Remove the resonator as per Junling's procedure. 
            netlistComponents["Capacitances"].pop("CR"+str(readoutResonatorIndex)+"Pad1_R"+str(readoutResonatorIndex)+"Pad2")
            #Remove capacitance to ground since they were included in the calculation for equivC
            netlistComponents["Capacitances"].pop("CR"+str(readoutResonatorIndex)+"Pad1_G")
            #netlistComponents["Capacitances"]["CR"+str(readoutResonatorIndex)+"Pad2_G"]["C"]=0#Don't need this since it's overwritten later. But important concept. 
            #Add effective lumped resonator
            equivL,equivC=self.calculateLumpedResonator(index=readoutResonatorIndex)
            node1Name=readoutResonator.pad2.node.name#pad1 is chosen arbitrarily here, could be pad1 instead because they will end up shorted. 
            node1NetlistName=self.netlistName(node1Name,circuitSim)
            node2Name="G"
            node2NetlistName=self.netlistName(node2Name,circuitSim)
            inductorName="L"+node1Name+"_"+node2Name
            capacitanceName="C"+node1Name+"_"+node2Name 
            
            netlistComponents["Inductors"][inductorName]={"node1NetlistName":node1NetlistName,\
                                                          "node2NetlistName":node2NetlistName,\
                                                          "L":equivL}
            netlistComponents["Capacitances"][capacitanceName]={"node1NetlistName":node1NetlistName,\
                                                                "node2NetlistName":node2NetlistName,\
                                                                "C":equivC}
            netlistComponents["Resistors"]["RR"+str(readoutResonatorIndex)+"Pad1_R"+str(readoutResonatorIndex)+"Pad2"]={"node1NetlistName":self.netlistName(self.allReadoutResonatorsDict[readoutResonatorIndex].pad1.node.name,circuitSim),\
                                                                                                          "node2NetlistName":self.netlistName(self.allReadoutResonatorsDict[readoutResonatorIndex].pad2.node.name,circuitSim),\
                                                                                                          "R":0}#Short the two resonator fingers
        if circuitSim[0:4]=="Z21Q":
            qubitIndices=Z21QIndices(circuitSim)
            qubit1=self.allQubitsDict[qubitIndices[0]]
            qubit2=self.allQubitsDict[qubitIndices[1]]
            for qubit in qubit1,qubit2:
                netlistComponents["Inductors"].pop("L"+qubit.pad1.node.name+"_"+qubit.pad2.node.name)#Delete these inductance values. 
        return netlistComponents         
    def generateSimulationParametersFile(self,simType):#Contains simulation-specific info
        lines=[]
        if simType=="capMat":
            lines+=[["PerRefine","100"],\
                   ["MaxPass","99"]]
        if simType=="fullS21" or\
           simType[0:9]=="circFreqQ" or\
           simType[0:6]=="decayQ" or\
           simType[0:5]=="exchQ" or\
           simType[0:9]=="circFreqR" or\
           simType[0:7]=="lumpedR" or\
           simType[0:11]=="freqLumpedR" or\
           simType[0:17]=="feedlineCouplingR":
            
           lines+=[["Type",simType],\
                   ["LNA_start (GHz)","4"],\
                   ["LNA_stop (GHz)","7"],\
                   ["LNA_counts","200"]]
        elif simType[0:8]=="quantize":
            quantizeList="["
            for component in self.postGEComponentList:
                quantizeList=quantizeList+component.name+":"
            quantizeList=quantizeList[0:-1]+"]"
            lines+=[["QuantizeList",quantizeList],\
                    ["NumResonatorPhotons","5"],\
                    ["NumQubitPhotons","5"],\
                    ["TrigOrder","10"]]
        csvWrite(self.simFiles[simType]["Params"],lines)      
    
    def netlistName(self,nodeName,circuitSim): #This method returns the base netlist name or port name if applicable based on the particular circuit simulation 
        #circuitSimType=fullS21,Y11R[N],YRestR[N],Y11Q[N]
        if circuitSim=="fullS21":
            if nodeName=="FL":
                return "Port1"
            if nodeName=="FR":
                return "Port2"
        elif circuitSim[0:4]=="Y11Q":
            index=int(circuitSim[4:])
            if nodeName==self.allQubitsDict[index].pad1.node.name:
                return "Port1"
        elif circuitSim[0:5]=="Y11BC":#FL and FR are treated as just regular nodes connected to the grounded 50ohm resistor. 
            index=int(circuitSim[5:])
            if nodeName==self.allStraightBusCouplersDict[index].pad1.node.name:
                return "Port1"
        elif circuitSim[0:4]=="Z21Q":
            qubitIndices=Z21QIndices(circuitSim)
            if nodeName==self.allQubitsDict[qubitIndices[0]].pad1.node.name:
                return "Port1"
            if nodeName==self.allQubitsDict[qubitIndices[1]].pad1.node.name:
                return "Port2"
        elif circuitSim[0:4]=="Y11R":
            readoutResonatorIndex=int(circuitSim[4:])
            if nodeName==self.allReadoutResonatorsDict[readoutResonatorIndex].pad2.node.name:
                return "Port1"
        elif circuitSim[0:6]=="YRestR":
            readoutResonatorIndex=int(circuitSim[6:])
            if nodeName==self.allReadoutResonatorsDict[readoutResonatorIndex].pad2.node.name:
                return "Port1"
        elif circuitSim[0:10]=="Y11LumpedR":
            readoutResonatorIndex=int(circuitSim[10:])
            if nodeName==self.allReadoutResonatorsDict[readoutResonatorIndex].pad2.node.name:
                return "Port1"
        #Common to all simulation types------------------------        
        if nodeName=="G":
            return "0"
        return "net_"+nodeName#Default if not caught by any of the above 'if' statements. 
    def netlistPortsLines(self,circuitSim):#circuitSimType=fullS21,Y11R[N],YRestR[N],Y11Q[N]
        portNet2Dict=dict()
        if circuitSim=="fullS21" or circuitSim[0:4]=="Z21Q":#Two ports on different nodes. 
            port1Net2="G"#Grounded by default. This is the case for grounded qubits. 
            port2Net2="G"
            if circuitSim[0:4]=="Z21Q":
                qubitIndices=Z21QIndices(circuitSim)
                if isinstance(self.allQubitsDict[qubitIndices[0]],floatingQubit):
                    port1Net2=self.allQubitsDict[qubitIndices[0]].pad2.node.name
                if isinstance(self.allQubitsDict[qubitIndices[1]],floatingQubit):
                    port2Net2=self.allQubitsDict[qubitIndices[1]].pad2.node.name
            portNet2Dict[1]=self.netlistName(port1Net2,circuitSim)
            portNet2Dict[2]=self.netlistName(port2Net2,circuitSim)
        elif circuitSim[0:4]=="Y11R" or circuitSim[0:6]=="YRestR" or circuitSim[0:10]=="Y11LumpedR":#One grounded port on one node  
            portNet2Dict[1]=self.netlistName("G",circuitSim)
        elif circuitSim[0:4]=="Y11Q":#One port across the qubit. Whether it's grounded depends on floating vs. grounded qubit. 
            index=int(circuitSim[4:])
            if isinstance(self.allQubitsDict[index],floatingQubit):
                padName="Q"+str(index)+"Pad2"
            elif isinstance(self.allQubitsDict[index],groundedQubit):
                padName="G"
            portNet2Dict[1]=self.netlistName(padName,circuitSim)
        elif circuitSim[0:5]=="Y11BC":#One non-grounded port across the component. Port 1 is on Pad1   
            index=int(circuitSim[5:])
            padName="BC"+str(index)+"Pad2"
            portNet2Dict[1]=self.netlistName(padName,circuitSim)
        portsLines=[]
        for portIndex,portNet2 in portNet2Dict.items():
            portsLines=portsLines+["RPort"+str(portIndex)+" Port"+str(portIndex)+" "+portNet2+" PORTNUM="+str(portIndex)+" RZ=50\n",\
                                   ".PORT Port"+str(portIndex)+" "+portNet2+" "+str(portIndex)+" RPort"+str(portIndex)+"\n"]    
        return portsLines
    def copyAnsysFile(self,ansysFile):
        if os.path.exists(ansysFile):
            self.deleteFile(str(ansysFile))
        copyAEDTTemplateCommand=""
        if self.sysParams["Compute Location"]=="Windows":
            copyAEDTTemplateCommand="copy "+str(self.sysParams["QSM Source Folder"]/"helperFiles"/"template.aedt")+" "+str(ansysFile)
        if self.sysParams["Compute Location"]=="Cluster":
            copyAEDTTemplateCommand="cp "+str(self.sysParams["QSM Source Folder"]/"helperFiles"/"template.aedt")+" "+str(ansysFile)
        subprocess.call(copyAEDTTemplateCommand,shell=True)
    def loadAllData(self):
        self.loadComponentParametersFile()
        self.loadGeometriesFile()
        self.CPW.vp=self.CPW.generalParamsDict["Phase Velocity(um/s)"]
        for simTypeName,simTypeDict in self.simFiles.items():#capMat and quantize will be loaded here, among others.
            if os.path.exists(simTypeDict["ResultsFile"]):
                self.loadSimResults(simTypeName)
    def simulation(self,command):#Contains simulation-specific info
        simType=command[1]
        simStage=command[2]
        simParams=dict()
        if simStage=="init":
            #Create the directory if it doesn't yet exist.
            bashCommand=""
            if self.sysParams["Compute Location"]=="Windows":
                bashCommand="if not exist "+str(self.simFiles[simType]["Directory"])+" mkdir "+str(self.simFiles[simType]["Directory"])
                subprocess.call(bashCommand,shell=True)
            elif self.sysParams["Compute Location"]=="Cluster":
                subprocess.call("rm -rf "+str(self.simFiles[simType]["Directory"]),shell=True)
                bashCommand="mkdir -p "+str(self.simFiles[simType]["Directory"])
                subprocess.call(bashCommand,shell=True)
            self.generateSimulationParametersFile(simType)
        else:
            simParams=self.loadSimulationParametersFile(simType)
        if simStage=="run":  
            #Delete previous run files
            if self.sysParams["Compute Location"]=="Cluster":
                subprocess.call("rm -f "+str(self.simFiles[simType]["Directory"]/"/*slurm*"),shell=True)
                subprocess.call("rm -f "+str(self.simFiles[simType]["Directory"]/"/*script.*"),shell=True)
                subprocess.call("rm -f "+str(self.simFiles[simType]["Directory"]/"/nodes"),shell=True)
                subprocess.call("rm -f "+str(self.simFiles[simType]["Directory"]/"/*.log*"),shell=True)
                subprocess.call("rm -f "+str(self.simFiles[simType]["Directory"]/"/*Results*"),shell=True)
            ansysSimulatorPreamb=["import ScriptEnv\n",\
                                  "ScriptEnv.Initialize(\"Ansoft.ElectronicsDesktop\")\n",\
                                  "oDesktop.RestoreWindow()\n"]
            if simType=="quantize":
                copyQuantizeQubitSimulatorCommand="cp "+str(self.sysParams["QSM Source Folder"]/"helperFiles"/"quantizeQubitSimulator.py")+" "+self.simFiles[simType]["Directory"]
                subprocess.call(copyQuantizeQubitSimulatorCommand,shell=True)
                self.runQuantizeSimulator(self.simFiles[simType]["Directory"],120)
            for q3dSimName,q3dSim in self.simFiles[simType]["Q3D Simulations"].items():#Run all Q3D simulations for the given simulation. Assumes they were initialized when the Ansys file was created.
                self.copyAnsysFile(q3dSim["Ansys"])
                #Generate and run the Ansys simulator file
                lines=ansysSimulatorPreamb
                lines=lines+["oProject = oDesktop.SetActiveProject(\""+str(q3dSim["Ansys"]).split("/")[-1][0:-5]+"\")\n",\
                             "oProject.InsertDesign(\"Q3D Extractor\", \""+q3dSimName+"\", \"\", \"\")\n",\
                             "oDesign = oProject.SetActiveDesign(\""+q3dSimName+"\")\n"]
                if simType=="capMat":
                    lines=lines+self.capMatLayout_Lines()
                lines=lines+["oModuleAnalysis = oDesign.GetModule(\"AnalysisSetup\")\n",\
                             "oModuleAnalysis.InsertSetup(\"Matrix\",\n",\
                             "    [\n",\
                             "        \"NAME:capSim\",\n",\
                             "        \"AdaptiveFreq:=\"	, \"5GHz\",\n",\
                             "        \"SaveFields:=\"		, False,\n",\
                             "        \"Enabled:=\"		, True,\n",\
                             "        [\n",\
                             "            \"NAME:Cap\",\n",\
                             "            \"MaxPass:=\"		, "+str(simParams["MaxPass"])+",\n",\
                             "            \"MinPass:=\"		, 1,\n",\
                             "            \"MinConvPass:=\"		, 1,\n",\
                             "            \"PerError:=\"		, 1,\n",\
                             "            \"PerRefine:=\"		, "+str(simParams["PerRefine"])+",\n",\
                             "            \"AutoIncreaseSolutionOrder:=\", True,\n",\
                             "            \"SolutionOrder:=\"	, \"High\",\n",\
                             "            \"Solver Type:=\"		, \"Iterative\"\n",\
                             "        ]\n",\
                             "    ])\n",\
                             "oDesign.AnalyzeAll()\n",\
                             "oDesign.ExportMatrixData(\""+str(q3dSim["ResultsFile"])+"\", \"C\", \"\", \"capSim:LastAdaptive\", \"Original\", \"ohm\", \"nH\", \"pF\", \"mSie\", 1000000000, \"Maxwell,Spice,Couple\", 0, False, 5, 8, 0)\n"]
                lines.append(ansysSaveLine())   
                simulatorFileInstance=open(q3dSim["Simulator"],"w+",newline='')
                simulatorFileInstance.writelines(lines)
                simulatorFileInstance.close()                
                self.runAnsysSimulator(q3dSim["Ansys"],q3dSim["Simulator"],self.simFiles[simType]["Directory"],60)
            for hfssSimName,hfssSim in self.simFiles[simType]["HFSS Simulations"].items():#Run all HFSS simulations for the given simulation
                self.copyAnsysFile(hfssSim["Ansys"])
                #Generate and run the Ansys simulator file
                lines=ansysSimulatorPreamb
                lines=lines+["oProject = oDesktop.SetActiveProject(\""+hfssSim["Ansys"].split("/")[-1][0:-5]+"\")\n",\
                             "oProject.InsertDesign(\"HFSS\", \""+hfssSimName+"\", \"\", \"\")\n"
                             "oDesign = oProject.SetActiveDesign(\""+hfssSimName+"\")\n"]
                #Insert model generation lines here.
                lines=lines+["oModuleAnalysis = oDesign.GetModule(\"AnalysisSetup\")\n"
                             "oModuleAnalysis.InsertSetup(\"HfssDriven\",\n",\
                             "    [\n",\
                             "        \"NAME:Setup1\",\n",\
                             "        \"AdaptMultipleFreqs:=\"	, False,\n",\
                             "        \"Frequency:=\"		, \"5GHz\",\n",\
                             "        \"MaxDeltaS:=\"		, 0.02,\n",\
                             "        \"PortsOnly:=\"		, False,\n",\
                             "        \"UseMatrixConv:=\"	, False,\n",\
                             "        \"MaximumPasses:=\"	, 6,\n",\
                             "        \"MinimumPasses:=\"	, 1,\n",\
                             "        \"MinimumConvergedPasses:=\", 1,\n",\
                             "        \"PercentRefinement:=\"	, 30,\n",\
                             "        \"IsEnabled:=\"		, True,\n",\
                             "        [\n",\
                             "            \"NAME:MeshLink\",\n",\
                             "            \"ImportMesh:=\"		, False\n",\
                             "        ],\n",\
                             "        \"BasisOrder:=\"		, 1,\n",\
                             "        \"DoLambdaRefine:=\"	, True,\n",\
                             "        \"DoMaterialLambda:=\"	, True,\n",\
                             "        \"SetLambdaTarget:=\"	, False,\n",\
                             "        \"Target:=\"		, 0.3333,\n",\
                             "        \"UseMaxTetIncrease:=\"	, False,\n",\
                             "        \"PortAccuracy:=\"	, 2,\n",\
                             "        \"UseABCOnPort:=\"	, False,\n",\
                             "        \"SetPortMinMaxTri:=\"	, False,\n",\
                             "        \"UseDomains:=\"		, False,\n",\
                             "        \"UseIterativeSolver:=\"	, False,\n",\
                             "        \"SaveRadFieldsOnly:=\"	, False,\n",\
                             "        \"SaveAnyFields:=\"	, True,\n",\
                             "        \"IESolverType:=\"	, \"Auto\",\n",\
                             "        \"LambdaTargetForIESolver:=\", 0.15,\n",\
                             "        \"UseDefaultLambdaTgtForIESolver:=\", True\n",\
                             "    ])\n",\
                             "oModuleAnalysis.InsertFrequencySweep(\"Setup1\",\n",\
                             "    [\n",\
                             "        \"NAME:Sweep\",\n",\
                             "        \"IsEnabled:=\"		, True,\n",\
                             "        \"RangeType:=\"		, \"LinearCount\",\n",\
                             "        \"RangeStart:=\"		, \"5GHz\",\n",\
                             "        \"RangeEnd:=\"		, \"6GHz\",\n",\
                             "        \"RangeCount:=\"		, 10,\n",\
                             "        \"Type:=\"		, \"Fast\",\n",\
                             "        \"SaveFields:=\"		, False,\n",\
                             "        \"SaveRadFields:=\"	, False,\n",\
                             "        \"InterpTolerance:=\"	, 0.5,\n",\
                             "        \"InterpMaxSolns:=\"	, 250,\n",\
                             "        \"InterpMinSolns:=\"	, 0,\n",\
                             "        \"InterpMinSubranges:=\"	, 1,\n",\
                             "        \"ExtrapToDC:=\"		, False,\n",\
                             "        \"InterpUseS:=\"		, True,\n",\
                             "        \"InterpUsePortImped:=\"	, False,\n",\
                             "        \"InterpUsePropConst:=\"	, True,\n",\
                             "        \"UseDerivativeConvergence:=\", False,\n",\
                             "        \"InterpDerivTolerance:=\", 0.2,\n",\
                             "        \"UseFullBasis:=\"	, True,\n",\
                             "        \"EnforcePassivity:=\"	, True,\n",\
                             "        \"PassivityErrorTolerance:=\", 0.0001,\n",\
                             "    ])\n",\
                             "oDesign.AnalyzeAll()\n"]
                lines.append(ansysSaveLine()) 
                simulatorFileInstance=open(hfssSim["Simulator"],"w+",newline='')
                simulatorFileInstance.writelines(lines)
                simulatorFileInstance.close()                
                self.runAnsysSimulator(hfssSim["Ansys"],hfssSim["Simulator"],self.simFiles[simType]["Directory"],90)
            for circuitSimName,circuitSim in self.simFiles[simType]["Circuit Simulations"].items():#Initialize all circuit simulations for the given simulation.
                self.copyAnsysFile(circuitSim["Ansys"])
                #Generate the netlist file and load it into the AEDT
                netlistComponents=self.generateNetlistComponents(circuitSimName)
                writeFile = open(circuitSim["Netlist"], "w")
                writeFile.writelines(netlistHeaderLines())
                writeFile.write("\n")
                writeFile.writelines(self.netlistCircuitLines(netlistComponents))
                writeFile.writelines(self.netlistPortsLines(circuitSimName))
                writeFile.write("\n")
                writeFile.writelines(netlistSimulationLines(simType,simParams))
                writeFile.write("\n")        
                writeFile.write(".end")
                writeFile.close()
                self.loadNetlistFile(circuitSim["Ansys"],circuitSim["Netlist"])
                #Generate and run the ansysRunSimulator file
                lines=ansysSimulatorPreamb
                lines=lines+["oProject = oDesktop.SetActiveProject(\""+str(circuitSim["Ansys"]).split("/")[-1][0:-5]+"\")\n",\
                             "oDesign = oProject.SetActiveDesign(\""+"Netlist"+"\")\n",\
                             "oModuleReport = oDesign.GetModule(\"ReportSetup\")\n",\
                             "oDesign.AnalyzeAll()\n"]
                #S21 circuit simulations
                if circuitSimName=="fullS21":
                    lines=lines+["oModuleReport.CreateReport(\"S Parameter Table 1\", \"Standard\", \"Data Table\", \"LNA\",\n",\
                                 "    [\n",\
                                 "        \"NAME:Context\",\n",\
                                 "        \"SimValueContext:=\"	, [3,0,2,0,False,False,-1,1,0,1,1,\"\",0,0]\n",\
                                 "    ],\n",\
                                 "    [\n",\
                                 "        \"F:=\"			, [\"All\"]\n",\
                                 "    ],\n",\
                                 "    [\n",\
                                 "        \"X Component:=\"		, \"F\",\n",\
                                 "        \"Y Component:=\"		, [\"S(2,1)\"]\n",\
                                 "    ], [])\n",\
                                 "oModuleReport.ExportToFile(\"S Parameter Table 1\", \""+str(circuitSim["ResultsFile"])+"\", False)\n"]
                #Y11 circuit simulations
                elif circuitSimName[0:4] in ["Y11R","Y11Q"] or circuitSimName[0:5]=="Y11BC" or circuitSimName[0:6]=="YRestR" or circuitSimName[0:10]=="Y11LumpedR":
                    lines=lines+["oModuleReport.CreateReport(\"Y Parameter Table 1\", \"Standard\", \"Data Table\", \"LNA\",\n",\
                                 "    [\n",\
                                 "        \"NAME:Context\",\n",\
                                 "        \"SimValueContext:=\"	, [3,0,2,0,False,False,-1,1,0,1,1,\"\",0,0]\n",\
                                 "    ],\n",\
                                 "    [\n",\
                                 "        \"F:=\"			, [\"All\"]\n",\
                                 "    ],\n",\
                                 "    [\n",\
                                 "        \"X Component:=\"		, \"F\",\n",\
                                 "        \"Y Component:=\"		, [\"Y(1,1)\"]\n",\
                                 "    ], [])\n",\
                                 "oModuleReport.ExportToFile(\"Y Parameter Table 1\", \""+str(circuitSim["ResultsFile"])+"\", False)\n"]
                elif circuitSimName[0:4]=="Z21Q":
                    lines=lines+["oModuleReport.CreateReport(\"Z Parameter Table 1\", \"Standard\", \"Data Table\", \"LNA\",\n",\
                                 "    [\n",\
                                 "        \"NAME:Context\",\n",\
                                 "        \"SimValueContext:=\"	, [3,0,2,0,False,False,-1,1,0,1,1,\"\",0,0]\n",\
                                 "    ],\n",\
                                 "    [\n",\
                                 "        \"F:=\"			, [\"All\"]\n",\
                                 "    ],\n",\
                                 "    [\n",\
                                 "        \"X Component:=\"		, \"F\",\n",\
                                 "        \"Y Component:=\"		, [\"Z(2,1)\"]\n",\
                                 "    ], [])\n",\
                                 "oModuleReport.ExportToFile(\"Z Parameter Table 1\", \""+str(circuitSim["ResultsFile"])+"\", False)\n"]
                lines.append(ansysSaveLine())   
                simulatorFileInstance=open(circuitSim["ansysRunSimulator"],"w+",newline='')
                simulatorFileInstance.writelines(lines)
                simulatorFileInstance.close()
                self.runAnsysSimulator(circuitSim["Ansys"],circuitSim["ansysRunSimulator"],self.simFiles[simType]["Directory"],3)#Circuit simulations are quite fast
        elif simStage=="postProcess":    
            #All calculations after the simulations
            #Only proceed once all simulations have completed. 
            if self.sysParams["Compute Location"]=="Cluster":
                proceed=False
                while proceed==False:
                    proceed=True
                    for q3dSimName,q3dSim in self.simFiles[simType]["Q3D Simulations"].items():
                        if not os.path.exists(q3dSim["ResultsFile"]):
                            proceed=False
                    for hfssSimName,hfssSim in self.simFiles[simType]["HFSS Simulations"].items():
                        if not os.path.exists(hfssSim["ResultsFile"]):
                            proceed=False
                    for circuitSimName,circuitSim in self.simFiles[simType]["Circuit Simulations"].items():
                        if not os.path.exists(circuitSim["ResultsFile"]):
                            proceed=False
            time.sleep(1)
            #Delete all Ansys results folders (~90MB for capmat)
            for q3dSimName,q3dSim in self.simFiles[simType]["Q3D Simulations"].items():
                self.deleteFolder(str(q3dSim["ResultsFolder"]))
            for circuitSimName,circuitSim in self.simFiles[simType]["Circuit Simulations"].items():
                resultsFolder=str(circuitSim["ResultsFolder"])
                if os.path.exists(resultsFolder):
                    self.deleteFolder(str(circuitSim["ResultsFolder"]))  
            
            if simType=="fullS21":
                freq,S21,S21interpFunc=readS21Data(self.simFiles[simType]["Circuit Simulations"]["fullS21"]["ResultsFile"])
                plt.plot([i*omegaToGHz for i in freq],[S21TodB(i) for i in S21])
                plt.xlabel('Freq (GHz)')
                plt.ylabel('S21(dB)')
                plt.savefig(self.simFiles[simType]["Directory"]+"/S21dB.png")                
            elif simType[0:3]=="ECQ":#Requires running capMatGE first. 
                qubitIndex=int(simType[3:])
                qubitObj=self.allQubitsDict[qubitIndex]
                qubitColumnIndex=self.postGEComponentList.index(qubitObj)
                cInv=np.linalg.inv(self.capMatGE)
                cSum=1/cInv[qubitColumnIndex,qubitColumnIndex]
                
                E_C=eConst**2/(2*cSum)#In Joules
                EJ=self.allQubitsDict[qubitIndex].EJ
                print(qubitObj.name+"EC (GHz): "+str(E_C*Joules_To_GHz))
                print(qubitObj.name+"EJ (GHz): "+str(EJ*Joules_To_GHz))
                print(qubitObj.name+"EJ/EC: "+str(EJ/E_C))
                resultsLines=[["EC",str(E_C)],\
                              ["EJ/EC",str(EJ/E_C)]]
                csvWrite(self.simFiles[simType]["ResultsFile"],resultsLines)
            
            elif simType[0:3]=="zzQ":#Depends on results of quantizeSimulation
                qubitIndices=zzQIndices(simType)
                quantizeIndices=[self.allQubitsDict[i].quantizeIndex for i in qubitIndices]
                
                stateList01=self.stateList([[quantizeIndices[1],1]])
                stateList10=self.stateList([[quantizeIndices[0],1]])
                stateList11=self.stateList([[quantizeIndices[0],1],[quantizeIndices[1],1]])
                
                E11=self.HEval(stateList11)
                E10=self.HEval(stateList10)
                E01=self.HEval(stateList01)
                
                print("E11 (GHz):",E11)
                print("E10 (GHz):",E10)
                print("E01 (GHz):",E01)
                
                gz=E11-E01-E10
                
                print("gz"+str(qubitIndices[0])+"-"+str(qubitIndices[1])+"(MHz): ",gz*1000)
                
                resultsLines=[["g_z (MHz):",str(gz*1000)]]
                csvWrite(self.simFiles[simType]["ResultsFile"],resultsLines)
            elif simType[0:14]=="anharmonicityQ":
                qubitIndex=int(simType[14:])
                quantizeIndex=self.allQubitsDict[qubitIndex].quantizeIndex
                
                stateList1=self.stateList([[quantizeIndex,1]])
                stateList2=self.stateList([[quantizeIndex,2]])
                
                E1=self.HEval(stateList1)
                E2=self.HEval(stateList2)
                
                anharmonicity=(E2-2*E1)*1000#In MHz
                print("anharmonicityQ"+str(qubitIndex)+" (MHz):",anharmonicity)
                resultsLines=[["anharmonicity (MHz):",str(anharmonicity)]]
                csvWrite(self.simFiles[simType]["ResultsFile"],resultsLines)
            elif simType[0:10]=="quantFreqQ":
                qubitIndex=int(simType[10:])
                quantizeIndex=self.allQubitsDict[qubitIndex].quantizeIndex
                
                stateList1=self.stateList([[quantizeIndex,1]])
                
                E1=self.HEval(stateList1)
                print("quantFreqQ"+str(qubitIndex)+" (GHz):",E1)
                resultsLines=[["Frequency (GHz):",str(E1)]]
                csvWrite(self.simFiles[simType]["ResultsFile"],resultsLines)
            
            elif simType[0:10]=="quantFreqR":
                readoutResonatorIndex=int(simType[10:])
                quantizeIndex=self.allReadoutResonatorsDict[readoutResonatorIndex].quantizeIndex
                
                stateList1=self.stateList([[quantizeIndex,1]])
                
                E1=self.HEval(stateList1)
                print("quantFreqR"+str(readoutResonatorIndex)+" (GHz):",E1)
                resultsLines=[["Frequency (GHz):",str(E1)]]
                csvWrite(self.simFiles[simType]["ResultsFile"],resultsLines)
            
            elif simType[0:4]=="L_iQ":
                qubitIndex=int(simType[4:])
                calculatedL_i=self.allQubitsDict[qubitIndex].L_i_calculated
                resultsLines=[["L_i(calculated):",calculatedL_i]]
                csvWrite(self.simFiles[simType]["ResultsFile"],resultsLines)
                print("L_iQ"+str(qubitIndex)+":",calculatedL_i)
            elif simType[0:9]=="circFreqQ":
                qubitIndex=int(simType[9:])
                freqGHz=self.calculateQubitFrequency(index=qubitIndex)*omegaToGHz
                resultsLines=[["Frequency (GHz):",freqGHz]]
                csvWrite(self.simFiles[simType]["ResultsFile"],resultsLines)
            elif simType[0:6]=="decayQ":
                qubitIndex=int(simType[6:])
                qubit=self.allQubitsDict[qubitIndex]
                qubitFreq=qubit.freq*GHzToOmega
                freq,Y11,Y11InterpFunc=readY11Data(self.simFiles[simType]["Circuit Simulations"]["Y11Q"+str(qubitIndex)]["ResultsFile"])
                derivativeResolution=np.abs(freq[1]-freq[0])
                resultsLines=[]
                deriv=derivative(Y11InterpFunc,qubitFreq,derivativeResolution)
                T1denom=(2*np.real(Y11InterpFunc(qubitFreq)))
                T1=np.imag(derivative(Y11InterpFunc,qubitFreq,derivativeResolution))/(2*np.real(Y11InterpFunc(qubitFreq)))
                resultsLines.append(["T1 (s):",T1])
                csvWrite(self.simFiles[simType]["ResultsFile"],resultsLines)
            elif simType[0:9]=="circFreqR":
                readoutResonatorIndex=int(simType[9:])
                freqGHz=self.calculateResonatorFrequency(index=readoutResonatorIndex)*omegaToGHz
                resultsLines=[["Frequency (GHz):",freqGHz]]
                csvWrite(self.simFiles[simType]["ResultsFile"],resultsLines)
            elif simType[0:17]=="feedlineCouplingR":
                readoutResonatorIndex=int(simType[17:])
                readoutResonator=self.allReadoutResonatorsDict[readoutResonatorIndex]
                resonatorFreq=readoutResonator.freq*GHzToOmega
                freq,Y11,Y11InterpFunc=readY11Data(self.simFiles[simType]["Circuit Simulations"]["Y11R"+str(readoutResonatorIndex)]["ResultsFile"])
                #derivativeResolution=np.abs(freq[1]-freq[0])*1e-6
                derivativeResolution=1
                resultsLines=[]
                tau=np.imag(derivative(Y11InterpFunc,resonatorFreq,derivativeResolution))/(2*np.real(Y11InterpFunc(resonatorFreq)))
                resultsLines.append(["Tau (s):",tau])
                Qc=resonatorFreq*tau
                print("Qc:"+str(Qc))
                resultsLines.append(["Qc:",Qc])
                csvWrite(self.simFiles[simType]["ResultsFile"],resultsLines)                
            elif simType[0:7]=="lumpedR":        
                readoutResonatorIndex=int(simType[7:])
                equivL,equivC=self.calculateLumpedResonator(index=readoutResonatorIndex)
                resultsLines=[["equivL(H):",equivL],["equivC(F):",equivC]]
                csvWrite(self.simFiles[simType]["ResultsFile"],resultsLines) 
                print("equivL(H):"+str(equivC))
                print("equivC(C):"+str(equivL))
            elif simType[0:11]=="freqLumpedR":                
                readoutResonatorIndex=int(simType[11:])
                print("Resonator "+str(readoutResonatorIndex)+" dressed frequency:"+str(self.calculateResonatorFrequency(index=readoutResonatorIndex)*omegaToGHz)+" GHz")
                print("Lumped resonator "+str(readoutResonatorIndex)+" dressed frequency:"+str(self.calculateLumpedFrequency(index=readoutResonatorIndex)*omegaToGHz)+" GHz")
            elif simType[0:3]=="ECR":#Requires running capMatGE first. 
                readoutResonatorIndex=int(simType[3:])
                readoutResonatorObj=self.allReadoutResonatorsDict[readoutResonatorIndex]
                resonatorColumnIndex=self.postGEComponentList.index(readoutResonatorObj)
                cInv=np.linalg.inv(self.capMatGE)
                cSum=1/cInv[resonatorColumnIndex,resonatorColumnIndex]
                
                E_C=eConst**2/(2*cSum)#In Joules
                resultsLines=[["EC",str(E_C)]]
                csvWrite(self.simFiles[simType]["ResultsFile"],resultsLines)
            elif simType[0:16]=="dispersiveShiftR":
                readoutResonatorIndex=int(simType[16:])
                resonatorQuantizeIndex=self.allReadoutResonatorsDict[readoutResonatorIndex].quantizeIndex
                
                qubitIndex=readoutResonatorIndex#Dependent on qubit/resonator pair convention!!!!
                qubitQuantizeIndex=self.allQubitsDict[qubitIndex].quantizeIndex
                
                stateList01=self.stateList([[qubitQuantizeIndex,0],[resonatorQuantizeIndex,1]])
                stateList10=self.stateList([[qubitQuantizeIndex,1],[resonatorQuantizeIndex,0]])
                stateList11=self.stateList([[qubitQuantizeIndex,1],[resonatorQuantizeIndex,1]])
                
                E00=0
                E01=self.HEval(stateList01)
                E10=self.HEval(stateList10)
                E11=self.HEval(stateList11)
                
                print(E11,E10,E01)
                
                dispersiveShift=((E11-E10)-(E01-E00))*1000#Difference in transition frequency depending on the state of the qubit. In MHz.
                print("dispersiveShiftR"+str(readoutResonatorIndex)+" (MHz):",dispersiveShift)
                
                resultsLines=[["Dispersive Shift (MHz):",str(dispersiveShift)]]
                csvWrite(self.simFiles[simType]["ResultsFile"],resultsLines)
                
            elif simType=="quantize":
                self.quantizeSimulation(simParams)
            elif simType=="capMat":
                capMatResultsFileLines=csvRead(self.simFiles["capMat"]["Q3D Simulations"]["q3dExtractor"]["ResultsFile"])
                capMatHeaderLineIndex=0
                for index,line in enumerate(capMatResultsFileLines):
                    if line!=[] and line[0]=="Capacitance Matrix":
                        capMatHeaderLineIndex=index+1
                unitsMultiplier=self.capMatUnitsToF
                self.ansysCapMatHeaders=arrayNoBlanks(capMatResultsFileLines[capMatHeaderLineIndex])
                numNodes=len(self.ansysCapMatHeaders)
                capMat=np.zeros((numNodes,numNodes))
                capMatStartLineIndex=capMatHeaderLineIndex+1
                for index1,header1 in enumerate(self.ansysCapMatHeaders):
                    for index2,header2 in enumerate(self.ansysCapMatHeaders):
                        matRow=capMatStartLineIndex+index1
                        matCol=1+index2
                        capacitanceValue=float(capMatResultsFileLines[matRow][matCol])*unitsMultiplier
                        capMat[index1,index2]=capacitanceValue 
                
                lines=[]
                lines.append(["Capacitance (F)"])
                lines.append([""]+self.ansysCapMatHeaders)
                for rowIndex in range(numNodes):
                    lines.append([self.ansysCapMatHeaders[rowIndex]]+list(capMat[rowIndex,:]))
                lines.append([""])
                lines.append(["Capacitance To Ground (F)"])
                for rowIndex in range(numNodes):
                    lines.append([self.ansysCapMatHeaders[rowIndex]]+[str(sum(capMat[rowIndex,:]))])
                
                csvWrite(self.simFiles[simType]["ResultsFile"],lines)
            elif simType=="capMatGE":#includes the lumped resonator capacitances. 
                lines=[]
                capMat_preGE=self.capMatForGE()
                capMat_GE,phiMat,RHS=self.gaussianElimination(capMat_preGE)
                
                numNodes=len(self.postGEComponentList)
                lines.append(["Capacitance (F)"])
                lines.append([""]+[component.name for component in self.postGEComponentList])
                for rowIndex in range(numNodes):
                    lines.append([self.postGEComponentList[rowIndex].name]+list(capMat_GE[rowIndex,:]))
                csvWrite(self.simFiles[simType]["ResultsFile"],lines)
    def simulationCommand(self,command):
        self.loadAllData()
        #Resolve the simulation command
        if command[0]=="simulation":    
            self.simulation(command)   
        #Helper commands
        elif command=="initAllCircuitSims":
            self.initAllCircuitSims()
        elif command=="runAllCircuitSims":
            self.runAllCircuitSims()
        elif command=="postProcessAllCircuitSims":
            self.postProcessAllCircuitSims()
        elif command=="GEPlusAllEC":
            self.GEPlusAllEC()
        elif command=="AllL_i":
            self.AllL_i()
        elif command=="Allzz":
            self.Allzz()  
        elif command=="AllAnharmonicityQ":
            self.AllAnharmonicityQ()
        elif command=="AllQuantFreq":
            self.AllQuantFreq()
        elif command=="AllDispersiveShiftR":
            self.AllDispersiveShiftR()
    def printCommand(self,command):
        self.loadAllData()
        if command=="frequencies":
            print("FREQUENCIES")
            for qubitIndex,qubit in self.allQubitsDict.items():
                print(qubit.name+":"+str(qubit.freq))
            for readoutResonatorIndex,readoutResonator in self.allReadoutResonatorsDict.items():
                print(readoutResonator.name+":"+str(readoutResonator.freq))
        elif command=="anharmonicities":
            print("ANHARMONICITIES")
            for qubitIndex,qubit in self.allQubitsDict.items():
                print(qubit.name+":"+str(qubit.anharmonicity))
    def calculateQubitFrequency(self,index):#Calculates from circFreqR files
        freq,Y11,Y11interpFunc=readY11Data(self.simFiles["circFreqQ"+str(index)]["Circuit Simulations"]["Y11Q"+str(index)]["ResultsFile"])
        return calculateDressedFrequency(freq,Y11interpFunc)
    def calculateResonatorFrequency(self,index):#Calculates from circFreqQ files
        freq,Y11,Y11interpFunc=readY11Data(self.simFiles["circFreqR"+str(index)]["Circuit Simulations"]["Y11R"+str(index)]["ResultsFile"])
        return calculateDressedFrequency(freq,Y11interpFunc)
    def calculateLumpedResonator(self,index):#Calculates from lumpedR files
        #Load Y11,YRest data
        Y11Freq,Y11_Y11,Y11InterpFunc=readY11Data(self.simFiles["lumpedR"+str(index)]["Circuit Simulations"]["Y11R"+str(index)]["ResultsFile"])
        YRestFreq,YRest_Y11,YRestInterpFunc=readY11Data(self.simFiles["lumpedR"+str(index)]["Circuit Simulations"]["YRestR"+str(index)]["ResultsFile"])
        derivativeResolution=np.abs(Y11Freq[1]-Y11Freq[0])
        dressedFreq=calculateDressedFrequency(Y11Freq,Y11InterpFunc)
        #print("Dressed Frequency: "+str(dressedFreq/(2*np.pi*1e9))+" GHz")
        #See Junling's thesis equations 4.19
        equivC=1/2*(np.imag(derivative(Y11InterpFunc,dressedFreq,derivativeResolution))-\
                    np.imag(derivative(YRestInterpFunc,dressedFreq,derivativeResolution))-
                    np.imag(YRestInterpFunc(dressedFreq))/dressedFreq)
        equivL=2/(dressedFreq**2*(np.imag(derivative(Y11InterpFunc,dressedFreq,derivativeResolution))-\
                                  np.imag(derivative(YRestInterpFunc,dressedFreq,derivativeResolution)))+\
                  dressedFreq*np.imag(YRestInterpFunc(dressedFreq))) 
        #print("equivW:"+str(1/(2*np.pi*1e9*np.sqrt(equivL*equivC)))+" GHz")
        return equivL,equivC
    def calculateLumpedFrequency(self,index):
        freq,Y11,Y11interpFunc=readY11Data(self.simFiles["freqLumpedR"+str(index)]["Circuit Simulations"]["Y11LumpedR"+str(index)]["ResultsFile"])
        return calculateDressedFrequency(freq,Y11interpFunc)     
    def quantizeSimulation(self,simParams):
        print("started quantize")
        quantizeStartTime=time.time()
        
        numQubitPhotons=simParams["NumQubitPhotons"]
        numResonatorPhotons=simParams["NumResonatorPhotons"]
        numPhotons=max(numQubitPhotons,numResonatorPhotons)
        
        #self.capMatGE needs to be reduced based on the requested components to quantize.
        quantizeComponentListNames=readQuantizeList(simParams["QuantizeList"])
        quantizeComponentList=[self.componentFromName(i) for i in quantizeComponentListNames]#Determines the index ordering in capMatGE_quant!
        for index,component in enumerate(quantizeComponentList):
            component.quantizeIndex=index
        
        numComponents=len(quantizeComponentList)
        capMatGEIndicesToKeep=[self.postGEComponentList.index(i) for i in quantizeComponentList]
        
        rows = np.array(capMatGEIndicesToKeep, dtype=np.intp)
        columns = np.array(capMatGEIndicesToKeep, dtype=np.intp)
        capMatGE_quant=self.capMatGE[rows[:, np.newaxis], columns]
        
        dim=numPhotons+2
        fullDim=dim**numComponents
        qObjDim=[dim for i in range(numComponents)]
        Cinv=np.linalg.inv(capMatGE_quant)
        
        #Assemble the Hamiltonian. H is in units of radians (H/hbar). Calculates 1/2*Q.T*Cinv*Q.
        print("Start assembling H")
        startTime=time.time()
        dimCinv=Cinv.shape[0]
        resolveRHS=[0 for i in range(dimCinv)]
        resolveLHSSum=qzero(qObjDim)
        for Cinv_rowIndex,Cinv_row in enumerate(Cinv):
            resolveRHSSum=qzero(qObjDim)
            for componentIndex,component in enumerate(quantizeComponentList):
                resolveRHSSum+=Cinv_row[componentIndex]*component.QsecondQuant(dim,numComponents)
            LHSComponent=quantizeComponentList[Cinv_rowIndex]
            resolveLHSSum+=1/2*LHSComponent.QsecondQuant(dim,numComponents)*resolveRHSSum
        H=resolveLHSSum
        endTime=time.time()
        print("Finished assembling H",(endTime-startTime)/60)
        print("Initial matrix dimension:",H.shape[0])
        
        print("Start adding inductance")
        startTime=time.time()
        #Add inductance terms
        for component in quantizeComponentList:
            print(component.name)
            #tot_m, used_m, free_m = map(int, os.popen('free -t -m').readlines()[-1].split()[1:])
            #print("Available memory (GB):",free_m/1e3)
            if issubclass(type(component),Qubit) or isinstance(component,StraightBusCoupler):
                x=((2*np.pi*np.sqrt(hbarConst)/Phi_0Const)*component.PhisecondQuant(dim,numComponents))
                for i in range(int(simParams["TrigOrder"]/2)+1):
                    cosTerm=(-1)**(i)*x**(2*i)/np.math.factorial(2*i)
                    H-=(component.EJ/hbarConst)*cosTerm
                    print("cos x^"+str(2*i)+" term Frobenius norm: ",cosTerm.norm(norm="fro"))
            elif isinstance(component,ReadoutResonator):
                term=component.PhisecondQuant(dim,numComponents)**2/(2*component.equivL)
                H+=term
        endTime=time.time()
        print("Finished adding inductance",(endTime-startTime)/60)
        
        #Truncate H based on numPhotons
        print("Truncating H")
        startTime=time.time()
        numAllStates=H.shape[0]
        #Compile a list of all the states in H
        allStatesList=[0]*numAllStates
        base=dim
        for i in range(numAllStates):
            stateList=baseRepresentation(i,base,numComponents)
            H_index=state_number_index(H.dims[0],stateList)
            allStatesList[H_index]=stateList#The order of allStatesList now corresponds to the order of rows/columns in H. 
        #Compile a list of all the states to keep based on the numPhotons parameters.
        keepStatesList=[]
        qubitIndices=[i for i in range(numComponents) if issubclass(type(quantizeComponentList[i]),Qubit)]
        readoutResonatorIndices=[i for i in range(numComponents) if isinstance(quantizeComponentList[i],ReadoutResonator)]
        for stateList in allStatesList:
            qubitExcitations=[stateList[i] for i in range(numComponents) if i in qubitIndices]
            readoutResonatorExcitations=[stateList[i] for i in range(numComponents) if i in readoutResonatorIndices]
            if all(i<=numQubitPhotons for i in qubitExcitations) and all(i<=numResonatorPhotons for i in readoutResonatorExcitations):
                keepStatesList.append(stateList)
        #Reduce H to only the states in keepStatesList
        indicesToKeep=[state_number_index(H.dims[0],stateList) for stateList in keepStatesList]
        indicesToKeep.sort()#This is crucial. Because the indices are sorted, state_number_index will still work after extract_states is called. 
        H=H.extract_states(indicesToKeep)
        #Update the dimension of H to reflect the truncation. 
        newHDim=[]
        for component in quantizeComponentList:
            if issubclass(type(component),Qubit):
                newHDim.append(numQubitPhotons+1)
            elif isinstance(component,ReadoutResonator):
                newHDim.append(numResonatorPhotons+1)
        H.dims=[newHDim,newHDim]
        stateListHIndices={str(stateList):state_number_index(H.dims[0],stateList) for stateList in keepStatesList}
        H=H*omegaToGHz
        endTime=time.time()
        print("Finished truncating H",(endTime-startTime)/60)

        #Extract the bare hamiltonian for each component. 
        print("Extracting subspaces")
        startTime=time.time()
        subspaceEigenstates=[]#Each element is a list of the eigenstates in fock ordering for a particular component. 
        for component in quantizeComponentList:
            fockStates=[[n if i==component.quantizeIndex else 0 for i in range(numComponents)] for n in range(newHDim[component.quantizeIndex])]
            subspaceStateIndices=[stateListHIndices[str(i)] for i in fockStates]
            componentH=H.extract_states(subspaceStateIndices)
            subspaceEigenstates.append(componentH.eigenstates()[1])
        endTime=time.time()
        print("Finished calculating subspaces",(endTime-startTime)/60)
        
        #Assemble output states in order of manifold.
        outputStatesList=[]
        for photonManifold in [0,1,2]:
            base=photonManifold+1
            allNumsBase=[baseRepresentation(i,base,numComponents) for i in range(1,base**(numComponents-1)*photonManifold+1)]
            manifoldNums=[i for i in allNumsBase if sum(i)==photonManifold]#Remove the numbers that aren't in the manifold
            manifoldNums.reverse()
            outputStatesList=outputStatesList+manifoldNums
        zeroStateList=[0 for i in range(numComponents)]
        outputStatesList=[zeroStateList]+outputStatesList
        H_output_dim=len(outputStatesList)
        H_output=np.zeros([H_output_dim,H_output_dim],dtype = 'complex_')
        H_output_headers=[H_Header(i) for i in outputStatesList]
        dressedKeepStates=[tensor([subspaceEigenstates[componentIndex][state[componentIndex]] for componentIndex in range(numComponents)]) for state in keepStatesList]
        
        print("Starting matrix element")
        startTime=time.time()
        numOutputStates=len(outputStatesList)
        H_output=np.zeros((numOutputStates,numOutputStates),dtype=complex)
        for i in range(numOutputStates):
            for j in range(numOutputStates):
                H_output[i,j]=H.matrix_element(bra(outputStatesList[i],newHDim),ket(outputStatesList[j],newHDim))
        endTime=time.time()
        print("Finished matrix element",(endTime-startTime)/60)

        print("Final matrix dimension:",H.dims)

        #Eigenvalues
        print("Calculating eigenvalues") 
        startTime=time.time()
        eigsComplex=H.eigenenergies()
        eigsReal=[np.real(i) for i in eigsComplex]
        eigsReal.sort()
        eigsRealNorm=[i-eigsReal[0] for i in eigsReal]#Normalize to the ground state being zero energy. 
        endTime=time.time()
        print("Finished calculating eigenvalues",(endTime-startTime)/60)
        
        #Output
        print("Starting output")
        lines=[]
        lines.append(["Index Order"])
        lines.append([i.name for i in quantizeComponentList])
        lines.append([""])
        lines.append(["H (GHz)"])
        lines.append([""]+H_output_headers)
        for index,H_output_line in enumerate(H_output):
            matRow=[H_output_headers[index]]+[np.real(j) for j in list(H_output_line)]
            lines.append(matRow)
        lines.append([""])
        lines.append(["H_evals"])
        lines.append(eigsRealNorm)
        lines.append([""])
        csvWrite(self.simFiles["quantize"]["ResultsFile"],lines)
        quantizeEndTime=time.time()
        print("Total time:",(quantizeEndTime-quantizeStartTime)/60)
        
        for component in quantizeComponentList:
            if isinstance(component,ReadoutResonator):
                print(component.equivL)
    def generateGDS(self):
        Main = gdspy.Cell('Main')
        for chipIndex,chip in self.chipDict.items():
            #Lists of GDS items to either add or subtract
            peripheries=[]#List of polygons to subtract from GND
            components=[]#List of polygons to add to GND
            meshPeripheries=[]
            addToMain=[]
            subtractFromGround=[]
            unitChange=1#Convert if necessary.
            chipWidth=chip.substrate.geometryParamsDict["Width"]*unitChange
            chipLength=chip.substrate.geometryParamsDict["Length"]*unitChange
            
            #Add all components
            for node in self.getChipNNodes(chip.index):#Add all nodes
                components.append(node.polyline)
                peripheries=peripheries+node.peripheryPolylines
                meshPeripheries=meshPeripheries+node.meshPeripheryPolylines
            for component in components:
                addToMain.append(gdspy.Polygon(multiplyPolyline(component,unitChange),layer=chip.index))
            for periphery in peripheries:
                subtractFromGround.append(gdspy.Polygon(multiplyPolyline(periphery,unitChange),layer=chip.index))
            #Dice Gap
            diceGap = OtherComponents.create_dice_gap(chip_size_x=chip.substrate.geometryParamsDict["Width"]*unitChange, chip_size_y=chip.substrate.geometryParamsDict["Length"]*unitChange)
            subtractFromGround.append(diceGap)
            #Chip Markers
            if self.sysParams["Chip Markers"]=="Pappas":
                chipMarkers = OtherComponents.createPappasMarkers(chip_size_x=chip.substrate.geometryParamsDict["Width"]*unitChange, chip_size_y=chip.substrate.geometryParamsDict["Length"]*unitChange)
                subtractFromGround.append(chipMarkers)
            elif self.sysParams["Chip Markers"]=="Schmidt":
                periphery1,marker1,periphery2,marker2=OtherComponents.import_schmidtMarker()#1 and 2 denote layers.
                if chip.index==0:
                    marker=marker1
                    periphery=periphery1
                elif chip.index==1:
                    marker=marker2
                    periphery=periphery2
                shiftX=self.chipDict[0].substrate.geometryParamsDict["Width"]/2*unitChange
                shiftY=self.chipDict[0].substrate.geometryParamsDict["Length"]/2*unitChange
                if self.sysParams["Flip Chip?"]=="Yes":
                    shiftX=self.chipDict[1].substrate.geometryParamsDict["Width"]/2*unitChange
                    shiftY=self.chipDict[1].substrate.geometryParamsDict["Length"]/2*unitChange
                
                markerCorners=[gdspy.copy(marker) for i in range(4)]
                markerCornerPeripheries=[gdspy.copy(periphery) for i in range(4)]
                
                buffer=250*unitChange
                
                markerCorners[0].translate(-shiftX+buffer,shiftY-buffer)
                markerCorners[1].translate(shiftX-buffer,shiftY-buffer)
                markerCorners[2].translate(shiftX-buffer,-shiftY+buffer)
                markerCorners[3].translate(-shiftX+buffer,-shiftY+buffer)
                
                markerCornerPeripheries[0].translate(-shiftX+buffer,shiftY-buffer)
                markerCornerPeripheries[1].translate(shiftX-buffer,shiftY-buffer)
                markerCornerPeripheries[2].translate(shiftX-buffer,-shiftY+buffer)
                markerCornerPeripheries[3].translate(-shiftX+buffer,-shiftY+buffer)
                
                for markerIndex,markerCorner in enumerate(markerCorners):
                    markerCorner.layers=[chip.index for i in range(len(markerCorner.layers))]
                    marker_cell=gdspy.Cell("Marker"+str(markerIndex)+"Chip"+str(chip.index))
                    subtractFromGround.append(markerCornerPeripheries[markerIndex])
                    marker_cell.add(markerCorners[markerIndex])
                    addToMain.append(gdspy.CellReference(marker_cell))
            #Nist Logo
            if chip.index==0:
                nist_logo_periphery,nist_logo=OtherComponents.import_nist_logo()
                for obj in [nist_logo,nist_logo_periphery]:
                    obj.translate(self.chipDict[chip.index].nistLogoCenter[0]*unitChange,self.chipDict[chip.index].nistLogoCenter[1]*unitChange)
                nist_logo.layers=[chip.index for i in range(77)]
                NIST_logo_cell=gdspy.Cell('NIST logo')
                subtractFromGround.append(nist_logo_periphery)
                NIST_logo_cell.add(nist_logo)
                addToMain.append(gdspy.CellReference(NIST_logo_cell))
            #Description. May have mesh holes in it. 
            descriptionText = gdspy.Text(self.sysParams["Chip Description"],100*unitChange,self.chipDict[0].chipDescriptionStart)
            subtractFromGround.append(descriptionText)
            
            #Draw mesh
            if self.sysParams["Add Mesh to GDS?"]=="Yes":
                #meshContainer=gdspy.Cell((-chipWidth/2,-chipLength/2),(chipWidth/2,chipLength/2),layer=chip.index+2)
                size=self.sysParams["Anti-Vortex Mesh Size"]*unitChange
                chipBorder=150
                for xVal in np.arange(-chipWidth/2+chipBorder,chipWidth/2-chipBorder,self.sysParams["Anti-Vortex Mesh Spacing"]*unitChange):
                    for yVal in np.arange(-chipLength/2+chipBorder,chipLength/2-chipBorder,self.sysParams["Anti-Vortex Mesh Spacing"]*unitChange):
                        exclude="No"
                        for meshPeriphery in meshPeripheries:
                            if pointInPolyline([xVal,yVal],meshPeriphery)==True:
                                exclude="Yes"
                        if exclude=="No":  
                            Main.add(gdspy.Rectangle((xVal-size/2,yVal-size/2),(xVal+size/2,yVal+size/2),layer=chip.index+2))
            #Create ground plane
            if self.sysParams["Invert GDS?"]=="No":
                GND=gdspy.Rectangle((-chipWidth/2,-chipLength/2),(chipWidth/2,chipLength/2),layer=chip.index)
                for item in subtractFromGround:
                    GND=gdspy.fast_boolean(GND,item,'not',layer=chip.index)
                for item in addToMain:
                    Main.add(item)
            else:
                GND=gdspy.Cell("invertedGround"+str(chip.index))
                for item in subtractFromGround:
                    GND.add(item)
                for item in addToMain:
                    GND=gdspy.fast_boolean(GND,item,'not',layer=chip.index)
                Main.add(GND)
            JJGDSList=[]
            for qubitIndex,qubit in self.chipDict[chip.index].qubitDict.items():#Add the JJ components
                JJGDSList=JJGDSList+qubit.JJGDSs
            for PTCIndex,PTC in self.chipDict[chip.index].PTCDict.items():
                JJGDSList=JJGDSList+PTC.JJGDSs
            for straightBusCouplerIndex,straightBusCoupler in self.chipDict[chip.index].straightBusCouplerDict.items():
                JJGDSList=JJGDSList+straightBusCoupler.JJGDSs
            for thisJJGDS in JJGDSList:        
                Main.add(thisJJGDS.patchGDS)
                patchCopy=gdspy.copy(thisJJGDS.patchGDS)#This is placed so that the etching process doesn't destroy the patch. 
                patchCopy.layers=[chip.index]
                Main.add(patchCopy)
                Main.add(thisJJGDS.topElectrodeGDS)
                Main.add(thisJJGDS.bottomElectrodeGDS)
                Main.add(thisJJGDS.connectionsGDS)
                
            Main.add(GND)
        #Add bumps if flip chip
        if self.sysParams["Flip Chip?"]=="Yes":
            for bump in self.bumpsDict["Bumps"]:
                Main.add(gdspy.Polygon(multiplyPolyline(bump.underBumpBottomNode.polyline,unitChange),layer=3))#Bottom chip underbump
                Main.add(gdspy.Polygon(multiplyPolyline(bump.bumpMetalBottomNode.polyline,unitChange),layer=4))#Bottom chip bump metal
                Main.add(gdspy.Polygon(multiplyPolyline(bump.bumpMetalTopNode.polyline,unitChange),layer=5))#Top chip bump metal
                Main.add(gdspy.Polygon(multiplyPolyline(bump.underBumpTopNode.polyline,unitChange),layer=6))#Top chip underbump
            
        gdspy.write_gds(self.gdspyFile, unit=1.0e-6, precision=1.0e-11)    
    def addToSimFiles(self,simType,q3dSims,hfssSims,circuitSims):
        simDirectory=self.sysParams["Project Folder"]/simType
        self.simFiles[simType]={"Directory":simDirectory,\
                                "Params":simDirectory/"SimulationParameters.csv",\
                                "ResultsFile":simDirectory/"Results.csv",\
                                "Q3D Simulations":dict(),\
                                "HFSS Simulations":dict(),\
                                "Circuit Simulations":dict()}#Establish the simFile dictionary as having "Params" and "ResultsFile". 
        for q3dSim in q3dSims:#Add each circuit simulation to the simulation dictionary.
            self.simFiles[simType]["Q3D Simulations"][q3dSim]={"Ansys":simDirectory/(q3dSim+".aedt"),\
                                                               "Simulator":simDirectory/(q3dSim+"_"+"Simulator.py"),\
                                                               "Log":simDirectory/(q3dSim+"_"+"Simulator.log"),\
                                                               "ResultsFile":simDirectory/(q3dSim+"_"+"Results.csv"),\
                                                               "ResultsFolder":simDirectory/("q3dExtractor.aedtresults")}
        for hfssSim in hfssSims:#Add each circuit simulation to the simulation dictionary.
            self.simFiles[simType]["HFSS Simulations"][hfssSim]={"Ansys":self.simFiles[simType]["Directory"]/(hfssSim+".aedt"),\
                                                                 "Simulator":self.simFiles[simType]["Directory"]/(hfssSim+"_"+"Simulator.py"),\
                                                                 "Log":self.simFiles[simType]["Directory"]/(hfssSim+"_"+"Simulator.log"),\
                                                                 "ResultsFile":self.simFiles[simType]["Directory"]/(hfssSim+"_"+"Results.csv")}
        for circuitSim in circuitSims:#Add each circuit simulation to the simulation dictionary.
            self.simFiles[simType]["Circuit Simulations"][circuitSim]={"Ansys":self.simFiles[simType]["Directory"]/(circuitSim+".aedt"),\
                                                                       "Netlist":self.simFiles[simType]["Directory"]/(circuitSim+"_"+"Netlist.txt"),\
                                                                       "ansysInitSimulator":self.simFiles[simType]["Directory"]/(circuitSim+"_"+"ansysInitSimulator.py"),\
                                                                       "ansysRunSimulator":self.simFiles[simType]["Directory"]/(circuitSim+"_"+"ansysRunSimulator.py"),\
                                                                       "Log":self.simFiles[simType]["Directory"]/(circuitSim+"_"+"Simulator.log"),\
                                                                       "ResultsFile":self.simFiles[simType]["Directory"]/(circuitSim+"_"+"Results.csv"),\
                                                                       "ResultsFolder":simDirectory/(circuitSim+".aedtresults")}      
    def capMatLayout_Lines(self):       
        lines=["oEditor = oDesign.SetActiveEditor(\"3D Modeler\")\n",\
               "oModuleBoundary = oDesign.GetModule(\"BoundarySetup\")\n"]  
        for chipIndex,chip in self.chipDict.items():
            #Draw substrate
            lines=lines+self.ansysPolyline_Lines(name=chip.substrate.name,\
                                                 color=chip.substrate.node.color,\
                                                 material=chip.substrate.node.material,\
                                                 polyline3D=[[point[0],point[1],chip.substrate.node.Z] for point in chip.substrate.node.polyline])
            lines=lines+self.ansysSweepAlongVector_Lines(chip.substrate.node)
            #Draw ground(s)
            lines=lines+self.ansysPolyline_Lines(name=chip.ground.outlineNode.name,\
                                                 color=chip.ground.outlineNode.color,\
                                                 material=chip.ground.outlineNode.material,\
                                                 polyline3D=[[point[0],point[1],chip.ground.outlineNode.Z] for point in chip.ground.outlineNode.polyline])
            #Draw qubits,resonators,controlLines,launchpads
            
            for thisNode in self.getChipNNodes_CapMat(chip.index):
                lines=lines+self.ansysPolyline_Lines(name=thisNode.name,\
                                                     color=thisNode.color,\
                                                     material=thisNode.material,\
                                                     polyline3D=[[point[0],point[1],thisNode.Z] for point in thisNode.polyline])
                lines=lines+self.ansysQ3DMake3D(thisNode)
                #Trench round 1
                addTrenchNodeLines,subtractTrenchPeripheryLines,makeTrenchComponent3DLines=self.ansysTrench(componentNode=thisNode,trench=self.CPW.geometryParamsDict["Trench"],chip=chip)
                lines=lines+addTrenchNodeLines+subtractTrenchPeripheryLines#Trench
                
                lines=lines+ansysSignalLine_Lines(thisNode)
                #Subtract the periphery from the ground. Still subtract the launchpad peripheries so the control lines aren't shorted to ground. 
                for index,peripheryPolyline in enumerate(thisNode.peripheryPolylines):
                    peripheryName=thisNode.name+"periphery"+str(index)
                    lines=lines+self.ansysPolyline_Lines(name=peripheryName,\
                                                         color=thisNode.color,\
                                                         material=thisNode.material,\
                                                         polyline3D=[[point[0],point[1],thisNode.Z] for point in peripheryPolyline])#First make the boundary
                    lines=lines+self.ansysSubtract_Lines(chip.ground.outlineNode.name,peripheryName)#Then subtract it from ground.
            for thisNode in self.getChipNNodes_CapMat(chip.index):#Trench round 2. 
                addTrenchNodeLines,subtractTrenchPeripheryLines,makeTrenchComponent3DLines=self.ansysTrench(componentNode=thisNode,trench=self.CPW.geometryParamsDict["Trench"],chip=chip)
                lines=lines+makeTrenchComponent3DLines
            #For grounded qubits unite pad 2 with ground. 
            for qubitIndex,qubit in self.allQubitsDict.items():
                if isinstance(qubit,groundedQubit):
                    lines=lines+ansysUniteNodes([chip.ground.outlineNode,qubit.pad2.node])
            #For control lines unite trace and launchpads, also unite flux bias if applicable. 
            for controlLineIndex,controlLine in self.chipDict[chip.index].controlLineDict.items():
                if controlLine.generalParamsDict["Type"]=="feedline" and self.sysParams["Simulate Feedline?"]=="Yes":
                    uniteNodeList=[controlLine.lineNode]
                    for launchPadName,launchPadNode in controlLine.launchPadNodeDict.items():
                        uniteNodeList.append(launchPadNode)
                    lines=lines+ansysUniteNodes(uniteNodeList)
                    if controlLine.generalParamsDict["Type"]=="fluxBias":
                        lines=lines+ansysUniteNodes([self.chipDict[0].ground.outlineNode,controlLine.lineNode])
            #Make the ground 3D
            lines=lines+self.ansysQ3DMake3D(chip.ground.outlineNode)
        #Draw bumps if flip chip, and join the ground nodes via the bumps
        if self.sysParams["Flip Chip?"]=="Yes":
            uniteNodeList=[self.chipDict[0].ground.outlineNode,self.chipDict[1].ground.outlineNode]
            for thisBump in self.bumpsDict["Bumps"]:
                for thisNode in [thisBump.underBumpBottomNode,\
                                 thisBump.bumpMetalBottomNode,\
                                 thisBump.bumpMetalTopNode,\
                                 thisBump.underBumpTopNode]:
                    lines=lines+self.ansysPolyline_Lines(name=thisNode.name,\
                                                         color=thisNode.color,\
                                                         material=thisNode.material,\
                                                         polyline3D=[[point[0],point[1],thisNode.Z] for point in thisNode.polyline])
                    lines=lines+self.ansysSweepAlongVector_Lines(thisNode)
                    uniteNodeList.append(thisNode)
            lines=lines+ansysUniteNodes(uniteNodeList)#Resulting single node is ground1
        #Assign ground signal line (independent of flip chip)
        lines=lines+self.ansysGroundSignalLine_Lines()

        return lines
    def ansysTrench(self,componentNode,trench,chip):
        #trenchPeripheryNode is the outline that is subtracted from the substrate, after which trenchComponentNode is added to have a resulting net trench.
        #Define the trench nodes
        trenchComponentNode=Node(componentNode.name+"TrenchComponent")#This is the substrate "platform" that the component will eventually be resting on. 
        trenchPeripheryNodes=[]#These are the peripheries that will be subtracted from the substrate. 
        for index,peripheryPolyline in enumerate(componentNode.peripheryPolylines):
            thisNode=Node(componentNode.name+"TrenchPeriphery"+str(index))
            thisNode.polyline=peripheryPolyline
            thisNode.material="silicon"
            thisNode.color=chip.substrate.node.color
            trenchPeripheryNodes.append(thisNode)
        trenchComponentNode.polyline=componentNode.polyline
        trenchComponentNode.material="silicon"
        trenchComponentNode.color=chip.substrate.node.color
        addTrenchNodeLines=[]
        for trenchNode in [trenchComponentNode]+trenchPeripheryNodes:
            if chip.index==0:
                trenchNode.Z=chip.substrate.node.height-self.CPW.geometryParamsDict["Trench"]
                trenchNode.height=self.CPW.geometryParamsDict["Trench"]
            elif chip.index==1:
                trenchNode.Z=chip.substrate.node.Z
                trenchNode.height=self.CPW.geometryParamsDict["Trench"]    
            #Add the trench nodes to the ansys file. 
            addTrenchNodeLines=addTrenchNodeLines+self.ansysPolyline_Lines(name=trenchNode.name,\
                                                                           color=trenchNode.color,\
                                                                           material=trenchNode.material,\
                                                                           polyline3D=[[point[0],point[1],trenchNode.Z] for point in trenchNode.polyline])
        #Make the trenchPeriphery node 3D, then subtract it from the substrate.Finally, make the trenchComponent 3D
        subtractTrenchPeripheryLines=[]
        for trenchPeripheryNode in trenchPeripheryNodes:
            subtractTrenchPeripheryLines=subtractTrenchPeripheryLines+self.ansysSweepAlongVector_Lines(trenchPeripheryNode)+self.ansysSubtract_Lines(chip.substrate.name,trenchPeripheryNode.name)
        
        makeTrenchComponent3DLines=self.ansysSweepAlongVector_Lines(trenchComponentNode)+ansysUniteNodes([chip.substrate.node,trenchComponentNode])

        return addTrenchNodeLines,subtractTrenchPeripheryLines,makeTrenchComponent3DLines       
    def updateBumpsDict(self):
        exclusionZonePolylines=[meshPeriphery for thisNode in self.getChipNNodes(0)+self.getChipNNodes(1) for meshPeriphery in thisNode.meshPeripheryPolylines]
        self.bumpsDict["Bumps"]=[]
        bumpIndex=0
        edgeBufferX=0.07*self.chipDict[1].substrate.geometryParamsDict["Width"]
        edgeBufferY=0.07*self.chipDict[1].substrate.geometryParamsDict["Length"]
        print("starting bumps")
        for xVal in np.arange(-self.chipDict[1].substrate.geometryParamsDict["Width"]/2+edgeBufferX,\
                               self.chipDict[1].substrate.geometryParamsDict["Width"]/2-edgeBufferX,\
                               self.bumpsDict["Spacing"]):
            for yVal in np.arange(-self.chipDict[1].substrate.geometryParamsDict["Length"]/2+edgeBufferY,\
                                   self.chipDict[1].substrate.geometryParamsDict["Length"]/2-edgeBufferY,\
                                   self.bumpsDict["Spacing"]):
                #Check if the point lies inside any of the exclusion zones
                exclude="No"
                i=0
                while exclude=="No" and i<len(exclusionZonePolylines):
                    thisExclusionZone=exclusionZonePolylines[i]
                    for point in rectanglePolyline(centerX=xVal,centerY=yVal,width=self.bumpsDict["Under Bump Width"],length=self.bumpsDict["Under Bump Width"],angle=0):
                        if pointInPolyline(point,thisExclusionZone):
                            exclude="Yes"
                    i+=1
                if exclude=="No":
                    #This model depends on what the bumps look like post-squish, which is not currently well known. 
                    totalBumpHeight=self.chipDict[1].ground.outlineNode.Z-(self.chipDict[0].ground.outlineNode.Z+self.chipDict[0].ground.outlineNode.height)
                    underBumpHeight=0.05
                    bumpMetalHeight=(totalBumpHeight-2*underBumpHeight)/2
                    thisBump=Bump()
                    
                    thisBump.underBumpBottomNode=Node(name="underBumpBot"+str(bumpIndex))
                    thisBump.bumpMetalBottomNode=Node(name="bumpMetalBot"+str(bumpIndex))
                    thisBump.bumpMetalTopNode=Node(name="bumpMetalTop"+str(bumpIndex))
                    thisBump.underBumpTopNode=Node(name="underBumpTop"+str(bumpIndex))
                    
                    thisBump.underBumpBottomNode.Z=self.chipDict[0].substrate.node.height+self.chipDict[0].ground.outlineNode.height
                    thisBump.bumpMetalBottomNode.Z=thisBump.underBumpBottomNode.Z+underBumpHeight
                    thisBump.bumpMetalTopNode.Z=self.chipDict[1].ground.outlineNode.Z-underBumpHeight-bumpMetalHeight
                    thisBump.underBumpTopNode.Z=thisBump.bumpMetalTopNode.Z+bumpMetalHeight
                    
                    thisBump.underBumpBottomNode.height=underBumpHeight
                    thisBump.bumpMetalBottomNode.height=bumpMetalHeight
                    thisBump.bumpMetalTopNode.height=bumpMetalHeight
                    thisBump.underBumpTopNode.height=underBumpHeight
                    
                    for node in [thisBump.underBumpBottomNode,thisBump.bumpMetalBottomNode,thisBump.bumpMetalTopNode,thisBump.underBumpTopNode]:
                        node.polylineShape="rectangle"
                    for node in [thisBump.underBumpBottomNode,thisBump.underBumpTopNode]:
                        node.polylineShapeParams={"Body Center X":xVal,\
                                                  "Body Center Y":yVal,\
                                                  "Body Width":self.bumpsDict["Under Bump Width"],\
                                                  "Body Length":self.bumpsDict["Under Bump Width"],\
                                                  "Angle":0,\
                                                  "Side 1 Boundary":0,\
                                                  "Side 2 Boundary":0,\
                                                  "Side 3 Boundary":0,\
                                                  "Side 4 Boundary":0,\
                                                  "Mesh Boundary":self.sysParams["Anti-Vortex Mesh Boundary"]}
                        node.updatePolylines()
                    for node in [thisBump.bumpMetalBottomNode,thisBump.bumpMetalTopNode]:
                        node.polylineShapeParams={"Body Center X":xVal,\
                                                  "Body Center Y":yVal,\
                                                  "Body Width":self.bumpsDict["Bump Metal Width"],\
                                                  "Body Length":self.bumpsDict["Bump Metal Width"],\
                                                  "Angle":0,\
                                                  "Side 1 Boundary":0,\
                                                  "Side 2 Boundary":0,\
                                                  "Side 3 Boundary":0,\
                                                  "Side 4 Boundary":0,\
                                                  "Mesh Boundary":self.sysParams["Anti-Vortex Mesh Boundary"]} 
                        node.updatePolylines()
                    
                    self.bumpsDict["Bumps"].append(thisBump)
                    #print(bumpIndex)
                    bumpIndex+=1
        print("finished bumps")
        lines=["oEditor = oDesign.SetActiveEditor(\"3D Modeler\")\n",\
               "oModuleBoundary = oDesign.GetModule(\"BoundarySetup\")\n"]
        #Draw substrate. Centered on (0,0)
        substrateNode=Node("S")
        substrateWidth=self.CPW.geometryParamsDict["Test Substrate Width"]
        substrateLength=self.CPW.geometryParamsDict["Test Substrate Length"]
        substrateNode.polyline=rectanglePolyline(centerX=0,centerY=0,angle=0,width=substrateWidth,length=substrateLength)#Need to figure out what dimensions are best.
        substrateNode.Z=0
        substrateNode.height=self.CPW.geometryParamsDict["Test Substrate Thickness"]
        substrateNode.color=self.chipDict[0].substrate.node.color
        substrateNode.material=self.chipDict[0].substrate.node.material
        
        lines=lines+self.ansysPolyline_Lines(name=substrateNode.name,\
                                             color=substrateNode.color,\
                                             material=substrateNode.material,\
                                             polyline3D=[[point[0],point[1],substrateNode.Z] for point in substrateNode.polyline])
        lines=lines+self.ansysSweepAlongVector_Lines(substrateNode)
        #Draw CPW
        testCPW=Node("testCPW")
        testCPW.polyline=[[-substrateWidth/2,-self.CPW.geometryParamsDict["Width"]/2],\
                          [-substrateWidth/2,self.CPW.geometryParamsDict["Width"]/2],\
                          [substrateWidth/2,self.CPW.geometryParamsDict["Width"]/2],\
                          [substrateWidth/2,-self.CPW.geometryParamsDict["Width"]/2]]
        testCPW.Z=substrateNode.Z+substrateNode.height
        testCPW.height=self.CPW.geometryParamsDict["Height"]
        testCPW.material=self.sysParams["Material"]
        lines=lines+self.ansysPolyline_Lines(name=testCPW.name,\
                                             color=testCPW.color,\
                                             material=testCPW.material,\
                                             polyline3D=[[point[0],point[1],testCPW.Z] for point in testCPW.polyline])
        lines=lines+self.ansysSweepAlongVector_Lines(testCPW)
        #Draw trenches
        trench1=Node("trench1")
        trench1.polyline=rectanglePolyline(centerX=0,\
                                           centerY=self.CPW.geometryParamsDict["Width"]/2+self.CPW.geometryParamsDict["Gap"]/2,\
                                           angle=0,\
                                           width=substrateWidth,\
                                           length=self.CPW.geometryParamsDict["Gap"])
        trench1.Z=substrateNode.Z+substrateNode.height-self.CPW.geometryParamsDict["Trench"]
        trench1.height=self.CPW.geometryParamsDict["Trench"]
        trench1.material="silicon"
        lines=lines+self.ansysPolyline_Lines(name=trench1.name,\
                                             color=trench1.color,\
                                             material=trench1.material,\
                                             polyline3D=[[point[0],point[1],trench1.Z] for point in trench1.polyline])
        lines=lines+self.ansysSweepAlongVector_Lines(trench1)
        lines=lines+self.ansysSubtract_Lines(substrateNode.name,trench1.name)
        
        trench2=Node("trench2")
        trench2.polyline=rectanglePolyline(centerX=0,\
                                           centerY=-self.CPW.geometryParamsDict["Width"]/2-self.CPW.geometryParamsDict["Gap"]/2,\
                                           angle=0,\
                                           width=substrateWidth,\
                                           length=self.CPW.geometryParamsDict["Gap"])
        trench2.Z=substrateNode.Z+substrateNode.height-self.CPW.geometryParamsDict["Trench"]
        trench2.height=self.CPW.geometryParamsDict["Trench"]
        trench2.material="silicon"
        lines=lines+self.ansysPolyline_Lines(name=trench2.name,\
                                             color=trench2.color,\
                                             material=trench2.material,\
                                             polyline3D=[[point[0],point[1],trench2.Z] for point in trench2.polyline])
        lines=lines+self.ansysSweepAlongVector_Lines(trench2)
        lines=lines+self.ansysSubtract_Lines(substrateNode.name,trench2.name)
        
        #Draw ground on either side (1 and 2). 
        groundLength=1/2*(substrateLength-2*self.CPW.geometryParamsDict["Gap"]-self.CPW.geometryParamsDict["Width"])
        groundWidth=substrateWidth
        groundPlusY=Node("groundPlusY")
        groundPlusY.polyline=rectanglePolyline(centerX=0,\
                                               centerY=self.CPW.geometryParamsDict["Width"]/2+\
                                                       self.CPW.geometryParamsDict["Gap"]+\
                                                       groundLength/2,\
                                               width=groundWidth,\
                                               length=groundLength,\
                                               angle=0)
        groundPlusY.material=self.sysParams["Material"]
        if self.sysParams["Flip Chip?"]=="Yes":
            groundPlusY.height=self.chipDict[0].ground.outlineNode.height
        elif self.sysParams["Flip Chip?"]=="No": 
            groundPlusY.height=self.chipDict[0].ground.outlineNode.height
        
        groundPlusY.Z=substrateNode.Z+substrateNode.height
        lines=lines+self.ansysPolyline_Lines(name=groundPlusY.name,\
                                             color=groundPlusY.color,\
                                             material=groundPlusY.material,\
                                             polyline3D=[[point[0],point[1],groundPlusY.Z] for point in groundPlusY.polyline])    
        lines=lines+self.ansysSweepAlongVector_Lines(groundPlusY)
        groundMinusY=Node("groundMinusY")
        groundMinusY.polyline=rectanglePolyline(centerX=0,\
                                                centerY=-self.CPW.geometryParamsDict["Width"]/2+\
                                                        -self.CPW.geometryParamsDict["Gap"]+\
                                                        -groundLength/2,\
                                                angle=0,\
                                                width=groundWidth,\
                                                length=groundLength)
        groundMinusY.material=self.sysParams["Material"]
        groundMinusY.height=groundPlusY.height
        groundMinusY.Z=substrateNode.Z+substrateNode.height
        lines=lines+self.ansysPolyline_Lines(name=groundMinusY.name,\
                                             color=groundMinusY.color,\
                                             material=groundMinusY.material,\
                                             polyline3D=[[point[0],point[1],groundMinusY.Z] for point in groundMinusY.polyline])
        lines=lines+self.ansysSweepAlongVector_Lines(groundMinusY)
        #Draw air box
        airBox=Node("airBox")
        airBox.polyline=substrateNode.polyline
        airBox.material="vacuum"
        airBox.color="(0 128 255)"#Blue
        airBox.height=3*substrateNode.height#3 is arbitrary. 
        airBox.Z=-substrateNode.height#starts a substrate height below the substrate so it is vertically centered. 
        lines=lines+self.ansysPolyline_Lines(name=airBox.name,\
                                             color=airBox.color,\
                                             material=airBox.material,\
                                             polyline3D=[[point[0],point[1],airBox.Z] for point in airBox.polyline])
        lines=lines+self.ansysSweepAlongVector_Lines(airBox)
        #Assign radiation boundary condition to airbox
        lines=lines+["oModuleBoundary.AssignRadiation(\n",\
                     "    [\n",\
                     "        \"NAME:Rad1\",\n",\
                     "        \"Objects:=\"		, [\"airBox\"],\n",\
                     "        \"IsFssReference:=\"	, False,\n",\
                     "        \"IsForPML:=\"		, False\n",\
                     "    ])\n"]
        #Draw waveport sheets, assign waveports. 
        waveportColor="(255 0 255)"#Pink
        waveportMaterial="vacuum"
        #Width and height given by blog post guidelines in Notes file. 
        #sheetHeight=4*self.CPW.geometryParamsDict["Gap"]
        #sheetLength=10*max(self.CPW.geometryParamsDict["Width"],self.CPW.geometryParamsDict["Gap"]) 
        sheetHeight=220
        sheetLength=220
        sheetCenterZ=substrateNode.height+1/2*self.CPW.geometryParamsDict["Height"]
        sheet1Polyline=[[-substrateWidth/2,-sheetLength/2,sheetCenterZ-sheetHeight/2],\
                        [-substrateWidth/2,sheetLength/2,sheetCenterZ-sheetHeight/2],\
                        [-substrateWidth/2,sheetLength/2,sheetCenterZ+sheetHeight/2],\
                        [-substrateWidth/2,-sheetLength/2,sheetCenterZ+sheetHeight/2]]
        sheet2Polyline=[[substrateWidth/2,-sheetLength/2,sheetCenterZ-sheetHeight/2],\
                        [substrateWidth/2,sheetLength/2,sheetCenterZ-sheetHeight/2],\
                        [substrateWidth/2,sheetLength/2,sheetCenterZ+sheetHeight/2],\
                        [substrateWidth/2,-sheetLength/2,sheetCenterZ+sheetHeight/2]]
        lines=lines+self.ansysPolyline_Lines(name="waveport1",\
                                             color=waveportColor,\
                                             material=waveportMaterial,\
                                             polyline3D=sheet1Polyline)
        lines=lines+self.ansysWaveport("waveport1",1)
        lines=lines+self.ansysPolyline_Lines(name="waveport2",\
                                             color=waveportColor,\
                                             material=waveportMaterial,\
                                             polyline3D=sheet2Polyline)
        lines=lines+self.ansysWaveport("waveport2",2)

        return lines  
    def netlistCircuitLines(self,netlistComponents): 
        lines=[]
        #Capacitors
        for capacitanceName,capacitance in netlistComponents["Capacitances"].items():
            lines.append(capacitanceName+" "+capacitance["node1NetlistName"]+" "+capacitance["node2NetlistName"]+" "+str(capacitance["C"])+"\n")
        #Inductors
        for inductorName,inductor in netlistComponents["Inductors"].items():
            lines.append(inductorName+" "+inductor["node1NetlistName"]+" "+inductor["node2NetlistName"]+" "+str(inductor["L"])+"\n")
        #Resistors
        for resistorName,resistor in netlistComponents["Resistors"].items():
            lines.append(resistorName+" "+resistor["node1NetlistName"]+" "+resistor["node2NetlistName"]+" "+str(resistor["R"])+"\n")
        #Transmission Lines
        for transmissionLineName,transmissionLine in netlistComponents["Transmission Lines"].items():
            lines.append(transmissionLineName+" "+transmissionLine["node1NetlistName"]+" 0 "+transmissionLine["node2NetlistName"]+" 0 "\
            +"Z0=50 TD="+str(transmissionLine["TD"])+"\n")
        
        return lines
    def loadSimulationParametersFile(self,simType):
        simParamsFileLines=csvRead(self.simFiles[simType]["Params"])
        simParams=dict()
        for line in simParamsFileLines:
            simParams[line[0]]=returnCorrectType(line[1])
        return simParams   
    @property
    def allQubitsDict(self):
        allQubits=dict()
        for chipIndex,chip in self.chipDict.items():
            for qubitIndex,qubit in chip.qubitDict.items():
                allQubits[qubitIndex]=qubit
        return allQubits
    @property
    def allReadoutResonatorsDict(self):
        allReadoutResonators=dict()
        for chipIndex,chip in self.chipDict.items():
            for readoutResonatorIndex,readoutResonator in chip.readoutResonatorDict.items():
                allReadoutResonators[readoutResonatorIndex]=readoutResonator
        return allReadoutResonators
    @property
    def allPTCsDict(self):
        allPTCs=dict()
        for chipIndex,chip in self.chipDict.items():
            for PTCIndex,PTC in chip.PTCDict.items():
                allPTCs[PTCIndex]=PTC
        return allPTCs
    @property
    def allStraightBusCouplersDict(self):
        allStraightBusCouplers=dict()
        for chipIndex,chip in self.chipDict.items():
            for straightBusCouplerIndex,straightBusCoupler in chip.straightBusCouplerDict.items():
                allStraightBusCouplers[straightBusCouplerIndex]=straightBusCoupler
        return allStraightBusCouplers
    @property
    def allControlLinesDict(self):
        allControlLines=dict()
        for chipIndex,chip in self.chipDict.items():
            for controlLineIndex,controlLine in chip.controlLineDict.items():
                allControlLines[controlLineIndex]=controlLine
        return allControlLines       
    def getChipNNodes(self,N):#Doesn't include ground,substrate, or launchPads
        allNodes=[]
        for qubitIndex,qubit in self.chipDict[N].qubitDict.items():
            allNodes=allNodes+[pad.node for pad in qubit.padListGeom]
        for readoutResonatorIndex,readoutResonator in self.chipDict[N].readoutResonatorDict.items():
            allNodes=allNodes+[readoutResonator.pad1.node,readoutResonator.pad2.node,readoutResonator.meanderNode]
        for PTCIndex,PTC in self.chipDict[N].PTCDict.items():
            allNodes=allNodes+[PTC.pad1.node,PTC.pad2.node,PTC.meanderNode]
        for straightBusCouplerIndex,straightBusCoupler in self.chipDict[N].straightBusCouplerDict.items():
            allNodes=allNodes+[straightBusCoupler.pad1.node,straightBusCoupler.pad2.node]
        for controlLineIndex,controlLine in self.chipDict[N].controlLineDict.items():
            #print(len(allNodes))
            allNodes.append(controlLine.lineNode)
            for launchPadName,launchPad in controlLine.launchPadNodeDict.items():
                allNodes.append(launchPad)
        return allNodes
    def getChipNNodes_CapMat(self,N):
        allNodes=[]
        for qubitIndex,qubit in self.chipDict[N].qubitDict.items():
            allNodes=allNodes+[pad.node for pad in qubit.padListGeom]
        for readoutResonatorIndex,readoutResonator in self.chipDict[N].readoutResonatorDict.items():
            allNodes=allNodes+[readoutResonator.pad1.node,readoutResonator.pad2.node]
        for PTCIndex,PTC in self.chipDict[N].PTCDict.items():
            allNodes=allNodes+[PTC.pad1.node,PTC.pad2.node]
        for straightBusCouplerIndex,straightBusCoupler in self.chipDict[N].straightBusCouplerDict.items():
            allNodes=allNodes+[straightBusCoupler.pad1.node,straightBusCoupler.pad2.node]
        for controlLineIndex,controlLine in self.chipDict[N].controlLineDict.items():
            if controlLine.generalParamsDict["Type"]=="feedline" and self.sysParams["Simulate Feedline?"]=="Yes":
                allNodes.append(controlLine.lineNode)
                for launchPadName,launchPad in controlLine.launchPadNodeDict.items():
                    allNodes.append(launchPad)
           # if not (controlLine.generalParamsDict["Type"]=="feedline" and self.sysParams["Simulate Feedline?"]=="No"):
               # allNodes.append(controlLine.lineNode)
               # for launchPadName,launchPad in controlLine.launchPadNodeDict.items():
                   # allNodes.append(launchPad)
        return allNodes
    @property
    def capMatUnitsToF(self):
        capMatResultsFileLines=csvRead(self.simFiles["capMat"]["Q3D Simulations"]["q3dExtractor"]["ResultsFile"])
        reportedUnits=capMatResultsFileLines[2][0][8:]#"C Units:pF"->"pF"
        unitsMultiplier=1
        if reportedUnits=="pF":
            unitsMultiplier=1e-12
        return unitsMultiplier
    def capMatForGE(self):
        dimPreGEQuant=len(self.preGECapMatHeaders)
        capMat_preGE=zeros(dimPreGEQuant,dimPreGEQuant)
        capMatReduced=Matrix(self.capMat)
        #Alter the resonator pad 2 capacitance to ground according to the lumped resonator model. 
        for readoutResonatorIndex,readoutResonator in self.allReadoutResonatorsDict.items():
            index=self.ansysCapMatHeaders.index(readoutResonator.pad2.node.name)
            capMatReduced[index,index]=capMatReduced[index,index]-sum(capMatReduced.row(index))+readoutResonator.equivC  
        #Remove all control lines and resonator pad1 from the capacitance matrix. This is under the assumption that
        #the resonator pad1 only has a non-negligible capacitance to the feedline, thereby not affecting the system Hamiltonian. 
        indicesToRemove=[]
        for nodeName in self.ansysCapMatHeaders:
            if nodeName in [controlLine.lineNode.name for controlLine in self.allControlLinesDict.values()]:
                index=self.ansysCapMatHeaders.index(nodeName)
                indicesToRemove.append(index)
        for readoutResonatorIndex,readoutResonator in self.allReadoutResonatorsDict.items():
            index=self.ansysCapMatHeaders.index(readoutResonator.pad1.node.name)
            indicesToRemove.append(index)
        for PTCIndex,PTC in self.allPTCsDict.items():
            index=self.ansysCapMatHeaders.index(PTC.pad1.node.name)
            indicesToRemove.append(index)
        indicesToRemove.sort(reverse=True)
        
        ansysCapMatHeadersReduced=[i for i in self.ansysCapMatHeaders]#Simple copy
        for i in indicesToRemove:
            capMatReduced.row_del(i)
            capMatReduced.col_del(i)
            del ansysCapMatHeadersReduced[i]  
        #Now reorder quantCapMat to align with self.preGECapMatHeaders
        for node1Index,node1Name in enumerate(self.preGECapMatHeaders):
            for node2Index,node2Name in enumerate(self.preGECapMatHeaders):
                capMat_preGE[node1Index,node2Index]=capMatReduced[ansysCapMatHeadersReduced.index(node1Name),ansysCapMatHeadersReduced.index(node2Name)]
        return capMat_preGE
    def loadSimResults(self,simType):
        resultsFileLines=csvRead(self.simFiles[simType]["ResultsFile"])
        if simType=="quantize":
            HIndexLineIndex=resultsFileLines.index([i for i in resultsFileLines if i[0]=="Index Order"][0])+1
            self.HComponentOrder=[self.componentFromName(i) for i in arrayNoBlanks(resultsFileLines[HIndexLineIndex])]
            for index,component in enumerate(self.HComponentOrder):
                component.quantizeIndex=index
            headerLineIndex=resultsFileLines.index([i for i in resultsFileLines if i[0]=="H (GHz)"][0])+1
            self.HStateOrder=[stateFromHeader(i) for i in arrayNoBlanks(resultsFileLines[headerLineIndex][1:])]
            
            HStartLineIndex=headerLineIndex+1

            numStates=len(self.HStateOrder)
            self.H=np.zeros((numStates,numStates))
            for index1 in range(numStates):
                for index2 in range(numStates):
                    matRow=HStartLineIndex+index1
                    matCol=1+index2
                    matElem=float(resultsFileLines[matRow][matCol])
                    self.H[index1,index2]=matElem
            
            HEvalsIndex=resultsFileLines.index([i for i in resultsFileLines if i[0]=="H_evals"][0])+1
            self.HEvals=[float(i) for i in arrayNoBlanks(resultsFileLines[HEvalsIndex])]
        if simType=="capMatGE":
            headerLineIndex=1
            numNodes=len(self.postGEComponentList)
            self.capMatGE=np.zeros((numNodes,numNodes))
            capMatGEStartLineIndex=headerLineIndex+1
            for index1 in range(numNodes):
                for index2 in range(numNodes):
                    matRow=capMatGEStartLineIndex+index1
                    matCol=1+index2
                    capacitanceValue=float(resultsFileLines[matRow][matCol])
                    self.capMatGE[index1,index2]=capacitanceValue
        if simType=="capMat":
            capMatHeaderLineIndex=resultsFileLines.index([i for i in resultsFileLines if i[0]=="Capacitance (F)"][0])+1
            self.ansysCapMatHeaders=arrayNoBlanks(resultsFileLines[capMatHeaderLineIndex])
            numNodes=len(self.ansysCapMatHeaders)
            
            self.capMat=np.zeros((numNodes,numNodes))
            capMatStartLineIndex=capMatHeaderLineIndex+1
            for index1 in range(numNodes):
                for index2 in range(numNodes):
                    matRow=capMatStartLineIndex+index1
                    matCol=1+index2
                    capacitanceValue=float(resultsFileLines[matRow][matCol])#Already in units of F
                    self.capMat[index1,index2]=capacitanceValue
            
            #If the feedline is not simulated, add in the capacitance to the resonators. 
            if self.sysParams["Simulate Feedline?"]=="No" and self.allControlLinesDict!={}:
                newCapMat=np.zeros((numNodes+1,numNodes+1))#The feedline will be the highest index.
                feedlineIndex=numNodes
                self.ansysCapMatHeaders.append(self.allControlLinesDict[0].lineNode.name)
                #Copy self.capMat
                for index1 in range(numNodes):
                    for index2 in range(numNodes):
                        newCapMat[index1,index2]=self.capMat[index1,index2]
                #Add resonator capacitances
                for readoutResonatorIndex,readoutResonator in self.allReadoutResonatorsDict.items():
                    pad1Index=self.ansysCapMatHeaders.index(readoutResonator.pad1.node.name)
                    #Capacitance to the feedline    
                    newCapMat[pad1Index,feedlineIndex]=-readoutResonator.generalParamsDict["Capacitance to Feedline (F)"]
                    newCapMat[feedlineIndex,pad1Index]=-readoutResonator.generalParamsDict["Capacitance to Feedline (F)"]
                    #Fix capacitance to ground
                    wrongCapToGround=sum(self.capMat[pad1Index,:])
                    correctCapToGround=readoutResonator.generalParamsDict["Feedline Pad Capacitance to Ground (F)"]
                    newCapMat[pad1Index,pad1Index]=self.capMat[pad1Index,pad1Index]-wrongCapToGround+correctCapToGround
                self.capMat=newCapMat
        if simType[0:6]=="decayQ":
            qubitIndex=int(simType[6:])
            qubit=self.allQubitsDict[qubitIndex]
            qubit.T1=resultsDict(self.simFiles[simType]["ResultsFile"])["T1 (s):"]
        # if simType[0:5]=="exchQ":#commented out because post-process has not yet been implemented.
            # qubitIndex=int(simType[5:])
        if simType[0:3]=="ECQ":
            qubitIndex=int(simType[3:])
            qubit=self.allQubitsDict[qubitIndex]
            qubit.EcVal=resultsDict(self.simFiles[simType]["ResultsFile"])["EC"]
        if simType[0:10]=="quantFreqQ":
            qubitIndex=int(simType[10:])
            qubit=self.allQubitsDict[qubitIndex]
            qubit.freq=resultsDict(self.simFiles[simType]["ResultsFile"])["Frequency (GHz):"]
        if simType[0:14]=="anharmonicityQ":
            qubitIndex=int(simType[14:])
            qubit=self.allQubitsDict[qubitIndex]
            qubit.anharmonicity=resultsDict(self.simFiles[simType]["ResultsFile"])["anharmonicity (MHz):"]
        if simType[0:7]=="lumpedR":
            readoutResonatorIndex=int(simType[7:])
            readoutResonator=self.allReadoutResonatorsDict[readoutResonatorIndex]
            readoutResonator.equivL=resultsDict(self.simFiles[simType]["ResultsFile"])["equivL(H):"]
            readoutResonator.equivC=resultsDict(self.simFiles[simType]["ResultsFile"])["equivC(F):"]
        if simType[0:3]=="ECR":
            readoutResonatorIndex=int(simType[3:])
            readoutResonator=self.allReadoutResonatorsDict[readoutResonatorIndex]
            readoutResonator.EcVal=resultsDict(self.simFiles[simType]["ResultsFile"])["EC"]
        # if simType[0:11]=="freqLumpedR":#Will work on when needed.        
                # readoutResonatorIndex=int(simType[11:])
        if simType[0:10]=="quantFreqR":
            readoutResonatorIndex=int(simType[10:])
            readoutResonator=self.allReadoutResonatorsDict[readoutResonatorIndex]
            readoutResonator.freq=resultsDict(self.simFiles[simType]["ResultsFile"])["Frequency (GHz):"]
        if simType[0:17]=="feedlineCouplingR":
            readoutResonatorIndex=int(simType[17:])  
    def loadCPWSimulationResults(self):
        CPWPhaseVelocityFileLines=csvRead(self.simFiles["CPW"]["HFSS Simulations"]["portSweep"]["phaseVelocityResults"])
        self.CPW.vp=CPWPhaseVelocityFileLines[1][1]#Just uses the 5GHz record for now. More accurate simulations should use experimentally-determined phase velocity. 
    def loadNetlistFile(self,ansysFile,netlistFile):#I hate this method, but it's the only way I know of to load the netlist into the aedt project. 
        netlistFile = open(netlistFile, 'r') 
        netlistFileLines = netlistFile.readlines()
        netlistFileLinesAedtEdit=[aedtEdit(i) for i in netlistFileLines]

        ansysProjectFile = open(ansysFile, 'r') 
        ansysProjectFileLines = ansysProjectFile.readlines()    
        
        startLineIndex=ansysProjectFileLines.index("\t\t$begin \'Netlist\'\n")
        endLineIndex=ansysProjectFileLines.index("\t\t$end \'Netlist\'\n")
        
        beforeLines=ansysProjectFileLines[0:startLineIndex+1]
        afterLines=ansysProjectFileLines[endLineIndex:]
        betweenLines=[]
        betweenLines.append("\t\t\tText=\'"+netlistFileLinesAedtEdit[0][0:-1]+"\\\n")#Need to remove \n at end of line. 
        for line in netlistFileLinesAedtEdit[1:-1]:
            betweenLines.append(line[0:-1]+"\\\n")
        betweenLines.append(netlistFileLinesAedtEdit[-1]+"\'\n")#No \n to remove at end of line!

        ansysProjectFileInstance=open(ansysFile,"w+",newline='')#Overwrites aedt file to insert netlist
        ansysProjectFileInstance.writelines(beforeLines+betweenLines+afterLines)#Initialization lines.
        ansysProjectFileInstance.close()
    def ansysGroundSignalLine_Lines(self):
        return ["oModuleBoundary.AssignGroundNet(\n",\
            "    [\n",\
            "        \"NAME:GroundNet1\",\n",\
            "        \"Objects:=\"		, [\""+self.chipDict[0].ground.name+"\"]\n",\
            "    ])\n"]
    def ansysQ3DMake3D(self,node):#This function makes the node 3D either by actually making it 3D, or assigning the thin conductor boundary condition (if simulation="2D")
        if self.sysParams["Simulation"]=="3D":
            return self.ansysSweepAlongVector_Lines(node)
        elif self.sysParams["Simulation"]=="2D":
            return self.ansysThinConductor(node)
    def runAnsysSimulator(self,ansysFile,simulatorFile,simDirectory,maxRunTime):
        simulateCommand=""
        if self.sysParams["Compute Location"]=="Windows":
            ansysExecutableFile="\"%ProgramFiles%/AnsysEM/AnsysEM19.5/Win64/ansysedt.exe\""
            simulateCommand=str(ansysExecutableFile)+' -features=beta -ng -runscriptandexit '\
                           +str(simulatorFile)+' '+str(ansysFile)
        elif self.sysParams["Compute Location"]=="Cluster":
            simulateCommand=str(self.sysParams["QSM Source Folder"]/"helperFiles"/"ansysBatch")+" ansys "+str(simulatorFile)+" "+str(ansysFile)+" "+str(simDirectory)+" "+str(maxRunTime)
        subprocess.call(simulateCommand,shell=True)
    def runQuantizeSimulator(self,simDirectory,maxRunTime):
        simulateCommand=str(self.sysParams["QSM Source Folder"]/"helperFiles"/"qubitSimulatorBatch")+" test "+simDirectory+" "+str(maxRunTime)
        subprocess.call(simulateCommand,shell=True)
    def ansysPolyline_Lines(self,name,color,material,polyline3D):#polyline3D has x,y,z vals, not just the x,y vals of node.polyline
        lines=["oEditor.CreatePolyline(\n",\
               "    [\n",\
               "        \"NAME:PolylineParameters\",\n",\
               "        \"IsPolylineCovered:=\"	, True,\n",\
               "        \"IsPolylineClosed:=\"	, True,\n",\
               "        [\n",\
			   "            \"NAME:PolylinePoints\",\n"]
        numPoints=len(polyline3D)
        pointIndex=0
        for point in polyline3D+[polyline3D[0]]:#The polyline wraps back to the first point. 
            lines=lines+["            [\n",\
                         "                \"NAME:PLPoint\",\n",\
                         "                \"X:=\"			, \""+str(point[0])+lengthUnits+"\",\n",\
                         "                \"Y:=\"			, \""+str(point[1])+lengthUnits+"\",\n",\
                         "                \"Z:=\"			, \""+str(point[2])+lengthUnits+"\"\n"]
            if pointIndex==numPoints:
                lines=lines+["            ]\n"]
            else:
                lines=lines+["            ],\n"]
            pointIndex=pointIndex+1
        lines=lines+["        ],\n",\
                     "        [\n",\
                     "            \"NAME:PolylineSegments\",\n"]
        for pointIndex in range(numPoints):
            lines=lines+["            [\n",\
                         "                \"NAME:PLSegment\",\n",\
                         "                \"SegmentType:=\"		, \"Line\",\n",\
                         "                \"StartIndex:=\"		, "+str(pointIndex)+",\n",\
                         "                \"NoOfPoints:=\"		, 2\n"]
            if pointIndex==numPoints-1:
                lines=lines+["            ]\n"]
            else:
                lines=lines+["            ],\n"]
        solveInside="False"
        if material=="silicon" or material=="vacuum":
            solveInside="True"
        lines=lines+["        ],\n",\
                     "        [\n",\
                     "            \"NAME:PolylineXSection\",\n",\
                     "            \"XSectionType:=\"	, \"None\",\n",\
                     "            \"XSectionOrient:=\"	, \"Auto\",\n",\
                     "            \"XSectionWidth:=\"	, \"0mm\",\n",\
                     "            \"XSectionTopWidth:=\"	, \"0mm\",\n",\
                     "            \"XSectionHeight:=\"	, \"0mm\",\n",\
                     "            \"XSectionNumSegments:=\"	, \"0\",\n",\
                     "            \"XSectionBendType:=\"	, \"Corner\"\n",\
                     "        ]\n",\
                     "    ],\n",\
	                 "    [\n",\
                     "        \"NAME:Attributes\",\n",\
                     "        \"Name:=\"		, \""+name+"\",\n",\
                     "        \"Flags:=\"		, \"\",\n",\
                     "        \"Color:=\"		, \""+color+"\",\n",\
                     "        \"Transparency:=\"	, 0,\n",\
                     "        \"PartCoordinateSystem:=\", \"Global\",\n",\
                     "        \"UDMId:=\"		, \"\",\n",\
                     "        \"MaterialValue:=\"	, \"\\\""+material+"\\\"\",\n",\
                     "        \"SurfaceMaterialValue:=\", \"\\\"\\\"\",\n",\
                     "        \"SolveInside:=\"		, "+solveInside+",\n",\
                     "        \"IsMaterialEditable:=\"	, True,\n",\
                     "        \"UseMaterialAppearance:=\", False,\n",\
                     "        \"IsLightweight:=\"	, False\n",\
                     "    ])\n"]
        return lines      
    def ansysSubtract_Lines(self,part1Name,part2Name):#Subtract polyline2 from polyline 1, leaving polyline 1. 
        return ["oEditor.Subtract(\n",\
                "    [\n",\
                "        \"NAME:Selections\",\n",\
                "        \"Blank Parts:=\"		, \""+part1Name+"\",\n",\
                "        \"Tool Parts:=\"		, \""+part2Name+"\"\n",\
                "    ],\n",\
                "    [\n",\
                "        \"NAME:SubtractParameters\",\n",\
                "        \"KeepOriginals:=\"	, False\n",\
                "    ])\n"]
    def ansysThinConductor(self,node):
        return ["oModuleBoundary.AssignThinConductor(\n",\
                "    [\n",\
                "        \"NAME:ThinCond"+node.name+"\",\n",\
                "        \"Objects:=\"		, [\""+node.name+"\"],\n",\
                "        \"Material:=\"		, \""+node.material+"\",\n",\
                "        \"Thickness:=\"		, \""+str(node.height)+lengthUnits+"\"\n",\
                "    ])\n"]
    def ansysSweepAlongVector_Lines(self,node):#Seeps along the positive Z direction.
        return["oEditor.SweepAlongVector(\n",\
               "    [\n",\
               "        \"NAME:Selections\",\n",\
               "        \"Selections:=\"		, \""+node.name+"\",\n",\
               "        \"NewPartsModelFlag:=\"	, \"Model\"\n",\
               "    ],\n",\
               "    [\n",\
               "        \"NAME:VectorSweepParameters\",\n",\
               "        \"DraftAngle:=\"		, \"0deg\",\n",\
               "        \"DraftType:=\"		, \"Round\",\n",\
               "        \"CheckFaceFaceIntersection:=\", False,\n",\
               "        \"SweepVectorX:=\"	, \"0mm\",\n",\
               "        \"SweepVectorY:=\"	, \"0mm\",\n",\
               "        \"SweepVectorZ:=\"	, \""+str(node.height)+lengthUnits+"\",\n",\
               "    ])\n"]
    def initAllCircuitSims(self):#Assumes all init files exist and are populated as intended. 
        self.simulation(["simulation","fullS21","init"])
        for qubitIndex in range(self.sysParams["Number of Qubits"]):
            self.simulation(["simulation","circFreqQ"+str(qubitIndex),"init"])
            self.simulation(["simulation","decayQ"+str(qubitIndex),"init"])
        for readoutResonatorIndex in range(self.sysParams["Number of Readout Resonators"]):
            self.simulation(["simulation","circFreqR"+str(readoutResonatorIndex),"init"])
            self.simulation(["simulation","lumpedR"+str(readoutResonatorIndex),"init"])
            self.simulation(["simulation","feedlineCouplingR"+str(readoutResonatorIndex),"init"])
    def runAllCircuitSims(self):#Assumes all init files exist and are populated as intended. 
        print("running fullS21")
        self.simulation(["simulation","fullS21","run"])
        for qubitIndex in range(self.sysParams["Number of Qubits"]):
            print("running circFreqQ"+str(qubitIndex))
            self.simulation(["simulation","circFreqQ"+str(qubitIndex),"run"])
            #print("running decayQ"+str(qubitIndex))
            #self.simulation(["simulation","decayQ"+str(qubitIndex),"run"])
        for readoutResonatorIndex in range(self.sysParams["Number of Readout Resonators"]):
            print("running circFreqR"+str(readoutResonatorIndex))
            self.simulation(["simulation","circFreqR"+str(readoutResonatorIndex),"run"])
            print("running lumpedR"+str(readoutResonatorIndex))
            self.simulation(["simulation","lumpedR"+str(readoutResonatorIndex),"run"])
            #print("running feedlineCouplingR"+str(readoutResonatorIndex))
            #self.simulation(["simulation","feedlineCouplingR"+str(readoutResonatorIndex),"run"])
    def postProcessAllCircuitSims(self):
        print("Post-Processing fullS21")
        self.simulation(["simulation","fullS21","postProcess"])
        for qubitIndex in range(self.sysParams["Number of Qubits"]):
            print("Post-Processing circFreqQ"+str(qubitIndex))
            self.simulation(["simulation","circFreqQ"+str(qubitIndex),"postProcess"])
            #print("Post-Processing decayQ"+str(qubitIndex))
            #self.simulation(["simulation","decayQ"+str(qubitIndex),"postProcess"])
        for readoutResonatorIndex in range(self.sysParams["Number of Readout Resonators"]):
            print("Post-Processing circFreqR"+str(readoutResonatorIndex))
            self.simulation(["simulation","circFreqR"+str(readoutResonatorIndex),"postProcess"])
            print("Post-Processing lumpedR"+str(readoutResonatorIndex))
            self.simulation(["simulation","lumpedR"+str(readoutResonatorIndex),"postProcess"])
            #print("Post-Processing feedlineCouplingR"+str(readoutResonatorIndex))
            #self.simulation(["simulation","feedlineCouplingR"+str(readoutResonatorIndex),"postProcess"])
    def GEPlusAllEC(self):
        print("running gaussianElimination")
        self.simulation(["simulation","capMatGE","init"])
        self.simulation(["simulation","capMatGE","postProcess"])
        for qubitIndex in range(self.sysParams["Number of Qubits"]):
            print("running ECQ"+str(qubitIndex))
            self.simulation(["simulation","ECQ"+str(qubitIndex),"init"])
            self.simulation(["simulation","ECQ"+str(qubitIndex),"postProcess"])
        for readoutResonatorIndex in range(self.sysParams["Number of Readout Resonators"]):
            print("running ECR"+str(readoutResonatorIndex))
            self.simulation(["simulation","ECR"+str(readoutResonatorIndex),"init"])
            self.simulation(["simulation","ECR"+str(readoutResonatorIndex),"postProcess"])
    def AllL_i(self):
        for qubitIndex in range(self.sysParams["Number of Qubits"]):
            print("running L_iQ"+str(qubitIndex))
            self.simulation(["simulation","L_iQ"+str(qubitIndex),"init"])
            self.simulation(["simulation","L_iQ"+str(qubitIndex),"postProcess"])
    def Allzz(self):
        qubitList=[component for component in self.HComponentOrder if isinstance(component,Qubit)]
        for qubit1 in qubitList:
            for qubit2 in qubitList:
                if qubit1.index<qubit2.index:
                    print("running zzQ"+str(qubit1.index)+"-"+str(qubit2.index))
                    self.simulation(["simulation","zzQ"+str(qubit1.index)+"-"+str(qubit2.index),"init"])
                    self.simulation(["simulation","zzQ"+str(qubit1.index)+"-"+str(qubit2.index),"postProcess"])
    def AllAnharmonicityQ(self):
        for component in self.HComponentOrder:
            if isinstance(component,Qubit):
                print("running anharmonicityQ"+str(component.index))
                self.simulation(["simulation","anharmonicityQ"+str(component.index),"init"])
                self.simulation(["simulation","anharmonicityQ"+str(component.index),"postProcess"])
    def AllQuantFreq(self):
        for component in self.HComponentOrder:
            if isinstance(component,Qubit):
                print("running quantFreqQ"+str(component.index))
                self.simulation(["simulation","quantFreqQ"+str(component.index),"init"])
                self.simulation(["simulation","quantFreqQ"+str(component.index),"postProcess"])
            elif isinstance(component,ReadoutResonator):
                print("running quantFreqR"+str(component.index))
                self.simulation(["simulation","quantFreqR"+str(component.index),"init"])
                self.simulation(["simulation","quantFreqR"+str(component.index),"postProcess"])
    def AllDispersiveShiftR(self):
        for component in self.HComponentOrder:
            if isinstance(component,ReadoutResonator):
                print("running dispersiveShiftR"+str(component.index))
                self.simulation(["simulation","dispersiveShiftR"+str(component.index),"init"])
                self.simulation(["simulation","dispersiveShiftR"+str(component.index),"postProcess"])         
    def gaussianElimination(self,capMat_preGE):
        I_c=symbols('I_c')
        capMat_GE=capMat_preGE
        dimPreGEQuant=len(self.preGECapMatHeaders)
        #Assemble the RHS and PhiMat
        RHS=zeros(dimPreGEQuant,1)
        phiMat=zeros(dimPreGEQuant,1)
        t=symbols('t')
        for component in self.postGEComponentList:
            if isinstance(component,floatingQubit) or isinstance(component,StraightBusCoupler):
                RHS[component.pad1.quantCapMatIndex,0]=I_c*sin((component.pad1.phiSym-component.pad2.phiSym)/Phi_0Const)
                RHS[component.pad2.quantCapMatIndex,0]=-RHS[component.pad1.quantCapMatIndex,0]
                phiMat[component.pad1.quantCapMatIndex,0]=component.pad1.phiSym.diff(t,2)
                phiMat[component.pad2.quantCapMatIndex,0]=component.pad2.phiSym.diff(t,2)
            elif isinstance(component,groundedQubit):
                RHS[component.pad1.quantCapMatIndex,0]=I_c*sin(component.pad1.phiSym/Phi_0Const)
                phiMat[component.pad1.quantCapMatIndex,0]=component.pad1.phiSym.diff(t,2)
            elif isinstance(component,ReadoutResonator):
                RHS[component.pad2.quantCapMatIndex,0]=component.pad2.phiSym/Phi_0Const
                phiMat[component.pad2.quantCapMatIndex,0]=component.pad2.phiSym.diff(t,2)
        capMat_GE=capMat_preGE
       #Perform the gaussian elimination on just the qubits.
        for componentIndex,component in enumerate(self.postGEComponentList):
            if isinstance(component,floatingQubit) or isinstance(component,StraightBusCoupler):
                component.padToEliminate=component.pad1
                component.padToKeep=component.pad2
                k=component.padToEliminate.quantCapMatIndex
                s=component.padToKeep.quantCapMatIndex
                O_c=zeros(dimPreGEQuant,dimPreGEQuant)
                for i in range(dimPreGEQuant):
                    for j in range(dimPreGEQuant):
                        if i==s and j==s:
                            O_c[i,j]=-1
                        elif i==j:
                            O_c[i,j]=1
                        elif (i==s and j==k) or (i==k and j==s):
                            O_c[i,j]=1
                        else:
                            O_c[i,j]=0
                O_e=zeros(dimPreGEQuant,dimPreGEQuant)
                for i in range(dimPreGEQuant):
                    for j in range(dimPreGEQuant):
                        if i==s and j==s:
                            O_e[i,j]=-1
                        elif i==k and j==s:
                            O_e[i,j]=1
                        elif i==j and i!=s:
                            O_e[i,j]=1
                        else:
                            O_e[i,j]=0
                capMatPrime=O_e*capMat_GE*O_c**-1
                O_GE=zeros(dimPreGEQuant,dimPreGEQuant)
                for i in range(dimPreGEQuant):
                    for j in range(dimPreGEQuant):
                        if i==j:
                            O_GE[i,j]=1
                        elif j==k and i!=k:
                            O_GE[i,j]=-capMatPrime[i,j]/capMatPrime[j,j]
                        else:
                            O_GE[i,j]=0
                capMat_GE=O_GE*capMatPrime
                RHS=O_e*RHS
                phiMat=O_c*phiMat
        dimGE=len(self.postGEComponentList)
        #Here we go through and remove the kth rows and columns by adding the non-k elements to a new matrix, first by column then by row. 
        kList=[]
        for component in self.postGEComponentList:
            if isinstance(component,floatingQubit) or isinstance(component,StraightBusCoupler):
                kList.append(component.padToEliminate.quantCapMatIndex)#By nature of how we performed GE it's the qubit pad1 that gets eliminated, but the resulting pad is not really "pad2" anymore, it's just the single qubit pad. 
        kListReverse=[i for i in kList]
        kListReverse.sort(reverse=True)
        
        colMatIter=0
        colMat=zeros(dimPreGEQuant,dimGE)
        for i in range(dimPreGEQuant):
            if i not in kList:
                colMat[:,colMatIter]=capMat_GE[:,i]
                colMatIter+=1
        RHSReduced=zeros(dimGE,1)
        phiMatReduced=zeros(dimGE,1)
        rowMatIter=0
        rowMat=zeros(dimGE,dimGE)
        for i in range(dimPreGEQuant):
            if i not in kList:
                rowMat[rowMatIter,:]=colMat[i,:]
                RHSReduced[rowMatIter,0]=RHS[i,0]
                phiMatReduced[rowMatIter,0]=phiMat[i,0]
                rowMatIter+=1
        capMat_GE_Reduced=rowMat
        #We now perform a change-of-variables (COV) and take phi1-phi2 to be our new phi1, etc.
        #RHS_COV=RHSReduced
        #for component in self.postGEComponentList:
        #    if isinstance(component,floatingQubit) or isinstance(component,StraightBusCoupler):
        #        RHS_COV=RHS_COV.subs(component.pad1.phiSym-component.pad2.phiSym,component.Phi)
        
        return capMat_GE_Reduced,phiMatReduced,RHSReduced
    def deleteFile(self,fileName):
        if self.sysParams["Compute Location"]=="Windows":
            subprocess.call("del "+fileName+" 2>nul",shell=True)
        elif self.sysParams["Compute Location"]=="Cluster":
            subprocess.call("rm -f "+fileName,shell=True)
    def deleteFolder(self,fileName):
        if os.path.exists(fileName):
            if self.sysParams["Compute Location"]=="Windows":
                subprocess.call("rmdir "+fileName+" /s /q",shell=True)
            elif self.sysParams["Compute Location"]=="Cluster":
                subprocess.call("rm -r "+fileName,shell=True)
    def stateList(self,excitationList):#Excitation list is of the form [[i,n],[j,m],...] where i,j are component indices, and m,n are the excitations.
        numComponents=len(self.HComponentOrder)
        s=[0]*numComponents
        for i in excitationList:
            s[i[0]]=i[1]
        return s
    def HEval(self,stateList):#Find the eigenvalue corresponding to the undressed energy. Only valid if the dressed states are close to the undressed states!
        diagonalComp=[]
        for index,state in enumerate(self.HStateOrder):
            diagonalComp.append([state,self.H[index,index]])#Pairs each state up with its diagonal element.
        diagonalCompSorted=sorted(diagonalComp,key=lambda l:l[1])#Sorts so diagonal elements are in ascending order.
        stateIndex=diagonalCompSorted.index([i for i in diagonalCompSorted if i[0]==stateList][0])
        return self.HEvals[stateIndex]
    def componentFromName(self,componentName):
        if componentName[0]=="Q":
            return self.allQubitsDict[int(componentName[1:])]
        elif componentName[0]=="R":
            return self.allReadoutResonatorsDict[int(componentName[1:])]
