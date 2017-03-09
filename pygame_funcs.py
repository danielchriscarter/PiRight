import pygame

def DisplayText(screen, text, size, colour, background=None, x=0, y=0):
    font = pygame.font.Font(None, size)
    text = font.render(text, 1, (colour), background)
    textpos = text.get_rect(centerx=x, centery=y)
    screen.blit(text, textpos)

def DetectCollision(boxPos, mousePos):
    if(mousePos[0]>boxPos[0] and mousePos[0] < boxPos[0]+boxPos[2] and mousePos[1] > boxPos\
[1] and mousePos[1] < boxPos[1]+boxPos[3]):
            return True
    return False

def DetectCircularCollision(circlePos, radius, mousePos):
    if(((circlePos[0]-mousePos[0])**2 + (circlePos[1]-mousePos[1])**2)<=(radius**2)):
        return True
    return False
