select productname, NAME from AMD_MASTER_CAT;

select * from MASTERPATHS;

SELECT Products.PRODUCT_URL, Paths.PATH MosaicFilePath
FROM (SELECT * FROM sde.MasterPaths WHERE PATH NOT LIKE '%AMD_%') Paths, SP_DBA.SP_ESRI_PRODUCT02 Products
WHERE
SUBSTR(REGEXP_REPLACE(Products.PRODUCT_URL,'\/', '\', 1, 0, 'in'), INSTR(REGEXP_REPLACE(Products.PRODUCT_URL,'\/', '\', 1, 0, 'in'), '\SOFPREP\') + 0) = 
(SUBSTR(Paths.PATH, INSTR(Paths.PATH, '\SOFPREP\') + 0));

SELECT PRODUCT_URL, (INSTR(PRODUCT_URL,'.I4T')-8) as B2,
SUBSTR(PRODUCT_URL, INSTR(PRODUCT_URL,'archive_root')+LENGTH('archive_root'),
(INSTR(PRODUCT_URL,'.I4T')-(INSTR(PRODUCT_URL,'archive_root')+LENGTH('archive_root')+8))) as JoinPath
from SP_DBA.SP_ESRI_PRODUCT02 Products WHERE FILENAME LIKE '%.I4T';