import pandas as pd
import seaborn as sns


s = pd.Series([10,88,12,4,5])
type(s)
s.index
s.dtype
s.size
s.ndim
s.values
type(s.values)
s.head(3)
s.tail(3)

df = pd.read_csv("datasets/Advertising.csv")

df = sns.load_dataset("titanic")
df.head()
df.shape
df.info
df.columns
df.index
df.describe().T
df.isnull().values
df.isnull().values.any()
df.isnull()
df.isnull().sum()
df["sex"].head()
df["sex"].value_counts()

df.index

df.drop(0, axis=0).head()

delete_indexes = [1, 3, 5,7]
df.drop(delete_indexes,axis=0).head(10)


# df.drop(delete_indexes,axis=0, inplace=True)  kalıcı olması için inplace, df=df.drop gibi

df["age"].head()
df.age.head()

df.index = df["age"]

df.drop("age", axis=1, inplace=True)

df.index

df["age"] = df.index #indexi değişkene
df.head()

df = df.reset_index().head()
df.head()

pd.set_option('display.max_columns',None)
    df.head()

"age" in df


df["age"].head()

type(df["age"].head())


df[["age"]].head()
type(df[["age"]].head())

df[["age","alive"]]

col_names = ["age","adult_male","alive"]

df[col_names]

df["age2"] = df["age"]**2
df["age3"] = df["age"] / df["age2"]

df.drop("age3",axis=1).head()

df.drop(col_names, axis=1).head()

column = df.loc[:, df.columns.str.contains("age")]
column.head()
df.drop(column,axis=1).head()

type(column)
aa.head()



