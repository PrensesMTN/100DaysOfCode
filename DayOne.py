import time

a="100 Days Of Code"
b="#100DaysOfCode"
print( "100 Days Of Code Day 1")

aint=len(a)
for i in a:
    print("*", end="")

print(" ")

for i in range(0,aint):
    for j in range(0,i+1):
        time.sleep(0.13)
        print(a[j], end="")

    print("\r")    
 

print("\r",b)    

for i in a:
    print("*", end="")