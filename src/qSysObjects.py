import numpy as np
from sympy import symbols
from constants import Phi_0Const, hbarConst, eConst
from basicGeometry import nearestPoint, distancePointPoint, midpoint, segmentBoundary, vertexBoundary
from meander import meanderNodeGen
from node import Node
from polyline import launchPadPolylines
from pointToLine import pnt2line
import qubitDesigns
import resonatorDesigns
import controlLineDesigns


class Qubit:
    def __init__(self, index, componentParams):
        self.index = index
        self.name = "Q" + str(self.index)
        self.design = qubitDesigns.interpretDesign(componentParams['Type'])(self.name)
        self.componentParams = componentParams

        self.omegaSym = symbols("omega_Q" + str(self.index))
        self.omegaEffSym = symbols("omega_effQ" + str(self.index))  # Used for quantization RWA
        self.omegaEffVal = 0

    @property
    def L_i_fixed(self):
        return self.componentParams["L_I(H)"]

    @property
    def LJ(self):
        return self.componentParams["L_J(H)"]

    @property
    def EJ(self):
        return (Phi_0Const / (2 * np.pi)) ** 2 / self.LJ

    def omega_J(self, EC):
        return 1 / np.sqrt(self.LJ * eConst ** 2 / (2 * EC))

    def omega_i(self, EC):
        return self.omega_J(EC) - (EC / hbarConst) / (1 - EC / (hbarConst * self.omega_J(EC)))

    def Z(self, EC):
        return self.omega_J(EC) * self.LJ


class ControlLine:  # Similar to node, except netlist name is a function of qubit index.
    def __init__(self, index, componentParams):
        self.index = index
        self.componentParams = componentParams
        self.name = "CL" + str(self.index)
        self.design = controlLineDesigns.interpretDesign(componentParams['Type'])(self.name)


class CPWResonator:
    def __init__(self, index, componentParams):
        self.index = index
        self.componentParams = componentParams
        self.name = "R" + str(self.index)
        self.design = resonatorDesigns.interpretDesign(componentParams['Type'])(self.name)

        self.omegaSym = symbols("omega_R" + str(self.index))
        self.omegaEffSym = symbols("omega_effR" + str(self.index))
        self.LSym = symbols("L_R" + str(self.index))
        self.omegaEffVal = 0
        self.omegaVal = 0

    def omega(self, equivL, EC):
        return 1 / np.sqrt(equivL * eConst ** 2 / (2 * EC))

    def bareFreq(self, CPW_obj):
        return CPW_obj.vp() / (2 * self.length)

    def Z(self, equivL, EC):
        return self.omega(equivL, EC) * equivL


class ReadoutResonator(CPWResonator):
    def __init__(self, index, componentParams):
        super().__init__(index,componentParams)

    @property
    def capacitanceToFeedline(self):
        return self.componentParams["Capacitance to Feedline (F)"]

    @property
    def feedlineCapacitanceToGround(self):
        return self.componentParams["Feedline Pad Capacitance to Ground (F)"]


class CPW:
    def __init__(self):
        self.componentParams = dict()  # Contains "Phase Velocity(um/s)"
        self.geometryParams = dict()  # Overwritten in loadGeometries
        self.vp = 0

    def TD(self, length):
        return length / self.vp


class Substrate:
    def __init__(self, index):
        self.index = index
        self.name = "S" + str(self.index)
        self.node = Node(self.name, "Rectangle")
        self.node.color = "(143 175 143)"
        self.geometryParams = dict()


class Ground:
    def __init__(self, index):
        self.index = index
        self.name = "G" + str(self.index)
        self.outlineNode = Node(self.name, "Rectangle")  # The polyline of this node is the outer outine of the ground.
        self.contourHolePolylines = []
        self.contourHoleNodes = []

    def calculateContourHoles(self, nodes, resolution):  # Not a function of height, so same for Q2D/Q3D.
        peripheryContourNodeList = []
        for thisNode in nodes:
            thisNodeContourPointsUnordered = []
            for nodeVertex in thisNode.polyline:
                vertexBoundaryList = vertexBoundary(
                    vertex=nodeVertex,
                    boundary=thisNode.boundary,
                    resolution=resolution
                )  # The list of all points a distance "boundary" away from that particular vertex.
                for candidateGroundPoint in vertexBoundaryList:
                    if not keepCandidateGroundPointOrNot(candidateGroundPoint, node):
                        updatedList = [x for x in vertexBoundaryList if x != candidateGroundPoint]  # Remove from list.
                        vertexBoundaryList = updatedList
                thisNodeContourPointsUnordered = thisNodeContourPointsUnordered + vertexBoundaryList
            for nodeSegment in thisNode.segmentList:
                segmentBoundaryList = segmentBoundary(segment=nodeSegment,
                                                      boundary=thisNode.boundary,
                                                      resolution=resolution)
                for candidateGroundPoint in segmentBoundaryList:
                    if not keepCandidateGroundPointOrNot(candidateGroundPoint, node):
                        updatedList = [x for x in segmentBoundaryList if x != candidateGroundPoint]
                        segmentBoundaryList = updatedList
                thisNodeContourPointsUnordered = thisNodeContourPointsUnordered + segmentBoundaryList
            """We now have a list of all periphery points for this node. Now we start at the beginning of the list 
            and sequentially find the next nearest point in the list.
            Once we get back to the original point, we are done"""
            # thisNodeContourPointsOrdered = [] # Making a copy to remove elements from as we form the contours.

            startPoint = thisNodeContourPointsUnordered[0]  # This will be a new point with each new contour hole.
            thisNodeContourPointsOrdered = [startPoint]

            """Second and third point are just to get it running, so that it doesn't jump back 
            to the other side fo the contour. Also resolution-dependent."""
            secondPoint = nearestPoint(point=startPoint, pointList=thisNodeContourPointsUnordered[1:])
            thisNodeContourPointsUnordered.remove(secondPoint)
            thisNodeContourPointsOrdered.append(secondPoint)

            thirdPoint = nearestPoint(point=secondPoint, pointList=thisNodeContourPointsUnordered[1:])
            thisNodeContourPointsUnordered.remove(thirdPoint)
            thisNodeContourPointsOrdered.append(thirdPoint)

            nextPoint = nearestPoint(point=thirdPoint, pointList=thisNodeContourPointsUnordered[1:])
            while thisNodeContourPointsUnordered:
                currentPoint = nextPoint
                thisNodeContourPointsUnordered.remove(currentPoint)
                thisNodeContourPointsOrdered.append(currentPoint)
                # No [1:] since we have now reintroduced startpoint as an option
                nextPoint = nearestPoint(point=currentPoint,
                                         pointList=thisNodeContourPointsUnordered)

            contourNode = node(name="contour" + thisNode.name)
            contourNode.polyline = thisNodeContourPointsOrdered
            contourNode.Z = self.outlineNode.Z
            peripheryContourNodeList.append(contourNode)

        self.contourHoleNodes = peripheryContourNodeList


class Chip:
    def __init__(self, index):
        self.index = index
        self.substrate = Substrate(index=self.index)
        self.ground = Ground(index=self.index)
        self.qubitDict = dict()
        self.readoutResonatorDict = dict()
        self.PTCDict = dict()
        self.straightBusCouplerDict = dict()
        self.controlLineDict = dict()


class Bump:
    underBumpBottomNode = dict()
    underBumpTopNode = dict()
    metalBottomNode = dict()
    metalTopNode = dict()
