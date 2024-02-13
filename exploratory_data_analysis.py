import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset("titanic")
df.head()
df.shape
df.info()
df.columns
df.describe()
df.isnull().values.any()
df.isnull().sum()

def check_df(dataframe, head = 5 ):
    print("############ SHAPE ##########")
    print(dataframe.shape)
    print("############ TYPES ##########")
    print(dataframe.dtypes)
    print("############ HEAD ##########")
    print(dataframe.head(head))
    print("############ TAIL ##########")
    print(dataframe.tail(head))
    print("############ NA ##########")
    print(dataframe.isnull().sum())
    print("############ QUANTILES ##########")
    print(dataframe.describe([0,0.05,0.50,0.95]))
check_df(df)

df = sns.load_dataset("tips")
check_df(df)

categoric_cols = [col for col in df.columns if str(df[col].dtypes) in [ "category", "object","bool"]]


num_but_categoric = [col for col in df.columns if df[col].nunique() < 10 and df[col].dtypes in ["int64","float64"]]

cat_but_car = [col for col in df.columns if df[col].nunique() > 20 and str(df[col].dtypes) in ["category","object"]]

categoric_cols = categoric_cols + num_but_categoric

categoric_cols = [col for col in categoric_cols if col not in categoric_cols_cols]

df[categoric_cols].nunique()

[col for col in df.columns if col not in categoric_cols]

def cat_summary(dataframe, col_name):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts( ) / len(dataframe)}))
    print("###############################################")

cat_summary(df,"sex")

for col in categoric_cols:
    cat_summary(df,col)
