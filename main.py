from quizzle import getQuestions, Question
from tkinter import *
from random import shuffle
from time import sleep

class QuestionBlock(Frame):


    def create_widgets(self):
        q = self.question
        self.label = Label(self, text = q.question,font = "Jokerman 20")
        #Генерируем кнопки с ответами в произвольном порядке
        self.buttons = []

        for key in q.answers:
            btn = Button(self ,text = q.answers[key],
                               font = "Jokerman 20",
                               background = "#1E90FF",
                               foreground = "#FFFFFF",
                               width= "200",
                        )
            btn['command'] = lambda arg=key, this_btn=btn: self.checkAnswer(arg,this_btn)
            self.buttons.append(btn)
        # пакуем в окно
        self.label.pack()
        shuffle(self.buttons)
        for btn in self.buttons:
            btn.pack()

    def checkAnswer(self, key, btn):
        self.label_answer = Label(self, text ='', font = ("Arial", 24, 'bold') )
        if key == self.question.right:
            btn['bg'] = "#0F9D58"
            btn.flash()
            self.label_answer.config(text= "Правильно!")
            self.label_answer['fg'] = "#0F9D58"
        else:
            btn['background'] = "#E50914"
            btn.flash()
            self.label_answer['text'] = "Не верно"
            self.label_answer['fg'] = "#E50914"
        self.label_answer.pack()
        sleep(2)
        self.quit()
    def __init__(self, master, q:Question):
        Frame.__init__(self, master)
        self.pack()
        #Текст вопроса
        self.question = q
        # Создаем элементы
        self.create_widgets()





root = Tk("Викторина")
root.title("Викторина")
root.geometry("400x320+800+200")

# Загружаем вопросы
questions = getQuestions()

# инициируем наш класс заготовку с вопросом
for currq in questions:
    app = QuestionBlock(root,currq)
    app.mainloop()
    app.destroy()

root.destroy()
