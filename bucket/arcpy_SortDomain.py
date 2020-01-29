#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      chrism
#
# Created:     20/11/2017
# Copyright:   (c) chrism 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import arcpy
schema_workspace = arcpy.GetParameter(0)
domain_name = arcpy.GetParameter(1)
sort_by = arcpy.GetParameter(2)
if sort_by = '#' or not sort_by:
    sort_by = "CODE"
sort_order = arcpy.GetParameterAsText(3)
if sort_order = '#' or not sort_order:
    sort_order = "ASCENDING"

arcpy.SortCodedValueDomain_management(schema_workspace, domain_name, sort_by, sort_order)

