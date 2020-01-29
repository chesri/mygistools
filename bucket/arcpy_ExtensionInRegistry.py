#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:     changes values in registry indicating ArcGIS extensions are
#              turned off when product(s) start. This will prevent the client
#              application from checking out license automatically due to an
#              extension being left "on" from a user session.
#
# Author:      chrism
#
# Sources:     (a) Stole original code from: http://code.activestate.com/recipes/66011-reading-from-and-writing-to-the-windows-registry/
#              (b) Identified locations from http://support.esri.com/technical-article/000007821
#              (c) Product codes from:
#                 (c.1) http://support.esri.com/technical-article%5C000013200
#                 (c.2) http://communityhub.esriuk.com/technicalsupport/2014/3/23/silently-enable-extensions-for-arcgis-for-desktop-10x.html
#                 (c.3) http://edndoc.esri.com/ArcObjectsOnline/TechnicalDocuments/ESRIExtIds.htm
#              (d) Python use at https://docs.python.org/2/library/_winreg.html
# Created:     12/01/2016
# Copyright:   (c) chrism 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from _winreg import *

def ExtLookup(product_code):
    product_name = ''
    if product_code == '{4D8C99BC-5096-406C-B48A-0581399ADD77}': product_name = 'Datreviewer'
    if product_code == '{DE0502C4-8D34-11D3-A63A-0008C7BF3347}': product_name = 'Geostaticial Analyst'
    if product_code == '{B7F5E5C3-D500-49B4-91F5-CDAAC07DE9BF}': product_name = 'Data Interoperability'
    if product_code == '{D53BF20F-24FB-11D4-B34C-00104BA2ABCC}': product_name = 'Tracking Analyst'
    if product_code == '{A212F759-F155-4BAF-A692-B9268CF9A465}': product_name = 'ArcScan Tools'
    if product_code == '{20664808-0045-0991-BBFE-1CAC27A0328A}': product_name = 'Maplex'
    if product_code == '{C967BD39-1118-42EE-AAAB-B31642C89C3E}': product_name = 'Network Analyst'
    if product_code == '{8AEE0DE1-535C-4788-95C8-1659444D4C02}': product_name = 'Publisher Extension'
    if product_code == '{EE89C7C1-20BB-4412-8239-301179CA4F0D}': product_name = 'Schematic Extension'
    if product_code == '{B679B84A-13FC-11D6-9269-00508B48AE82}': product_name = 'SurveyAnalyst_ArcMapExtension'
    if product_code == '{3C5059FE-9F15-401A-94ED-EED914D73E3E}': product_name = 'Spatial Analyst'
    if product_code == '{94305472-592E-11D4-80EE-00C04FA0ADF8}': product_name = '3D Analyst'
    if product_code == '{0050490F-E5E4-463F-AC40-5121E4816743}': product_name = 'ArcMap: ESRI Route Events Application Extension'
    if product_code == '{37025245-BBCC-4582-B46F-02C5307296F7}': product_name = 'ArcMap: Overposter Validation'
    if product_code == '{9A8C77AD-4841-434B-9863-C948BE05B5C0}': product_name = 'ArcMap: ESRI Representation Application Extension'
    if product_code == '{AED6E9C7-C161-439D-B816-A9066A2A29FA}': product_name = 'ArcMap: ESRI Route Hatching Extension'
    if product_code == '{C88A0E93-855F-11D7-B877-00010265ADC5}': product_name = 'ArcMap: Tracking Environment'
    if product_code == '{E32524C6-8C5D-4D7E-9302-E61680088EF3}': product_name = 'ArcMap: TabletPC Support'
    if product_code == '{E8521349-795A-4E57-9900-907E7A09BA2D}': product_name = 'ArcMap: SMWindow'
    if product_code == '{F8842F20-BB23-11D0-802B-0000F8037368}': product_name = 'ArcMap: ESRI Object Editor'
    if product_code == '{5E94138C-C8B7-42BD-8BA6-0F9DC3ACCE07}': product_name = 'ArcMap: ESRI Raster Cleanup'
    if product_code == '{E4F593DA-3675-4778-95EE-FE8197BB43EA}': product_name = 'ArcMap: ESRI Animation'
    if product_code == '{1536D839-3CE3-4400-9403-2540D24E4E26}': product_name = 'ArcMap: ESRI ArcPad Tools'
    if product_code == '{F63C1653-16E2-45B0-B428-5CB0E5E20867}': product_name = 'ArcMap: ESRI Replication Extension'
    if product_code == '{C994BFE6-47F1-4BAC-8F35-0743C7576673}': product_name = 'ArcMap: GPS Extension'
    if product_code == '{C50D33D1-DBED-11D3-B9BD-00C0F0567A4A}': product_name = 'ArcMap: Georeferencing'
    if product_code == '{BC36CF3B-1FC1-461D-92DF-CA51CDC9C84C}': product_name = 'ArcMap: StreetDirectionsUI'
    if product_code == '{88284BC5-C5E8-4BAD-B402-941258A1C224}': product_name = 'ArcMap: ESRI Adjustment Tools'
    if product_code == '{C2B54945-2EFA-458E-92B3-C5492FA38D06}': product_name = 'ArcMap: ESRI Topology Extension'
    if product_code == '{98528F9B-B971-11D2-BABD-00C04FA33C20}': product_name = 'ArcMap: Utility Network Analyst'
    if product_code == '{36C99530-923C-11D3-9F6B-00C04F6BDF06}': product_name = 'ArcMap: Locator Database Extension'
    if product_code == '{DED68A1B-31D0-4CFA-B984-A33519DF464E}': product_name = 'ArcCatalog: ArcToolboxExtension'
    if product_code == '{055B2B99-F2C9-11D2-9FC1-00C04F8ED211}': product_name = 'ArcCatalog: ESRI Metadata Extension'
    if product_code == '{DED68A1B-31D0-4CFA-B984-A33519DF464E}': product_name = 'ArcCatalog: ArcToolboxExtension'
    if product_code == '{055B2B99-F2C9-11D2-9FC1-00C04F8ED211}': product_name = 'ArcCatalog: ESRI Metadata Extension'

    return product_name

