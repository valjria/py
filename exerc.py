text = "The goal is to turn data into information, and information into insight"
text = text.upper()
text_split = text.split(" ")
print(text_split)

lst = ["D","A","T","A","S","C","I","E","N","C","E"]
print(len(lst))
print(lst[0])

data_list=lst[0:4]
print(data_list)

lst.pop(8)
print(lst)

lst.append("O")
print(lst)

lst.insert(8,"N")
print(lst)

dict = {'Christian': ["America", 18],
        'Daisy': ["England",12],
        'Antonio': ["Spain", 22],
        'Dante': ["Italy",25]}

print(dict.keys())
print(dict.values())

dict["Daisy"][1]=14

dict['Ahmet']= "Turkey", 24
print(dict.keys())
print(dict.values())
dict
del dict['Antonio']
print(dict.keys())
print(dict.values())

l=[2,13,18,93,22]
odd_list=[]
even_list=[]
def func(l, odd_list, even_list):


    for i in l:
        if i%2==0:
         odd_list.append[i]
        else:
         even_list.append[i]

        return odd_list, even_list

ogrenciler = ["Ali","Veli","Ayşe","Talat","Zeynep","Ece"]

for count, item in enumerate(ogrenciler):

    if  count <3:
        count += 1
        print("Mühendislik Fakültesi", count,".","öğrenci:",item)
    else:
        count -= 2
        print("Tıp Fakültesi", count,".","öğrenci:",item)


ders_kodu=["CMP1005","PSY1001","HUK1005","SEN2204"]
kredi = [3,4,2,4]
kontenjan = [30,75,150,25]

x=zip(kredi,ders_kodu,kontenjan)
x_list=list(x)
print(x_list)

kume1 = set(["data","python"])
kume2= set(["data","function","qcut","lambda","python","miuul"])

if kume1.issuperset(kume2):
    print(kume1.intersection(kume2))
else:
    print(kume2.difference(kume1))






