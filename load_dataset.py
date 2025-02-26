import pandas as pd

def load_dataset():
  df = pd.read_csv("ADIAclasswork/ecommerce.csv", index_col="Unnamed: 0")
  return df
