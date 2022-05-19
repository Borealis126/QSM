# Import modules
import sys
import os

computeLocation = "Wendian"
QSMSourceFolder = ""
if computeLocation == "68707Max":
    QSMSourceFolder = "O:/68707/JoelHoward/ChipDesign/QSMSource/"
elif computeLocation == "Wendian":
    QSMSourceFolder = "/beegfs/scratch/joelhoward/QSMSimulations/QSMSource/"
sys.path.append(QSMSourceFolder)
import qubitSimulationModule as QSM

projectPath = os.path.dirname(os.path.abspath(__file__)) + "/.."
projectFolder = projectPath.replace("\\", "/")
# -------------Capacitance Matrix,CPW Simulation, and generateGDS------------
qArch = QSM.initialize(projectFolder, computeLocation, QSMSourceFolder)
qArch.simulationCommand(["simulation", "quantize", "postProcess"])
