#This file has merge conflicts - please check through it
#Updated upstream
import os, sys
import pygame
from pygame.locals import *
import time

class Timer(pygame.sprite.Sprite):

    def __init__ (self, screen, width, height):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((800, 480))

    def Main(self):
        answered = False

        while 1:
            self.screen.fill((255,249,216))

            timerImage = pygame.sprite.Sprite()
            timerImage.image = pygame.image.load("/home/pi/2016-17/blue-car-top-view-hi.png")
            screen.blit(timerImage, (width/2, height/2))

            pygame.display.update

Window = Timer()
Window.Main()

#Stashed changes
import time

t = 0
pause = False

while pause == False:
    time.sleep(1)
    t += 1
    print (t)
    if t == 10:
        pause = True
