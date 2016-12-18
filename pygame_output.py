import os, sys
import pygame
from pygame.locals import *
import time
import logic

class PygameOutput(pygame.sprite.Sprite):

    def __init__(self, quiz, width = 800, height = 480):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.quiz = quiz
        
    def Main(self):
        answered = False
        finished = False
        index = 0
        startTime = time.time() # To declare scope

        while 1:
            self.screen.fill((100, 100, 50))

            quizImage = pygame.sprite.Sprite()
            quizImage.image = pygame.image.load("./test pygame/image")
            quizImage.rect = quizImage.image.get_rect()
            quizImage.rect.topleft = [0, 0]
            self.screen.blit(quizImage.image, quizImage.rect)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            if pygame.font:
                if(finished==True):
                    self.DisplayText("Your score is: " + str(self.quiz.questions_score),60, x=self.width/2, y=self.height/4)
                    self.DisplayText("Total Time: " + "%.2f" % self.quiz.totalTime() + "s", 60, x=self.width/2, y=3*self.height/4)

                elif(answered==False):
                    self.DisplayQuestion(index)
                else:
                    if self.quiz.questions[index].checkAnswer():
                        self.DisplayText("Correct!", 60, x=self.width/2, y=self.height/2)
                    else:
                        self.DisplayText("Incorrect, The Corect Answer Was " + self.quiz.questions[index].printCorrectAnswer(), 30, x=self.width/2, y=self.height/2)

            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    correctFont = pygame.font.Font(None, 1000)
                    result = correctFont.render("L", 1, (255, 0, 0))
                    textpos = result.get_rect(centerx=self.width/2, centery=self.height/2)
                    self.screen.blit(result, textpos)
                elif event.key == K_a:
                    self.quiz.questions[index].answer = "a"
                    answered = True
                elif event.key == K_b:
                    self.quiz.questions[index].answer = "b"
                    answered = True
                elif event.key == K_c:
                    self.quiz.questions[index].answer = "c"
                    answered = True
                elif event.key == K_d:
                    self.quiz.questions[index].answer = "d"
                    answered = True
                elif event.key == K_RETURN and answered==True and finished==False:
                    self.quiz.questions[index].duration = time.time() - startTime
                    if self.quiz.questions[index].checkAnswer():
                            self.quiz.questions_score = self.quiz.questions_score + 1

                    if(index==len(self.quiz.questions)-1):
                        finished = True
                    else:
                        answered = False;
                        index += 1
                        startTime = time.time()
                    
                    
            pygame.display.update()

    def DisplayText(self,text, size, x=0, y=0):
        font = pygame.font.Font(None, size)
        text = font.render(text, 1, (255, 0, 0))
        textpos = text.get_rect(centerx=x, centery=y)
        self.screen.blit(text, textpos)

    def DisplayQuestion(self,index):
        self.DisplayText(self.quiz.questions[index].text,36,x=self.width/2)
        self.DisplayText("A: " + self.quiz.questions[index].choices['a'],20,x=self.width/2, y=self.height/4)
        self.DisplayText("B: " + self.quiz.questions[index].choices['b'],20,x=self.width/2, y=self.height/2)
        self.DisplayText("C: " + self.quiz.questions[index].choices['c'],20,x=self.width/2, y=3*self.height/4)
        self.DisplayText("D: " + self.quiz.questions[index].choices['d'],20,x=self.width/2, y=self.height)
        
