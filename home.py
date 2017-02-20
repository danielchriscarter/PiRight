import os, sys
import subprocess
import pygame
import logic
import pygame_output
from pygame.locals import *
from pygame_funcs import *

class HomeScreen(pygame.sprite.Sprite):

    def __init__(self, width = 800, height = 480):
        pygame.init()
        self.width = width
        self.height = height
        # Remove third argument to test on non-touchscreen display
        self.screen = pygame.display.set_mode((self.width, self.height))#, pygame.FULLSCREEN)
        #pygame.mouse.set_visible(False)

    def Main(self):

        playButton = pygame.image.load('images/green-road-sign-md.png')
        playButton = pygame.transform.scale(playButton, (300, 200))
        stopButton = pygame.image.load('images/stop.png')
        teacherButton = pygame.image.load('images/teacherIcon.png')
        homeBackground = pygame.image.load('images/country-side-hi.png')
        homeBackground = pygame.transform.scale(homeBackground, (860,480))
        
        while 1:
            self.screen.fill((255, 249, 216))
            self.screen.blit(homeBackground, (-30,0))
            self.screen.blit(playButton, (250,175))
            btn_play = (250, 175, 300, 110)
            btn_teacher = (590,10,100,89)
            btn_exit = (700,0,100,100)

            self.screen.blit(stopButton, (700,0))
            self.screen.blit(teacherButton, (590,10))
            
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == KEYDOWN:
                    #Test code only
                    if event.key == K_q and pygame.key.get_mods() and KMOD_CTRL:
                        pygame.quit()
                        sys.exit()
                    
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    if(DetectCollision(btn_teacher, pygame.mouse.get_pos())):
                        self.screen = pygame.display.set_mode((self.width, self.height), pygame.NOFRAME)
                        subprocess.call(["gksudo", "python3", "teacher.py"])
                        self.screen = pygame.display.set_mode((self.width, self.height), pygame.FULLSCREEN)
                    elif(DetectCollision(btn_exit, pygame.mouse.get_pos())):
                        pygame.quit()
                        sys.exit()
                    elif(DetectCollision(btn_play, pygame.mouse.get_pos())):
                        quiz = logic.Quiz("./data/questions.csv")
                        Window = pygame_output.PygameOutput(self.width, self.height, self.screen, quiz, [24,25,7,8])
                        Window.Main()

            if pygame.font:
                DisplayText(self.screen, "PLAY!", 64, (255,255,255), x=400, y=240)

            pygame.display.update()

Window = HomeScreen()
Window.Main()
