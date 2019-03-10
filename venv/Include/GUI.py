import pygame
import game
import random
import InventoryAndCrafts as IAC
import sys
from PyQt5.QtWidgets import QDesktopWidget,QApplication
from threading import Thread
import numpy

app = QApplication(sys.argv)
q= QDesktopWidget().availableGeometry()
run = True
height = q.height()-100
width  = q.width()-100
pygame.init()
a=pygame.display.set_mode((width,height))
pygame.display.set_caption("Game")
s=1
pos = game.mouse_pos()



#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#Важно знать:
#формат данных инвентаря как множества- (название предмета,вес премета,кол-во предметов в инаентаре, урон(если есть), востановление хп,маны,выноса(если есть),тип)
#т.е
#item[0] - название
#item[1] - вес
#item[2] - кол-во
#item[3] - урон
#item[4] - хп
#item[5] - мана
#item[6] - вынос
#item[7] - тип(0 - ничего, 1 - легкие, 2 - тяжелые)
#
#
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

#для инвентарь
character_inventory = []
character_inventory_weight = 0

#картинки
backpack_surf = pygame.image.load('C:/Users/HOME/PycharmProjects/game/venv/icons/backpack.jpg')
backpack_rect = backpack_surf.get_rect(bottomright=(width-240, height))
map_surf = pygame.image.load('C:/Users/HOME/PycharmProjects/game/venv/icons/map.jpg')
map_rect = map_surf.get_rect(bottomright=(width-120, height))
besteary_surf = pygame.image.load('C:/Users/HOME/PycharmProjects/game/venv/icons/besteary.jpg')
besteary_rect = besteary_surf.get_rect(bottomright=(width-80, height))
settings_surf = pygame.image.load('C:/Users/HOME/PycharmProjects/game/venv/icons/settings.jpg')
settings_rect = settings_surf.get_rect(bottomright=(width, height))
#железный сет номер 1
iron_helmet_surf = pygame.image.load('C:/Users/HOME/PycharmProjects/game/venv/icons/iron_helmet.jpg')
#locations
#trees
tree1_surf = pygame.image.load('C:/Users/HOME/PycharmProjects/game/venv/icons/tree1.png')
tree1_rect = tree1_surf.get_rect(bottomright=(500, 500))
tree2_surf = pygame.image.load('C:/Users/HOME/PycharmProjects/game/venv/icons/tree2.png')
tree2_rect = tree2_surf.get_rect(bottomright=(500, 500))
#swamp_surf = pygame.image.load('C:/Users/HOME/PycharmProjects/game/venv/icons/swamp.jpg')
#swamp_rect = swamp_surf.get_rect(bottomright=(width-200, height+3))

#цвета
WHITE = (255, 255, 255)
RED = (225, 0, 50)
GREEN = (0, 225, 0)
BLUE = (0, 0, 225)
BLACK = (0, 0, 0)
BROWN = (165, 42, 42)
#
step_size = 10
#отвечают за открытие\закрытие окoн
inventory_bool = False
map_bool       = False
settings_bool  = False
besteary_bool  = False
character_bool = False
craftbook_bool = False
skill_bool     = False
top_bool       = False

# основные параметры
mana        = 100
healpoints  = 100
strongpower = 100

mana1 = mana
healpoints1 = strongpower
strongpower1 = healpoints

#стандартный показатель силы в дальнем, ближнем боях, магии и отхила
power_in_bow_attack = 0
power_in_sword_attack = 0
power_in_magick_attack = 0
power_in_heal_attack = 0

#параметры (перемножение обычного урона на значение крит урона)
krirical_bow_attack = 0.5
krirical_sword_attack = 0.5
krirical_magick_attack = 0.5
krirical_heal_attack = 0.5
#шанс критической атаки (выбор крит/не крит по рандому)
chance_of_krirical_bow_attack = 50
chance_of_krirical_sword_attack = 50
chance_of_krirical_magick_attack = 50
chance_of_krirical_heal_attack = 50
#доп сила умения (процент -> обычный-100 при 0.10(т.е миниму=1 потом по увеличение) обычный станет 110)
dop_percent_of_bow_attack = 1
dop_percent_of_sword_attack = 1
dop_percent_of_magick_attack = 1
dop_percent_of_heal_attack = 1
#защитные характеристики
defence = 0     #защита(физ урон)
resistance = 0  #сопротивление(маг урон)

