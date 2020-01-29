#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# To Run: C:\Box Sync\My Toolboxes>\Python27\ArcGIS10.6\python.exe archive_scripts.py
#
# Author:      chrism
#
# Created:     14/06/2017
# Copyright:   (c) chrism 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

##import datetime
import time
import shutil
import os, sys

thedate = time.strftime("%Y-%m-%d")
tool_path = os.path.dirname(sys.argv[0])
archive_path = r'E:\MyToolboxes_BACKUP'

if os.path.isdir(r'E:\\'):
    destination = os.path.join(archive_path, thedate)
    if not os.path.exists(destination):
        os.mkdir(destination)

    files = []
    ##files += [each for each in os.listdir(tool_path) if each.endswith('.py')]
    files += [each for each in os.listdir(tool_path)]
    for i in files:
        if os.path.isfile(os.path.join(tool_path,i)):
            curloc = os.path.join(tool_path,i)
            newloc = os.path.join(destination,i)
            print('File: {} to destination: {}'.format(curloc,newloc))

            shutil.copy2(curloc, newloc)
else:
    print('{} not accessible. Check that drive "E:\" is turned on, connected, and mounted.'.format(archive_path))