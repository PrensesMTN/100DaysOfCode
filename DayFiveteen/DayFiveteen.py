import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data = pd.read_csv("iris.csv")

print(data.head())                      # data setinin ilk 5 datasını gösterir
#print(data.tail())                       # data setinin son 5 datasını gösterir
print(data.isnull().sum())            # csv içerinde boş (null) data olup olmadığı kontrol et ve varsa kaç adet olduğu topla

data.rename(columns={'SepalLengthCm':'Sepal_lengt_cm',
                   'SepalWidthCm':'Sepal_width_cm',
                   'PetalLengthCm':'Petal_length_cm',
                   'PetalWidthCm':'Petal_width_cm',},inplace=True)

print(data.head(7))                     # data setinin ilk parantez içerisi kadar datasını gösterir


s= data['Species'].unique()         # datanın "Species" kolonunun kaç farklı değere sahip olduğunu listele

for sp in s:
   print("Species : ",sp)               # listelenen veriyi yazdır


Iris_setosa = data[data["Species"] == 'Iris-setosa'].value_counts().sum()           # datanın "Species" kolonunda kaç tane Iris-setosa olduğunu say
print("How many Iris-setosa value we have: ",Iris_setosa)

print(data[data ["Species"]=='Iris-setosa'])
