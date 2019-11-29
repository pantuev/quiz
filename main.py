from quizzle import getQuestions, Question
from tkinter import Tk
from random import shuffle
from time import sleep
from gui import QuestionBlock, StartScreen





root = Tk("Викторина")
root.title("Викторина")
root.geometry("400x320+800+200")

# Загружаем стартовый экран
start = StartScreen(root)
start.mainloop()
start.destroy()

# TODO экран выбора темы

# Загружаем вопросы и перемешиваем

questions = getQuestions()
shuffle(questions)

# инициируем наш класс заготовку с вопросом
for currq in questions:
    app = QuestionBlock(root,currq)
    app.mainloop()
    app.destroy()



# когда все кончиться убиваем главное окно
root.destroy()
