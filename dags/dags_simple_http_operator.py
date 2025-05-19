from airflow import DAG
from airflow.providers.http.operators.http import HttpOperator
from airflow.operators.bash import BashOperator
from airflow.operators.trigger_dagrun import TriggerDagRunOperator
from airflow.decorators import task
import pendulum

with DAG(
    dag_id='dags_simple_http_operator',
    start_date=pendulum.datetime(2025, 5, 1, tz='Asia/Seoul'),
    schedule='30 9 * * *',
    catchup=False
) as dag:
    
    ''' 서울시 부동산 실거래가 정보 '''
    seoul_apt_info = HttpOperator(
        task_id='seoul_apt_info',
        http_conn_id='seoul_api',
        endpoint='{{var.value.apikey_openapi_seoul_go_kr}}/json/tbLnOpendataRtmsV/1/5/',
        method='GET',
        headers={
            'Content-Type': 'application/json',
            'charset': 'utf-8',
            'Accept': '*/*'
        }
    )

    @task(task_id='python_2')
    def python_2(**kwargs):
        ti = kwargs['ti']
        result = ti.xcom_pull(task_ids='seoul_apt_info')

        import json
        from pprint import pprint

        pprint(json.loads(result))

    seoul_apt_info >> python_2()
