#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      chrism
#
# Created:     23/01/2020
# Copyright:   (c) chrism 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import re

def DMS2DD(x,y):
    coords = []
    for dd in x,y:
##        print("Length of dd: {}".format(len(dd)))
        debug_string = "dd: {}".format(dd)
##        print(debug_string)

        if len(dd) > 0:
##            pstring =  ''.join(dd) + ": " + re.sub('\D', ' ', dd)
            string = str(re.sub('\D', ' ', dd.translate(None,' '))).strip()
            if len(string.split(' ')) == 3:
                dd = (float(string.split(' ')[0])/1) + (float(string.split(' ')[1])/60) + (float(string.split(' ')[2])/3600)
            if len(string.split(' ')) == 2:
                dd = (float(string.split(' ')[0])/1) + (float(string.split(' ')[1])/60)
            if len(string.split(' ')) == 1:
                dd = (float(string.split(' ')[0])/1)
        coords.append(dd)
    return coords

def DD2DMS(x,y):
    coords = []
    for dd in x,y:
        is_positive = dd >= 0
        dd = abs(dd)
        min,sec = divmod(dd*3600,60)
        deg,min = divmod(min,60)
        dir = 'E' if is_positive else 'W'
        if len(coords) == 1:
            dir = 'N' if is_positive else 'S'

        coords.append('{}-{}-{}{}'.format(int(deg),int(min),round(sec,1), dir))

    return coords

print("processing -78.9375275142")

##ixy = input('enter x,y: ' )
##print(ixy.split(','))
##ix = float(ixy.split(",")[0])
##iy = float(ixy.split(',')[1])
##print(DD2DMS(ix,iy))

inDD = [-78.9375275142,36.45678]
inDMS = ['-79-34-23','36-24-35']
print("inDD: {}, DMS: {}".format(inDD,DD2DMS(inDD[0],inDD[1])))
print("inDMS: {}, DD: {}".format(inDMS, DMS2DD(inDMS[0],inDMS[1])))