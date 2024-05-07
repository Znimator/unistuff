import math
sqrt = math.sqrt


def h(x):
    if x >= -math.inf and x < -4: return (x, -3)
    elif x >= -4 and x <= -3: return (x, x + 3)
    elif x >= -3 and x <= 3: return (x, sqrt(3**2 - (x) ** 2))
    elif x > 3 and x <= 8: return (x, x * (3 / 5) - (9 / 5))
    elif x >= 8: return (x, 3)
    else: return (x, None)

xnach = float(input("Введите начальное значение: "))
xkon = float(input("Введите конечное значение: "))
dx = float(input("Введите шаг: "))
print("Аргумент значение функции")

while xnach <= xkon:
        x, y = h(xnach)
        if y != None: print('   {0:2.1f}    {1:2.1f}'.format(x,float(y)))
        else: print('   {0:2}    {1:27}'.format(x, 'Точка не принадлежит графику'))
        xnach += dx