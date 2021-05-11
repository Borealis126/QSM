import numpy as np
from sympy import symbols,MatrixSymbol
from qutip import qeye,destroy,tensor
from constants import Phi_0Const,hbarConst,eConst
from basicGeometryFunctions import nearestPoint,distancePointPoint,midpoint,segmentBoundary,vertexBoundary
from meanderFunctions import meanderNodeGen
from node import Node
from polylineFunctions import launchPadPolylines
from pointToLine import pnt2line

class JJGDS:
    def __init__(self,patchGDS,topElectrodeGDS,bottomElectrodeGDS,connectionsGDS):
        self.patchGDS=patchGDS
        self.topElectrodeGDS=topElectrodeGDS
        self.bottomElectrodeGDS=bottomElectrodeGDS
        self.connectionsGDS=connectionsGDS
class componentPad:
    def __init__(self,componentName,padIndex):
        self.index=padIndex
        self.name=componentName+"Pad"+str(self.index)
        self.node=Node(self.name)

        self.quantCapMatIndex=0#Updated in quantizeSimulation
        
        self.phiIndex=0#Updated in quantizeSimulation
        self.phiSym=symbols("Phi_"+componentName+"P"+str(self.index))
class Qubit:
    def __init__(self,index):
        self.index=index
        self.quantizeIndex=None #Assigned and used in quantizeSimulation
        self.name="Q"+str(self.index)
        
        self.pad1=componentPad(componentName=self.name,padIndex=1)
        self.pad2=componentPad(componentName=self.name,padIndex=2)
        self.padListGeom=[self.pad1,self.pad2]#Even for grounded qubits there are two pads, one is just shorted to ground. 
        self.padList=[]#These are the actually distinct pads.
        
        self.JJGDSs=[]
        self.fingers=dict()#Only used if the qubit pads have fingers
        self.generalParamsDict={"Chip":0}#Chip 1 unless flip chip overwrites. 
        self.geometryParamsDict=dict()  
        
        self.freq=0#Updated when sims results are loaded. 
        self.anharmonicity=0#Updated when sims results are loaded. 
        self.T1=0
        self.EcVal=0
        
        self.omegaSym=symbols("omega_Q"+str(self.index))
        self.omegaEffSym=symbols("omega_effQ"+str(self.index))#Used for quantization RWA 
        self.omegaEffVal=0
    def QSym(self,dim,numComponents):
        return MatrixSymbol("Q_Q"+str(self.index),dim**numComponents,dim**numComponents)
    def PhiSym(self,dim,numComponents):
        return MatrixSymbol("Phi_Q"+str(self.index),dim**numComponents,dim**numComponents)
    def QsecondQuant(self,dim,numComponents):#Returns a Qobj matrix. Already divided out hbar.
        return 1j*np.sqrt(1/(2*self.Z))*(self.aDagger(dim,numComponents)-self.a(dim,numComponents))
    def PhisecondQuant(self,dim,numComponents):#Returns a Qobj matrix. Already divided out hbar.
        return np.sqrt(1*self.Z/2)*(self.aDagger(dim,numComponents)+self.a(dim,numComponents))
    @property
    def LJ(self):
        return self.generalParamsDict["L_J(H)"]
    @property
    def L_i_fixed(self):
        return self.generalParamsDict["L_I(H)"]
    @property
    def L_i_calculated(self):
        return 1/(self.omega_i**2*eConst**2/(2*self.EcVal))
    @property
    def EJ(self):
        return (Phi_0Const/(2*np.pi))**2/self.LJ
    @property
    def omega_J(self):
        return 1/np.sqrt(self.LJ*eConst**2/(2*self.EcVal))
    @property
    def omega_i(self):
        return self.omega_J-(self.EcVal/hbarConst)/(1-self.EcVal/(hbarConst*self.omega_J))
    @property
    def Z(self):
        return self.omega_J*self.LJ
    def a(self,dim,numComponents):
        tensorState=[qeye(dim) for i in range(numComponents)]
        tensorState[self.quantizeIndex]=destroy(N=dim)
        return tensor(tensorState)
    def aDagger(self,dim,numComponents):
        return self.a(dim,numComponents).dag()
