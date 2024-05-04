from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.python_operator import PythonOperator
import subprocess

def install_deps():
    subprocess.run(["/usr/local/airflow/dbt_venv/bin/dbt", "deps"], cwd="/usr/local/airflow/dbt/traffic")

import subprocess

def run_dbt():
    subprocess.run(["dbt", "run", "--profiles-dir", "/usr/local/airflow/dbt"], cwd="/usr/local/airflow/dbt/traffic")

def test_dbt():
    subprocess.run(["dbt", "test", "--profiles-dir", "/usr/local/airflow/dbt"], cwd="/usr/local/airflow/dbt/traffic")

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}

dag = DAG(
    'dbt_workflow',
    default_args=default_args,
    description='A DAG to install dependencies, run dbt, and test dbt for the traffic project',
    schedule_interval=None,
    start_date=days_ago(1),
    tags=['dbt'],
)

install_deps_task = PythonOperator(
    task_id='traffic_install_deps',
    python_callable=install_deps,
    dag=dag,
)

run_dbt_task = PythonOperator(
    task_id='traffic_run_dbt',
    python_callable=run_dbt,
    dag=dag,
)

test_dbt_task = PythonOperator(
    task_id='traffic_test_dbt',
    python_callable=test_dbt,
    dag=dag,
)

install_deps_task >> run_dbt_task >> test_dbt_task
