WITH component_runs AS (

  SELECT * 
  
  FROM {{ source('hive_metastore.prophecy_rajat_dev_cloud', 'component_runs') }}

)

SELECT *

FROM component_runs
