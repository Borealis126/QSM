from basicGeometryFunctions import rotate,translate,nextPointSegment
import numpy as np
def launchPadPolylines(tipPoint,angle,CPW,meshPeriphery):#startPoint is the center of where it meets the CPW
    centerPoint=nextPointSegment(tipPoint,angle+np.pi,300)
    
    padSeed=[[-100,-100],\
             [-100,100],\
             [100,100],\
             [300,CPW.geometryParamsDict["Width"]/2],\
             [300,-CPW.geometryParamsDict["Width"]/2],\
             [100,-100]]
    peripherySeed=[[-260,-260],\
                   [-260,260],\
                   [100,260],\
                   [300,CPW.geometryParamsDict["Width"]/2+CPW.geometryParamsDict["Gap"]],\
                   [300,-CPW.geometryParamsDict["Width"]/2-CPW.geometryParamsDict["Gap"]],\
                   [100,-260]]
    meshPeripherySeed=[[-260-meshPeriphery,-260-meshPeriphery],\
                       [-260-meshPeriphery,260+meshPeriphery],\
                       [100+meshPeriphery,260+meshPeriphery],\
                       [300+meshPeriphery,CPW.geometryParamsDict["Width"]/2+CPW.geometryParamsDict["Gap"]+meshPeriphery],\
                       [300+meshPeriphery,-CPW.geometryParamsDict["Width"]/2-CPW.geometryParamsDict["Gap"]-meshPeriphery],\
                       [100+meshPeriphery,-260-meshPeriphery]]
    
    padTranslated=[translate(rotate(point,angle),centerPoint[0],centerPoint[1]) for point in padSeed]
    peripheryTranslated=[translate(rotate(point,angle),centerPoint[0],centerPoint[1]) for point in peripherySeed]
    meshPeripheryTranslated=[translate(rotate(point,angle),centerPoint[0],centerPoint[1]) for point in meshPeripherySeed]
    
    return padTranslated,peripheryTranslated,meshPeripheryTranslated
def pathPolyline(width,startPoint,startAngle,sectionCode):
    interpretedSectionCode=interpretSectionCode(sectionCode)
    #Paths are restricted to alternating straight and turn segments. 
    #Commands are of the form [[length],[radius,angle],[length],[radius,angle],...]
    polylineLeft=[]
    polylineRight=[]
    angle=startAngle
    #First points
    polylineLeft.append(translate(rotate([0,width/2],angle),startPoint[0],startPoint[1])) 
    polylineRight.append(translate(rotate([0,-width/2],angle),startPoint[0],startPoint[1]))
    for section in interpretedSectionCode:
        if section["Type"]=="Segment":
            polylineLeft.append(nextPointSegment(polylineLeft[-1],angle,section["Length"]))
            polylineRight.append(nextPointSegment(polylineRight[-1],angle,section["Length"]))
        elif section["Type"]=="Turn":
            pointsPerRadian=50
            
            
            numPoints=int(pointsPerRadian*np.abs(section["Turn Angle"]))
            dTheta=section["Turn Angle"]/numPoints
            actualWidth=width*np.cos(dTheta/2)
            #innerTurnRadius=section["Turn Radius"]-actualWidth/2
            #outerTurnRadius=section["Turn Radius"]+actualWidth/2
            innerTurnRadius=section["Turn Radius"]-width/2
            outerTurnRadius=section["Turn Radius"]+width/2
            turnStartAngle=angle
            for i in range(numPoints):#Add points along the turn
                if i==0:
                    angle=angle+dTheta/2
                else:
                    angle=angle+dTheta
                innerTurnLength=2*innerTurnRadius*np.sin(np.abs(dTheta)/2)
                outerTurnLength=2*outerTurnRadius*np.sin(np.abs(dTheta)/2)

                if section["Turn Angle"]>0:
                    turnRadiusLeft=innerTurnRadius
                    turnLengthLeft=innerTurnLength
                    turnRadiusRight=outerTurnRadius
                    turnLengthRight=outerTurnLength
                elif section["Turn Angle"]<0:
                    turnRadiusLeft=outerTurnRadius
                    turnLengthLeft=outerTurnLength
                    turnRadiusRight=innerTurnRadius
                    turnLengthRight=innerTurnLength
                polylineLeft.append(nextPointSegment(polylineLeft[-1],angle,turnLengthLeft))
                polylineRight.append(nextPointSegment(polylineRight[-1],angle,turnLengthRight))
            
            angle=turnStartAngle+section["Turn Angle"]
    #Assemble polyline from polylineLeft and polylineRight
    endPoint=[(polylineLeft[-1][0]+polylineRight[-1][0])/2,\
              (polylineLeft[-1][1]+polylineRight[-1][1])/2,]#Average of the two end X and Y values.
    endAngle=angle
    polylineRight.reverse()
    return polylineLeft+polylineRight,endPoint,endAngle
def rectanglePolylineSet(centerX,centerY,width,length,side1Boundary,side2Boundary,side3Boundary,side4Boundary,meshBoundary,angle):
    peripheryCenterX=centerX+(side1Boundary-side3Boundary)/2
    peripheryCenterY=centerY+(side2Boundary-side4Boundary)/2
    peripheryWidth=width+side1Boundary+side3Boundary
    meshPeripheryWidth=peripheryWidth+2*meshBoundary
    peripheryLength=length+side2Boundary+side4Boundary
    meshPeripheryLength=peripheryLength+2*meshBoundary
    
    polyline=rectanglePolyline(centerX,centerY,width,length,angle)
    peripheryPolyline=rectanglePolyline(peripheryCenterX,peripheryCenterY,peripheryWidth,peripheryLength,angle)
    meshPeripheryPolyline=rectanglePolyline(peripheryCenterX,peripheryCenterY,meshPeripheryWidth,meshPeripheryLength,angle)
    return polyline,peripheryPolyline,meshPeripheryPolyline
def rectanglePolyline(centerX,centerY,width,length,angle):
    seed=[[-width/2,-length/2],\
          [-width/2,length/2],\
          [width/2,length/2],\
          [width/2,-length/2]]
    rotated=[rotate(point,angle) for point in seed]
    translated=[translate(point,centerX,centerY) for point in rotated]
    return translated
def circlePolyline(centerX,centerY,diameter):
    points=[]
    numPoints=10
    radius=diameter/2
    for angle in np.linspace(0,2*np.pi,numPoints):
        points.append([centerX+radius*np.cos(angle),centerY+radius*np.sin(angle)])
    return points
def multiplyPolyline(polyline,factor):
    return [[i[0]*factor,i[1]*factor] for i in polyline]
def interpretSectionCode(code):
    sections=[]
    sectionStrings=[]
    sectionIndex=1
    i=0
    while i<len(code):
        if code[i]=="(":
            currentSection=""
            i=i+1
            while code[i]!=")":
                currentSection=currentSection+code[i]
                i+=1
            sectionStrings.append(currentSection)
        i+=1
    for sectionString in sectionStrings:
        if sectionString[0]=="S":
            sections.append({"Type":"Segment",\
                             "Length":float(sectionString.split(":")[1])})
        elif sectionString[0]=="R":
            turnAngle=float(sectionString.split(":")[1])
            turnRadius=float(sectionString.split(":")[2])
            sections.append({"Type":"Turn",\
                             "Turn Angle":turnAngle,\
                             "Turn Radius":turnRadius})
    return sections