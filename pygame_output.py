import os, sys
import pygame
from pygame.locals import *
import time
import random
import logic

class PygameOutput(pygame.sprite.Sprite):

    def __init__(self, quiz, buttons, width = 800, height = 480):
        pygame.init()
        self.width = width
        self.height = height
        # Remove third argument to test on non-touchscreen display
        self.screen = pygame.display.set_mode((self.width, self.height))#, pygame.FULLSCREEN)
        self.quiz = quiz
        self.BUTTONS = buttons
        pygame.mouse.set_visible(False)
        
    def Main(self):
        answered = False
        finished = False
        index = 0
        startTime = time.time() # To declare scope
        colour = self.RandomiseColour()

        while 1:
            self.screen.fill((100, 100, 50))

            quizImage = pygame.sprite.Sprite()
            quizImage.image = pygame.image.load("./test pygame/image")
            quizImage.rect = quizImage.image.get_rect()
            quizImage.rect.topleft = [0, 0]
            self.screen.blit(quizImage.image, quizImage.rect)
            button_string = ""
            for button in self.BUTTONS:
                button_string += (str(button) + " ")
            buttonPressed = [0,0,0,0,0]#os.system("gksudo ./scripts/run_buttons.sh " + button_string)
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


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == KEYDOWN:
                    if event.key == K_q and pygame.key.get_mods() and KMOD_CTRL:
                        pygame.quit()
                        sys.exit()
                    elif event.key == K_RIGHT:
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
                            colour = self.RandomiseColour()
                
            if pygame.font:
                if(finished==True):
                    timeTaken = round(self.quiz.totalTime(),2)
                    self.DisplayText("Your score is: " + str(self.quiz.questions_score),60, (255,0,0), x=self.width/2, y=self.height/4)
                    self.DisplayText("Total Time: " + str(timeTaken) + "s", 60, (255,0,0), x=self.width/2, y=3*self.height/4)
                    if(answered==True):
                        # Need to add name gathering mechanism here!
                        self.SaveScore("Joe Bloggs", self.quiz.questions_score, timeTaken)
                        answered = False

                elif(answered==False):
                    self.DisplayQuestion(index, colour)
                else:
                    if self.quiz.questions[index].checkAnswer():
                        self.DisplayText("Correct!", 60, (0,255,0), x=self.width/2, y=self.height/2)
                    else:
                        self.DisplayText("Incorrect", 50, (255,0,0), x=self.width/2, y=self.height/2)
                        self.DisplayText("The Correct Answer Was " + self.quiz.questions[index].printCorrectAnswer(),  30, (255,0,0), x=self.width/2, y=self.height/2+30)

                    
            pygame.display.update()

    def DisplayText(self,text, size, colour, x=0, y=0):
        font = pygame.font.Font(None, size)
        text = font.render(text, 1, (colour))
        textpos = text.get_rect(centerx=x, centery=y)
        self.screen.blit(text, textpos)

    def DisplayQuestion(self,index, colour):
        self.DisplayText(self.quiz.questions[index].text,50, colour ,x=self.width/2, y= 50)
        self.DisplayText("A: " + self.quiz.questions[index].choices['a'], 35, (255,255,0),x=self.width/3, y=300)
        self.DisplayText("B: " + self.quiz.questions[index].choices['b'], 35, (0,255,0),x=2*self.width/3, y=300)
        self.DisplayText("C: " + self.quiz.questions[index].choices['c'], 35, (255,0,0),x=self.width/3, y=400)
        self.DisplayText("D: " + self.quiz.questions[index].choices['d'], 35, (0,0,255),x=2*self.width/3, y=400)

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
        fileOut.write(name + "," + str(score) + "," + str(time) + "\n")
        fileOut.close()
