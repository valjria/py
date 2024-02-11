import numpy as np
import seaborn as sns
import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
df= sns.load_dataset("car_crashes")


#1
["NUM_" + col.upper() if df[col].dtype != "O" else col.upper() for col in df.columns ]

#2
[col.upper() + "_FLAG" if "no" not in col else col.upper() for col in df.columns]

#3
og_list = ["abbrev", "no_previous"]
new_cols = [col for col in df.columns if col not in og_list ]
new_df = df[new_cols]

#PANDAS 1
# Görev 1: Seaborn kütüphanesi içerisinden Titanic veri setini tanımlayınız.

df = sns.load_dataset("titanic")

#Görev 2: Titanic veri setindeki kadın ve erkek yolcuların sayısını bulunuz.
df["sex"].value_counts()

#Görev 3: Her bir sutuna ait unique değerlerin sayısını bulunuz.

df.nunique()

#Görev 4: pclass değişkeninin unique değerlerinin sayısını bulunuz.

df["pclass"].nunique()

# Görev 5:  pclass ve parch değişkenlerinin unique değerlerinin sayısını bulunuz.

df[["pclass","parch"]].nunique()

#Görev 6: embarked değişkeninin tipini kontrol ediniz. Tipini category olarak değiştiriniz ve tekrar kontrol ediniz.
df["embarked"].dtype
df["embarked"] = df["embarked"].astype("category")
df["embarked"].dtype

# Görev 7: embarked değeri C olanların tüm bilgilerini gösteriniz.

df[df["embarked"]=="C"].head()

# Görev 8: embarked değeri S olmayanların tüm bilgelerini gösteriniz.

df[df["embarked"]!="S"].head()

df[df["embarked"] != "S"]["embarked"].unique()

df[~(df["embarked"] == "S")]["embarked"].unique()

# Görev 9: Yaşı 30 dan küçük ve kadın olan yolcuların tüm bilgilerini gösteriniz.

df[(df["age"]<30)&(df["sex"] == "female")]

# Görev 10: Fare'i 500'den büyük veya yaşı 70 den büyük yolcuların bilgilerini gösteriniz.


df[(df["fare"] > 500) | (df["age"] > 70)].head

# Görev 11: Her bir değişkendeki boş değerlerin toplamını bulunuz.
df.isnull().sum()

# Görev 12: who değişkenini dataframe'den düşürün.

df.drop("who", axis=1, inplace=True)

# Görev 13: deck değişkenindeki boş değerleri deck değişkenin en çok tekrar eden değeri (mode) ile doldurunuz.

df["deck"]=df["deck"].fillna(df["deck"].mode()[0])
df["deck"].isnull().sum()
#or
df["deck"].fillna(df["deck"].mode()[0], inplace=True)
df["deck"].isnull().sum()

# Görev 14: age değikenindeki boş değerleri age değişkenin medyanı ile doldurun.

df["age"].fillna(df["age"].median(), inplace=True)
df["age"].isnull().sum()

# Görev 15: survived değişkeninin Pclass ve Cinsiyet değişkenleri kırılımınında sum, count, mean değerlerini bulunuz.

df.groupby(["pclass","sex"]).agg({"survived":["sum","count","mean"]})

# Görev 16:  30 yaşın altında olanlar 1, 30'a eşit ve üstünde olanlara 0 vericek bir fonksiyon yazınız.
# Yazdığınız fonksiyonu kullanarak titanik veri setinde age_flag adında bir değişken oluşturunuz.

df["age_flag"] = df["age"].apply (lambda x : 1 if x < 30 else 0 )

# Görev 17: Seaborn kütüphanesi içerisinden Tips veri setini tanımlayınız.

df = sns.load_dataset("tips")
df.head()
df.shape

# Görev 18: Time değişkeninin kategorilerine (Dinner, Lunch) göre total_bill  değerlerinin toplamını, min, max ve ortalamasını bulunuz.

df.groupby(["time"]).agg({"total_bill":["sum","min", "max" ,"mean"]})

# Görev 19: Günlere ve time göre total_bill değerlerinin toplamını, min, max ve ortalamasını bulunuz.

df.groupby(["day","time"]).agg({"total_bill":["sum","min", "max" ,"mean"]})

# Görev 20:Lunch zamanına ve kadın müşterilere ait total_bill ve tip  değerlerinin day'e göre toplamını, min, max ve ortalamasını bulunuz.

df[(df["time"] == "Lunch") & (df["sex"] == "Female")].groupby("day").agg({"total_bill": ["sum","min","max","mean"],
                                                                           "tip":  ["sum","min","max","mean"]})

# Görev 21: size'i 3'ten küçük, total_bill'i 10'dan büyük olan siparişlerin ortalaması nedir?

df.loc[(df["size"] < 3) & (df["total_bill"] >10 ) , "total_bill"].mean() # 17.184965034965035

# Görev 22: total_bill_tip_sum adında yeni bir değişken oluşturun. Her bir müşterinin ödediği totalbill ve tip in toplamını versin.

df["total_bill_tip_sum"] = df["total_bill"] + df["tip"]

# Görev 23: total_bill_tip_sum değişkenine göre büyükten küçüğe sıralayınız ve ilk 30 kişiyi yeni bir dataframe'e atayınız.

sorted_total = df.sort_values("total_bill_tip_sum", ascending = False)[:30]
sorted_total.shape




















