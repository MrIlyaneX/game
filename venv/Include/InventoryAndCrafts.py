import pygame
import random
import game
from threading import Thread
#import GUI

pygame.init()
a=pygame.display.set_mode((1250,626))

# словарь inventory- инвентарь игрока (рюкзак)
# словарь materials- характеристика материала(свойства)
# элементы массива по порядку: прочность, температура плавления, сложность обработки, % появления(вероятность спавна)
materials = {'gold'     : '3,800,4,0' ,   'platinum'   :  '5,300,5,0' ,
		    'metall_3'  : '1,500,1,0',    'iron'       :  '3,1000,2,0' ,
		    'metall_5'  : '5,1500,3,0',   'metall_6'   :  '7,3000,7,0' ,
		    'metall_7'  : '8,4500,8,0' ,  'metall_8'   :  '9,6000,9,0',
		    'sounder'   : '10,9500,10,0',
            'oak'       : 'ничего нет'
            }
# словарь ниже содержит численные данные об инвентаре игрока (точнее: кол-во каждого вида предметов(всех существующих)
inventory = {'gold'      : 0,   'platinum'   :  3,
		     'metall_3'  : 0,   'iron'       :  0,
		     'metall_5'  : 0,   'metall_6'   :  0,
		     'metall_7'  : 0,   'metall_8'   :  0,
		     'sounder'   : 3,
             #виды дерева
             'oak'     : 0,   'dark_oak'   :  0,
             'birch'   : 0,
             #рукоятки мечей(и прочего)
             'oak_wooden_handle'   : 0, 'dark_oak_wooden_handle' : 0,
             'birch_wooden_handle' : 0,
             'iron_handle'         : 0,
             'sounder_handle'      : 0, 'plat_sounder_handle' : 0
            }



def crafts():
    while 1>0:
        witch_craft = 0
        if witch_craft == 0:
            print("0 деревянный (по 4 на рукоять)")
            print("1 железные (3 слитка)")
            print("2 звуковые (3 слитка)")
            print("3 драгоценные (2 слитка платина + 2 слитка звуковика)")
            type = int(input())
            if type == 0:
                # деревянная(4)
                print("0 дуб (4 дуба)")
                print("1 темный дуб (4 темного дуба")
                print("2 береза (4 березы")
                type = int(input())
                if type == 0 and inventory['oak'] >= 4:
                    inventory['oak_wooden_handle'] += 1
                    inventory['oak'] -= 4
                    print("изготовлено!")
                elif type == 1 and inventory['dark_oak'] >= 4:
                    inventory['dark_oak_wooden_handle'] += 1
                    inventory['dark_oak'] -= 4
                    print("изготовлено!")
                elif type == 2 and inventory['birch'] >= 4:
                    inventory['birch_wooden_handle'] += 1
                    inventory['birch'] -= 4
                    print("изготовлено!")
                else:
                    print("недостаточно ресурсов! (или не верный выбор) ")
            elif type == 1:
                # металлическая(3)
                if inventory['iron'] >= 3:
                    inventory['iron_handle'] += 1
                    inventory['iron'] -= 3
                    print("изготовлено!")
                else:
                    print("недостаточно ресурсов! ")
            elif type == 2:
                # звуковая(3)
                if inventory['sounder'] >= 2:
                    inventory['plat_sounder_handle'] += 1
                    inventory['sounder'] -= 2
                    print("изготовлено!")
                else:
                    print("недостаточно ресурсов! ")
            elif type == 3:
                # платиновая + звуковик (2 + 2)
                if inventory['sounder'] >= 2 and inventory['platinum'] >= 2:
                    inventory['plat_sounder_handle'] += 1
                    inventory['sounder'] -= 2
                    inventory['platinum'] -= 2
                    print("изготовлено!")
                else:
                    print("недостаточно ресурсов! ")
        # рукояти
        elif witch_craft == 1:
            a = a
            a -= 1
        # adsa
        elif witch_craft == 2:
            a = a
            eg
        #
        elif witch_craft == 3:
            a = se
            fsd
        #
        elif witch_craft == 4:
            a = a
            fesf
        #

def inventory():
    print("выберите: ")
    print("1 крафты: ")
    print("2 рюкзак: ")
    q = int(input())
    if q == 1:
        print("Выберите тип")
        print("0 рукояти: ")
        q = int(input())
        crafts(q)
    elif q == 2:
        print("ваши ресурсы: (словарь)")
        print(inventory)