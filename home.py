import os, sys
import pygame
import logic
import teacher
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
        
        while 1:
            self.screen.fill((255, 249, 216))

            centre_play = (400,240)
            radius_play = 100
            btn_teacher = (590,0,100,50)
            btn_exit = (700,0,100,50)

            self.circle = pygame.draw.circle(self.screen, (160,224,87), centre_play, radius_play)
            self.rect = pygame.draw.rect(self.screen, (0,0,255), btn_teacher ,0)
            self.rect = pygame.draw.rect(self.screen, (255,0,0), btn_exit ,0)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == KEYDOWN:
                    if event.key == K_q and pygame.key.get_mods() and KMOD_CTRL:
                        pygame.quit()
                        sys.exit()

                    #elif event.key == K_b:
                        #Window = PygameOutput(quiz, [24,25,8,7]) #Check these numbers work
                        #Window.Main()

                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    if(DetectCollision(btn_teacher, pygame.mouse.get_pos())):
                        Window = teacher.TeacherMode(self.screen)
                        Window.Main()
                    elif(DetectCollision(btn_exit, pygame.mouse.get_pos())):
                        pygame.quit()
                        sys.exit()
                    elif(DetectCircularCollision(centre_play, radius_play, pygame.mouse.get_pos())):
                        quiz = logic.Quiz("./data/questions.csv")
                        Window = pygame_output.PygameOutput(self.width, self.height, self.screen, quiz, [24,25,7,8])
                        Window.Main()

            if pygame.font:
                DisplayText(self.screen, "PLAY!", 64, (255,255,255), x=400, y=240)
                DisplayText(self.screen, "Teacher Mode", 18, (255,255,255), x=640, y=25)
                DisplayText(self.screen, "Exit", 18, (255,255,255), x=750, y=25)

            pygame.display.update()

Window = HomeScreen()
Window.Main()
