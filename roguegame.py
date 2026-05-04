#random imports that we might need idk
import struct
import time
import pygame
import math
import socket
import threading
import random


class Player:
    def __init__(self ,Hp ,Mp ,Strength ,Speed ,Defense ,Intellgence ,inventory ,level):
        self.Hp = Hp
        #hp points, depends on user_class
        self.Mp = Mp
        #attacks - from mp for magecraft
        self.Strength = Speed
        #base damage, depends on user_class
        self.Speed = Speed
        #base speed, depends on user_class
        self.Defense = Defense
        #damage reduction
        self.Intellgence = Int
        #changes magic damage, base increase depends on user_class
        self.inventory = []
        #pulls items from dungeon, effects(boomerang gun, ice effect, idk)
        self.level = 1
        #scales exponetly with higher levels, randomized xp requirement but still exponetial

Mage = Player(Hp ,Mp ,Strength ,Speed ,Defense ,Intellgence ,inventory ,1)
# items
common = ["Broken knife", ]
Broken knife
uncommon = []
rare = []
epic = []
legebdary = []
unique = []

# starting variables
x = 32
y = 32
boxy = 0
boxx = 0
floorx = 32
floory = 32
newroom = 1
debug_mode = False
enemycount = 2
run = True
health = 10
enemie_x = 608
enemie_y = 608
pygame.init()
screen = pygame.display.set_mode((640,640))
running = True
clock = pygame.time.Clock()
firstime = 1

# list
walls = [
]
textures = [
]
floors = [
]
floortextures = [
]
enemys = [
]
enemytextures = [
]
#functions
def blitall(listyss):
    for II in listyss:
        pygame.draw.rect(screen, (255,0,0), II, 10)

# screen size math
player = pygame.Rect(x,y,32,32)
boxes = screen.width/50

#the actual game
while running:
    run = True
    #player    # player end
    #wall code
    if newroom == 1:
        while screen.height > boxy >= 0:
            walls.append(pygame.Rect(boxx,boxy,32,32))
            boxy += 32
            print("check A")
            print(boxy)
            print(boxx)
        while boxy == screen.height:
            boxy -= 32
            print("check A-b")
            print(boxy)
            print(boxx)
        while screen.width > boxx >= 0:
            walls.append(pygame.Rect(boxx,boxy,32,32))
            boxx += 32
            print("check b")
            print(boxy)
            print(boxx)
        while boxx == screen.width:
            boxx -= 32
            print("check A-b2")
            print(boxy)
            print(boxx)
        while screen.height > boxy >= 0:
            walls.append(pygame.Rect(boxx,boxy,32,32))
            boxy -= 32
            print("check A2")
            print(boxy)
            print(boxx)
        boxy = 0
        while screen.width > boxx >= 0:
            walls.append(pygame.Rect(boxx,boxy,32,32))
            boxx -= 32
            print("check b2")
            print(boxy)
            print(boxx)
    #wall code end
    # floor code start
    while floory < screen.height and newroom == 1:
        floors.append(pygame.Rect(floorx, floory, 32,32))
        floory += 32
        while floorx < screen.width and floory == screen.height-32 and floorx != screen.width-32:
            floorx += 32
            floory = 32
        if floorx == screen.width -32:
            floory = 9999
    # floor code end
    # begging of the drawing process
    if newroom == 1:
        for wall in walls:
            texture = random.randint(1,3)
            print(texture)
            boxx = wall.x
            boxy = wall.y
            if texture == 1:
                platformimage = pygame.image.load('tree1.png')
            if texture == 2:
                platformimage = pygame.image.load('tree2.png')
            if texture == 3:
                platformimage = pygame.image.load('tree3.png')
            textures.append(platformimage)
            screen.blit(platformimage, (boxx,boxy))
        for floor in floors:
            texture = random.randint(1,3)
            print(texture)
            floorx = floor.x
            floory = floor.y
            if texture == 1:
                floortexture = pygame.image.load('Grassfloor1.png')
            if texture == 2:
                floortexture = pygame.image.load('Grassfloor2.png')
            if texture == 3:
                floortexture = pygame.image.load('Daisy1.png')
            floortextures.append(floortexture)
            screen.blit(floortexture, (floorx, floory))
    # new enemy generation
    while enemycount > 0:
        enemie_x = random.randrange(0,640,32)
        enemie_y = random.randrange(0,640,32)
        print(enemie_y)
        print(enemie_x)
        enemys.append(pygame.Rect(enemie_x, enemie_y,32,32))
        enemycount -= 1
    for enemy in enemys:
        #texture = random.randint(1,3)
        #print(texture)
        enemie_x = enemy.x
        enemie_y = enemy.y
        #if texture == 1:
            #platformimage = pygame.image.load('tree1.png')
        #if texture == 2:
            #platformimage = pygame.image.load('tree2.png')
        #if texture == 3:
            #platformimage = pygame.image.load('tree3.png')
        enemyimage = pygame.image.load('skelly(D).png')
        enemytextures.append(enemyimage)
        screen.blit(enemyimage, (enemie_x,enemie_y))
    if debug_mode == True:
        for wall in walls:
            pygame.draw.rect(screen, (255,0,0), wall, 2)
    # end of room/enemu generation
    if newroom == 1:
        newroom = 0
    #enemy MOVEMENT
    for index, enemy in enumerate(enemys):
        enemie_x = enemy.x
        enemie_y = enemy.y
        # RIGHT MOVEMENT
        if x > enemie_x:
            enemie_x += 32
            enemys[index] = pygame.Rect(enemie_x, enemie_y,32,32)
            if enemy.colliderect(player):
                health -= 1
                print(health)
                enemie_x -= 32
            for otherenemy in enemys:
                if otherenemy == enemy:
                    continue
                if enemy.colliderect(otherenemy):
                    enemie_x -= 32
        # LEFT MOVEMENT
        elif x < enemie_x:
            enemie_x -= 32
            enemys[index] = pygame.Rect(enemie_x, enemie_y,32,32)
            if enemy.colliderect(player):
                health -= 1
                print(health)
                enemie_x += 32
            for otherenemy in enemys:
                if otherenemy == enemy:
                    continue
                if enemy.colliderect(otherenemy):
                    enemie_x += 32
        # UP MOVEMENT
        elif y < enemie_y:
            enemie_y -= 32
            enemys[index] = pygame.Rect(enemie_x, enemie_y,32,32)
            if enemy.colliderect(player):
                health -= 1
                print(health)
                enemie_y += 32
            for otherenemy in enemys:
                if otherenemy == enemy:
                    continue
                if enemy.colliderect(otherenemy):
                    enemie_y += 32
        # DOWN MOVEMENT
        elif y > enemie_y:
            enemie_y += 32
            enemys[index] = pygame.Rect(enemie_x, enemie_y,32,32)
            if enemy.colliderect(player):
                health -= 1
                print(health)
                enemie_y -= 32
            for otherenemy in enemys:
                if otherenemy == enemy:
                    continue
                if enemy.colliderect(otherenemy):
                    enemie_y -= 32
    #rendering
    for wall, platformimage in zip(walls, textures):
        boxx = wall.x
        boxy = wall.y
        screen.blit(platformimage, (boxx,boxy))
    for floor, floortexture in zip(floors, floortextures):
        floorx = floor.x
        floory = floor.y
        screen.blit(floortexture, (floorx, floory))
    for enemy, enemyimage in zip(enemys, enemytextures):
        enemie_x = enemy.x
        enemie_y = enemy.y
        screen.blit(enemyimage, (enemie_x,enemie_y))

