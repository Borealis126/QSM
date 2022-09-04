from sympy import symbols, solve
from .polyline import pathPolyline
import numpy as np
from .node import Node
from .basicGeometry import translate, rotate, arcLength


def meanderNodeGen(name, turnRadius, length, endSeparation, meanderToEndMinDist, endAngles, angle, centerX, centerY,
                   height, Z, meshBoundary, CPWObj):
    R = turnRadius
    meanderToEnd, width, numLeftHumps = symbols('meanderToPad,width,numLeftHumps')
    """Note: "Length" includes the FULL length of the end pads, 
    whereas "Distance between pads" is between their midpoints."""
    # Each of the below equations are equal to zero.
    totalLengthEq = (
            -length
            + 2 * meanderToEnd + 2 * arcLength(R, np.pi / 2)
            + 2 * (width / 2 - 2 * R)
            + numLeftHumps * (arcLength(R, np.pi) + 2 * (width - 2 * R))
            + (numLeftHumps + 1) * arcLength(R, np.pi)
    )
    endSeparationEq = -endSeparation + 2 * meanderToEnd + 2 * R + (numLeftHumps * 2 + 1) * 2 * R
    eqn = totalLengthEq - endSeparationEq
    """totalLengthEq-endSeparationEq gives us a single equation for numLeftHumps and width.
    We want it to be as narrow as possible while satisfying numLeftHumps>=1 and 
    meanderToPadSolved>self.geometryParams["Meander To Pad Minimum Distance"].
    So simply iterate upwards from numLeftHumps=1 until width no longer satisfies width>=4R or meanderToPad<0"""
    numLeftHumpsIter = 1
    solvedWidthIter = solve(eqn.subs(numLeftHumps, numLeftHumpsIter), width)[0]
    meanderToPadIter = solve(endSeparationEq.subs(numLeftHumps, numLeftHumpsIter), meanderToEnd)[0]
    bestSolution = [numLeftHumpsIter, solvedWidthIter, meanderToPadIter]
    numLeftHumpsIter += 1
    solvedWidthIter = solve(eqn.subs(numLeftHumps, numLeftHumpsIter), width)[0]
    meanderToPadIter = solve(endSeparationEq.subs(numLeftHumps, numLeftHumpsIter), meanderToEnd)[0]
    while solvedWidthIter >= 4 * R and meanderToPadIter >= meanderToEndMinDist:
        if solvedWidthIter < bestSolution[1]:
            bestSolution = [numLeftHumpsIter, solvedWidthIter, meanderToPadIter]
        numLeftHumpsIter += 1
        solvedWidthIter = solve(eqn.subs(numLeftHumps, numLeftHumpsIter), width)[0]
        meanderToPadIter = solve(endSeparationEq.subs(numLeftHumps, numLeftHumpsIter), meanderToEnd)[0]

    # bestSolution now contains the values for the smallest width
    numLeftHumpsSolved = int(bestSolution[0])
    widthSolved = float(bestSolution[1])
    meanderToPadSolved = float(bestSolution[2])
    lengthLongSegment = widthSolved - 2 * R
    lengthShortSegment = widthSolved / 2 - 2 * R
    lengthToPad = meanderToPadSolved

    # Now draw the meander
    peripheryWidth = CPWObj.geometryParams["Width"] + 2 * CPWObj.geometryParams["Gap"]
    meshPeripheryWidth = peripheryWidth + 2 * meshBoundary

    traceWidth = CPWObj.geometryParams["Width"]

    """Addition of 3*pi/2 is because we think of the resonators as oriented along the y-axis pre-rotation, 
    and it starts moving downward."""
    startAngle = angle + 3 * np.pi / 2

    sectionCode = ""
    normalizedStartPoint = np.array([0, endSeparation / 2 - lengthToPad])  # normalized = pre rotation.
    # Initial length
    curveAngle = endAngles[0]
    if curveAngle == 0:
        normalizedStartPoint[1] += lengthToPad
        sectionCode = sectionCode + segmentCode(length=lengthToPad)
    else:
        # Notation and equations from https://mathworld.wolfram.com/CircularSegment.html
        R_seg = np.abs(lengthToPad / curveAngle)
        r = R_seg * np.cos(curveAngle / 2)
        h = R_seg - r
        a = 2 * np.sqrt(h * (2 * R_seg - r))
        innerTheta = (np.pi - np.abs(curveAngle)) / 2
        deltaX = a * np.cos(innerTheta)
        deltaY = a * np.sin(innerTheta)
        normalizedStartPoint = np.array([normalizedStartPoint[0] - deltaX * curveAngle / np.abs(curveAngle),
                                         normalizedStartPoint[1] + deltaY])  # Corrects for sign of curveAngle
        sectionCode = sectionCode + turnCode(turnAngle=-curveAngle, turnRadius=R_seg)
        startAngle += curveAngle

    startPoint = translate(rotate(normalizedStartPoint, angle), centerX, centerY)
    angle = startAngle
    # First turn to the left
    sectionCode += turnCode(turnAngle=np.pi / 2, turnRadius=R)

    angle = angle + np.pi / 2
    sectionCode += segmentCode(length=lengthShortSegment)
    # Bulk of meander (humps)
    for i in range(numLeftHumpsSolved):  # Right turn followed by left turn
        # First turn to the right
        sectionCode += turnCode(turnAngle=-np.pi, turnRadius=R)
        angle = angle + np.pi
        sectionCode += segmentCode(length=lengthLongSegment)
        # Turn to the left
        sectionCode += turnCode(turnAngle=np.pi, turnRadius=R)
        # Second straight segment
        angle = angle + np.pi
        sectionCode += segmentCode(length=lengthLongSegment)
    # Add the last few turns
    sectionCode += turnCode(turnAngle=-np.pi, turnRadius=R)
    angle = angle + np.pi
    sectionCode += segmentCode(length=lengthShortSegment)
    sectionCode += turnCode(turnAngle=np.pi / 2, turnRadius=R)
    angle = angle + np.pi / 2
    # Final length
    curveAngle = endAngles[1]
    if curveAngle == 0:
        sectionCode += segmentCode(length=lengthToPad)
    else:
        # Notation and equations from https://mathworld.wolfram.com/CircularSegment.html
        R_seg = np.abs(lengthToPad / curveAngle)
        sectionCode += turnCode(turnAngle=curveAngle, turnRadius=R_seg)
        angle += curveAngle

    meanderTracePolyline, endPoint, endAngle = pathPolyline(traceWidth, startPoint, startAngle, sectionCode)
    meanderPeripheryPolyline, endPoint, endAngle = pathPolyline(peripheryWidth, startPoint, startAngle, sectionCode)
    meanderMeshPeripheryPolyline, endPoint, endAngle = pathPolyline(meshPeripheryWidth, startPoint, startAngle,
                                                                    sectionCode)

    meanderNode = Node(name, 'Path')
    meanderNode.polyline = meanderTracePolyline
    meanderNode.peripheryPolylines.append(meanderPeripheryPolyline)
    meanderNode.meshPeripheryPolylines.append(meanderMeshPeripheryPolyline)
    meanderNode.shape.paramsDict['Height'] = height
    meanderNode.Z = Z
    return meanderNode, startPoint, startAngle, endPoint, endAngle


def segmentCode(length):
    return "(S:" + str(length) + ")"


def turnCode(turnAngle, turnRadius):
    return "(R:" + str(turnAngle) + ":" + str(turnRadius) + ")"
