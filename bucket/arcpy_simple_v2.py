import arcpy, os, sys

source = arcpy.GetParameterAsText(0)


##arcpy.Exists(source)
##    message.append("File {} found. Loading...".format(source))
##    worked = True
##else:
##    message.append("File not found or corrupt. Nothing loaded.")
##    worked = False
##
##string = "\nUpload process complete. FAILED"
##if worked:
##    string = "\nUpload process complete. SUCCESS!"
##
##message.append(string)
##message_count = arcpy.GetMessageCount()
##string = 'Upload Geodetic File is complete.'
####arcpy.SetParameterAsText(1,arcpy.GetMessage(message_count - 1))
##arcpy.SetParameterAsText(1,string)
tmp = os.path.dirname(sys.argv[0])
arcpy.AddMessage(tmp)