#for debug mode it shows the hit boxxes
    if debug_mode == True:
        for wall in walls:
            pygame.draw.rect(screen, (255,0,0), wall, 2)
    # end of room generation
    if newroom == 1:
        newroom = 0
     # controls
    waiting =1
    if firstime == 1:
        firstime = 0
        waiting = 0
        print("click arrows to begin")
    while waiting == 1:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                #debug mode with one button
                if event.key == pygame.K_d:
                    waiting = 0
                    #if debug modes on its sets it to off
                    if debug_mode == True:
                        debug_mode = False
                            #if debug modes off its sets it to on
                    elif debug_mode == False:
                        debug_mode = True
                            #moves the player left 32
                if event.key == pygame.K_UP:
                    waiting = 0
                    y -= 32
                    player = pygame.Rect(x,y,32,32)
                    for wall in walls:
                            #detects if player hits a wall
                        if player.colliderect(wall):
                            y +=32
                            print("hit wall")
                                #moves the player down 32
                if event.key == pygame.K_DOWN:
                    waiting = 0
                    y += 32
                    player = pygame.Rect(x,y,32,32)
                    for wall in walls:
                            #detects if player hits a wall
                        if player.colliderect(wall):
                            y -=32
                            print("hit wall")
                            #moves the player left 32
                if event.key == pygame.K_LEFT:
                    waiting = 0
                    x -= 32
                    player = pygame.Rect(x,y,32,32)
                    for wall in walls:
                            #detects if player hits a wall
                        if player.colliderect(wall):
                            x +=32
                            print("hit wall")
                            #moves the player right 32
                if event.key == pygame.K_RIGHT:
                    waiting = 0
                    x += 32
                    player = pygame.Rect(x,y,32,32)
                    #detects if player hits a wall
                    for wall in walls:
                        if player.colliderect(wall):
                            x -=32
                            print("hit wall")
                        #ends game
                if event.type == pygame.QUIT:
                    waiting = 0
                    running = False
#special character loading to avoid delay
    player = pygame.Rect(x,y,32,32)
    pygame.draw.rect(screen, (0,255,0), player, 2)

#tick rate and prints it to screen
    clock.tick(60)
    pygame.display.flip()
pygame.quit()
