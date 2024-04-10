def parabola(x):
    return -x ** 2 + 2

def line(x):
    return x # Потому что 45% линия, значит y = x

while True:
    print("Координата точки:")
    x = float(input("X: "))
    Y = float(input("Y: "))

    y1 = parabola(x)
    y2 = line(x)

    if (Y <= y1 and Y <= y2) or (Y <= y1 and Y >= y2):
        print("Внутри")
    else:
        print("Вне Зоны")