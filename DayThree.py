import numpy as np

Data1 = np.arange(225)
# print up to 225 values with the 'Arange' function.
print(Data1)
# But it's shapeless and not the way we want it to be.


rs=Data1.reshape(15,15)
print("RESHAPE",rs)
#The RESHAPE method allows us to give the data the shape we want and turns it into a matrix.

cs=Data1.cumsum().reshape(15,15)# cumulatively collects
print("cumulatively sum: ",cs)

mins=Data1.min()# returns the smallest value
print("min value: ",mins)

maxs=Data1.max()# returns the largest value
print("max value: ",maxs)

sums=Data1.sum()# sum all value
print("sum:",sums)
