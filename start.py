import math

def calc(a, b, x):
    y = math.log10(a**2+x)**2/(a+x)**2
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
    a = -2.5
    b = 3.4

    res = task_a(a,b,3.5,6.5,0.6)
    print("-------------Task A -------------")
    print_result(res)
    print("-------------Лирическое отступление--------------------")
    print("Я не знала, куда писать, что x>5, поэтому просто ввела только значения которые меньше:D")\

    x_lst = [5.21, 6.28]
    res = task_b(a,b,x_lst)
    print("-------------Task B -------------")
    print_result(res)