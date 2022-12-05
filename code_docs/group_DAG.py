from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG('group_dag', start_date = datetime(2022, 1, 1),
         schedule_interval = '@daily', catchup = False) as dag:
  
  download_a = BashOperator(
    task_id = 'download_a',
    bash_command = 'sleep 10'
  )
  
  download_b= BashOperator(
    task_id = 'download_b,
    bash_command = 'sleep 10'
  )
  
  download_c = BashOperator(
    task_id = 'download_c',
    bash_command = 'sleep 10'
  )
  
  check_files = BashOperator(
    task_id = 'check_files',
    bash_command = 'sleep 10'
  )
  
  transform_a = BashOperator(
    task_id = 'transform_a',
    bash_command = 'sleep 10'
  )
  
  transform_b = BashOperator(
    task_id = 'transform_b',
    bash_command = 'sleep 10'
  )
  
  transform_c = BashOperator(
    task_id = 'transform_c',
    bash_command = 'sleep 10'
  )
  
  [download_a, download_b, download_c] >> check_files >> [transform_a, transform_b, transform_c]
