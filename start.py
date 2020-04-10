print("Hello world")
import math
a = 1.2
b = 0.48
x = 0.7

def calc(a, b, x):
    y = (b**3 + math.sin(a*x)**2)/(math.acos(x*b*x)+math.exp(-x/2))
    return y

def task_a(a,b,xn,xk,dx):
    x = xn
    res = []
    while x <= xk:
        y = calc(a, b, x)
        res.append((x,y))
        x = x + dx
    return res

def print_result(result):    
    for item in result:
        x,y = item
        print(f"x={x} y={y}")

def task_b(a,b,x_lst):
    res = []
    for x in x_lst:
        y = calc(a,b,x)
        res.append((x,y))
    return res 

if __name__ == "__main__": 
     a = 1.2
     b = 0.48   

res = task_a(a<b,0,7,2.2,0.3)
print("---------Task B----------")
print_result(res)

x_lst = [0.25, 0.36, 0.56, 0.94,1.28]

res = task_b(a,b,x_lst)
print("---------Task B----------")
print_result(res)
