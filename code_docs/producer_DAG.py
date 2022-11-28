# import dataset
from airflow import DAG, Dataset
from airflow.decorators import task

from datetime import datetime

# define dataset with URI
my_file = Dataset("/tmp/my_file.txt")

# define DAG object
with DAG(
  dag_id = "producer",
  schedule = "@daily",
  start_date = datetime(2022, 1, 1),
  catchup = False
):
  
  # task that updates the dataset with parameter 'outlets'
  @task(outlets = [my_file])
  def update_dataset():
    with open(my_file.uri, "a+") as f:
      f.write("producer update")
      
  update_dataset()
  
  # after running task successfully, DAG that depends on this dataset will get triggered
