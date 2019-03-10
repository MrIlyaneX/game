import pygame
from threading import Thread
pygame.init()
import math
def write(display,color,pos,size,text):
    font = pygame.font.Font(None, size)
    text = font.render(text, True, (color))
    display.blit(text, pos)
def display(width,height):
    return pygame.display.set_mode((width,height))
def mouse_pos():
    return pygame.mouse.get_pos()
def move(speed,pos1,pos2):
    q=pos2[0]-pos1[0]
    w=pos2[1]-pos1[1]
    if q==0 and w==0:
        return pos1[0], pos1[1]
    else:
        e = math.sqrt(q ** 2 + w ** 2)
        r = speed / e
        if e <= speed:
            return pos2[0], pos2[1]
        else:
            return int(pos1[0] + q * r), int(pos1[1] + w * r)
def mouse_visible(q):
    if q==True:
        pygame.mouse.set_visible(1)
    else:
        pygame.mouse.set_visible(0)