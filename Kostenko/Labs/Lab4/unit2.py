from math import exp, factorial
from prettytable import PrettyTable


def count(func):
    c = 0
    def wrapper(*args, **kwargs):
        nonlocal c
        c += 1
        print(f"Функция вызвана {c} раз")
        return func(*args, **kwargs)
    return wrapper


@count
def f(x, eps, n = 0, s = 0):
    sl = (((-1) ** n) * (x ** n)) / factorial(n)
    if abs(sl) > eps:
        return f(x, eps, n + 1, s + sl)
    else:
        return (s, n - 1)



@count
def fi(x):
    x -= 1
    if x > 10:
        return fi(x)
    elif x < 10:
        x += 3
        return fi(x)
    else:
        print(x)


x0 = int(input("введите х начальное: "))
x1 = int(input("введите х конечное: "))
dx = float(input("введите шаг: "))
eps = float(input("введите погрешность(меньше 1 больше 0): "))
mytable = PrettyTable()
mytable.field_names = ['exp', 'func', 'num', 'x']
while x0 <= x1:
    s, n = f(x0, eps)
    mytable.add_row([exp(-x0), s, n, x0])
    x0 += dx
print(mytable)
fi(6)
