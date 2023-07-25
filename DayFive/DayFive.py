import pandas as pd
 
# list of strings
lst = ['Prenses', 'Metin', 'is', 'my', 
            'name', 'and', 'workin','on','pandas']
 
# Calling DataFrame constructor on list
df = pd.DataFrame(lst)
print(df)

print(" \n ")

################################################
data = {'Name':['Tom', 'nick', 'krish', 'jack'],
        'Age':[20, 21, 19, 18]}
 
# Create DataFrame
df = pd.DataFrame(data)
 
# Print the output.
print(df)
print(" \n ")

################################################
import numpy as np
 
# dictionary of lists
dict = {'First Score':[100, 90, np.nan, 95],
        'Second Score': [30, 45, 56, np.nan],
        'Third Score':[np.nan, 40, 80, 98]}
 
# creating a dataframe from list
df = pd.DataFrame(dict)
 
# using isnull() function  
df.isnull()
print(df)