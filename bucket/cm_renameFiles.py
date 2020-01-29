#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      chrism
#
# Created:     09/08/2017
# Copyright:   (c) chrism 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import os

d_dir = r'G:\clt-cmcguire7l_backup\C_Drive\chrism\Local_AppData\Desktop10.4\ArcCatalog\SearchIndex'


for root, dirs, files in os.walk(d_dir):
    c = 0
    for f in files:
        old = os.path.join(d_dir,f)
        new = os.path.join(d_dir, str(c) + os.path.splitext(f)[1])
        #print new
        print "rename %s %s" % (old,new)
        os.rename(old,new)
        c = c + 1