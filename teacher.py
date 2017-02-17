import os, sys
import pygame
from pygame.locals import *
from pygame_funcs import *
import tkinter
from tkinter import filedialog

class TeacherMode(pygame.sprite.Sprite):

    def __init__(self, width = 800, height = 480):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.NOFRAME)
        
    def Main(self):
        warning = False
        # All buttons use x-position, y-position, x-size, y-size
        import_btn = (140, 150, 200,50)
        set_btn = (140, 350, 200,50)
        export_btn = (460, 150, 200,50)
        clear_btn = (460, 350, 200,50)
        exit_btn = (300,250,200,50)

        yes_btn = (150, 300, 180, 80)
        no_btn = (470, 300, 180, 80)

        while 1:
            self.screen.fill((0, 0, 0))
            
            if(warning):
                self.rect = pygame.draw.rect(self.screen, (255,0,0), yes_btn,0)
                self.rect = pygame.draw.rect(self.screen, (255,0,0), no_btn,0)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    
                    if event.type == MOUSEBUTTONDOWN and event.button == 1:
                        if(DetectCollision(yes_btn, pygame.mouse.get_pos())):
                            os.system("cp ./data/score_template.csv ./data/scores.csv")
                            warning = False
                        elif(DetectCollision(no_btn, pygame.mouse.get_pos())):
                            warning = False
                
                if pygame.font:
                    DisplayText(self.screen, "Are you sure you wish to erase all scores?", 40, (255,255,255), x=400, y=50)
                    DisplayText(self.screen, "Yes", 40, (255,255,255), x=240, y=340)
                    DisplayText(self.screen, "No", 40, (255,255,255), x=560, y=340)
            
            else:   
                self.rect = pygame.draw.rect(self.screen, (255,0,0), import_btn,0)
                self.rect = pygame.draw.rect(self.screen, (255,0,0), set_btn,0)
                self.rect = pygame.draw.rect(self.screen, (255,0,0), exit_btn,0)
                self.rect = pygame.draw.rect(self.screen, (255,0,0), export_btn,0)
                self.rect = pygame.draw.rect(self.screen, (255,0,0), clear_btn,0)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                                                            
                    if event.type == MOUSEBUTTONDOWN and event.button == 1:
                        if(DetectCollision(import_btn, pygame.mouse.get_pos())):
                            root = tkinter.Tk()
                            root.withdraw()
                            name = filedialog.askopenfilename(filetypes=[("CSV files","*.csv")],initialdir="/media")
                            os.system("cp " + name + " ./questions/")
                        elif(DetectCollision(exit_btn, pygame.mouse.get_pos())):
                            return
                        elif(DetectCollision(export_btn, pygame.mouse.get_pos())):
                            root = tkinter.Tk()
                            root.withdraw()
                            name = filedialog.asksaveasfilename(defaultextension=".csv",initialdir="/media")
                            os.system("cp ./data/scores.csv " + name)
                        elif(DetectCollision(clear_btn, pygame.mouse.get_pos())):
                            warning = True
                        elif(DetectCollision(set_btn, pygame.mouse.get_pos())):
                            root = tkinter.Tk()
                            root.withdraw()
                            name = filedialog.askopenfilename(filetypes=[("CSV files","*.csv")],initialdir="./questions")
                            os.system("cp " + name + " ./data/questions.csv")
                    
                if pygame.font:
                    DisplayText(self.screen, "Teacher Mode", 60, (255,255,255), x=400, y=50)
                    DisplayText(self.screen, "Import questions", 30, (255,255,255), x=240, y=175)
                    DisplayText(self.screen, "Select question set", 30, (255,255,255), x=240, y=375)
                    DisplayText(self.screen, "Export scores", 30, (255,255,255), x=560, y=175)
                    DisplayText(self.screen, "Clear scores", 30, (255,255,255), x=560, y=375)
                    DisplayText(self.screen, "Exit", 30, (255,255,255), x=400, y=275)
                    
            pygame.display.update()

Window = TeacherMode()
Window.Main()
