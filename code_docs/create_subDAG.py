from airflow import DAG
from airflow.operators.bash import BashOperator

def subdag_downloads(parent_dag_id, child_dag_id, args):
  with DAG(f"{parent_dag_id}.{child_dag_id}",
           start_date = args['start_date'],
           schedule_interval = args['schedule_interval'],
           catchup = args['catchup']) as dag:
    
    download_a = BashOperator(
      task_id = 'download_a',
      bash_command = 'sleep 10'
    )
    
    download_b = BashOperator(
      task_id = 'download_b',
      bash_command = 'sleep 10'
    )
    
    download_c = BashOperator(
      task_id = 'download_c',
      bash_command = 'sleep 10'
    )
    
    return dag


```py
# DAG code for above subDAG

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.subdag import SubDagOperator
from datetime import datetime
from subdags.create_subDAG import subdag_downloads

with DAG('group_dag', start_date = datetime(2022, 1, 1),
         schedule_interval = '@daily', catchup = False) as dag:
  
  args = {'start_date' : dag.start_date, 'scheduele_interval' : dag.schedule_interval, 'catchup' : dag.catchup}
  
  downloads = SubDagOperator(
    task_id = 'downloads',
    subdag = subdag_downloads(dag.dag_id, 'downloads', args)
  )
  
  
