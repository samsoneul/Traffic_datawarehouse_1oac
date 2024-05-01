from airflow import DAG
from airflow.utils.task_group import TaskGroup
from pendulum import datetime

from cosmos.providers.dbt.core.operators import (
    DbtDepsOperator,
    DbtSeedOperator,
)

with DAG(
    dag_id="import-seeds",
    start_date=datetime(2023, 1, 1),
    schedule=None,
    catchup=False,
    max_active_runs=1,
) as dag:

    deps_install = DbtDepsOperator(
        task_id="jaffle_shop_install_deps",
        project_dir="/usr/local/airflow/dbt/traffic",
        schema="public",
        dbt_executable_path="/usr/local/airflow/dbt_venv/bin/dbt",
        conn_id="postgres",
    )
    deps_install    