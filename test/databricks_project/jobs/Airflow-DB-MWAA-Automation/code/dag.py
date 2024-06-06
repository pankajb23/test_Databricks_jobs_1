import os
import sys
import pendulum
from datetime import timedelta
import airflow
from airflow import DAG
from airflow.models.param import Param
from airflow.decorators import task
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from executionk3s_pankaj_databricks_automationjobs_project_airflow_db_mwaa_automation.tasks import Model_0
PROPHECY_RELEASE_TAG = "__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__"

with DAG(
    dag_id = "executionk3s_pankaj_Databricks_AutomationJobs_Project_Airflow_DB_MWAA_Automation", 
    schedule_interval = "0 0 17 2 *", 
    default_args = {"owner" : "Prophecy", "ignore_first_depends_on_past" : True, "do_xcom_push" : True}, 
    start_date = pendulum.today('UTC'), 
    end_date = pendulum.datetime(2024, 6, 29, tz = "UTC"), 
    catchup = True, 
    tags = []
) as dag:
    Model_0_op = Model_0()