phis_blocking = 0 #блокирование (при ношении персонажем щита) физ урона
magic_blocking = 0 #блокирование маг урона
evasion = 0  #уклонение
parry = 0    #парирование
#resilience-устойчивость
resilience_sword = 1 #устойчивость к ближнему бою
resilience_bow = 1   #устойчивость к дальнему бою
resilience_magic = 1 #как хил(если врог хил) так и магия
resilience_pvp = 1   #устойчивость к пвп атакам(против игроков)
resilience_pve = 1   #устойчивость к пве атакам(протмв мобов)
resilience_siege = 1 #устойчивость к осадному урону
#типо фпс
clock = pygame.time.Clock()



def lobby():
    global a, s, pos
    global inventory_bool, besteary_bool, settings_bool, map_bool, character_bool, top_bool, skill_bool, craftbook_bool
    global mana, strongpower, healpoints, mana1, strongpower1, healpoints1
    while run:
        clock.tick(120)
        pos = game.mouse_pos()
        s = pos
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if width - 320 <= pos[0] <= width - 280 and height - 40 <= pos[1] <= height:
                    if character_bool == True:
                        character_bool = False
                    else:
                        character_bool = True
                elif width - 280 <= pos[0] <= width - 240 and height - 40 <= pos[1] <= height:
                    if inventory_bool == True:
                        inventory_bool = False
                    else:
                        inventory_bool = True
                elif width - 240 <= pos[0] <= width - 200 and height - 40 <= pos[1] <= height:
                    if skill_bool == True:
                        skill_bool = False
                    else:
                        skill_bool = True
                elif width - 200 <= pos[0] <= width - 160 and height - 40 <= pos[1] <= height:
                    if craftbook_bool == True:
                        craftbook_bool = False
                    else:
                        craftbook_bool = True
                elif width - 160 <= pos[0] <= width - 120 and height - 40 <= pos[1] <= height:
                    if map_bool == True:
                        map_bool = False
                    else:
                        map_bool = True
                elif width - 120 <= pos[0] <= width - 80 and height - 40 <= pos[1] <= height:
                    if besteary_bool == True:
                        besteary_bool = False
                    else:
                        besteary_bool = True
                elif width - 80 <= pos[0] <= width - 40 and height - 40 <= pos[1] <= height:
                    if top_bool == True:
                        top_bool = False
                    else:
                        top_bool = True
                elif width - 40 <= pos[0] <= width and height - 40 <= pos[1] <= height:
                    if settings_bool == True:
                        settings_bool = False
                    else:
                        settings_bool = True
                #с клавы
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    if map_bool == True:
                        map_bool = False
                    else:
                        map_bool = True
                if event.key == pygame.K_n:
                    if besteary_bool == True:
                        besteary_bool = False
                    else:
                        besteary_bool = True
                if event.key == pygame.K_ESCAPE:
                    if settings_bool == True:
                        settings_bool = False
                    else:
                        settings_bool = True
                if event.key == pygame.K_i:
                    if character_bool == True:
                        character_bool = False
                    else:
                        character_bool = True
                if event.key == pygame.K_u:
                    if inventory_bool == True:
                        inventory_bool = False
                    else:
                        inventory_bool = True
                if event.key == pygame.K_h:
                    if top_bool == True:
                        top_bool = False
                    else:
                        top_bool = True
                if event.key == pygame.K_j:
                    if skill_bool == True:
                        skill_bool = False
                    else:
                        skill_bool = True
                if event.key == pygame.K_k:
                    if craftbook_bool == True:
                        craftbook_bool = False
                    else:
                        craftbook_bool = True
                if event.key == pygame.K_1:
                    skills(1)
                if event.key == pygame.K_2:
                    skills(2)
                if event.key == pygame.K_3:
                    skills(3)
                if keys[pygame.K_q]:
                    skills(4)
                if keys[pygame.K_e]:
                    skills(5)
                if event.key == pygame.K_x:
                    skills(6)
                if event.key == pygame.K_c:
                    skills(7)
                if event.key == pygame.K_f:
                    skills(8)
                if event.key == pygame.KMOD_SHIFT and event.key == pygame.q:
                    skills(9)
                elif event.key == pygame.KMOD_SHIFT and event.key == pygame.e:
                    skills(10)
                elif event.key == pygame.K_CAPSLOCK:
                    skills(11)
            if keys[pygame.K_q]:
                skills(4)
            if keys[pygame.K_e]:
                skills(5)
        GR = Thread(name="GR", target=graf(), args=(a, 10))
        GR.start()
        GR.join()


