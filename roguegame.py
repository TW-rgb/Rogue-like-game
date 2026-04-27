import struct
import time
import pygame
import math
import socket
import threading


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

x = 32
y = 32
boxy = 0
boxx = 0
x_floor = 32
y_floor = 32
floor_running = True
pygame.init()
screen = pygame.display.set_mode((640,640))
floor = pygame.image.load('Grassfloor1.png')
floor2 = pygame.image.load('Grassfloor2.png')
running = True
clock = pygame.time.Clock()
platforms = [
]
player = pygame.Rect(x,y,50,50)
boxes = screen.width/50
counter = 1
while running:
    player = pygame.Rect(x,y,32,32)
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
    while x_floor < 608:
        screen.blit(floor, (x_floor, y_floor))
        x_floor += 32
        y_floor = 32
    while y_floor < 608:
        screen.blit(floor2, (x_floor, y_floor))
        y_floor += 32
        x_floor = 32
    for platform in platforms:
        pygame.draw.rect(screen, (255,0,0), platform, 10)
    pygame.draw.rect(screen, (0,255,0), player, 2)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                if debug_mode == True:
                    debug_mode = False
                elif debug_mode == False:
                    debug_mode = True
            if event.key == pygame.K_UP:
                y -= 32
            if event.key == pygame.K_DOWN:
                y += 32
            if event.key == pygame.K_LEFT:
                x -= 32
            if event.key == pygame.K_RIGHT:
                x += 32
            if event.type == pygame.QUIT:
                running = False
            if x < 32:
                x = 32
                print("you hit a wall")
            if x > 608:
                x = 608
                print("you hit a wall")
            if y < 32:
                y = 32
                print("you hit a wall")
            if y > 608:
                y = 608
                print("you hit a wall")
    clock.tick(60)
    pygame.display.flip()
pygame.quit()
