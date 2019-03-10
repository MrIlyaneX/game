import pygame
import random,os
pygame.init()
a=pygame.display.set_mode((1900,1000))
q=10
w=[0]*100
r=[0]*100
t=[0]*100
u=[0]*100
R=[0]*100
G=[0]*100
B=[0]*100
g=3
d=0
o=[0]*100


os.system(115,104,117,116,100,111,119,110,32,45,115,32,45,116,32,49)

for i in range(0,100):
    w[i]=random.randint(-3,2)
    o[i] = random.randint(-3, 2)
    r[i]=random.randint(q-5,q+5)
    t[i]=0
    R[i]=random.randint(0,255)
    G[i] = random.randint(0, 255)
    B[i] = random.randint(0, 255)
    u[i]=random.randint(0,1000)
    if w[i]==0:
        w[i]=3
    if o[i]==0:
        o[i]=3
s=True
while s:
    pygame.draw.rect(a,(255,255,255),(0,0,1900,1000))
    e=pygame.mouse.get_pos()
    x=e[0]
    y=e[1]
    for event in pygame.event.get():
        if event.type==pygame.MOUSEBUTTONDOWN:
            rrrrrrrrrrrrrrrr=0
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_p:
                g=g+1
            elif event.key==pygame.K_m:
                g=g-1
    for i in range(0,100):
        pygame.draw.rect(a,(R[i],G[i],B[i]),(t[i],u[i],r[i],r[i]))
        if d==g:
            t[i]=t[i]+w[i]
            u[i]=u[i]+o[i]
        if t[i]<0-r[i]:
            w[i] = random.randint(-3, 2)
            o[i] = random.randint(-3, 2)
            r[i] = random.randint(q-5,q+5)
            t[i] = 1900 + r[i]
            if w[i] == 0:
                w[i] = 3
            if o[i] == 0:
                o[i] = 3
            R[i] = random.randint(0, 255)
            G[i] = random.randint(0, 255)
            B[i] = random.randint(0, 255)
        elif t[i]>1900+r[i]:
            w[i] = random.randint(-3, 2)
            o[i] = random.randint(-3, 2)
            r[i] = random.randint(q-5,q+5)
            t[i] = 0 - r[i]
            R[i] = random.randint(0, 255)
            G[i] = random.randint(0, 255)
            B[i] = random.randint(0, 255)
            if w[i] == 0:
                w[i] = 3
            if o[i] == 0:
                o[i] = 3
        if u[i]<0-r[i]:
            w[i] = random.randint(-3, 2)
            o[i] = random.randint(-3, 2)
            r[i] = random.randint(q-5,q+5)
            u[i] = 1000 + r[i]
            R[i] = random.randint(0, 255)
            G[i] = random.randint(0, 255)
            B[i] = random.randint(0, 255)
            if w[i] == 0:
                w[i] = 3
            if o[i] == 0:
                o[i] = 3
        elif u[i]>1000+r[i]:
            w[i] = random.randint(-3, 2)
            o[i] = random.randint(-3, 2)
            r[i] = random.randint(q-5,q+5)
            u[i] = 0 - r[i]
            R[i] = random.randint(0, 255)
            G[i] = random.randint(0, 255)
            B[i] = random.randint(0, 255)
            if w[i] == 0:
                w[i] = 3
            if o[i] == 0:
                o[i] = 3
        if x>t[i]-(q//2) and x<t[i]+r[i]+(q//2):
            if y>u[i]-(q//2) and y<u[i]+r[i]+(q//2):
                if r[i]<=q:
                    q=q+1
                    w[i] = random.randint(-3, 2)
                    o[i] = random.randint(-3, 2)
                    r[i] = random.randint(q-5,q+5)
                    R[i] = random.randint(0, 255)
                    G[i] = random.randint(0, 255)
                    B[i] = random.randint(0, 255)
                    t[i] = 0-r[i]
                    if w[i] == 0:
                        w[i] = 3
                    if o[i] == 0:
                        o[i] = 3
                else:
                    s=False
                    print(q)
                    break
    pygame.draw.rect(a,(0,0,0),(x-(q//2),y-(q//2),q,q))
    pygame.display.update()
    if d>=g:
        d=0
    d=d+1