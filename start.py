import math
a = 4.1
b = 2.7
x = 1.2

def calc(a, b, x):
    y = (a*math.sqrt(x)-b*math.log(5, x))/(math.log(math.fabs(x-1)))
    print(x,y)
calc(a, b, x)