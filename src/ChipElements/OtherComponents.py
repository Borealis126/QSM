#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'a module for other components on a chip'

__author__ = 'Junling Long'

import numpy as np
import gdspy
import os

def launchPadPolyLines(tipPoint,angle,CPW,meshPeriphery):#startPoint is the center of where it meets the CPW
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

def create_dice_gap(chip_size_x=9500, chip_size_y=7500):
    conner_cut_top_right = gdspy.Polygon([(chip_size_x / 2, chip_size_y / 2), (chip_size_x / 2, chip_size_y / 2 - 20),
                                          (chip_size_x / 2 - 5, chip_size_y / 2 - 20),
                                          (chip_size_x / 2 - 5, chip_size_y / 2 - 5),
                                          (chip_size_x / 2 - 20, chip_size_y / 2 - 5),
                                          (chip_size_x / 2 - 20, chip_size_y / 2)], 1)
    conner_cut_top_left = gdspy.copy(conner_cut_top_right, 0, 0)
    conner_cut_top_left.mirror((0, 0), (0, 1))
    conner_cut_bot_right = gdspy.copy(conner_cut_top_right, 0, 0)
    conner_cut_bot_right.mirror((0, 0), (1, 0))
    conner_cut_bot_left = gdspy.copy(conner_cut_bot_right, 0, 0)
    conner_cut_bot_left.mirror((0, 0), (0, 1))

    side_cut_left = gdspy.Rectangle((chip_size_x / 2 - 20, -chip_size_y / 2 + 200),
                                    (chip_size_x / 2, chip_size_y / 2 - 200))
    side_cut_right = gdspy.copy(side_cut_left, 0, 0)
    side_cut_right.mirror((0, 0), (0, 1))

    side_cut_top = gdspy.Rectangle((- chip_size_x / 2 + 200, chip_size_y / 2 - 20),
                                   (chip_size_x / 2 - 200, chip_size_y / 2))
    side_cut_bot = gdspy.copy(side_cut_top, 0, 0)
    side_cut_bot.mirror((0, 0), (1, 0))
    dice_gap = gdspy.fast_boolean(conner_cut_top_right, conner_cut_bot_right, 'or')
    dice_gap = gdspy.fast_boolean(dice_gap, conner_cut_bot_left, 'or')
    dice_gap = gdspy.fast_boolean(dice_gap, conner_cut_top_left, 'or')
    dice_gap = gdspy.fast_boolean(dice_gap, side_cut_top, 'or')
    dice_gap = gdspy.fast_boolean(dice_gap, side_cut_right, 'or')
    dice_gap = gdspy.fast_boolean(dice_gap, side_cut_bot, 'or')
    dice_gap = gdspy.fast_boolean(dice_gap, side_cut_left, 'or')

    return dice_gap


def createPappasMarkers(chip_size_x=9500, chip_size_y=7500):
    chip_mark_sq0 = gdspy.Rectangle((-75, -75),
                                    (-75 - 24.5, -75 - 24.5))
    mark0 = gdspy.fast_boolean(chip_mark_sq0, gdspy.copy(chip_mark_sq0).translate(0, -25.5), 'or')
    mark0 = gdspy.fast_boolean(mark0, gdspy.copy(chip_mark_sq0).translate(-25.5, 0), 'or')
    mark0 = gdspy.fast_boolean(mark0, gdspy.copy(chip_mark_sq0).translate(-25.5, -25.5), 'or')
    mark0 = gdspy.fast_boolean(mark0, gdspy.Rectangle((-125, -125),
                                                      (-425, -425)), 'or')

    mark1 = gdspy.copy(mark0).rotate(np.pi / 2, center=(0, 0))
    mark2 = gdspy.copy(mark1).rotate(np.pi / 2, center=(0, 0))
    mark3 = gdspy.copy(mark2).rotate(np.pi / 2, center=(0, 0))

    mark0.translate(chip_size_x / 2, chip_size_y / 2)
    mark1.translate(-chip_size_x / 2, chip_size_y / 2)
    mark2.translate(-chip_size_x / 2, -chip_size_y / 2)
    mark3.translate(chip_size_x / 2, -chip_size_y / 2)
    chip_marker = gdspy.fast_boolean(mark0, mark1, 'or')
    chip_marker = gdspy.fast_boolean(chip_marker, mark2, 'or')
    chip_marker = gdspy.fast_boolean(chip_marker, mark3, 'or')

    return chip_marker

def import_schmidtMarker():
    path=os.path.dirname(os.path.realpath(__file__))+"\\schmidtMarkers.gds"
    lib_temp = gdspy.GdsLibrary(infile=path)
    temp_cell = lib_temp.top_level()[0]
    polygon_list = temp_cell.get_polygonsets()
    marker1 = polygon_list[0]
    marker2 = polygon_list[60]
    for layer1Polygon in [i for i in polygon_list if i.layers[0]==1]:
        marker1 = gdspy.fast_boolean(marker1, layer1Polygon, 'or')
    for layer2Polygon in [i for i in polygon_list if i.layers[0]==2]:
        marker2 = gdspy.fast_boolean(marker2, layer2Polygon, 'or')
    bounding_box_1 = marker1.get_bounding_box()
    bounding_box_2 = marker2.get_bounding_box()
    periphery1 = gdspy.Rectangle((bounding_box_1[0][0],bounding_box_1[0][1]),
                                (bounding_box_1[1][0],bounding_box_1[1][1]))
    periphery2 = gdspy.Rectangle((bounding_box_2[0][0],bounding_box_2[0][1]),
                                (bounding_box_2[1][0],bounding_box_2[1][1]))
    gdspy.current_library.remove(cell=temp_cell)
    
    return periphery1,marker1,periphery2,marker2

