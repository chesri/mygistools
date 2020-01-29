#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      chrism
#
# Created:     02/07/2019
# Copyright:   (c) chrism 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import os, sys, json

smartEditor = r"C:\Temp\JS_API_Learning\survey_request\configs\SmartEditor\config_widgets_SmartEditor_Widget_21.json"
with open(smartEditor, 'r') as read_file:
    se = json.load(read_file)

editor = se['editor']
layerinfo = editor['layerInfos']

##for x,l in enumerate(layerinfo[0]):
##    print x, l

for layer in layerinfo:
    print "Layer ID: {}".format(layer['featureLayer']['id']),  " (Edit flag={})".format(layer['_editFlag'])