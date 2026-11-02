import pygame
import math
import sys
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1000,500))
stopwatch = 0
mousedown = False
stuf = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

#variables for game

#x, y, x - vector/velocity, y - same thing
tank = [0, 0, 0, 0]
#x - start, y - start, degrees, thiccness, reload, reloading, bullet speed, bullet damage
turret = []
#x, y, x - vector/velocity, y - same thing, size, damage
bullet = []

movingup = False
movingdown = False
movingright = False
movingleft = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                movingup = True
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                movingleft = True
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                movingdown = True
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                movingright = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                movingup = False
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                movingleft = False
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                movingdown = False
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                movingright = False

    tank[0] += tank[2]
    tank[1] += tank[3]

    if movingdown == True:
        tank[3]

    mousex, mousey = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
        mousedown = True
    if event.type == pygame.MOUSEBUTTONUP:
        mousedown = False
    screen.fill((225, 225, 225))
    stopwatch += 1

    clock.tick(100)
    pygame.display.flip()