from abc import ABC, abstractmethod
from sympy import symbols
from .node import Node
from .basicGeometry import translate, rotate, rotatePolyline
import numpy as np
from copy import copy

'A design consists of two pads. Each pad is a Node. A Node stores the absolute location of the element.'


class ComponentPad:
    def __init__(self, componentName, padIndex):
        self.index = padIndex
        self.name = componentName + "Pad" + str(self.index)
        self.node = None  # Updated later

        self.quantCapMatIndex = 0  # Updated in quantizeSimulation
        self.phiIndex = 0  # Updated in quantizeSimulation
        self.phiSym = symbols("Phi_" + componentName + "P" + str(self.index))


class QubitDesign(ABC):
    @property
    @abstractmethod
    def padList(self):
        ...

    @abstractmethod
    def updateNodes(self):
        ...

    def __init__(self, name, params):
        self.name = name
        self.paramsDict = dict({i: None for i in params})
        self.paramsDict["Mesh Boundary"] = 0
        self.paramsDict["Z"] = 0  # Based on the substrate height
        self.JJGDSs = list()
        self.geometryParams = dict()

        '''All qubits have two pads, for grounded qubits the second is shorted to ground'''
        self.pad1 = ComponentPad(componentName=self.name, padIndex=1)
        self.pad2 = ComponentPad(componentName=self.name, padIndex=2)

        self.padListGeom = [self.pad1, self.pad2]

    @property
    def promptedParams(self):
        # Remove elements set indirectly
        return {i: self.paramsDict[i] for i in self.paramsDict if i != "Mesh Boundary" and i != "Z"}


class JJGDS:
    def __init__(self, patchGDS, topElectrodeGDS, bottomElectrodeGDS, connectionsGDS):
        self.patchGDS = patchGDS
        self.topElectrodeGDS = topElectrodeGDS
        self.bottomElectrodeGDS = bottomElectrodeGDS
        self.connectionsGDS = connectionsGDS


class FloatingRectangularTransmonSingleJJ(QubitDesign):
    """JJ location is any number between 0 and 100 representing the location
                        of the JJ relative to the pads. 0 is on the left, 100 is on the right, 50 is in the middle."""

    def __init__(self, name):
        super().__init__(name, ["Angle", "Center X", "Center Y", "Pad Spacing",
                                "Pad 1 Width", "Pad 1 Length", "Pad 1 Height", "Pad 1 Boundaries",
                                "Pad 2 Width", "Pad 2 Length", "Pad 2 Height", "Pad 2 Boundaries",
                                "JJ Location", "JJ Stem Boundary", "JJ Stem Width",
                                "JJ Patch Width", "JJ Patch Length", "JJ Top Electrode Width",
                                "JJ Bottom Electrode Width"])
        pad1, pad2 = self.padListGeom
        pad1.node = Node(pad1.name, 'RectanglePlusStem')
        pad2.node = Node(pad2.name, 'RectanglePlusStem')

    @property
    def padList(self):
        return self.padListGeom

    def updateNodes(self):
        stemLength = (self.paramsDict['Pad Spacing'] - self.paramsDict["JJ Patch Length"]) / 2
        #Update the shapes
        pad1, pad2 = self.padListGeom
        pad1.node.shape.paramsDict['Width'] = self.paramsDict['Pad 1 Width']
        pad1.node.shape.paramsDict['Length'] = self.paramsDict['Pad 1 Length']
        pad1.node.shape.paramsDict['Height'] = self.paramsDict['Pad 1 Height']
        pad1.node.shape.paramsDict['Boundaries'] = self.paramsDict['Pad 1 Boundaries']
        pad1.node.shape.paramsDict['StemWidth'] = self.paramsDict['JJ Stem Width']
        pad1.node.shape.paramsDict['StemLength'] = stemLength
        pad1.node.shape.paramsDict['MeshBoundary'] = self.paramsDict['Mesh Boundary']

        pad2.node.shape.paramsDict['Width'] = self.paramsDict['Pad 2 Width']
        pad2.node.shape.paramsDict['Length'] = self.paramsDict['Pad 2 Length']
        pad2.node.shape.paramsDict['Height'] = self.paramsDict['Pad 2 Height']
        pad2.node.shape.paramsDict['Boundaries'] = self.paramsDict['Pad 2 Boundaries']
        pad2.node.shape.paramsDict['StemWidth'] = self.paramsDict['JJ Stem Width']
        pad2.node.shape.paramsDict['StemLength'] = stemLength
        pad2.node.shape.paramsDict['MeshBoundary'] = self.paramsDict['Mesh Boundary']
        #Update the nodes
        pad1Center_design = np.array([0, pad1.node.shape.paramsDict['Length'] / 2
                                     + self.paramsDict['Pad Spacing'] / 2])
        pad1Center_absolute = translate(rotate(pad1Center_design, self.paramsDict['Angle']),
                                    self.paramsDict['Center X'], self.paramsDict['Center Y'])
        pad1.node.centerX, pad1.node.centerY = pad1Center_absolute
        pad1.node.angle = self.paramsDict['Angle']
        pad1.node.Z = self.paramsDict['Z']
        pad1.node.orientShape()

        pad2Center_design = np.array([0, -pad2.node.shape.paramsDict['Length'] / 2
                                         - self.paramsDict['Pad Spacing'] / 2])
        pad2Center_absolute = translate(rotate(pad2Center_design, self.paramsDict['Angle']),
                                        self.paramsDict['Center X'], self.paramsDict['Center Y'])
        pad2.node.centerX, pad2.node.centerY = pad2Center_absolute
        pad2.node.angle = self.paramsDict['Angle']+np.pi
        pad2.node.Z = self.paramsDict['Z']
        pad2.node.orientShape()


