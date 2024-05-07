def password(func):
    flag = 0
    def check(x):
        nonlocal flag
        if flag == 0:
            if input("Введите пароль: ") != "admin":
                print("Неправильный пароль!")
                return check(x)
            else:
                flag = 1
                return func(x)
        else:
            return func(x)
    return check

def parabola(x):
    return -x ** 2 + 2

def line(x):
    return x # Потому что 45% линия, значит y = x

@password
def test(x, y):
    y1 = parabola(x)
    y2 = line(x)

    if (Y <= y1 and Y <= y2) or (Y <= y1 and Y >= y2):
        print("Внутри")
    else:
        print("Вне Зоны")

n = int(input("Введите кол-во координат: "))
for i in range(n):
    print("Координата точки:")
    X = float(input("X: "))
    Y = float(input("Y: "))

    test(X, Y)