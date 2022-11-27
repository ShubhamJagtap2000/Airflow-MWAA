#import the DAG object
from airflow import DAG        
from datetime import datetime
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.providers.sensors.http import HttpSensor
from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.operators.python import PythonOperator
import json
from pandas import json_normalize

def _process_user(ti):
    user = ti.xcom_pull(task_ids = "extract_user")
    user = user['results'][0]
    processed_user = json_normalize({
        'firstname' : user['name']['first'],
        'lastname' : user['name']['last'],
        'country' : user['location']['country'],
        'username' : user['login']['username'],
        'password' : user['login']['password'],
        'email' : user['email'] })
        
    processed_user.to_csv('/tmp/processed_user.csv', index = None, header = False)

#define unique DAG Id, start date, schedule interval, catchup
with DAG('user_processing', start_date = datetime(2022, 1, 1), 
    schedule_interval = "@daily", catchup = False) as dag:
   
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

    #task to identify API is available or not
    is_api_available = HttpSensor(
        task_id = 'is_api_available', 
        http_conn_id = 'user_api,
        endpoint = 'api/')

    #http operator
    extract_user = SimpleHttpOperator(
        task_id = 'extract_user',
        http_conn_id = 'user_api',
        endpoint = 'api/',
        method = 'GET',
        response_filter = lambda response: json.loads(response.text),
        log_response = True
    )

    #Python operator to process user data from the given API
    process_user = PythonOperator(
        task_id = 'process_user',
        python_callable = _process_user
    )
