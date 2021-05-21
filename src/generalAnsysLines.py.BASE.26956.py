from constants import lengthUnits
from node import Node

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
        "oDesign.ExportMatrixData(\""
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
    trenchComponentNode = Node(componentNode.name + "TrenchComponent")
    # These are the peripheries that will be subtracted from the substrate.
    trenchPeripheryNodes = []
    for index, peripheryPolyline in enumerate(componentNode.peripheryPolylines):
        thisNode = Node(componentNode.name + "TrenchPeriphery" + str(index))
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
            trenchNode.Z = chip.substrate.node.height - trench
            trenchNode.height = trench
        elif chip.index == 1:
            trenchNode.Z = chip.substrate.node.Z
            trenchNode.height = trench
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
