from staging_abhisheks_e2etests_databricks_automationjobs_project_airflow_db_mwaa_automation.utils import *

def Model_1():
    from datetime import timedelta
    from airflow.operators.bash import BashOperator
    envs = {}
    dbt_props_cmd = ""

    if "/home/airflow/gcs/data":
        envs = {"DBT_PROFILES_DIR" : "/home/airflow/gcs/data"}

    if "run_profile":
        dbt_props_cmd = " --profile run_profile"

    return BashOperator(
        task_id = "Model_1",
        bash_command = " && ".join(
          ["{} && cd $tmpDir/{}".format(
             (
               "set -euxo pipefail && tmpDir=`mktemp -d` && git clone "
               + "{} --branch {} --single-branch $tmpDir".format(
                 "https://github.com/pankajb23/test_Databricks_jobs_1",
                 "main2"
               )
             ),
             "test/databricks_project"
           ),            "dbt run" + dbt_props_cmd,  "dbt test" + dbt_props_cmd]
        ),
        env = envs,
        append_env = True,
    )
