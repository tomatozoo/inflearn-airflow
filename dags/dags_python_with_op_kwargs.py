from airflow import DAG
from airflow.operators.python import PythonOperator
from common.common_func import regist2
import pendulum

with DAG(
    dag_id="dags_python_with_op_kwargs",
    schedule="0 2 * * 1",
    start_date=pendulum.datetime(2025, 3, 1, tz="Asia/Seoul"),
    catchup=False, 
    tags=["example"],
) as dag:
    
    regist2_t1 = PythonOperator(
        task_id = 'regist_t2',
        python_callable=regist2,
        op_args=["yj", "woman", "hi"],
        op_kwargs={"email": "yj@naver.com", "phone": "010000000000"}
    )

    regist2_t1
