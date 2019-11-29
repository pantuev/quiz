from quizzle import getQuestions, Question
from tkinter import Tk, Frame, Label, Button
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
        self.label_answer = Label(self, text ='', font = ("Arial", 24, 'bold') )
        self.label_answer.pack()

    def checkAnswer(self, key, btn):

        if key == self.question.right:
            btn['bg'] = "#0F9D58"
            self.label_answer.config(text= "Правильно!")
            self.label_answer['fg'] = "#0F9D58"
        else:
            btn['background'] = "#E50914"
            self.label_answer['text'] = "Не верно"
            self.label_answer['fg'] = "#E50914"

        self.update()
        self.after(1500, self.quit)

    def __init__(self, master, q:Question):
        Frame.__init__(self, master)
        self.pack()
        #Текст вопроса
        self.question = q
        # Создаем элементы
        self.create_widgets()

class StartScreen(Frame):
    def create_widgets(self):
        self.greeting_text = Label(self, text ='Добро пожаловать на викторину. Бла-Бла', font = ("Arial", 14))
        self.button_start = Button(self, text = 'Начать')
        self.button_start['command'] = self.start_game
        self.greeting_text.pack()
        self.button_start.pack()
   # Начать игру выходим из экрана
    def start_game(self):
        self.after(500, self.quit)
    def __init__(self, master):
        Frame.__init__(self, master)
        self.pack()
        self.create_widgets()
