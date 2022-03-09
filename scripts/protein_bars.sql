CREATE OR REPLACE TABLE `ml-q-a.protein_bars.protein_bars` AS
WITH
  _getting_id_a AS (
  SELECT
    DISTINCT product_description,
    product_url,
    ARRAY_REVERSE(SPLIT(product_url, '/'))[SAFE_OFFSET(0)] AS product_id
  FROM
    `ml-q-a.protein_bars.descriptions_base`
  WHERE
    product_description != ""
    AND CONTAINS_SUBSTR(product_url,
      "https://www.walmart.com/ip/") != FALSE ),
  
  _getting_id_b AS (
  SELECT
    * EXCEPT(product_id),
    SPLIT(product_id, '?')[SAFE_OFFSET(0)] AS product_id
  FROM
    _getting_id_a),
  
  _feature_engineering_join AS (
  SELECT
    _getting_id_b.product_url,
    _getting_id_b.product_id,
    LOWER(REPLACE(dplus.product_title, ",", "")) AS product_title,
    REGEXP_REPLACE(LOWER(REPLACE(TRIM(REGEXP_REPLACE(dplus.product_description, r'<[^>]*>', ' ')), ",", "")),'[ ]+',' ') AS product_description,
    REGEXP_REPLACE(LOWER(REPLACE(TRIM(REGEXP_REPLACE(dplus.product_ingredients, r'<[^>]*>', ' ')), ",", "")),'[ ]+',' ') AS product_ingredients
  FROM
    _getting_id_b
  JOIN
    `ml-q-a.protein_bars.descriptions_plus` AS dplus
  ON
    _getting_id_b.product_id = CAST(dplus.product_id AS STRING) )
  
  SELECT
    DISTINCT product_url,
    product_title,
    TRIM(CONCAT(product_description,' ', product_ingredients)) AS product_full_description,
    '' AS question
  FROM
    _feature_engineering_join
  ORDER BY
    product_title
