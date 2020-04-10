import math

def calc(a,b,x):
    y = 1 + math.log10(x/a)**2/(b - math.exp(x/a))
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
    b = 0.95
    
    res = task_a(a,b,1.25,2.75,0.3)
    print("-------------Task A -------------")
    print_result(res)

    x_lst = [2.2, 3.78, 4.51, 6.58, 1.2] 
    res = task_b(a,b,x_lst)
    print("-------------Task B -------------")
    print_result(res)