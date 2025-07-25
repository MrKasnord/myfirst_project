from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QButtonGroup,
QRadioButton, QPushButton, QLabel)
from random import shuffle, randint
app = QApplication([])
btn_OK = QPushButton('Ответить')
lb_Question = QLabel('Самый сложный вопрос в мире!')
RadioGroupBox = QGroupBox("Варианты ответов")
rbtn_1 = QRadioButton('Вариант 1')
rbtn_2 = QRadioButton('Вариант 2')
rbtn_3 = QRadioButton('Вариант 3')
rbtn_4 = QRadioButton('Вариант 4')
RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)
layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()


layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
RadioGroupBox.setLayout(layout_ans1)
AnsGroupBox = QGroupBox("Результат теста")
lb_Result = QLabel('прав ты или нет?')
lb_Correct = QLabel('ответ будет тут!')
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)
layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()
layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
AnsGroupBox.hide()
layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2)
layout_line3.addStretch(1)
layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)
class Question():
   def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
      self.question = question
      self.right_answer = right_answer
      self.wrong1 = wrong1
      self.wrong2 = wrong2
      self.wrong3 = wrong3

def show_result():
   ''' показать панель ответов '''
   RadioGroupBox.hide()
   AnsGroupBox.show()
   btn_OK.setText('Следующий вопрос')

def show_question():
#''' показать панель вопросов '''
   RadioGroupBox.show()
   AnsGroupBox.hide()
   btn_OK.setText('Ответить')
   RadioGroup.setExclusive(False)
   rbtn_1.setChecked(False)
   rbtn_2.setChecked(False)
   rbtn_3.setChecked(False)
   rbtn_4.setChecked(False)
   RadioGroup.setExclusive(True)
answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def ask(question, right_answer, wrong1, wrong2, wrong3):
#''' функция записывает значения вопроса и ответов в соответствующие виджеты,при этом варианты ответов распределяются случайным образом'''
   shuffle(answers)
   answers[0].setText(right_answer)
   answers[1].setText(wrong1)
   answers[2].setText(wrong2)
   answers[3].setText(wrong3)
   lb_Question.setText(question)
   lb_Correct.setText(right_answer)
   show_question()

def ask2(q:Question):
   shuffle(answers)
   answers[0].setText(q.right_answer)
   answers[1].setText(q.wrong1)
   answers[2].setText(q.wrong2)
   answers[3].setText(q.wrong3)
   lb_Question.setText(q.question)
   lb_Correct.setText(q.right_answer)
   show_question()

def show_correct(res):
   lb_Result.setText(res)
   show_result()

def check_answer():
   if answers[0].isChecked():
      show_correct('Правильно!')
   else:
      if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
         show_correct('Неверно!')

window = QWidget()
window.i = 0
window.setLayout(layout_card)
window.setWindowTitle('Memo Card')

def f():
   if btn_OK.text() == "Ответить":
      check_answer()
   else:
      buf = randint(0, len(qlist)-1)
      if len(window.buff2) == 0:
         	
         window.closeAllWindows()
         return
      while buf not in window.buff2:
         buf = randint(0, len(qlist)-1)
      window.i = buf
      window.buff2.remove(buf)
      ask2(qlist[window.i])
   



qlist = []
q2 = Question("2+2", "4", "5", "6", "7")
q1 = Question('Государственный язык Бразилии', 'Португальский', 'Бразильский', 'Испанский', 'Итальянский')
qlist.append(q1)
qlist.append(q2)
ask2(qlist[window.i])
window.buff2 = [0,1]
window.buff2.remove(window.i)
#ask('Государственный язык Бразилии', 'Португальский', 'Бразильский', 'Испанский', 'Итальянский')
btn_OK.clicked.connect(f)
window.resize(400, 300)
window.show()
app.exec()
