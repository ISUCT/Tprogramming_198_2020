import math

def calc(a, b, x):
    y = math.log((b**2 - x**2),a)/(math.fabs(x**2 - a**2)**(1/3))
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
        y = calc(a, b, x)
        res.append((x,y))
    return res


if __name__ == "__main__":
    a = 2.0
    b = 4.1

    res = task_a(a,b,0.77,1.77, 0.2)
    print("-------------Task A -------------")
    print_result(res)

    x_lst = [1.24, 1.38, 2.38, 3.21, 0.68]
    res = task_b(a,b,x_lst)
    print("-------------Task B -------------")
    print_result(res)


