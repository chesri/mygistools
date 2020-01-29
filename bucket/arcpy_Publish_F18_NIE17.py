#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      chrism
#
# Created:     31/01/2018
# Copyright:   (c) chrism 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------


import arcpy, os

files = os.listdir(r'D:\Workspace\TSMO\Demo\NIE_2017')
for file in files:
    search = '_DMZ_'
    if file.find('_DMZ_') > 1 and file.find('xx') != 0:
        # strip out DMZ and mxd extension to derive the service name
        service = ''.join((file[:3] + file[7:]).split())[:-4]
        print service

        mapDoc = arcpy.mapping.MapDocument(file)
        # strip out DMZ and mxd extension to derive the service name
        service = ''.join((file[:3] + file[7:]).split())[:-4]
        print service
        sddraft = 'D:/Temp/sd_staging/{}.sddraft'.format(service)
        sd = 'D:/Temp/sd_staging/{}.sd'.format(service)
#       ## create service definition draft
        ##CreateMapSDDraft (map_document, out_sddraft, service_name, {server_type}, {connection_file_path}, {copy_data_to_server}, {folder_name}, {summary}, {tags})
        connection_file= r'C:\Users\chrism\AppData\Roaming\ESRI\Desktop10.4\ArcCatalog\clt-defense-demo as PortalAdmin (admin).ags'
        analysis = arcpy.mapping.CreateMapSDDraft(mapDoc, sddraft, service, 'FROM_CONNECTION_FILE', connection_file, 'FALSE', 'TSMO_Feb2018')

        con = r'GIS Servers\clt-defense-demo as PortalAdmin (admin)'
        if analysis['errors'] == {}:
            # create service definition
            ##arcpy.StageService_server(sddraft, sd)
            # publish to My Hosted Services
            ##arcpy.UploadServiceDefinition_server(sd, con)
            pass
        else:
            # if the sddraft analysis contained errors, display them
            print analysis['errors']