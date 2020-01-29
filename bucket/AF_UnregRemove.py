#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:     Scan a "DIR /S/B file" and print lines that contain Unsupported Software
#
# Author:      chrism
#
# Created:     25/09/2018
# Copyright:   (c) chrism 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import os, sys
import codecs

# Step 1:

ureg = []
ren = []

badFiles = ['mfcm80.dll','mfcm90.dll','msvcm80.dll','msvcm90.dll','msvcp80.dll','msvcp90.dll','msvcr100.dll','msvcr80.dll','msvcr90.dll']
read_file = open(r'G:\Results\05_wMCS.txt', 'r')
write_file = r'G:\Results\06_wMCS_OFlist.txt'

with open(write_file, "w") as f:
    for line in read_file:
        tmpline = line.strip('\n')
        if os.path.basename(tmpline) in badFiles:
            string1 = 'regsvr32 /u "' + tmpline +'"'
            ureg.append(string1)
            string2 = 'rename "' + tmpline + '" ' + 'xx_' + os.path.basename(tmpline)
            ren.append(string2)

    for u in ureg:
        print u
        f.write(u.encode("utf-8") + "\n")

    for r in ren:
        print r
        f.write(r.encode("utf-8") + "\n")

read_file.close()
f.close()

