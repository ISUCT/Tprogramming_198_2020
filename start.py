print("Hello world")
print("For new Commit")
import math

def calc(a, b, x):
    y = (math.asin(x**a))+(math.acos(x**b))
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
    a = 2.0
    b = 3.0           

result = task_a(a,b,0.11,0.36,0.05) 
print("-------------Task A-------------")         
print_result(result)

x_lst = [0.08,0.26,0.35,0.41,0.53]
res = task_b(a,b,x_lst)
print("-------------Task B-------------")
print_result(result)
