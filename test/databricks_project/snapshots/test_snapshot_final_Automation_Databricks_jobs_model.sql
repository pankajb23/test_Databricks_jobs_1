{% snapshot test_snapshot_final_Automation_Databricks_jobs_model %}
{{
  config({    
    "check_cols": ["id", "name"],
    "strategy": 'check',
    "target_schema": "QA_SCHEMA",
    "unique_key": "id",
    "updated_at": "updated_at"
  })
}}

WITH test_Automation_Databricks_jobs_model AS (

  SELECT *
  
  FROM {{ ref('test_Automation_Databricks_jobs_model')}}

)

SELECT *

FROM test_Automation_Databricks_jobs_model

{% endsnapshot %}