class floatingQubit(Qubit):
    def __init__(self, index):
        super().__init__(index)
        self.padList=[self.pad1,self.pad2]        
class groundedQubit(Qubit):
    def __init__(self, index):
        super().__init__(index)
        self.padList=[self.pad1]
class ControlLine:#Similar to node, except netlist name is a function of qubit index.
    def __init__(self,index):
        self.index=index
        self.name="CL"+str(self.index)
        self.generalParamsDict=dict()
        self.geometryParamsDict=dict()
        self.lineNode=Node(name=self.name+"lineNode")
        self.launchPadNodeDict=dict()
    def pathLengthFromStartToPoint(self,point):
        leftLine=self.lineNode.polyline[0:int(len(self.lineNode.polyline)/2)]
        rightLine=self.lineNode.polyline[int(len(self.lineNode.polyline)/2):]
        rightLine.reverse()
        cumulativeLength=0
        nearestApproachPointToLine=distancePointPoint(point,midpoint(leftLine[0],rightLine[0]))
        pathLengthToNearestApproachPointToLine=0
        for i in range(1,len(leftLine)):
            nearestApproachPointToSegment,pointOfNearestApproach=pnt2line(point+[0],midpoint(leftLine[i-1],rightLine[i-1])+[0],midpoint(leftLine[i],rightLine[i])+[0])
            if nearestApproachPointToSegment<nearestApproachPointToLine:
                pathLengthToNearestApproachPointToLine=cumulativeLength+distancePointPoint(midpoint(leftLine[i-1],rightLine[i-1]),pointOfNearestApproach)
                nearestApproachPointToLine=nearestApproachPointToSegment
            cumulativeLength+=distancePointPoint(midpoint(leftLine[i-1],rightLine[i-1]),midpoint(leftLine[i],rightLine[i]))
        return pathLengthToNearestApproachPointToLine
    def pathLengthFromEndToPoint(self,point):
        leftLine=self.lineNode.polyline[0:int(len(self.lineNode.polyline)/2)]
        leftLine.reverse()
        rightLine=self.lineNode.polyline[int(len(self.lineNode.polyline)/2):]
        cumulativeLength=0
        nearestApproachPointToLine=distancePointPoint(point,midpoint(leftLine[0],rightLine[0]))
        pathLengthToNearestApproachPointToLine=0
        for i in range(1,len(leftLine)):
            nearestApproachPointToSegment,pointOfNearestApproach=pnt2line(point+[0],midpoint(leftLine[i-1],rightLine[i-1])+[0],midpoint(leftLine[i],rightLine[i])+[0])
            if nearestApproachPointToSegment<nearestApproachPointToLine:
                pathLengthToNearestApproachPointToLine=cumulativeLength+distancePointPoint(midpoint(leftLine[i-1],rightLine[i-1]),pointOfNearestApproach)
                nearestApproachPointToLine=nearestApproachPointToSegment
            cumulativeLength+=distancePointPoint(midpoint(leftLine[i-1],rightLine[i-1]),midpoint(leftLine[i],rightLine[i]))
        return pathLengthToNearestApproachPointToLine
    def pathLengthPointToPoint(self,point1,point2):
        return np.abs(self.pathLengthFromStartToPoint(point2)-self.pathLengthFromStartToPoint(point1))   
    def updateLaunchPadNodes(self):
        startPoint=[self.lineNode.polylineShapeParams["Start X"],self.lineNode.polylineShapeParams["Start Y"]]
        startAngle=self.lineNode.polylineShapeParams["Start Angle"]
        endPoint=self.lineNode.endPoint 
        endAngle=self.lineNode.endAngle
        if self.generalParamsDict["Type"]=="fluxBias" or self.generalParamsDict["Type"]=="feedline" or self.generalParamsDict["Type"]=="drive":
            launchPad1,launchPadPeriphery1,launchPadMeshPeriphery1=launchPadPolylines(startPoint,startAngle,self.lineNode.polylineShapeParams["CPW"],self.lineNode.polylineShapeParams["Mesh Boundary"])
            launchPad1Node=Node(name=self.name+"launchPad1Node")
            launchPad1Node.polyline=launchPad1
            launchPad1Node.peripheryPolylines.append(launchPadPeriphery1)
            launchPad1Node.meshPeripheryPolylines.append(launchPadMeshPeriphery1)
            launchPad1Node.Z=self.lineNode.Z
            launchPad1Node.height=self.lineNode.height
            self.launchPadNodeDict[launchPad1Node.name]=launchPad1Node
        if self.generalParamsDict["Type"]=="feedline":
            launchPad2,launchPadPeriphery2,launchPadMeshPeriphery2=launchPadPolylines(endPoint,endAngle+np.pi,self.lineNode.polylineShapeParams["CPW"],self.lineNode.polylineShapeParams["Mesh Boundary"])#+pi is so the launch pad is facing the right way. 
            launchPad2Node=Node(name=self.name+"launchPad2Node")
            launchPad2Node.polyline=launchPad2
            launchPad2Node.peripheryPolylines.append(launchPadPeriphery2)
            launchPad2Node.meshPeripheryPolylines.append(launchPadMeshPeriphery2)
            launchPad2Node.Z=self.lineNode.Z
            launchPad2Node.height=self.lineNode.height
            self.launchPadNodeDict[launchPad2Node.name]=launchPad2Node
