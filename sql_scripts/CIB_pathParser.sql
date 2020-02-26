SELECT 
row_number() over ( order by PRODUCT_ID ) as row_id,
P_SUBTYPE || ' ' ||INFORMATION_DATE as Title,
SEC_CLASS|| ' ' ||CAVEATS|| ' ' ||SOURCE_AGENCY|| ' ' ||COUNTRY1|| ' ' ||FILENAME|| ' ' ||DATA_FORMAT|| ' ' ||RESOLUTION|| ' ' ||RES_MEASURE|| ' ' ||COLLECTION_METHOD || ' ' || SENSOR_TYPE || ' ' ||AZIMUTH|| ' ' ||OBLIQUITY as Information,
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
Products.SEC_CLASS,
Products.CAVEATS,
Products.SOURCE_AGENCY,
Products.INFORMATION_DATE,
Products.DATA_FORMAT,
--Products.DATA_FORMAT_INFO,
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
--Products.COORD_FMT,
Products.IMAGERY_ID,
Products.RESOLUTION,
Products.RES_MEASURE,
Products.RESOLUTION || ' ' ||Products.RES_MEASURE as RESOLUTION_FULL,
--Products.COLLECTION_METHOD,
Products.SENSOR_TYPE,
Products.AZIMUTH,
Products.OBLIQUITY,
--Products.NIMA_ID,
Products.PRODUCT_DESCRIPTION,
--Products.VERIFY_USER,
Products.VERIFY_DATE,
--Products.INACTIVE,
Products.PRODUCT_URL,
--Products.PREVIEW_URL,
--Products.MULTIPOINT,
Products.INSERT_DATE,
Products.INSERT_USER,
--Products.CONTAINER_FOLDER,
Products.FILENAME,
--Products.PST_GROUP,
--Products.PST_SUBGROUP,
--Products.SPECTRUM,
--Products.BAND_QTY,
Products.P_SIZE_USED_MB,PRODUCT_URL,COUNTRY1,
Products.GEOCELL,
--Products.GCLQUAD,
--Products.DD_CRD_CHECK,
--Products.TSCHECK_RESPONSE,
--Products.DMS_CRD_CHECK,
--Products.OLN_YN,
--Products.OLN_STAT,
--Products.P_UINP_YN,
--Products.CC2,
--Products.CC3,
--Products.UCC1,
--Products.UCC2,
--Products.UCC3,
--Products.CCQTY,
--Products.LOCALE1,
--Products.LOC2,
--Products.LOC3,
--Products.LOC4,
Path.PATH as MasterPathPATHS,
  NVL2(Paths.PATH,'Yes','No') as is_downloadable,
  NVL2(Paths.PATH,'https://dartweb.esri.com/workflow/rest/services/'||P_SUBTYPE||'/ImageServer',null) as web_url,
  NVL2(Paths.PATH,sde.ST_MinX(mosaics.shape),Products.LL_LONG) as LL_LONG,
  NVL2(Paths.PATH,sde.ST_MinY(mosaics.shape),Products.LL_LAT) as LL_LAT,
  NVL2(Paths.PATH,sde.ST_MaxX(mosaics.shape),Products.UR_LONG) as UR_LONG,
  NVL2(Paths.PATH,sde.ST_MaxY(mosaics.shape),Products.UR_LAT) as UR_LAT
--,ST_GEOMETRY(SP_DBA.GET_EXTENT( NVL2(Paths.PATH,sde.ST_MinX(mosaics.shape),Products.LL_LONG),NVL2(Paths.PATH,sde.ST_MinY(mosaics.shape),Products.LL_LAT),NVL2(Paths.PATH,sde.ST_MaxX(mosaics.shape),Products.UR_LONG) ,NVL2(Paths.PATH,sde.ST_MaxY(mosaics.shape),Products.UL_LAT))) as Extent 
  FROM SP_DBA.SP_ESRI_PRODUCT02 Products
  LEFT JOIN 
  sde.MasterPaths Paths on 
    (SUBSTR(REGEXP_REPLACE(Products.PRODUCT_URL,'\/', '\', 1, 0, 'in'), INSTR(REGEXP_REPLACE(Products.PRODUCT_URL,'\/', '\', 1, 0, 'in'), '\archive_root\') + 0) 
    = 
    (SUBSTR(REGEXP_REPLACE(Paths.PATH,'\/', '\', 1, 0, 'in'),           INSTR(REGEXP_REPLACE(Paths.PATH,'\/', '\', 1, 0, 'in'), '\archive_root\') + 0)))
  --REGEXP_REPLACE(Products.PRODUCT_URL,'\/', '\', 1, 0, 'in')                           =    regexp_replace(Paths.PATH, '^[a-zA-Z]:\', '\archive_root')
  
  LEFT JOIN sde.AMD_MASTER_CAT Mosaics on regexp_replace(Mosaics.NAME,'\.[^\.]*$','')  =    regexp_replace(Products."FILENAME",'\.[^\.]*$','')
  
  
  
  --WHERE Products.INSERT_DATE > sysdate-1 OR Products.INSERT_DATE is null