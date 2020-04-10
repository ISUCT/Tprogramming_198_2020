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

result = task_a(a, b, 3.2, 6.2, 0.6)
print_result(result)
