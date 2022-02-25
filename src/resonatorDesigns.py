from abc import ABC, abstractmethod
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
        CPW_obj = self.CPW
        endAngles = [self.paramsDict["Pad 1 Curve Angle"], self.paramsDict["Pad 2 Curve Angle"]]

        #We are bypassing the 'shape' aspect of the meanderNode due to already-existing code.
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

        pad1RealCenterPoint = translate(rotate(np.array([0, self.paramsDict["Pad 1 Length"] / 2
                                                         + self.paramsDict["Pad T Stem Length"]]),
                                               meanderStartAngle + np.pi / 2),
                                        meanderStartPoint[0],
                                        meanderStartPoint[1])
        pad2RealCenterPoint = translate(rotate(np.array([0, self.paramsDict["Pad 2 Length"] / 2
                                                         + self.paramsDict["Pad T Stem Length"]]),
                                               meanderEndAngle + 3 * np.pi / 2),
                                        meanderEndPoint[0],
                                        meanderEndPoint[1])

        self.pad1.node.centerX, self.pad1.node.centerY = pad1RealCenterPoint
        self.pad1.node.angle = (meanderStartAngle - 3 * np.pi / 2)
        self.pad2.node.centerX, self.pad2.node.centerY = pad2RealCenterPoint
        self.pad2.node.angle = meanderEndAngle - np.pi / 2

        self.pad1.node.orientShape()
        self.pad2.node.orientShape()


def interpretDesign(designName):
    if designName == 'CPWResonatorWithT':
        return CPWResonatorWithT
