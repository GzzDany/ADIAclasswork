import pandas as pd 

def load_orders():
  df1 = pd.read_csv("ADIAclasswork/orders1.csv", index="Unnamed 0: ")
  df2 = pd.read_csv("ADIAclasswork/orders2.csv", index="Unnamed 0: ")
  return df1, df2

def load_customers():
  df1 = pd.read_csv("ADIAclasswork/customers1.csv", index="Unnamed 0: ")
  df2 = pd.read_csv("ADIAclasswork/customers2.csv", index="Unnamed 0: ")
  return df1, df2

def load_producst():
  df = pd.read_csv("ADIAclasswork/olist_products_dataset.csv", index="Unnamed 0: ")
  return df

def load_reviews():
  df = pd.read_csv("ADIAclasswork/olist_order_reviews_dataset.csv", index="Unnamed 0: ")
  return df

def load_order_items():
  df = pd.read_csv("ADIAclasswork/olist_oder_items_dataset.csv", index="Unnamed 0: ")
  return df


  
