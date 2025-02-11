import pandas as pd

def load_dataset():
  # URL to the dataset (Example: January 2024 Yellow Taxi Data in Parquet format)
  url = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2024-01.parquet"

  # Read the dataset directly into a Pandas DataFrame
  df = pd.read_parquet(url).astype(str)
  return df

def grade_p1(gobals):
  if "columns_float" not in globals:
    print("Error, the variable columns_float is not defined.")
    return
  if "columns_datetime" not in globals:
    print("Error, the variable columns_datetime is not defined.")
    return

  passed = True
  columns_float = globals["columns_float"]
  columns_datetime = globals["columns_datetime"]
  ### check the float columns:
  columns_float_ans = ["passenger_count", "trip_distance", "RatecodeID", "fare_amount", "extra", "mta_tax", "tip_amount", "tolls_amount", "improvement_surcharge", "total_amount", "congestion_surcharge", "Airport_fee"]
  columns_datetime_ans = ["tpep_pickup_datetime", "tpep_dropoff_datetime"]

  for col in columns_float_ans:
    if col not in columns_float:
      print(f"Your forgot to add {col} to your columns_float list!")
      passed = False
  for col in columns_datetime_ans:
    if col not in columns_datetime:
      prin(f"You forgot to add {col} to your columns_datetime list!")
      passed = False
  if passed:
    print("Great job! Now you can move on to the next part.")
