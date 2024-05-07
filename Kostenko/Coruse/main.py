import pandas as pd
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
import openpyxl
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("DataBase")
        self.setFixedSize(800, 500)

        self.input = QLineEdit()
        self.sort = QPushButton("Сортировка")

        self.list = QListWidget()
        self.list.setMaximumSize(300, 70)
        self.list.insertItem(1, QListWidgetItem("Авто"))
        self.list.insertItem(1, QListWidgetItem("Водители"))
        self.list.insertItem(1, QListWidgetItem("Рейсы"))

        self.text = QTextEdit()

        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.list)
        layout.addWidget(self.sort)
        layout.addWidget(self.text)
        layout.setAlignment(self.list, Qt.AlignmentFlag.AlignCenter)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)



class Main(QWidget):
    def __init__(self):
        super(Main, self).__init__()
        self.setWindowTitle("Load Excel data to QTableWidget")
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        
        self.table_widget = QTableWidget()
        self.input = QLineEdit()
        self.sort = QPushButton("Сортировка")

        self.list = QListWidget()
        self.list.setMaximumSize(300, 70)
        self.list.insertItem(1, QListWidgetItem("Авто"))
        self.list.insertItem(1, QListWidgetItem("Водители"))
        self.list.insertItem(1, QListWidgetItem("Рейсы"))

        layout.addWidget(self.table_widget)
        layout.addWidget(self.input)
        layout.addWidget(self.list)
        layout.addWidget(self.sort)
        layout.setAlignment(self.list, Qt.AlignmentFlag.AlignCenter)
        
        self.load_data()
        
    def load_data(self):
        path = "./data.xlsx"
        workbook = openpyxl.load_workbook(path)
        sheet = workbook.active
        
        self.table_widget.setRowCount(sheet.max_row)
        self.table_widget.setColumnCount(sheet.max_column)
        
        list_values = list(sheet.values)
        self.table_widget.setHorizontalHeaderLabels(list_values[0])
        
        row_index = 0
        for value_tuple in list_values[1:]:
            col_index = 0
            for value in value_tuple:
                self.table_widget.setItem(row_index , col_index, QTableWidgetItem(str(value)))
                col_index += 1
            row_index += 1
        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Main()
    window.showMaximized()
    app.exec()