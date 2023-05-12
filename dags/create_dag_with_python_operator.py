from datetime import timedelta,datetime

from airflow import DAG
from airflow.operators.python import PythonOperator

defaults_args={
    'owner':'Ariel',
    'retries':5,
    'retry_delay':timedelta(minutes=5)
}

def greet(name,age):
    print(f'Hello World ! My name is {name} and I am {age} years old')

with DAG(
    default_args=defaults_args,
    dag_id='our_first_dag_with_python_operator_v1',
    description='Our first DAG with Python Operator',
    start_date=datetime(2023,5,12),
    schedule_interval='@daily'

) as dag:
    task1=PythonOperator(
        task_id='greet',
        python_callable=greet,
        op_kwargs={'name':'Ariel',
                 'age':36}
    )

task1

