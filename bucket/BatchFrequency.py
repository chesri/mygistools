#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      chrism
#
# Created:     06/07/2015
# Copyright:   (c) chrism 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import os
import arcpy
import sys
from time import ctime


# Tool will read through feature classes in Workspace and generate a Frequency report for each FC with a defined set of fields.

def FieldExist(featureclass, fieldname):
    fieldList = arcpy.ListFields(featureclass, fieldname)

    fieldCount = len(fieldList)

    if (fieldCount == 1):
        return True
    else:
        return False

# set variables.
freq_field_list = []
data = []
scratch_ws = r"C:\Users\chrism\Documents\ArcGIS\Default.gdb"
arcpy.env.overwriteOutput = True
tablename = os.path.join(scratch_ws, "tmp_frequency1")
timestr = time.strftime("%Y%m%d-%H%M%S")
header = "Dataset, Field=Value, Frequency\n"
fcount = 0


# when running from ArcGIS, set variables.
source_workspace = arcpy.GetParameterAsText(0)
if source_workspace == '#' or not source_workspace:
    source_workspace = r"C:\Users\chrism\Documents\ArcGIS\Default.gdb"

fields = arcpy.GetParameter(1)
if (fields):
    for it in arcpy.GetParameter(1).split(","):
         freq_field_list.append(it.strip(" "))
outfile = arcpy.GetParameter(2)

if (not freq_field_list):
##    freq_field_list = ["featureAreaUOM", "siteName"]
    freq_field_list = ["siteName","installationName","installationID","regionalTrainingSupportCenter","trainingSupportCenter","operationalStatus","featurePerimterUOM","predominantDesignUse","predominantDesignUseQtyUOM","featureAreaUOM","featureAreaAcresUOM","featureAreaSqKilometersUOM","featureLengthUOM","featureSurfaceType","featureHeightUOM","ceilingHeightUOM","netExplosiveWeightUOM","referenceGridType","firingSiteType"]

if (not outfile):
    outfile = os.path.join(r"D:\Temp\BatchFrequency", timestr + ".txt")

# describe the workspace and make sure it is 10.x or better
desc = arcpy.Describe(source_workspace)
if not desc.release == "3,0,0":
    arcpy.AddMessage("\n*********************************************\nSorry, this tool only works with 10.x geodatabases")
    if desc.release == "2,2,0":
        gdb_version ="9.2"
    elif desc.release == "2,3,0":
        gdb_version = "9.3"
    arcpy.AddMessage(source_workspace + " is reporting to be: " + gdb_version + "\n")
    exit()
else:
    arcpy.env.workspace = source_workspace
    output = open(outfile, 'w')
    output.write(header)

    fc_list = arcpy.ListFeatureClasses()
    for ds in arcpy.ListDatasets("","Feature"):
        for fc in arcpy.ListFeatureClasses("*","",ds):
            fc_list.append(fc)

    # cycle through feature classes (fc_list), test for the field and if present, run Frequency command
    try:
        for fc in fc_list:
            arcpy.AddMessage("Processing Feature Class: " + fc)
            print("Processing Feature Class: " + fc)
            for fld in freq_field_list:
                arcpy.AddMessage("\tRunning FREQUENCY Report for: " + fld)
                print("\tRunning FREQUENCY Report for: " + fld)
                if (not FieldExist(fc,fld)):
                    arcpy.AddMessage("\tField " + fld + " does not exist in " + fc)
                    myrow = fc, fld, "Does not exist"
                    data.append(myrow)
                else:
                    arcpy.Frequency_analysis(fc, tablename, fld)
                    fcount = fcount + 1
                    cursor = arcpy.da.SearchCursor(tablename,[fld,'FREQUENCY'])
                    for row in cursor:
                        value = fld + "=\"" + str(row[0]) +"\""
                        count = row[1]
                        myrow = fc, value, count
                        data.append(myrow)

        # write the information out to the log file.
        for i in data:
            string = i[0] + "," + i[1] + "," + str(i[2])
            print string,
            output.write(string + "\n")

        # print some status information, close the log file, and clean up.
        msg = ["\nOutput copied to " + output.name +"\n", "Processed " + str(fcount) + " frequency reports."]
        for i in range(2):
            arcpy.AddMessage(msg[i])
            print(msg[i])

        output.close()

        arcpy.Delete_management(tablename)
    except IOError as e:
        print "I/O error({0}): {1}".format(e.errno, e.strerror)
        arcpy.AddMessage("I/O error({0}): {1}".format(e.errno, e.strerror))
        arcpy.AddMessage(arcpy.GetMessage(2))
    except ValueError:
        print "Value Error"
        arcpy.AddMessage(arcpy.GetMessage(2))
    except TypeError as e:
        print "Type Error. Possibly number not handled as string"
        ##print "Type error({0}): {1}".format(e.errno, e.strerror)
    except:
        print "Unexpected error:", sys.exc_info()[0]
        arcpy.AddMessage(arcpy.GetMessage(2))
        raise
    finally:
        arcpy.AddMessage(arcpy.GetMessage(2))
