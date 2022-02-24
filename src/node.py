from polyline import pathPolyline
from basicGeometry import rotate, translate
from constants import traceBuffer
from abc import ABC, abstractmethod
import numpy as np


# class Node:  # A Node is any 3D element.
#     def __init__(self, name):
#         self.name = name
#         self.polyline = []  # This is the polyline of the base of each node.
#         self.polylineShape = "rectangle"
#         self.polylineShapeParams = dict()
#         self.peripheryPolylines = []
#         self.meshPeripheryPolylines = []
#         self.height = 0  # Only assigned and used if Q3D.
#         self.Z = 0  # Height above X-Y plane.
#         self.material = "perfect conductor"  # Default material.
#         self.color = "(143 143 175)"  # Grey by default
#         self.endPoint = []  # Only used for paths
#         self.endAngle = []
#
#     def updatePolylines(self):  # Once polylineShapeParams is loaded update the polyline and peripheryPolyline
#         shapeParams = self.polylineShapeParams
#         if self.polylineShape[0:9] == "rectangle":  # Pre-rotation the fingers point up and JJ elements point down.
#             if "PlusFinger(s)" in self.polylineShape:  # Stems are bottom of rectangle, fingers are top.
#                 numFingers = shapeParams["Number of Fingers"]
#                 fingerSpacing = shapeParams["Finger Spacing"]
#                 # The fingers are all inserted between component[1] and component[2]
#                 componentLeft = component[0:2]
#                 componentRight = component[2:]
#                 # Fingers are indexed left to right along the top of the rectangle.
#                 for fingerIndex in range(numFingers):
#                     # First make the stem of each finger.
#                     fingerStemPolyline, fingerStemPeripheryPolyline, fingerStemMeshPeripheryPolyline = \
#                         rectanglePolylineSet(
#                             centerX=-(numFingers - 1) * fingerSpacing / 2 + fingerIndex * fingerSpacing,
#                             centerY=(shapeParams["Body Length"] / 2 +
#                                      shapeParams["Finger " + str(fingerIndex) + " Stem Length"] / 2),
#                             width=shapeParams["Finger " + str(fingerIndex) + " Stem Width"],
#                             length=shapeParams["Finger " + str(fingerIndex) + " Stem Length"],
#                             side1Boundary=shapeParams["Finger Stem Boundary"],
#                             side2Boundary=shapeParams["Finger Stem Boundary"],
#                             side3Boundary=shapeParams["Finger Stem Boundary"],
#                             side4Boundary=shapeParams["Finger Stem Boundary"],
#                             meshBoundary=shapeParams["Mesh Boundary"],
#                             angle=0
#                         )
#                     # Then make the T
#                     fingerTPolyline, fingerTPeripheryPolyline, fingerTMeshPeripheryPolyline = rectanglePolylineSet(
#                         centerX=-(numFingers - 1) * fingerSpacing / 2 + fingerIndex * fingerSpacing,
#                         centerY=(shapeParams["Body Length"] / 2
#                                  + shapeParams["Finger " + str(fingerIndex) + " Stem Length"]
#                                  + shapeParams["Finger " + str(fingerIndex) + " T Head Length"] / 2),
#                         width=shapeParams["Finger " + str(fingerIndex) + " T Width"],
#                         length=shapeParams["Finger " + str(fingerIndex) + " T Head Length"],
#                         side1Boundary=shapeParams["Finger " + str(fingerIndex) + " T Side 1 Boundary"],
#                         side2Boundary=shapeParams["Finger " + str(fingerIndex) + " T Side 2 Boundary"],
#                         side3Boundary=shapeParams["Finger " + str(fingerIndex) + " T Side 3 Boundary"],
#                         side4Boundary=shapeParams["Finger " + str(fingerIndex) + " T Side 4 Boundary"],
#                         meshBoundary=shapeParams["Mesh Boundary"],
#                         angle=0
#                     )
#                     componentLeft += [
#                         fingerStemPolyline[0], fingerStemPolyline[1],
#                         fingerTPolyline[0], fingerTPolyline[1], fingerTPolyline[2], fingerTPolyline[3],
#                         fingerStemPolyline[2], fingerStemPolyline[3]
#                     ]
#                     peripheryPolylines += [fingerStemPeripheryPolyline, fingerTPeripheryPolyline]
#                     meshPeripheryPolylines += [fingerStemMeshPeripheryPolyline, fingerTMeshPeripheryPolyline]
#                 component = componentLeft + componentRight

'''A node has an absolute location either on its own or relative to a design.'''
class Node:
    def __init__(self, name, shapeName):
        self.name = name
        self.shape = interpretShape(shapeName)
        self.material = "perfect conductor"  # Default material.
        self.color = "(143 143 175)"  # Grey by default

        '''The polylines of the shape assume center x = centery = z = angle = 0. The node polylines update these values
        and place the shape appropriately relative to the rest of the design.'''
        self.polyline = np.zeros(0)
        self.peripheryPolylines = list()
        self.meshPeripheryPolylines = list()
        self.centerX = 0
        self.centerY = 0
        self.angle = 0
        self.Z = 0  # Height above X-Y plane.

    def createPolylines(self):
        self.shape.createPolylines()
        self.polyline = np.array([translate(rotate(point, self.angle), self.centerX, self.centerY)
                                  for point in self.shape.polyline])
        self.peripheryPolylines = [np.array([translate(rotate(point, self.angle), self.centerX, self.centerY)
                                             for point in peripheryPolyline])
                                   for peripheryPolyline in self.shape.peripheryPolylines]
        self.meshPeripheryPolylines = [np.array([translate(rotate(point, self.angle), self.centerX, self.centerY)
                                                 for point in meshPeripheryPolyline])
                                       for meshPeripheryPolyline in self.shape.meshPeripheryPolylines]

    @property
    def centroid(self):  # Return the centroid of the polyline.
        return np.array([np.sum(self.polyline[:, 0]),
                         np.sum(self.polyline[:, 1])]) / self.polyline.shape[0]

    @property
    def segmentList(self):  # Returns the segment list of the polyline
        segList = []
        for index, point in enumerate(self.polyline):
            point1 = point
            if index == len(self.polyline) - 1:
                point2 = self.polyline[0]
            else:
                point2 = self.polyline[index + 1]
            segList.append([point1, point2])
        return segList

    @property
    def height(self):
        return self.shape.paramsDict['Height']


