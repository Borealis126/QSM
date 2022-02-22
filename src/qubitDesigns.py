from abc import ABC, abstractmethod
from sympy import symbols
from node import Node


class ComponentPad:
    def __init__(self, componentName, padIndex):
        self.index = padIndex
        self.name = componentName + "Pad" + str(self.index)
        self.node = Node(self.name)

        self.quantCapMatIndex = 0  # Updated in quantizeSimulation

        self.phiIndex = 0  # Updated in quantizeSimulation
        self.phiSym = symbols("Phi_" + componentName + "P" + str(self.index))


class QubitDesign(ABC):
    @property
    @abstractmethod
    def params(self):
        ...

    @property
    @abstractmethod
    def padList(self):
        ...

    @property
    def initialParamsDict(self):
        return dict({i: 0 for i in self.params})

    def __init__(self, name):
        self.name = name
        self.paramsDict = self.initialParamsDict
        self.JJGDSs = list()
        self.geometryParams = dict()

        '''All qubits have two pads, for grounded qubits the second is shorted to ground'''
        self.padListGeom = [ComponentPad(componentName=self.name, padIndex=1),
                            ComponentPad(componentName=self.name, padIndex=2)]


class FloatingRectangularTransmon(QubitDesign):
    def __init__(self, name):
        super().__init__(name)

    @property
    def params(self):
        return ["Angle", "Center X", "Center Y", "Pad Spacing", "JJ Location"]

    @property
    def padList(self):
        return self.padListGeom


class GroundedRectangularTransmon(QubitDesign):
    def __init__(self, name):
        super().__init__(name)

    @property
    def params(self):
        return ["Angle", "Center X", "Center Y", "JJ Location"]

    @property
    def padList(self):
        return [self.padListGeom[0]]


def interpretDesign(designName):
    if designName == 'FloatingRectangularTransmon':
        return FloatingRectangularTransmon
    elif designName == 'GroundedRectangularTransmon':
        return GroundedRectangularTransmon