#снизу отвечает за отрисовку
def graf():
    global a, s, pos, run
    global inventory_bool, besteary_bool, settings_bool, map_bool, character_bool, top_bool, skill_bool, craftbook_bool
    global mana, strongpower, healpoints, mana1, strongpower1, healpoints1
    pos = game.mouse_pos()
    s = pos
    pygame.draw.rect(a, WHITE, (0, 0, width, height))
    tree1_rect = tree1_surf.get_rect(bottomright=(500, 500))
    a.blit(tree1_surf, tree1_rect)
    tree1_rect = tree1_surf.get_rect(bottomright=(1000, 400))
    a.blit(tree1_surf, tree1_rect)
    tree2_rect = tree2_surf.get_rect(bottomright=(700, 600))
    a.blit(tree2_surf, tree2_rect)

    # настройки->характеристики перса
    if 1 + 1 == 2:
        a.blit(settings_surf, settings_rect)
        pygame.draw.rect(a, BLACK, (width - 80, height - 40, 40, 40))
        a.blit(besteary_surf, besteary_rect)
        a.blit(map_surf, map_rect)
        pygame.draw.rect(a, BLACK, (width - 200, height - 40, 40, 40))
        pygame.draw.rect(a, BLACK, (width - 240, height - 40, 40, 40))
        a.blit(backpack_surf, backpack_rect)
        pygame.draw.rect(a, BLACK, (width - 320, height - 40, 40, 40))
        game.write(a, (BLACK), (0, 0), 100, str(s))
    # "окно" активных умений: иконка потом кнопка этой иконки
    if 1 + 1 == 2:
        pygame.draw.rect(a, BLACK, (width - 1180, height - 60, 40, 40), 1)
        game.write(a, BLACK, (width - 1179, height - 35), 20, "1")
        pygame.draw.rect(a, BLACK, (width - 1141, height - 60, 40, 40), 1)
        game.write(a, BLACK, (width - 1140, height - 35), 20, "2")
        pygame.draw.rect(a, BLACK, (width - 1102, height - 60, 40, 40), 1)
        game.write(a, BLACK, (width - 1101, height - 35), 20, "3")
        pygame.draw.rect(a, BLACK, (width - 1063, height - 60, 40, 40), 1)
        game.write(a, BLACK, (width - 1062, height - 35), 20, "q")
        pygame.draw.rect(a, BLACK, (width - 1024, height - 60, 40, 40), 1)
        game.write(a, BLACK, (width - 1023, height - 35), 20, "e")
        pygame.draw.rect(a, BLACK, (width - 985, height - 60, 40, 40), 1)
        game.write(a, BLACK, (width - 984, height - 35), 20, "x")
        pygame.draw.rect(a, BLACK, (width - 946, height - 60, 40, 40), 1)
        game.write(a, BLACK, (width - 945, height - 35), 20, "c")
        pygame.draw.rect(a, BLACK, (width - 907, height - 60, 40, 40), 1)
        game.write(a, BLACK, (width - 906, height - 35), 20, "f")
        pygame.draw.rect(a, BLACK, (width - 868, height - 60, 40, 40), 1)
        game.write(a, BLACK, (width - 867, height - 32), 17, "shift+q")
        pygame.draw.rect(a, BLACK, (width - 829, height - 60, 40, 40), 1)
        game.write(a, BLACK, (width - 828, height - 32), 17, "shift+e")
        pygame.draw.rect(a, BLACK, (width - 790, height - 60, 40, 40), 1)
        game.write(a, BLACK, (width - 789, height - 32), 17, "CAPS")
    # окна
    if inventory_bool == True:
        pygame.draw.rect(a, (BLACK), (width - 600, height - 750, 550, 600))
        game.write(a, WHITE, (width - 600, height - 750), 30, "Рюкзак")
    if besteary_bool == True:
        pygame.draw.rect(a, (BLACK), (width - 600, height - 750, 550, 600))
        game.write(a, WHITE, (width - 600, height - 750), 30, "Бестиарий")
    if settings_bool == True:
        pygame.draw.rect(a, (BLACK), (width - 1200, height - 750, 550, 600))
        game.write(a, WHITE, (width - 1200, height - 750), 30, "Настройки")
    if map_bool == True:
        pygame.draw.rect(a, (BLACK), (width - 800, height - 900, 750, 700))
        game.write(a, WHITE, (width - 800, height - 900), 30, "Карта")
    if character_bool == True:
        pygame.draw.rect(a, (BLACK), (width - 1700, height - 900, 500, 700))
        game.write(a, WHITE, (width - 1700, height - 900), 30, "Персонаж")
    if top_bool == True:
        pygame.draw.rect(a, (BLACK), (width - 1750, height - 900, 1000, 850))
        game.write(a, WHITE, (width - 1750, height - 900), 30, "Рейтинг")
    if skill_bool == True:
        pygame.draw.rect(a, (BLACK), (width - 1250, height - 850, 650, 650))
        game.write(a, WHITE, (width - 1250, height - 850), 30, "Умения")
    if craftbook_bool == True:
        pygame.draw.rect(a, (BLACK), (width - 1400, height - 900, 900, 800))
        game.write(a, WHITE, (width - 1400, height - 900), 30, "Книга рецептов")

    # oтображение хп, маны и выноса(от 07.03.2019 вроде нормальная работа)
    if mana1 < mana:
        if mana1<=0:
            i=0+1
            pygame.draw.rect(a, BLUE, (15, 900, 250 - 249, 15))
        else:
            qw =250 + (250/100)*mana1*(-1)
            pygame.draw.rect(a, BLUE, (15, 900, 250 - qw, 15))
    if healpoints1 < healpoints:
        if healpoints1 <=0:
            run=False
        else:
            qw = 250 + (250 / 100) * healpoints1 * (-1)
            pygame.draw.rect(a, RED, (15, 860, 250 - qw, 15))
    if strongpower1 < strongpower:
        if strongpower1 <=0:
            pygame.draw.rect(a, BROWN, (15, 880, 250 - 249, 15))
        else:
            qw = 250 + (250 / 100) * strongpower1 * (-1)
            pygame.draw.rect(a, BROWN, (15, 880, 250 - qw, 15))
    pygame.display.update()

