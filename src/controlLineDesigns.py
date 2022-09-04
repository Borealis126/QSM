from abc import ABC, abstractmethod
from .node import Node
import numpy as np
from .meander import meanderNodeGen
from .polyline import launchPadPolylines
from .pointToLine import pnt2line
from .meander import meanderNodeGen
from .basicGeometry import nearestPoint, distancePointPoint, midpoint, segmentBoundary, vertexBoundary


class ControlLineDesign(ABC):

    @abstractmethod
    def updateNodes(self):
        ...

    def __init__(self, name, params):
        self.name = name
        self.paramsDict = dict({i: None for i in params})
        self.paramsDict["Mesh Boundary"] = 0
        self.paramsDict["Z"] = 0  # Based on the substrate height
        self.CPW = None
        self.lineNode = Node(self.name + "lineNode", 'Path')
        self.launchPadNodeDict = dict()

    @property
    def promptedParams(self):
        return {i: self.paramsDict[i] for i in self.paramsDict if i != "Mesh Boundary" and i != "Z"}

    @property
    def lineType(self):
        return self.componentParams["Type"]

    def pathLengthFromStartToPoint(self, point):
        leftLine = self.lineNode.polyline[0:int(len(self.lineNode.polyline) / 2)]
        rightLine = self.lineNode.polyline[int(len(self.lineNode.polyline) / 2):]
        rightLine = np.flip(rightLine)
        cumulativeLength = 0
        nearestApproachPointToLine = distancePointPoint(point, midpoint(leftLine[0], rightLine[0]))
        pathLengthToNearestApproachPointToLine = 0
        for i in range(1, len(leftLine)):
            nearestApproachPointToSegment, pointOfNearestApproach = pnt2line(
                point + [0],
                midpoint(leftLine[i - 1], rightLine[i - 1]) + [0],
                midpoint(leftLine[i], rightLine[i]) + [0]
            )
            if nearestApproachPointToSegment < nearestApproachPointToLine:
                pathLengthToNearestApproachPointToLine = cumulativeLength + distancePointPoint(
                    midpoint(leftLine[i - 1], rightLine[i - 1]), pointOfNearestApproach)
                nearestApproachPointToLine = nearestApproachPointToSegment
            cumulativeLength += distancePointPoint(midpoint(leftLine[i - 1], rightLine[i - 1]),
                                                   midpoint(leftLine[i], rightLine[i]))
        return pathLengthToNearestApproachPointToLine

    def pathLengthFromEndToPoint(self, point):
        leftLine = self.lineNode.polyline[0:int(len(self.lineNode.polyline) / 2)]
        leftLine = np.flip(leftLine)
        rightLine = self.lineNode.polyline[int(len(self.lineNode.polyline) / 2):]
        cumulativeLength = 0
        nearestApproachPointToLine = distancePointPoint(point, midpoint(leftLine[0], rightLine[0]))
        pathLengthToNearestApproachPointToLine = 0
        for i in range(1, len(leftLine)):
            nearestApproachPointToSegment, pointOfNearestApproach = pnt2line(
                point + [0],
                midpoint(leftLine[i - 1], rightLine[i - 1]) + [0],
                midpoint(leftLine[i], rightLine[i]) + [0]
            )
            if nearestApproachPointToSegment < nearestApproachPointToLine:
                pathLengthToNearestApproachPointToLine = cumulativeLength + distancePointPoint(
                    midpoint(leftLine[i - 1], rightLine[i - 1]), pointOfNearestApproach)
                nearestApproachPointToLine = nearestApproachPointToSegment
            cumulativeLength += distancePointPoint(midpoint(leftLine[i - 1], rightLine[i - 1]),
                                                   midpoint(leftLine[i], rightLine[i]))
        return pathLengthToNearestApproachPointToLine

    def pathLengthPointToPoint(self, point1, point2):
        return np.abs(self.pathLengthFromStartToPoint(point2) - self.pathLengthFromStartToPoint(point1))


