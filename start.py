print("Hello word!")
import math
a = 0.4
b = 0.8
x = 3.2

def calc(a, b, x):
    y = ((a**b-b**x)/(math.log1p(a/b)))*((a*b))**(1/3)
    return y

def task_a(a, b, xn, xk, dx):
    x = xn
    res = []
    while x <= xk:
        y = calc(a, b, x)
        res.append((x,y))
        x = x + dx
    return res

def print_result(result):
    for item in result:
        x, y = item
        print(f"x={x} y={y}")

def task_b(a, b, x_lst):
    res = []
    for x in x_lst:
        y = calc(a, b, x)
        res.append((x, y))
    return res


if __name__ == "__main__":
    a = 0.4
    b = 0.8

    res = task_a(a, b, 0.77, 1.77, 0.2)
    print("-------------Task A -------------")
    print_result(res)

    x_lst = [4.48, 3.56, 2.78, 5.28, 3.21]
    res = task_b(a,b,x_lst)
    print("-------------Task B -------------")

    print_result(res)
