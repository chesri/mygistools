select productname, NAME from AMD_MASTER_CAT;

select * from MASTERPATHS;

SELECT Products.PRODUCT_URL, Paths.PATH MosaicFilePath
FROM (SELECT * FROM sde.MasterPaths WHERE PATH NOT LIKE '%AMD_%') Paths, SP_DBA.SP_ESRI_PRODUCT02 Products
WHERE
SUBSTR(REGEXP_REPLACE(Products.PRODUCT_URL,'\/', '\', 1, 0, 'in'), INSTR(REGEXP_REPLACE(Products.PRODUCT_URL,'\/', '\', 1, 0, 'in'), '\SOFPREP\') + 0) = 
(SUBSTR(Paths.PATH, INSTR(Paths.PATH, '\SOFPREP\') + 0));
