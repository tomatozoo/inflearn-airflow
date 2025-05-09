from airflow import DAG
import pendulum
import datetime
from airflow.decorators import task

with DAG(
    dag_id="dags_python_with_xcom_eg1",
    schedule="30 6 * * *",
    start_date=pendulum.datetime(2025, 5, 1, tz="Asia/Seoul"),
    catchup=False
) as dag:
    # xcom 첫번째 방식. kwargs - ti - xcom_push / xcom_pull
    # 주의: 서로 다른 task에서 같은 key의 값을 push하는 경우, 
    # pull할 때 task id를 지정해줘야 함 (아닌 경우, 가장 마지막꺼 리턴함)
    @task(task_id='python_xcom_push_task1')
    def xcom_push1(**kwargs):
        ti = kwargs.get('ti')
        ti.xcom_push(key="result1", value="value_1")
        ti.xcom_push(key="result2", value=[1, 2, 3])
    
    @task(task_id='python_xcom_push_task2')
    def xcom_push2(**kwargs):
        ti = kwargs.get('ti')
        ti.xcom_push(key="result1", value="value_2")
        ti.xcom_push(key="result2", value=[1, 2, 3, 4])
        print(ti)

    @task(task_id='python_xcom_pull_task')
    def xcom_pull(**kwargs):
        ti = kwargs.get('ti')
        value1 = ti.xcom_pull(key='result1')
        value2 = ti.xcom_pull(key='result2', task_ids='python_xcom_push_task1')
        print(value1)
        print(value2)

    xcom_push1() >> xcom_push2() >> xcom_pull()
