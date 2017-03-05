import os, sys
import pygame
from pygame.locals import *
import time
import random
import logic
import buttons
#import buttons_non_pi as buttons
import re
import virtualKeyboard
from pygame_funcs import *

class PygameOutput(pygame.sprite.Sprite):

    def __init__(self, width, height, screen, quiz, buttonSet):
        self.width = width
        self.height = height
        self.quiz = quiz
        self.BUTTONS = buttonSet
        buttons.Setup(self.BUTTONS)
        self.screen = screen
       
        
    def Main(self):
        answered = False
        finished = False
        ans_waiting = False
        name_entered = False
        index = 0
        startTime = time.time()
        colour = (0,0,0) #self.RandomiseColour()
        back_btn = (300,300,200,120)
        car = pygame.image.load('images/light-blue-car-top-view-th.png')
        carSprite = pygame.transform.scale(car, (40, 20))
        board = pygame.image.load('images/bigBoard.png')
        board = pygame.transform.scale(board, (650, 350))
        road = pygame.image.load('images/passing-zone-md.png')
        road = pygame.transform.scale(road, (800, 50))
        carWidth = 70
        carHeight = 402
        speed = 1
        speed_file = open("./speed", 'r')
        correct_progress_height = 0
        incorrect_progress_height = 0
        #scores = []
        try:
            speed = int(speed_file.read().strip())
        except ValueError:
            speed = 1
        speed_file.close()

        while 1:
            self.screen.fill((255, 249, 216))
            self.screen.blit(board,(75,20))
            self.screen.blit(road, (0,400))
            
            if((300*self.quiz.questions_score)/len(self.quiz.questions)>correct_progress_height):
                correct_progress_height += speed
            if((300*index)/len(self.quiz.questions)>(incorrect_progress_height+correct_progress_height)):
                incorrect_progress_height += speed

            self.rect = pygame.draw.rect(self.screen, (0,0,255), (730, 50 , 50, 320), 0)
            self.rect = pygame.draw.rect(self.screen, (255, 0, 0), (735, (360-incorrect_progress_height), 40, incorrect_progress_height), 0)
            self.rect = pygame.draw.rect(self.screen, (0, 255, 0), (735, (360-incorrect_progress_height-correct_progress_height), 40, correct_progress_height), 0)
           
            if(answered==False):
                buttonPressed = buttons.CheckPins(self.BUTTONS) 
                if(buttonPressed==self.BUTTONS[0]):
                    self.quiz.questions[index].answer = "a"
                    answered = True
                elif(buttonPressed==self.BUTTONS[1]):
                    self.quiz.questions[index].answer = "b"
                    answered = True
                elif(buttonPressed==self.BUTTONS[2]):
                    self.quiz.questions[index].answer = "c"
                    answered = True 
                elif(buttonPressed==self.BUTTONS[3]):
                    self.quiz.questions[index].answer = "d"
                    answered = True
                else:
                    self.screen.blit(car, (carWidth, carHeight))
                    carWidth+=speed
                    if carWidth >= 730:
                        answered = True
                        self.quiz.questions[index].duration = time.time() - startTime
                if(answered==True):
                    carWidth = 70

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    if(name_entered==True):
                        if(DetectCollision(back_btn, pygame.mouse.get_pos())):
                            return
                
                elif event.type == MOUSEBUTTONUP:
                    pygame.mouse.set_pos(self.width,self.height)
                
                #Test code using keyboard
                if event.type == KEYDOWN:
                    if event.key == K_q and pygame.key.get_mods() and KMOD_CTRL:
                        buttons.Cleanup()
                        pygame.quit()
                        sys.exit()
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
                    if(answered==True):
                        carWidth = 70
                    
            if(answered==True and finished==False):
                if(ans_waiting == False):
                    self.quiz.questions[index].duration = time.time() - startTime
                    if self.quiz.questions[index].checkAnswer():
                        self.quiz.questions_score = self.quiz.questions_score + 1
                    startTime = time.time()
                    ans_waiting = True
                elif((time.time()-startTime)>2):
                    startTime = time.time()
                    #scores.append(self.quiz.questions[index].checkanswer())
                    index += 1
                    if(index==len(self.quiz.questions)):
                        finished = True
                    else:
                        colour = (0,0,0) #self.RandomiseColour()
                        answered = False
                        ans_waiting = False
                
            if pygame.font:
                if(finished==True):
                    timeTaken = round(self.quiz.totalTime(),2)
                    DisplayText(self.screen, "Your score is: " + str(self.quiz.questions_score),60, (255,0,0), x=self.width/2, y=25 + self.height/8)
                    DisplayText(self.screen, "Total Time: " + str(timeTaken) + "s", 60, (255,0,0), x=self.width/2, y=25 + self.height/4)
                    if(name_entered==False):
                        DisplayText(self.screen, "Please enter your name", 40, (255,0,0), x=self.width/2, y= 25 + 3*self.height/8)
                        if((time.time()-startTime)>5):
                            vkeybd = virtualKeyboard.VirtualKeyboard(self.screen)
                            self.SaveScore(vkeybd.run(""), self.quiz.questions_score, timeTaken)
                            name_entered = True
                    else:
                        self.rect = pygame.draw.rect(self.screen, (160,224,87), back_btn, 0)
                        DisplayText(self.screen, "Main Menu", 40, (255,255,255), x=400, y=360)

                #If user hasn't finished
                elif(answered==False):
                    self.DisplayQuestion(index, colour)
                else:
                    if self.quiz.questions[index].checkAnswer():
                        DisplayText(self.screen, "Correct!", 60, (0,255,0), x=self.width/2, y=self.height/4)
                    else:
                        DisplayText(self.screen, "Incorrect", 50, (255,0,0), x=self.width/2, y=self.height/4)
                        DisplayText(self.screen, "The Correct Answer Was " + self.quiz.questions[index].printCorrectAnswer(),  30, (255,0,0), x=self.width/2, y=self.height/4+30)

                    
            pygame.display.update()

    def DisplayQuestion(self,index, colour):
        DisplayText(self.screen, self.quiz.questions[index].text,50, colour ,x=self.width/2, y= 75)
        DisplayText(self.screen, "A: " + self.quiz.questions[index].choices['a'], 35, (252,217,32),x=self.width/3, y=150)
        DisplayText(self.screen, "B: " + self.quiz.questions[index].choices['b'], 35, (20,224,20),x=2*self.width/3, y=150)
        DisplayText(self.screen, "C: " + self.quiz.questions[index].choices['c'], 35, (229,59,81),x=self.width/3, y=200)
        DisplayText(self.screen, "D: " + self.quiz.questions[index].choices['d'], 35, (60,181,181),x=2*self.width/3, y=200)

    def RandomiseColour(self):
        a = 0
        b = 0
        c = 0
        while(a<150 and b<150 and c<150):
            a = random.randint(0,255)
            b = random.randint(0,255)
            c = random.randint(0,255)
        return ((a, b, c))

    def SaveScore(self, name, score, time):
        fileOut = open("./data/scores.csv","a")
        fileOut.write(name + "," + str(score) + "," + str(time) + "," + str.split(self.quiz.questions_path,"/")[-1] + "\n")
        fileOut.close()
