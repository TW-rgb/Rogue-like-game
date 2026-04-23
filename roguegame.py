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

x = 50
y = 50
boxy = 0
boxx = 0
background = pygame.image.load('checker.jpg')
pygame.init()
screen = pygame.display.set_mode((600,600))
running = True
clock = pygame.time.Clock()
platforms = [
]
player = pygame.Rect(x,y,50,50)
boxes = screen.width/50
boxupdown = boxes*3
boxleftright = boxes
while running:
    screen.blit(background,(0,0))
    player = pygame.Rect(x,y,50,50)
    pygame.draw.rect(screen, (0,255,0), player, 2)
    if boxes > 0:
        if boxes < boxupdown and boxleftright < boxupdown :
            platforms.append(pygame.Rect(boxx,boxy,50,50))
            boxy += 50
            #time.sleep(1)
            boxupdown -= 1
            boxleftright += 1
            print(boxleftright,"A")
            print(boxupdown,"A")
        if boxleftright == boxupdown:
            boxupdown = boxupdown - boxes
            boxleftright = boxleftright + boxes
            boxy -= 50
            print(boxleftright,"b")
            print(boxupdown,"b")
        if boxes < boxleftright and boxleftright > boxupdown:
            platforms.append(pygame.Rect(boxx,boxy,50,50))
            boxx += 50
            #time.sleep(1)
            boxupdown += 1
            boxleftright -= 1
            print(boxleftright,"c")
            print(boxupdown,"c")
    for platform in platforms:
        pygame.draw.rect(screen, (255,0,0), platform, 10)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                if debug_mode == True:
                    debug_mode = False
                elif debug_mode == False:
                    debug_mode = True
            if event.key == pygame.K_UP:
                y -= 50
            if event.key == pygame.K_DOWN:
                y += 50
            if event.key == pygame.K_LEFT:
                x -= 50
            if event.key == pygame.K_RIGHT:
                x += 50
            if event.type == pygame.QUIT:
                running = False

    clock.tick(60)
    pygame.display.flip()
pygame.quit()
