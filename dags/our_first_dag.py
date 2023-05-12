from datetime import datetime,timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator

default_args={
    'owner':'Ariel',
    'retries':5,
    'retry_delay':timedelta(minutes=2)
}

with DAG (
    dag_id='our_first_dag_v5',
    default_args=default_args,
    description='This is our first DAG',
    start_date=datetime(2023,5,12,12),
    schedule_interval='@daily'
) as dag:
    task1=BashOperator(
        task_id='first_task',
        bash_command='echo hello world, this is our first task'
    )
    task2=BashOperator(
        task_id='second_task',
        bash_command='echo hey, I am task two, i will run after task 1'
    )
    task3=BashOperator(
        task_id='third_task',
        bash_command='echo hello, i am task 3 and will round after task1'
    )

    #first method of dependencies
    #task1.set_downstream(task2)
    #task1.set_downstream(task3)
    #second method of dependencies
    #task1>>task2
    #task1>>task3
    #third method of dependencies
    task1>>[task2,task3]