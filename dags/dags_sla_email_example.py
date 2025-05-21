from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.decorators import task
from airflow.exceptions import AirflowException
import pendulum
from datetime import timedelta
from airflow.models import Variable


email_str = Variable.get("email_target")
email_lst = [email.strip() for email in email_str.split(",")]

with DAG(
    dag_id="dags_sla_email_example",
    start_date=pendulum.datetime(2025, 5, 1, tz="Asia/Seoul"),
    catchup=False,
    schedule="0 1 * * *",
    default_args={
        "sla": timedelta(seconds=70), 
        "email": email_lst
    }
) as dag:
    task_slp_30s = BashOperator(
        task_id='task_slp_30s',
        bash_command='sleep 30'
    )

    task_slp_60s = BashOperator(
        task_id='task_slp_60',
        bash_command='sleep 60'
    )

    task_slp_30s >> task_slp_60s
