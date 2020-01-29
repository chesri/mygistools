#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      chrism
#
# Created:     05/03/2019
# Copyright:   (c) chrism 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import os, sys, re
import tempfile
def writeline(string):
    txt.write(string.encode("utf-8"))

##tmp = tempfile.NamedTemporaryFile(prefix='FolderGISInventory',delete=False)
##output = tmp.name + ".txt"
desktop = r'C:\Users\chrism\Desktop'
output = tempfile.NamedTemporaryFile(suffix='.txt', dir=desktop, prefix='FolderGISInventory_',delete=False)
txt = open(output.name, "w")

d_dir = r'C:\Temp'
ext_dict = {'.shp':'shapefile',
            '.mdb':'pGDB',
            '.lyr':'layer file',
            '.sde':'eGDB',
            '.img':'raster (img)',
            '.jpg':'raster (jpg)',
            '.mxd':'map document',
            '.ja1':'RPF',
            '.csv':'CSV',
            '.kmz':'KML',
            '.kml':'KML',
            '.osm':'open streetmap',
            '.shp':'shapefile',
            '.dwg':'autocad DWG',
            '.dxf':'DXF',
            '.dgn':'Bently DGN',
            '.tif':'raster (tif)',
            '.tiff':'raster (tif)',
            '.e00':'arcinfo_export',
            '.qgs':'QGIS',
            '.gdb':'fGDB',
            'rpf':'RPF',
            '.prj':'projection',
            'mgcp':'metadata'}

##dirext_dict = {'.gdb':'fGDB', 'rpf':'RPF dir'}

type_counts = {}
types = [gtype for gtype in ext_dict.keys()]
for t in types:
    type_counts[t] = 0

for root, dirs, files in os.walk(d_dir):
    if len(dirs) > 0:
        for d in dirs:
            d_ext = os.path.splitext(d)[1].lower()
            if d_ext in ext_dict.keys():
                string = ext_dict[d_ext] + "," + os.path.join(root, d) + "," + d
                print(string)
                writeline(string)
                type_counts[d_ext] = type_counts[d_ext] + 1
            elif d in ext_dict.keys():
                string = ext_dict[d] + "," + os.path.join(root, d) + "," + d
                print string
                type_counts[d] = type_counts[d] + 1

    for f in files:
        f_ext = os.path.splitext(f)[1].lower()
        if f_ext in ext_dict.keys():
            string = ext_dict[f_ext] + "," + os.path.join(root,f) + "," + f
            print(string)
            writeline(string)
            type_counts[f_ext] = type_counts[f_ext] + 1

print(type_counts)