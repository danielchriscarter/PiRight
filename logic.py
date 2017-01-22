import csv
import time

class Quiz:
    def __init__(self, questions_path):
        self.questions_path = questions_path
        self.questions = []
        self.loadQuestions()
        self.questions_score = 0

    def randomise(self):
        randomList = []
        while(len(self.questions)>0):
            randomList.append(list.pop(random.randrange(0,len(self.questions))))
        self.questions = randomList

    def loadQuestions(self):
        with open(self.questions_path) as data:
            reader = csv.DictReader(data)
            for row in reader:
                self.questions.append(Question(row))

    def totalTime(self):
        self.total = 0
        for question in self.questions:
            self.total += question.duration
        return self.total


class Question:
    def __init__(self, row):
        self.text = row['Question']
        self.choices = {}
        self.choices['a'] = row['Answer A']
        self.choices['b'] = row['Answer B']
        self.choices['c'] = row['Answer C']
        self.choices['d'] = row['Answer D']
        self.correct = row['Correct Answer']

    def checkAnswer(self):
        return self.correct.lower() == self.answer.lower()

    def printCorrectAnswer(self):
        return self.correct + ": " + self.choices[self.correct.lower()]
