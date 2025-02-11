import pandas as pd

def load_dataset():
  # URL to the dataset (Example: January 2024 Yellow Taxi Data in Parquet format)
  url = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2024-01.parquet"

  # Read the dataset directly into a Pandas DataFrame
  df = pd.read_parquet(url).astype(str)
  return df

def grade_p1(globals):
  if "columns_float" not in globals:
    print("Error, the variable columns_float is not defined.")
    return
  columns_float = globals["columns_float"]
  if type(columns_float) != list:
    print("You should store a list in columns_float, defined using square brackets [] and separating items with commas.")
  passed = True
  columns_float_ans = ["passenger_count", "trip_distance", "RatecodeID", "fare_amount", "extra", "mta_tax", "tip_amount", "tolls_amount", "improvement_surcharge", "total_amount", "congestion_surcharge", "Airport_fee"]
  for col in columns_float_ans:
    if col not in columns_float:
      print(f"You forgot to include {col} in columns_float. ")
      passed = False

  if "columns_datetime" not in globals:
    print("Error, the variable columns_datetime is not defined.")
    return
  columns_datetime = globals["columns_datetime"]
  if type(columns_datetime) != list:
    print("You should store a list in columns_datetime, defined using square brackets [] and separating items with commas.")
  passed = True
  columns_datetime_ans = ["tpep_pickup_datetime", "tpep_dropoff_datetime"]
  for col in columns_datetime_ans:
    if col not in columns_datetime:
      print(f"You forgot to include {col} in columns_float. ")
      passed = False

  if passed:
    print("Well done! Now you can move on to the next section.")
  else:
    print("You should fix your code until you pass this section, because this will be required in the next part!")



