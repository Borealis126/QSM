from constants import lengthUnits
from node import Node
from controlLineDesigns import FeedLine, FluxBiasLine
from qubitDesigns import GroundedRectangularTransmonSingleJJ

ansysSimulatorPreamb = [
    "import ScriptEnv\n",
    "ScriptEnv.Initialize(\"Ansoft.ElectronicsDesktop\")\n",
    "oDesktop.RestoreWindow()\n"
]

HFSSAnalysisLines = [
    "oModuleAnalysis = oDesign.GetModule(\"AnalysisSetup\")\n",
    "oModuleAnalysis.InsertSetup(\"HfssDriven\",\n",
    "    [\n",
    "        \"NAME:Setup1\",\n",
    "        \"AdaptMultipleFreqs:=\"	, False,\n",
    "        \"Frequency:=\"		, \"5GHz\",\n",
    "        \"MaxDeltaS:=\"		, 0.02,\n",
    "        \"PortsOnly:=\"		, False,\n",
    "        \"UseMatrixConv:=\"	, False,\n",
    "        \"MaximumPasses:=\"	, 6,\n",
    "        \"MinimumPasses:=\"	, 1,\n",
    "        \"MinimumConvergedPasses:=\", 1,\n",
    "        \"PercentRefinement:=\"	, 30,\n",
    "        \"IsEnabled:=\"		, True,\n",
    "        [\n",
    "            \"NAME:MeshLink\",\n",
    "            \"ImportMesh:=\"		, False\n",
    "        ],\n",
    "        \"BasisOrder:=\"		, 1,\n",
    "        \"DoLambdaRefine:=\"	, True,\n",
    "        \"DoMaterialLambda:=\"	, True,\n",
    "        \"SetLambdaTarget:=\"	, False,\n",
    "        \"Target:=\"		, 0.3333,\n",
    "        \"UseMaxTetIncrease:=\"	, False,\n",
    "        \"PortAccuracy:=\"	, 2,\n",
    "        \"UseABCOnPort:=\"	, False,\n",
    "        \"SetPortMinMaxTri:=\"	, False,\n",
    "        \"UseDomains:=\"		, False,\n",
    "        \"UseIterativeSolver:=\"	, False,\n",
    "        \"SaveRadFieldsOnly:=\"	, False,\n",
    "        \"SaveAnyFields:=\"	, True,\n",
    "        \"IESolverType:=\"	, \"Auto\",\n",
    "        \"LambdaTargetForIESolver:=\", 0.15,\n",
    "        \"UseDefaultLambdaTgtForIESolver:=\", True\n",
    "    ])\n",
    "oModuleAnalysis.InsertFrequencySweep(\"Setup1\",\n",
    "    [\n",
    "        \"NAME:Sweep\",\n",
    "        \"IsEnabled:=\"		, True,\n",
    "        \"RangeType:=\"		, \"LinearCount\",\n",
    "        \"RangeStart:=\"		, \"5GHz\",\n",
    "        \"RangeEnd:=\"		, \"6GHz\",\n",
    "        \"RangeCount:=\"		, 10,\n",
    "        \"Type:=\"		, \"Fast\",\n",
    "        \"SaveFields:=\"		, False,\n",
    "        \"SaveRadFields:=\"	, False,\n",
    "        \"InterpTolerance:=\"	, 0.5,\n",
    "        \"InterpMaxSolns:=\"	, 250,\n",
    "        \"InterpMinSolns:=\"	, 0,\n",
    "        \"InterpMinSubranges:=\"	, 1,\n",
    "        \"ExtrapToDC:=\"		, False,\n",
    "        \"InterpUseS:=\"		, True,\n",
    "        \"InterpUsePortImped:=\"	, False,\n",
    "        \"InterpUsePropConst:=\"	, True,\n",
    "        \"UseDerivativeConvergence:=\", False,\n",
    "        \"InterpDerivTolerance:=\", 0.2,\n",
    "        \"UseFullBasis:=\"	, True,\n",
    "        \"EnforcePassivity:=\"	, True,\n",
    "        \"PassivityErrorTolerance:=\", 0.0001,\n",
    "    ])\n",
    "oDesign.AnalyzeAll()\n"
]

