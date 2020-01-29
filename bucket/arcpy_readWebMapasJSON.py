#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      chrism
#
# Created:     20/05/2019
# Copyright:   (c) chrism 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import os, json, re

jFile = r'C:\OneDrive - Esri\DS_Workspace\TSMO_DIJ\tsmoapp_configuration\DIJ_EW_MAP-Cmac Copy_Data.json'

def readDICT(obj):
    listkeys = []
    for d in obj.keys():
        listkeys.append(d)

    return listkeys

def fetchDrawInfo(drawinfo):

    for di in drawinfo.keys():

        if type(drawinfo[di]) == list:
            for listItem in drawinfo[di]:
                #print("{}: {}".format(drawinfo[di],listItem))
                if type(listItem) == dict:
                    for x,a in enumerate(listItem.keys()):
                        if a != 'symbol':
                            print("{}: {}".format(a,listItem[a]))
                        else:
                            print "Symbol:"
                            for symkey in listItem[a].keys():
                                print("\t{}: {}".format(symkey,listItem[a][symkey]))

        if type(drawinfo[di]) == dict:
            di_dict = drawinfo[di]
            for drawItem in di_dict.keys():
                print("{} keys: {}".format(drawItem,di_dict[drawItem]))


def fetchOperationalLayers(m):
    layers = []

    # prop_list is list of properties that we want to capture/report (verses all of them)
    prop_list = ['title','id','layerType','opacity','timeAnimation','url','visibility','disablePopup','showLabels','mode','refreshInterval','itemId','layerDefinition','popupInfo']

    for lid,lyr_properties in enumerate(m['operationalLayers']):
        print "---------"

        # check to validate key exists in property list before proceeding to report on it.
        keyExists = []
##        for check in lyr_properties.keys():
##            if check in prop_list:
##                keyExists.append(check)

        for check in prop_list:
            if check in lyr_properties.keys():
                keyExists.append(check)

        if keyExists:
            for prop in keyExists:

                # if not another list or dictionary, simply print key and value to screen.
                if type(lyr_properties[prop]) != dict and type(lyr_properties[prop]) != list:
                    print("{}: {}".format(prop,lyr_properties[prop]))

                # if key is a dictionary, then we have to dissect it and report parts.
                elif type(lyr_properties[prop]) == dict:
                    #print("Keys: {}".format(lyr_properties[prop].keys()))

                    for a in lyr_properties[prop].keys():

                        if a != 'description' and a != 'drawingInfo':
                            print("{}: {}".format(a,lyr_properties[prop][a]))
                        elif a == 'drawingInfo':
                            fetchDrawInfo(lyr_properties[prop][a])
                        else:
                            print ""
                            print("{}, type {}".format(a,type(lyr_properties[prop][a])))

    return

# ##############################################################################
# START

try:
    mapjson = json.load(open(jFile,"r"))

except ValueError as v:
    print("ValueError: {}".format(v))
    exit()
except Exception as e:
    print(e)
    exit()

print(fetchOperationalLayers(mapjson))

exit()

##print(readDICT(mapjson))
##for x,j in enumerate(readDICT(mapjson)):
##    if type(mapjson[j]) == dict:
##        print(j + " (dict)")
##        print(readDICT(mapjson[j]))
##        print("--")
##    if type(mapjson[j]) == list:
##        ##print(j + " (list)")
##        for li in mapjson[j]:
##            if type(li) == dict:
##                for liv in li.keys():
##                    if type(li[liv]) == dict:
##                        print(readDICT(li[liv]))
##                    else:
##                        print("{}: {}".format(liv,li[liv]))
##
##            print("--")


##for key in mapjson['operationalLayers']:
##
##    if 'featureCollection' in key.keys():
##        print(key['featureCollection'])
##        fc = key['featureCollection']
##        layers = fc['layers']
##
##        for layer in layers:
##
##            ld = layer['layerDefinition']
##
##            print("Layer Def Name: {}".format(ld['name']))
##
##            features = layer['featureSet']['features']
##            print('featureSet/features count: {}'.format(len(features)) )
##
##            if ld['name'] <> 'polygonLayer':
##                for feature in features:
##                    if 'attributes' in feature.keys():
##
##                        print("attributes/name: \"{}\"".format(feature['attributes']['name']))
##
##                        if 'project_uid' in feature['attributes']:
##
##                            project_uid = feature['attributes']['project_uid']
##
##                            print("project_UID: {}".format(project_uid))
##
##                    elif 'symbol' in feature.keys():
##                        print('symbol/text: {}'.format(feature['symbol']['text']))
##





