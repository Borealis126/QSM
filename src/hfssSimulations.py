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

