#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QHBoxLayout, QVBoxLayout, QRadioButton, QGroupBox, QButtonGroup
from random import shuffle

app = QApplication([])
window = QWidget ()
window.setWindowTitle('Memory Card')

class Question():
    def __init__(self, question, right_a, w1, w2, w3):
        self.question = question
        self.right_a = right_a
        self.w1 = w1
        self.w2 = w2
        self.w3 = w3

######################################################

question = QLabel('Какой национальности не существует?')
btnok = QPushButton('Ответить')
rbtn1 = QRadioButton('Энцы')
rbtn2 = QRadioButton('Смурфы')
rbtn3 = QRadioButton('Чулымцы')
rbtn4 = QRadioButton('Алеуты')
group = QGroupBox('Варианты ответов')
groupR = QButtonGroup()
groupR.addButton(rbtn1)
groupR.addButton(rbtn2)
groupR.addButton(rbtn3)
groupR.addButton(rbtn4)

rbg1 = QVBoxLayout()
rbg2 = QVBoxLayout()

rbg1.addWidget(rbtn1)
rbg1.addWidget(rbtn2)
rbg2.addWidget(rbtn3)
rbg2.addWidget(rbtn4)

rbgmain = QHBoxLayout()
rbgmain.addLayout(rbg1)
rbgmain.addLayout(rbg2)

group.setLayout(rbgmain)

groupok = QGroupBox('Результаты теста')
answer = QLabel('Неправильный ответ')
groupokline = QVBoxLayout()
groupokline.addWidget(answer, alignment=Qt.AlignCenter)
groupok.setLayout(groupokline)
groupok.hide()

linemain = QVBoxLayout()
linemain.addWidget(question, stretch=2, alignment=Qt.AlignCenter)
linemain.addWidget(group, stretch=8, alignment=Qt.AlignCenter)
linemain.addWidget(groupok, stretch=8, alignment=Qt.AlignCenter)
linemain.addWidget(btnok,stretch=2, alignment=Qt.AlignCenter)

window.setLayout(linemain)


window.a = 0
window.b = 0

def checkAnswer():
    if list_btns[0].isChecked():
        answer.setText('Правильный ответ')
        window.a = window.a + 1
        answer.setText('Ваши правильные ответы ' + str( window.a))
    else:
        answer.setText('Неправильный ответ')
        window.b = window.b + 1
        answer.setText('Ваши неправильные ответы ' + str(window.b))
    group.hide()
    groupok.show()
    btnok.setText('Следующий вопрос')

def showQ():
    groupok.hide()
    group.show()
    btnok.setText('Ответить')
    groupR.setExclusive(False)
    rbtn1.setChecked(False)
    rbtn2.setChecked(False)
    rbtn3.setChecked(False)
    rbtn4.setChecked(False)
    groupR.setExclusive(True)

def btnclick():
    text = btnok.text()
    if text == 'Ответить':
        checkAnswer()
    else:
        qlist.remove(qlist[0])
        if len(qlist) > 0:
            ask(qlist[0])
        else:
            quit()
list_btns = [rbtn1, rbtn2, rbtn3, rbtn4]
def ask(q):
    shuffle(list_btns) # Перемешиваем кнопки
    list_btns[0].setText(q.right_a) # Первая кнопка в списке будет правильным ответом
    list_btns[1].setText(q.w1)
    list_btns[2].setText(q.w2)
    list_btns[3].setText(q.w3)
    question.setText(q.question)
    showQ()

btnok.clicked.connect(btnclick)


qlist = [
Question('дай пж 2 рубля', 'недам', 'на 2 доллара', 'на 1 фунт', 'на 2 рубля'),
Question('Ломай ломай мы же - ', 'мультимелиардеры', 'меллионеры', 'бомжи', 'олиграхи'),
Question('Щэ не вмерла - ', 'Омерика', 'Россия', 'США блин', 'беларуски'),
Question('Вопрос от жака флекса - ', 'да', 'слава укриина', 'ты кто', 'я тут?'),
Question('Что сделал Слава - ', 'Не сделал', 'Сделал', 'реп', 'ыы моргинштерн')
]

shuffle(qlist)
ask(qlist[0])
###########################################################

window.show()
app.exec_()