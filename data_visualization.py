import numpy as np

#kategorik değişken: sütun grafik. countplot bar
#sayısal değişken: hist, boxplot

#kategorik değişken görselleştirme
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset("titanic")
df.head()

df["sex"].value_counts().plot(kind="bar")
plt.show()

#sayısal değişken görselleştirme

plt.hist(df["age"])

plt.boxplot(df["fare"])
plt.show()

#matplot plot özelliği

x = np.array([1,8])
y = np.array([0,150])
plt.plot(x,y)

plt.plot(x,y,'o')

x = np.array([2,4,6,8,10])
y = np.array([1,3,5,7,9])

plt.plot(x,y)
plt.plot(x,y,'o')

#marker

y = np.array([13,28,11,100])

plt.plot(y, marker = 'o')
plt.show()

#line
y = np.array([13,28,11,100])
plt.plot(y,linestyle="dashed",color = "purple")

#multiple lines
x = np.array([2,4,6,8,10])
y = np.array([1,3,5,7,9])
plt.plot(x)
plt.plot(y)
plt.show()

#labels

x = np.array([80,85,90,95])
y = np.array([250,250,260,270])
plt.plot(x,y)
plt.title("ana başlık")

plt.xlabel("x başlık")
plt.ylabel("y başlık")

plt.grid()

#subplots

x = np.array([80,85,90,95])
y = np.array([250,250,260,270])
plt.subplot(1,2,1) #1'e 2lik grafik, 1.eleman
plt.title("1")
plt.plot(x,y)



x = np.array([80,85,90,95])
y = np.array([250,250,260,270])
plt.subplot(1,2,2)
plt.title("2")
plt.plot(x,y)

df = sns.load_dataset("tips")

df["sex"].value_counts()
sns.countplot(x=df["sex"],data = df)


sns.boxplot(x=df["total_bill"])

df["total_bill"].hist()