def import_nist_logo():
    NISTLogoPath=os.path.dirname(os.path.realpath(__file__))+"/NIST_Logo.gds"
    lib_temp = gdspy.GdsLibrary(infile=NISTLogoPath)
    temp_cell = lib_temp.top_level()[0]
    polygon_list = temp_cell.get_polygonsets()
    nist_logo = temp_cell.get_polygonsets()[0]
    for i in range(len(polygon_list)):
        nist_logo = gdspy.fast_boolean(nist_logo, polygon_list[i], 'or')
    nist_logo_bounding_box = nist_logo.get_bounding_box()
    nist_logo_periphery = gdspy.Rectangle((nist_logo_bounding_box[0][0], nist_logo_bounding_box[0][1]),
                                          (nist_logo_bounding_box[1][0], nist_logo_bounding_box[1][1]))
    gdspy.current_library.remove(cell=temp_cell)
    return nist_logo_periphery, nist_logo
    


def create_launch_pad(cpw_trace=10, cpw_gap=6, locations=[[-np.pi / 2], [0], [0]]):
    launch_pad_periphery_seed = gdspy.Rectangle((-300, -300), (300, 300))
    points_launch_pad_gap = [(-260, 260), (100, 260), (300, cpw_trace / 2 + cpw_gap),
                             (300, cpw_trace / 2), (100, 100), (-100, 100),
                             (-100, -100), (100, -100), (300, -cpw_trace / 2),
                             (300, -cpw_trace / 2 - cpw_gap), (100, -260), (-260, -260)]
    launch_pad_gap = gdspy.Polygon(points_launch_pad_gap, 1)
    launch_pad_seed = gdspy.fast_boolean(launch_pad_periphery_seed, launch_pad_gap, 'not', layer=1)
    launch_pad_periphery = gdspy.copy(launch_pad_periphery_seed)
    launch_pad = gdspy.copy(launch_pad_seed)
    launch_pad_periphery.rotate(locations[0][0]).translate(locations[1][0], locations[2][0])
    launch_pad.rotate(locations[0][0]).translate(locations[1][0], locations[2][0])
    for i in range(1, len(locations[0])):
        temp_launch_pad_periphery = gdspy.copy(launch_pad_periphery_seed)
        temp_launch_pad_periphery.rotate(locations[0][i]).translate(locations[1][i], locations[2][i])
        temp_launch_pad = gdspy.copy(launch_pad_seed)
        temp_launch_pad.rotate(locations[0][i]).translate(locations[1][i], locations[2][i])
        launch_pad_periphery = gdspy.fast_boolean(launch_pad_periphery, temp_launch_pad_periphery, 'or')
        launch_pad = gdspy.fast_boolean(launch_pad, temp_launch_pad, 'or')
    return launch_pad_periphery, launch_pad


def JJGDSComponents(top_electrode_width=0.5,\
                    bot_electrode_width=0.1,\
                    rotate=0,\
                    dx=0,\
                    dy=0,\
                    chip=1,\
                    patchLength=10):
    points_bot_electrode = [(-1.5, -3.5),\
                            (-1.5, -2),\
                            (1.25, -2),\
                            (1.25, -bot_electrode_width/2),\
                            (-1.5, -bot_electrode_width/2),\
                            (-1.5, bot_electrode_width/2),
                            (1.5, bot_electrode_width/2),\
                            (1.5, -3.5),\
                            (-1, -3.5)]
    points_top_electrode = [(1.5, 3.5),\
                            (1.5, 2),\
                            (top_electrode_width/2, 2),\
                            (top_electrode_width/2, -1),\
                            (-top_electrode_width/2, -1),\
                            (-top_electrode_width/2, 2),\
                            (-1.5, 2),\
                            (-1.5, 3.5),\
                            (1.5, 3.5)]
    if chip==0:
        layerBotElectrode=7
        layerTopElectrode=8
        layerConnections=9
        layerPatch=10
    elif chip==1:
        layerBotElectrode=11
        layerTopElectrode=12
        layerConnections=13
        layerPatch=14
    bot_electrode = gdspy.Polygon(points_bot_electrode, layer=layerBotElectrode)
    top_electrode = gdspy.Polygon(points_top_electrode, layer=layerTopElectrode)
    connection_path = gdspy.Rectangle((-3,patchLength/4),(3,3*patchLength/4))
    connection_path = gdspy.fast_boolean(connection_path, gdspy.Rectangle((-3,-(patchLength/4)),(3,-(3*patchLength/4))), 'or', layer=layerConnections)
    liftoff_patch = gdspy.Rectangle((-3, -patchLength/2), (3, patchLength/2), layer=layerPatch)
    bot_electrode.rotate(rotate)
    top_electrode.rotate(rotate)
    connection_path.rotate(rotate)
    liftoff_patch.rotate(rotate)
    bot_electrode.translate(dx, dy)
    top_electrode.translate(dx, dy)
    connection_path.translate(dx, dy)
    liftoff_patch.translate(dx, dy)
    return bot_electrode, top_electrode, connection_path, liftoff_patch

