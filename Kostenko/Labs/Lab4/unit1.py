from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
import sys
import math

def parabola(x):
    return -x ** 2 + 2

def line(x):
    return x # Потому что 45% линия, значит y = x


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Координаты")
        self.X = QLineEdit()
        self.X.setPlaceholderText("Координата X")
        self.Y = QLineEdit()
        self.Y.setPlaceholderText("Координата Y")

        self.button = QPushButton("Узнать Ответ")

        self.Answer = QLabel("Ответ:")


        layout = QVBoxLayout()
        layout.addWidget(self.X)
        layout.addWidget(self.Y)
        layout.addWidget(self.button)
        layout.addWidget(self.Answer)

        container = QWidget()
        container.setLayout(layout)

        self.button.clicked.connect(self.answerFunc)

        self.setCentralWidget(container)
    
    def answerFunc(self):
        x = int(self.X.text())
        y = int(self.Y.text())

        y1 = parabola(x)
        y2 = line(x)

        if (y <= y1 and y <= y2) or (y <= y1 and y >= y2):
            self.Answer.setText("Внутри")
            print("Внутри")
        else:
            self.Answer.setText("Вне зоны")
            print("Вне Зоны")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec()
