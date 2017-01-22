import os, sys
import pygame
from pygame.locals import *

class TeacherMode(pygame.sprite.Sprite):

    def __init__(self, width = 800, height = 480):
        pygame.init()
        self.width = width
        self.height = height
        # Remove third argument to test on non-touchscreen display
        self.screen = pygame.display.set_mode((self.width, self.height))#, pygame.FULLSCREEN)
        pygame.mouse.set_visible(True)#temporarily, to test
        
    def Main(self):
        warning = False
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
                        if(self.DetectCollision(yes_btn, pygame.mouse.get_pos())):
                            os.system("gksudo ./scripts/clear.sh")
                            warning = False
                        elif(self.DetectCollision(no_btn, pygame.mouse.get_pos())):
                            warning = False
                
                if pygame.font:
                    self.DisplayText("Are you sure you wish to erase all scores?", 40, (255,255,255), x=400, y=50)
                    self.DisplayText("Yes", 40, (255,255,255), x=240, y=340)
                    self.DisplayText("No", 40, (255,255,255), x=560, y=340)
            
            else:   
                self.rect = pygame.draw.rect(self.screen, (255,0,0), import_btn,0)
                self.rect = pygame.draw.rect(self.screen, (255,0,0), exit_btn,0)
                self.rect = pygame.draw.rect(self.screen, (255,0,0), export_btn,0)
                self.rect = pygame.draw.rect(self.screen, (255,0,0), clear_btn,0)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    
                    #if event.type == KEYDOWN:
                        #if event.key == K_RETURN:
                            #os.system("gksudo ./scripts/import.sh")
                    
                    if event.type == MOUSEBUTTONDOWN and event.button == 1:
                        if(self.DetectCollision(import_btn, pygame.mouse.get_pos())):
                            os.system("gksudo ./scripts/import.sh")
                        elif(self.DetectCollision(exit_btn, pygame.mouse.get_pos())):
                            # May need reworking to return to user mode
                            pygame.quit()
                        elif(self.DetectCollision(export_btn, pygame.mouse.get_pos())):
                            os.system("gksudo ./scripts/export.sh")
                        elif(self.DetectCollision(clear_btn, pygame.mouse.get_pos())):
                            warning = True
                    
                if pygame.font:
                    self.DisplayText("Teacher Mode", 60, (255,255,255), x=400, y=50)
                    self.DisplayText("Import questions", 30, (255,255,255), x=240, y=175)
                    self.DisplayText("Exit", 30, (255,255,255), x=240, y=375)
                    self.DisplayText("Export scores", 30, (255,255,255), x=560, y=175)
                    self.DisplayText("Clear scores", 30, (255,255,255), x=560, y=375)
                    
            pygame.display.update()

    def DisplayText(self,text, size, colour, x=0, y=0):
        font = pygame.font.Font(None, size)
        text = font.render(text, 1, (colour))
        textpos = text.get_rect(centerx=x, centery=y)
        self.screen.blit(text, textpos)

    def DetectCollision(self, boxPos, mousePos):
        if(mousePos[0]>boxPos[0] and mousePos[0] < boxPos[0]+boxPos[2] and mousePos[1] > boxPos[1] and mousePos[1] < boxPos[1]+boxPos[3]):
                return True
        return False


#These are present for testing only - REMOVE when adding to final product
Window = TeacherMode()
Window.Main()
