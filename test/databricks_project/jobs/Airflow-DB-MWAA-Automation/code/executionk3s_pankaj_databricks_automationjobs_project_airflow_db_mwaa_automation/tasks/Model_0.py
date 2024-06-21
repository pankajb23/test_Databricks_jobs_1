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
               + "{} --branch {} --single-branch $tmpDir".format(
                 "https://github.com/pankajb23/test_Databricks_jobs_1",
                 None
               )
             ),
             "test/databricks_project"
           ),            "dbt seed --profile run_profile",  "dbt run --profile run_profile",  "dbt test --profile run_profile"]
        ),
        env = {"DBT_DATABRICKS_INVOCATION_ENV" : "prophecy", "DBT_PROFILES_DIR" : "/home/airflow/gcs/data"},
        append_env = True,
    )
