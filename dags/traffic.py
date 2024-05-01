# dags/jaffle_shop.py

from cosmos.providers.dbt.dag import DbtDag
from airflow.datasets import Dataset
from datetime import datetime

traffic = DbtDag(
    dag_id="traffic",
    dbt_project_name="traffic",
    start_date=datetime(2024, 1, 5),
    schedule="@daily",
    conn_id="postgres",
    dbt_args={
        "schema": "public",
        "dbt_executable_path": "/usr/local/airflow/dbt_venv/bin/dbt",
        },
)

traffic