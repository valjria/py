#############################################
# Kural Tabanlı Sınıflandırma ile Potansiyel Müşteri Getirisi Hesaplama
#############################################

#############################################
# İş Problemi
#############################################
# Gezinomi yaptığı satışların bazı özelliklerini kullanarak seviye tabanlı (level based) yeni satış tanımları
# oluşturmak ve bu yeni satış tanımlarına göre segmentler oluşturup bu segmentlere göre yeni gelebilecek müşterilerin şirkete
# ortalama ne kadar kazandırabileceğini tahmin etmek istemektedir.
# Örneğin: Antalya’dan Herşey Dahil bir otele yoğun bir dönemde gitmek isteyen bir müşterinin ortalama ne kadar kazandırabileceği belirlenmek isteniyor.
#############################################
# PROJE GÖREVLERİ

 #GÖREV 1: Aşağıdaki soruları yanıtlayınız.
#############################################

# Soru 1: miuul_gezinomi.xlsx dosyasını okutunuz ve veri seti ile ilgili genel bilgileri gösteriniz.

import pandas as pd
pd.set_option("display.max_rows", 100)
pd.set_option("display.max_columns", None)

df = pd.read_excel('datasets/miuul_gezinomi.xlsx')
df.head()
df.shape
df.columns

# Soru 2: Kaç unique şehir vardır? Frekansları nedir?

df["SaleCityName"].nunique()
df["SaleCityName"].value_counts()

# Soru 3: Kaç unique Concept vardır?

df["ConceptName"].nunique()

#Soru4: Hangi Concept’den kaçar tane satış gerçekleşmiş?
df["ConceptName"].value_counts()

#Soru5: Şehirlere göre satışlardan toplam ne kadar kazanılmış?
df.groupby("SaleCityName").agg({"Price": "sum"})

#Soru6: Concept türlerine göre göre ne kadar kazanılmış?
df.groupby("ConceptName").agg({"Price":"sum"})

#Soru7: Şehirlere göre PRICE ortalamaları nedir?
df.groupby("SaleCityName").agg({"Price": "mean"})
df.groupby(by=['SaleCityName']).agg({"Price": "mean"})

#Soru 8: Conceptlere göre PRICE ortalamaları nedir?
df.groupby("ConceptName").agg({"Price":"mean"})

#Soru 9: Şehir-Concept kırılımında PRICE ortalamalarınedir?
df.groupby(["SaleCityName","ConceptName"]).agg({"Price": ["mean"]})

# GÖREV 2: Sale_checkin_day_diff değişkenini EB_Score adında yeni bir kategorik değişkene çeviriniz.

df["EB_Score"] = pd.cut(x = df["SaleCheckInDayDiff"], bins=[0,7,30,90, df["SaleCheckInDayDiff"].max()],labels=['Last Minuters',"Potential Planners", "Planners","Early Bookers"])

df["EB_Score"]

# GÖREV 3: Şehir,Concept, [EB_Score,Sezon,CInday] kırılımında ücret ortalamalarına ve frekanslarına bakınız

# Şehir-Concept-EB Score kırılımında ücret ortalamaları
df.groupby(by=["SaleCityName", 'ConceptName', "EB_Score" ]).agg({"Price": ["mean", "count"]})

# Şehir-Concept-Sezon kırılımında ücret ortalamaları
df.groupby(by=["SaleCityName", "ConceptName", "Seasons"]).agg({"Price": ["mean", "count"]})

# Şehir-Concept-CInday kırılımında ücret ortalamaları
df.groupby(by=["SaleCityName", "ConceptName", "CInDay"]).agg({"Price": ["mean", "count"]})

# GÖREV 4: City-Concept-Season kırılımın çıktısını PRICE'a göre sıralayınız.
#############################################
# Önceki sorudaki çıktıyı daha iyi görebilmek için sort_values metodunu azalan olacak şekilde PRICE'a uygulayınız.
# Çıktıyı agg_df olarak kaydediniz.

agg_df = df.groupby(by=["SaleCityName", "ConceptName", "Seasons"]).agg({"Price":"mean"}).sort_values("Price",ascending=False)

# GÖREV 5: Indekste yer alan isimleri değişken ismine çeviriniz.
#############################################
# Üçüncü sorunun çıktısında yer alan PRICE dışındaki tüm değişkenler index isimleridir.
# Bu isimleri değişken isimlerine çeviriniz.
# İpucu: reset_index()



























