from datetime import datetime,timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator

default_args={
    'owner':'Ariel',
    'retries':5,
    'retry_delay':timedelta(minutes=2)
}
with DAG (
    dag_id='dag_with_cron_expresion_v2',
    default_args=default_args,
    description='Dag with CRON EXPRESION',
    start_date=datetime(2023,5,1),
    schedule_interval='0 0 * * *',
    catchup=True
) as dag:
    task1=BashOperator(
        task_id='first_task',
        bash_command='echo Dag with CRON EXPRESION!'
        )