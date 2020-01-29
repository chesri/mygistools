#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      chrism
#
# Created:     25/09/2018
# Copyright:   (c) chrism 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import os, sys
import codecs

##def writeline(string):
##    print(string)
##    txt.write(string.encode("utf-8") + "\n")
##
##
##if len(sys.argv) > 1:
##    output = sys.argv[1]
##else:
##    outfile = 'cm_findFileInFS.txt'
##    output = os.path.join(os.path.dirname(__file__),outfile)
##
##
##with open(output, "w") as txt:

fcount = 0
root_folder = os.path.join('C:\\')
badFiles = ['mfcm80.dll','mfcm90.dll','msvcm80.dll','msvcm90.dll','msvcp80.dll','msvcp90.dll','msvcr100.dll','msvcr80.dll','msvcr90.dll']
found = []

for root, dirs, files in os.walk(root_folder):
    for f in files:
        if f in badFiles:
            found.append(os.path.join(root,f))
            fcount += 1

for f in found:
    print f

print('Found files count: ' + str(fcount))

