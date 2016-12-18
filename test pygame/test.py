import os, sys
import pygame
from pygame.locals import *
import time

class PyManMain(pygame.sprite.Sprite):

    def __init__(self, width = 800, height = 480):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.screen.fill((100, 100, 50))
        
        quizImage = pygame.sprite.Sprite()
        quizImage.image = pygame.image.load("image")
        quizImage.rect = quizImage.image.get_rect()
        quizImage.rect.topleft = [0, 0]
        self.screen.blit(quizImage.image, quizImage.rect)
        
    def Main(self):

        while 1:
            pygame.draw.rect(self.screen, (100,100,50), (100,50,20,20))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            if pygame.font:
                font = pygame.font.Font(None, 36)
                text = font.render("THE QUIZ", 1, (255, 0, 0))
                textpos = text.get_rect(centerx=self.width/2)
                self.screen.blit(text, textpos)

            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    correctFont = pygame.font.Font(None, 1000)
                    result = correctFont.render("L", 1, (255, 0, 0))
                    textpos = result.get_rect(centerx=self.width/2, centery=self.height/2)
                    self.screen.blit(result, textpos)

            


#class testImage(pygame.sprite.Sprite):
#    def __init__(self):
#        quizImage = pygame.sprite.Sprite()
#        quizImage.image = pygame.image.load("image")
#        quizImage.rect = quizImage.image.get_rect()
#        quizImage.rect.topleft = [0, 0]


if __name__ == "__main__":
    Window = PyManMain()
    Window.Main()
