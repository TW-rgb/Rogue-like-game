#various imports
import struct
import time
import pygame
import math
import socket
#handling multiple things at once.
import threading

#player class
class Player:
    def __init__(self ,Hp ,Mp ,Strength ,Speed ,Defense ,Intellgence ,inventory ,level ,user_class ,x ,y ,bullet):
        self.Hp
        #hp points, depends on user_class
        self.Mp
        #attacks - from mp for magecraft
        self.Strength
        #base damage, depends on user_class
        self.Speed
        #base speed, depends on user_class
        self.Defense
        #damage reduction
        self.Intellgence
        #changes magic damage, base increase depends on user_class
        self.inventory
        #pulls items from dungeon, effects(boomerang gun, ice effect, idk)
        self.level
        #scales exponetly with higher levels, randomized xp requirement but still exponetial
        self.user_class
        #picks at beggining of game
        self.x
        #location x
        self.y
        #location y
        self.bullet
        #sub classes - bullet speed, bullet size, bullet path(boomerang type shish), bullet effects



# starting variables
x = 32
y = 32
#box x axis and y axis
boxy = 0
boxx = 0
#for floors
x_floor2 = 0
y_floor2 = 0
floor_running = True
#idk
counter = 1
#wall Score
wall_score = 10

pygame.init()
#images
screen = pygame.display.set_mode((640,640))
floor = pygame.image.load('Grassfloor1.png')
floor2 = pygame.image.load('Grassfloor2.png')
#basic start stuff
running = True
clock = pygame.time.Clock()

# list
platforms = [
]
floors = [
]

#functions
def blitall(listyss):
    for II in listyss:
        pygame.draw.rect(screen, (255,0,0), II, 10)

# screen size math
player = pygame.Rect(x,y,50,50)
boxes = screen.width/50

#the actual game
while running:


    #player
    player = pygame.Rect(x,y,32,32)
    # player end
    #wall code
    if counter == 1:
        while screen.height > boxy >= 0:
            platforms.append(pygame.Rect(boxx,boxy,32,32))
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
            platforms.append(pygame.Rect(boxx,boxy,32,32))
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
            platforms.append(pygame.Rect(boxx,boxy,32,32))
            boxy -= 32
            print("check A2")
            print(boxy)
            print(boxx)
        boxy = 0
        while screen.width > boxx >= 0:
            platforms.append(pygame.Rect(boxx,boxy,32,32))
            boxx -= 32
            print("check b2")
            print(boxy)
            print(boxx)
        counter = 0
    for platform in platforms:
        pygame.draw.rect(screen, (255,0,0), platform, 10)
    #wall code end
    # floor code start
    #floor code for x axis
    if x_floor2 < 641:
        screen.blit(floor2, (x_floor2, y_floor2))
        x_floor2 += 32
        print("floor2")
    #floor code to move down 32
    if x_floor2 > 608:
        screen.blit(floor, (x_floor2, y_floor2))
        x_floor2 = 0
        y_floor2 += 32
    #resets floor code to beggiing
    if y_floor2 > 640 and x_floor2 > 640:
        y_floor2 = 32
        x_floor2 = 32

    # floor code end
    # begging of the drawing process
    blitall(platforms)
    blitall(floors)
    pygame.draw.rect(screen, (0,255,0), player, 2)
    # ending
    #gets key presses single cuz 32 bit system
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            #debug mode
            if event.key == pygame.K_d:
                if debug_mode == True:
                    debug_mode = False
                elif debug_mode == False:
                    debug_mode = True
            #movement for y axis
            if event.key == pygame.K_UP:
                y -= 32
            if event.key == pygame.K_DOWN:
                y += 32
            #movement for x axis
            if event.key == pygame.K_LEFT:
                x -= 32
            if event.key == pygame.K_RIGHT:
                x += 32
            #quit button
            if event.type == pygame.QUIT:
                running = False
            #wall code up
            if x < 32:
                x = 32
                print("you hit a wall")
                wall_score -= 1
            #wall code down
            if x > 608:
                x = 608
                print("you hit a wall")
                wall_score -= 1
            #wall code left side
            if y < 32:
                y = 32
                print("you hit a wall")
                wall_score -= 1
            #wall code right side
            if y > 608:
                y = 608
                print("you hit a wall")
                wall_score -= 1
    #prints wall score/score
    print(wall_Score)
    clock.tick(60)
    pygame.display.flip()
pygame.quit()
