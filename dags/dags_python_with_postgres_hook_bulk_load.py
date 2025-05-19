from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook
import pendulum


with DAG(
    dag_id='dags_python_with_postgres_hook_bulk_load',
    start_date=pendulum.datetime(2025, 5, 1, tz='Asia/Seoul'),
    schedule='30 9 * * *',
    catchup=False
) as dag:
    
    def insrt_postgres(postgres_conn_id, tbl_nm, file_nm, **kwargs):
        postgres_hook = PostgresHook(postgres_conn_id)
        postgres_hook.bulk_load(tbl_nm, file_nm)
    
    insrt_postgres = PythonOperator(
        task_id='insrt_postgres',
        python_callable=insrt_postgres,
        op_kwargs={
            "postgres_conn_id": "postgres-custom-db",
            "tbl_nm": "tb_bulk",
            "file_nm": "/opt/airflow/files/bigdata.csv"
        }

    )

    insrt_postgres