#
#отрисовка
#GR = Thread(name="GR", target=graf(), args=(a, -10))
#GR.join()
#
#
#
def enchant():
    global a, s
    while 1 > 0:
        pos = game.mouse_pos()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if a == a:
                    s+=1
        pygame.draw.rect(a, (0, 0, 0), (0, 0, 1250, 626))

        pygame.display.update()

def skills(type):
    global s
    if type == 1:   #1
        s += s
    elif type == 2: #2
        s += s
    elif type == 3: #3
        s += s
    elif type == 4: #q
        s += 1
    elif type == 5: #e
        s += 1
    elif type == 6: #x
        s += s
    elif type == 7: #c
        s += s
    elif type == 8: #f
        s += s
    elif type == 9: #shift + q
        s += s
    elif type == 10: #shift + e
        s += s
    elif type == 11: #CAPS
        s += s

class inventory():
    global a, s, pos, character_inventory, character_inventory_weight
    # доработать
    def __add_item__(item):
        global character_inventory_weight, character_inventory
        if len(character_inventory) > 0:
            if item in character_inventory:
                i=0
                while item[0]!=character_inventory[i][0]:
                    i+=1
                character_inventory[i][2]+=1
            # вес предмета
                e = item[1]
                character_inventory_weight += e
            else:
                item[2] = 1
                character_inventory.append(item)
            # вес предмета
                e = item[1]
                character_inventory_weight = character_inventory_weight + e
        else:
            item[2]=1
            character_inventory.append(item)
            e = item[1]
            character_inventory_weight += e
    def __drop_item__(item):
        global character_inventory_weight, character_inventory
        i=0
        while item[0] != character_inventory[i][0]:
            i += 1
        character_inventory_weight-=item[1]
        character_inventory.pop(i)
    def __use__(item):
        #в процессе
        r = 0
    def sroll():
        print("вес", character_inventory_weight)

sword = ['sword', 10, 0, 7,0,0,0,0]
stack = ['stack', 120, 0, 0, 0, 0, 0, 0]
inventory.__add_item__(sword)
inventory.__add_item__(stack)
inventory.__add_item__(sword)
inventory.sroll()
print(character_inventory)
inventory.__drop_item__(stack)
inventory.sroll()
print(character_inventory)
#graf()
lobby()
#GR = Thread(name="GR", target=graf(), args=(a, -10))
#GR.start()
#GR.join()