class CPWResonator:
    def __init__(self,index):
        self.index=index
        self.quantizeIndex=0 #Assigned and used in quantizeSimulation
        self.name="R"+str(self.index)
        
        self.pad1=componentPad(componentName=self.name,padIndex=1)
        self.pad2=componentPad(componentName=self.name,padIndex=2)#Only pad 2 should be used in quantization.

        self.meanderNode=dict()
        self.meanderStartPoint=[]
        self.meanderStartAngle=0
        self.meanderEndPoint=[]
        self.meanderEndAngle=0
        
        self.generalParamsDict={"Chip":0}#Chip 1 unless flip chip overwrites. 
        self.geometryParamsDict=dict()
        
        self.omegaSym=symbols("omega_R"+str(self.index))
        self.omegaEffSym=symbols("omega_effR"+str(self.index))
        self.LSym=symbols("L_R"+str(self.index))
        self.omegaEffVal=0
        self.omegaVal=0
        self.equivL=0
        self.equivC=0
        
        self.EcVal=0
    def QSym(self,dim,numComponents):
        return MatrixSymbol("Q_R"+str(self.index),dim**numComponents,dim**numComponents)
    def PhiSym(self,dim,numComponents):
        return MatrixSymbol("Phi_R"+str(self.index),dim**numComponents,dim**numComponents)
    @property
    def omega(self):
        return 1/np.sqrt(self.equivL*eConst**2/(2*self.EcVal))
    def QsecondQuant(self,dim,numComponents):#Returns a Qobj matrix. Already divided out hbar.
        return 1j*np.sqrt(1/(2*self.Z))*(self.aDagger(dim,numComponents)-self.a(dim,numComponents))
    def PhisecondQuant(self,dim,numComponents):#Returns a Qobj matrix. Already divided out hbar.
        return np.sqrt(1*self.Z/2)*(self.aDagger(dim,numComponents)+self.a(dim,numComponents))
    def updateMeanderNode(self,CPW): 
        endAngles=[self.geometryParamsDict["Pad 1 Curve Angle"],self.geometryParamsDict["Pad 2 Curve Angle"]]
        self.meanderNode,\
        self.meanderStartPoint,self.meanderStartAngle,\
        self.meanderEndPoint,self.meanderEndAngle=meanderNodeGen(name=self.name+"Meander",
                                                                 turnRadius=self.geometryParamsDict["Meander Turn Radius"],\
                                                                 length=self.geometryParamsDict["Length"]-self.geometryParamsDict["Pad 1 Length"]-self.geometryParamsDict["Pad 2 Length"]-2*self.geometryParamsDict["Pad T Stem Length"],\
                                                                 endSeparation=self.geometryParamsDict["Pad Separation"]-self.geometryParamsDict["Pad 1 Length"]/2-self.geometryParamsDict["Pad 2 Length"]/2-2*self.geometryParamsDict["Pad T Stem Length"],\
                                                                 meanderToEndMinDist=self.geometryParamsDict["Meander To Pad Minimum Distance"],\
                                                                 endAngles=endAngles,\
                                                                 angle=self.geometryParamsDict["Angle"],\
                                                                 centerX=self.geometryParamsDict["Center X"],\
                                                                 centerY=self.geometryParamsDict["Center Y"],\
                                                                 height=self.geometryParamsDict["Pad 1 Height"],\
                                                                 Z=self.pad1.node.Z,\
                                                                 meshBoundary=self.pad1.node.polylineShapeParams["Mesh Boundary"],\
                                                                 CPWObj=CPW)
    def bareFreq(self,CPW):
        return CPW.vp()/(2*self.length)  
    @property
    def Z(self):
        return self.omega*self.equivL
    def a(self,dim,numComponents):
        tensorState=[qeye(dim) for i in range(numComponents)]
        tensorState[self.quantizeIndex]=destroy(N=dim)
        return tensor(tensorState)
    def aDagger(self,dim,numComponents):
        return self.a(dim,numComponents).dag()
