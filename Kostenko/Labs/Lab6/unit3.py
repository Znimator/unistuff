from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6 import uic

from prettytable import PrettyTable

def chart(x, R):
    if -5 <= x <= -3:
        return 1
    elif -3 < x < -1:
        return - ((R**2 - x**2) ** 0.5)
    elif -1 >= x <= 2:
        return -2
    elif 2 <= x <= 5:
        return -2 + x - 2
    
table = PrettyTable()
table.field_names = ["Arguments", "Names"]

def solve():

    # tableWidget.reset()

    X = int(form.lineEdit.text())
    R = int(form.lineEdit_2.text())

    row = -1

    for x in range(X, 6):
        arg = QTableWidgetItem(x)
        item = QTableWidgetItem(str(chart(x, R)))

        row += 1

        tableWidget.setItem(row, 0, QTableWidgetItem(str(x)))
        tableWidget.setItem(row, 1, QTableWidgetItem(str(chart(x, R))))

        table.add_row([x, chart(x, R)])
    
    print(table)

Form, Window = uic.loadUiType("untitled.ui")
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

# for x in range(-5, 6):
#     table.add_row([x, chart(x, R)])