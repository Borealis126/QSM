from abc import ABC, abstractmethod
from sympy import symbols
from node import Node
from basicGeometry import translate, rotatePolyline
import numpy as np

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
        self.padListGeom = [ComponentPad(componentName=self.name, padIndex=1),
                            ComponentPad(componentName=self.name, padIndex=2)]

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

        pad1, pad2 = self.padListGeom
        pad1.node.shape.paramsDict['Width'] = self.paramsDict['Pad 1 Width']
        pad1.node.shape.paramsDict['Length'] = self.paramsDict['Pad 1 Length']
        pad1.node.shape.paramsDict['Height'] = self.paramsDict['Pad 1 Height']
        pad1.node.shape.paramsDict['Boundaries'] = self.paramsDict['Pad 1 Boundaries']
        pad1.node.shape.paramsDict['JJStemWidth'] = self.paramsDict['JJ Stem Width']
        pad1.node.shape.paramsDict['JJStemLength'] = stemLength
        pad1.node.shape.paramsDict['MeshBoundary'] = self.paramsDict['Mesh Boundary']
        pad1.node.Z = self.paramsDict['Z']
        pad1.node.createPolylines()

        pad2.node.shape.paramsDict['Width'] = self.paramsDict['Pad 2 Width']
        pad2.node.shape.paramsDict['Length'] = self.paramsDict['Pad 2 Length']
        pad2.node.shape.paramsDict['Height'] = self.paramsDict['Pad 2 Height']
        pad2.node.shape.paramsDict['Boundaries'] = self.paramsDict['Pad 2 Boundaries']
        pad2.node.shape.paramsDict['JJStemWidth'] = self.paramsDict['JJ Stem Width']
        pad2.node.shape.paramsDict['JJStemLength'] = stemLength
        pad2.node.shape.paramsDict['MeshBoundary'] = self.paramsDict['Mesh Boundary']
        pad2.node.Z = self.paramsDict['Z']
        pad2.node.createPolylines()

        def placePad1(polyline):
            return translate(polyline, 0, pad1.node.shape.paramsDict['Length'] / 2 + self.paramsDict['Pad Spacing'] / 2)

        pad1.node.polyline = placePad1(pad1.node.polyline)
        pad1.node.peripheryPolylines = [placePad1(i) for i in pad1.node.peripheryPolylines]
        pad1.node.meshPeripheryPolylines = [placePad1(i) for i in pad1.node.meshPeripheryPolylines]

        def placePad2(polyline):
            return translate(rotatePolyline(polyline, np.pi), 0,
                             -pad2.node.shape.paramsDict['Length'] / 2 - self.paramsDict['Pad Spacing'] / 2)

        pad2.node.polyline = placePad2(pad2.node.polyline)
        pad2.node.peripheryPolylines = [placePad2(i) for i in pad2.node.peripheryPolylines]
        pad2.node.meshPeripheryPolylines = [placePad2(i) for i in pad2.node.meshPeripheryPolylines]

        # rotate and translate everything.
        def placeDesign(polyline):
            return translate(rotatePolyline(polyline, self.paramsDict['Angle']),
                             self.paramsDict['Center X'],
                             self.paramsDict['Center Y'])

        for pad in [pad1, pad2]:
            pad.node.polyline = placeDesign(pad.node.polyline)
            pad.node.peripheryPolylines = [placeDesign(i) for i in pad.node.peripheryPolylines]
            pad.node.meshPeripheryPolylines = [placeDesign(i) for i in pad.node.meshPeripheryPolylines]


class GroundedRectangularTransmonSingleJJ(QubitDesign):
    def __init__(self, name):
        super().__init__(name, ["Angle", "Center X", "Center Y",
                                "Pad 1 Width", "Pad 1 Length", "Pad 1 Height", "Pad 1 Boundaries",
                                "JJ Location", "JJ Stem Boundary", "JJ Stem Width",
                                "JJ Patch Width", "JJ Patch Length", "JJ Top Electrode Width",
                                "JJ Bottom Electrode Width", "Mesh Boundary"])
        pad1, pad2 = self.padListGeom
        pad1.node = Node(pad1.name, 'RectanglePlusSingleJJ')
        pad2.node = Node(pad2.name, 'RectanglePlusSingleJJ')

    @property
    def padList(self):
        return [self.padListGeom[0]]

    def updateNodes(self):
        pad1, pad2 = self.padListGeom
        pad1.node.shape.paramsDict['Width'] = self.paramsDict['Pad 1 Width']
        pad1.node.shape.paramsDict['Length'] = self.paramsDict['Pad 1 Length']
        pad1.node.shape.paramsDict['Height'] = self.paramsDict['Pad 1 Height']
        pad1.node.shape.paramsDict['Boundaries'] = self.paramsDict['Pad 1 Boundaries']
        pad1.node.shape.paramsDict['MeshBoundary'] = self.paramsDict['Mesh Boundary']
        pad1.node.createPolylines()

        pad2.node.shape.paramsDict['Width'] = self.paramsDict['Pad 2 Width']
        pad2.node.shape.paramsDict['Length'] = self.paramsDict['Pad 2 Length']
        pad2.node.shape.paramsDict['Height'] = self.paramsDict['Pad 2 Height']
        pad2.node.shape.paramsDict['Boundaries'] = self.paramsDict['Pad 2 Boundaries']
        pad2.node.shape.paramsDict['MeshBoundary'] = self.paramsDict['Mesh Boundary']
        pad2.node.createPolylines()

        for polyline in [pad1.node.polyline] + pad1.node.peripheryPolylines + pad1.node.meshPeripheryPolylines:
            polyline = translate(polyline, 0,
                                 pad1.node.shape.paramsDict['Length'] / 2 + self.paramsDict['Pad Spacing'] / 2)

        for polyline in [pad2.polyline] + pad2.peripheryPolylines + pad2.meshPeripheryPolylines:
            polyline = rotatePolyline(polyline, np.pi)
            polyline = translate(polyline, 0,
                                 -pad2.node.shape.paramsDict['Length'] / 2 - self.paramsDict['Pad Spacing'] / 2)

        # rotate and translate everything.
        for pad in [pad1, pad2]:
            for polyline in [pad.node.polyline] + pad.node.peripheryPolylines + pad.node.meshPeripheryPolylines:
                translate(rotatePolyline(polyline, self.paramsDict['Angle']),
                          self.paramsDict['Center X'],
                          self.paramsDict['Center Y'])


def interpretDesign(designName):
    if designName == 'FloatingRectangularTransmonSingleJJ':
        return FloatingRectangularTransmonSingleJJ
    elif designName == 'GroundedRectangularTransmonSingleJJ':
        return GroundedRectangularTransmonSingleJJ