class ReadoutResonator(CPWResonator):
    def __init__(self, index):
        super().__init__(index)
class ResonatorBusCoupler(CPWResonator):
    def __init__(self, index):
        super().__init__(index)
class StraightBusCoupler:
    def __init__(self,index):
        self.index=index
        self.quantizeIndex=None #Assigned and used in quantizeSimulation
        self.name="bC"+str(self.index)
        
        self.pad1=componentPad(componentName=self.name,padIndex=1)
        self.pad2=componentPad(componentName=self.name,padIndex=2)
        self.padListGeom=[self.pad1,self.pad2]#Even for grounded qubits there are two pads, one is just shorted to ground. 
        self.padList=[]#These are the actually distinct pads.
        
        self.JJGDSs=[]
        self.fingers=dict()#Only used if the qubit pads have fingers
        self.generalParamsDict={"Chip":0}#Chip 1 unless flip chip overwrites. 
        self.geometryParamsDict=dict()  
        
        self.freq=0#Updated when sims results are loaded. 
        self.anharmonicity=0#Updated when sims results are loaded. 
        self.T1=0
        self.EcVal=0
        
        self.omegaSym=symbols("omega_bC"+str(self.index))
        self.omegaEffSym=symbols("omega_effbC"+str(self.index))#Used for quantization RWA 
        self.omegaEffVal=0
    def QSym(self,dim,numComponents):
        return MatrixSymbol("Q_bC"+str(self.index),dim**numComponents,dim**numComponents)
    def PhiSym(self,dim,numComponents):
        return MatrixSymbol("Phi_bC"+str(self.index),dim**numComponents,dim**numComponents)
    def QsecondQuant(self,dim,numComponents):#Returns a Qobj matrix. Already divided out hbar.
        return 1j*np.sqrt(1/(2*self.Z))*(self.aDagger(dim,numComponents)-self.a(dim,numComponents))
    def PhisecondQuant(self,dim,numComponents):#Returns a Qobj matrix. Already divided out hbar.
        return np.sqrt(1*self.Z/2)*(self.aDagger(dim,numComponents)+self.a(dim,numComponents))
    @property
    def LJ(self):
        return self.generalParamsDict["L_J(H)"]
    @property
    def L_i_fixed(self):
        return self.generalParamsDict["L_I(H)"]
    @property
    def L_i_calculated(self):
        return 1/(self.omega_i**2*eConst**2/(2*self.EcVal))
    @property
    def EJ(self):
        return (Phi_0Const/(2*np.pi))**2/self.LJ
    @property
    def omega_J(self):
        return 1/np.sqrt(self.LJ*eConst**2/(2*self.EcVal))
    @property
    def omega_i(self):
        return self.omega_J-(self.EcVal/hbarConst)/(1-self.EcVal/(hbarConst*self.omega_J))
    @property
    def Z(self):
        return self.omega_J*self.LJ
    def a(self,dim,numComponents):
        tensorState=[qeye(dim) for i in range(numComponents)]
        tensorState[self.quantizeIndex]=destroy(N=dim)
        return tensor(tensorState)
    def aDagger(self,dim,numComponents):
        return self.a(dim,numComponents).dag()
