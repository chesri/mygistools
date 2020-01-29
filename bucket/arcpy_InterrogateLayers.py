import arcpy, os, sys

def sendMessage(message):
    print(message)
    arcpy.AddMessage(message)

def print_table(header,table):

    the_new_table = []
    the_new_table.append(header)
    for t in table:
        the_new_table.append(t)
##    for t in range(len(table)):
##        row = table[t].data
##        nTable = [unicode(f) for f in table[t].data]
##        the_new_table.append(nTable)

    ##longest_cols = [ (max([len(str(row[i])) for row in the_new_table]) + 3) for i in range(len(the_new_table[0])) ]
    longest_cols = [ (max([len(unicode(row[i])) for row in the_new_table]) + 3) for i in range(len(the_new_table[0])) ]
##    #row_format = "".join(["{:>" + unicode(longest_col) + "}" for longest_col in longest_cols])               ## right justify all columns (numbers)
##    #row_format = "".join(["{:" + unicode(longest_col) + "}" for longest_col in longest_cols])                ## no justify
    first_col_format = "".join("{:<" + unicode(longest_cols[-1:][0]) + "}")                                     ## left justify first column (text)
    rem_col_format = "".join(["{:^" + unicode(longest_col - 1) + "}" for longest_col in longest_cols[1:]])      ## center justify remainder of columns
    row_format = "".join(first_col_format + rem_col_format)
    rIndex = 0
    for row in the_new_table:
        if rIndex == 0:
            sendMessage('\n')
        if rIndex == 1:
            sendMessage('{}'.format("-"*80))
        sendMessage(row_format.format(*row))
        rIndex += 1

if __name__ == '__main__':
    if len(sys.argv) == 3:
        mxd_file = sys.argv[1]
    else:
        mxd_file = arcpy.GetParameterAsText(0)

    mxd = arcpy.mapping.MapDocument(mxd_file)
    df = arcpy.mapping.ListDataFrames(mxd)[0]
    sendMessage("Processing: %s" % (mxd.filePath))
    layers = arcpy.mapping.ListLayers(mxd)

    table = []
    for x,lyr in enumerate(layers):

        lyrType = "Unknown"
        if lyr.isFeatureLayer:
            lyrType = "Feature Layer"
        if lyr.isGroupLayer:
            lyrType = "Group Layer"
        if lyr.isNetworkAnalystLayer:
            lyrType = "NetworkAnalystLayer"
        if lyr.isServiceLayer:
            lyrType = "Service Layer"
        string = [lyr.name,lyrType,lyr.description,lyr.dataSource,lyr.definitionQuery]
        table.append(string)

    header= ['Layer Name', 'Type','Description','Data Source','Definition Query']
    ##print_table(header,table)
    sendMessage('\t'.join(header))
    for t in table:
        sendMessage('\t'.join(t))




