import subprocess
import numpy as np
import os
import gdspy
from .ChipElements import OtherComponents
from .basicGeometry import pointInPolyline, rotate, translate
from .qSysObjects import *
from .constants import *
from .dataIO import jsonRead, jsonWrite


def generateSystemParams(folder):
    sysParamsDict = {"Chip Description": "description",
                     "Number of Qubits": 1, "Number of Readout Resonators": 1, "Number of Control Lines": 1,
                     "Material": "perfect conductor",
                     "Flip Chip?": "No", "Chip Markers": "Pappas",
                     "Simulate Feedline?": "No"}
    jsonWrite(folder / "systemParameters.json", sysParamsDict)


def initialize(projectFolder, computeLocation, QSMSourceFolder, layoutCompleted=False):
    qArch = loadSystemParams(projectFolder, computeLocation, QSMSourceFolder)
    if layoutCompleted:
        qArch.loadDesignFiles()
    return qArch


def loadSystemParams(projectFolder, computeLocation, QSMSourceFolder):
    sysParams = jsonRead(projectFolder / "systemParameters.json")
    sysParams["Project Folder"] = projectFolder
    sysParams["Compute Location"] = computeLocation
    sysParams["QSM Source Folder"] = QSMSourceFolder
    return QubitSystem(sysParams)


