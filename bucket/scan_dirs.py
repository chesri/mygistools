#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      chrism
#
# Created:     25/10/2019
# Copyright:   (c) chrism 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import os

folder = r'C:\OneDrive - Esri\CM_DATA\Todd_new'

gdbcount = 0
mdbcount = 0
lyrcount = 0
shpcount = 0
sdecount = 0
imgcount = 0
jpgcount = 0
mxdcount = 0
counter = {'.shp':0, '.mdb':0, '.gdb':0,'.sde':0,'.img':0,'.mxd':0,'.lyr':0,'.jpg':0}

objects = [['.shp','file','Shapefile','SHAPEFILE'],
           ['.mdb','file','Personal Geodatabase','pGDB'],
           ['.gdb','dir','File Geodatabase','fGDB'],
           ['.sde','file','Enterprise Geodatabase (connection file)','eGDB'],
           ['.img','file','Rasters','Erdas'],
           ['.jpg','file','Rasters','JPG'],
           ['.mxd','file','Map Documents (MXD)','MXD'],
           ['.lyr','file','Layer File (lyr)','LYR File']
           ]

exts = [ext[0] for ext in objects]

for root, dirs, files in os.walk(folder):
    if len(dirs) > 0:
        for d in dirs:
            if d[-4:] in exts:
                i = exts.index(d[-4:])
                label = objects[i][3]
                string = "{:>10}: {},{}".format(label,os.path.join(root, d),d)
                print(string)
                counter[d[-4:]] += 1

    for f in files:
        if f[-4:] in exts:
            i = exts.index(f[-4:])
            label = objects[i][3]
            string = "{:>10}: {},{}".format(label,os.path.join(root, f),f)
            print string
            counter[f[-4:]] += 1

print "-"*80
print("{:>10}: {}".format("File Type","Count"))
print("{:>10}: {}".format("-"*10,"-"*69))

for l in objects:
    print("{:>10}: {}".format(l[3],counter[l[0]]))



