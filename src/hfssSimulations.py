from generalAnsysLines import *


class HFSSSim:
    def __init__(self, simName, simDirectory):
        # "capMatExtractor" is the name, but the type is q3dExtractor
        self.name = simName
        self.aedtPath = simDirectory / (simName + ".aedt")
        self.simulatorPath = simDirectory / (simName + "_" + "Simulator.py")
        self.logPath = simDirectory / (simName + "_" + "Simulator.log")
        self.resultsFilePath = simDirectory / (simName + "_" + "Results.csv")
        self.aedtFolderPath = simDirectory / "q3dExtractor.aedtresults"
        self.lines = []


class HFSSModeler(HFSSSim):
    lines = []

    def updateLines(self, capMatLines):
        lines = ansysSimulatorPreamb.copy()
        lines += [
            ansysSetActiveProjectLine(self.name),
            ansysInsertHFSSDesignLine(self.name),
            ansysSetActiveDesignLine(self.name)
        ]
        lines += capMatLines
        lines.append(ansysSaveLine)
        self.lines = lines

    @property
    def capMatUnitsToF(self):
        reportedUnits = self.resultsFileLines[2][0][8:]  # "C Units:pF"->"pF"
        unitsMultiplier = 1
        if reportedUnits == "pF":
            unitsMultiplier = 1e-12
        return unitsMultiplier


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


def ansysInsertHFSSDesignLine(hfssSimName):
    return "oProject.InsertDesign(\"HFSS\", \"" + hfssSimName + "\", \"DrivenModal\", \"\")\n"