class FeedLine(ControlLineDesign):
    def __init__(self, name):
        params = ["Start X", "Start Y", "Start Angle", "Section Code", "Material", "Mesh Boundary", "Z"]
        super().__init__(name, params)

    def updateNodes(self):
        self.updateLineNode()
        self.updateLaunchPadNodes()

    def updateLineNode(self):
        self.lineNode.shape.paramsDict["Width"] = self.CPW.geometryParams["Width"]
        self.lineNode.shape.paramsDict["Gap"] = self.CPW.geometryParams["Gap"]
        self.lineNode.shape.paramsDict['Height'] = self.CPW.geometryParams["Height"]
        self.lineNode.shape.paramsDict["SectionCode"] = self.paramsDict["Section Code"]
        self.lineNode.shape.paramsDict["Mesh Boundary"] = self.paramsDict["Mesh Boundary"]

        # It's actually the start not the center, but the math is the same.
        self.lineNode.centerX = self.paramsDict['Start X']
        self.lineNode.centerY = self.paramsDict['Start Y']
        self.lineNode.angle = self.paramsDict['Start Angle']
        self.lineNode.Z = self.paramsDict["Z"]
        self.lineNode.orientShape()

    def updateLaunchPadNodes(self):
        launchPad1Node = Node(self.name + "launchPad1Node", "LaunchPad")
        launchPad1Node.shape.paramsDict["CPW"] = self.CPW
        launchPad1Node.shape.paramsDict["MeshBoundary"] = self.paramsDict['Mesh Boundary']
        launchPad1Node.shape.paramsDict["Height"] = self.CPW.geometryParams["Height"]
        launchPad1Node.centerX, launchPad1Node.centerY = [self.paramsDict["Start X"], self.paramsDict["Start Y"]]
        launchPad1Node.angle = self.paramsDict["Start Angle"]
        launchPad1Node.Z = self.paramsDict['Z']
        launchPad1Node.orientShape()

        launchPad2Node = Node(self.name + "launchPad2Node", "LaunchPad")
        launchPad2Node.shape.paramsDict["CPW"] = self.CPW
        launchPad2Node.shape.paramsDict["MeshBoundary"] = self.paramsDict['Mesh Boundary']
        launchPad2Node.shape.paramsDict["Height"] = self.CPW.geometryParams["Height"]
        launchPad2Node.centerX, launchPad2Node.centerY = self.lineNode.shape.orientEndPoint(self.paramsDict["Start X"],
                                                                                            self.paramsDict["Start Y"],
                                                                                            self.paramsDict['Start Angle'])
        launchPad2Node.angle = self.lineNode.shape.endAngle + self.paramsDict['Start Angle']+np.pi
        launchPad2Node.Z = self.paramsDict['Z']
        launchPad2Node.orientShape()

        self.launchPadNodeDict[launchPad1Node.name] = launchPad1Node
        self.launchPadNodeDict[launchPad2Node.name] = launchPad2Node


class DriveLine(ControlLineDesign):

    def __init__(self, name):
        params = ["Length", "Angle", "Center X", "Center Y", "Pad Separation", "Meander Turn Radius",
                  "Pad T Stem Length", "Meander To Pad Minimum Distance"]
        super().__init__(name, params)

    def updateNodes(self):
        CPW_obj = self.CPW
        endAngles = [self.paramsDict["Pad 1 Curve Angle"], self.paramsDict["Pad 2 Curve Angle"]]
        self.meanderNode, meanderStartPoint, meanderStartAngle, meanderEndPoint, meanderEndAngle = \
            meanderNodeGen(
                name=self.name + "Meander",
                turnRadius=self.paramsDict["Meander Turn Radius"],
                length=(self.paramsDict["Length"] -
                        self.paramsDict["Pad 1 Length"] -
                        self.paramsDict["Pad 2 Length"] - 2 *
                        self.paramsDict["Pad T Stem Length"]),
                endSeparation=(self.paramsDict["Pad Separation"]
                               - self.paramsDict["Pad 1 Length"] / 2
                               - self.paramsDict["Pad 2 Length"] / 2
                               - 2 * self.paramsDict["Pad T Stem Length"]),
                meanderToEndMinDist=self.paramsDict["Meander To Pad Minimum Distance"],
                endAngles=endAngles,
                angle=self.paramsDict["Angle"],
                centerX=self.paramsDict["Center X"],
                centerY=self.paramsDict["Center Y"],
                height=self.paramsDict["Pad 1 Height"],
                Z=self.pad1.node.Z,
                meshBoundary=self.paramsDict["Mesh Boundary"],
                CPWObj=CPW_obj
            )


class FluxBiasLine(ControlLineDesign):

    def __init__(self, name):
        params = ["Length", "Angle", "Center X", "Center Y", "Pad Separation", "Meander Turn Radius",
                  "Pad T Stem Length", "Meander To Pad Minimum Distance"]
        super().__init__(name, params)

    def updateNodes(self):
        CPW_obj = self.CPW
        endAngles = [self.paramsDict["Pad 1 Curve Angle"], self.paramsDict["Pad 2 Curve Angle"]]
        self.meanderNode, meanderStartPoint, meanderStartAngle, meanderEndPoint, meanderEndAngle = \
            meanderNodeGen(
                name=self.name + "Meander",
                turnRadius=self.paramsDict["Meander Turn Radius"],
                length=(self.paramsDict["Length"] -
                        self.paramsDict["Pad 1 Length"] -
                        self.paramsDict["Pad 2 Length"] - 2 *
                        self.paramsDict["Pad T Stem Length"]),
                endSeparation=(self.paramsDict["Pad Separation"]
                               - self.paramsDict["Pad 1 Length"] / 2
                               - self.paramsDict["Pad 2 Length"] / 2
                               - 2 * self.paramsDict["Pad T Stem Length"]),
                meanderToEndMinDist=self.paramsDict["Meander To Pad Minimum Distance"],
                endAngles=endAngles,
                angle=self.paramsDict["Angle"],
                centerX=self.paramsDict["Center X"],
                centerY=self.paramsDict["Center Y"],
                height=self.paramsDict["Pad 1 Height"],
                Z=self.pad1.node.Z,
                meshBoundary=self.paramsDict["Mesh Boundary"],
                CPWObj=CPW_obj
            )


def interpretDesign(designName):
    if designName == 'FeedLine':
        return FeedLine
    elif designName == 'DriveLine':
        return DriveLine
    elif designName == 'FluxBiasLine':
        return FluxBiasLine
