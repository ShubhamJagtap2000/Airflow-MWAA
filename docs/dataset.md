# Dataset 

A dataset is like logical grouping of data

A dataset has 2 properties:

1. URI - It is like the path tot he data
2. EXTRA - JSON dictionary that you can define to attach additional information to your dataset

URI is Unique Identifier of your data, so that Airflow knows uniqueness of your data

URI is must composed of ASCII characters, case sensitive

```py
from airflow import Dataset

# valid datasets
schemeless = Dataset("/path/file.txt")
csv_file = Dataset("file.csv")

# invalid datasets
reserved = Dataset("airflow://file.txt")
not_ascii = Dataset("file_dataset")
```
With EXTRA parameter you can describe JSON dictionary for more info about the datasaet

```py
from airflow import Dataset

my_file = Dataset(
"s3://dataset/file.csv",
extra = {'owner':'vignesh'},
)
```
