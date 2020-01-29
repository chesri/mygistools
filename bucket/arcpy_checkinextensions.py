#-------------------------------------------------------------------------------
# Name:        checkinextensions.py
# Purpose:
#
# Author:      chrism
#
# Created:     29/11/2016
# Copyright:   (c) chrism 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import arcpy

extensions = ['3D','Datareviewer','DataInteroperability','Airports','Aeronautical','Bathymetry','Nautical','GeoStats','Network','Spatial','Schematics','Tracking','JTX','ArcScan','Business','Defense','Foundation','Highways','StreetMap']

for ext in extensions:
    arcpy.AddMessage("checking in extension: " + ext)
    arcpy.CheckInExtension(ext)


## Reference: http://desktop.arcgis.com/en/arcmap/10.3/analyze/python/access-to-licensing-and-extensions.htm
## Keyword for the extension product that is being checked.
## 3D —ArcGIS 3D Analyst extension
## Datareviewer —ArcGIS Data Reviewer for Desktop
## DataInteroperability —ArcGIS Data Interoperability extension for Desktop
## Airports —ArcGIS for Aviation: Airports
## Aeronautical —ArcGIS for Aviation: Charting
## Bathymetry —ArcGIS for Maritime: Bathymetry
## Nautical —ArcGIS for Maritime: Charting
## GeoStats —ArcGIS Geostatistical Analyst extension
## Network —ArcGIS Network Analyst extension
## Spatial —ArcGIS Spatial Analyst extension
## Schematics —ArcGIS Schematics extension
## Tracking —ArcGIS Tracking Analyst extension
## JTX —ArcGIS Workflow Manager for Desktop
## ArcScan —ArcScan
## Business —Business Analyst
## Defense —Esri Defense Solution
## Foundation —Esri Production Mapping
## Highways —Esri Roads and Highways
## StreetMap —StreetMap