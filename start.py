print("Hello world")
import math
a = 0.8
b = 0.4
x = 1.23

def calc(a, b, x):
    y = (((x-a)**2)**(1/3)) + (math.fabs(x+b))**(1/5)/((x**2-(a+b)**2)**(1/9))
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

    res  = task_a(a,b,1.23,7.23,1.2)
    print_result(res)

    x_lst = [1.88, 2.26, 3.84, 4.55, -6.21]
    res = task_b(a,b,x_lst)

 