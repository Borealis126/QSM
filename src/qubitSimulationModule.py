import subprocess
import numpy as np
import os
import gdspy
from ChipElements import OtherComponents
from basicGeometryFunctions import pointInPolyline, rotate, translate
from node import Node
from polylineFunctions import rectanglePolyline, multiplyPolyline
from qSysObjects import *
from constants import *
import json
from csvFunctions import jsonRead, jsonWrite


def generateSystemParametersFile(folder):
    sysParamsDict = {"Chip Description": "description",
                     "Number of Qubits": 1, "Number of Readout Resonators": 1,
                     "Material": "perfect conductor",
                     "Flip Chip?": "No", "Chip Markers": "Pappas", "Simulation": "2D",
                     "Simulate Feedline?": "No",
                     "Add Mesh to GDS?": "No", "Invert GDS?": "No",
                     "Anti-Vortex Mesh Boundary": 40, "Anti-Vortex Mesh Spacing": 50, "Anti-Vortex Mesh Size": 5}
    jsonWrite(folder / "systemParametersFile.json", sysParamsDict)


def initialize(projectFolder, computeLocation, QSMSourceFolder):
    qSys = loadSystemParametersFile(projectFolder, computeLocation, QSMSourceFolder)
    return qSys


def loadSystemParametersFile(projectFolder, computeLocation, QSMSourceFolder):
    """Returns qubitSystem object based on data in systemParametersFile"""
    with open(projectFolder / "systemParametersFile.json", "r") as read_file:
        sysParams = json.load(read_file)
    sysParams["Project Folder"] = projectFolder
    sysParams["Compute Location"] = computeLocation
    sysParams["QSM Source Folder"] = QSMSourceFolder
    return QubitSystem(sysParams)


