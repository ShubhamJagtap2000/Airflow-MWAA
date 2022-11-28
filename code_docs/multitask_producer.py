# import dataset
from airflow import DAG, Dataset
from airflow.decorators import task

from datetime import datetime

# define dataset with URI
my_file = Dataset("/tmp/my_file.txt")
my_file_2 = Dataset("/tmp/my_file_2.txt")

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
  
  # another task
  @task(outlets = [my_file_2])
  def update_dataset_2():
    with open(my_file_@.uri, "a+") as f:
      f.write("producer update 2")
      
  # task order schedule
  update_dataset() >> update_dataset_2()
  
  # after running task successfully, DAG that depends on this dataset will get triggered
