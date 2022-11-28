# producer DAG will update the dataset that will trigger consumer DAG 

# import dataset object
from airflow import Dataset
from airflow.decorators import task

from datetime import datetime

# use same dataset as the producer DAG
my_file = Dataset("/tmp/my_file.txt")
my_file_2 = Dataset("/tmp/my_file_2.txt")

# use the same dataset as 'schedule' to your consumer DAG, add files in list
with DAG(
  dag_id = "consumer",
  schedule = [my_file, my_file_2],
  start_date = datetime(2022, 1, 1),
  catchup = False
):
  
  # no outlets as the task doesn't update the dataset
  @task
  def read_dataset():
    with open(my_file.uri, "r") as f:
      print(f.read())
  
  def read_dataset():
    with open(my_file_2.uri, "r") as f:
      print(f.read())
      
  read_dataset()
