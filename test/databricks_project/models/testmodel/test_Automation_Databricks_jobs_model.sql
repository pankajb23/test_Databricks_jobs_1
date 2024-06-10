{{
  config({    
    "materialized": "table",
    "full_refresh": true
  })
}}

WITH newSnap AS (

  SELECT * 
  
  FROM {{ ref('newSnap')}}

)

SELECT *

FROM newSnap