ansysSaveLine = "oProject.Save()\n"


def ansysSetActiveProjectLine(simName):
    return "oProject = oDesktop.SetActiveProject(\"" + simName + "\")\n"


def ansysInsertQ3DExtractorLine(q3dSimName):
    return "oProject.InsertDesign(\"Q3D Extractor\", \"" + q3dSimName + "\", \"\", \"\")\n"


def ansysInsertHFSSDesignLine(hfssSimName):
    return "oProject.InsertDesign(\"HFSS\", \"" + hfssSimName + "\", \"\", \"\")\n"


def ansysSetActiveDesignLine(simName):
    return "oDesign = oProject.SetActiveDesign(\"" + simName + "\")\n"


def capMatAnalysisLines(maxPass, perRefine, resultsFile):
    return [
        "oModuleAnalysis = oDesign.GetModule(\"AnalysisSetup\")\n",
        "oModuleAnalysis.InsertSetup(\"Matrix\",\n",
        "    [\n",
        "        \"NAME:capSim\",\n",
        "        \"AdaptiveFreq:=\"	, \"5GHz\",\n",
        "        \"SaveFields:=\"		, False,\n",
        "        \"Enabled:=\"		, True,\n",
        "        [\n",
        "            \"NAME:Cap\",\n",
        "            \"MaxPass:=\"		, " + str(maxPass) + ",\n",
        "            \"MinPass:=\"		, 1,\n",
        "            \"MinConvPass:=\"		, 1,\n",
        "            \"PerError:=\"		, 1,\n",
        "            \"PerRefine:=\"		, " + str(perRefine) + ",\n",
        "            \"AutoIncreaseSolutionOrder:=\", True,\n",
        "            \"SolutionOrder:=\"	, \"High\",\n",
        "            \"Solver Type:=\"		, \"Iterative\"\n",
        "        ]\n",
        "    ])\n",
        "oDesign.AnalyzeAll()\n",
        "oDesign.ExportMatrixData(r\""
        + str(resultsFile)
        + "\", \"C\", \"\", \"capSim:LastAdaptive\", \"Original\", \"ohm\", \"nH\", \"pF\", \"mSie\", 5000000000, \"Maxwell,Spice,Couple\", 0, False, 5, 8, 0)\n"
    ]


def ansysSignalLine_Lines(node):
    return [
        "oModuleBoundary.AssignSignalNet(\n",
        "    [\n",
        "        \"NAME:" + node.name + "\",\n",
        "        \"Objects:=\"		, [\"" + node.name + "\"]\n",
        "    ])\n"
    ]


def ansysUniteNodes(nodeList):
    insertionLine = nodeList[0].name + ","
    for thisNode in nodeList[1:-1]:
        insertionLine = insertionLine + thisNode.name + ","
    insertionLine = insertionLine + nodeList[-1].name
    return [
        "oEditor.Unite(\n",
        "    [\n",
        "        \"NAME:Selections\",\n",
        "        \"Selections:=\"		, \"" + insertionLine + "\"\n",
        "    ],\n",
        "    [\n",
        "        \"NAME:UniteParameters\",\n",
        "        \"KeepOriginals:=\"	, False\n",
        "    ])\n"
    ]


def aedtEdit(line):
    """This function edits the aedt file lines to add a backslash before each single quote.
    Needed for loading in the netlist"""
    returnLine = ""
    for char in line:
        if char == "\'":
            returnLine = returnLine + "\\" + char
        else:
            returnLine = returnLine + char
    return returnLine


def ansysOutputToComplex(complexString):
    return complexString.replace("i", "j").replace(" ", "")


