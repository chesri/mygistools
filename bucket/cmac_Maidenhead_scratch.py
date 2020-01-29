#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      chrism
#
# Created:     06/09/2018
# Copyright:   (c) chrism 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import os

import re

def dms2dd(degrees, minutes, seconds, direction='N'):
    dd = float(degrees) + float(minutes)/60 + float(seconds)/(60*60);
    if direction == 'W' or direction == 'S':
        dd *= -1
    return dd;

def dd2dms(deg):
    d = int(deg)
    md = abs(deg - d) * 60
    m = int(md)
    sd = (md - m) * 60
    return [d, m, sd]

def parse_dms(dms):
    parts = re.split('[^\d\w]+', dms)
    lat = dms2dd(parts[0], parts[1], parts[2], parts[3])

    return (lat)

def checkCoords(x_coord,y_coord):
    #
    # Seek out X Coordinate
    #
    findex=0
    for i in range(-180,180,20):
        if x_coord >= i and x_coord < (i + 20):
            field1 = 'ABCDEFGHIJKLMNOPQR'[findex]

            sindex = 0
            for s in range(i,i + 20,2):
                #print('\t' + str(s))
                if x_coord >= s and x_coord < (s + 20):
                    square1 = '0123456789'[sindex]
                sindex += 1

                print("s: {}".format(s))
                # 2.5' of latitude by 5' of longitude - 24 divisions

                gap = 2.0/24
                bindex = 0
                bx = s
                bx_end = s + 2
                while bx < (s + 2):
                    if x_coord >= bx and x_coord < (bx + gap):
                        subsq = 'abcdefghijklmnopqrstuvwxyz'[bindex]
                    bx += gap
                    bindex += 1

        findex += 1

    #
    # Seek out Y Coordinate
    #
    findex=0
    for i in range(-90,90,10):
        if y_coord >= i and y_coord < (i + 10):
            field2 = 'ABCDEFGHIJKLMNOPQR'[findex]
            sindex = 0
            for s in range(i,i + 10,1):
                if y_coord > s:
                    square2 = '0123456789'[sindex]
                sindex += 1

        findex += 1

    grid = field1 + field2 + square1 + square2 + subsq
    return grid


x_coord = -81
y_coord = 35

grid = checkCoords(x_coord,y_coord)
print('{} ({},{})'.format(grid,x_coord,y_coord))