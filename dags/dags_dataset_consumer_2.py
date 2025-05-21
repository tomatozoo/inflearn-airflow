from airflow import Dataset
from airflow import DAG
from airflow.operators.bash import BashOperator
import pendulum

dataset_dags_dataset_producer_1 = Dataset("dataset_dags_dataset_producer_1")
dataset_dags_dataset_producer_2 = Dataset("dataset_dags_dataset_producer_2")

with DAG(
    dag_id='dags_dataset_consumer_2',
    # 객체를 구독하겠다는 의미
    schedule=[dataset_dags_dataset_producer_1, dataset_dags_dataset_producer_2],
    start_date=pendulum.datetime(2025, 5, 1, tz="Asia/Seoul"),
    catchup=False
) as dag:
    bash_task = BashOperator(
        task_id="bash_task",
        bash_command="echo {{ti.run_id}} && echo 'producer_1와 producer_2이 완료되면 수행'"
    )