def ansysSweepAlongVector_Lines(node):  # Sweeps along the positive Z direction.
    return [
        "oEditor.SweepAlongVector(\n",
        "    [\n",
        "        \"NAME:Selections\",\n",
        "        \"Selections:=\"		, \"" + node.name + "\",\n",
        "        \"NewPartsModelFlag:=\"	, \"Model\"\n",
        "    ],\n",
        "    [\n",
        "        \"NAME:VectorSweepParameters\",\n",
        "        \"DraftAngle:=\"		, \"0deg\",\n",
        "        \"DraftType:=\"		, \"Round\",\n",
        "        \"CheckFaceFaceIntersection:=\", False,\n",
        "        \"SweepVectorX:=\"	, \"0mm\",\n",
        "        \"SweepVectorY:=\"	, \"0mm\",\n",
        "        \"SweepVectorZ:=\"	, \"" + str(node.height) + lengthUnits + "\",\n",
        "    ])\n"
    ]


def ansysSubtract_Lines(part1Name, part2Name):  # Subtract polyline2 from polyline 1, leaving polyline 1.
    return [
        "oEditor.Subtract(\n",
        "    [\n",
        "        \"NAME:Selections\",\n",
        "        \"Blank Parts:=\"		, \"" + part1Name + "\",\n",
        "        \"Tool Parts:=\"		, \"" + part2Name + "\"\n",
        "    ],\n",
        "    [\n",
        "        \"NAME:SubtractParameters\",\n",
        "        \"KeepOriginals:=\"	, False\n",
        "    ])\n"
    ]


def ansysThinConductor(node):
    return [
        "oModuleBoundary.AssignThinConductor(\n",
        "    [\n",
        "        \"NAME:ThinCond" + node.name + "\",\n",
        "        \"Objects:=\"		, [\"" + node.name + "\"],\n",
        "        \"Material:=\"		, \"" + node.material + "\",\n",
        "        \"Thickness:=\"		, \"" + str(node.height) + lengthUnits + "\"\n",
        "    ])\n"
    ]


def ansysPolyline_Lines(name, color, material, polyline3D):
    # polyline3D has x,y,z vals, not just the x,y vals of node.polyline
    lines = [
        "oEditor.CreatePolyline(\n",
        "    [\n",
        "        \"NAME:PolylineParameters\",\n",
        "        \"IsPolylineCovered:=\"	, True,\n",
        "        \"IsPolylineClosed:=\"	, True,\n",
        "        [\n",
        "            \"NAME:PolylinePoints\",\n"
    ]
    numPoints = len(polyline3D)
    pointIndex = 0
    for point in polyline3D + [polyline3D[0]]:  # The polyline wraps back to the first point.
        lines += [
            "            [\n",
            "                \"NAME:PLPoint\",\n",
            "                \"X:=\"			, \"" + str(point[0]) + lengthUnits + "\",\n",
            "                \"Y:=\"			, \"" + str(point[1]) + lengthUnits + "\",\n",
            "                \"Z:=\"			, \"" + str(point[2]) + lengthUnits + "\"\n"
        ]
        if pointIndex == numPoints:
            lines += ["            ]\n"]
        else:
            lines += ["            ],\n"]
        pointIndex = pointIndex + 1
    lines += [
        "        ],\n",
        "        [\n",
        "            \"NAME:PolylineSegments\",\n"
    ]
    for pointIndex in range(numPoints):
        lines += [
            "            [\n",
            "                \"NAME:PLSegment\",\n",
            "                \"SegmentType:=\"		, \"Line\",\n",
            "                \"StartIndex:=\"		, " + str(pointIndex) + ",\n",
            "                \"NoOfPoints:=\"		, 2\n"
        ]
        if pointIndex == numPoints - 1:
            lines += ["            ]\n"]
        else:
            lines += ["            ],\n"]
    solveInside = "False"
    if material == "silicon" or material == "vacuum":
        solveInside = "True"
    lines += [
        "        ],\n",
        "        [\n",
        "            \"NAME:PolylineXSection\",\n",
        "            \"XSectionType:=\"	, \"None\",\n",
        "            \"XSectionOrient:=\"	, \"Auto\",\n",
        "            \"XSectionWidth:=\"	, \"0mm\",\n",
        "            \"XSectionTopWidth:=\"	, \"0mm\",\n",
        "            \"XSectionHeight:=\"	, \"0mm\",\n",
        "            \"XSectionNumSegments:=\"	, \"0\",\n",
        "            \"XSectionBendType:=\"	, \"Corner\"\n",
        "        ]\n",
        "    ],\n",
        "    [\n",
        "        \"NAME:Attributes\",\n",
        "        \"Name:=\"		, \"" + name + "\",\n",
        "        \"Flags:=\"		, \"\",\n",
        "        \"Color:=\"		, \"" + color + "\",\n",
        "        \"Transparency:=\"	, 0,\n",
        "        \"PartCoordinateSystem:=\", \"Global\",\n",
        "        \"UDMId:=\"		, \"\",\n",
        "        \"MaterialValue:=\"	, \"\\\"" + material + "\\\"\",\n",
        "        \"SurfaceMaterialValue:=\", \"\\\"\\\"\",\n",
        "        \"SolveInside:=\"		, " + solveInside + ",\n",
        "        \"IsMaterialEditable:=\"	, True,\n",
        "        \"UseMaterialAppearance:=\", False,\n",
        "        \"IsLightweight:=\"	, False\n",
        "    ])\n"
    ]
    return lines


