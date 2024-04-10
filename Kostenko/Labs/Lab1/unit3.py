from math import sqrt


def h(x, r):
    if x >= -7 and x <= -6: return (x, x + 3)
    elif x >= -2 and x < 4: return (x, (-0.5) * x)
    elif x >= 4 and x <= 6: return (x, -2)
    elif x > 6 and x <= 10: return (x, sqrt(4 - (x-8) ** 2) - 2)
    elif x == -3 or x == 0 or x == 8: return (x, 0)
    else: return (x, None)

xnach = float(input("Введите начальное значение: "))
xkon = float(input("Введите конечное значение: "))
dx = float(input("Введите шаг: "))
r = float(input("Введите радиус: "))
print("Аргумент значение функции")

while xnach <= xkon:
        x, y = h(xnach, r)
        if y != None: print('   {0:2.1f}    {1:2.1f}'.format(x,float(y)))
        else: print('   {0:2}    {1:27}'.format(x, 'Точка не принадлежит графику'))
        xnach += dx