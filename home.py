import os, sys
import pygame
from pygame.locals import *

class HomeScreen(pygame.sprite.Sprite):

    def __init__(self, width = 800, height = 480):
        pygame.init()
        self.width = width
        self.height = height
        # Remove third argument to test on non-touchscreen display
        self.screen = pygame.display.set_mode((self.width, self.height))#, pygame.FULLSCREEN)
        pygame.mouse.set_visible(False)

    def Main(self):
        
        while 1:
            self.screen.fill((255, 249, 216))

            self.circle = pygame.draw.circle(self.screen, (160,224,87), (400,240) ,100)
            self.rect = pygame.draw.rect(self.screen, (0,0,255), (590,0,100,50) ,0)
            self.rect = pygame.draw.rect(self.screen, (255,0,0), (700,0,100,50) ,0)

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


            if pygame.font:
                    self.DisplayText("PLAY!", 64, (255,255,255), x=400, y=240)
                    self.DisplayText("Teacher Mode", 18, (255,255,255), x=640, y=25)
                    self.DisplayText("Exit", 18, (255,255,255), x=750, y=25)

            pygame.display.update()

    def DisplayText(self,text, size, colour, x=0, y=0):
        font = pygame.font.Font(None, size)
        text = font.render(text, 1, (colour))
        textpos = text.get_rect(centerx=x, centery=y)
        self.screen.blit(text, textpos)


Window = HomeScreen()
Window.Main()
