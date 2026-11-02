import pygame
import sys
import random
import math
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1000, 500))
stopwatch = 0
mousedown = False

zoom = 1

bomb = []
# [x, y, xx, yy, timer (500 = no countdown, 499 = -1 each tick, flashing at 30-60, 130-160, ...)]
block = [[]]
# [x, y, xx, yy]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill((100, 100, 255))
    mousex, mousey = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
        mousedown = True
    if event.type == pygame.MOUSEBUTTONUP:
        mousedown = False
    stopwatch += 1

    for cat in range(0, len(block)):
        pygame.draw.rect(screen, )

    pygame.display.flip()
    clock.tick(100)