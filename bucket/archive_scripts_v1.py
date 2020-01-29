#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
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
import os

thedate = time.strftime("z_%Y-%m-%d")
tool_path = r'C:\OneDrive - Esri\My Toolboxes'
archive_path = r'E:\MyToolboxes_BACKUP'

destination = os.path.join(archive_path, thedate)
if not os.path.exists(destination):
    os.mkdir(destination)

files = []
##files += [each for each in os.listdir(tool_path) if each.endswith('.py')]
files += [each for each in os.listdir(tool_path)]

for i in files:
    curloc = os.path.join(tool_path,i)
    newloc = os.path.join(destination,i)
    if os.path.isfile(curloc):
        print('File: {} to destination: {}'.format(curloc,newloc))
        shutil.copy2(curloc, newloc)