class GroundedTransmon(QubitDesign):
    def __init__(self, name, params):
        super().__init__(name, params)

    @property
    def padList(self):
        return [self.padListGeom[0]]

    def updateNodes(self):
        ...


class GroundedRectangularTransmonSingleJJ(GroundedTransmon):
    def __init__(self, name):
        super().__init__(name, ["Angle", "Center X", "Center Y",
                                "Pad Width", "Pad Length", "Pad Height", "Pad Boundaries",
                                "JJ Location", "JJ Stem Boundary", "JJ Stem Width", "JJ Patch Length", "Mesh Boundary"])
        pad1, pad2 = self.padListGeom
        pad1.node = Node(pad1.name, 'RectanglePlusStem')
        pad2.node = Node(pad2.name, 'Rectangle')

    def updateNodes(self):
        stemGap = self.paramsDict['Pad Boundaries'][3]
        stemLength = (stemGap - self.paramsDict["JJ Patch Length"]) / 2
        # Update the shapes
        pad1, pad2 = self.padListGeom
        pad1.node.shape.paramsDict['Width'] = self.paramsDict['Pad Width']
        pad1.node.shape.paramsDict['Length'] = self.paramsDict['Pad Length']
        pad1.node.shape.paramsDict['Height'] = self.paramsDict['Pad Height']
        pad1.node.shape.paramsDict['Boundaries'] = self.paramsDict['Pad Boundaries']
        pad1.node.shape.paramsDict['StemWidth'] = self.paramsDict['JJ Stem Width']
        pad1.node.shape.paramsDict['StemLength'] = stemLength
        pad1.node.shape.paramsDict['MeshBoundary'] = self.paramsDict['Mesh Boundary']

        pad2.node.shape.paramsDict['Width'] = self.paramsDict['JJ Stem Width']
        pad2.node.shape.paramsDict['Length'] = stemLength
        pad2.node.shape.paramsDict['Height'] = self.paramsDict['Pad Height']
        pad2.node.shape.paramsDict['Boundaries'] = copy(self.paramsDict['Pad Boundaries'])
        pad2.node.shape.paramsDict['Boundaries'][1] = pad2.node.shape.paramsDict['Boundaries'][3] = 0
        pad2.node.shape.paramsDict['MeshBoundary'] = self.paramsDict['Mesh Boundary']
        # Update the nodes
        pad1Center_design = np.array([0, pad1.node.shape.paramsDict['Length'] / 2
                                      + stemGap / 2])
        pad1Center_absolute = translate(rotate(pad1Center_design, self.paramsDict['Angle']),
                                        self.paramsDict['Center X'], self.paramsDict['Center Y'])
        pad1.node.centerX, pad1.node.centerY = pad1Center_absolute
        pad1.node.angle = self.paramsDict['Angle']
        pad1.node.Z = self.paramsDict['Z']
        pad1.node.orientShape()

        pad2Center_design = np.array([0, -pad2.node.shape.paramsDict['Length'] / 2
                                      - self.paramsDict["JJ Patch Length"] / 2])
        pad2Center_absolute = translate(rotate(pad2Center_design, self.paramsDict['Angle']),
                                        self.paramsDict['Center X'], self.paramsDict['Center Y'])
        pad2.node.centerX, pad2.node.centerY = pad2Center_absolute
        pad2.node.angle = self.paramsDict['Angle'] + np.pi
        pad2.node.Z = self.paramsDict['Z']
        pad2.node.orientShape()

