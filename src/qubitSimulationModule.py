import subprocess
import numpy as np
import matplotlib.pyplot as plt
import os
from scipy.misc import derivative
import gdspy
import time
from ChipElements import OtherComponents
from sympy import symbols, Matrix, zeros, sin
from qutip import state_number_index, qzero, ket, bra
from analysisFunctions import S21TodB, calculateDressedFrequency
from ansysFunctions import *
from basicGeometryFunctions import pointInPolyline, rotate, translate
from csvFunctions import *
from node import Node
from polylineFunctions import rectanglePolyline, multiplyPolyline
from qSysObjects import *
from quantumStateFunctions import stateFromHeader, baseRepresentation, H_Header
from constants import *
from simulations import *


def generateSystemParametersFile(folder):
    file = folder / "systemParametersFile.csv"
    lines = [
        ["Chip Description", "description"],
        ["Number of Qubits", 1],
        ["Number of Readout Resonators", 1],
        ["Number of Bus Coupler Resonators", 1],
        ["Number of PTCs", 0],
        ["Number of Straight Bus Couplers", 0],
        ["Number of Control Lines", 1],
        ["Material", "perfect conductor"],
        ["Flip Chip?", "No"],
        ["Chip Markers", "Pappas"],
        ["Simulation", "2D"],
        ["Simulate Feedline?", "No"],
        ["Add Mesh to GDS?", "No"],
        ["Invert GDS?", "No"],
        ["Anti-Vortex Mesh Boundary", 40],
        ["Anti-Vortex Mesh Spacing", 50],
        ["Anti-Vortex Mesh Size", 5]
    ]  # This is how far the holes in the substrate are from any given component.
    csvWrite(file, lines)


def initialize(projectFolder, computeLocation, QSMSourceFolder):
    qSys = loadSystemParametersFile(projectFolder, computeLocation, QSMSourceFolder)
    return qSys


def loadSystemParametersFile(projectFolder, computeLocation, QSMSourceFolder):
    """Returns qubitSystem object based on data in systemParametersFile"""
    systemParametersFileLines = csvRead(projectFolder / "systemParametersFile.csv")
    systemParams = dict()
    for line in systemParametersFileLines:
        systemParams[line[0]] = returnCorrectType(line[1])
    systemParams["Project Folder"] = projectFolder
    systemParams["Compute Location"] = computeLocation
    systemParams["QSM Source Folder"] = QSMSourceFolder
    return QubitSystem(sysParams=systemParams)


