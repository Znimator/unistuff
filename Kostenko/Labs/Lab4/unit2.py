from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
import sys
import math


questions = [
    {"Question": "Можете ли Вы жить в казенной неуютной квартире и не замечать этого?", "YesPoints": 1, "NoPoints": 2},
    {"Question": "Одеваясь, Вы скорее опираетесь не на моду, а на собственный вкус?", "YesPoints": 2, "NoPoints": 1},
    {"Question": "У Вас хороший почерк?", "YesPoints": 2, "NoPoints": 1},
    {"Question": "Когда Вы очень спешите, может ли Вас заставить остановиться редкой красоты закат?", "YesPoints": 2, "NoPoints": 1},
    {"Question": "Любите ли Вы чертить геометрические фигуры?", "YesPoints": 1, "NoPoints": 2},
    {"Question": "Любите ли бесцельно бродить по улицам?", "YesPoints": 2, "NoPoints": 1},
    {"Question": "Бывает ли, что Вы чувствуете неловкость, когда кто-то начинает декламировать стихи?", "YesPoints": 1, "NoPoints": 2},
    {"Question": "Считаете ли Вы, что красивый пейзаж лучше запомнить, чем сфотографировать?", "YesPoints": 2, "NoPoints": 1},
    {"Question": "Любите ли Вы новые встречи и знакомства?", "YesPoints": 1, "NoPoints": 2},
    {"Question": "Возникало ли у Вас когда-нибудь желание разрисовать стены в квартире?", "YesPoints": 2, "NoPoints": 1},
    {"Question": "Пробовали ли Вы когда-нибудь писать стихи?", "YesPoints": 2, "NoPoints": 1},
    {"Question": "Часто ли у Вас возникает желание переставить мебель в квартире?", "YesPoints": 2, "NoPoints": 1},
]

def clamp(n, min, max):
    if n < min: 
        return min
    elif n > max: 
        return max
    else: 
        return n 

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Вопросы")
        self.currentQuestion = 1
        self.points = 0

        self.yes = QPushButton("Да")
        self.no = QPushButton("Нет")

        self.questionNum = QLabel()
        self.label = QLabel()

        self.questionNum.setText("Вопрос " + str(self.currentQuestion))
        self.label.setText(questions[self.currentQuestion - 1]["Question"])


        layout = QVBoxLayout()
        layout.addWidget(self.questionNum)
        layout.addWidget(self.label)
        layout.addWidget(self.yes)
        layout.addWidget(self.no)
        layout.setAlignment(self.label, Qt.AlignmentFlag.AlignCenter)
        layout.setAlignment(self.questionNum, Qt.AlignmentFlag.AlignCenter)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

        self.yes.clicked.connect(self.answerYes)
        self.no.clicked.connect(self.answerNo)

    def changeAnswer(self):
        if self.currentQuestion > len(questions):
            self.questionNum.setText("Очков: " + str(self.points))
            if 16 < self.points < 24:
                self.label.setText("Вы, несомненно, человек возвышенный. У Вас хорошо развито чувство прекрасного, Вы артистичны и умеете «парить» над мелочностью жизни")
            elif 8 < self.points < 16:
                self.label.setText("Иногда Вы любите витать в облаках. Но хотя Вы и не возвышенный человек, а скорее рационалист, чувство прекрасного Вам не чуждо. Вы отлично умеете сочетать приятное с полезным")
            elif 0 < self.points < 8:
                self.label.setText("Да, такого человека, как Вы, трудно сбить с намеченной цели всякими восходами и закатами. Гармония для Вас – лишь ненужные сантименты. Эх, наверно, Вы никогда не любили!")

            self.yes.close()
            self.no.close()
            return
        
        self.questionNum.setText("Вопрос " + str(self.currentQuestion))
        self.label.setText(questions[self.currentQuestion - 1]["Question"])

    def answerYes(self):
        self.points += questions[self.currentQuestion - 1]["YesPoints"]
        self.currentQuestion += 1

        self.changeAnswer()

        print(self.points)

    def answerNo(self):
        self.points += questions[self.currentQuestion - 1]["NoPoints"]
        self.currentQuestion += 1

        self.changeAnswer()

        print(self.points)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec()