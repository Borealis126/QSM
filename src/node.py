from polylineFunctions import pathPolyline,rectanglePolylineSet,rectanglePolyline,circlePolyline
from basicGeometryFunctions import rotate,translate
from constants import traceBuffer

class Node:#A Node is any 3D element. 
    def __init__(self,name):
        self.name=name
        self.polyline=[]#This is the polyline of the base of each node. 
        self.polylineShape="rectangle"
        self.polylineShapeParams=dict()
        self.peripheryPolylines=[]
        self.meshPeripheryPolylines=[]
        self.height=0#Only assigned and used if Q3D. 
        self.Z=0#Height above X-Y plane. 
        self.material="perfect conductor"#Default material.
        self.color="(143 143 175)"#Grey by default
    def updatePolylines(self):#Once polylineShapeParams is loaded update the polyline and peripheryPolyline
        if self.polylineShape[0:9]=="rectangle":#Pre-rotation the fingers point up and JJ elements point down. 
            #Pad is centered on 0,0 to start as normalization. Rotated later. 
            padPolyline,padPeripheryPolyline,padMeshPeripheryPolyline=rectanglePolylineSet(centerX=0,\
                                                                                           centerY=0,\
                                                                                           width=self.polylineShapeParams["Body Width"],\
                                                                                           length=self.polylineShapeParams["Body Length"],\
                                                                                           side1Boundary=self.polylineShapeParams["Side 1 Boundary"],\
                                                                                           side2Boundary=self.polylineShapeParams["Side 2 Boundary"],\
                                                                                           side3Boundary=self.polylineShapeParams["Side 3 Boundary"],\
                                                                                           side4Boundary=self.polylineShapeParams["Side 4 Boundary"],\
                                                                                           meshBoundary=self.polylineShapeParams["Mesh Boundary"],\
                                                                                           angle=0) 
            component=padPolyline
            peripheryPolylines=[padPeripheryPolyline]
            meshPeripheryPolylines=[padMeshPeripheryPolyline]
            if "PlusSingleJJ" in self.polylineShape:
                stemPolyline,stemPeripheryPolyline,stemMeshPeripheryPolyline=rectanglePolylineSet(centerX=self.polylineShapeParams["JJ Stem X"],\
                                                                                                  centerY=-self.polylineShapeParams["Body Length"]/2-self.polylineShapeParams["JJ Stem Length"]/2,\
                                                                                                  width=self.polylineShapeParams["JJ Stem Width"],\
                                                                                                  length=self.polylineShapeParams["JJ Stem Length"],\
                                                                                                  side1Boundary=self.polylineShapeParams["JJ Stem Side Boundary"],\
                                                                                                  side2Boundary=0,\
                                                                                                  side3Boundary=self.polylineShapeParams["JJ Stem Side Boundary"],\
                                                                                                  side4Boundary=self.polylineShapeParams["JJ Stem End Boundary"],\
                                                                                                  meshBoundary=self.polylineShapeParams["Mesh Boundary"],\
                                                                                                  angle=0)
                #The stem is now added after the last rectangle polyline point in such a way that the full component has the correct polyline ordering. 
                component+=[stemPolyline[2],stemPolyline[3],stemPolyline[0],stemPolyline[1]]#Due to the order in which a rectangle polyline is defined. 
                peripheryPolylines.append(stemPeripheryPolyline)
                meshPeripheryPolylines.append(stemMeshPeripheryPolyline) 
            elif "PlusDoubleJJ" in self.polylineShape:
                #Available values
                #"SQUID Stem Separation"
                #"SQUID T Head Width"
                #"SQUID T Head Length"
                #"JJ Boundary"
                #"SQUID T Stem Length"
                #"SQUID Stem Width"
                #"SQUID Stem Length"
                #"SQUID T Stem Width"
                #"SQUID T Stem Length"
                #T Stem
                JJTStemPolyline,\
                JJTStemPeripheryPolyline,\
                JJTStemMeshPeripheryPolyline=rectanglePolylineSet(centerX=self.polylineShapeParams["JJ Stem X"],\
                                                                  centerY=-self.polylineShapeParams["Body Length"]/2\
                                                                          -self.polylineShapeParams["SQUID T Stem Length"]/2,\
                                                                  width=self.polylineShapeParams["SQUID T Stem Width"],\
                                                                  length=self.polylineShapeParams["SQUID T Stem Length"],\
                                                                  side1Boundary=self.polylineShapeParams["JJ Boundary"],\
                                                                  side2Boundary=0,\
                                                                  side3Boundary=self.polylineShapeParams["JJ Boundary"],\
                                                                  side4Boundary=self.polylineShapeParams["JJ Boundary"],\
                                                                  meshBoundary=self.polylineShapeParams["Mesh Boundary"],\
                                                                  angle=0)
                #T Head
                JJTHeadPolyline,\
                JJTHeadPeripheryPolyline,\
                JJTHeadMeshPeripheryPolyline=rectanglePolylineSet(centerX=self.polylineShapeParams["JJ Stem X"],\
                                                                  centerY=-self.polylineShapeParams["Body Length"]/2\
                                                                          -self.polylineShapeParams["SQUID T Stem Length"]
                                                                          -self.polylineShapeParams["SQUID T Head Length"]/2,\
                                                                  width=self.polylineShapeParams["SQUID T Head Width"],\
                                                                  length=self.polylineShapeParams["SQUID T Head Length"],\
                                                                  side1Boundary=self.polylineShapeParams["JJ Boundary"],\
                                                                  side2Boundary=self.polylineShapeParams["JJ Boundary"],\
                                                                  side3Boundary=self.polylineShapeParams["JJ Boundary"],\
                                                                  side4Boundary=self.polylineShapeParams["JJ Boundary"],\
                                                                  meshBoundary=self.polylineShapeParams["Mesh Boundary"],\
                                                                  angle=0)
                #JJ Squid Right Stem
                JJSquidRightStemPolyline,\
                JJSquidRightStemPeripheryPolyline,\
                JJSquidRightStemMeshPeripheryPolyline=rectanglePolylineSet(centerX=self.polylineShapeParams["JJ Stem X"]+self.polylineShapeParams["SQUID Stem Separation"]/2,\
                                                                           centerY=-self.polylineShapeParams["Body Length"]/2\
                                                                                   -self.polylineShapeParams["SQUID T Stem Length"]
                                                                                   -self.polylineShapeParams["SQUID T Head Length"]
                                                                                   -self.polylineShapeParams["SQUID Stem Length"]/2,\
                                                                           width=self.polylineShapeParams["SQUID Stem Width"],\
                                                                           length=self.polylineShapeParams["SQUID Stem Length"],\
                                                                           side1Boundary=self.polylineShapeParams["JJ Boundary"],\
                                                                           side2Boundary=self.polylineShapeParams["JJ Boundary"],\
                                                                           side3Boundary=self.polylineShapeParams["JJ Boundary"],\
                                                                           side4Boundary=self.polylineShapeParams["JJ Boundary"],\
                                                                           meshBoundary=self.polylineShapeParams["Mesh Boundary"],\
                                                                           angle=0)
                #JJ Squid Left Stem 
                JJSquidLeftStemPolyline,\
                JJSquidLeftStemPeripheryPolyline,\
                JJSquidLeftStemMeshPeripheryPolyline=rectanglePolylineSet(centerX=self.polylineShapeParams["JJ Stem X"]-self.polylineShapeParams["SQUID Stem Separation"]/2,\
                                                                          centerY=-self.polylineShapeParams["Body Length"]/2\
                                                                                  -self.polylineShapeParams["SQUID T Stem Length"]
                                                                                  -self.polylineShapeParams["SQUID T Head Length"]
                                                                                  -self.polylineShapeParams["SQUID Stem Length"]/2,\
                                                                          width=self.polylineShapeParams["SQUID Stem Width"],\
                                                                          length=self.polylineShapeParams["SQUID Stem Length"],\
                                                                          side1Boundary=self.polylineShapeParams["JJ Boundary"],\
                                                                          side2Boundary=self.polylineShapeParams["JJ Boundary"],\
                                                                          side3Boundary=self.polylineShapeParams["JJ Boundary"],\
                                                                          side4Boundary=self.polylineShapeParams["JJ Boundary"],\
                                                                          meshBoundary=self.polylineShapeParams["Mesh Boundary"],\
                                                                          angle=0)
                component+=[JJTStemPolyline[2],JJTStemPolyline[3],\
                                JJTHeadPolyline[2],JJTHeadPolyline[3],\
                                    JJSquidRightStemPolyline[2],JJSquidRightStemPolyline[3],JJSquidRightStemPolyline[0],JJSquidRightStemPolyline[1],\
                                    JJSquidLeftStemPolyline[2],JJSquidLeftStemPolyline[3],JJSquidLeftStemPolyline[0],JJSquidLeftStemPolyline[1],\
                                JJTHeadPolyline[0],JJTHeadPolyline[1],\
                            JJTStemPolyline[0],JJTStemPolyline[1]]
                peripheryPolylines+=[JJTStemPeripheryPolyline,JJTHeadPeripheryPolyline,JJSquidRightStemPeripheryPolyline,JJSquidLeftStemPeripheryPolyline]
                meshPeripheryPolylines+=[JJTStemMeshPeripheryPolyline,JJTHeadMeshPeripheryPolyline,JJSquidRightStemMeshPeripheryPolyline,JJSquidLeftStemMeshPeripheryPolyline]
            if "PlusFinger(s)" in self.polylineShape:#Stems are bottom of rectangle, fingers are top. 
                numFingers=self.polylineShapeParams["Number of Fingers"]
                fingerSpacing=self.polylineShapeParams["Finger Spacing"]
                #The fingers are all inserted between component[1] and component[2]
                componentLeft=component[0:2]
                componentRight=component[2:]
                for fingerIndex in range(numFingers):#Fingers are indexed left to right along the top of the rectangle.
                    #First make the stem of each finger. 
                    fingerStemPolyline,fingerStemPeripheryPolyline,fingerStemMeshPeripheryPolyline=rectanglePolylineSet(centerX=-(numFingers-1)*fingerSpacing/2+fingerIndex*fingerSpacing,\
                                                                                                                        centerY=self.polylineShapeParams["Body Length"]/2+\
                                                                                                                                self.polylineShapeParams["Finger "+str(fingerIndex)+" Stem Length"]/2,\
                                                                                                                        width=self.polylineShapeParams["Finger "+str(fingerIndex)+" Stem Width"],\
                                                                                                                        length=self.polylineShapeParams["Finger "+str(fingerIndex)+" Stem Length"],\
                                                                                                                        side1Boundary=self.polylineShapeParams["Finger Stem Boundary"],\
                                                                                                                        side2Boundary=self.polylineShapeParams["Finger Stem Boundary"],\
                                                                                                                        side3Boundary=self.polylineShapeParams["Finger Stem Boundary"],\
                                                                                                                        side4Boundary=self.polylineShapeParams["Finger Stem Boundary"],\
                                                                                                                        meshBoundary=self.polylineShapeParams["Mesh Boundary"],\
                                                                                                                        angle=0)
                    #Then make the T
                    fingerTPolyline,fingerTPeripheryPolyline,fingerTMeshPeripheryPolyline=rectanglePolylineSet(centerX=-(numFingers-1)*fingerSpacing/2+fingerIndex*fingerSpacing,\
                                                                                                               centerY=self.polylineShapeParams["Body Length"]/2+\
                                                                                                                       self.polylineShapeParams["Finger "+str(fingerIndex)+" Stem Length"]+\
                                                                                                                       self.polylineShapeParams["Finger "+str(fingerIndex)+" T Head Length"]/2,\
                                                                                                               width=self.polylineShapeParams["Finger "+str(fingerIndex)+" T Width"],\
                                                                                                               length=self.polylineShapeParams["Finger " +str(fingerIndex)+" T Head Length"],\
                                                                                                               side1Boundary=self.polylineShapeParams["Finger "+str(fingerIndex)+" T Side 1 Boundary"],\
                                                                                                               side2Boundary=self.polylineShapeParams["Finger "+str(fingerIndex)+" T Side 2 Boundary"],\
                                                                                                               side3Boundary=self.polylineShapeParams["Finger "+str(fingerIndex)+" T Side 3 Boundary"],\
                                                                                                               side4Boundary=self.polylineShapeParams["Finger "+str(fingerIndex)+" T Side 4 Boundary"],\
                                                                                                               meshBoundary=self.polylineShapeParams["Mesh Boundary"],\
                                                                                                               angle=0)
                    componentLeft+=[fingerStemPolyline[0],fingerStemPolyline[1],\
                                        fingerTPolyline[0],fingerTPolyline[1],fingerTPolyline[2],fingerTPolyline[3],\
                                    fingerStemPolyline[2],fingerStemPolyline[3]]
                    peripheryPolylines+=[fingerStemPeripheryPolyline,fingerTPeripheryPolyline]
                    meshPeripheryPolylines+=[fingerStemMeshPeripheryPolyline,fingerTMeshPeripheryPolyline]
                component=componentLeft+componentRight
            if "sideT" in self.polylineShape:
                leftSideTPolyline,leftSideTPeripheryPolyline,leftSideTMeshPeripheryPolyline=rectanglePolylineSet(centerX=-self.polylineShapeParams["Body Width"]/2-self.polylineShapeParams["Side T Width"]/2,\
                                                                                                                 centerY=0,\
                                                                                                                 width=self.polylineShapeParams["Side T Width"],\
                                                                                                                 length=self.polylineShapeParams["Side T Length"],\
                                                                                                                 side1Boundary=self.polylineShapeParams["Side T Boundary"],\
                                                                                                                 side2Boundary=self.polylineShapeParams["Side T Boundary"],\
                                                                                                                 side3Boundary=self.polylineShapeParams["Side T Boundary"],\
                                                                                                                 side4Boundary=self.polylineShapeParams["Side T Boundary"],\
                                                                                                                 meshBoundary=self.polylineShapeParams["Mesh Boundary"],\
                                                                                                                 angle=0)
                rightSideTPolyline,rightSideTPeripheryPolyline,rightSideTMeshPeripheryPolyline=rectanglePolylineSet(centerX=self.polylineShapeParams["Body Width"]/2+self.polylineShapeParams["Side T Width"]/2,\
                                                                                                                    centerY=0,\
                                                                                                                    width=self.polylineShapeParams["Side T Width"],\
                                                                                                                    length=self.polylineShapeParams["Side T Length"],\
                                                                                                                    side1Boundary=self.polylineShapeParams["Side T Boundary"],\
                                                                                                                    side2Boundary=self.polylineShapeParams["Side T Boundary"],\
                                                                                                                    side3Boundary=self.polylineShapeParams["Side T Boundary"],\
                                                                                                                    side4Boundary=self.polylineShapeParams["Side T Boundary"],\
                                                                                                                    meshBoundary=self.polylineShapeParams["Mesh Boundary"],\
                                                                                                                    angle=0)
                
                componentLeft=[component[0]]
                componentRight=component[1:]
                
                componentLeft+=[leftSideTPolyline[3],leftSideTPolyline[0],leftSideTPolyline[1],leftSideTPolyline[2]]
                component=componentLeft+componentRight
                
                
                componentLeft=component[0:7]
                componentRight=component[7:]
                if len(componentRight)==1:
                    componentRight=[component[7:]]
                componentLeft+=[rightSideTPolyline[1],rightSideTPolyline[2],rightSideTPolyline[3],rightSideTPolyline[0]]
                component=componentLeft+componentRight
                
                peripheryPolylines+=[leftSideTPeripheryPolyline,rightSideTPeripheryPolyline]
                meshPeripheryPolylines+=[leftSideTMeshPeripheryPolyline,rightSideTMeshPeripheryPolyline]
                
            #Finally rotate every point in the unrotated components about the origin (center of the body rectangle), then translate them accordingly
            self.polyline=[translate(rotate(point,self.polylineShapeParams["Angle"]),\
                                     self.polylineShapeParams["Body Center X"],\
                                     self.polylineShapeParams["Body Center Y"]) for point in component]
            for periphery in peripheryPolylines:
                self.peripheryPolylines.append([translate(rotate(point,self.polylineShapeParams["Angle"]),\
                                                               self.polylineShapeParams["Body Center X"],\
                                                               self.polylineShapeParams["Body Center Y"]) for point in periphery])
            for meshPeriphery in meshPeripheryPolylines:
                self.meshPeripheryPolylines.append([translate(rotate(point,self.polylineShapeParams["Angle"]),\
                                                           self.polylineShapeParams["Body Center X"],\
                                                           self.polylineShapeParams["Body Center Y"]) for point in meshPeriphery])
        if self.polylineShape=="circle":
            self.polyline=circlePolyline(centerX=self.polylineShapeParams["Center X"],\
                                         centerY=self.polylineShapeParams["Center Y"],\
                                         diameter=self.polylineShapeParams["Diameter"])
            self.peripheryPolylines.append(circlePolyline(centerX=self.polylineShapeParams["Center X"],\
                                                          centerY=self.polylineShapeParams["Center Y"],\
                                                          diameter=self.polylineShapeParams["Diameter"]+self.polylineShapeParams["Boundary"]/2))
            self.meshPeripheryPolylines.append(circlePolyline(centerX=self.polylineShapeParams["Center X"],\
                                                              centerY=self.polylineShapeParams["Center Y"],\
                                                              diameter=self.polylineShapeParams["Diameter"]+self.polylineShapeParams["Mesh Boundary"]/2))
        if self.polylineShape=="path":
            width=self.polylineShapeParams["CPW"].geometryParamsDict["Width"]
            peripheryWidth=self.polylineShapeParams["CPW"].geometryParamsDict["Width"]+2*self.polylineShapeParams["CPW"].geometryParamsDict["Gap"]
            
            polyline,endPoint,endAngle=pathPolyline(width=width,\
                                                    startPoint=[self.polylineShapeParams["Start X"],self.polylineShapeParams["Start Y"]],\
                                                    startAngle=self.polylineShapeParams["Start Angle"],\
                                                    sectionCode=self.polylineShapeParams["Section Code"])
            peripheryPolyline,endPointPeriphery,endAnglePeriphery=pathPolyline(width=peripheryWidth,\
                                                                               startPoint=[self.polylineShapeParams["Start X"],self.polylineShapeParams["Start Y"]],\
                                                                               startAngle=self.polylineShapeParams["Start Angle"],\
                                                                               sectionCode=self.polylineShapeParams["Section Code"]+"(S:"+str(traceBuffer)+")")
            meshPeripheryPolyline,endPointMeshPeriphery,endAngleMeshPeriphery=pathPolyline(width=peripheryWidth+2*self.polylineShapeParams["Mesh Boundary"],\
                                                                                           startPoint=[self.polylineShapeParams["Start X"],self.polylineShapeParams["Start Y"]],\
                                                                                           startAngle=self.polylineShapeParams["Start Angle"],\
                                                                                           sectionCode=self.polylineShapeParams["Section Code"])
            self.polyline=polyline
            self.peripheryPolylines.append(peripheryPolyline)
            self.meshPeripheryPolylines.append(meshPeripheryPolyline)
            self.endPoint=endPoint#Note that we don't need endPointPeriphery, endPointMeshPeriphery, etc. because they should be all the same. 
            self.endAngle=endAngle
    @property
    def segmentList(self):#Returns the segment list of the polyline
        segList=[]
        for index,point in enumerate(self.polyline):
            point1=point
            if index==len(self.polyline)-1:
                point2=self.polyline[0]
            else:
                point2=self.polyline[index+1]
            segList.append([point1,point2])
        return segList
    @property
    def centerX(self):#Return the x component of the centroid of the polyline points. 
        return sum([i[0] for i in self.polyline])/len(self.polyline)
    @property
    def centerY(self):#Return the y component of the centroid of the polyline points. 
        return sum([i[1] for i in self.polyline])/len(self.polyline)