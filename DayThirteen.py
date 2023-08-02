# Basic Math Limit

def f(x):
    x = float(x)
    return (x**2 -1) / (x-1)

for i in range(0,1):
    i = i - 0.1
    print(f(i))
