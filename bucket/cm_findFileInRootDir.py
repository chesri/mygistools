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

output = os.path.join(os.environ['USERPROFILE'], 'Desktop','output.txt')
root_folder = r'C:\\'
badFiles = ['mfcm80.dll','mfcm90.dll','msvcm80.dll','msvcm90.dll','msvcp80.dll','msvcp90.dll','msvcr100.dll','msvcr80.dll','msvcr90.dll']


## with open(output, "w") as txt:
for root, dirs, files in os.walk(root_folder):
    ##print(root)
    for f in files:
        if f in badFiles:
            print(os.path.join(root,f))

