import pygame
import game
import random
pygame.init()
days=3
b=100
a=pygame.display.set_mode((1250,626))
buying=0
celling=0
kurs=random.randint(50,150)
bitcoins=0
while 1>0:
    pos=game.mouse_pos()
    R = 0
    B = 255
    r1=0
    b1=255
    r2=0
    b2=255
    r3=0
    b3=255
    r4=0
    b4=255
    r5=0
    b5=255
    r6=0
    b6=255
    r7=0
    b7=255
    r8=0
    b8=255
    for event in pygame.event.get():
        if event.type==pygame.MOUSEBUTTONDOWN:
            if 200 < pos[0] < 250 and 150 < pos[1] < 200:
                if buying>0:
                    buying-=1
            if 200 < pos[0] < 250 and 200 < pos[1] < 250:
                if celling>0:
                    celling-=1
            if 0 < pos[0] < 150 and 150 < pos[1] < 200:
                if buying*kurs<=b:
                    bitcoins+=buying
                    b-=buying*kurs
            if 550 < pos[0] < 624 and 150 < pos[1] < 200:
                buying=b//kurs
            if 500 < pos[0] < 550 and 150 < pos[1] < 200:
                buying += 1
            if 500 < pos[0] < 550 and 200 < pos[1] < 250:
                celling += 1
            if 0 < pos[0] < 200 and 200 < pos[1] < 250:
                if celling<=bitcoins:
                    b+=celling*kurs
                    bitcoins-=celling
            if 550 < pos[0] < 624 and 200 < pos[1] < 250:
                celling=bitcoins
            if 250<pos[0]<500 and 200<pos[1]<250:
                chek = 0
                buying = 0
                while chek == 0:
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            chek = 1
                        elif event.type == pygame.KEYDOWN:
                            if event.key==pygame.K_0:
                                celling=celling*10+0
                            elif event.key==pygame.K_1:
                                celling=celling*10+1
                            elif event.key==pygame.K_2:
                                celling=celling*10+2
                            elif event.key==pygame.K_3:
                                celling=celling*10+3
                            elif event.key==pygame.K_4:
                                celling=celling*10+4
                            elif event.key==pygame.K_5:
                                celling=celling*10+5
                            elif event.key==pygame.K_6:
                                celling=celling*10+6
                            elif event.key==pygame.K_7:
                                celling=celling*10+7
                            elif event.key==pygame.K_8:
                                celling=celling*10+8
                            elif event.key==pygame.K_9:
                                celling=celling*10+9
                    pygame.draw.rect(a, (255, 255, 255), (0, 0, 1250, 626))
                    if days > 1:
                        game.write(a, (0, 0, 0), (0, 0), 50, str(days) + " дня до налога")
                    else:
                        game.write(a, (0, 0, 0), (0, 0), 50, "1 день до налога")
                    game.write(a, (0, 0, 0), (0, 100), 50, "Bitcoins:" + str(bitcoins))
                    game.write(a, (0, 0, 0), (0, 50), 50, "Баланс:" + str(b) + "$")
                    game.write(a, (0, 0, 0), (0, 574), 50, "Курс биткоина:" + str(kurs) + "$")
                    game.write(a, (R, 0, B), (0, 150), 50, "Купить")
                    pygame.draw.rect(a, (0, 0, 0), (250, 150, 250, 50), 1)
                    game.write(a, (r3, 0, b3), (0, 200), 50, "Продать")
                    pygame.draw.rect(a, (0, 0, 0), (250, 200, 250, 50), 1)
                    game.write(a, (r4, 0, b4), (500, 150), 50, "+")
                    game.write(a, (r6, 0, b6), (500, 200), 50, "+")
                    game.write(a, (r1, 0, b1), (200, 150), 50, "-")
                    game.write(a, (r5, 0, b5), (200, 200), 50, "-")
                    game.write(a, (r2, 0, b2), (550, 150), 50, "max")
                    game.write(a, (r7, 0, b7), (550, 200), 50, "max")
                    game.write(a, (r8, 0, b8), (900, 576), 50, "Следующий день...")
                    game.write(a, (0, 0, 0), (250, 150), 50, str(buying))
                    game.write(a, (0, 0, 0), (250, 200), 50, str(celling))
                    pygame.draw.rect(a, (0, 0, 0), (0, 260, 625, 300), 3)
                    pygame.display.update()
            if 250<pos[0]<500 and 150<pos[1]<200:
                chek = 0
                buying=0
                while chek == 0:
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            chek=1
                        elif event.type==pygame.KEYDOWN:
                            if event.key==pygame.K_0:
                                buying=buying*10+0
                            elif event.key==pygame.K_1:
                                buying=buying*10+1
                            elif event.key==pygame.K_2:
                                buying=buying*10+2
                            elif event.key==pygame.K_3:
                                buying=buying*10+3
                            elif event.key==pygame.K_4:
                                buying=buying*10+4
                            elif event.key==pygame.K_5:
                                buying=buying*10+5
                            elif event.key==pygame.K_6:
                                buying=buying*10+6
                            elif event.key==pygame.K_7:
                                buying=buying*10+7
                            elif event.key==pygame.K_8:
                                buying=buying*10+8
                            elif event.key==pygame.K_9:
                                buying=buying*10+9
                    pygame.draw.rect(a, (255, 255, 255), (0, 0, 1250, 626))
                    if days > 1:
                        game.write(a, (0, 0, 0), (0, 0), 50, str(days) + " дня до налога")
                    else:
                        game.write(a, (0, 0, 0), (0, 0), 50, "1 день до налога")
                    game.write(a, (0, 0, 0), (0, 100), 50, "Bitcoins:" + str(bitcoins))
                    game.write(a, (0, 0, 0), (0, 50), 50, "Баланс:" + str(b) + "$")
                    game.write(a, (0, 0, 0), (0, 574), 50, "Курс биткоина:" + str(kurs) + "$")
                    game.write(a, (R, 0, B), (0, 150), 50, "Купить")
                    pygame.draw.rect(a, (0, 0, 0), (250, 150, 250, 50), 1)
                    game.write(a, (r3, 0, b3), (0, 200), 50, "Продать")
                    pygame.draw.rect(a, (0, 0, 0), (250, 200, 250, 50), 1)
                    game.write(a, (r4, 0, b4), (500, 150), 50, "+")
                    game.write(a, (r6, 0, b6), (500, 200), 50, "+")
                    game.write(a, (r1, 0, b1), (200, 150), 50, "-")
                    game.write(a, (r5, 0, b5), (200, 200), 50, "-")
                    game.write(a, (r2, 0, b2), (550, 150), 50, "max")
                    game.write(a, (r7, 0, b7), (550, 200), 50, "max")
                    game.write(a, (r8, 0, b8), (900, 576), 50, "Следующий день...")
                    game.write(a, (0, 0, 0), (250, 150), 50, str(buying))
                    game.write(a, (0, 0, 0), (250, 200), 50, str(celling))
                    pygame.draw.rect(a, (0, 0, 0), (0, 260, 625, 300), 3)
                    pygame.display.update()
            if 900 < pos[0] < 1250 and 576 < pos[1] < 626:
                kurs=random.randint(50,150)
                if days>1:
                    days-=1
                else:
                    days=3
                    qwe=int(b*0.13)
                    b-=int(b*0.13)
                    chek=0
                    while chek==0:
                        for event in pygame.event.get():
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                chek=1
                        game.write(a,(0,0,0),(350,0),75,"Вы оплатили налог суммой "+str(int(qwe))+"$")
                        pygame.display.update()
    if 200<pos[0]<250 and 150<pos[1]<200:
        r1=255
        b1=0
    if 200<pos[0]<250 and 200<pos[1]<250:
        r5=255
        b5=0
    if 0<pos[0]<150 and 150<pos[1]<200:
        R=255
        B=0
    if 550<pos[0]<624 and 150<pos[1]<200:
        r2=255
        b2=0
    if 500<pos[0]<550 and 150<pos[1]<200:
        r4=255
        b4=0
    if 500<pos[0]<550 and 200<pos[1]<250:
        r6=255
        b6=0
    if 0<pos[0]<200 and 200<pos[1]<250:
        b3=0
        r3=255
    if 550<pos[0]<624 and 200<pos[1]<250:
        r7=255
        b7=0
    if 900<pos[0]<1250 and 576<pos[1]<626:
        r8=255
        b8=0
    pygame.draw.rect(a,(255,255,255),(0,0,1250,626))
    if days>1:
        game.write(a, (0, 0, 0), (0, 0), 50, str(days) + " дня до налога")
    else:
        game.write(a,(0,0,0),(0,0),50,"1 день до налога")
    game.write(a,(0,0,0),(0,100),50,"Bitcoins:"+str(bitcoins))
    game.write(a,(0,0,0),(0,50),50,"Баланс:"+str(b)+"$")
    game.write(a,(0,0,0),(0,574),50,"Курс биткоина:"+str(kurs)+"$")
    game.write(a,(R,0,B),(0,150),50,"Купить")
    pygame.draw.rect(a,(0,0,0),(250,150,250,50),1)
    game.write(a,(r3,0,b3),(0,200),50,"Продать")
    pygame.draw.rect(a, (0, 0, 0), (250, 200, 250, 50), 1)
    game.write(a, (r4, 0, b4), (500, 150), 50, "+")
    game.write(a, (r6, 0, b6), (500, 200), 50, "+")
    game.write(a,(r1,0,b1),(200,150),50,"-")
    game.write(a, (r5, 0, b5), (200, 200), 50, "-")
    game.write(a,(r2,0,b2),(550,150),50,"max")
    game.write(a, (r7, 0, b7), (550, 200), 50, "max")
    game.write(a,(r8,0,b8),(900,576),50,"Следующий день...")
    game.write(a,(0,0,0),(250,150),50,str(buying))
    game.write(a, (0, 0, 0), (250, 200), 50, str(celling))
    pygame.draw.rect(a,(0,0,0),(0,260,625,300),3)
    pygame.display.update()