from airflow import Dataset

# valid datasets
schemeless = Dataset("/path/file.txt")
csv_file = Dataset("file.csv")

# invalid datasets
reserved = Dataset("airflow://file.txt")
not_ascii = Dataset("file_dataset")

# 'extra' parameter
my_file = Dataset(
"s3://dataset/file.csv",
extra = {'owner':'vignesh'},
)
