from executionk3s_pankaj_databricks_automationjobs_project_airflow_db_mwaa_automation.utils import *

def Model_0():
    from airflow.operators.bash import BashOperator
    import os
    import zipfile
    import tempfile

    return BashOperator(
        task_id = "Model_0",
        bash_command = " && ".join(
          ["{} && cd $tmpDir/{}".format(
             (
               "set -euxo pipefail && tmpDir=`mktemp -d` && git clone "
               + "--depth 1 {} --branch {} $tmpDir".format(
                 "https://github.com/pankajb23/test_Databricks_jobs_1",
                 "__PROJECT_FULL_RELEASE_TAG_PLACEHOLDER__"
               )
             ),
             "test/databricks_project"
           ),            "dbt snapshot --profile run_profile -s +newSnap",  "dbt seed --profile run_profile -s +newSnap",            "dbt test --profile run_profile -s +newSnap"]
        ),
        env = {"DBT_DATABRICKS_INVOCATION_ENV" : "prophecy", "DBT_PROFILES_DIR" : "/home/airflow/gcs/data"},
        append_env = True,
    )
