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

# # boolarray1
boolarray = np.full((3,3),True,dtype=bool)
print("boolean array: \n",boolarray)

# # boolarray2
# boolarray2 = np.full((9),True,dtype=bool).reshape(3,3)
# print("boolean array: \n", boolarray2)

# # boolarray3
# boolarray3 = np.ones((3,3), dtype=bool)
# print(boolarray3)

# # boolarray4
# boolarray4 = np.ones((9), dtype=bool).reshape(3,3)
# print(boolarray4)

# # odd numbers = tek sayılar
# numar = numarray[numarray%2 != 0]
# print("\nodd numbers: ", numar)

# #even numbers = çift sayılar
# numar = numarray[numarray%2 == 0]
# print( "\neven numbers: ", numar)

# # How to replace items that satisfy a condition with another value in numpy array?
# numarray[numarray%2 != 0]  = -1
# print("\nodd numbers: ", numarray)

# # How to replace items that satisfy a condition without affecting the original array?
arr = numarray.copy()
print("copy of numarray: ", arr)

arr[arr%2 == 1] = -1
print ("\nreplace even number by -1: " , arr)

# marr[(marr % 5)!=  0 ] *=-1 
# print("\nreplace even number by minus ones: " , marr)