from ansysFunctions import *
import qSysObjects
from csvFunctions import csvRead

class Q3DSim():  # capMat is a simulation that has the Q3DSim q3dExtractor
    def __init__(self, q3dSimName, simDirectory, qSys):
        # "capMatExtractor" is the name, but the type is q3dExtractor
        qSys.loadDesignFiles()
        self.qSys = qSys
        self.name = q3dSimName
        self.aedtPath = simDirectory / (q3dSimName + ".aedt")
        self.simulatorPath = simDirectory / (q3dSimName + "_" + "Simulator.py")
        self.logPath = simDirectory / (q3dSimName + "_" + "Simulator.log")
        self.resultsFilePath = simDirectory / (q3dSimName + "_" + "Results.csv")
        self.aedtFolderPath = simDirectory / "q3dExtractor.aedtresults"
        self.lines = []

    @property
    def resultsFileLines(self):
        return csvRead(self.resultsFilePath)

class Q3DExtractor(Q3DSim):
    lines = []

    def updateLines(self, simParams):
        lines = ansysSimulatorPreamb.copy()
        lines += [
            ansysSetActiveProjectLine(self.name),
            ansysInsertQ3DExtractorLine(self.name),
            ansysSetActiveDesignLine(self.name)
        ]
        lines += self.capMatLayout_Lines()
        lines += capMatAnalysisLines(simParams["MaxPass"], simParams["PerRefine"], self.resultsFilePath)
        lines.append(ansysSaveLine)
        self.lines = lines

    def capMatLayout_Lines(self):
        lines = ["oEditor = oDesign.SetActiveEditor(\"3D Modeler\")\n",
                 "oModuleBoundary = oDesign.GetModule(\"BoundarySetup\")\n"]
        for chipIndex, chip in self.qSys.chipDict.items():
            # Draw substrate
            lines += ansysPolyline_Lines(
                name=chip.substrate.name,
                color=chip.substrate.node.color,
                material=chip.substrate.node.material,
                polyline3D=[[point[0], point[1], chip.substrate.node.Z]
                            for point in chip.substrate.node.polyline]
            )
            lines += ansysSweepAlongVector_Lines(chip.substrate.node)
            # Draw ground(s)
            lines += ansysPolyline_Lines(
                name=chip.ground.outlineNode.name,
                color=chip.ground.outlineNode.color,
                material=chip.ground.outlineNode.material,
                polyline3D=[[point[0], point[1], chip.ground.outlineNode.Z]
                            for point in chip.ground.outlineNode.polyline]
            )
            # Draw qubits,resonators,controlLines,launchpads

            for thisNode in self.qSys.getChipNNodes_CapMat(chip.index):
                lines += ansysPolyline_Lines(
                    name=thisNode.name,
                    color=thisNode.color,
                    material=thisNode.material,
                    polyline3D=[[point[0], point[1], thisNode.Z] for point in
                                thisNode.polyline]
                )
                lines += ansysQ3DMake3D(self.qSys.sysParams["Simulation"], thisNode)
                # Trench round 1
                addTrenchNodeLines, subtractTrenchPeripheryLines, makeTrenchComponent3DLines = ansysTrench(
                    componentNode=thisNode, trench=self.qSys.CPW.geometryParamsDict["Trench"], chip=chip)
                lines += addTrenchNodeLines + subtractTrenchPeripheryLines  # Trench

                lines += ansysSignalLine_Lines(thisNode)
                """Subtract the periphery from the ground. 
                Still subtract the launchpad peripheries so the control lines aren't shorted to ground."""
                for index, peripheryPolyline in enumerate(thisNode.peripheryPolylines):
                    peripheryName = thisNode.name + "periphery" + str(index)
                    lines += ansysPolyline_Lines(
                        name=peripheryName,
                        color=thisNode.color,
                        material=thisNode.material,
                        polyline3D=[[point[0], point[1], thisNode.Z]
                                    for point in peripheryPolyline]
                    )  # First make the boundary
                    """Then subtract it from ground"""
                    lines += ansysSubtract_Lines(chip.ground.outlineNode.name, peripheryName)
            for thisNode in self.qSys.getChipNNodes_CapMat(chip.index):  # Trench round 2.
                addTrenchNodeLines, subtractTrenchPeripheryLines, makeTrenchComponent3DLines = ansysTrench(
                    componentNode=thisNode, trench=self.qSys.CPW.geometryParamsDict["Trench"], chip=chip)
                lines += makeTrenchComponent3DLines
            # For grounded qubits unite pad 2 with ground.
            for qubitIndex, qubit in self.qSys.allQubitsDict.items():
                if isinstance(qubit, qSysObjects.GroundedQubit):
                    lines += ansysUniteNodes([chip.ground.outlineNode, qubit.pad2.node])
            # For control lines unite trace and launchpads, also unite flux bias if applicable.
            for controlLineIndex, controlLine in self.qSys.chipDict[chip.index].controlLineDict.items():
                if (controlLine.generalParamsDict["Type"] == "feedline"
                        and self.qSys.sysParams["Simulate Feedline?"] == "Yes"):
                    uniteNodeList = [controlLine.lineNode]
                    for launchPadName, launchPadNode in controlLine.launchPadNodeDict.items():
                        uniteNodeList.append(launchPadNode)
                    lines += ansysUniteNodes(uniteNodeList)
                    if controlLine.generalParamsDict["Type"] == "fluxBias":
                        lines += ansysUniteNodes([self.chipDict[0].ground.outlineNode, controlLine.lineNode])
            # Make the ground 3D
            lines += ansysQ3DMake3D(self.qSys.sysParams["Simulation"], chip.ground.outlineNode)
        # Draw bumps if flip chip, and join the ground nodes via the bumps
        if self.qSys.sysParams["Flip Chip?"] == "Yes":
            uniteNodeList = [self.qSys.chipDict[0].ground.outlineNode, self.qSys.chipDict[1].ground.outlineNode]
            for thisBump in self.bumpsDict["Bumps"]:
                for thisNode in [
                    thisBump.underBumpBottomNode,
                    thisBump.bumpMetalBottomNode,
                    thisBump.bumpMetalTopNode,
                    thisBump.underBumpTopNode
                ]:
                    lines += ansysPolyline_Lines(
                        name=thisNode.name,
                        color=thisNode.color,
                        material=thisNode.material,
                        polyline3D=[[point[0], point[1], thisNode.Z] for point in
                                    thisNode.polyline]
                    )
                    lines += ansysSweepAlongVector_Lines(thisNode)
                    uniteNodeList.append(thisNode)
            lines += ansysUniteNodes(uniteNodeList)  # Resulting single node is ground1
        # Assign ground signal line (independent of flip chip)
        lines += ansysGroundSignalLine_Lines(self.qSys.chipDict[0].ground)

        return lines


    @property
    def capMatUnitsToF(self):
        reportedUnits = self.resultsFileLines[2][0][8:]  # "C Units:pF"->"pF"
        unitsMultiplier = 1
        if reportedUnits == "pF":
            unitsMultiplier = 1e-12
        return unitsMultiplier

