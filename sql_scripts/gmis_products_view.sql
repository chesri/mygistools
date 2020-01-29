SELECT 
row_number() over ( order by PRODUCT_ID ) as row_id, 
NVL2(P_SUBTYPE,P_SUBTYPE || ' ' ||INFORMATION_DATE,Mosaics.NAME) as Title, 
NVL2(P_SUBTYPE,SEC_CLASS|| ' ' ||CAVEATS|| ' ' ||SOURCE_AGENCY|| ' ' ||COUNTRY1|| ' ' ||FILENAME|| ' ' ||DATA_FORMAT|| ' ' ||RESOLUTION|| ' ' ||RES_MEASURE|| ' ' ||COLLECTION_METHOD || ' ' || SENSOR_TYPE || ' ' ||AZIMUTH|| ' ' ||OBLIQUITY,Mosaics.NAME) as Information,
Products.OBJECTID,
Products.PRODUCT_ID,
Products.MEDIA_ID,
Products.P_SUBTYPE,
Products.PROD_TYPE,
CASE Products.PROD_TYPE WHEN 'D' THEN 'Database'
   WHEN 'M' THEN 'Model'
   WHEN 'F' THEN 'ISP'
   WHEN 'V' THEN 'Vector'
   WHEN 'I' THEN 'Image'
   WHEN 'E' THEN 'Elevation'
   WHEN 'C' THEN 'Chart'
   ELSE Products.PROD_TYPE END as PROD_TYPE_FULL,
NVL2(Mosaics.SECCLASS,Products.SEC_CLASS,Mosaics.SECCLASS) as SEC_CLASS,
Products.CAVEATS,
Products.SOURCE_AGENCY,
Products.INFORMATION_DATE,
Products.DATA_FORMAT,
Products.DATA_FORMAT_INFO,
Products.DATUM,
Products.LOD,
Products.SW_LAT,
Products.SW_LONG,
Products.NW_LAT,
Products.NW_LONG,
Products.NE_LAT,
Products.NE_LONG,
Products.SE_LAT,
Products.SE_LONG,
Products.COORD_FMT,
Products.IMAGERY_ID,
Products.RESOLUTION,
Products.RES_MEASURE,
Products.RESOLUTION || ' ' ||Products.RES_MEASURE as RESOLUTION_FULL,
Products.COLLECTION_METHOD,
Products.SENSOR_TYPE,
Products.AZIMUTH,
Products.OBLIQUITY,
Products.NIMA_ID,
Products.PRODUCT_DESCRIPTION,
Products.VERIFY_USER,
Products.VERIFY_DATE,
Products.INACTIVE,
Products.PRODUCT_URL,
Products.PREVIEW_URL,
Products.MULTIPOINT,
Products.INSERT_DATE,
Products.INSERT_USER,
Products.CONTAINER_FOLDER,
Products.FILENAME,
Products.PST_GROUP,
Products.PST_SUBGROUP,
Products.SPECTRUM,
Products.BAND_QTY,
Products.P_SIZE_USED_MB,LOAD_PATH,COUNTRY1,
Products.GEOCELL,
Products.GCLQUAD,
Products.DD_CRD_CHECK,
Products.TSCHECK_RESPONSE,
Products.DMS_CRD_CHECK,
Products.OLN_YN,
Products.OLN_STAT,
Products.P_UINP_YN,
Products.CC2,
Products.CC3,
Products.UCC1,
Products.UCC2,
Products.UCC3,
Products.CCQTY,
Products.LOCALE1,
Products.LOC2,
Products.LOC3,
Products.LOC4,
  NVL2(Services.PATH,NVL2(Paths.PATH,'Yes',NVL2(Products.PRODUCT_ID,'No','Yes')),'No') as is_downloadable,
  NVL2(Services.PATH,NVL2(Paths.PATH,'https://dartweb.esri.com/workflow/rest/services/'||RTRIM(SUBSTR (Services.PATH, 4 + INSTR (Services.PATH, 'AMD_', -1)),'_CAT')||'/ImageServer',NVL2(Products.PRODUCT_ID,null,'https://dartweb.esri.com/workflow/rest/services/'||RTRIM(SUBSTR (Services.PATH, 4 + INSTR (Services.PATH, 'AMD_', -1)),'_CAT')||'/ImageServer')),null) as web_url,
  NVL2(Services.PATH,NVL2(Paths.PATH,sde.ST_MinX(mosaics.shape),NVL2(Products.PRODUCT_ID,Products.LL_LONG,sde.ST_MinX(mosaics.shape))),Products.LL_LONG) as LL_LONG,
  NVL2(Services.PATH,NVL2(Paths.PATH,sde.ST_MinY(mosaics.shape),NVL2(Products.PRODUCT_ID,Products.LL_LAT,sde.ST_MinY(mosaics.shape))),Products.LL_LAT) as LL_LAT,
  NVL2(Services.PATH,NVL2(Paths.PATH,sde.ST_MaxX(mosaics.shape),NVL2(Products.PRODUCT_ID,Products.UR_LONG,sde.ST_MaxX(mosaics.shape))),Products.UR_LONG) as UR_LONG,
  NVL2(Services.PATH,NVL2(Paths.PATH,sde.ST_MaxY(mosaics.shape),NVL2(Products.PRODUCT_ID,Products.UR_LAT,sde.ST_MaxY(mosaics.shape))),Products.LL_LONG) as UR_LAT
FROM SP_DBA.SP_ESRI_PRODUCT02 Products   
FULL OUTER JOIN 
sde.AMD_MASTER_CAT Mosaics on 
regexp_replace(Products.FILENAME, '\.[^\.]*$','') = regexp_replace(Mosaics.NAME, '\.[^\.]*$','')
LEFT JOIN 
(SELECT * FROM sde.MasterPaths WHERE PATH NOT LIKE '%AMD_%') 
Paths on Mosaics.OBJECTID = Paths.SOURCEOID and 
  (SUBSTR(REGEXP_REPLACE(Products.PRODUCT_URL,'\/', '\', 1, 0, 'in'), INSTR(REGEXP_REPLACE(Products.PRODUCT_URL,'\/', '\', 1, 0, 'in'), '\archive_root\') + 0) 
    = 
--  regexp_replace(Paths.PATH, '^[a-zA-Z]:\', '\archive_root') 
  (SUBSTR(Paths.PATH, INSTR(Paths.PATH, '\archive_root\') + 0)) 
  or 
  REGEXP_REPLACE(Products.PRODUCT_URL,'\/', '\', 1, 0, 'in') = Paths.PATH
    or 
  Products.PRODUCT_URL=Paths.PATH )
LEFT JOIN
(SELECT SOURCEOID,PATH FROM sde.MasterPaths WHERE PATH LIKE '%AMD_%' GROUP BY SOURCEOID,PATH) Services on Mosaics.OBJECTID = Services.SOURCEOID