#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      chrism
#
# Created:     05/02/2019
# Copyright:   (c) chrism 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import collections

def mkList(input_list):
    if input_list == 'station':
        the_list = ('st_id:Station ID',
        'st_x:X',
        'st_y:Y',
        'st_z:Z',
        'st_hi:HI (incl.),HI (incl),HI'
        )

    if input_list == 'backsight':
        the_list = ('bs_id:Backsight ID,Backsight',
        'bs_computed_az:Computed Az',
        'bs_observed_az:Observed Az'
        )

    if input_list == 'equipment':
        the_list = ('pt_id:Point ID',
        'pt_ha:HA',
        'pt_hd:HD',
        'pt_vd:VD',
        'pt_ht:HT,HT (incl.),HT (incl)',
        'pt_ypg_x:X',
        'pt_ypg_y:Y',
        'pt_ypg_z:Z',
        'pt_wgs84_x:pt_wgs84_x',
        'pt_wgs84_y:pt_wgs84_y',
        'pt_wgs84_z:pt_wgs84_z',
        )

    if input_list == 'project':
        the_list = ('project:Project',
        'classification:Classification',
        'program:Program,Program Name',
        'site:Site',
        'date:Date',
        'poc:POC,Test Officer',
        'instrument_type:Intrument Type,Inst Type,Instrument Type',
        'instrument_sn:Instrument S/N',
        'surveyor:Surveyor',
        'reference:REF,Reference',
        'grid:Grid',
        'source_file:source_file',
        'source_status:source_status',
        'projectIDFK:projectIDFK',
        'comments:Comments'
        )

    return the_list


class Lookup():
    ''' takes a list of 'key:values' pairs and provides lookup capabilities
    '''

    count = 0

    def __init__(self,a_list):
        self.a_dict = collections.OrderedDict()
        for i in a_list:
            self.a_dict[i.split(":")[0]] = i.split(":")[1].split(",")
            Lookup.count += 1

    def as_keylist(self):
        output = []
        for k in self.a_dict.iterkeys():
            output.append(k)
        return output

    def as_valuelist(self):
        output = []
        for v in self.a_dict.itervalues():
            if len(v) > 1:
                for sm in v:
                    output.append(''.join(sm))
            else:
                output.append(''.join(v))
        return output

    def return_key(self,search_value):
        output = []
        for k,v in self.a_dict.items():
            if search_value in v:
                output.append(k)
        return output

    def return_value(self,search_key):
        output = []
        for k,v in self.a_dict.items():
            if search_key in k:
                output.append(''.join(v))
        return output

class YTCProject():

    def __init__(self):
        self.name = ''
        self.classification  = ''
        self.program = ''
        self.site = ''
        self.date = ''
        self.poc = ''
        self.instrument_type = ''
        self.instrument_sn = ''
        self.surveyor = ''
        self.reference = ''
        self.grid = ''
        self.uom = ''
        self.source_file = ''
        self.source_status = ''
        self.projectIDFK = ''
        self.comments = ''


prj_list = Lookup(mkList('equipment'))
project = YTCProject()

print (prj_list.as_keylist())