class XMon(GroundedTransmon):
    def __init__(self, name):
        super().__init__(name, ["Angle", "Center X", "Center Y",
                                "Width", "Thickness", "Pad Height", "Boundary",
                                "JJ Location", "JJ Stem Boundary", "JJ Stem Width", "JJ Patch Length", "Mesh Boundary"])
        pad1, pad2 = self.padListGeom
        pad1.node = Node(pad1.name, 'PlusSign')
        pad2.node = Node(pad2.name, 'Rectangle')

    def updateNodes(self):
        stemGap = self.paramsDict['Boundary']
        stemLength = (stemGap - self.paramsDict["JJ Patch Length"]) / 2
        # Update the shapes
        pad1, pad2 = self.padListGeom
        pad1.node.shape.paramsDict['Width'] = self.paramsDict['Width']
        pad1.node.shape.paramsDict['Thickness'] = self.paramsDict['Thickness']
        pad1.node.shape.paramsDict['Height'] = self.paramsDict['Pad Height']
        pad1.node.shape.paramsDict['Boundary'] = self.paramsDict['Boundary']
        pad1.node.shape.paramsDict['StemWidth'] = self.paramsDict['JJ Stem Width']
        pad1.node.shape.paramsDict['StemLength'] = stemLength
        pad1.node.shape.paramsDict['MeshBoundary'] = self.paramsDict['Mesh Boundary']

        pad2.node.shape.paramsDict['Width'] = self.paramsDict['JJ Stem Width']
        pad2.node.shape.paramsDict['Length'] = stemLength
        pad2.node.shape.paramsDict['Height'] = self.paramsDict['Pad Height']
        pad2.node.shape.paramsDict['Boundaries'] = [self.paramsDict['Boundary']]*4
        pad2.node.shape.paramsDict['Boundaries'][1] = pad2.node.shape.paramsDict['Boundaries'][3] = 0
        pad2.node.shape.paramsDict['MeshBoundary'] = self.paramsDict['Mesh Boundary']
        # Update the nodes
        pad1Center_design = np.array([0, pad1.node.shape.paramsDict['Width'] / 2
                                      + stemGap / 2])
        pad1Center_absolute = translate(rotate(pad1Center_design, self.paramsDict['Angle']),
                                        self.paramsDict['Center X'], self.paramsDict['Center Y'])
        pad1.node.centerX, pad1.node.centerY = pad1Center_absolute
        pad1.node.angle = self.paramsDict['Angle']
        pad1.node.Z = self.paramsDict['Z']
        pad1.node.orientShape()

        pad2Center_design = np.array([0, -pad2.node.shape.paramsDict['Width'] / 2
                                      - self.paramsDict["JJ Patch Length"] / 2])
        pad2Center_absolute = translate(rotate(pad2Center_design, self.paramsDict['Angle']),
                                        self.paramsDict['Center X'], self.paramsDict['Center Y'])
        pad2.node.centerX, pad2.node.centerY = pad2Center_absolute
        pad2.node.angle = self.paramsDict['Angle'] + np.pi
        pad2.node.Z = self.paramsDict['Z']
        pad2.node.orientShape()


def interpretDesign(designName):
    if designName == 'FloatingRectangularTransmonSingleJJ':
        return FloatingRectangularTransmonSingleJJ
    elif designName == 'GroundedRectangularTransmonSingleJJ':
        return GroundedRectangularTransmonSingleJJ
    elif designName == 'XMon':
        return XMon
