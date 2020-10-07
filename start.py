print("Hello world!")
print("Hello world")
import math
a = 2.5
b = 4.6
x = 1.1

def calc(a, b, x):
    y = ((a+b*x)**2.5)/(1+math.log(a+b*x))
    return y

def task_a(a,b,xn,xk,dx):
    x=xn
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
        y = calc(a, b, x)
        res.append((x,y))
    return res

if __name__ == "__main__":
    a = 0.8
    b = 0.4

    res  = task_a(a,b,1.1,3.6,0.5)
    print_result(res)

    x_lst = [1.2, 1.28, 1.36, 1.46, 2.35]
    res = task_b(a,b,x_lst)
