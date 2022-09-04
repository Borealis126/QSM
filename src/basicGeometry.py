from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
import numpy as np
from . import pointToLine


def nearestPoint(point, pointList):  # Point in format [x,y]
    currentNearestPoint = pointList[0]
    for testPoint in pointList:
        if distancePointPoint(testPoint, point) < distancePointPoint(currentNearestPoint, point):
            currentNearestPoint = testPoint
    return currentNearestPoint


def distancePointPoint(point1, point2):  # point1,point2 in format [x,y]
    return np.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)


def distancePointSegment(point, segment):  # Point in format [x,y], segment in format [[x,y],[x,y]]
    return pointToLine.pnt2line(point + [0], segment[0] + [0], segment[1] + [0])[
        0]  # Adding the zeros is because pnt2line is 3 dimensional.


def midpoint(point1, point2):
    return [(point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2]


def segmentBoundary(segment, boundary, resolution):
    # Return the set of points "boundary" away from "segment", on both sides of the line.
    x1 = segment[0][0]
    y1 = segment[0][1]
    x2 = segment[1][0]
    y2 = segment[1][1]
    segmentLength = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    segmentAngle = 0
    if x2 - x1 == 0:
        if y2 - y1 > 0:
            segmentAngle = np.pi / 2
        else:
            segmentAngle = -np.pi / 2
    else:
        segmentAngle = np.arctan((y2 - y1) / (x2 - x1))

    numPoints = int(segmentLength / resolution) + 1  # Round down to the nearest integer, add 1 to include start point.
    deltaX = (x2 - x1) / numPoints
    deltaY = (y2 - y1) / numPoints
    linePoints = [[x1 + deltaX * i, y1 + deltaY * i] for i in
                  range(numPoints)]  # Gives the points along the line segment.
    # Then need to extend them out perpendicularly to get the boundary points.
    boundaryPoints = []
    for point in linePoints:
        deltaX = boundary * np.sin(segmentAngle)
        deltaY = boundary * np.cos(segmentAngle)
        boundaryPoint1 = [point[0] - deltaX, point[1] + deltaY]
        boundaryPoint2 = [point[0] + deltaX, point[1] - deltaY]
        boundaryPoints = boundaryPoints + [boundaryPoint1, boundaryPoint2]

    return boundaryPoints


def vertexBoundary(vertex, boundary,
                   resolution):  # Create a circular set of points a distance "boundary" away from vertex.
    boundaryPointsList = []
    centerX = vertex[0]
    centerY = vertex[1]
    numPoints = int(2 * np.pi * boundary / resolution)
    angleList = np.linspace(0, 2 * np.pi, numPoints)
    for angle in angleList:
        x = boundary * np.cos(angle) + centerX
        y = boundary * np.sin(angle) + centerY
        boundaryPointsList.append([x, y])
    return boundaryPointsList


def pointInPolyline(point, polyline):
    shapelyPoint = Point(point[0], point[1])
    shapelyPolygon = Polygon([(i[0], i[1]) for i in polyline])
    return shapelyPolygon.contains(shapelyPoint)


def rotate(point, angle):  # Rotates a point in [x,y] format about the point [0,0] and returns in [x,y] format.
    rotationMatrix = np.array([[np.cos(angle), -np.sin(angle)],
                               [np.sin(angle), np.cos(angle)]])
    return np.transpose(np.matmul(rotationMatrix, point.transpose()))

def rotatePolyline(polyline, angle):
    return np.array([rotate(point, angle) for point in polyline])


def translate(point, x, y): #Point is an np array
    return point + np.array([x, y])


def arcLength(radius, angle):
    return radius * angle


def nextPointSegment(point, angle, length):
    """Build segment from an initial point, angle, and distance. Return the second point in the segment."""
    return [point[0] + length * np.cos(angle), point[1] + length * np.sin(angle)]
