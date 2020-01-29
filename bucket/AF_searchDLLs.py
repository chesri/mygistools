#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      chrism
#
# Created:     26/09/2018
# Copyright:   (c) chrism 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import os, sys, re

rx = ['atl80.dll ','atl90.dll','atl100.dll ','mfcm80.dll','mfcm90.dll','msvcm80.dll','msvcm90.dll','msvcp80.dll','msvcp90.dll','msvcr100.dll','msvcr80.dll','msvcr90.dll']
#rx = re.compile(r'[A-Za-z]90\.dll')
r = []
##for path, dnames, fnames in os.walk('C:\\Program Files (x86)\\ArcGIS'):
##    r.extend([os.path.join(path, x) for x in fnames if rx.search(x)])
##print r
for path, dnames, fnames in os.walk('C:\\'):
    if fnames in rx:
        r.append(os.path.join(path,fnames))
##    r.extend([os.path.join(path, x) for x in fnames if rx.search(x)])
##    r.append([x for x in fnames if rx.search(x)])
##    r.extend(x for x in fnames if fnames in rx)
##    r.extend([x for x in fnames if rx.match(x)])

for i in r:
    print i


