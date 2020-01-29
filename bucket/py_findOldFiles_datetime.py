#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      chrism
#
# Created:     15/08/2019
# Copyright:   (c) chrism 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import os, sys, shutil, time
#import datetime
from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

def listFiles(rootdir, filelist):
    for f in filelist:
        fullfilename = os.path.join(rootdir,f)
        c_date = datetime.fromtimestamp(os.path.getctime(fullfilename)) ## os.path.getctime(fullfilename)
        if c_date < too_old:
         print("too old: ", f[:3], f[-3:], c_date)


s = r'C:\arcgisserver\directories\arcgissystem\arcgisinput\yuma19\printsurveyprojectmap.GPServer\extracted\v101\range_survey_gis'
l = r'C:\arcgisserver\directories\arcgissystem\arcgisinput\yuma19\printsurveyprojectmap.GPServer\extracted\v101\logs'

too_old = datetime.now() - timedelta(hours=1)

for root, dirs, filenames in os.walk(s):
    listFiles(root,filenames)

for root, dirs, filenames in os.walk(l):
    listFiles(root,filenames)
