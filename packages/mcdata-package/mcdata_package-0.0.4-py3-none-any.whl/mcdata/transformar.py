import pandas as pd

def csv_to_parquet(csv_filepath, parquet_filepath):
   df = pd.read_csv(csv_filepath)
   df.to_parquet(parquet_filepath)

from pyarrow import csv, parquet

def rds_to_parquet(rds_filepath, parquet_filepath):
   table = csv.read_csv(rds_filepath)
   parquet.write_table(table, parquet_filepath)
   


