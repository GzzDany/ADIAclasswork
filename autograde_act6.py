import pandas as pd

def load_dataset():
  # URL to the dataset (Example: January 2024 Yellow Taxi Data in Parquet format)
  url = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2024-01.parquet"

  # Read the dataset directly into a Pandas DataFrame
  df = pd.read_parquet(url)
  df_clean = df.dropna()
  df_clean = df_clean[df_clean["passenger_count"]>0]
  df_clean = df_clean[df_clean["trip_distance"]>0]
  df_clean = df_clean[df_clean["fare_amount"]>0]
  df_clean = df_clean[df_clean["tip_amount"]>=0]
  df_clean = df_clean[df_clean["total_amount"]>0]

  
  return df_clean
def categorize_length_sol(length):
  if length > 5:
    return "long"
  else:
    return "short"

def categorize_time_of_day_sol(hour):
  if hour < 6:
    return "late night"
  elif hour < 12:
    return "morning"
  elif hour < 21:
    return "afternoon"
  else:
    return "night"
    

def make_solution():
  df_sol = load_dataset()
  df_sol["trip_distance_km"] = df_sol["trip_distance"]* 1.60934
  df_sol["tip_percentage"] = (df_sol["tip_amount"]/df_sol["fare_amount"])*100
  df_sol["trip_duration"] = (df_sol["tpep_dropoff_datetime"] - df_sol["tpep_pickup_datetime"]).dt.total_seconds()/60
  df_sol["hour_start"] = df_sol["tpep_pickup_datetime"].dt.hour
  df_sol["weekday"] = df_sol["tpep_pickup_datetime"].dt.day_name()
  df_sol["average_speed"] = df_sol["trip_distance_km"]/(df_sol["trip_duration"]/60)
  df_sol["length_category"] = df_sol["trip_distance_km"].apply(categorize_length_sol)
  df_sol["time_of_day"] = df_sol["hour_start"].apply(categorize_time_of_day_sol)
  df_sol.reset_index(drop=True, inplace=True)
  return df_sol


df_sol = make_solution()

def grade_p1(globals):
  if "df" not in globals:
    print("Error. Did you load the DataFrame into a variable called 'df'?")
    return
  else:
    df = globals["df"]
  if df.equals(df_sol):
    print("Great!")
  else:
    print("Error. You did not correctly load the dataframe. Make sure you make no modifications to it!")
