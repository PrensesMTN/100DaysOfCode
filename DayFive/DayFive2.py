import pandas as pd
import matplotlib.pyplot as plt

#import data
df = pd.read_csv('data.csv')

#find meian and replace  to null calories cells
x = df["Calories"].median()

df["Calories"].fillna(x, inplace = True)


#plot to data 
df.plot()

df.plot(kind = 'scatter', x = 'Duration', y = 'Calories')

plt.show()
