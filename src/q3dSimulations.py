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


class q3dExtractor(Q3DSim):
    lines = []

    def updateLines(self, simParams):
        lines = ansysSimulatorPreamb.copy()
        lines += [
            ansysSetActiveProjectLine(self.name),
            ansysInsertQ3DExtractorLine(self.name),
            ansysSetActiveDesignLine(self.name)
        ]
        lines += self.qSys.capMatLayout_Lines()
        lines += capMatAnalysisLines(simParams["MaxPass"], simParams["PerRefine"], self.resultsFilePath)
        lines.append(ansysSaveLine)
        self.lines = lines

