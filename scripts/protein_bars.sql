CREATE OR REPLACE TABLE `ml-q-a.protein_bars.protein_bars` AS
WITH
  clean AS (
  SELECT
    DISTINCT product_description,
    product_url,
    ARRAY_REVERSE(SPLIT(product_url, '/'))[SAFE_OFFSET(0)] AS product_id
  FROM
    `ml-q-a.protein_bars.descriptions_base`
  WHERE
    product_description != ""
    AND CONTAINS_SUBSTR(product_url,"https://www.walmart.com/ip/") != FALSE ),

  ids AS (
  SELECT
    * EXCEPT(product_id),
    SPLIT(product_id, '?')[SAFE_OFFSET(0)] AS product_id
  FROM
    clean),
  
  clean2 AS (
  SELECT
    product_url,
    ids.product_id,
    LOWER(REPLACE(product_title, ",", "")) AS product_title,
    REGEXP_REPLACE(LOWER(REPLACE(TRIM(REGEXP_REPLACE(ids2.product_description, r'<[^>]*>', ' ')), ",", "")),'[ ]+',' ') AS product_description,
    REGEXP_REPLACE(LOWER(REPLACE(TRIM(REGEXP_REPLACE(ids2.product_ingredients, r'<[^>]*>', ' ')), ",", "")),'[ ]+',' ') AS product_ingredients
  FROM
    ids
  JOIN
    `ml-q-a.protein_bars.descriptions_plus` AS ids2
  ON
    ids.product_id = CAST(ids2.product_id AS STRING) )

SELECT
  *,
  CONCAT(product_description,' ', product_ingredients) AS product_full_description,
  '' AS question
FROM
  clean2
