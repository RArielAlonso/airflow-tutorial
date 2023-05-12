from datetime import timedelta,datetime

from airflow import DAG
from airflow.operators.python import PythonOperator

defaults_args={
    'owner':'Ariel',
    'retries':5,
    'retry_delay':timedelta(minutes=5)
}

def greet(ti):
    first_name=ti.xcom_pull(task_ids='get_name', key='first_name')
    last_name=ti.xcom_pull(task_ids='get_name', key='last_name')
    age=ti.xcom_pull(task_ids='get_age', key='age')
    print(f'Hello World ! My name is {first_name} {last_name} and I am {age} years old')

def get_name(ti):
    ti.xcom_push(key='first_name',value='Ariel')
    ti.xcom_push(key='last_name',value='Alonso')

def get_age(ti):
    ti.xcom_push(key='age',value=36)

with DAG(
    default_args=defaults_args,
    dag_id='our_first_dag_with_python_operator_xcom_v4',
    description='Our first DAG with Python Operator',
    start_date=datetime(2023,5,12),
    schedule_interval='@daily'

) as dag:
    task1=PythonOperator(
        task_id='greet',
        python_callable=greet,
    )
    task2=PythonOperator(
        task_id='get_name',
        python_callable=get_name
    )
    task3=PythonOperator(
        task_id='get_age',
        python_callable=get_age
    )


[task3,task2]>>task1

