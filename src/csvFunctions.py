import csv
from math import floor
from ansysFunctions import ansysOutputToComplex
from constants import GHzToOmega
from scipy.interpolate import interp1d


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


def readComponentRowData(fileLines, componentName):  # Only for components that are assigned indices instead of names.
    componentDict = {}
    componentHeaderLineNumber = headerLineIndex(fileLines, componentName)
    componentHeader = fileLines[componentHeaderLineNumber]
    componentDataLineNumber = componentHeaderLineNumber + 1
    componentDataLine = fileLines[componentDataLineNumber]
    while componentDataLine[1] != "":
        componentIndex = int(componentDataLine[1])
        componentDict[componentIndex] = {}
        for parameterIndex in range(1, len(componentHeader)):
            parameterName = componentHeader[parameterIndex]
            parameterValue = componentDataLine[parameterIndex]
            componentDict[componentIndex][parameterName] = returnCorrectType(parameterValue)
        componentDataLineNumber += 1
        if componentDataLineNumber >= len(fileLines):
            break
        componentDataLine = fileLines[componentDataLineNumber]
    return componentDict


def readSingleRowData(fileLines, rowTitle):
    rowDict = dict()
    headerLineNumber = headerLineIndex(fileLines, rowTitle)
    header = fileLines[headerLineNumber]
    dataLineNumber = headerLineNumber + 1
    dataLine = fileLines[dataLineNumber]
    for parameterIndex in range(1, len(header)):
        parameterName = header[parameterIndex]
        parameterValue = dataLine[parameterIndex]
        rowDict[parameterName] = returnCorrectType(parameterValue)
    return rowDict


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
    resultsFileLines = csvRead(resultsFile)
    returnDict = dict()
    for line in resultsFileLines:
        returnDict[line[0]] = returnCorrectType(line[1])
    return returnDict


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


def readJJLocation(JJLocationCode):
    """JJLocationCode is in the form [10:-20] corresponding to a shift 10um to the right and 20um down."""
    JJLoc = [float(i) for i in JJLocationCode[1:-1].split(":")]
    return JJLoc[0], JJLoc[1]


def readQuantizeList(quantizeList):
    return [str(i) for i in quantizeList[1:-1].split(":")]


def exchQIndices(simName):
    indices = [int(i) for i in simName[5:].split("-")]
    return indices


def zzQIndices(simName):
    indices = [int(i) for i in simName[3:].split("-")]
    return indices


def Z21QIndices(simName):
    indices = [int(i) for i in simName[4:].split("-")]
    return indices
