from polyline import pathPolyline, rectanglePolylineSet, rectanglePolyline, circlePolyline
from basicGeometry import rotate, translate
from constants import traceBuffer
from abc import ABC


class Node:  # A Node is any 3D element.
    def __init__(self, name):
        self.name = name
        self.polyline = []  # This is the polyline of the base of each node.
        self.polylineShape = "rectangle"
        self.polylineShapeParams = dict()
        self.peripheryPolylines = []
        self.meshPeripheryPolylines = []
        self.height = 0  # Only assigned and used if Q3D.
        self.Z = 0  # Height above X-Y plane.
        self.material = "perfect conductor"  # Default material.
        self.color = "(143 143 175)"  # Grey by default
        self.endPoint = []  # Only used for paths
        self.endAngle = []

    def updatePolylines(self):  # Once polylineShapeParams is loaded update the polyline and peripheryPolyline
        shapeParams = self.polylineShapeParams
        if self.polylineShape[0:9] == "rectangle":  # Pre-rotation the fingers point up and JJ elements point down.
            # Pad is centered on 0,0 to start as normalization. Rotated later.
            padPolyline, padPeripheryPolyline, padMeshPeripheryPolyline = rectanglePolylineSet(
                centerX=0,
                centerY=0,
                width=shapeParams["Body Width"],
                length=shapeParams["Body Length"],
                side1Boundary=shapeParams["Side 1 Boundary"],
                side2Boundary=shapeParams["Side 2 Boundary"],
                side3Boundary=shapeParams["Side 3 Boundary"],
                side4Boundary=shapeParams["Side 4 Boundary"],
                meshBoundary=shapeParams["Mesh Boundary"],
                angle=0
            )
            component = padPolyline
            peripheryPolylines = [padPeripheryPolyline]
            meshPeripheryPolylines = [padMeshPeripheryPolyline]
            if "PlusSingleJJ" in self.polylineShape:
                stemPolyline, stemPeripheryPolyline, stemMeshPeripheryPolyline = rectanglePolylineSet(
                    centerX=shapeParams["JJ Stem X"],
                    centerY=-shapeParams["Body Length"] / 2 - shapeParams["JJ Stem Length"] / 2,
                    width=shapeParams["JJ Stem Width"],
                    length=shapeParams["JJ Stem Length"],
                    side1Boundary=shapeParams["JJ Stem Side Boundary"],
                    side2Boundary=0,
                    side3Boundary=shapeParams["JJ Stem Side Boundary"],
                    side4Boundary=shapeParams["JJ Stem End Boundary"],
                    meshBoundary=shapeParams["Mesh Boundary"],
                    angle=0
                )
                """The stem is now added after the last rectangle polyline point in such a way that 
                the full component has the correct polyline ordering."""
                # Due to the order in which a rectangle polyline is defined.
                component += [stemPolyline[2], stemPolyline[3], stemPolyline[0], stemPolyline[1]]
                peripheryPolylines.append(stemPeripheryPolyline)
                meshPeripheryPolylines.append(stemMeshPeripheryPolyline)
            elif "PlusDoubleJJ" in self.polylineShape:
                # Available values
                # "SQUID Stem Separation"
                # "SQUID T Head Width"
                # "SQUID T Head Length"
                # "JJ Boundary"
                # "SQUID T Stem Length"
                # "SQUID Stem Width"
                # "SQUID Stem Length"
                # "SQUID T Stem Width"
                # "SQUID T Stem Length"
                # T Stem
                JJTStemPolyline, JJTStemPeripheryPolyline, JJTStemMeshPeripheryPolyline = \
                    rectanglePolylineSet(
                        centerX=shapeParams["JJ Stem X"],
                        centerY=-shapeParams["Body Length"] / 2 - shapeParams["SQUID T Stem Length"] / 2,
                        width=shapeParams["SQUID T Stem Width"],
                        length=shapeParams["SQUID T Stem Length"],
                        side1Boundary=shapeParams["JJ Boundary"],
                        side2Boundary=0,
                        side3Boundary=shapeParams["JJ Boundary"],
                        side4Boundary=shapeParams["JJ Boundary"],
                        meshBoundary=shapeParams["Mesh Boundary"],
                        angle=0
                    )
                # T Head
                JJTHeadPolyline, JJTHeadPeripheryPolyline, JJTHeadMeshPeripheryPolyline = \
                    rectanglePolylineSet(
                        centerX=shapeParams["JJ Stem X"],
                        centerY=(-shapeParams["Body Length"] / 2
                                 - shapeParams["SQUID T Stem Length"]
                                 - shapeParams["SQUID T Head Length"] / 2),
                        width=shapeParams["SQUID T Head Width"],
                        length=shapeParams["SQUID T Head Length"],
                        side1Boundary=shapeParams["JJ Boundary"],
                        side2Boundary=shapeParams["JJ Boundary"],
                        side3Boundary=shapeParams["JJ Boundary"],
                        side4Boundary=shapeParams["JJ Boundary"],
                        meshBoundary=shapeParams["Mesh Boundary"],
                        angle=0
                    )
                # JJ Squid Right Stem
                JJSquidRightStemPolyline, JJSquidRightStemPeripheryPolyline, JJSquidRightStemMeshPeripheryPolyline = \
                    rectanglePolylineSet(
                        centerX=shapeParams["JJ Stem X"] + shapeParams["SQUID Stem Separation"] / 2,
                        centerY=(-shapeParams["Body Length"] / 2
                                 - shapeParams["SQUID T Stem Length"]
                                 - shapeParams["SQUID T Head Length"]
                                 - shapeParams["SQUID Stem Length"] / 2),
                        width=shapeParams["SQUID Stem Width"],
                        length=shapeParams["SQUID Stem Length"],
                        side1Boundary=shapeParams["JJ Boundary"],
                        side2Boundary=shapeParams["JJ Boundary"],
                        side3Boundary=shapeParams["JJ Boundary"],
                        side4Boundary=shapeParams["JJ Boundary"],
                        meshBoundary=shapeParams["Mesh Boundary"],
                        angle=0
                    )
                # JJ Squid Left Stem
                JJSquidLeftStemPolyline, JJSquidLeftStemPeripheryPolyline, JJSquidLeftStemMeshPeripheryPolyline = \
                    rectanglePolylineSet(
                        centerX=(shapeParams["JJ Stem X"] - shapeParams["SQUID Stem Separation"] / 2),
                        centerY=(-shapeParams["Body Length"] / 2
                                 - shapeParams["SQUID T Stem Length"]
                                 - shapeParams["SQUID T Head Length"]
                                 - shapeParams["SQUID Stem Length"] / 2),
                        width=shapeParams["SQUID Stem Width"],
                        length=shapeParams["SQUID Stem Length"],
                        side1Boundary=shapeParams["JJ Boundary"],
                        side2Boundary=shapeParams["JJ Boundary"],
                        side3Boundary=shapeParams["JJ Boundary"],
                        side4Boundary=shapeParams["JJ Boundary"],
                        meshBoundary=shapeParams["Mesh Boundary"],
                        angle=0
                    )
                component += [
                    JJTStemPolyline[2], JJTStemPolyline[3],
                    JJTHeadPolyline[2], JJTHeadPolyline[3],
                    JJSquidRightStemPolyline[2], JJSquidRightStemPolyline[3], JJSquidRightStemPolyline[0],
                    JJSquidRightStemPolyline[1],
                    JJSquidLeftStemPolyline[2], JJSquidLeftStemPolyline[3], JJSquidLeftStemPolyline[0],
                    JJSquidLeftStemPolyline[1],
                    JJTHeadPolyline[0], JJTHeadPolyline[1],
                    JJTStemPolyline[0], JJTStemPolyline[1]
                ]
                peripheryPolylines += [JJTStemPeripheryPolyline, JJTHeadPeripheryPolyline,
                                       JJSquidRightStemPeripheryPolyline, JJSquidLeftStemPeripheryPolyline]
                meshPeripheryPolylines += [JJTStemMeshPeripheryPolyline, JJTHeadMeshPeripheryPolyline,
                                           JJSquidRightStemMeshPeripheryPolyline, JJSquidLeftStemMeshPeripheryPolyline]
            if "PlusFinger(s)" in self.polylineShape:  # Stems are bottom of rectangle, fingers are top.
                numFingers = shapeParams["Number of Fingers"]
                fingerSpacing = shapeParams["Finger Spacing"]
                # The fingers are all inserted between component[1] and component[2]
                componentLeft = component[0:2]
                componentRight = component[2:]
                # Fingers are indexed left to right along the top of the rectangle.
                for fingerIndex in range(numFingers):
                    # First make the stem of each finger.
                    fingerStemPolyline, fingerStemPeripheryPolyline, fingerStemMeshPeripheryPolyline = \
                        rectanglePolylineSet(
                            centerX=-(numFingers - 1) * fingerSpacing / 2 + fingerIndex * fingerSpacing,
                            centerY=(shapeParams["Body Length"] / 2 +
                                     shapeParams["Finger " + str(fingerIndex) + " Stem Length"] / 2),
                            width=shapeParams["Finger " + str(fingerIndex) + " Stem Width"],
                            length=shapeParams["Finger " + str(fingerIndex) + " Stem Length"],
                            side1Boundary=shapeParams["Finger Stem Boundary"],
                            side2Boundary=shapeParams["Finger Stem Boundary"],
                            side3Boundary=shapeParams["Finger Stem Boundary"],
                            side4Boundary=shapeParams["Finger Stem Boundary"],
                            meshBoundary=shapeParams["Mesh Boundary"],
                            angle=0
                        )
                    # Then make the T
                    fingerTPolyline, fingerTPeripheryPolyline, fingerTMeshPeripheryPolyline = rectanglePolylineSet(
                        centerX=-(numFingers - 1) * fingerSpacing / 2 + fingerIndex * fingerSpacing,
                        centerY=(shapeParams["Body Length"] / 2
                                 + shapeParams["Finger " + str(fingerIndex) + " Stem Length"]
                                 + shapeParams["Finger " + str(fingerIndex) + " T Head Length"] / 2),
                        width=shapeParams["Finger " + str(fingerIndex) + " T Width"],
                        length=shapeParams["Finger " + str(fingerIndex) + " T Head Length"],
                        side1Boundary=shapeParams["Finger " + str(fingerIndex) + " T Side 1 Boundary"],
                        side2Boundary=shapeParams["Finger " + str(fingerIndex) + " T Side 2 Boundary"],
                        side3Boundary=shapeParams["Finger " + str(fingerIndex) + " T Side 3 Boundary"],
                        side4Boundary=shapeParams["Finger " + str(fingerIndex) + " T Side 4 Boundary"],
                        meshBoundary=shapeParams["Mesh Boundary"],
                        angle=0
                    )
                    componentLeft += [
                        fingerStemPolyline[0], fingerStemPolyline[1],
                        fingerTPolyline[0], fingerTPolyline[1], fingerTPolyline[2], fingerTPolyline[3],
                        fingerStemPolyline[2], fingerStemPolyline[3]
                    ]
                    peripheryPolylines += [fingerStemPeripheryPolyline, fingerTPeripheryPolyline]
                    meshPeripheryPolylines += [fingerStemMeshPeripheryPolyline, fingerTMeshPeripheryPolyline]
                component = componentLeft + componentRight
            if "sideT" in self.polylineShape:
                leftSideTPolyline, leftSideTPeripheryPolyline, leftSideTMeshPeripheryPolyline = rectanglePolylineSet(
                    centerX=-shapeParams["Body Width"] / 2 - shapeParams["Side T Width"] / 2,
                    centerY=0,
                    width=shapeParams["Side T Width"],
                    length=shapeParams["Side T Length"],
                    side1Boundary=shapeParams["Side T Boundary"],
                    side2Boundary=shapeParams["Side T Boundary"],
                    side3Boundary=shapeParams["Side T Boundary"],
                    side4Boundary=shapeParams["Side T Boundary"],
                    meshBoundary=shapeParams["Mesh Boundary"],
                    angle=0
                )
                rightSideTPolyline, rightSideTPeripheryPolyline, rightSideTMeshPeripheryPolyline = rectanglePolylineSet(
                    centerX=shapeParams["Body Width"] / 2 + shapeParams["Side T Width"] / 2,
                    centerY=0,
                    width=shapeParams["Side T Width"],
                    length=shapeParams["Side T Length"],
                    side1Boundary=shapeParams["Side T Boundary"],
                    side2Boundary=shapeParams["Side T Boundary"],
                    side3Boundary=shapeParams["Side T Boundary"],
                    side4Boundary=shapeParams["Side T Boundary"],
                    meshBoundary=shapeParams["Mesh Boundary"],
                    angle=0
                )

                componentLeft = [component[0]]
                componentRight = component[1:]

                componentLeft += [leftSideTPolyline[3], leftSideTPolyline[0], leftSideTPolyline[1],
                                  leftSideTPolyline[2]]
                component = componentLeft + componentRight

                componentLeft = component[0:7]
                componentRight = component[7:]
                if len(componentRight) == 1:
                    componentRight = [component[7:]]
                componentLeft += [rightSideTPolyline[1], rightSideTPolyline[2], rightSideTPolyline[3],
                                  rightSideTPolyline[0]]
                component = componentLeft + componentRight

                peripheryPolylines += [leftSideTPeripheryPolyline, rightSideTPeripheryPolyline]
                meshPeripheryPolylines += [leftSideTMeshPeripheryPolyline, rightSideTMeshPeripheryPolyline]

            """Finally rotate every point in the unrotated components about the origin (center of the body rectangle), 
            then translate them accordingly"""
            self.polyline = [translate(rotate(point, shapeParams["Angle"]),
                                       shapeParams["Body Center X"],
                                       shapeParams["Body Center Y"])
                             for point in component]
            for periphery in peripheryPolylines:
                self.peripheryPolylines.append([translate(rotate(point, shapeParams["Angle"]),
                                                          shapeParams["Body Center X"],
                                                          shapeParams["Body Center Y"])
                                                for point in periphery])
            for meshPeriphery in meshPeripheryPolylines:
                self.meshPeripheryPolylines.append([translate(rotate(point, shapeParams["Angle"]),
                                                              shapeParams["Body Center X"],
                                                              shapeParams["Body Center Y"])
                                                    for point in meshPeriphery])
        if self.polylineShape == "circle":
            self.polyline = circlePolyline(
                centerX=shapeParams["Center X"],
                centerY=shapeParams["Center Y"],
                diameter=shapeParams["Diameter"]
            )
            self.peripheryPolylines.append(circlePolyline(
                centerX=shapeParams["Center X"],
                centerY=shapeParams["Center Y"],
                diameter=shapeParams["Diameter"] + shapeParams["Boundary"] / 2)
            )
            self.meshPeripheryPolylines.append(circlePolyline(
                centerX=shapeParams["Center X"],
                centerY=shapeParams["Center Y"],
                diameter=shapeParams["Diameter"] + shapeParams["Mesh Boundary"] / 2)
            )
        if self.polylineShape == "path":
            width = shapeParams["CPW"].geometryParams["Width"]
            peripheryWidth = (shapeParams["CPW"].geometryParams["Width"] + 2 *
                              shapeParams["CPW"].geometryParams["Gap"])

            polyline, endPoint, endAngle = pathPolyline(
                width=width,
                startPoint=[shapeParams["Start X"], shapeParams["Start Y"]],
                startAngle=shapeParams["Start Angle"],
                sectionCode=shapeParams["Section Code"]
            )
            peripheryPolyline, endPointPeriphery, endAnglePeriphery = pathPolyline(
                width=peripheryWidth,
                startPoint=[shapeParams["Start X"], shapeParams["Start Y"]],
                startAngle=shapeParams["Start Angle"],
                sectionCode=shapeParams["Section Code"] + "(S:" + str(traceBuffer) + ")"
            )
            meshPeripheryPolyline, endPointMeshPeriphery, endAngleMeshPeriphery = pathPolyline(
                width=peripheryWidth + 2 * shapeParams["Mesh Boundary"],
                startPoint=[shapeParams["Start X"], shapeParams["Start Y"]],
                startAngle=shapeParams["Start Angle"],
                sectionCode=shapeParams["Section Code"]
            )
            self.polyline = polyline
            self.peripheryPolylines.append(peripheryPolyline)
            self.meshPeripheryPolylines.append(meshPeripheryPolyline)
            self.endPoint = endPoint
            self.endAngle = endAngle
            # We don't need endPointPeriphery, endPointMeshPeriphery, etc. because they should be all the same.

    @property
    def segmentList(self):  # Returns the segment list of the polyline
        segList = []
        for index, point in enumerate(self.polyline):
            point1 = point
            if index == len(self.polyline) - 1:
                point2 = self.polyline[0]
            else:
                point2 = self.polyline[index + 1]
            segList.append([point1, point2])
        return segList

    @property
    def centerX(self):  # Return the x component of the centroid of the polyline points.
        return sum([i[0] for i in self.polyline]) / len(self.polyline)

    @property
    def centerY(self):  # Return the y component of the centroid of the polyline points.
        return sum([i[1] for i in self.polyline]) / len(self.polyline)


class NodeShape(ABC):
    @property
    @abstractmethod
    def params(self):
        ...

    @property
    def initialParamsDict(self):
        return dict({i: 0 for i in self.params})

    def __init__(self):
        self.paramsDict = self.initialParamsDict


class Rectangle(NodeShape):
    def __init__(self):
        super().__init__()

    @property
    def params(self):
        return ["Width", "Length", "Height", "BoundaryList"]
