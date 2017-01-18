import os, sys
import pygame
from pygame.locals import *

class TeacherMode(pygame.sprite.Sprite):

    def __init__(self, width = 800, height = 480):
        pygame.init()
        self.width = width
        self.height = height
#        self.font = pygame.font(None,20)
        # Remove third argument to test on non-touchscreen display
        self.screen = pygame.display.set_mode((self.width, self.height))#, pygame.FULLSCREEN)
        pygame.mouse.set_visible(False)
        
    def Main(self):
        while 1:
            self.screen.fill((100, 100, 50))

            self.rect = pygame.draw.rect(self.screen, (255,0,0), (400, 200, 150,75),0)
 #           self.screen.blit(self.font.render("Import", True, (255,255,255)),(self.widt

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == KEYDOWN:
                    if event.key == K_RETURN:
                        os.system("gksudo ./import.sh")
                
            if pygame.font:
                self.DisplayText("Import", 30, (255,255,255), x=450, y=225)
#                self.DisplayText("Press enter to import files", 50, (255,0,0), x=400, y=200)
                    
            pygame.display.update()

    def DisplayText(self,text, size, colour, x=0, y=0):
        font = pygame.font.Font(None, size)
        text = font.render(text, 1, (colour))
        textpos = text.get_rect(centerx=x, centery=y)
        self.screen.blit(text, textpos)


#These are present for testing only - REMOVE when adding to final product
Window = TeacherMode()
Window.Main()
