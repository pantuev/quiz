from quizzle import getQuestions, Question
from tkinter import *

class QuestionBlock(object):
    def __init__(self, master, q:Question):
        #Текст вопроса
        self.question = q
        self.label = Label(master, text = q.question,font = "Jokerman 20")
        #Генерируем кнопки с ответами в произвольном порядке
        self.buttons = []
        for key in q.answers:
            btn = Button(root ,text = q.answers[key],
                               font = "Jokerman 20",
                               background = "#1E90FF",
                               foreground = "#FFFFFF",
                               width= "200",
                        )
            btn['command'] = lambda arg=key, this_btn=btn: self.checkAnswer(arg,this_btn)
            self.buttons.append(btn)
        # пакуем в окно
        self.label.pack()
        for btn in self.buttons:
            btn.pack()
    def checkAnswer(self, key, btn):
        if key == self.question.right:
            btn['background'] = "#0f9d58"
        else:
            btn['background'] = "#e50914"

root = Tk("Викторина")
root.title("Викторина")
root.geometry("400x320+800+200")

# Загружаем вопросы
questions = getQuestions()
fq = questions[0]

# инициируем наш класс заготовку с вопросом
QuestionBlock(root,fq)

root.mainloop()
