import csv

class Question(object):
    def __init__(self, question : str, answers : dict, right : int):
        self.question = question
        self.answers = answers
        self.right = right
    def __str__(self):
        return f"{self.question} \n"+'\n'.join(list(self.answers.values()))+f'\nПравильный ответ: {self.right+1}'
def csvAdapter(filename = 'quizquestions.csv')->list:
    questions = list()
    with open(filename, encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            answers = dict()
            for col in range(1,len(row)):
                if row[col]:
                    answers[col-1] = row[col]
            questions.append(Question(row[0], answers, 0))
    return questions

def getQuestions(source = csvAdapter) ->list :
    return source()