class NodeShape(ABC):
    '''A NodeShape is a 3D element. '''
    def __init__(self, params):
        self.paramsDict = dict({i: 0 for i in params})
        self.polyline = np.zeros(0)
        self.peripheryPolylines = list()  # List of numpy arrays
        self.meshPeripheryPolylines = list()  # List of numpy arrays

    @abstractmethod
    def createPolylines(self):  # Calculate polylines based on loaded params.
        ...


def rect(W, L):
    return [[-W / 2, -L / 2], [-W / 2, L / 2], [W / 2, L / 2], [W / 2, -L / 2]]


class Rectangle(NodeShape):
    def __init__(self, extraParams=None):
        if extraParams is None:
            extraParams = []
        params = ["Width", "Length", "Height", "Boundaries", "MeshBoundary"] + extraParams
        super().__init__(params)
        self.paramsDict['Boundaries'] = [0] * 4  # Default value

    def createPolylines(self):
        width = self.paramsDict['Width']
        length = self.paramsDict['Length']

        self.polyline = np.array(rect(width, length))

        peripheryWidth = width + self.paramsDict['Boundaries'][0] + self.paramsDict['Boundaries'][2]
        peripheryLength = length + self.paramsDict['Boundaries'][1] + self.paramsDict['Boundaries'][3]
        self.peripheryPolylines = [np.array(rect(peripheryWidth, peripheryLength))]

        meshPeripheryWidth = peripheryWidth + 2 * self.paramsDict['MeshBoundary']
        meshPeripheryLength = peripheryLength + 2 * self.paramsDict['MeshBoundary']
        self.meshPeripheryPolylines = [np.array(rect(meshPeripheryWidth, meshPeripheryLength))]


class RectanglePlusStem(Rectangle):
    '''Stem is pointed downward, origin is the center of the rectangle'''

    def __init__(self):
        super().__init__(['StemX', 'StemLength', 'StemWidth', 'StemBoundary'])

    def createPolylines(self):
        body = Rectangle()
        body.paramsDict['Width'] = self.paramsDict['Width']
        body.paramsDict['Length'] = self.paramsDict['Length']
        body.paramsDict['Height'] = self.paramsDict['Height']
        body.paramsDict['Boundaries'] = self.paramsDict['Boundaries']
        body.paramsDict['MeshBoundary'] = self.paramsDict['MeshBoundary']
        body.createPolylines()

        stem = Rectangle()
        stem.paramsDict['Width'] = self.paramsDict['StemWidth']
        stem.paramsDict['Length'] = self.paramsDict['StemLength']
        stem.paramsDict['Height'] = self.paramsDict['Height']
        stem.paramsDict['Boundaries'] = [self.paramsDict['StemBoundary']]*4
        stem.paramsDict['MeshBoundary'] = self.paramsDict['MeshBoundary']
        stem.createPolylines()
        stem.polyline = translate(stem.polyline, 0, -stem.paramsDict['Length']/2 - body.paramsDict['Length']/2)

        self.polyline = np.concatenate((body.polyline,
                                        np.array([stem.polyline[2],
                                                  stem.polyline[3],
                                                  stem.polyline[0],
                                                  stem.polyline[1]])))
        self.peripheryPolylines = body.peripheryPolylines + stem.peripheryPolylines
        self.meshPeripheryPolylines = body.meshPeripheryPolylines + stem.meshPeripheryPolylines


class Path(NodeShape):
    def __init__(self):
        super().__init__(['Width', 'Gap', 'SectionCode', 'MeshBoundary'])
        self.endPoint = []  # Only used for paths
        self.endAngle = []

    def createPolylines(self):
        polyline, endPoint, endAngle = pathPolyline(self.paramsDict['Width'], self.paramsDict['SectionCode'])
        peripheryWidth = (self.paramsDict["Width"] + 2 * self.paramsDict["Gap"])

        peripheryPolyline, _, _ = pathPolyline(
            width=peripheryWidth,
            sectionCode=self.paramsDict["SectionCode"] + "(S:" + str(traceBuffer) + ")"
        )
        meshPeripheryPolyline, _, _ = pathPolyline(
            width=peripheryWidth + 2 * self.paramsDict["MeshBoundary"],
            sectionCode=self.paramsDict["SectionCode"]
        )

        self.endPoint = endPoint
        self.endAngle = endAngle
        self.polyline = np.array(polyline)
        self.peripheryPolylines = [peripheryPolyline]
        self.meshPeripheryPolylines = [meshPeripheryPolyline]


def interpretShape(shapeName):
    if shapeName == 'Rectangle':
        return Rectangle()
    elif shapeName == 'RectanglePlusStem':
        return RectanglePlusStem()
    elif shapeName == 'Path':
        return Path()