def ansysGroundSignalLine_Lines(ground):
    return [
        "oModuleBoundary.AssignGroundNet(\n",
        "    [\n",
        "        \"NAME:GroundNet1\",\n",
        "        \"Objects:=\"		, [\"" + ground.name + "\"]\n",
        "    ])\n"
    ]


def ansysTrench(componentNode, trench, chip):
    """trenchPeripheryNode is the outline that is subtracted from the substrate,
    after which trenchComponentNode is added to have a resulting net trench."""
    # Define the trench nodes
    # This is the substrate "platform" that the component will eventually be resting on.
    trenchComponentNode = Node(componentNode.name + "TrenchComponent", "Rectangle")
    # These are the peripheries that will be subtracted from the substrate.
    trenchPeripheryNodes = []
    for index, peripheryPolyline in enumerate(componentNode.peripheryPolylines):
        thisNode = Node(componentNode.name + "TrenchPeriphery" + str(index), "Rectangle")
        thisNode.polyline = peripheryPolyline
        thisNode.material = "silicon"
        thisNode.color = chip.substrate.node.color
        trenchPeripheryNodes.append(thisNode)
    trenchComponentNode.polyline = componentNode.polyline
    trenchComponentNode.material = "silicon"
    trenchComponentNode.color = chip.substrate.node.color
    addTrenchNodeLines = []
    for trenchNode in [trenchComponentNode] + trenchPeripheryNodes:
        if chip.index == 0:
            trenchNode.Z = chip.substrate.node.shape.paramsDict['Height'] - trench
            trenchNode.shape.paramsDict['Height'] = trench
        elif chip.index == 1:
            trenchNode.Z = chip.substrate.node.Z
            trenchNode.shape.paramsDict['Height'] = trench
            # Add the trench nodes to the ansys file.
        addTrenchNodeLines = addTrenchNodeLines + ansysPolyline_Lines(
            name=trenchNode.name,
            color=trenchNode.color,
            material=trenchNode.material,
            polyline3D=[[point[0], point[1], trenchNode.Z] for point in trenchNode.polyline]
        )
    # Make the trenchPeriphery node 3D, then subtract it from the substrate.Finally, make the trenchComponent 3D
    subtractTrenchPeripheryLines = []
    for trenchPeripheryNode in trenchPeripheryNodes:
        subtractTrenchPeripheryLines = (
                subtractTrenchPeripheryLines
                + ansysSweepAlongVector_Lines(trenchPeripheryNode)
                + ansysSubtract_Lines(chip.substrate.name, trenchPeripheryNode.name)
        )

    makeTrenchComponent3DLines = (ansysSweepAlongVector_Lines(trenchComponentNode)
                                  + ansysUniteNodes([chip.substrate.node, trenchComponentNode]))

    return addTrenchNodeLines, subtractTrenchPeripheryLines, makeTrenchComponent3DLines