class PTCClass:
    def __init__(self,index):
        self.index=index
        self.quantizeIndex=None #Assigned and used in quantizeSimulation
        self.name="PTC"+str(self.index)
        
        self.pad1=componentPad(componentName=self.name,padIndex=1)
        self.pad2=componentPad(componentName=self.name,padIndex=2)
        self.padListGeom=[self.pad1,self.pad2]#Even for grounded qubits there are two pads, one is just shorted to ground. 
        self.padList=[]#These are the actually distinct pads.
        
        self.JJGDSs=[]
        self.fingers=dict()#Only used if the qubit pads have fingers
        self.generalParamsDict={"Chip":0}#Chip 1 unless flip chip overwrites. 
        self.geometryParamsDict=dict()  
        
        self.freq=0#Updated when sims results are loaded. 
        self.anharmonicity=0#Updated when sims results are loaded. 
        self.T1=0
        self.EcVal=0
        
        self.omegaSym=symbols("omega_PTC"+str(self.index))
        self.omegaEffSym=symbols("omega_effPTC"+str(self.index))#Used for quantization RWA 
        self.omegaEffVal=0
    def updateMeanderNode(self,CPW): 
        self.meanderNode,\
        self.meanderStartPoint,self.meanderStartAngle,\
        self.meanderEndPoint,self.meanderEndAngle=meanderNodeGen(name=self.name+"Meander",
                                                              turnRadius=self.geometryParamsDict["Meander Turn Radius"],\
                                                              length=self.geometryParamsDict["Length"],\
                                                              endSeparation=self.geometryParamsDict["End Separation"],\
                                                              meanderToEndMinDist=self.geometryParamsDict["Meander To End Minimum Distance"],\
                                                              endAngles=[0,0],\
                                                              angle=self.geometryParamsDict["Angle"],\
                                                              centerX=self.geometryParamsDict["Center X"],\
                                                              centerY=self.geometryParamsDict["Center Y"],\
                                                              height=self.pad1.node.height,\
                                                              Z=self.pad1.node.Z,\
                                                              meshBoundary=self.pad1.node.polylineShapeParams["Mesh Boundary"],\
                                                              CPWObj=CPW)
    @property
    def TD(self):
        return self.geometryParamsDict["Length"]/self.generalParamsDict["Phase Velocity (um/s)"]
class CPW:
    def __init__(self):
        self.generalParamsDict=dict()#Contains "Phase Velocity(um/s)"
        self.geometryParamsDict=dict()#Overwritten in loadGeometries
        self.vp=0
    def TD(self,length):
        return length/self.vp
class Substrate:
    def __init__(self,index):
        self.index=index
        self.name="S"+str(self.index)
        self.node=Node(name=self.name)
        self.node.color="(143 175 143)"
        self.geometryParamsDict=dict()
