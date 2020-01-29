#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      chrism
#
# Created:     08/02/2019
# Copyright:   (c) chrism 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import arcpy

ypg = r"PROJCS['NAD27_YUMA_PROVING_GROUND',GEOGCS['GCS_North_American_1927',DATUM['D_North_American_1927',SPHEROID['Clarke_1866',6378206.4,294.9786982]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Transverse_Mercator'],PARAMETER['False_Easting',84738.012],PARAMETER['False_Northing',-175814.044],PARAMETER['Central_Meridian',-113.75],PARAMETER['Scale_Factor',0.999933333],PARAMETER['Latitude_Of_Origin',31.0],UNIT['Meter',1.0]];-6100292.49622249 -14607719.0234388 409368153.975199;-100000 10000;-100000 10000;0.001;0.001;0.001;IsHighPrecision"

ypg = r"GEOGCS['WGS_1984_(G1150)',DATUM['World_Geodetic_System_1984_(G1150)',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119521E-09;0.001;0.001;IsHighPrecision"

sr = arcpy.SpatialReference()
sr.loadFromString(ypg)
labels = ['GCS','abbreviation','alias','angularUnitCode','angularUnitName','azimuth','centralMeridian','centralMeridianInDegrees','centralParallel','classification','datumCode','datumName','domain','factoryCode','falseEasting','falseNorthing','falseOriginAndUnits','flattening','GCSCode','GCSName','hasMPrecision','hasXYPrecision','hasZPrecision','isHighPrecision','latitudeOf1st','latitudeOf2nd','linearUnitCode','linearUnitName','longitude','longitude','longitudeOf1st','longitudeOf2nd','longitudeOfOrigin','MDomain','metersPerUnit','MFalseOriginAndUnits','MResolution','MTolerance','name','PCSCode','PCSName','primeMeridianCode','primeMeridianName','projectionCode','projectionName','radiansPerUnit','remarks','scaleFactor','semiMajorAxis','semiMinorAxis','spheroidCode','spheroidName','standardParallel1','standardParallel2','type','usage','VCS','XYResolution','XYTolerance','ZDomain','ZFalseOriginAndUnits','ZResolution','ZTolerance']

all = [sr.GCS,sr.abbreviation,sr.alias,sr.angularUnitCode,sr.angularUnitName,sr.azimuth,sr.centralMeridian,sr.centralMeridianInDegrees,sr.centralParallel,sr.classification,sr.datumCode,sr.datumName,sr.domain,sr.factoryCode,sr.falseEasting,sr.falseNorthing,sr.falseOriginAndUnits,sr.flattening,sr.GCSCode,sr.GCSName,sr.hasMPrecision,sr.hasXYPrecision,sr.hasZPrecision,sr.isHighPrecision,sr.latitudeOf1st,sr.latitudeOf2nd,sr.linearUnitCode,sr.linearUnitName,sr.longitude,sr.longitude,sr.longitudeOf1st,sr.longitudeOf2nd,sr.longitudeOfOrigin,sr.MDomain,sr.metersPerUnit,sr.MFalseOriginAndUnits,sr.MResolution,sr.MTolerance,sr.name,sr.PCSCode,sr.PCSName,sr.primeMeridianCode,sr.primeMeridianName,sr.projectionCode,sr.projectionName,sr.radiansPerUnit,sr.remarks,sr.scaleFactor,sr.semiMajorAxis,sr.semiMinorAxis,sr.spheroidCode,sr.spheroidName,sr.standardParallel1,sr.standardParallel2,sr.type,sr.usage,sr.VCS,sr.XYResolution,sr.XYTolerance,sr.ZDomain,sr.ZFalseOriginAndUnits,sr.ZResolution,sr.ZTolerance]

for i in range(0,len(all)):
    print("{:>28}".format(labels[i]) + ": " + str(all[i]))

