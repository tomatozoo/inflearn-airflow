from airflow import DAG
from airflow.decorators import task
import pendulum

with DAG(
    dag_id="dags_python_task_decorator",
    schedule="0 2 * * 1",
    start_date=pendulum.datetime(2025, 3, 1, tz="Asia/Seoul"),
    catchup=False, 
    tags=["example"],
) as dag:
    
    @task(task_id="python_task_1")
    def print_context(some_input):
        print(some_input)

    python_task_1 = print_context("task decorator 실행")