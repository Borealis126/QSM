import subprocess
from pathlib import Path
computeLocation = "Windows"  # Edit this based on where the QSM is being run. Should be "Windows" for most users.


def copyFile(sourceFile, destinationFile):
    copyCommand = ""
    if computeLocation == "Windows":
        copyCommand = "copy " + str(Path(sourceFile)) + " " + str(Path(destinationFile))
    elif computeLocation == "Cluster":
        copyCommand = "cp " + str(Path(sourceFile)) + " " + str(Path(destinationFile))
    subprocess.call(copyCommand, shell=True)