{{
  config({    
    "materialized": "table",
    "full_refresh": true
  })
}}

WITH pipeline_runs AS (

  SELECT * 
  
  FROM {{ source('hive_metastore.prophecy_rajat_dev_cloud', 'pipeline_runs') }}

)

SELECT *

FROM pipeline_runs
