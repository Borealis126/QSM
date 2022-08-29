from polyline import pathPolyline
from basicGeometry import rotate, translate
from constants import traceBuffer
from abc import ABC, abstractmethod
import numpy as np
class Node:
    '''A node has an absolute location either on its own or relative to a design.'''

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

    def orientShape(self):
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
        self.peripheryPolylines = [translate(np.array(rect(peripheryWidth, peripheryLength)),
                                             (self.paramsDict['Boundaries'][2] - self.paramsDict['Boundaries'][0])/2,
                                             (self.paramsDict['Boundaries'][1] - self.paramsDict['Boundaries'][3])/2)]

        meshPeripheryWidth = peripheryWidth + 2 * self.paramsDict['MeshBoundary']
        meshPeripheryLength = peripheryLength + 2 * self.paramsDict['MeshBoundary']
        self.meshPeripheryPolylines = [np.array(rect(meshPeripheryWidth, meshPeripheryLength))]


class PlusSign(NodeShape):
    def __init__(self, extraParams=None):
        if extraParams is None:
            extraParams = []
        params = ["Width", "Thickness", "Height", "Boundary", "MeshBoundary"] + extraParams
        super().__init__(params)
        self.paramsDict['Boundary'] = 0

    def createPolylines(self):
        width = self.paramsDict['Width']
        length = self.paramsDict['Thickness']

        horiz = np.array(rect(width, length))
        vert = np.array(rect(length, width))
        self.polyline = np.array([horiz[0], horiz[1], 
                                  np.array([-length/2, length/2]),
                                  vert[1], vert[2], 
                                  np.array([length/2, length/2]),
                                  horiz[2], horiz[3], 
                                  np.array([length/2, -length/2]),
                                  vert[3], vert[0],
                                  np.array([-length/2, -length/2])])

        peripheryWidth = width + 2*self.paramsDict['Boundary']
        peripheryLength = length + 2*self.paramsDict['Boundary']
        self.peripheryPolylines = [np.array(rect(peripheryWidth, peripheryLength)), np.array(rect(peripheryLength, peripheryWidth))]

        meshPeripheryWidth = peripheryWidth + 2 * self.paramsDict['MeshBoundary']
        meshPeripheryLength = peripheryLength + 2 * self.paramsDict['MeshBoundary']
        self.meshPeripheryPolylines = [np.array(rect(meshPeripheryWidth, meshPeripheryLength)), np.array(rect(meshPeripheryLength, meshPeripheryWidth))]

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
        stem.paramsDict['Boundaries'] = [self.paramsDict['StemBoundary']] * 4
        stem.paramsDict['MeshBoundary'] = self.paramsDict['MeshBoundary']
        stem.createPolylines()

        stem.polyline = translate(stem.polyline, 0, -stem.paramsDict['Length'] / 2 - body.paramsDict['Length'] / 2)
        stem.peripheryPolylines = [translate(i, 0, -stem.paramsDict['Length'] / 2 - body.paramsDict['Length'] / 2)
                                   for i in stem.peripheryPolylines]
        stem.meshPeripheryPolylines = [translate(i, 0, -stem.paramsDict['Length'] / 2 - body.paramsDict['Length'] / 2)
                                       for i in stem.meshPeripheryPolylines]

        self.polyline = np.concatenate((body.polyline,
                                        np.array([stem.polyline[2],
                                                  stem.polyline[3],
                                                  stem.polyline[0],
                                                  stem.polyline[1]])))
        self.peripheryPolylines = body.peripheryPolylines + stem.peripheryPolylines
        self.meshPeripheryPolylines = body.meshPeripheryPolylines + stem.meshPeripheryPolylines


class Path(NodeShape):
    def __init__(self):
        super().__init__(['Width', 'Gap', 'Height', 'SectionCode', 'MeshBoundary'])
        self.endPoint = []  # Only used for paths
        self.endAngle = []

    def createPolylines(self):
        startPoint = np.array([0, 0])
        startAngle = 0
        self.polyline, endPoint, endAngle = pathPolyline(self.paramsDict['Width'], startPoint, startAngle,
                                                         self.paramsDict['SectionCode'])
        peripheryWidth = (self.paramsDict["Width"] + 2 * self.paramsDict["Gap"])

        peripheryPolyline, _, _ = pathPolyline(peripheryWidth, startPoint, startAngle,
                                               self.paramsDict["SectionCode"] + "(S:" + str(traceBuffer) + ")")
        meshPeripheryPolyline, _, _ = pathPolyline(peripheryWidth + 2 * self.paramsDict["MeshBoundary"], startPoint,
                                                   startAngle, self.paramsDict["SectionCode"])

        self.endPoint = endPoint
        self.endAngle = endAngle
        self.peripheryPolylines = [peripheryPolyline]
        self.meshPeripheryPolylines = [meshPeripheryPolyline]

    def orientEndPoint(self, centerX, centerY, angle):
        return translate(rotate(self.endPoint, angle), centerX, centerY)


class LaunchPad(NodeShape):
    def __init__(self):
        params = ["CPW", "MeshBoundary", "Height"]
        super().__init__(params)
        self.paramsDict['Boundaries'] = [0] * 4  # Default value

    def createPolylines(self):
        CPW = self.paramsDict['CPW']
        meshPeriphery = self.paramsDict['MeshBoundary']
        self.polyline = np.array([
            [-400, -100],
            [-400, 100],
            [-200, 100],
            [0, CPW.geometryParams["Width"] / 2],
            [0, -CPW.geometryParams["Width"] / 2],
            [-200, -100]
        ])
        self.peripheryPolylines = [np.array([
            [-560, -260],
            [-560, 260],
            [-200, 260],
            [0, CPW.geometryParams["Width"] / 2 + CPW.geometryParams["Gap"]],
            [0, -CPW.geometryParams["Width"] / 2 - CPW.geometryParams["Gap"]],
            [-200, -260]
        ])]
        self.meshPeripheryPolylines = [np.array([
            [-560 - meshPeriphery, -260 - meshPeriphery],
            [-560 - meshPeriphery, 260 + meshPeriphery],
            [-200 + meshPeriphery, 260 + meshPeriphery],
            [0 + meshPeriphery, CPW.geometryParams["Width"] / 2 + CPW.geometryParams["Gap"] + meshPeriphery],
            [0 + meshPeriphery, -CPW.geometryParams["Width"] / 2 - CPW.geometryParams["Gap"] - meshPeriphery],
            [-200 + meshPeriphery, -260 - meshPeriphery]
        ])]


def interpretShape(shapeName):
    if shapeName == 'Rectangle':
        return Rectangle()
    elif shapeName == 'RectanglePlusStem':
        return RectanglePlusStem()
    elif shapeName == 'Path':
        return Path()
    elif shapeName == 'LaunchPad':
        return LaunchPad()
    elif shapeName == 'PlusSign':
        return PlusSign()
