def circle(x, y, radius):
    if (y <= 0 and x <= 0 or y >= 0 and x >= 0) and (x * 2 + y * 2 ) ** 0.5 <= radius:
        return 'YES'
    else:
        if y <= abs(x) and abs(x) <= radius and abs(y) <= radius and x < 0:
            return 'В области'
        return 'Вне области'


r = float(input('radius= '))

for i in range(int(input('количество точек'))):
    print(circle(float(input('x= ')), float(input('y= ')), r))