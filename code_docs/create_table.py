#import the DAG object
from airflow import DAG        
from datetime import datetime
from airflow.providers.postgres.operators.postgres import PostgresOperator

#define unique DAG Id, start date, schedule interval, catchup
with DAG('user_processing', start_date = datetime(2022, 1, 1), 
    schedule_interval = "@daily", catchup = False) as dag:
    #None


    #create table, unique task id, sql request
    create_table = PostgresOperator(
        task_id = 'create_table',
        postgres_conn_id = 'postgres',
        sql = '''
            CREATE table IF NOT EXISTS users {
                firstname TEXT NOT NULL,
                lastname TEXT NOT NULL,
                country TEXT NOT NULL,
                username TEXT NOT NULL,
                password TEXT NOT NULL,
                email TEXT NOT NULL
            };
        '''
    )
