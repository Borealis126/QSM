from abc import ABC, abstractmethod
from sympy import symbols
from node import Node
from basicGeometry import translate, rotate
import numpy as np
from qubitDesigns import ComponentPad
from meander import meanderNodeGen


class ResonatorDesign(ABC):

    @abstractmethod
    def updateNodes(self):
        ...

    def __init__(self, name, params):
        self.name = name
        self.paramsDict = dict({i: None for i in params})
        self.paramsDict["Mesh Boundary"] = 0
        self.paramsDict["Z"] = 0  # Based on the substrate height
        self.CPW = []

        self.meanderNode = dict()
        self.meanderStartPoint = []
        self.meanderStartAngle = 0
        self.meanderEndPoint = []
        self.meanderEndAngle = 0

        # Only pad 2 should be used in quantization (closest to qubit)
        self.pad1 = ComponentPad(componentName=self.name, padIndex=1)
        self.pad2 = ComponentPad(componentName=self.name, padIndex=2)
    @property
    def padListGeom(self):
        return [self.pad1, self.pad2]

    @property
    def promptedParams(self):
        return {i: self.paramsDict[i] for i in self.paramsDict if i != "Mesh Boundary" and i != "Z"}

class CPWResonatorWithT(ResonatorDesign):

    def __init__(self, name):
        params = ["Length", "Angle", "Center X", "Center Y", "Pad Separation", "Meander Turn Radius",
                  "Pad T Stem Length", "Meander To Pad Minimum Distance"]
        for padIndex in [1, 2]:
            params += ["Pad " + str(padIndex) + " " + i
                       for i in ["Width", "Length", "Curve Angle", "Height", "Boundaries"]]
        super().__init__(name, params)

        self.pad1.node = Node(self.pad1.name, 'RectanglePlusStem')
        self.pad2.node = Node(self.pad2.name, 'RectanglePlusStem')

    @property
    def padList(self):
        return self.padListGeom

    def updateNodes(self):
        self.updateMeanderNode()

        for padIndex, padNode in enumerate([self.pad1.node, self.pad2.node]):
            padNode.shape.paramsDict['Width'] = self.paramsDict['Pad '+str(padIndex+1)+' Width']
            padNode.shape.paramsDict['Length'] = self.paramsDict['Pad '+str(padIndex+1)+' Length']
            padNode.shape.paramsDict['Height'] = self.paramsDict['Pad '+str(padIndex+1)+' Height']
            padNode.shape.paramsDict['Boundaries'] = self.paramsDict['Pad '+str(padIndex+1)+' Boundaries']
            padNode.shape.paramsDict['StemWidth'] = self.CPW.geometryParams["Width"]
            padNode.shape.paramsDict['StemLength'] = self.paramsDict["Pad T Stem Length"]
            padNode.shape.paramsDict['StemBoundary'] = self.CPW.geometryParams["Gap"]
            padNode.shape.paramsDict['MeshBoundary'] = self.paramsDict['Mesh Boundary']
            padNode.Z = self.paramsDict['Z']
            padNode.createPolylines()

        pad1RealCenterPoint = translate(
            rotate(
                np.array([0, self.paramsDict["Pad 1 Length"] / 2 + self.paramsDict["Pad T Stem Length"]]),
                self.meanderStartAngle + np.pi / 2
            ),
            self.meanderStartPoint[0],
            self.meanderStartPoint[1]
        )
        pad2RealCenterPoint = translate(
            rotate(
                np.array([0, self.paramsDict["Pad 2 Length"] / 2 + self.paramsDict["Pad T Stem Length"]]),
                self.meanderEndAngle + 3 * np.pi / 2),
            self.meanderEndPoint[0],
            self.meanderEndPoint[1]
        )

        self.pad1.node.paramsDict["Center X"] = pad1RealCenterPoint[0]
        self.pad1.node.paramsDict["Center Y"] = pad1RealCenterPoint[1]
        self.pad1.node.paramsDict["Angle"] = (self.meanderStartAngle + 3 * np.pi / 2)
        self.pad2.node.paramsDict["Center X"] = pad2RealCenterPoint[0]
        self.pad2.node.paramsDict["Center Y"] = pad2RealCenterPoint[1]
        self.pad2.node.paramsDict["Angle"] = self.meanderEndAngle + np.pi / 2

        self.pad1.node.createPolylines()
        self.pad2.node.createPolylines()


    def updateMeanderNode(self):
        CPW_obj = self.CPW
        endAngles = [self.paramsDict["Pad 1 Curve Angle"], self.paramsDict["Pad 2 Curve Angle"]]
        self.meanderNode, self.meanderStartPoint, self.meanderStartAngle, self.meanderEndPoint, self.meanderEndAngle = \
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
                meshBoundary=self.pad1.node.shape.paramsDict["Mesh Boundary"],
                CPWObj=CPW_obj
            )
        for pad in [self.pad1, self.pad2]:
            for polyline in [pad.node.polyline] + pad.node.peripheryPolylines + pad.node.meshPeripheryPolylines:
                translate(rotate(polyline, self.paramsDict['Angle']),
                          self.paramsDict['Center X'],
                          self.paramsDict['Center Y'])


def interpretDesign(designName):
    if designName == 'CPWResonatorWithT':
        return CPWResonatorWithT