aReg = ConnectRegistry(None,HKEY_CURRENT_USER)
for product in ('Desktop10.2\\ArcMap', 'Desktop10.2\\ArcCatalog', 'Desktop10.2\\ArcScene', 'Desktop10.2\\ArcGlobe','Desktop10.3\\ArcMap', 'Desktop10.3\\ArcCatalog', 'Desktop10.3\\ArcScene', 'Desktop10.3\\ArcGlobe'):
    print "Diabling " + product + " Extensions:"

    keypath = 'Software\\Esri\\' + product + r'\Extensions'
    try:
        aKey = OpenKey(aReg, keypath,0, KEY_ALL_ACCESS)

        for i in range(QueryInfoKey(aKey)[1]):
            try:
                n,v,t = EnumValue(aKey,i)
##                print i, n, v, t
                print "Disabling " + ExtLookup(n)
                SetValueEx(aKey,n,0,t,2)
                # SetValueEx arguments:
                #     aKey = either the ArcMap\Extensions or ArcCatalog\Extensions key from the "product" loop above
                #     n = name of the key value; the product codes listed in "ExtLookup" routine.
                #     0 = reserved argument for SetValueEx; it does nothing but has to be there
                #     t = is the type of key value (REG_DWORD for all of the Extension values; could hard code it)
                #     v = value of the key:
                #          value of 0 =
                #          value of 1 = esriESEnabled = Enabled for use.
                #          value of 2 = esriESDisabled = Diabled by the user
                #          value of 4 = esriESUnavailable = Unavailable, not licensed.
            except EnvironmentError, Argument:
                print Argument

    except:
        print '  ' + product + ' extension key does not exists.'

CloseKey(aReg)