class QubitSystem:
    def __init__(self, sysParams):
        # ---independent of flip chip
        self.sysParams = sysParams
        self.projectFolder = self.sysParams["Project Folder"]
        self.componentParametersFile = self.projectFolder / "componentParametersFile.json"
        self.componentGeometriesFile = self.projectFolder / "componentGeometriesFile.json"
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
        componentsDict = {"CPW": {"Phase Velocity(um/s)": 0}}
        qubitParams = ["Type", "L_J(H)", "L_I(H)"]
        readoutResonatorParams = ["Pad 1 Type", "Pad 2 Type"]

        controlLineParams = ["Type"]
        if self.sysParams["Flip Chip?"] == "Yes":
            for paramsList in [qubitParams, readoutResonatorParams, controlLineParams]:
                paramsList.append("Chip")
            bumpsParams = ["Bumps", "Spacing", "Bump Metal Width", "Under Bump Width"]
            componentsDict["Bumps"] = {param: None for param in bumpsParams}
        if self.sysParams["Number of Qubits"] != 0:
            componentsDict["Qubits"] = dict()
            for qubitIndex in range(self.sysParams["Number of Qubits"]):
                componentsDict["Qubits"][qubitIndex] = {param: None for param in qubitParams}
        if self.sysParams["Number of Readout Resonators"] != 0:
            componentsDict["Readout Resonators"] = dict()
            if self.sysParams["Simulate Feedline?"] == "No":
                readoutResonatorParams += ["Capacitance to Feedline (F)", "Feedline Pad Capacitance to Ground (F)"]
            for readoutResonatorIndex in range(self.sysParams["Number of Readout Resonators"]):
                componentsDict["Readout Resonators"][readoutResonatorIndex] = \
                    {param: None for param in readoutResonatorParams}
        if self.sysParams["Number of Control Lines"] != 0:
            componentsDict["Control Lines"] = dict()
            for controlLineIndex in range(self.sysParams["Number of Control Lines"]):
                componentsDict["Control Lines"][controlLineIndex] = {param: None for param in controlLineParams}

        jsonWrite(self.componentParametersFile, componentsDict)

    def loadComponentParams(self):
        componentsDict = jsonRead(self.componentParametersFile)

        # Qubits
        if self.sysParams["Number of Qubits"] != 0:
            paramsDict = componentsDict["Qubits"]
            for qubitIndexStr, params in paramsDict.items():
                qubit = None
                qubitIndex=int(qubitIndexStr)
                if "Floating" in params["Type"]:
                    qubit = FloatingQubit(qubitIndex, params)
                elif "Grounded" in params["Type"]:
                    qubit = GroundedQubit(qubitIndex, params)
                chipIndex = 0
                if self.sysParams["Flip Chip?"] == "Yes":
                    chipIndex = params["Chip"]
                self.chipDict[chipIndex].qubitDict[qubitIndex] = qubit
        # Readout Resonators
        if self.sysParams["Number of Readout Resonators"] != 0:
            paramsDict = componentsDict["Readout Resonators"]
            for indexStr, params in paramsDict.items():
                index = int(indexStr)
                readoutResonator = ReadoutResonator(index, params)
                chipIndex = 0
                if self.sysParams["Flip Chip?"] == "Yes":
                    chipIndex = params["Chip"]
                self.chipDict[chipIndex].readoutResonatorDict[index] = readoutResonator
        # Control Lines
        if self.sysParams["Number of Control Lines"] != 0:
            controlLinesDict = componentsDict["Control Lines"]
            for indexStr, params in controlLinesDict.items():
                index=int(indexStr)
                controlLine = ControlLine(index, params)
                controlLineChipIndex = 0
                if self.sysParams["Flip Chip?"] == "Yes":
                    controlLineChipIndex = params["Chip"]
                self.chipDict[controlLineChipIndex].controlLineDict[index] = controlLine
        # Load CPW info
        self.CPW.componentParams = componentsDict["CPW"]
        # Load bumps info
        if self.sysParams["Flip Chip?"] == "Yes":
            self.bumpsDict = componentsDict["Bumps"]

    def generateGeometries(self):
        geometriesDict = {}
        self.loadComponentParams()
        """For flip chip the polylines for the nodes, substrate, etc. are relative to looking top-down on the assembly,
        which is centered on the origin. The chip furthest from the viewer is chip 0."""
        # Qubits
        geometriesDict["Qubits"] = dict()
        for qubitIndex, qubit in self.allQubitsDict.items():
            params = []
            if "rectangularPads" in qubit.qubitType:
                if isinstance(qubit, FloatingQubit):
                    params += ["Angle", "Center X", "Center Y", "Pad Spacing",
                               "Pad 1 Width", "Pad 1 Length", "Pad 1 Height", "Pad 1 Side 1 Boundary",
                               "Pad 1 Side 2 Boundary", "Pad 1 Side 3 Boundary", "Pad 1 Side 4 Boundary",
                               "Pad 2 Width", "Pad 2 Length", "Pad 2 Height", "Pad 2 Side 1 Boundary",
                               "Pad 2 Side 2 Boundary", "Pad 2 Side 3 Boundary", "Pad 2 Side 4 Boundary", "JJ Location"]
                    """JJ location is any number between 0 and 100 representing the location 
                    of the JJ relative to the pads. 0 is on the left, 100 is on the right, 50 is in the middle."""
                elif isinstance(qubit, GroundedQubit):
                    params += ["Angle", "Center X", "Center Y",
                               "Pad 1 Width", "Pad 1 Length", "Pad 1 Height", "Pad 1 Side 1 Boundary",
                               "Pad 1 Side 2 Boundary", "Pad 1 Side 3 Boundary", "Pad 1 Side 4 Boundary",
                               "JJ Location"]
                if "doubleJJ" in qubit.qubitType:
                    params += ["SQUID Stem Separation", "SQUID Stem Width", "SQUID Stem Length"
                               "SQUID T Stem Width", "SQUID T Head Width", "SQUID T Head Length",
                               "JJ Patch Length", "JJ Patch Width", "JJ Boundary"]
                elif "singleJJ" in qubit.componentParams["Type"]:  # Default along the line of symmetry of pads.
                    params += ["JJ Stem Boundary", "JJ Stem Width", "JJ Patch Width", "JJ Patch Length"]
                params += ["JJ Top Electrode Width", "JJ Bottom Electrode Width"]
                for padName, numFingers in qubit.fingers.items():
                    if numFingers > 1:
                        params += [padName + " Finger Spacing"]
                    for fingerIndex in range(numFingers):
                        params += [
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
            geometriesDict["Qubits"][qubitIndex] = {param: None for param in params}
        # Readout resonators
        geometriesDict["Readout Resonators"] = dict()
        for readoutResonatorIndex, readoutResonator in self.allReadoutResonatorsDict.items():
            params = ["Length", "Angle", "Center X", "Center Y", "Pad Separation", "Meander Turn Radius",
                      "Pad T Stem Length", "Meander To Pad Minimum Distance", "Pad 1 Curve Angle", "Pad 2 Curve Angle"]
            for padIndex in [1, 2]:
                if "T" in readoutResonator.padType(padIndex).split("-"):
                    params += ["Pad " + str(padIndex) + " " + i
                               for i in ["Width", "Length", "Height", "Side 1 Boundary",
                                         "Side 2 Boundary", "Side 3 Boundary", "Side 4 Boundary"]]
            geometriesDict["Readout Resonators"][readoutResonatorIndex] = {param: None for param in params}

        # Control lines
        geometriesDict["Control Lines"] = dict()
        for controlLineIndex, controlLine in self.allControlLinesDict.items():
            params = ["Start X", "Start Y", "Start Angle", "Section Code"]
            if controlLine.lineType == "fluxBias":
                params += ["loop" + i for i in ["Thickness", "Seg1Length", "Seg2Length", "Seg3Length", "Seg1Boundary",
                                                "Seg2Boundary", "Seg3Boundary"]]
            if controlLine.componentParams["Type"] == "drive":
                params += ["End Gap"]
            geometriesDict["Control Lines"][controlLineIndex] = {param: None for param in params}
        # CPW.
        geometriesDict["CPW"] = {"Width": 10, "Gap": 6, "Trench": 0.1, "Height": 0.1}

        # Prompt for the ground/substrate
        geometriesDict["Ground(s)"] = dict()
        geometriesDict["Substrate(s)"] = dict()
        for chipIndex, chip in self.chipDict.items():
            groundParams = {"Height": 0.1}
            geometriesDict["Ground(s)"][chipIndex] = groundParams
            substrateParams = {"Material": "silicon", "Thickness": 500, "Width": 9500, "Length": 7500}
            geometriesDict["Substrate(s)"][chipIndex] = substrateParams

        # NIST logo
        geometriesDict["NIST Logo"] = {"Center X": 2000, "Center Y": -3000}
        # Chip description
        geometriesDict["Chip Description"] = {"Start X": 1500, "Start Y": -2500}

        # If flip chip, prompt for chip spacing
        if self.sysParams["Flip Chip?"] == "Yes":
            geometriesDict["Flip Chip"] = {"Chip Spacing": 1000}

        jsonWrite(self.componentGeometriesFile, geometriesDict)

    def loadGeometries(self):
        componentsDict = jsonRead(self.componentGeometriesFile)
        # Load CPW info
        self.CPW.geometryParams = componentsDict["CPW"]
        # Load NIST Logo info
        NISTLogoParams = componentsDict["NIST Logo"]
        self.chipDict[0].nistLogoCenter = [NISTLogoParams["Center X"], NISTLogoParams["Center Y"]]
        # Load Chip Description info
        chipDescriptionParams = componentsDict["Chip Description"]
        self.chipDict[0].chipDescriptionStart = [chipDescriptionParams["Start X"], chipDescriptionParams["Start Y"]]
        # If flip chip, load chip spacing
        if self.sysParams["Flip Chip?"] == "Yes":
            self.chipSpacing = componentsDict["Flip Chip"]["Chip Spacing"]
        substrateParamsDict = componentsDict["Substrate(s)"]
        groundComponentsDict = componentsDict["Ground(s)"]
        # Load geometries
        for chipIndex, chip in self.chipDict.items():
            # Substrates
            chip.substrate.geometryParams = substrateParamsDict[str(chipIndex)]
            chip.substrate.node.height = chip.substrate.geometryParams["Thickness"]
            chip.substrate.node.material = chip.substrate.geometryParams["Material"]
            chip.substrate.node.polyline = rectanglePolyline(centerX=0,
                                                             centerY=0,
                                                             width=chip.substrate.geometryParams["Width"],
                                                             length=chip.substrate.geometryParams["Length"],
                                                             angle=0)
            if chipIndex == 0:
                chip.substrate.node.Z = 0  # Always 0 for substrate 0, convention
            elif chipIndex == 1:
                chip.substrate.node.Z = self.chipDict[0].substrate.node.height + self.chipSpacing
            # Ground
            chip.ground.geometryParams = groundComponentsDict[str(chipIndex)]
            chip.ground.outlineNode.height = chip.ground.geometryParams["Height"]
            chip.ground.outlineNode.polyline = chip.substrate.node.polyline  # Ground covers the full substrate
            if chipIndex == 0:
                chip.ground.outlineNode.Z = self.chipDict[0].substrate.node.height
            elif chipIndex == 1:
                chip.ground.outlineNode.Z = self.chipDict[1].substrate.node.Z - chip.ground.outlineNode.height
            # Qubits
            for qubitIndex, qubit in chip.qubitDict.items():
                qubit.geometryParams = componentsDict["Qubits"][str(qubitIndex)]
                geoms = qubit.geometryParams
                JJLoc_x, JJLoc_y = readJJLocation(geoms["JJ Location"])
                pad1Node = qubit.pad1.node
                pad2Node = qubit.pad2.node
                # Polylines
                if "rectangularPads" in qubit.componentParams["Type"]:
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

                        padSpacing = (geoms["Pad 1 Side 4 Boundary"] - geoms["Pad 2 Length"])
                        centerX = geoms["Center X"]
                        centerY = (geoms["Center Y"] - geoms["Pad 1 Length"] / 2 - padSpacing / 2)
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
                    if "singleJJ" in qubit.componentParams["Type"]:
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
                    elif "doubleJJ" in qubit.componentParams["Type"]:
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
                readoutResonator.geometryParams = componentsDict["Readout Resonators"][str(readoutResonatorIndex)]
                geoms = readoutResonator.geometryParams
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
                    shapeParams["Finger 0 Stem Width"] = self.CPW.geometryParams["Width"]
                    shapeParams["Finger Stem Boundary"] = self.CPW.geometryParams["Gap"]
                    shapeParams["Finger 0 T Head Length"] = geoms["Pad T Stem Length"] / 2
                    shapeParams["Finger 0 T Width"] = self.CPW.geometryParams["Width"]
                    shapeParams["Finger 0 T Side 1 Boundary"] = self.CPW.geometryParams["Gap"]
                    shapeParams["Finger 0 T Side 2 Boundary"] = 1
                    shapeParams["Finger 0 T Side 3 Boundary"] = self.CPW.geometryParams["Gap"]
                    shapeParams["Finger 0 T Side 4 Boundary"] = 1

                pad1Node.updatePolylines()
                pad2Node.updatePolylines()
            # Control Lines
            for controlLineIndex, controlLine in chip.controlLineDict.items():
                controlLine.geometryParams = componentsDict["Control Lines"][str(controlLineIndex)]
                geoms = controlLine.geometryParams
                lineNode = controlLine.lineNode
                # Height
                lineNode.height = self.CPW.geometryParams["Height"]
                # Path Polyline
                lineNode.polylineShape = "path"
                lineNode.polylineShapeParams["CPW"] = self.CPW
                lineNode.polylineShapeParams["Mesh Boundary"] = self.sysParams["Anti-Vortex Mesh Boundary"]
                for param in geoms:
                    lineNode.polylineShapeParams[param] = geoms[param]
                lineNode.updatePolylines()
                # Drive line option
                if controlLine.componentParams["Type"] == "drive":
                    loopCutout1Width = geoms["End Gap"]
                    loopCutout1Length = self.CPW.geometryParams["Width"] + 2 * self.CPW.geometryParams["Gap"]
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
                if controlLine.componentParams["Type"] == "fluxBias":
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
                                - self.CPW.geometryParams["Width"] / 2
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
                                + self.CPW.geometryParams["Width"] / 2
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
                    shortLength = self.CPW.geometryParams["Gap"]
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
                    traceEdgePoint = translate(rotate([0, self.CPW.geometryParams["Width"] / 2], lineNode.endAngle),
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
                    lineNode.Z = self.chipDict[1].substrate.node.Z - self.CPW.geometryParams["Height"]
                # Launch pads
                controlLine.updateLaunchPadNodes()
        # If flip chip update bump nodes
        if self.sysParams["Flip Chip?"] == "Yes":
            self.updateBumpsDict()

    def loadDesignFiles(self):
        self.loadComponentParams()
        self.loadGeometries()
        self.CPW.vp = self.CPW.componentParams["Phase Velocity(um/s)"]

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
            chipWidth = chip.substrate.geometryParams["Width"] * unitChange
            chipLength = chip.substrate.geometryParams["Length"] * unitChange

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
                chip_size_x=chip.substrate.geometryParams["Width"] * unitChange,
                chip_size_y=chip.substrate.geometryParams["Length"] * unitChange)
            subtractFromGround.append(diceGap)
            # Chip Markers
            if self.sysParams["Chip Markers"] == "Pappas":
                chipMarkers = OtherComponents.createPappasMarkers(
                    chip_size_x=chip.substrate.geometryParams["Width"] * unitChange,
                    chip_size_y=chip.substrate.geometryParams["Length"] * unitChange)
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
                shiftX = self.chipDict[0].substrate.geometryParams["Width"] / 2 * unitChange
                shiftY = self.chipDict[0].substrate.geometryParams["Length"] / 2 * unitChange
                if self.sysParams["Flip Chip?"] == "Yes":
                    shiftX = self.chipDict[1].substrate.geometryParams["Width"] / 2 * unitChange
                    shiftY = self.chipDict[1].substrate.geometryParams["Length"] / 2 * unitChange

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
                Main.add(gdspy.Polygon(multiplyPolyline(bump.underBumpBottomNode.polyline, unitChange), layer=3))
                Main.add(gdspy.Polygon(multiplyPolyline(bump.bumpMetalBottomNode.polyline, unitChange), layer=4))
                Main.add(gdspy.Polygon(multiplyPolyline(bump.bumpMetalTopNode.polyline, unitChange), layer=5))
                Main.add(gdspy.Polygon(multiplyPolyline(bump.underBumpTopNode.polyline, unitChange), layer=6))

        gdspy.write_gds(self.gdspyFile, unit=1.0e-6, precision=1.0e-11)

    def updateBumpsDict(self):
        exclusionZonePolylines = [meshPeriphery for thisNode in self.getChipNNodes(0) + self.getChipNNodes(1)
                                  for meshPeriphery in thisNode.meshPeripheryPolylines]
        self.bumpsDict["Bumps"] = []
        bumpIndex = 0
        edgeBufferX = 0.07 * self.chipDict[1].substrate.geometryParams["Width"]
        edgeBufferY = 0.07 * self.chipDict[1].substrate.geometryParams["Length"]
        print("starting bumps")
        for xVal in np.arange(-self.chipDict[1].substrate.geometryParams["Width"] / 2 + edgeBufferX,
                              self.chipDict[1].substrate.geometryParams["Width"] / 2 - edgeBufferX,
                              self.bumpsDict["Spacing"]):
            for yVal in np.arange(-self.chipDict[1].substrate.geometryParams["Length"] / 2 + edgeBufferY,
                                  self.chipDict[1].substrate.geometryParams["Length"] / 2 - edgeBufferY,
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
        for controlLineIndex, controlLine in self.chipDict[N].controlLineDict.items():
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

    def componentFromName(self, componentName):
        if componentName[0] == "Q":
            return self.allQubitsDict[int(componentName[1:])]
        elif componentName[0] == "R":
            return self.allReadoutResonatorsDict[int(componentName[1:])]


def readJJLocation(JJLocationCode):
    """JJLocationCode is in the form [10:-20] corresponding to a shift 10um to the right and 20um down."""
    JJLoc = [float(i) for i in JJLocationCode[1:-1].split(":")]
    return JJLoc[0], JJLoc[1]