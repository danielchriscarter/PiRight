import os, sys
import pygame
from pygame.locals import *
from pygame_funcs import *

class TeacherMode(pygame.sprite.Sprite):

    def __init__(self, screen):
        self.screen = screen
        
    def Main(self):
        warning = False
        # All buttons use x-position, y-position, x-size, y-size
        import_btn = (150, 150, 180,50)
        exit_btn = (150, 350, 180,50)
        export_btn = (470, 150, 180,50)
        clear_btn = (470, 350, 180,50)

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
                            os.system("gksudo ./scripts/clear.sh")
                            warning = False
                        elif(DetectCollision(no_btn, pygame.mouse.get_pos())):
                            warning = False
                
                if pygame.font:
                    DisplayText(self.screen, "Are you sure you wish to erase all scores?", 40, (255,255,255), x=400, y=50)
                    DisplayText(self.screen, "Yes", 40, (255,255,255), x=240, y=340)
                    DisplayText(self.screen, "No", 40, (255,255,255), x=560, y=340)
            
            else:   
                self.rect = pygame.draw.rect(self.screen, (255,0,0), import_btn,0)
                self.rect = pygame.draw.rect(self.screen, (255,0,0), exit_btn,0)
                self.rect = pygame.draw.rect(self.screen, (255,0,0), export_btn,0)
                self.rect = pygame.draw.rect(self.screen, (255,0,0), clear_btn,0)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                                                            
                    if event.type == MOUSEBUTTONDOWN and event.button == 1:
                        if(DetectCollision(import_btn, pygame.mouse.get_pos())):
                            os.system("gksudo ./scripts/import.sh")
                        elif(DetectCollision(exit_btn, pygame.mouse.get_pos())):
                            return
                        elif(DetectCollision(export_btn, pygame.mouse.get_pos())):
                            os.system("gksudo ./scripts/export.sh")
                        elif(DetectCollision(clear_btn, pygame.mouse.get_pos())):
                            warning = True
                    
                if pygame.font:
                    DisplayText(self.screen, "Teacher Mode", 60, (255,255,255), x=400, y=50)
                    DisplayText(self.screen, "Import questions", 30, (255,255,255), x=240, y=175)
                    DisplayText(self.screen, "Exit", 30, (255,255,255), x=240, y=375)
                    DisplayText(self.screen, "Export scores", 30, (255,255,255), x=560, y=175)
                    DisplayText(self.screen, "Clear scores", 30, (255,255,255), x=560, y=375)
                    
            pygame.display.update()
