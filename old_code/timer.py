#This file has merge conflicts - please check through it
#Updated upstream
import os, sys
import pygame
from pygame.locals import *
import time

class Timer(pygame.sprite.Sprite):

    def __init__ (self):
        pygame.init()
        self.width = 800
        self.height = 480
        self.screen = pygame.display.set_mode((self.width,self.height))

    def Main(self):
        answered = False

        while 1:
            self.screen.fill((255,249,216))

            timerImage = pygame.sprite.Sprite()
            timerImage.image = pygame.image.load("blue-car-top-view-hi.png")
            timerImage.rect = timerImage.image.get_rect()
            timerImage.rect.topleft = [0,0]
            self.screen.blit(pygame.transform.scale(timerImage.image, (80,40)),  timerImage.rect)

            pygame.display.update()

Window = Timer()
Window.Main()

#Stashed changes

"""t = 0
pause = False

while pause == False:
    time.sleep(1)
    t += 1
    print (t)
    if t == 10:
        pause = True"""
