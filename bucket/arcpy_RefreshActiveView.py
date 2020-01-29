#-------------------------------------------------------------------------------
# Name:        Refresh TOC/Map
# Purpose:
#
# Author:      chrism
#
# Created:     12/01/2017
# Copyright:   (c) chrism 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import arcpy

mxd = arcpy.mapping.MapDocument("CURRENT")
arcpy.RefreshActiveView()

