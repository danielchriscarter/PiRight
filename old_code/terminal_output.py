import logic
import time

class TerminalOutput:

    def __init__(self, quiz):
        self.quiz = quiz
        
    def printQuestion(self, index):
        print (self.quiz.questions[index].text)
        print ("A: " + self.quiz.questions[index].choices['a'])
        print ("B: " + self.quiz.questions[index].choices['b'])
        print ("C: " + self.quiz.questions[index].choices['c'])
        print ("D: " + self.quiz.questions[index].choices['d'])

    def printAllQuestions(self):
        for index in range(len(self.quiz.questions)):
            self.printQuestion(index)
            startTime = time.time()
            self.quiz.questions[index].answer = input('Enter Answer Here: ')
            endTime = time.time()
            self.quiz.questions[index].duration = endTime - startTime
            if self.quiz.questions[index].checkAnswer():
                print ("Correct")
                self.quiz.questions_score = self.quiz.questions_score + 1
            else:
                print ("Incorrect, The Corect Answer Was " + self.quiz.questions[index].printCorrectAnswer())
            print ("Your score is: " + str(self.quiz.questions_score))
            print ("%.2f" % self.quiz.questions[index].duration + "s")
