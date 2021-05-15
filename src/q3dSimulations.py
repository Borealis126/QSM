from ansysFunctions import *
from csvFunctions import csvRead

class Q3DSim():  # capMat is a simulation that has the Q3DSim q3dExtractor
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
        lines += capMatAnalysisLines(simParams["MaxPass"], simParams["PerRefine"], self.resultsFilePath)
        lines.append(ansysSaveLine)
        self.lines = lines

    @property
    def capMatUnitsToF(self):
        reportedUnits = self.resultsFileLines[2][0][8:]  # "C Units:pF"->"pF"
        unitsMultiplier = 1
        if reportedUnits == "pF":
            unitsMultiplier = 1e-12
        return unitsMultiplier

