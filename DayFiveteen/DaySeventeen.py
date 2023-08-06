import numpy as np
#print(help(np))

print("numpy version: ",np.__version__)

numarray = np.arange(10)
print("numeric array: ",numarray)

# for i in range(len(numarray)):
#     print(numarray[i])

# print(help(np.full))

# def full (x,y=1):
#     print(x,y)

# full(6)

# argüman   = 6
# parametre = x,y(optionel)
# default   = 1

boolarray = np.full((3,3),True,dtype=bool)
print("boolean array: \n",boolarray)
np.ones((3,3), dtype=bool)


