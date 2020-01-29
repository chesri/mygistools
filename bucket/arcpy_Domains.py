#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      chrism
#
# Created:     16/11/2017
# Copyright:   (c) chrism 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import arcpy
ws = r'D:\Workspace\MCIEAST_IR_Project\Data\IRDM_schema_v1.gdb'
domains = arcpy.da.ListDomains(ws)
for domain in domains:
    print('Domain name: {0}'.format(domain.name))
    if domain.domainType == 'CodedValue':
        coded_values = domain.codedValues
        for val, desc in coded_values.items():
            print('{0} : {1}'.format(val, desc))
    elif domain.domainType == 'Range':
        print('Min: {0}'.format(domain.range[0]))
        print('Max: {0}'.format(domain.range[1]))