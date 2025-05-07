from airflow import DAG
import pendulum
import datetime
from airflow.decorators import task
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="dags_python_show_templates",
    schedule="10 0 * * 6#1",
    start_date=pendulum.datetime(2025, 5, 1, tz="Asia/Seoul"),
    catchup=False
) as dag:
    
    @task(task_id='python_task')
    def show_templates(**kwargs):
        from pprint import pprint
        pprint(kwargs)
    show_templates()
