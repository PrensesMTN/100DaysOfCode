import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data = pd.read_csv("iris.csv")

print(data.head())                      # data setinin ilk 5 datasını gösterir
#print(data.tail())                       # data setinin son 5 datasını gösterir
print(data.isnull().sum())            # csv içerinde boş (null) data olup olmadığı kontrol et ve varsa kaç adet olduğu topla

data.rename(columns={'SepalLengthCm':'Sepal_length_cm',
                   'SepalWidthCm':'Sepal_width_cm',
                   'PetalLengthCm':'Petal_length_cm',
                   'PetalWidthCm':'Petal_width_cm',},inplace=True)

print(data.head(7))                     # data setinin ilk parantez içerisi kadar datasını gösterir


s= data['Species'].unique()         # datanın "Species" kolonunun kaç farklı değere sahip olduğunu listele

for sp in s:
   print("Species : ",sp)               # listelenen veriyi yazdır


Iris_setosa = data[data["Species"] == 'Iris-setosa'].value_counts().sum()           # datanın "Species" kolonunda kaç tane Iris-setosa olduğunu say
print("How many Iris-setosa value we have: ",Iris_setosa)

#print(data[data ["Species"]=='Iris-setosa'])                                                          # bütün Iris-setosa verileirni yazdır

Iris_versicolor = data[data["Species"] == 'Iris-versicolor'].value_counts().sum()           # datanın "Species" kolonunda kaç tane Iris-versicolor olduğunu say
print("How many Iris-versicolor value we have: ",Iris_versicolor)

#print(data[data ["Species"]=='Iris-versicolor'])                                                          # bütün Iris-setosa verileirni yazdır

Iris_virginica = data[data["Species"] == 'Iris-virginica'].value_counts().sum()           # datanın "Species" kolonunda kaç tane Iris-virginica olduğunu say
print("How many Iris-virginica value we have: ",Iris_virginica)

#print(data[data ["Species"]=='Iris-virginica'])                                                          # bütün Iris-setosa verileirni yazdır

colm = data.columns                    # kaç tane sütün olduğu bul

for col in colm:
   print("--",col)                              # slünları yazdır



"################ DATA GÖRSELLEŞTİRME ################"


sns.pairplot(data,hue='Species', diag_kind='hist')   


plt.show()

sns.violinplot(x = 'Species', y='Petal_length_cm', data=data)
plt.title("petal length by species")
plt.show()

sns.swarmplot(x = 'Species', y='Petal_width_cm', data=data)
plt.title("petal width by species")
plt.show()

plt.figure(figsize=(16,7))
x = plt.xticks(rotation=90)
sns.kdeplot(data=data ,x="Sepal_length_cm", hue='Species', shade=True)
plt.show()

