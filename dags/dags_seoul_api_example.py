from airflow import DAG
from airflow.providers.http.operators.http import HttpOperator
from airflow.operators.bash import BashOperator
from airflow.operators.trigger_dagrun import TriggerDagRunOperator
from airflow.decorators import task
import pendulum

from operators.seoul_api_to_csv_operator import SeoulApiToCsvOperator


with DAG(
    dag_id='dags_seoul_api_example',
    start_date=pendulum.datetime(2025, 5, 1, tz='Asia/Seoul'),
    schedule='30 9 * * *',
    catchup=False
) as dag:
    
    # http://openapi.seoul.go.kr:8088/(인증키)/xml/tbLnOpendataRtmsV/1/5/
    seoul_apt_status = SeoulApiToCsvOperator(
        task_id='seoul_apt_status',
        dataset_name='tbLnOpendataRtmsV',
        path='/opt/airflow/files/tbLnOpendataRtmsV/{{data_interval_end.in_timezone("Asia/Seoul") | ds_nodash }}',
        file_name='tbLnOpendataRtmsV.csv'
    )

    seoul_apt_status


