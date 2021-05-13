class HFSSSim:
    def __init__(self, hfssSimName, simDirectory):
        self.aedtPath = simDirectory / (hfssSimName + ".aedt")
        self.simulatorPath = simDirectory / (hfssSimName + "_" + "Simulator.py")
        self.logPath = simDirectory / (hfssSimName + "_" + "Simulator.log")
        self.resultsFilePath = simDirectory / (hfssSimName + "_" + "Results.csv")

