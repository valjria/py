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

categoric_cols = [col for col in categoric_cols if col not in categoric_cols]

df[categoric_cols].nunique()

[col for col in df.columns if col not in categoric_cols]

def cat_summary(dataframe, col_name):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts( ) / len(dataframe)}))
    print("###############################################")

cat_summary(df,"sex")

for col in categoric_cols:
    cat_summary(df,col)


def cat_summary(dataframe, col_name, plot=False ):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts( ) / len(dataframe)}))
    print("###############################################")
    if plot:
        sns.countplot(x=dataframe[col_name], data= dataframe)
        plt.show(block = True)

cat_summary(df, "sex", plot=True)

for col in categoric_cols:
    if df[col].dtypes =="bool":
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    else:
        cat_summary(df, col, plot= True)


df["adult_male"].astype(int)


for col in categoric_cols:
    if df[col].dtypes =="bool":
        df[col] = df[col].astype(int)
        cat_summary(df, col, plot=True)
    else:
        cat_summary(df, col, plot= True)

#NUMERICAL VARIABLES ANALYSIS
df = sns.load_dataset("titanic")

categoric_cols = [col for col in df.columns if str(df[col].dtypes) in [ "category", "object","bool"]]
num_but_categoric = [col for col in df.columns if df[col].nunique() < 10 and df[col].dtypes in ["int64","float64"]]
cat_but_car = [col for col in df.columns if df[col].nunique() > 20 and str(df[col].dtypes) in ["category","object"]]
categoric_cols = categoric_cols + num_but_categoric
categoric_cols = [col for col in categoric_cols if col not in cat_but_car]

df[["age","fare"]].describe().T

num_cols = [col for col in df.columns if df[col].dtypes in ["int64", "float64" ]]
num_cols = [col for col in num_cols if col not in categoric_cols]

def num_summary(dataframe, numerical_col):
    quantiles = [0.05, 0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 0.95, 0.99]
    print(dataframe[numerical_col].describe(quantiles).T)

num_summary(df,"age")

for col in num_cols:
    num_summary(df, col)

def num_summary(dataframe, numerical_col, plot=False):
    quantiles = [0.05, 0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 0.95, 0.99]
    print(dataframe[numerical_col].describe(quantiles).T)

    if plot:
        dataframe[numerical_col].hist()
        plt.xlabel(numerical_col)
        plt.title(numerical_col)
        plt.show(block=True)

num_summary(df,"age", plot=True)

for col in num_cols:
    num_summary(df, col, plot=True)

#DEĞİŞKENLERİN YAKALANMASI VE İŞLEMLERİN GENELLEŞTİRİLMESİ


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset("titanic")
df.head()
df.info


def grab_col_names(dataframe, cat_th=10, car_th=20):
    #docstring ekle

    categoric_cols = [col for col in df.columns if str(df[col].dtypes) in ["category", "object", "bool"]]
    num_but_categoric = [col for col in df.columns if df[col].nunique() < 10 and df[col].dtypes in ["int64", "float64"]]
    cat_but_car = [col for col in df.columns if
                   df[col].nunique() > 20 and str(df[col].dtypes) in ["category", "object"]]
    categoric_cols = categoric_cols + num_but_categoric
    categoric_cols = [col for col in categoric_cols if col not in cat_but_car]

    num_cols = [col for col in df.columns if df[col].dtypes in ["int64", "float64"]]
    num_cols = [col for col in num_cols if col not in categoric_cols]

    print(f"Observations:   {dataframe.shape[0]}")
    print(f"Variables:   {dataframe.shape[1]}")
    print(f"categoric_cols:   {len(categoric_cols)}")
    print(f"num_cols:   {len(num_cols)}")
    print(f"cat_but_car:   {len(cat_but_car)}")
    print(f"num_but_categoric:   {len(num_but_categoric)}")

    return categoric_cols, num_cols, cat_but_car


categoric_cols, num_cols, cat_but_car = grab_col_names(df)

def cat_summary(dataframe, col_name, plot = False ):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts( ) / len(dataframe)}))
    print("###############################################")

cat_summary(df, "sex")

def num_summary(dataframe, numerical_col, plot=False):
    quantiles = [0.05, 0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 0.95, 0.99]
    print(dataframe[numerical_col].describe(quantiles).T)

    if plot:
        dataframe[numerical_col].hist()
        plt.xlabel(numerical_col)
        plt.title(numerical_col)
        plt.show(block=True)

for col in num_cols:
    num_summary(df, col, plot=True)

#BONUS
df = sns.load_dataset("titanic")

for col in df.columns:
    if df[col].dtypes == "bool":
        df[col]= df[col].astype("int")

categoric_cols, num_cols, cat_but_car = grab_col_names(df)

def cat_summary(dataframe, col_name, plot = False ):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts( ) / len(dataframe)}))
    print("###############################################")
    if plot:
        sns.countplot(x=dataframe[col_name], data= dataframe)
        plt.show(block = True)

for col in categoric_cols:
    cat_summary(df,col,plot=True)

for col in num_cols:
    num_summary(df, col, plot=True)
