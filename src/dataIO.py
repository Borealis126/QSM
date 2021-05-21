import csv
from math import floor
from generalAnsysLines import ansysOutputToComplex
from constants import GHzToOmega
from scipy.interpolate import interp1d
import json


def headerLineIndex(fileLines, sectionTitle):
    headerLineNumber = 0
    for index, line in enumerate(fileLines):
        if line != [] and line[0] == sectionTitle:
            headerLineNumber = index
    return headerLineNumber


def csvRead(inputFile):
    returnLines = []
    with open(inputFile, newline='') as csvfile:
        csvReader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for line in csvReader:
            returnLines.append(line)
    return returnLines


def readY11Data(file):
    fileLines = csvRead(file)
    dataLines = fileLines[1:]
    dataLinesNumeric = [[float(line[0]), complex(ansysOutputToComplex(line[1]))] for line in
                        dataLines]  # line[0] is the frequency in GHz, line[1] is Y value
    freq = [i[0] * GHzToOmega for i in dataLinesNumeric]  # Convert to angular frequency.
    Y11 = [i[1] * 1e-3 for i in dataLinesNumeric]  # Convert from mSie to Sie
    return freq, Y11, interp1d(freq, Y11)


def readS21Data(file):
    fileLines = csvRead(file)
    dataLines = fileLines[1:]
    dataLinesNumeric = [[float(line[0]), complex(ansysOutputToComplex(line[1]))] for line in
                        dataLines]  # line[0] is the frequency in GHz, line[1] is Y value
    freq = [i[0] * GHzToOmega for i in dataLinesNumeric]  # Convert to angular frequency.
    S21 = [i[1] for i in dataLinesNumeric]
    return freq, S21, interp1d(freq, S21)


def resultsDict(resultsFile):
    return jsonRead(resultsFile)


def csvWrite(file, lines):
    fileInstance = open(file, "w", newline='')
    csvWriter = csv.writer(fileInstance)
    for line in lines:
        csvWriter.writerow(line)
    fileInstance.close()


def arrayNoBlanks(array):
    return [i for i in array if i != '']


def returnCorrectType(x):
    try:
        if floor(float(x)) == float(x):
            return int(float(x))
        else:
            return float(x)
    except:
        return str(x)


def jsonRead(file):
    with open(file, "r") as read_file:
        readDict = json.load(read_file)
    return readDict


def jsonWrite(file, writeDict):
    with open(file, "w") as write_file:
        json.dump(writeDict, write_file, indent=1)


