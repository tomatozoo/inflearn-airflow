from airflow import Dataset 
from airflow import DAG
from airflow.operators.bash import BashOperator
import pendulum


dataset_dags_dataset_producer_1 = Dataset("dataset_dags_dataset_producer_1")


with DAG(
    dag_id='dags_dataset_producer_1',
    schedule="0 7 * * *",
    start_date=pendulum.datetime(2025, 5, 1, tz="Asia/Seoul"),
    catchup=False
) as dag:
    bash_task = BashOperator(
        task_id = 'bash_task',
        outlets=[dataset_dags_dataset_producer_1],
        bash_command='echo "producer_2 수행 완료"'
    )
