import os

f = open("Kostenko\Labs\Lab2\data.csv", "r")
lines = f.readlines()

plrs = []
info = {}

for index in range(len(lines)):
    line = lines[index].split(";")
    if index == 0:
        for index in range(len(line)):
            info[line[index]] = index
        print(info)
    else:
        print(lines[index].split(";"))

        player = {}

        for key, value in info.items():
            player[key.strip()] = line[value].strip()
        plrs.append(player)

for plr in plrs:
    print(plr)

def sortCriteria(criteria):
    print(criteria)
    tempList = plrs.copy()
    tempList.sort(key=lambda plr: plr[criteria], reverse=True)
    for plr in tempList:
        print(plr)

def showMin(criteria):
    m = 9999
    toShow = 0
    for plr in plrs:
        attr = plr[criteria]
        if int(attr) < m:
            m = int(attr)
            toShow = plr
    print(toShow)

def showMax(criteria):
    m = 0
    toShow = 0
    for plr in plrs:
        attr = plr[criteria]
        if int(attr) > m:
            m = int(attr)
            toShow = plr
    print(toShow)

def showResult(**kargs):
    if kargs["command"] == "min":
        showMin(kargs["criteria"])
    elif kargs["command"] == "max":
        showMax(kargs["criteria"])
    elif kargs["command"] == "sort":
        sortCriteria(kargs["criteria"])
    else:
        print("Команды не существует или введена неверно, help - для списка команд")

while True:
    answr = input("Введите команду: ")
    if answr == "help":
        print("""Список команд:
        min:КРИТЕРИЙ - вывод по минимальному критерию
        max:КРИТЕРИЙ - вывод по максимальному критерию
        sort:КРИТЕРИЙ - сортировка списка по критерию
        """)
    elif answr == "exit":
        break
    else:
        cmd = answr.split(':')[0]
        crit = answr.split(':')[1]
        showResult(command=cmd, criteria=crit)

f.close()