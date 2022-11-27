#import the DAG object
from airflow import DAG        
from datetime import datetime

#define unique DAG Id, start date, schedule interval, catchup 
with DAG('user_processing', start_date = datetime(2022, 1, 1), schedule_interval = "@daily", catchup = False) as dag:
    None 
