import arcpy, os, sys

source = arcpy.GetParameterAsText(0)

message = []

message.append("Looking for file: {}".format(source))

if arcpy.Exists(source):
    message.append("File {} found. Loading...".format(source))
    worked = True
else:
    message.append("File not found or corrupt. Nothing loaded.")
    worked = False

string = "\nUpload process complete. FAILED"
if worked:
    string = "\nUpload process complete. SUCCESS!"

message.append(string)

arcpy.SetParameterAsText(1,"This is a message.")



