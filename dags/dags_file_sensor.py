from airflow import DAG
from airflow.sensors.filesystem import FileSensor
import pendulum


with DAG(
    dag_id='dags_file_sensor',
    start_date=pendulum.datetime(2025, 5, 1, tz="Asia/Seoul"),
    schedule="0 7 * * *",
    catchup=False
) as dag:
    file_sensor = FileSensor(
        task_id='file_sensor',
        fs_conn_id='file_connection',
        filepath='bigdata.csv',
        recursive=False,
        poke_interval=10,
        timeout=60*60*24,
        mode='reschedule'
    )