from generalAnsysLines import *
from dataIO import csvRead


class Q3DSim:  # capMat is a simulation that has the Q3DSim q3dExtractor
    def __init__(self, q3dSimName, simDirectory):
        # "capMatExtractor" is the name, but the type is q3dExtractor
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

    def updateLines(self, simParams, capMatLines):
        lines = ansysSimulatorPreamb.copy()
        lines += [
            ansysSetActiveProjectLine(self.name),
            ansysInsertQ3DExtractorLine(self.name),
            ansysSetActiveDesignLine(self.name)
        ]
        lines += capMatLines
        lines += capMatAnalysisLines(simParams["MaxPass"], simParams["PerRefine"])
        lines += radiationBoxLines
        lines.append(analyzeLine)
        lines.append(exportLine(self.resultsFilePath))
        lines.append(ansysSaveLine)
        self.lines = lines

    @property
    def capMatUnitsToF(self):
        reportedUnits = self.resultsFileLines[2][0][8:]  # "C Units:pF"->"pF"
        unitsMultiplier = 1
        if reportedUnits == "pF":
            unitsMultiplier = 1e-12
        return unitsMultiplier


def ansysInsertQ3DExtractorLine(q3dSimName):
    return "oProject.InsertDesign(\"Q3D Extractor\", \"" + q3dSimName + "\", \"\", \"\")\n"


def capMatAnalysisLines(maxPass, perRefine):
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
    ]

analyzeLine = "oDesign.AnalyzeAll()\n"

radiationBoxLines = [
    "oModule = oDesign.GetModule(\"RadField\")\n",
    "oModule.InsertBoxSetup(\n",
    "    [\n",
    "        \"NAME:Box1\",\n",
    "        \"UseCustomRadiationSurface:=\", False,\n",
    "        \"Length:=\"		, \"2mm\",\n",
    "        \"Width:=\"		, \"2mm\",\n",
    "        \"LengthSamples:=\"	, 21,\n",
    "        \"WidthSamples:=\"	, 21,\n",
    "        \"CoordSystem:=\"		, \"Global\",\n",
    "        \"Height:=\"		, \"2mm\",\n",
    "        \"HeightSamples:=\"	, 21\n",
    "    ])\n"
]

def exportLine(resultsFile):
    return "oDesign.ExportMatrixData(r\"" + str(resultsFile)\
           + "\", \"C\", \"\", \"capSim:LastAdaptive\", \"Original\", \"ohm\", \"nH\", \"pF\", \"mSie\", 5000000000, \"Maxwell,Spice,Couple\", 0, False, 5, 8, 0)\n"
