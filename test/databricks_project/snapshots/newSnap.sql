{% snapshot newSnap %}
{{
  config({    
    "strategy": 'timestamp',
    "target_schema": 'delta01',
    "unique_key": 'fabric_uid',
    "updated_at": 'created_at'
  })
}}

WITH newTemporaryModel AS (

  SELECT *
  
  FROM {{ ref('newTemporaryModel')}}

)

SELECT *

FROM newTemporaryModel

{% endsnapshot %}
