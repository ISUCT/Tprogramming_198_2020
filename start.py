import math
a = 4.1
b = 2.7
x = 1.2

def calc(a, b, x):
    y = (a*math.sqrt(x)-b*math.log(5, x))/(math.log(math.fabs(x-1)))
    return y
calc(a, b, x)

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

def task_b(a,b, x_lst):
    res = []
    for x in x_lst:
        y = calc(a, b, x)
        res.append((x,y))
    return res

if _name_ == "_main_":    
    res = task_a(a,b,4.1, 2.7, 1.2)
    print("task A")
    print_result(res)

    x_lst [1.9, 2.15, 2.34, 2.73, 3.16]
    res = task_b(a,b,x_lst)
    print("task B")
    print_result(res)
    а