def ansysQ3DMake3D(simType, node):
    """This function makes the node 3D either by actually making it truly 3D,
        or assigning the thin conductor boundary condition (if simulation="2D")"""
    if simType == "3D":
        return ansysSweepAlongVector_Lines(node)
    elif simType == "2D":
        return ansysThinConductor(node)


def ansysDrawNodes(qArch, dimension):
    lines = ["oEditor = oDesign.SetActiveEditor(\"3D Modeler\")\n",
             "oModuleBoundary = oDesign.GetModule(\"BoundarySetup\")\n"]
    for chipIndex, chip in qArch.chipDict.items():
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

        for thisNode in getChipNNodes_ansysModeler(qArch, chip.index):
            lines += ansysPolyline_Lines(
                name=thisNode.name,
                color=thisNode.color,
                material=thisNode.material,
                polyline3D=[[point[0], point[1], thisNode.Z] for point in
                            thisNode.polyline]
            )
            lines += ansysQ3DMake3D(dimension, thisNode)
            # Trench round 1
            addTrenchNodeLines, subtractTrenchPeripheryLines, makeTrenchComponent3DLines = ansysTrench(
                componentNode=thisNode, trench=qArch.CPW.geometryParams["Trench"], chip=chip)
            lines += addTrenchNodeLines + subtractTrenchPeripheryLines  # Trench
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
        for thisNode in getChipNNodes_ansysModeler(qArch, chip.index):  # Trench round 2.
            addTrenchNodeLines, subtractTrenchPeripheryLines, makeTrenchComponent3DLines = ansysTrench(
                componentNode=thisNode, trench=qArch.CPW.geometryParams["Trench"], chip=chip)
            lines += makeTrenchComponent3DLines
        # For grounded qubits unite pad 2 with ground.
        for qubitIndex, qubit in qArch.allQubitsDict.items():
            if isinstance(qubit.design, GroundedRectangularTransmonSingleJJ):
                lines += ansysUniteNodes([chip.ground.outlineNode, qubit.design.pad2.node])
        # For control lines unite trace and launchpads, also unite flux bias if applicable.
        for controlLineIndex, controlLine in qArch.chipDict[chip.index].controlLineDict.items():
            if isinstance(controlLine.design, FeedLine) and qArch.sysParams["Simulate Feedline?"] == "Yes":
                uniteNodeList = [controlLine.design.lineNode]
                for launchPadName, launchPadNode in controlLine.design.launchPadNodeDict.items():
                    uniteNodeList.append(launchPadNode)
                lines += ansysUniteNodes(uniteNodeList)
                if isinstance(controlLine.design, FluxBiasLine):
                    lines += ansysUniteNodes([qArch.chipDict[0].ground.outlineNode, controlLine.design.lineNode])
        # Make the ground 3D
        lines += ansysQ3DMake3D(dimension, chip.ground.outlineNode)
    # Draw bumps if flip chip, and join the ground nodes via the bumps
    if qArch.sysParams["Flip Chip?"] == "Yes":
        uniteNodeList = [qArch.chipDict[0].ground.outlineNode, qArch.chipDict[1].ground.outlineNode]
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
    return lines


def getChipNNodes_ansysModeler(qArch, N):
    allNodes = []
    for qubitIndex, qubit in qArch.chipDict[N].qubitDict.items():
        allNodes += [pad.node for pad in qubit.design.padListGeom]
    for readoutResonatorIndex, readoutResonator in qArch.chipDict[N].readoutResonatorDict.items():
        allNodes += [readoutResonator.design.pad1.node, readoutResonator.design.pad2.node]
    for controlLineIndex, controlLine in qArch.chipDict[N].controlLineDict.items():
        if isinstance(controlLine.design, FeedLine) and qArch.sysParams["Simulate Feedline?"] == "Yes":
            allNodes.append(controlLine.design.lineNode)
            for launchPadName, launchPad in controlLine.design.launchPadNodeDict.items():
                allNodes.append(launchPad)
    return allNodes
