from __future__ import annotations

import datetime

import pendulum # type을 좀더 쉽게 사용할 수 있게 해줌

from airflow.models.dag import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator

with DAG(
    dag_id="dags_bash_operator",
    schedule="0 0 * * *",
    start_date=pendulum.datetime(2021, 1, 1, tz="Asia/Seoul"),
    catchup=False,
) as dag:
    bash_t1 = BashOperator(
        task_id="bash_t1",
        bash_command="echo whoami",
    )

    bash_t2 = BashOperator(
        task_id = "bash_t2",
        bash_command="echo $HOSTNAME",
    )

    bash_t1 >> bash_t2
    

if __name__ == "__main__":
    dag.test()