class QubitSystem:
    def __init__(self, sysParams):
        # ---independent of flip chip
        self.sysParams = sysParams
        self.projectFolder = self.sysParams["Project Folder"]
        self.componentParametersFile = self.projectFolder / "componentParametersFile.csv"
        self.componentGeometriesFile = self.projectFolder / "componentGeometriesFile.csv"
        self.gdspyFile = self.projectFolder / "layout.gds"

        # Dictionaries that are only used until the components are assigned to their respective chips
        self.chipDict = dict()
        # ------------------------------------
        if self.sysParams["Flip Chip?"] == "Yes":
            self.chipDict = {0: Chip(0), 1: Chip(1)}
            self.bumpsDict = dict()  # Not clearly tied to a single chip.
            self.chipSpacing = 0  # Not clearly tied to a single chip.
        elif self.sysParams["Flip Chip?"] == "No":
            self.chipDict = {0: Chip(0)}
        self.CPW = CPW()  # Substantiated in loadGeometries.

    def generateComponentParams(self):
        lines = []
        qubitRow = ["Qubits", "Index", "Type", "L_J(H)", "L_I(H)"]
        readoutResonatorRow = ["Readout Resonators", "Index", "Pad 1 Type", "Pad 2 Type"]
        busCouplerResonatorRow = ["Bus Coupler Resonators", "Index", "Pad 1 Type", "Pad 2 Type"]
        PTCRow = ["PTCs", "Index", "SQUID Inductance(H)", "Phase Velocity (um/s)"]
        straightBusCouplerRow = ["Straight Bus Couplers", "Index", "L_J(H)", "L_I(H)"]
        controlLineRow = ["Control Lines", "Index",
                          "Type"]
        bumpsRow = []
        if self.sysParams["Flip Chip?"] == "Yes":
            qubitRow = qubitRow + ["Chip"]
            readoutResonatorRow = readoutResonatorRow + ["Chip"]
            PTCRow = PTCRow + ["Chip"]
            controlLineRow = controlLineRow + ["Chip"]
            bumpsRow = ["Bumps", "Spacing", "Bump Metal Width", "Under Bump Width"]
        if self.sysParams["Number of Qubits"] != 0:
            lines.append(qubitRow)
            for qubitIndex in range(self.sysParams["Number of Qubits"]):
                lines.append(["", qubitIndex])
            lines.append([""])
        if self.sysParams["Number of Readout Resonators"] != 0:
            if self.sysParams["Simulate Feedline?"] == "No":
                readoutResonatorRow = readoutResonatorRow + ["Capacitance to Feedline (F)",
                                                             "Feedline Pad Capacitance to Ground (F)"]
            lines.append(readoutResonatorRow)
            for readoutResonatorIndex in range(self.sysParams["Number of Readout Resonators"]):
                lines.append(["", readoutResonatorIndex])
            lines.append([""])
        if self.sysParams["Number of Bus Coupler Resonators"] != 0:
            lines.append(busCouplerResonatorRow)
            for busCouplerResonatorIndex in range(self.sysParams["Number of Bus Coupler Resonators"]):
                lines.append(["", busCouplerResonatorIndex])
            lines.append([""])
        if self.sysParams["Number of PTCs"] != 0:
            lines.append(PTCRow)
            for PTCIndex in range(self.sysParams["Number of PTCs"]):
                lines.append(["", PTCIndex])
            lines.append([""])
        if self.sysParams["Number of Straight Bus Couplers"] != 0:
            lines.append(straightBusCouplerRow)
            for straightBusCouplerIndex in range(self.sysParams["Number of Straight Bus Couplers"]):
                lines.append(["", straightBusCouplerIndex])
            lines.append([""])
        if self.sysParams["Number of Control Lines"] != 0:
            lines.append(controlLineRow)
            for controlLineIndex in range(self.sysParams["Number of Control Lines"]):
                lines.append(["", controlLineIndex])
            lines.append([""])

        lines.append(["CPW", "Phase Velocity(um/s)"])
        lines.append([""])
        lines.append([""])

        if self.sysParams["Flip Chip?"] == "Yes":
            lines.append(bumpsRow)

        csvWrite(self.componentParametersFile, lines)

    def loadComponentParams(self):
        fileLines = csvRead(self.componentParametersFile)
        # Qubits
        if self.sysParams["Number of Qubits"] != 0:
            qubitComponentsDict = readComponentRowData(fileLines, "Qubits")
            for qubitIndex, params in qubitComponentsDict.items():
                qubitChipIndex = None
                if self.sysParams["Flip Chip?"] == "Yes":
                    qubitChipIndex = returnCorrectType(qubitComponentsDict[qubitIndex]["Chip"])
                elif self.sysParams["Flip Chip?"] == "No":
                    qubitChipIndex = 0
                qubit = dict()
                if "Floating" in params["Type"]:
                    qubit = FloatingQubit(self,index=qubitIndex)
                elif "Grounded" in params["Type"]:
                    qubit = GroundedQubit(self,index=qubitIndex)
                qubit.generalParamsDict = params
                # Interpret the qubit type
                fingersStrings = [i for i in qubit.generalParamsDict["Type"].split("-") if "Fingers" in i]
                for fingersString in fingersStrings:  # Allowing both pads to have fingers
                    padIndex = returnCorrectType([i for i in fingersString.split("_") if "Pad" in i][0][3:])
                    numFingers = returnCorrectType([i for i in fingersString.split("_") if "Num" in i][0][3:])
                    qubit.fingers["Pad " + str(padIndex)] = numFingers
                self.chipDict[qubitChipIndex].qubitDict[
                    qubitIndex] = qubit  # Copy the qubit object to the chip's qubit dictionary
        # Resonators
        if self.sysParams["Number of Readout Resonators"] != 0:
            resonatorComponentsDict = readComponentRowData(fileLines, "Readout Resonators")
            for index, params in resonatorComponentsDict.items():
                resonatorChipIndex = 0
                if self.sysParams["Flip Chip?"] == "Yes":
                    resonatorChipIndex = resonatorComponentsDict[index]["Chip"]
                elif self.sysParams["Flip Chip?"] == "No":
                    resonatorChipIndex = 0
                readoutResonator = ReadoutResonator(self,index)
                self.chipDict[resonatorChipIndex].readoutResonatorDict[index] = readoutResonator
                readoutResonator.generalParamsDict = params
        # PTCs
        if self.sysParams["Number of PTCs"] != 0:
            PTCComponentsDict = readComponentRowData(fileLines, "PTCs")
            for index, params in PTCComponentsDict.items():
                PTCChipIndex = None
                if self.sysParams["Flip Chip?"] == "Yes":
                    PTCChipIndex = PTCComponentsDict[index]["Chip"]
                elif self.sysParams["Flip Chip?"] == "No":
                    PTCChipIndex = 0
                PTC = PTCClass(index)
                PTC.generalParamsDict = params
                self.chipDict[PTCChipIndex].PTCDict[index] = PTC  # Copy the qubit object to the chip's qubit dictionary
        # Straight Bus Couplers
        if self.sysParams["Number of Straight Bus Couplers"] != 0:
            componentsDict = readComponentRowData(fileLines, "Straight Bus Couplers")
            for index, params in componentsDict.items():
                chipIndex = None
                if self.sysParams["Flip Chip?"] == "Yes":
                    chipIndex = componentsDict[index]["Chip"]
                elif self.sysParams["Flip Chip?"] == "No":
                    chipIndex = 0
                straightBusCoupler = StraightBusCoupler(index)
                straightBusCoupler.generalParamsDict = params
                self.chipDict[chipIndex].straightBusCouplerDict[
                    index] = straightBusCoupler  # Copy the qubit object to the chip's qubit dictionary
        # Control Lines
        if self.sysParams["Number of Control Lines"] != 0:
            controlLineComponentsDict = readComponentRowData(fileLines, "Control Lines")
            for index, params in controlLineComponentsDict.items():
                controlLineChipIndex = None
                if self.sysParams["Flip Chip?"] == "Yes":
                    controlLineChipIndex = controlLineComponentsDict[index]["Chip"]
                elif self.sysParams["Flip Chip?"] == "No":
                    controlLineChipIndex = 0
                controlLine = ControlLine(index)
                controlLine.generalParamsDict = params
                self.chipDict[controlLineChipIndex].controlLineDict[
                    index] = controlLine  # Copy the qubit object to the chip's qubit dictionary
        # Load CPW info
        self.CPW.generalParamsDict = readSingleRowData(fileLines, "CPW")
        # Load bumps info
        if self.sysParams["Flip Chip?"] == "Yes":
            self.bumpsDict = readSingleRowData(fileLines, "Bumps")

        # Components ordering
        nonGECapMatIndex = 0
        self.preGECapMatHeaders = []
        self.postGEComponentList = []
        for qubitIndex, qubit in self.allQubitsDict.items():
            qubit.pad1.quantCapMatIndex = nonGECapMatIndex
            self.preGECapMatHeaders.append(qubit.pad1.name)
            nonGECapMatIndex += 1
            if isinstance(qubit, FloatingQubit):
                qubit.pad2.quantCapMatIndex = nonGECapMatIndex
                nonGECapMatIndex += 1
                self.preGECapMatHeaders.append(qubit.pad2.name)
            self.postGEComponentList.append(qubit)
        for straightBusCouplerIndex, straightBusCoupler in self.allStraightBusCouplersDict.items():
            straightBusCoupler.pad1.quantCapMatIndex = nonGECapMatIndex
            self.preGECapMatHeaders.append(straightBusCoupler.pad1.name)
            straightBusCoupler.pad2.quantCapMatIndex = nonGECapMatIndex + 1
            self.preGECapMatHeaders.append(straightBusCoupler.pad2.name)
            self.postGEComponentList.append(straightBusCoupler)
            nonGECapMatIndex += 2
        for readoutResonatorIndex, readoutResonator in self.allReadoutResonatorsDict.items():
            readoutResonator.pad2.quantCapMatIndex = nonGECapMatIndex  # Only pad2 is included in quantization
            self.preGECapMatHeaders.append(readoutResonator.pad2.node.name)
            self.postGEComponentList.append(readoutResonator)
            nonGECapMatIndex += 1

    def generateGeometries(self):
        self.loadComponentParams()
        """For flip chip the polylines for the nodes, substrate, etc. are relative to looking top-down on the assembly,
        which is centered on the origin. The chip furthest from the viewer is chip 1."""
        lines = []
        # Prompt for the qubits
        for qubitIndex, qubit in self.allQubitsDict.items():
            properties = []
            if "rectangularPads" in qubit.generalParamsDict["Type"]:
                if isinstance(qubit, FloatingQubit):
                    properties += [
                        "Angle",
                        "Center X",
                        "Center Y",
                        "Pad Spacing",
                        "Pad 1 Width",
                        "Pad 1 Length",
                        "Pad 1 Height",
                        "Pad 1 Side 1 Boundary",
                        "Pad 1 Side 2 Boundary",
                        "Pad 1 Side 3 Boundary",
                        "Pad 1 Side 4 Boundary",
                        "Pad 2 Width",
                        "Pad 2 Length",
                        "Pad 2 Height",
                        "Pad 2 Side 1 Boundary",
                        "Pad 2 Side 2 Boundary",
                        "Pad 2 Side 3 Boundary",
                        "Pad 2 Side 4 Boundary",
                        "JJ Location"
                    ]
                    """JJ location is any number between 0 and 100 representing the location 
                    of the JJ relative to the pads. 0 is on the left, 100 is on the right, 50 is in the middle."""
                elif isinstance(qubit, GroundedQubit):
                    properties += [
                        "Angle",
                        "Center X",
                        "Center Y",
                        "Pad 1 Width",
                        "Pad 1 Length",
                        "Pad 1 Height",
                        "Pad 1 Side 1 Boundary",
                        "Pad 1 Side 2 Boundary",
                        "Pad 1 Side 3 Boundary",
                        "Pad 1 Side 4 Boundary",
                        "JJ Location"
                    ]
                if "doubleJJ" in qubit.generalParamsDict["Type"]:
                    properties += [
                        "SQUID Stem Separation",
                        "SQUID T Stem Width",
                        "SQUID T Head Width",
                        "SQUID T Head Length",
                        "JJ Patch Length",
                        "JJ Patch Width",
                        "JJ Boundary",
                        "SQUID Stem Width",
                        "SQUID Stem Length"
                    ]
                elif "singleJJ" in qubit.generalParamsDict["Type"]:  # Default along the line of symmetry of pads.
                    properties += [
                        "JJ Stem Boundary",
                        "JJ Stem Width",
                        "JJ Patch Width",
                        "JJ Patch Length"
                    ]
                properties += ["JJ Top Electrode Width", "JJ Bottom Electrode Width"]
                for padName, numFingers in qubit.fingers.items():
                    if numFingers > 1:
                        properties += [padName + " Finger Spacing"]
                    for fingerIndex in range(numFingers):
                        properties += [
                            padName + " Finger " + str(fingerIndex) + " Stem Length",
                            padName + " Finger " + str(fingerIndex) + " Stem Width",
                            padName + " Finger Stem Boundary",
                            padName + " Finger " + str(fingerIndex) + " T Head Length",
                            padName + " Finger " + str(fingerIndex) + " T Width",
                            padName + " Finger " + str(fingerIndex) + " T Side 1 Boundary",
                            padName + " Finger " + str(fingerIndex) + " T Side 2 Boundary",
                            padName + " Finger " + str(fingerIndex) + " T Side 3 Boundary",
                            padName + " Finger " + str(fingerIndex) + " T Side 4 Boundary"
                        ]
            lines.append([qubit.name] + properties)
            lines += [[""], [""]]
            # Prompt for resonators
        for readoutResonatorIndex, readoutResonator in self.allReadoutResonatorsDict.items():
            properties = [
                "Length",
                "Angle",
                "Center X",
                "Center Y",
                "Pad Separation",
                "Meander Turn Radius",
                "Pad T Stem Length",
                "Meander To Pad Minimum Distance",
                "Pad 1 Curve Angle",
                "Pad 2 Curve Angle"
            ]
            for padIndex in ["1", "2"]:
                if "T" in readoutResonator.generalParamsDict["Pad " + padIndex + " Type"].split("-"):
                    properties += [
                        "Pad " + padIndex + " Width",
                        "Pad " + padIndex + " Length",
                        "Pad " + padIndex + " Height",
                        "Pad " + padIndex + " Side 1 Boundary",
                        "Pad " + padIndex + " Side 2 Boundary",
                        "Pad " + padIndex + " Side 3 Boundary",
                        "Pad " + padIndex + " Side 4 Boundary"
                    ]
            lines.append([readoutResonator.name] + properties)
            lines += [[""], [""]]
        # Prompt for PTCs
        for PTCIndex, PTC in self.allPTCsDict.items():
            properties = [
                "Length",
                "Angle",
                "Center X",
                "Center Y",
                "End Separation",
                "Meander Turn Radius",
                "Meander To End Minimum Distance",
                "Height",
                "CPW Width",
                "CPW Gap",
                "SQUID Stem Separation",
                "SQUID T Stem Length",
                "SQUID T Head Width",
                "SQUID T Head Length",
                "SQUID Patch Length",
                "SQUID Patch Width",
                "SQUID Boundary",
                "SQUID Stem Width",
                "SQUID Stem Length",
                "SQUID Bar Width",
                "SQUID Bar Boundary",
                "SQUID Bar Length",
                "SQUID Bar T Length",
                "SQUID Bar T Width",
                "SQUID Bar T Boundary",
                "JJ Top Electrode Width",
                "JJ Bottom Electrode Width"
            ]
            lines.append([PTC.name] + properties)
            lines += [[""], [""]]
        # Prompt for the bus couplers
        for straightBusCouplerIndex, straightBusCoupler in self.allStraightBusCouplersDict.items():
            properties = [
                "Total Length",
                "Angle",
                "Center X",
                "Center Y",
                "Height",
                "Body Width",
                "Body Boundary",
                "End Width",
                "End Length",
                "End Boundary",
                "SQUID Stem Separation",
                "SQUID T Stem Width",
                "SQUID T Stem Length",
                "SQUID T Head Width",
                "SQUID T Head Length",
                "SQUID Patch Length",
                "SQUID Patch Width",
                "SQUID Boundary",
                "SQUID Stem Width",
                "SQUID Stem Length",
                "JJ Top Electrode Width",
                "JJ Bottom Electrode Width"
            ]
            lines.append([straightBusCoupler.name] + properties)
            lines += [[""], [""]]
        # Prompt for the control lines.
        for controlLineIndex, controlLine in self.allControlLinesDict.items():
            properties = [
                "Start X",
                "Start Y",
                "Start Angle",
                "Section Code"
            ]
            if controlLine.generalParamsDict["Type"] == "fluxBias":
                properties += [
                    "loopThickness",
                    "loopSeg1Length",
                    "loopSeg2Length",
                    "loopSeg3Length",
                    "loopSeg1Boundary",
                    "loopSeg2Boundary",
                    "loopSeg3Boundary"
                ]
            if controlLine.generalParamsDict["Type"] == "drive":
                properties += ["End Gap"]
            lines.append([controlLine.name] + properties)
            lines += [[""], [""]]
        # Prompt for the CPW.
        CPWParams = ["CPW", "Width", "Gap", "Trench", "Height"]
        lines.append(CPWParams)
        lines.append(["", "10", "6", "0.1", "0.1"])
        lines.append([""])

        # Prompt for the ground(s).
        lines.append(["Ground(s)", "Index", "Height"])
        for chipIndex, chip in self.chipDict.items():
            lines.append(["", chip.ground.index, 0.1])
        lines.append([""])

        # Prompt for the substrate(s).
        lines.append(["Substrate(s)", "Index", "Material", "Thickness", "Width", "Length"])
        for chipIndex, chip in self.chipDict.items():
            lines.append(["", chip.substrate.index, "silicon", 500, 9500, 7500])
        lines.append([""])

        # Prompt for NIST logo location
        lines.append(["NIST Logo", "Center X", "Center Y"])
        lines.append(["", 2000, -3000])
        lines.append([""])

        # Prompt for Chip Description location
        lines.append(["Chip Description", "Start X", "Start Y"])
        lines.append(["", 1500, -2500])
        lines.append([""])
        # If flip chip, prompt for chip spacing
        if self.sysParams["Flip Chip?"] == "Yes":
            lines.append(["Flip Chip", "Chip Spacing"])
            lines.append(["", 1000])
            lines.append([""])
        csvWrite(self.componentGeometriesFile, lines)

    def loadGeometries(self):
        fileLines = csvRead(self.componentGeometriesFile)
        # Load CPW info
        self.CPW.geometryParamsDict = readSingleRowData(fileLines, "CPW")
        # Load NIST Logo info
        NISTLogoParams = readSingleRowData(fileLines, "NIST Logo")
        self.chipDict[0].nistLogoCenter = [NISTLogoParams["Center X"],
                                           NISTLogoParams["Center Y"]]  # Logo always on the first chip.
        # Load Chip Description info
        chipDescriptionParams = readSingleRowData(fileLines, "Chip Description")
        self.chipDict[0].chipDescriptionStart = [chipDescriptionParams["Start X"],
                                                 chipDescriptionParams["Start Y"]]  # Logo always on the first chip.
        # If flip chip, load chip spacing
        if self.sysParams["Flip Chip?"] == "Yes":
            self.chipSpacing = readSingleRowData(fileLines, "Flip Chip")["Chip Spacing"]
        substrateParamsDict = readComponentRowData(fileLines, "Substrate(s)")
        groundComponentsDict = readComponentRowData(fileLines, "Ground(s)")
        # Load geometries
        for chipIndex, chip in self.chipDict.items():
            # Substrates
            chip.substrate.geometryParamsDict = substrateParamsDict[chipIndex]
            chip.substrate.node.height = chip.substrate.geometryParamsDict["Thickness"]
            chip.substrate.node.material = chip.substrate.geometryParamsDict["Material"]
            chip.substrate.node.polyline = rectanglePolyline(centerX=0,
                                                             centerY=0,
                                                             width=chip.substrate.geometryParamsDict["Width"],
                                                             length=chip.substrate.geometryParamsDict["Length"],
                                                             angle=0)
            if chipIndex == 0:
                chip.substrate.node.Z = 0  # Always 0 for substrate 0, convention
            elif chipIndex == 1:
                chip.substrate.node.Z = self.chipDict[0].substrate.node.height + self.chipSpacing
            # Ground
            chip.ground.geometryParamsDict = groundComponentsDict[chipIndex]
            chip.ground.outlineNode.height = chip.ground.geometryParamsDict["Height"]
            chip.ground.outlineNode.polyline = chip.substrate.node.polyline  # Ground covers the full substrate
            if chipIndex == 0:
                chip.ground.outlineNode.Z = self.chipDict[0].substrate.node.height
            elif chipIndex == 1:
                chip.ground.outlineNode.Z = self.chipDict[1].substrate.node.Z - chip.ground.outlineNode.height
            # Qubits
            for qubitIndex, qubit in chip.qubitDict.items():
                qubit.geometryParamsDict = readSingleRowData(fileLines, qubit.name)
                geoms = qubit.geometryParamsDict
                JJLoc_x, JJLoc_y = readJJLocation(geoms["JJ Location"])
                pad1Node = qubit.pad1.node
                pad2Node = qubit.pad2.node
                # Polylines
                if "rectangularPads" in qubit.generalParamsDict["Type"]:
                    padSpacing = 0
                    centerX = 0  # X,Y coordinates of the symmetric center of the two-pad structure.
                    centerY = 0
                    pad1NormalizedCenterPoint = [0, 0]
                    pad2NormalizedCenterPoint = [0, 0]
                    if isinstance(qubit, FloatingQubit):
                        padSpacing = geoms["Pad Spacing"]
                        centerX = geoms["Center X"]
                        centerY = geoms["Center Y"]
                        pad1NormalizedCenterPoint = [0, padSpacing / 2 + geoms["Pad 1 Length"] / 2]
                        pad2NormalizedCenterPoint = [0, -padSpacing / 2 - geoms["Pad 2 Length"] / 2]
                        pad2Node.polylineShapeParams["JJ Stem X"] = -JJLoc_x
                    if isinstance(qubit, GroundedQubit):
                        # Pad 2 is a sliver that will be shorted to ground.
                        pad2Node.polylineShape = "rectangle"
                        geoms["Pad 2 Length"] = 0.01
                        geoms["Pad 2 Height"] = geoms["Pad 1 Height"]
                        geoms["Pad 2 Side 1 Boundary"] = 0
                        geoms["Pad 2 Side 2 Boundary"] = 0
                        geoms["Pad 2 Side 3 Boundary"] = 0
                        geoms["Pad 2 Side 4 Boundary"] = 0

                        padSpacing = (geoms["Pad 1 Side 4 Boundary"]
                                      - geoms["Pad 2 Length"])
                        centerX = geoms["Center X"]
                        centerY = (geoms["Center Y"]
                                   - geoms["Pad 1 Length"] / 2
                                   - padSpacing / 2)
                        pad1NormalizedCenterPoint = [0, padSpacing / 2 + geoms["Pad 1 Length"] / 2]
                        pad2NormalizedCenterPoint = [JJLoc_x, -padSpacing / 2 - geoms["Pad 2 Length"] / 2]
                        pad2Node.polylineShapeParams["JJ Stem X"] = 0
                    for pad in qubit.padListGeom:
                        pad.node.polylineShape = "rectangle"
                    # Top pad
                    pad1CenterPoint = translate(rotate(pad1NormalizedCenterPoint, geoms["Angle"]), centerX, centerY)
                    pad1Node.polylineShapeParams["Body Center X"] = pad1CenterPoint[0]
                    pad1Node.polylineShapeParams["Body Center Y"] = pad1CenterPoint[1]
                    pad1Node.polylineShapeParams["Angle"] = geoms["Angle"]
                    pad1Node.polylineShapeParams["JJ Stem X"] = JJLoc_x

                    # Bottom pad
                    pad2CenterPoint = translate(rotate(pad2NormalizedCenterPoint, geoms["Angle"]), centerX, centerY)
                    pad2Node.polylineShapeParams["Body Center X"] = pad2CenterPoint[0]
                    pad2Node.polylineShapeParams["Body Center Y"] = pad2CenterPoint[1]
                    pad2Node.polylineShapeParams["Angle"] = geoms["Angle"] + np.pi
                    """+pi is so stem points the right way"""

                    # Add fingers if applicable
                    if qubit.fingers != {}:  # If fingers for either pad 1 or pad 2 are specified:
                        if "Pad 1" in qubit.fingers:
                            pad1Node.polylineShape += "PlusFinger(s)"
                            pad1Node.polylineShapeParams["Number of Fingers"] = qubit.fingers["Pad 1"]
                        if "Pad 2" in qubit.fingers:
                            pad2Node.polylineShape += "PlusFinger(s)"
                            pad2Node.polylineShapeParams["Number of Fingers"] = qubit.fingers["Pad 2"]
                        for padName, numFingers in qubit.fingers.items():
                            thisNode = None
                            if padName == "Pad 1":
                                thisNode = pad1Node
                            elif padName == "Pad 2":
                                thisNode = pad2Node
                            for fingerIndex in range(numFingers):
                                shapeParams = thisNode.polylineShapeParams
                                if numFingers > 1:
                                    shapeParams["Finger Spacing"] = geoms[padName + " Finger Spacing"]
                                else:
                                    shapeParams["Finger Spacing"] = 0
                                shapeParams["Finger " + str(fingerIndex) + " Stem Length"] = \
                                    geoms[padName + " Finger " + str(fingerIndex) + " Stem Length"]
                                shapeParams["Finger " + str(fingerIndex) + " Stem Width"] = \
                                    geoms[padName + " Finger " + str(fingerIndex) + " Stem Width"]
                                shapeParams["Finger Stem Boundary"] = geoms[padName + " Finger Stem Boundary"]
                                shapeParams["Finger " + str(fingerIndex) + " T Head Length"] = \
                                    geoms[padName + " Finger " + str(fingerIndex) + " T Head Length"]
                                shapeParams["Finger " + str(fingerIndex) + " T Width"] = \
                                    geoms[padName + " Finger " + str(fingerIndex) + " T Width"]
                                shapeParams["Finger " + str(fingerIndex) + " T Side 1 Boundary"] = \
                                    geoms[padName + " Finger " + str(fingerIndex) + " T Side 1 Boundary"]
                                shapeParams["Finger " + str(fingerIndex) + " T Side 2 Boundary"] = \
                                    geoms[padName + " Finger " + str(fingerIndex) + " T Side 2 Boundary"]
                                shapeParams["Finger " + str(fingerIndex) + " T Side 3 Boundary"] = \
                                    geoms[padName + " Finger " + str(fingerIndex) + " T Side 3 Boundary"]
                                shapeParams["Finger " + str(fingerIndex) + " T Side 4 Boundary"] = \
                                    geoms[padName + " Finger " + str(fingerIndex) + " T Side 4 Boundary"]
                    # JJ additions
                    if "singleJJ" in qubit.generalParamsDict["Type"]:
                        for pad in qubit.padListGeom:
                            pad.node.polylineShape += "PlusSingleJJ"
                        for i in [pad.node for pad in qubit.padListGeom]:
                            i.polylineShapeParams["JJ Stem Width"] = geoms["JJ Stem Width"]
                            i.polylineShapeParams["JJ Stem End Boundary"] = geoms["JJ Patch Length"] / 2
                            i.polylineShapeParams["JJ Stem Side Boundary"] = geoms["JJ Stem Boundary"]

                        pad1Node.polylineShapeParams["JJ Stem Length"] = ((padSpacing - geoms["JJ Patch Length"]) / 2
                                                                          - JJLoc_y)
                        pad2Node.polylineShapeParams["JJ Stem Length"] = ((padSpacing - geoms["JJ Patch Length"]) / 2
                                                                          + JJLoc_y)
                        if isinstance(qubit, GroundedQubit):
                            geoms["Pad 2 Width"] = geoms["JJ Stem Width"]

                        unrotatedCenter = [JJLoc_x, JJLoc_y]
                        rotatedCenter = rotate(unrotatedCenter, geoms["Angle"])
                        bottomElectrodeGDS, topElectrodeGDS, connectionsGDS, patchGDS = OtherComponents.JJGDSComponents(
                            top_electrode_width=geoms["JJ Top Electrode Width"],
                            bot_electrode_width=geoms["JJ Bottom Electrode Width"],
                            rotate=geoms["Angle"],
                            dx=rotatedCenter[0] + centerX,
                            dy=rotatedCenter[1] + centerY,
                            chip=chip.index,
                            patchLength=geoms["JJ Patch Length"]
                        )
                        qubit.JJGDSs.append(JJGDS(patchGDS, topElectrodeGDS, bottomElectrodeGDS, connectionsGDS))
                    elif "doubleJJ" in qubit.generalParamsDict["Type"]:
                        for pad in qubit.padListGeom:
                            pad.node.polylineShape += "PlusDoubleJJ"
                        pad1Node.polylineShapeParams["SQUID T Stem Length"] = (
                                padSpacing / 2
                                - geoms["JJ Patch Length"] / 2
                                - geoms["SQUID Stem Length"]
                                - geoms["SQUID T Head Length"]
                                - JJLoc_y
                        )
                        pad2Node.polylineShapeParams["SQUID T Stem Length"] = (
                                padSpacing / 2
                                - geoms["JJ Patch Length"] / 2
                                - geoms["SQUID Stem Length"]
                                - geoms["SQUID T Head Length"]
                                + JJLoc_y
                        )
                        if isinstance(qubit, GroundedQubit):
                            geoms["Pad 2 Width"] = geoms["SQUID T Stem Width"]
                        for i in [pad.node for pad in qubit.padListGeom]:
                            i.polylineShapeParams["SQUID Stem Separation"] = geoms["SQUID Stem Separation"]
                            i.polylineShapeParams["SQUID T Head Width"] = geoms["SQUID T Head Width"]
                            i.polylineShapeParams["SQUID T Head Length"] = geoms["SQUID T Head Length"]
                            i.polylineShapeParams["JJ Boundary"] = geoms["JJ Boundary"]
                            i.polylineShapeParams["SQUID Stem Width"] = geoms["SQUID Stem Width"]
                            i.polylineShapeParams["SQUID Stem Length"] = geoms["SQUID Stem Length"]
                            i.polylineShapeParams["SQUID T Stem Width"] = geoms["SQUID T Stem Width"]

                            # Left. Takes advantage of symmetry.
                            unrotatedCenter = [JJLoc_x + geoms["SQUID Stem Separation"] / 2, JJLoc_y]
                            rotatedCenter = rotate(unrotatedCenter, geoms["Angle"])
                            bottomElectrodeGDS, topElectrodeGDS, connectionsGDS, patchGDS = \
                                OtherComponents.JJGDSComponents(
                                    top_electrode_width=geoms["JJ Top Electrode Width"],
                                    bot_electrode_width=geoms["JJ Bottom Electrode Width"],
                                    rotate=geoms["Angle"],
                                    dx=rotatedCenter[0] + centerX,
                                    dy=rotatedCenter[1] + centerY,
                                    chip=chip.index,
                                    patchLength=geoms["JJ Patch Length"]
                                )
                            qubit.JJGDSs.append(JJGDS(patchGDS, topElectrodeGDS, bottomElectrodeGDS, connectionsGDS))
                            # Right
                            unrotatedCenter = [JJLoc_x - geoms["SQUID Stem Separation"] / 2, JJLoc_y]
                            rotatedCenter = rotate(unrotatedCenter, geoms["Angle"])
                            bottomElectrodeGDS, topElectrodeGDS, connectionsGDS, patchGDS = \
                                OtherComponents.JJGDSComponents(
                                    top_electrode_width=geoms["JJ Top Electrode Width"],
                                    bot_electrode_width=geoms["JJ Bottom Electrode Width"],
                                    rotate=geoms["Angle"],
                                    dx=rotatedCenter[0] + centerX,
                                    dy=rotatedCenter[1] + centerY,
                                    chip=chip.index,
                                    patchLength=geoms["JJ Patch Length"]
                                )
                            qubit.JJGDSs.append(JJGDS(patchGDS, topElectrodeGDS, bottomElectrodeGDS, connectionsGDS))
                    for pad in qubit.padListGeom:
                        pad.node.polylineShapeParams["Body Width"] = geoms["Pad " + str(pad.index) + " Width"]
                        pad.node.polylineShapeParams["Body Length"] = geoms["Pad " + str(pad.index) + " Length"]
                        pad.node.height = geoms["Pad " + str(pad.index) + " Height"]
                        for side in [1, 2, 3, 4]:
                            pad.node.polylineShapeParams["Side " + str(side) + " Boundary"] = \
                                geoms["Pad " + str(pad.index) + " Side " + str(side) + " Boundary"]
                # Common to all qubit geometries
                for qubitPad in qubit.padListGeom:
                    qubitPad.node.polylineShapeParams["Mesh Boundary"] = self.sysParams["Anti-Vortex Mesh Boundary"]
                    qubitPad.node.updatePolylines()
                    # Z values
                    if chipIndex == 0:
                        qubitPad.node.Z = self.chipDict[0].substrate.node.height
                    elif chipIndex == 1:
                        qubitPad.node.Z = self.chipDict[1].substrate.node.Z - qubitPad.node.height
            # Readout Resonators
            for readoutResonatorIndex, readoutResonator in chip.readoutResonatorDict.items():
                readoutResonator.geometryParamsDict = readSingleRowData(fileLines, readoutResonator.name)
                geoms = readoutResonator.geometryParamsDict
                pad1Node = readoutResonator.pad1.node
                pad2Node = readoutResonator.pad2.node
                # Z values
                for resonatorPadNode in [pad1Node, pad2Node]:
                    if chipIndex == 0:
                        resonatorPadNode.Z = self.chipDict[0].substrate.node.height
                    elif chipIndex == 1:
                        resonatorPadNode.Z = self.chipDict[1].substrate.node.Z - resonatorPadNode.height
                # Mesh boundary
                pad1Node.polylineShapeParams["Mesh Boundary"] = self.sysParams["Anti-Vortex Mesh Boundary"]
                pad2Node.polylineShapeParams["Mesh Boundary"] = self.sysParams["Anti-Vortex Mesh Boundary"]
                # Meanders
                readoutResonator.updateMeanderNode(self.CPW)
                # Height
                pad1Node.height = geoms["Pad 1 Height"]
                pad2Node.height = geoms["Pad 2 Height"]
                # Pad Polylines
                pad1Node.polylineShape = "rectangle-PlusFinger(s)"
                pad2Node.polylineShape = "rectangle-PlusFinger(s)"
                pad1Node.polylineShapeParams["Number of Fingers"] = 1
                pad2Node.polylineShapeParams["Number of Fingers"] = 1

                pad1RealCenterPoint = translate(
                    rotate(
                        [0, geoms["Pad 1 Length"] / 2 + geoms["Pad T Stem Length"]],
                        readoutResonator.meanderStartAngle + np.pi / 2
                    ),
                    readoutResonator.meanderStartPoint[0],
                    readoutResonator.meanderStartPoint[1]
                )
                pad2RealCenterPoint = translate(
                    rotate(
                        [0, geoms["Pad 2 Length"] / 2 + geoms["Pad T Stem Length"]],
                        readoutResonator.meanderEndAngle + 3 * np.pi / 2),
                    readoutResonator.meanderEndPoint[0],
                    readoutResonator.meanderEndPoint[1]
                )

                pad1Node.polylineShapeParams["Body Center X"] = pad1RealCenterPoint[0]
                pad1Node.polylineShapeParams["Body Center Y"] = pad1RealCenterPoint[1]
                pad1Node.polylineShapeParams["Angle"] = (readoutResonator.meanderStartAngle + 3 * np.pi / 2)
                pad2Node.polylineShapeParams["Body Center X"] = pad2RealCenterPoint[0]
                pad2Node.polylineShapeParams["Body Center Y"] = pad2RealCenterPoint[1]
                pad2Node.polylineShapeParams["Angle"] = readoutResonator.meanderEndAngle + np.pi / 2

                pad1Node.polylineShapeParams["Body Width"] = geoms["Pad 1 Width"]
                pad1Node.polylineShapeParams["Body Length"] = geoms["Pad 1 Length"]
                pad1Node.polylineShapeParams["Body Height"] = geoms["Pad 1 Height"]
                pad1Node.polylineShapeParams["Side 1 Boundary"] = geoms["Pad 1 Side 1 Boundary"]
                pad1Node.polylineShapeParams["Side 2 Boundary"] = geoms["Pad 1 Side 2 Boundary"]
                pad1Node.polylineShapeParams["Side 3 Boundary"] = geoms["Pad 1 Side 3 Boundary"]
                pad1Node.polylineShapeParams["Side 4 Boundary"] = geoms["Pad 1 Side 4 Boundary"]

                # pad2Params=[param for param in geoms if param[0:5]=="Pad 2"]
                pad2Node.polylineShapeParams["Body Width"] = geoms["Pad 2 Width"]
                pad2Node.polylineShapeParams["Body Length"] = geoms["Pad 2 Length"]
                pad2Node.polylineShapeParams["Body Height"] = geoms["Pad 2 Height"]
                pad2Node.polylineShapeParams["Side 1 Boundary"] = geoms["Pad 2 Side 1 Boundary"]
                pad2Node.polylineShapeParams["Side 2 Boundary"] = geoms["Pad 2 Side 2 Boundary"]
                pad2Node.polylineShapeParams["Side 3 Boundary"] = geoms["Pad 2 Side 3 Boundary"]
                pad2Node.polylineShapeParams["Side 4 Boundary"] = geoms["Pad 2 Side 4 Boundary"]

                # Pad T
                for thisNode in [pad1Node, pad2Node]:
                    shapeParams = thisNode.polylineShapeParams
                    shapeParams["Finger Spacing"] = 0
                    shapeParams["Finger 0 Stem Length"] = geoms["Pad T Stem Length"] / 2
                    shapeParams["Finger 0 Stem Width"] = self.CPW.geometryParamsDict["Width"]
                    shapeParams["Finger Stem Boundary"] = self.CPW.geometryParamsDict["Gap"]
                    shapeParams["Finger 0 T Head Length"] = geoms["Pad T Stem Length"] / 2
                    shapeParams["Finger 0 T Width"] = self.CPW.geometryParamsDict["Width"]
                    shapeParams["Finger 0 T Side 1 Boundary"] = self.CPW.geometryParamsDict["Gap"]
                    shapeParams["Finger 0 T Side 2 Boundary"] = 1
                    shapeParams["Finger 0 T Side 3 Boundary"] = self.CPW.geometryParamsDict["Gap"]
                    shapeParams["Finger 0 T Side 4 Boundary"] = 1

                pad1Node.updatePolylines()
                pad2Node.updatePolylines()
                # PTCs
            for PTCIndex, PTC in chip.PTCDict.items():
                PTC.geometryParamsDict = readSingleRowData(fileLines, PTC.name)
                geoms = PTC.geometryParamsDict
                pad1Node = PTC.pad1.node
                pad2Node = PTC.pad2.node
                # Height
                pad1Node.height = geoms["Height"]
                pad2Node.height = geoms["Height"]
                # Polylines
                pad1Node.polylineShape = "rectangle-PlusDoubleJJ"
                pad2Node.polylineShape = "rectangle-PlusDoubleJJ-sideT"
                pad1BodyLength = 0.0001  # The "body" here is just an artifact of the rectangle-plusDoubleJJ shape.
                squidTStemLength = geoms["SQUID T Stem Length"]
                padSpacing = (2 * geoms["SQUID Stem Length"]
                              + geoms["SQUID Patch Length"]
                              + 2 * geoms["SQUID T Head Length"]
                              + 2 * squidTStemLength)
                PTCNormalizedSquidCenter = [0, -geoms["End Separation"] / 2 - pad1BodyLength - padSpacing / 2]
                PTCSQUIDCenter = translate(rotate(PTCNormalizedSquidCenter, geoms["Angle"]),
                                           geoms["Center X"],
                                           geoms["Center Y"])
                # For SQUIDPad[N]NormalizedCenterPoint, the center is at the center of the squid.
                SQUIDPad1NormalizedCenterPoint = [0, padSpacing / 2 + pad1BodyLength / 2]
                pad1CenterPoint = translate(rotate(SQUIDPad1NormalizedCenterPoint, geoms["Angle"]),
                                            PTCSQUIDCenter[0],
                                            PTCSQUIDCenter[1])

                pad1Node.polylineShapeParams["Body Center X"] = pad1CenterPoint[0]
                pad1Node.polylineShapeParams["Body Center Y"] = pad1CenterPoint[1]
                pad1Node.polylineShapeParams["Angle"] = geoms["Angle"]
                pad1Node.polylineShapeParams["Body Width"] = self.CPW.geometryParamsDict["Width"]
                pad1Node.polylineShapeParams["Body Length"] = pad1BodyLength
                pad1Node.polylineShapeParams["Body Height"] = geoms["Height"]
                pad1Node.polylineShapeParams["Side 1 Boundary"] = self.CPW.geometryParamsDict["Gap"]
                pad1Node.polylineShapeParams["Side 2 Boundary"] = 0
                pad1Node.polylineShapeParams["Side 3 Boundary"] = self.CPW.geometryParamsDict["Gap"]
                pad1Node.polylineShapeParams["Side 4 Boundary"] = 0
                pad1Node.polylineShapeParams["JJ Stem X"] = 0

                SQUIDPad2NormalizedCenterPoint = [0, -padSpacing / 2 - geoms["SQUID Bar Length"] / 2]
                pad2CenterPoint = translate(rotate(SQUIDPad2NormalizedCenterPoint, geoms["Angle"]),
                                            PTCSQUIDCenter[0],
                                            PTCSQUIDCenter[1])
                pad2Node.polylineShapeParams["Body Center X"] = pad2CenterPoint[0]
                pad2Node.polylineShapeParams["Body Center Y"] = pad2CenterPoint[1]
                pad2Node.polylineShapeParams["Angle"] = geoms["Angle"] + np.pi
                """addition of pi is so the stem points the right way."""
                pad2Node.polylineShapeParams["Body Width"] = geoms["SQUID Bar Width"]
                pad2Node.polylineShapeParams["Body Length"] = geoms["SQUID Bar Length"]
                pad2Node.polylineShapeParams["Body Height"] = geoms["Height"]
                pad2Node.polylineShapeParams["Side 1 Boundary"] = geoms["SQUID Bar Boundary"]
                pad2Node.polylineShapeParams["Side 2 Boundary"] = geoms["SQUID Bar Boundary"]
                pad2Node.polylineShapeParams["Side 3 Boundary"] = geoms["SQUID Bar Boundary"]
                pad2Node.polylineShapeParams["Side 4 Boundary"] = geoms["SQUID Bar Boundary"]
                pad2Node.polylineShapeParams["JJ Stem X"] = 0
                pad2Node.polylineShapeParams["Side T Width"] = geoms["SQUID Bar T Width"]
                pad2Node.polylineShapeParams["Side T Length"] = geoms["SQUID Bar T Length"]
                pad2Node.polylineShapeParams["Side T Boundary"] = geoms["SQUID Bar T Boundary"]
                for i in [pad1Node, pad2Node]:
                    i.polylineShapeParams["SQUID Stem Separation"] = geoms["SQUID Stem Separation"]
                    i.polylineShapeParams["SQUID T Head Width"] = geoms["SQUID T Head Width"]
                    i.polylineShapeParams["SQUID T Head Length"] = geoms["SQUID T Head Length"]
                    i.polylineShapeParams["JJ Boundary"] = geoms["SQUID Boundary"]
                    i.polylineShapeParams["SQUID Stem Width"] = geoms["SQUID Stem Width"]
                    i.polylineShapeParams["SQUID Stem Length"] = geoms["SQUID Stem Length"]
                    i.polylineShapeParams["SQUID T Stem Width"] = self.CPW.geometryParamsDict["Width"]
                    i.polylineShapeParams["SQUID T Stem Length"] = squidTStemLength
                # Left.
                unrotatedCenter = [-geoms["SQUID Stem Separation"] / 2, 0]
                rotatedCenter = rotate(unrotatedCenter, geoms["Angle"])
                bottomElectrodeGDS, topElectrodeGDS, connectionsGDS, patchGDS = OtherComponents.JJGDSComponents(
                    top_electrode_width=geoms["JJ Top Electrode Width"],
                    bot_electrode_width=geoms["JJ Bottom Electrode Width"],
                    rotate=geoms["Angle"],
                    dx=rotatedCenter[0] + PTCSQUIDCenter[0],
                    dy=rotatedCenter[1] + PTCSQUIDCenter[1],
                    chip=chip.index,
                    patchLength=geoms["SQUID Patch Length"]
                )
                PTC.JJGDSs.append(JJGDS(patchGDS, topElectrodeGDS, bottomElectrodeGDS, connectionsGDS))
                # Right
                unrotatedCenter = [geoms["SQUID Stem Separation"] / 2, 0]
                rotatedCenter = rotate(unrotatedCenter, geoms["Angle"])
                bottomElectrodeGDS, topElectrodeGDS, connectionsGDS, patchGDS = OtherComponents.JJGDSComponents(
                    top_electrode_width=geoms["JJ Top Electrode Width"],
                    bot_electrode_width=geoms["JJ Bottom Electrode Width"],
                    rotate=geoms["Angle"],
                    dx=rotatedCenter[0] + PTCSQUIDCenter[0],
                    dy=rotatedCenter[1] + PTCSQUIDCenter[1],
                    chip=chip.index,
                    patchLength=geoms["SQUID Patch Length"]
                )
                PTC.JJGDSs.append(JJGDS(patchGDS, topElectrodeGDS, bottomElectrodeGDS, connectionsGDS))

                # Mesh
                pad1Node.polylineShapeParams["Mesh Boundary"] = self.sysParams["Anti-Vortex Mesh Boundary"]
                pad2Node.polylineShapeParams["Mesh Boundary"] = self.sysParams["Anti-Vortex Mesh Boundary"]
                pad1Node.updatePolylines()
                pad2Node.updatePolylines()
                # Z values
                for PTCPadNode in [pad1Node, pad2Node]:
                    if chipIndex == 0:
                        PTCPadNode.Z = self.chipDict[0].substrate.node.height
                    elif chipIndex == 1:
                        PTCPadNode.Z = self.chipDict[1].substrate.node.Z - PTCPadNode.height

                        # Meanders
                PTC_CPW = CPW()
                PTC_CPW.geometryParamsDict["Width"] = geoms["CPW Width"]
                PTC_CPW.geometryParamsDict["Gap"] = geoms["CPW Gap"]

                PTC.updateMeanderNode(PTC_CPW)
            # Straight Bus Couplers
            for straightBusCouplerIndex, straightBusCoupler in chip.straightBusCouplerDict.items():
                straightBusCoupler.geometryParamsDict = readSingleRowData(fileLines, straightBusCoupler.name)
                geoms = straightBusCoupler.geometryParamsDict
                pad1Node = straightBusCoupler.pad1.node
                pad2Node = straightBusCoupler.pad2.node
                # Height
                pad1Node.height = geoms["Height"]
                pad2Node.height = geoms["Height"]
                # Polyline Shape
                pad1Node.polylineShape = "rectangle-PlusFinger(s)"
                pad2Node.polylineShape = "rectangle-PlusFinger(s)"
                pad1Node.polylineShapeParams["Number of Fingers"] = 1
                pad2Node.polylineShapeParams["Number of Fingers"] = 1
                # Base Rectangle
                pad1NormalizedCenterPoint = [0, (geoms["SQUID Patch Length"] / 2
                                                 + geoms["SQUID Stem Length"]
                                                 + geoms["SQUID T Head Length"]
                                                 + geoms["SQUID T Stem Length"]
                                                 + geoms["End Length"] / 2
                                                 )
                                             ]
                pad1CenterPoint = translate(rotate(pad1NormalizedCenterPoint, geoms["Angle"]),
                                            geoms["Center X"],
                                            geoms["Center Y"])

                pad1Node.polylineShapeParams["Body Center X"] = pad1CenterPoint[0]
                pad1Node.polylineShapeParams["Body Center Y"] = pad1CenterPoint[1]
                pad1Node.polylineShapeParams["Angle"] = geoms["Angle"]
                pad1Node.polylineShapeParams["Body Width"] = geoms["End Width"]
                pad1Node.polylineShapeParams["Body Length"] = geoms["End Length"]
                pad1Node.polylineShapeParams["Body Height"] = geoms["Height"]
                pad1Node.polylineShapeParams["Side 1 Boundary"] = geoms["End Boundary"]
                pad1Node.polylineShapeParams["Side 2 Boundary"] = 0
                pad1Node.polylineShapeParams["Side 3 Boundary"] = geoms["End Boundary"]
                pad1Node.polylineShapeParams["Side 4 Boundary"] = 0
                pad1Node.polylineShapeParams["JJ Stem X"] = 0

                pad2NormalizedCenterPoint = [0, (-geoms["SQUID Patch Length"] / 2
                                                 - geoms["SQUID Stem Length"]
                                                 - geoms["SQUID T Head Length"]
                                                 - geoms["SQUID T Stem Length"]
                                                 - geoms["End Length"] / 2
                                                 )
                                             ]
                pad2CenterPoint = translate(rotate(pad2NormalizedCenterPoint, geoms["Angle"]),
                                            geoms["Center X"],
                                            geoms["Center Y"])
                pad2Node.polylineShapeParams["Body Center X"] = pad2CenterPoint[0]
                pad2Node.polylineShapeParams["Body Center Y"] = pad2CenterPoint[1]
                pad2Node.polylineShapeParams["Angle"] = geoms["Angle"] + np.pi
                pad2Node.polylineShapeParams["Body Width"] = geoms["End Width"]
                pad2Node.polylineShapeParams["Body Length"] = geoms["End Length"]
                pad2Node.polylineShapeParams["Body Height"] = geoms["Height"]
                pad2Node.polylineShapeParams["Side 1 Boundary"] = geoms["End Boundary"]
                pad2Node.polylineShapeParams["Side 2 Boundary"] = 0
                pad2Node.polylineShapeParams["Side 3 Boundary"] = geoms["End Boundary"]
                pad2Node.polylineShapeParams["Side 4 Boundary"] = 0
                pad2Node.polylineShapeParams["JJ Stem X"] = 0

                fingerStemLength = (geoms["Total Length"]
                                    - 4 * geoms["End Length"]
                                    - geoms["SQUID Patch Length"]
                                    - 2 * geoms["SQUID Stem Length"]
                                    - 2 * geoms["SQUID T Head Length"]
                                    - 2 * geoms["SQUID T Stem Length"]) / 2

                for thisNode in [pad1Node, pad2Node]:
                    shapeParams = thisNode.polylineShapeParams
                    shapeParams["Finger Spacing"] = 0
                    shapeParams["Finger 0 Stem Length"] = fingerStemLength
                    shapeParams["Finger 0 Stem Width"] = geoms["Body Width"]
                    shapeParams["Finger Stem Boundary"] = geoms["Body Boundary"]
                    shapeParams["Finger 0 T Head Length"] = geoms["End Length"]
                    shapeParams["Finger 0 T Width"] = geoms["End Width"]
                    shapeParams["Finger 0 T Side 1 Boundary"] = 0
                    shapeParams["Finger 0 T Side 2 Boundary"] = 0
                    shapeParams["Finger 0 T Side 3 Boundary"] = 0
                    shapeParams["Finger 0 T Side 4 Boundary"] = 0
                # JJ additions
                pad1Node.polylineShape += "PlusDoubleJJ"
                pad2Node.polylineShape += "PlusDoubleJJ"
                for i in [pad1Node, pad2Node]:
                    i.polylineShapeParams["SQUID Stem Separation"] = geoms["SQUID Stem Separation"]
                    i.polylineShapeParams["SQUID T Head Width"] = geoms["SQUID T Head Width"]
                    i.polylineShapeParams["SQUID T Head Length"] = geoms["SQUID T Head Length"]
                    i.polylineShapeParams["JJ Boundary"] = geoms["SQUID Boundary"]
                    i.polylineShapeParams["SQUID Stem Width"] = geoms["SQUID Stem Width"]
                    i.polylineShapeParams["SQUID Stem Length"] = geoms["SQUID Stem Length"]
                    i.polylineShapeParams["SQUID T Stem Width"] = geoms["SQUID T Stem Width"]
                    i.polylineShapeParams["SQUID T Stem Length"] = geoms["SQUID T Stem Length"]
                # Left. Takes advantage of symmetry. May need to be generalized if an off-symmetric JJ is needed.
                unrotatedCenter = [geoms["SQUID Stem Separation"] / 2, 0]
                rotatedCenter = rotate(unrotatedCenter, geoms["Angle"])
                bottomElectrodeGDS, topElectrodeGDS, connectionsGDS, patchGDS = OtherComponents.JJGDSComponents(
                    top_electrode_width=geoms["JJ Top Electrode Width"],
                    bot_electrode_width=geoms["JJ Bottom Electrode Width"],
                    rotate=geoms["Angle"],
                    dx=rotatedCenter[0] + geoms["Center X"],
                    dy=rotatedCenter[1] + geoms["Center Y"],
                    chip=chip.index,
                    patchLength=geoms["SQUID Patch Length"]
                )
                straightBusCoupler.JJGDSs.append(JJGDS(patchGDS, topElectrodeGDS, bottomElectrodeGDS, connectionsGDS))
                # Right
                unrotatedCenter = [-geoms["SQUID Stem Separation"] / 2, 0]
                rotatedCenter = rotate(unrotatedCenter, geoms["Angle"])
                bottomElectrodeGDS, topElectrodeGDS, connectionsGDS, patchGDS = OtherComponents.JJGDSComponents(
                    top_electrode_width=geoms["JJ Top Electrode Width"],
                    bot_electrode_width=geoms["JJ Bottom Electrode Width"],
                    rotate=geoms["Angle"],
                    dx=rotatedCenter[0] + geoms["Center X"],
                    dy=rotatedCenter[1] + geoms["Center Y"],
                    chip=chip.index,
                    patchLength=geoms["SQUID Patch Length"]
                )
                straightBusCoupler.JJGDSs.append(JJGDS(patchGDS, topElectrodeGDS, bottomElectrodeGDS, connectionsGDS))
                # Common to all straightBusCoupler geometries
                for node in [pad1Node, pad2Node]:
                    node.polylineShapeParams["Mesh Boundary"] = self.sysParams["Anti-Vortex Mesh Boundary"]

                pad1Node.updatePolylines()
                pad2Node.updatePolylines()
                # Z values
                for node in [pad1Node, pad2Node]:
                    if chipIndex == 0:
                        node.Z = self.chipDict[0].substrate.node.height
                    elif chipIndex == 1:
                        node.Z = self.chipDict[1].substrate.node.Z - straightBusCouplerNode.height
            # Control Lines
            for controlLineIndex, controlLine in chip.controlLineDict.items():
                controlLine.geometryParamsDict = readSingleRowData(fileLines, controlLine.name)
                geoms = controlLine.geometryParamsDict
                lineNode = controlLine.lineNode
                # Height
                lineNode.height = self.CPW.geometryParamsDict["Height"]
                # Path Polyline
                lineNode.polylineShape = "path"
                lineNode.polylineShapeParams["CPW"] = self.CPW
                lineNode.polylineShapeParams["Mesh Boundary"] = self.sysParams["Anti-Vortex Mesh Boundary"]
                for param in geoms:
                    lineNode.polylineShapeParams[param] = geoms[param]
                lineNode.updatePolylines()
                # Drive line option
                if controlLine.generalParamsDict["Type"] == "drive":
                    loopCutout1Width = geoms["End Gap"]
                    loopCutout1Length = self.CPW.geometryParamsDict["Width"] + 2 * self.CPW.geometryParamsDict["Gap"]
                    loopCutout1RawCenter = [loopCutout1Width / 2 - traceBuffer,
                                            0]  # Raw=assuming path endpoint is at [0,0]
                    loopCutout1RawPolyline = rectanglePolyline(
                        centerX=loopCutout1RawCenter[0],
                        centerY=loopCutout1RawCenter[1],
                        width=loopCutout1Width,
                        length=loopCutout1Length,
                        angle=0
                    )
                    loopCutout1RotatedPolyline = [rotate(point, lineNode.endAngle) for point in loopCutout1RawPolyline]
                    loopCutout1TranslatedPolyline = [translate(point, lineNode.endPoint[0], lineNode.endPoint[1])
                                                     for point in loopCutout1RotatedPolyline]
                    lineNode.peripheryPolylines.append(loopCutout1TranslatedPolyline)
                # Flux bias option
                if controlLine.generalParamsDict["Type"] == "fluxBias":
                    loopThickness = geoms["loopThickness"]
                    loopSeg1Length = geoms["loopSeg1Length"]
                    loopSeg2Length = geoms["loopSeg2Length"]
                    loopSeg3Length = geoms["loopSeg3Length"]
                    loopSeg1Boundary = geoms["loopSeg1Boundary"]
                    loopSeg2Boundary = geoms["loopSeg2Boundary"]
                    loopSeg3Boundary = geoms["loopSeg3Boundary"]

                    loopCutout1Width = loopSeg1Length
                    loopCutout1Length = loopSeg1Boundary + loopSeg2Length - loopThickness
                    """Raw=assuming path endpoint is at [0,0]"""
                    loopCutout1RawCenter = [
                        loopCutout1Width / 2 - traceBuffer,
                        - (
                                loopSeg2Length
                                - loopThickness
                                - loopCutout1Length / 2
                                - self.CPW.geometryParamsDict["Width"] / 2
                        )
                    ]
                    loopCutout1RawPolyline = rectanglePolyline(
                        centerX=loopCutout1RawCenter[0],
                        centerY=loopCutout1RawCenter[1],
                        width=loopCutout1Width,
                        length=loopCutout1Length,
                        angle=0
                    )
                    loopCutout1RotatedPolyline = [rotate(point, lineNode.endAngle) for point in loopCutout1RawPolyline]
                    loopCutout1TranslatedPolyline = [translate(point, lineNode.endPoint[0], lineNode.endPoint[1])
                                                     for point in loopCutout1RotatedPolyline]
                    lineNode.peripheryPolylines.append(loopCutout1TranslatedPolyline)

                    loopCutout2Width = loopSeg3Length + loopSeg2Boundary
                    loopCutout2Length = loopSeg2Length + loopSeg1Boundary + loopSeg3Boundary
                    loopCutout2RawCenter = [
                        loopSeg1Length - loopSeg3Length + loopCutout2Width / 2,
                        (
                                -loopCutout2Length / 2
                                + self.CPW.geometryParamsDict["Width"] / 2
                                + loopSeg1Boundary
                        )
                    ]
                    loopCutout2RawPolyline = rectanglePolyline(
                        centerX=loopCutout2RawCenter[0],
                        centerY=loopCutout2RawCenter[1],
                        width=loopCutout2Width,
                        length=loopCutout2Length,
                        angle=0
                    )
                    loopCutout2RotatedPolyline = [rotate(point, lineNode.endAngle) for point in loopCutout2RawPolyline]
                    loopCutout2TranslatedPolyline = [
                        translate(point, lineNode.endPoint[0], lineNode.endPoint[1])
                        for point in loopCutout2RotatedPolyline
                    ]
                    lineNode.peripheryPolylines.append(loopCutout2TranslatedPolyline)
                    # Loop
                    insertIndex = int(len(lineNode.polyline) / 2 - 1)  # -1 is for the short to ground
                    seg3Buffer = 0  # May be needed when generating GDS
                    loopSeg3Length += seg3Buffer

                    # point1 = lineNode.polyline[insertIndex]
                    # point2 = lineNode.polyline[insertIndex]
                    shortThickness = loopThickness
                    shortLength = self.CPW.geometryParamsDict["Gap"]
                    # shortPoint = [point2[0] - shortThickness * np.cos(lineNode.endAngle),
                    #               point2[1] - shortThickness * np.sin(lineNode.endAngle)]

                    loopPolylineRaw = [
                        [-shortThickness, 0],
                        [-shortThickness, shortLength],
                        [0, shortLength],
                        [0, 0],
                        [loopSeg1Length, 0],
                        [loopSeg1Length, -loopSeg2Length],
                        [loopSeg1Length - loopSeg3Length, -loopSeg2Length],
                        [loopSeg1Length - loopSeg3Length, -loopSeg2Length + loopThickness],
                        [loopSeg1Length - loopThickness, -loopSeg2Length + loopThickness],
                        [loopSeg1Length - loopThickness, -loopThickness],
                        [0, -loopThickness]
                    ]
                    loopPolylineRotated = [rotate(point, lineNode.endAngle) for point in loopPolylineRaw]
                    traceEdgePoint = translate(rotate([0, self.CPW.geometryParamsDict["Width"] / 2], lineNode.endAngle),
                                               lineNode.endPoint[0], lineNode.endPoint[1])
                    loopPolylineTranslated = [translate(point, traceEdgePoint[0], traceEdgePoint[1])
                                              for point in loopPolylineRotated]
                    lineNode.polyline = (lineNode.polyline[0:insertIndex]
                                         + loopPolylineTranslated
                                         + lineNode.polyline[insertIndex + 1:])
                    """Plus one is because the corner point is included in loopPolylineRaw"""

                # Z values
                if chipIndex == 0:
                    lineNode.Z = self.chipDict[0].substrate.node.height
                elif chipIndex == 1:
                    lineNode.Z = self.chipDict[1].substrate.node.Z - straightBusCouplerPadNode.height
                # Launch pads
                controlLine.updateLaunchPadNodes()
        # If flip chip update bump nodes
        if self.sysParams["Flip Chip?"] == "Yes":
            self.updateBumpsDict()

    def loadDesignFiles(self):
        self.loadComponentParams()
        self.loadGeometries()
        self.CPW.vp = self.CPW.generalParamsDict["Phase Velocity(um/s)"]

    def generateGDS(self):
        self.loadDesignFiles()
        Main = gdspy.Cell('Main')
        unitChange = 1  # Convert if necessary.
        for chipIndex, chip in self.chipDict.items():
            # Lists of GDS items to either add or subtract
            peripheries = []  # List of polygons to subtract from GND
            components = []  # List of polygons to add to GND
            meshPeripheries = []
            addToMain = []
            subtractFromGround = []
            chipWidth = chip.substrate.geometryParamsDict["Width"] * unitChange
            chipLength = chip.substrate.geometryParamsDict["Length"] * unitChange

            # Add all components
            for node in self.getChipNNodes(chip.index):  # Add all nodes
                components.append(node.polyline)
                peripheries = peripheries + node.peripheryPolylines
                meshPeripheries = meshPeripheries + node.meshPeripheryPolylines
            for component in components:
                addToMain.append(gdspy.Polygon(multiplyPolyline(component, unitChange), layer=chip.index))
            for periphery in peripheries:
                subtractFromGround.append(gdspy.Polygon(multiplyPolyline(periphery, unitChange), layer=chip.index))
            # Dice Gap
            diceGap = OtherComponents.create_dice_gap(
                chip_size_x=chip.substrate.geometryParamsDict["Width"] * unitChange,
                chip_size_y=chip.substrate.geometryParamsDict["Length"] * unitChange)
            subtractFromGround.append(diceGap)
            # Chip Markers
            if self.sysParams["Chip Markers"] == "Pappas":
                chipMarkers = OtherComponents.createPappasMarkers(
                    chip_size_x=chip.substrate.geometryParamsDict["Width"] * unitChange,
                    chip_size_y=chip.substrate.geometryParamsDict["Length"] * unitChange)
                subtractFromGround.append(chipMarkers)
            elif self.sysParams["Chip Markers"] == "Schmidt":
                periphery1, marker1, periphery2, marker2 = OtherComponents.import_schmidtMarker()  # 1/2 denote layers.
                marker = None
                periphery = None
                if chip.index == 0:
                    marker = marker1
                    periphery = periphery1
                elif chip.index == 1:
                    marker = marker2
                    periphery = periphery2
                shiftX = self.chipDict[0].substrate.geometryParamsDict["Width"] / 2 * unitChange
                shiftY = self.chipDict[0].substrate.geometryParamsDict["Length"] / 2 * unitChange
                if self.sysParams["Flip Chip?"] == "Yes":
                    shiftX = self.chipDict[1].substrate.geometryParamsDict["Width"] / 2 * unitChange
                    shiftY = self.chipDict[1].substrate.geometryParamsDict["Length"] / 2 * unitChange

                markerCorners = [gdspy.copy(marker)] * 4
                markerCornerPeripheries = [gdspy.copy(periphery)] * 4

                buffer = 250 * unitChange

                markerCorners[0].translate(-shiftX + buffer, shiftY - buffer)
                markerCorners[1].translate(shiftX - buffer, shiftY - buffer)
                markerCorners[2].translate(shiftX - buffer, -shiftY + buffer)
                markerCorners[3].translate(-shiftX + buffer, -shiftY + buffer)

                markerCornerPeripheries[0].translate(-shiftX + buffer, shiftY - buffer)
                markerCornerPeripheries[1].translate(shiftX - buffer, shiftY - buffer)
                markerCornerPeripheries[2].translate(shiftX - buffer, -shiftY + buffer)
                markerCornerPeripheries[3].translate(-shiftX + buffer, -shiftY + buffer)

                for markerIndex, markerCorner in enumerate(markerCorners):
                    markerCorner.layers = [chip.index] * len(markerCorner.layers)
                    marker_cell = gdspy.Cell("Marker" + str(markerIndex) + "Chip" + str(chip.index))
                    subtractFromGround.append(markerCornerPeripheries[markerIndex])
                    marker_cell.add(markerCorners[markerIndex])
                    addToMain.append(gdspy.CellReference(marker_cell))
            # Nist Logo
            if chip.index == 0:
                nist_logo_periphery, nist_logo = OtherComponents.import_nist_logo()
                for obj in [nist_logo, nist_logo_periphery]:
                    obj.translate(self.chipDict[chip.index].nistLogoCenter[0] * unitChange,
                                  self.chipDict[chip.index].nistLogoCenter[1] * unitChange)
                nist_logo.layers = [chip.index] * 77
                NIST_logo_cell = gdspy.Cell('NIST logo')
                subtractFromGround.append(nist_logo_periphery)
                NIST_logo_cell.add(nist_logo)
                addToMain.append(gdspy.CellReference(NIST_logo_cell))
            # Description. May have mesh holes in it.
            descriptionText = gdspy.Text(self.sysParams["Chip Description"], 100 * unitChange,
                                         self.chipDict[0].chipDescriptionStart)
            subtractFromGround.append(descriptionText)

            # Draw mesh
            if self.sysParams["Add Mesh to GDS?"] == "Yes":
                # meshContainer=gdspy.Cell((-chipWidth/2,-chipLength/2),(chipWidth/2,chipLength/2),layer=chip.index+2)
                size = self.sysParams["Anti-Vortex Mesh Size"] * unitChange
                chipBorder = 150
                for xVal in np.arange(-chipWidth / 2 + chipBorder, chipWidth / 2 - chipBorder,
                                      self.sysParams["Anti-Vortex Mesh Spacing"] * unitChange):
                    for yVal in np.arange(-chipLength / 2 + chipBorder, chipLength / 2 - chipBorder,
                                          self.sysParams["Anti-Vortex Mesh Spacing"] * unitChange):
                        exclude = "No"
                        for meshPeriphery in meshPeripheries:
                            if pointInPolyline([xVal, yVal], meshPeriphery):
                                exclude = "Yes"
                        if exclude == "No":
                            Main.add(gdspy.Rectangle(
                                (xVal - size / 2, yVal - size / 2),
                                (xVal + size / 2, yVal + size / 2),
                                layer=chip.index + 2
                            ))
            # Create ground plane
            if self.sysParams["Invert GDS?"] == "No":
                GND = gdspy.Rectangle((-chipWidth / 2, -chipLength / 2), (chipWidth / 2, chipLength / 2),
                                      layer=chip.index)
                for item in subtractFromGround:
                    GND = gdspy.fast_boolean(GND, item, 'not', layer=chip.index)
                for item in addToMain:
                    Main.add(item)
            else:
                GND = gdspy.Cell("invertedGround" + str(chip.index))
                for item in subtractFromGround:
                    GND.add(item)
                for item in addToMain:
                    GND = gdspy.fast_boolean(GND, item, 'not', layer=chip.index)
                Main.add(GND)
            JJGDSList = []
            for qubitIndex, qubit in self.chipDict[chip.index].qubitDict.items():  # Add the JJ components
                JJGDSList = JJGDSList + qubit.JJGDSs
            for PTCIndex, PTC in self.chipDict[chip.index].PTCDict.items():
                JJGDSList = JJGDSList + PTC.JJGDSs
            for straightBusCouplerIndex, straightBusCoupler in self.chipDict[chip.index].straightBusCouplerDict.items():
                JJGDSList = JJGDSList + straightBusCoupler.JJGDSs
            for thisJJGDS in JJGDSList:
                Main.add(thisJJGDS.patchGDS)
                patchCopy = gdspy.copy(thisJJGDS.patchGDS)
                patchCopy.layers = [chip.index]
                Main.add(patchCopy)
                Main.add(thisJJGDS.topElectrodeGDS)
                Main.add(thisJJGDS.bottomElectrodeGDS)
                Main.add(thisJJGDS.connectionsGDS)

            Main.add(GND)
        # Add bumps if flip chip
        if self.sysParams["Flip Chip?"] == "Yes":
            for bump in self.bumpsDict["Bumps"]:
                Main.add(gdspy.Polygon(multiplyPolyline(bump.underBumpBottomNode.polyline, unitChange),
                                       layer=3))  # Bottom chip underbump
                Main.add(gdspy.Polygon(multiplyPolyline(bump.bumpMetalBottomNode.polyline, unitChange),
                                       layer=4))  # Bottom chip bump metal
                Main.add(gdspy.Polygon(multiplyPolyline(bump.bumpMetalTopNode.polyline, unitChange),
                                       layer=5))  # Top chip bump metal
                Main.add(gdspy.Polygon(multiplyPolyline(bump.underBumpTopNode.polyline, unitChange),
                                       layer=6))  # Top chip underbump

        gdspy.write_gds(self.gdspyFile, unit=1.0e-6, precision=1.0e-11)

    def updateBumpsDict(self):
        exclusionZonePolylines = [meshPeriphery for thisNode in self.getChipNNodes(0) + self.getChipNNodes(1)
                                  for meshPeriphery in thisNode.meshPeripheryPolylines]
        self.bumpsDict["Bumps"] = []
        bumpIndex = 0
        edgeBufferX = 0.07 * self.chipDict[1].substrate.geometryParamsDict["Width"]
        edgeBufferY = 0.07 * self.chipDict[1].substrate.geometryParamsDict["Length"]
        print("starting bumps")
        for xVal in np.arange(-self.chipDict[1].substrate.geometryParamsDict["Width"] / 2 + edgeBufferX,
                              self.chipDict[1].substrate.geometryParamsDict["Width"] / 2 - edgeBufferX,
                              self.bumpsDict["Spacing"]):
            for yVal in np.arange(-self.chipDict[1].substrate.geometryParamsDict["Length"] / 2 + edgeBufferY,
                                  self.chipDict[1].substrate.geometryParamsDict["Length"] / 2 - edgeBufferY,
                                  self.bumpsDict["Spacing"]):
                # Check if the point lies inside any of the exclusion zones
                exclude = "No"
                i = 0
                while exclude == "No" and i < len(exclusionZonePolylines):
                    thisExclusionZone = exclusionZonePolylines[i]
                    for point in rectanglePolyline(centerX=xVal, centerY=yVal, width=self.bumpsDict["Under Bump Width"],
                                                   length=self.bumpsDict["Under Bump Width"], angle=0):
                        if pointInPolyline(point, thisExclusionZone):
                            exclude = "Yes"
                    i += 1
                if exclude == "No":
                    # This model depends on what the bumps look like post-squish, which is not currently well known.
                    totalBumpHeight = self.chipDict[1].ground.outlineNode.Z - (
                            self.chipDict[0].ground.outlineNode.Z + self.chipDict[0].ground.outlineNode.height)
                    underBumpHeight = 0.05
                    bumpMetalHeight = (totalBumpHeight - 2 * underBumpHeight) / 2
                    thisBump = Bump()

                    thisBump.underBumpBottomNode = Node(name="underBumpBot" + str(bumpIndex))
                    thisBump.bumpMetalBottomNode = Node(name="bumpMetalBot" + str(bumpIndex))
                    thisBump.bumpMetalTopNode = Node(name="bumpMetalTop" + str(bumpIndex))
                    thisBump.underBumpTopNode = Node(name="underBumpTop" + str(bumpIndex))

                    thisBump.underBumpBottomNode.Z = self.chipDict[0].substrate.node.height + self.chipDict[
                        0].ground.outlineNode.height
                    thisBump.bumpMetalBottomNode.Z = thisBump.underBumpBottomNode.Z + underBumpHeight
                    thisBump.bumpMetalTopNode.Z = self.chipDict[
                                                      1].ground.outlineNode.Z - underBumpHeight - bumpMetalHeight
                    thisBump.underBumpTopNode.Z = thisBump.bumpMetalTopNode.Z + bumpMetalHeight

                    thisBump.underBumpBottomNode.height = underBumpHeight
                    thisBump.bumpMetalBottomNode.height = bumpMetalHeight
                    thisBump.bumpMetalTopNode.height = bumpMetalHeight
                    thisBump.underBumpTopNode.height = underBumpHeight

                    for node in [thisBump.underBumpBottomNode, thisBump.bumpMetalBottomNode, thisBump.bumpMetalTopNode,
                                 thisBump.underBumpTopNode]:
                        node.polylineShape = "rectangle"
                    for node in [thisBump.underBumpBottomNode, thisBump.underBumpTopNode]:
                        node.polylineShapeParams = {
                            "Body Center X": xVal,
                            "Body Center Y": yVal,
                            "Body Width": self.bumpsDict["Under Bump Width"],
                            "Body Length": self.bumpsDict["Under Bump Width"],
                            "Angle": 0,
                            "Side 1 Boundary": 0,
                            "Side 2 Boundary": 0,
                            "Side 3 Boundary": 0,
                            "Side 4 Boundary": 0,
                            "Mesh Boundary": self.sysParams["Anti-Vortex Mesh Boundary"]
                        }
                        node.updatePolylines()
                    for node in [thisBump.bumpMetalBottomNode, thisBump.bumpMetalTopNode]:
                        node.polylineShapeParams = {
                            "Body Center X": xVal,
                            "Body Center Y": yVal,
                            "Body Width": self.bumpsDict["Bump Metal Width"],
                            "Body Length": self.bumpsDict["Bump Metal Width"],
                            "Angle": 0,
                            "Side 1 Boundary": 0,
                            "Side 2 Boundary": 0,
                            "Side 3 Boundary": 0,
                            "Side 4 Boundary": 0,
                            "Mesh Boundary": self.sysParams["Anti-Vortex Mesh Boundary"]
                        }
                        node.updatePolylines()

                    self.bumpsDict["Bumps"].append(thisBump)
                    # print(bumpIndex)
                    bumpIndex += 1
        print("finished bumps")

    @property
    def allQubitsDict(self):
        allQubits = dict()
        for chipIndex, chip in self.chipDict.items():
            for qubitIndex, qubit in chip.qubitDict.items():
                allQubits[qubitIndex] = qubit
        return allQubits

    @property
    def allReadoutResonatorsDict(self):
        allReadoutResonators = dict()
        for chipIndex, chip in self.chipDict.items():
            for readoutResonatorIndex, readoutResonator in chip.readoutResonatorDict.items():
                allReadoutResonators[readoutResonatorIndex] = readoutResonator
        return allReadoutResonators

    @property
    def allPTCsDict(self):
        allPTCs = dict()
        for chipIndex, chip in self.chipDict.items():
            for PTCIndex, PTC in chip.PTCDict.items():
                allPTCs[PTCIndex] = PTC
        return allPTCs

    @property
    def allStraightBusCouplersDict(self):
        allStraightBusCouplers = dict()
        for chipIndex, chip in self.chipDict.items():
            for straightBusCouplerIndex, straightBusCoupler in chip.straightBusCouplerDict.items():
                allStraightBusCouplers[straightBusCouplerIndex] = straightBusCoupler
        return allStraightBusCouplers

    @property
    def allControlLinesDict(self):
        allControlLines = dict()
        for chipIndex, chip in self.chipDict.items():
            for controlLineIndex, controlLine in chip.controlLineDict.items():
                allControlLines[controlLineIndex] = controlLine
        return allControlLines

    def getChipNNodes(self, N):  # Doesn't include ground,substrate, or launchPads
        allNodes = []
        for qubitIndex, qubit in self.chipDict[N].qubitDict.items():
            allNodes += [pad.node for pad in qubit.padListGeom]
        for readoutResonatorIndex, readoutResonator in self.chipDict[N].readoutResonatorDict.items():
            allNodes += [readoutResonator.pad1.node, readoutResonator.pad2.node, readoutResonator.meanderNode]
        for PTCIndex, PTC in self.chipDict[N].PTCDict.items():
            allNodes += [PTC.pad1.node, PTC.pad2.node, PTC.meanderNode]
        for straightBusCouplerIndex, straightBusCoupler in self.chipDict[N].straightBusCouplerDict.items():
            allNodes += [straightBusCoupler.pad1.node, straightBusCoupler.pad2.node]
        for controlLineIndex, controlLine in self.chipDict[N].controlLineDict.items():
            allNodes.append(controlLine.lineNode)
            for launchPadName, launchPad in controlLine.launchPadNodeDict.items():
                allNodes.append(launchPad)
        return allNodes

    def getChipNNodes_CapMat(self, N):
        allNodes = []
        for qubitIndex, qubit in self.chipDict[N].qubitDict.items():
            allNodes += [pad.node for pad in qubit.padListGeom]
        for readoutResonatorIndex, readoutResonator in self.chipDict[N].readoutResonatorDict.items():
            allNodes += [readoutResonator.pad1.node, readoutResonator.pad2.node]
        for PTCIndex, PTC in self.chipDict[N].PTCDict.items():
            allNodes += [PTC.pad1.node, PTC.pad2.node]
        for straightBusCouplerIndex, straightBusCoupler in self.chipDict[N].straightBusCouplerDict.items():
            allNodes += [straightBusCoupler.pad1.node, straightBusCoupler.pad2.node]
        for controlLineIndex, controlLine in self.chipDict[N].controlLineDict.items():
            if controlLine.generalParamsDict["Type"] == "feedline" and self.sysParams["Simulate Feedline?"] == "Yes":
                allNodes.append(controlLine.lineNode)
                for launchPadName, launchPad in controlLine.launchPadNodeDict.items():
                    allNodes.append(launchPad)
        return allNodes

    def deleteFile(self, fileName):
        if self.sysParams["Compute Location"] == "Windows":
            subprocess.call("del " + fileName + " 2>nul", shell=True)
        elif self.sysParams["Compute Location"] == "Cluster":
            subprocess.call("rm -f " + fileName, shell=True)

    def deleteFolder(self, fileName):
        if os.path.exists(fileName):
            if self.sysParams["Compute Location"] == "Windows":
                subprocess.call("rmdir " + fileName + " /s /q", shell=True)
            elif self.sysParams["Compute Location"] == "Cluster":
                subprocess.call("rm -r " + fileName, shell=True)

    def stateList(self, excitationList):
        """Excitation list is of the form [[i,n],[j,m],...]
        where i,j are component indices, and m,n are the excitations."""
        numComponents = len(self.HComponentOrder)
        s = [0] * numComponents
        for i in excitationList:
            s[i[0]] = i[1]
        return s

    def componentFromName(self, componentName):
        if componentName[0] == "Q":
            return self.allQubitsDict[int(componentName[1:])]
        elif componentName[0] == "R":
            return self.allReadoutResonatorsDict[int(componentName[1:])]
