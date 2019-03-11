def inversia(x,y):
    a=pygame.display.set_mode((x,y))
    root=tkinter.Tk()
    label=tkinter.Label(text='0%')
    label.pack()
    global image
    global proc1
    a.blit(image,(0,0))
    pygame.display.update()
    for i in range(0,x):
        for j in range(0,y):
            color=a.get_at((i,j))
            a.set_at((i,j),(255-color[0],255-color[1],255-color[2]))
        proc=((i+1)*y)//proc1
        label['text']=str(proc)+"%"
        root.update()
    label['text'] = "100%"
    root.update()
def black_white(x,y):
    a=pygame.display.set_mode((x,y))
    root = tkinter.Tk()
    label = tkinter.Label(text='0%')
    label.pack()
    global image
    global proc1
    a.blit(image,(0,0))
    pygame.display.update()
    for i in range(0,x):
        for j in range(0,y):
            color = a.get_at((i, j))
            t=(color[0]+color[1]+color[2])//3
            a.set_at((i, j), (t,t,t))
        proc = ((i+1) * y) // proc1
        label['text'] = str(proc) + "%"
        root.update()
    label['text'] = "100%"
    root.update()
def piksel(x,y):
    pygame.display.quit()
    global image
    global proc1
    l=int(input("на сколько пикселей будет 1 пиксель?"))
    a=pygame.display.set_mode((x,y))
    a.blit(image, (0, 0))
    pygame.display.update()
    root = tkinter.Tk()
    label = tkinter.Label(text='0%')
    label.pack()
    e=x
    r=y
    for i in range(0, e, l):
        for j in range(0, r, l):
            b = []
            R = 0
            B = 0
            G = 0
            for k in range(i, i + l):
                for n in range(j, j + l):
                    try:
                        m = a.get_at((k, n))
                        b.append(m)
                        R += m[0]
                        G += m[1]
                        B += m[2]
                    except:
                        pass
            if e - i >= l and r - j >= l:
                R //= l * l
                B //= l * l
                G //= l * l
            elif e - i >= l:
                R //= l * (r - j)
                B //= l * (r - j)
                G //= l * (r - j)
            elif r - j >= l:
                R //= (e - i) * l
                B //= (e - i) * l
                G //= (e - i) * l
            else:
                R //= (e - i) * (r - j)
                B //= (e - i) * (r - j)
                G //= (e - i) * (r - j)
            for k in range(i, i + l):
                for n in range(j, j + l):
                    try:
                        a.set_at((k, n), (R, G, B))
                    except:
                        pass
        proc = ((i + 1) * y) // proc1
        label['text'] = str(proc) + "%"
        root.update()
    label['text'] = "100%"
    root.update()
import pygame

import tkinter

image_name=input("Введите название изображения, которое нужно отредактировать:")
try:
    image = pygame.image.load(image_name)
except:
    print("Такого файла не существует!")
else:
    x=-1
    y=-1
    w=str(image)
    e=''
    for i in range(9,len(w)-5):
        if w[i]=="x":
            if x==-1:
                x=int(e)
            elif y==-1:
                y=int(e)
            e = ''
        else:e+=w[i]
    proc1=x*y//100
    a=pygame.display.set_mode((1000,500))
    game.write(a, "что вы хотите сделать с этим изображением?", (255, 255, 255), (10, 10), 50)
    commands=['инверсия','черно белый','пиксельная']
    for i in range(50,500,50):
        pygame.draw.line(a,(255,255,255),(0,i),(1000,i))
    for i in range(len(commands)):
        game.write(a,commands[i],(255,255,255),(10,i*50+110),50)
    pygame.display.update()
    h=1
    while h:
        for event in pygame.event.get():
            if event.type==pygame.MOUSEBUTTONDOWN:
                pos=game.mouse_pos()
                h=0
                if 100<pos[1]<150:
                    inversia(x,y)
                elif 150<pos[1]<200:
                    black_white(x,y)
                elif 200<pos[1]<250:
                    piksel(x,y)
                else:
                    h=1
    pygame.display.update()
    pygame.image.save(a,input("под каким названием вы хотите сохранить это изображение:"))
