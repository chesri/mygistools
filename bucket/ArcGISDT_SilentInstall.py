#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      chrism
#
# Created:     13/04/2016
# Copyright:   (c) chrism 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import os
import subprocess

def authorizeArcGIS(exe, level, licenseFilePath):
    prvc = ''
    if level == '1':
        prvc = os.path.join(licenseFilePath, 'DTADvanced.prvc')
    if level == '2':
        prvc = os.path.join(licenseFilePath, 'DTStandard.prvc')
    if level == '3':
        prvc = os.path.join(licenseFilePath, 'DTBasic.prvc')

    args = '-s -lif ' + prvc
    main(exe, args)


def is32bit():
    if os.environ['PROCESSOR_ARCHITECTURE'] == '32bit':
        return True
    else:
        return False

def main(exe, args):
    command = '\"' + exe + '\" ' + args
    print("Command is: " + command)
##    process = subprocess.Popen(command,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
##    out, err = process.communicate()
##    errcode = process.returncode

if __name__ == '__main__':

    swAuthExe = r'C:\Program Files\Common Files\ArcGIS\bin\softwareauthorization.exe'
    if is32bit:
        swAuthExe = r'C:\Program Files (x86)\Common Files\ArcGIS\bin\softwareauthorization.exe'

    if os.path.isfile(r'\\chrismvm\ArcGISDT1031_NetworkServer\setup.exe'):
        dtinstaller = r'\\chrismvm\ArcGISDT1031_NetworkServer\setup.exe'

    licenseFilePath = os.path.dirname(dtinstaller)

    print "Select License Level:"
    print "\t 1) Advanced"
    print "\t 2) Standard"
    print "\t 3) Basic\n"
    licenseLevel = raw_input('Enter number for choice: ')

    args = 'ESRI_LICENSE_HOST=localhost SOFTWARE_CLASS=Professional SEAT_PREFERENCE=Fixed DESKTOP_CONFIG=TRUE BLOCKADDINS=#0 ENABLEEUEI=0 MODIFYFLEXDACL=FALSE ADDLOCAL=ArcMap,ArcCatalog,Python,Ext_3D_Analyst,SpatialAnalyst,NetworkAnalyst'
    main(dtinstaller,args)

    if os.path.isfile(swAuthExe):
        authorizeArcGIS(swAuthExe,licenseLevel,licenseFilePath)


