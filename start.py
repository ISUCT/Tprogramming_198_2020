print("Hello world")
import math
a = 0.05
b = 0.06
x = 0.2

def calc(a, b, x):
    y = math.acos(x**2 - b**2)/(math.asin(x**2 - a**2))
    return y

    
def task_a(a,b,xn,xk,dx):
    x = xn
    res = []
    while x <= xk:
        y = calc(a, b, x)
        res.append((x,y))
        x = x + dx
    return res

result = task_a(a,b,0.2,0.95, 0.15)
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
    a = 0.05
    b = 0.06

    res = task_a(a,b,0.2,0.95, 0.15)
    print("-------------Task A -------------")
    print_result(res)

    x_lst = [0.15, 0.26, 0.37, 0.48, 0.56]
    res = task_b(a,b,x_lst)
    print("-------------Task B -------------")
    print_result(res)