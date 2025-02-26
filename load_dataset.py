import pandas as pd

def load_dataset():
  df = pd.read_csv("ADIAclasswork/ecommerce.csv")
  return df
