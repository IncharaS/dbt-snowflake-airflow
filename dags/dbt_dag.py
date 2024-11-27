
from airflow.decorators import dag
from cosmos import DbtTaskGroup
from cosmos.config import ProjectConfig, ProfileConfig, ExecutionConfig
from cosmos.profiles import SnowflakeUserPasswordProfileMapping
from pendulum import datetime

# Profile, project, and execution configurations remain the same

# Define profile configuration
profile_config = ProfileConfig(
    profile_name="default",
    target_name="dev",
    profile_mapping=SnowflakeUserPasswordProfileMapping(
        conn_id="snowflake_conn",  # Ensure this is a valid Airflow connection
        profile_args={"database": "dbt_db", "schema": "dbt_schema"},
    )
)

# Define project configuration
project_config = ProjectConfig(
    dbt_project_path="/usr/local/airflow/dags/dbt/data_pipeline",
)

# Define execution configuration
execution_config = ExecutionConfig(
    dbt_executable_path="dbt", # Adjust this to your dbt executable path
)



@dag(
    dag_id="dbt_snowflake_dag",
    schedule_interval="@daily",
    start_date=datetime(2024, 11, 25),
    catchup=False,
    default_args={"owner": "airflow"},
    tags=["dbt", "snowflake"],
)
def dbt_snowflake_dag():

    dbt_run = DbtTaskGroup(
        group_id="dbt_dag",
        project_config=project_config,
        profile_config=profile_config,
        execution_config=execution_config,
        operator_args={"install_deps": True},
    )

    # You can add other tasks here if needed
    # For example:
    # @task
    # def pre_dbt_task():
    #     print("Preparing for DBT run")
    # 
    # @task
    # def post_dbt_task():
    #     print("DBT run completed")
    #
    # pre_dbt_task() >> dbt_run >> post_dbt_task()

dbt_snowflake_dag()