class Ground:
    def __init__(self,index):
        self.index=index
        self.name="G"+str(self.index)
        self.outlineNode=Node(name=self.name)#The polyline of this node is the outer outine of the ground.
        self.contourHolePolylines=[]
    def calculateContourHoles(self,nodes,resolution):#Not a function of height, so same for Q2D/Q3D. 
        peripheryContourNodeList=[]
        for thisNode in nodes:
            thisNodeContourPointsUnordered=[]
            for nodeVertex in thisNode.polyline:
                vertexBoundaryList=vertexBoundary(vertex=nodeVertex,\
                                                  boundary=thisNode.boundary,\
                                                  resolution=resolution)#The list of all points a distance "boundary" away from that particular vertex. 
                for candidateGroundPoint in vertexBoundaryList:
                    if keepCandidateGroundPointOrNot(candidateGroundPoint,node)==False:
                        updatedList=[x for x in vertexBoundaryList if x!=candidateGroundPoint]#Remove from list. 
                        vertexBoundaryList=updatedList
                thisNodeContourPointsUnordered=thisNodeContourPointsUnordered+vertexBoundaryList
            for nodeSegment in thisNode.segmentList:
                segmentBoundaryList=segmentBoundary(segment=nodeSegment,\
                                                    boundary=thisNode.boundary,\
                                                    resolution=resolution)
                for candidateGroundPoint in segmentBoundaryList:
                    if keepCandidateGroundPointOrNot(candidateGroundPoint,node)==False:
                        updatedList=[x for x in segmentBoundaryList if x!=candidateGroundPoint]
                        segmentBoundaryList=updatedList
                thisNodeContourPointsUnordered=thisNodeContourPointsUnordered+segmentBoundaryList
            #We now have a list of all periphery points for this node. Now we start at the beginning of the list and sequentially find the next 
            #nearest point in the list.Once we get back to the original point, we are done. 
            thisNodeContourPointsOrdered=[] #Making a copy to remove elements from as we form the contours. 

            startPoint=thisNodeContourPointsUnordered[0]#This will be a new point with each new contour hole. 
            thisNodeContourPointsOrdered=[startPoint]
            
            secondPoint=nearestPoint(point=startPoint,pointList=thisNodeContourPointsUnordered[1:])#Second and third point are just to get it running, so that it doesn't jump back to the other side fo the contour. Also resolution-dependent. 
            thisNodeContourPointsUnordered.remove(secondPoint)
            thisNodeContourPointsOrdered.append(secondPoint)
            
            thirdPoint=nearestPoint(point=secondPoint,pointList=thisNodeContourPointsUnordered[1:])
            thisNodeContourPointsUnordered.remove(thirdPoint)
            thisNodeContourPointsOrdered.append(thirdPoint)
        
            nextPoint=nearestPoint(point=thirdPoint,pointList=thisNodeContourPointsUnordered[1:])
            while thisNodeContourPointsUnordered!=[]:
                currentPoint=nextPoint
                thisNodeContourPointsUnordered.remove(currentPoint)
                thisNodeContourPointsOrdered.append(currentPoint)
                nextPoint=nearestPoint(point=currentPoint,pointList=thisNodeContourPointsUnordered)#No [1:] since we have now reintroduced startpoint as an option
            
            contourNode=node(name="contour"+thisNode.name)
            contourNode.polyline=thisNodeContourPointsOrdered
            contourNode.Z=self.outlineNode.Z
            peripheryContourNodeList.append(contourNode)
            
        self.contourHoleNodes=peripheryContourNodeList     
class Chip:
    def __init__(self,index):
        self.index=index
        self.substrate=Substrate(index=self.index)
        self.ground=Ground(index=self.index)
        self.qubitDict=dict()
        self.readoutResonatorDict=dict()
        self.PTCDict=dict()
        self.straightBusCouplerDict=dict()
        self.controlLineDict=dict()
class Bump:
    underBumpBottomNode=dict()
    underBumpTopNode=dict()
    metalBottomNode=dict()
    metalTopNode=dict() 