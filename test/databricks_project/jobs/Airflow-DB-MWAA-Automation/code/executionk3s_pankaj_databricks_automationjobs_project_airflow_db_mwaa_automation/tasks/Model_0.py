from executionk3s_pankaj_databricks_automationjobs_project_airflow_db_mwaa_automation.utils import *

def Model_0():
    from airflow.operators.bash import BashOperator
    import os
    import zipfile
    import tempfile
    envs = {"DBT_DATABRICKS_INVOCATION_ENV" : "prophecy"}
    dbt_props_cmd = ""

    if "/home/airflow/gcs/data":
        envs = {"DBT_DATABRICKS_INVOCATION_ENV" : "prophecy", "DBT_PROFILES_DIR" : "/home/airflow/gcs/data"}

    if "run_profile":
        dbt_props_cmd = " --profile run_profile"

    # avoiding false positive here,
    # there will be gems which are following older model and after migration will have both these things set.
    # it means that maybe customer move to project runMode but entityKind is not updated.
    # and also this is two level search
    # project contains project but model contains model / snapshots
    if "newSnap":
        dbt_props_cmd = f"{dbt_props_cmd} -s newSnap" #dbt_props_cmd + " -s +" + snapshot_selector

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
           ),            "dbt snapshot" + dbt_props_cmd,  "dbt seed" + dbt_props_cmd,  "dbt test" + dbt_props_cmd]
        ),
        env = envs,
        append_env = True,
    )
