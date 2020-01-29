#-------------------------------------------------------------------------------
#        module2
# Purpose:
#
# Author:      chrism
#
# Created:     20/12/2019
# Copyright:   (c) chrism 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

parameters = []
parameters.append(['GDB Connection File', 'workspace','DEWorkspace','Required','Input'])
parameters.append(['Choose Project__Test_Officer__Program__Location__Date_', 'chooseproject','GPString','Required','Input'])
parameters.append(['Program Name', 'program_name','GPString','Optional','Input'])
parameters.append(['Test Officer', 'test_officer','GPString','Optional','Input'])
parameters.append(['Location', 'location','GPString','Optional','Input'])
parameters.append(['Choose Technician', 'technician','GPString','Required','Input'])
parameters.append(['p0 hidden_', 'p0__hidden_','GPString','Optional','Input'])
parameters.append(['All Day Event', 'allday','GPBoolean','Optional','Input'])
parameters.append(['Start Date', 'start_date','GPDate','Optional','Input'])
parameters.append(['End Date', 'enddate', 'GPDate','Optional','Input'])
parameters.append(['Reoccuring', 'reoccuring', 'GPString','Optional','Input'])
parameters.append(['Every', 'interval', 'GPLong','Optional','Input'])
print parameters

params = []
for x,p in enumerate(parameters):
    ##print x, p
    print "\nparam{} = arcpy.Parameter(".format(x)
    print "\tdisplayName='{}',".format(p[0])
    print "\tname='{}',".format(p[1])
    print "\tdatatype='{}',".format(p[2])
    print "\tparameterType='{}',".format(p[3])
    print "\tdirection='{}')".format(p[4])
    params.append("param" + str(x))

print params
