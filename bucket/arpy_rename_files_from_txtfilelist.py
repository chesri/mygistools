#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      chrism
#
# Created:     20/09/2018
# Copyright:   (c) chrism 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import os, sys

##f = open(r'C:\Box Sync\DS_Workspace\AFNIC\2018 Scans\unsupported.txt','r')
##for line in f:
##    if os.path.isfile(line):
##        print("EXIST: " + line)
##    else:
##        print("NOT EXISTS: "+ line)

with open(r'C:\Box Sync\My Toolboxes\test.txt') as file:
    data = file.readlines()

rename = False

for line in data:
    line = line.rstrip('\n')
    folder = os.path.dirname(line)
    filen = os.path.basename(line)

    if os.path.isfile(line):
        if rename:
            print("renaming {} to {}".format(filen,'xx_' + filen))
            os.rename(line,os.path.join(folder,'xx_' + filen))
            string = 'REGSVR32 /U ' + line
        else:
            print("EXIST: " + filen + ' @ ' + folder)
            string = 'REGSVR32 /U ' + line
            print string
    elif os.path.isfile(os.path.join(folder,'xx_' + filen)) and not rename:
        print("renaming {} to {}".format('xx_' + filen,filen))
        os.rename(os.path.join(folder,'xx_' + filen),line)
    else:
        print("NOT EXISTS: "+ line)