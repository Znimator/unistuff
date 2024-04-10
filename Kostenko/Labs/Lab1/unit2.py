from prettytable import PrettyTable 
from decimal import Decimal 
from math import log 
 
def teilor(x, q): 
    n = 0 
    answer = 0 
    if -1 < x < 1: 
        while True: 
            if n + 1 != 0: 
                a = 2 * ((Decimal(x) ** (2 * n + 1)) / (2 * n + 1)) 
                n += 1 
                answer += a 
            if abs(a) < q: 
                return answer, n - 1 
    return None, None 
 
x = Decimal(input('Введите начало интервала: ')) 
x0 = Decimal(input('Введите конец интервала: ')) 
dx = Decimal(input('задайте шаг интервала: ')) 
q = Decimal(input('задайте точность: ')) 
 
table = PrettyTable() 
table.field_names = ['аргумент', 'значение', 'проверка', 'кол операций '] 
while x <= x0 - dx - dx: 
    x = round(x + dx, len(str(dx))) 
    t, n = teilor(x, q) 
    if t != None: 
        table.add_row([x, t, log((x + 1) / (1 - x)) ,n]) 
print(table)