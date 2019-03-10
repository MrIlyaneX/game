import pygame
import game
pygame.init()
a=game.display(500,500)
s=0
while 1>0:
    pos=game.mouse_pos()
    for event in pygame.event.get():
        if event.type==pygame.MOUSEBUTTONDOWN:
            if 100<pos[0]<400 and 200<pos[1]<300:
                s+=1
    pygame.draw.rect(a,(0,0,0),(0,0,500,500))
    game.write(a,(255,255,255),(0,0),100,str(s))
    pygame.draw.rect(a,(255,255,255),(100,200,300,100),3)
    game.write(a,(255,255,255),(102,225),59,"Кликай здесь!")
    pygame.display.update()