class QubitSystem:
    def __init__(self, sysParams):
        # ---independent of flip chip
        self.sysParams = sysParams
        self.projectFolder = self.sysParams["Project Folder"]
        self.componentParametersFile = self.projectFolder / "componentParameters.json"
        self.componentGeometriesFile = self.projectFolder / "componentGeometries.json"
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
        readoutResonatorParams = ["Type"]

        controlLineParams = ["Type"]
        if self.sysParams["Flip Chip?"] == "Yes":
            for paramsList in [qubitParams, readoutResonatorParams, controlLineParams]:
                paramsList.append("Chip")
            bumpsParams = ["Bumps", "Spacing", "Bump Metal Width", "Under Bump Width", "Mesh Boundary"]
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
            for qubitIndexStr, componentParams in paramsDict.items():
                qubitIndex = int(qubitIndexStr)
                qubit = Qubit(qubitIndex, componentParams)
                chipIndex = 0
                if self.sysParams["Flip Chip?"] == "Yes":
                    chipIndex = componentParams["Chip"]
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
                index = int(indexStr)
                controlLine = ControlLine(index, params)
                self.chipDict[0].controlLineDict[index] = controlLine
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
            geometriesDict["Qubits"][qubitIndex] = qubit.design.promptedParams
        # Readout resonators
        geometriesDict["Readout Resonators"] = dict()
        for readoutResonatorIndex, readoutResonator in self.allReadoutResonatorsDict.items():
            geometriesDict["Readout Resonators"][readoutResonatorIndex] = readoutResonator.design.promptedParams
        geometriesDict["Control Lines"] = dict()
        for controlLineIndex, controlLine in self.allControlLinesDict.items():
            geometriesDict["Control Lines"][controlLineIndex] = controlLine.design.promptedParams
        # CPW.
        geometriesDict["CPW"] = {"Width": 10, "Gap": 6, "Trench": 0.1, "Height": 0.1}
        #
        # Prompt for the ground/substrate
        geometriesDict["Ground(s)"] = dict()
        geometriesDict["Substrate(s)"] = dict()
        for chipIndex, chip in self.chipDict.items():
            groundParams = {"Height": 0.1, "Mesh Boundary": 40, "Mesh Spacing": 50, "Mesh Size": 5}
            geometriesDict["Ground(s)"][chipIndex] = groundParams
            substrateParams = {"Material": "silicon", "Thickness": 500, "Width": 9500, "Length": 7500}
            geometriesDict["Substrate(s)"][chipIndex] = substrateParams
        #
        # NIST logo
        geometriesDict["NIST Logo"] = {"Center X": 2000, "Center Y": -3000}
        # Chip description
        geometriesDict["Chip Description"] = {"Start X": 1500, "Start Y": -2500}
        #
        # # If flip chip, prompt for chip spacing
        # if self.sysParams["Flip Chip?"] == "Yes":
        #     geometriesDict["Flip Chip"] = {"Chip Spacing": 1000}

        jsonWrite(self.componentGeometriesFile, geometriesDict)

    def loadGeometries(self):
        self.loadComponentParams()
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
            chip.substrate.node.material = chip.substrate.geometryParams["Material"]
            # X,Y, angle = 0
            chip.substrate.node.shape.paramsDict["Width"] = chip.substrate.geometryParams["Width"]
            chip.substrate.node.shape.paramsDict["Length"] = chip.substrate.geometryParams["Length"]
            chip.substrate.node.shape.paramsDict["Height"] = chip.substrate.geometryParams["Thickness"]
            chip.substrate.node.shape.createPolylines()
            chip.substrate.node.orientShape() #Substrate is centered on the origin, so no need to update.

            if chipIndex == 0:
                chip.substrate.node.Z = 0  # Always 0 for substrate 0, convention
            elif chipIndex == 1:
                chip.substrate.node.Z = self.chipDict[0].substrate.node.height + self.chipSpacing
            # Ground
            chip.ground.geometryParams = groundComponentsDict[str(chipIndex)]
            chip.ground.outlineNode.shape.paramsDict['Height'] = chip.ground.geometryParams["Height"]
            chip.ground.outlineNode.polyline = chip.substrate.node.polyline  # Ground covers the full substrate
            chip.ground.outlineNode.material = self.sysParams["Material"]
            if chipIndex == 0:
                chip.ground.outlineNode.Z = self.chipDict[0].substrate.node.shape.paramsDict['Height']
            elif chipIndex == 1:
                chip.ground.outlineNode.Z = self.chipDict[1].substrate.node.Z - \
                                            chip.ground.outlineNode.shape.paramsDict['Height']
            # Qubits
            for qubitIndex, qubit in chip.qubitDict.items():
                qubit.design.paramsDict['Mesh Boundary'] = chip.ground.geometryParams['Mesh Boundary']
                qubit.design.paramsDict['Z'] = self.chipDict[0].substrate.node.shape.paramsDict["Height"] #Flip chip?
                for key, val in componentsDict["Qubits"][str(qubitIndex)].items():
                    if key in qubit.design.paramsDict:
                        qubit.design.paramsDict[key] = val
                    else:
                        raise ValueError(str(key) + ' not in design dict')
                qubit.design.updateNodes()
            # Readout Resonators
            for readoutResonatorIndex, readoutResonator in chip.readoutResonatorDict.items():
                #Load data into the design
                readoutResonator.design.paramsDict['Mesh Boundary'] = chip.ground.geometryParams['Mesh Boundary']
                readoutResonator.design.paramsDict['Z'] = self.chipDict[0].substrate.node.shape.paramsDict["Height"]
                for key, val in componentsDict["Readout Resonators"][str(readoutResonatorIndex)].items():
                    if key in readoutResonator.design.paramsDict:
                        readoutResonator.design.paramsDict[key] = val
                    else:
                        raise ValueError(str(key) + ' not in design dict')
                readoutResonator.design.CPW = self.CPW
                readoutResonator.design.updateNodes()
            # Control Lines
            for controlLineIndex, controlLine in chip.controlLineDict.items():
                controlLine.design.paramsDict['Mesh Boundary'] = chip.ground.geometryParams['Mesh Boundary']
                controlLine.design.paramsDict['Z'] = self.chipDict[0].substrate.node.shape.paramsDict["Height"]
                for key, val in componentsDict["Control Lines"][str(controlLineIndex)].items():
                    if key in controlLine.design.paramsDict:
                        controlLine.design.paramsDict[key] = val
                    else:
                        raise ValueError(str(key) + ' not in design dict')
                controlLine.design.CPW = self.CPW
                controlLine.design.updateNodes()
        # If flip chip update bump nodes
        if self.sysParams["Flip Chip?"] == "Yes":
            self.updateBumpsDict()

    def loadDesignFiles(self):
        self.loadComponentParams()
        self.loadGeometries()
        self.CPW.vp = self.CPW.componentParams["Phase Velocity(um/s)"]

    def generateGDS(self, addMesh=False, invertGDS=False):
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
                addToMain.append(gdspy.Polygon(component * unitChange, layer=chip.index))
            for periphery in peripheries:
                subtractFromGround.append(gdspy.Polygon(periphery * unitChange, layer=chip.index))
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
            if addMesh:
                # meshContainer=gdspy.Cell((-chipWidth/2,-chipLength/2),(chipWidth/2,chipLength/2),layer=chip.index+2)
                size = chip.ground.geometryParams["Mesh Size"] * unitChange
                chipBorder = 150
                for xVal in np.arange(-chipWidth / 2 + chipBorder, chipWidth / 2 - chipBorder,
                                      chip.ground.geometryParams["Mesh Spacing"] * unitChange):
                    for yVal in np.arange(-chipLength / 2 + chipBorder, chipLength / 2 - chipBorder,
                                          chip.ground.geometryParams["Mesh Spacing"] * unitChange):
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
            if not invertGDS:
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
            # JJGDSList = []
            # for qubitIndex, qubit in self.chipDict[chip.index].qubitDict.items():  # Add the JJ components
            #     JJGDSList = JJGDSList + qubit.JJGDSs
            # for thisJJGDS in JJGDSList:
            #     Main.add(thisJJGDS.patchGDS)
            #     patchCopy = gdspy.copy(thisJJGDS.patchGDS)
            #     patchCopy.layers = [chip.index]
            #     Main.add(patchCopy)
            #     Main.add(thisJJGDS.topElectrodeGDS)
            #     Main.add(thisJJGDS.bottomElectrodeGDS)
            #     Main.add(thisJJGDS.connectionsGDS)

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
                            "Mesh Boundary": self.bumpsDict["Mesh Boundary"]
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
                            "Mesh Boundary": self.bumpsDict["Mesh Boundary"]
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
            allNodes += [pad.node for pad in qubit.design.padListGeom]
        for readoutResonatorIndex, readoutResonator in self.chipDict[N].readoutResonatorDict.items():
            allNodes += [readoutResonator.design.pad1.node,
                         readoutResonator.design.pad2.node,
                         readoutResonator.design.meanderNode]
        for controlLineIndex, controlLine in self.chipDict[N].controlLineDict.items():
            allNodes.append(controlLine.design.lineNode)
            for launchPadName, launchPad in controlLine.design.launchPadNodeDict.items():
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
