# producer DAG will update the dataset that will trigger consumer DAG 

# import dataset object
from airflow import Dataset
from airflow.decorators import task

from datetime import datetime

# use same daatset as the producer DAG
my_file = Dataset("/tmp/my_file.txt")

# use the same daatset as 'schedule' to your consumer DAG
with DAG(
  dag_id = "consumer",
  schedule = [my_file],
  start_date = datetime(2022, 1, 1),
  catchup = False
):
  
  # no outlets as the task doesn't update the dataset
  @task
  def read_dataset():
    with open(my_file.uri, "r") as f:
      print(f.read())
      
  read_dataset()
