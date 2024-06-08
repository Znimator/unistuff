from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6 import uic

import math
sqrt = math.sqrt

from prettytable import PrettyTable

def h(x):
    if x >= -math.inf and x < -4: return (x, -3)
    elif x >= -4 and x <= -3: return (x, x + 3)
    elif x >= -3 and x <= 3: return (x, sqrt(3**2 - (x) ** 2))
    elif x > 3 and x <= 8: return (x, x * (3 / 5) - (9 / 5))
    elif x >= 8: return (x, 3)
    else: return (x, None)

def solve():

    # tableWidget.reset()

    X1 = int(form.lineEdit.text())
    X2 = int(form.lineEdit_2.text())

    row = -1

    for x in range(X1, X2 + 1):
        arg = QTableWidgetItem(x)
        item = QTableWidgetItem(str(h(x)))

        row += 1

        tableWidget.setItem(row, 0, QTableWidgetItem(str(x)))
        tableWidget.setItem(row, 1, QTableWidgetItem(str(h(x)[1])))

Form, Window = uic.loadUiType("untitled2.ui")
app = QApplication([])
window :QMainWindow = Window()

form = Form()
form.setupUi(window)

tableWidget :QTableWidget = form.tableWidget
tableWidget.setRowCount(10)
tableWidget.setColumnCount(2)
tableWidget.setHorizontalHeaderLabels(["Аргументы", "Значения"])

form.pushButton.clicked.connect(solve)

window.show()
app.exec()