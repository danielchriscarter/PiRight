import csv
import time

class Quiz:
    def __init__(self, questions_path):
        self.questions_path = questions_path
        self.questions = []
        self.loadQuestions()
        self.questions_score = 0

    def loadQuestions(self):
        with open(self.questions_path) as data:
            reader = csv.DictReader(data)
            for row in reader:
                self.questions.append(Question(row))

    def printQuestion(self, index):
        print (self.questions[index].text)
        print ("A: " + self.questions[index].choices['a'])
        print ("B: " + self.questions[index].choices['b'])
        print ("C: " + self.questions[index].choices['c'])
        print ("D: " + self.questions[index].choices['d'])

    def printAllQuestions(self):
        for index in range(len(self.questions)):
            self.printQuestion(index)
            startTime = time.time()
            self.questions[index].answer = input('Enter Answer Here: ')
            endTime = time.time()
            self.questions[index].duration = endTime - startTime
            if self.questions[index].checkAnswer():
                print ("Correct")
                self.questions_score = self.questions_score + 1
            else:
                print ("Incorrect, The Corect Answer Was " + self.questions[index].printCorrectAnswer())
            print ("Your score is: " + str(self.questions_score))
            print ("%.2f" % self.questions[index].duration + "s")

    def calculateTotalTime(self):
        self.totalTime = 0
        for question in self.questions:
            self.totalTime += question.duration
        

            
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


        
    

def main():
    quiz = Quiz('E:\Default Questions.csv')
    quiz.printAllQuestions()
    quiz.calculateTotalTime()
    print ("Total Time: " + "%.2f" % quiz.totalTime + "s")

            
    
