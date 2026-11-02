import pygame

import sys

import time

screen1 = 0
screen2 = 255
screen3 = 0

screen1_switch = "up"
screen2_switch = "down"
screen3_switch = "up"

bullet1x = 1
bullet1y = 1
bullet1 = "no"
bullet1xx = 4
bullet1yy = 3
bullet2x = 1
bullet2y = 1
bullet2 = "no"
bullet2xx = 2
bullet2yy = 4
bullet3x = 1
bullet3y = 1
bullet3 = "no"
bullet3xx = 3
bullet3yy = 2
bullet4x = 1
bullet4y = 1
bullet4 = "no"
bullet4xx = 2
bullet4yy = 3
bullet5x = 1
bullet5y = 1
bullet5 = "no"
bullet5xx = 2
bullet5yy = 4
bullet6x = 1
bullet6y = 1
bullet6 = "no"
bullet6xx = 5
bullet6yy = 2
bullet7x = 1
bullet7y = 1
bullet7 = "no"
bullet7xx = 3
bullet7yy = 3
bullet8x = 1
bullet8y = 1
bullet8 = "no"
bullet8xx = 1
bullet8yy = 4
bullet9x = 1
bullet9y = 1
bullet9 = "no"
bullet9xx = 3
bullet9yy = 2
bullet10x = 1
bullet10y = 1
bullet10 = "no"
bullet10xx = 2
bullet10yy = 3
bullet11x = 1
bullet11y = 1
bullet11 = "no"
bullet11xx = 3
bullet11yy = 4
bullet12x = 1
bullet12y = 1
bullet12 = "no"
bullet12xx = 5
bullet12yy = 2

time1 = 0

clock = pygame.time.Clock()

pygame.init()
font = pygame.font.Font("freesansbold.ttf", 32)
screen = pygame.display.set_mode((1080,540))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    mousex, mousey = pygame.mouse.get_pos()

    if screen1 > 249:
        screen1_switch = "down"
    if screen1 < 5:
        screen1_switch = "up"

    if screen2 > 249:
        screen2_switch = "down"
    if screen2 < 5:
        screen2_switch = "up"

    if screen3 > 249:
        screen3_switch = "down"
    if screen3 < 5:
        screen3_switch = "up"

    if screen1_switch == "up":
        screen1 += 1

    if screen1_switch == "down":
        screen1 -= 3

    if screen2_switch == "up":
        screen2 += 2

    if screen2_switch == "down":
        screen2 -= 3

    if screen3_switch == "up":
        screen3 += 2

    if screen3_switch == "down":
        screen3 -= 1

    screen.fill((screen1, screen2, screen3))

    if time1 == 300:
        bullet1 = "yes"
    if bullet1 == "yes":
        bullet1x += bullet1xx
        bullet1y += bullet1yy
    if bullet1x > 1064:
        bullet1xx = -1*bullet1xx
    if bullet1x < 1:
        bullet1xx = -1*bullet1xx
    if bullet1y > 524:
        bullet1yy = -1*bullet1yy
    if bullet1y < 1:
        bullet1yy = -1*bullet1yy

    if time1 == 320:
        bullet2 = "yes"
    if bullet2 == "yes":
        bullet2x += bullet2xx
        bullet2y += bullet2yy
    if bullet2x > 1064:
        bullet2xx = -1*bullet2xx
    if bullet2x < 1:
        bullet2xx = -1*bullet2xx
    if bullet2y > 524:
        bullet2yy = -1*bullet2yy
    if bullet2y < 1:
        bullet2yy = -1*bullet2yy

    if time1 == 340:
        bullet3 = "yes"
    if bullet3 == "yes":
        bullet3x += bullet3xx
        bullet3y += bullet3yy
    if bullet3x > 1064:
        bullet3xx = -1*bullet3xx
    if bullet3x < 1:
        bullet3xx = -1*bullet3xx
    if bullet3y > 524:
        bullet3yy = -1*bullet3yy
    if bullet3y < 1:
        bullet3yy = -1*bullet3yy

    if time1 == 360:
        bullet4 = "yes"
    if bullet4 == "yes":
        bullet4x += bullet4xx
        bullet4y += bullet4yy
    if bullet4x > 1064:
        bullet4xx = -1*bullet4xx
    if bullet4x < 1:
        bullet4xx = -1*bullet4xx
    if bullet4y > 524:
        bullet4yy = -1*bullet4yy
    if bullet4y < 1:
        bullet4yy = -1*bullet4yy

    if time1 == 380:
        bullet5 = "yes"
    if bullet5 == "yes":
        bullet5x += bullet5xx
        bullet5y += bullet5yy
    if bullet5x > 1064:
        bullet5xx = -1*bullet5xx
    if bullet5x < 1:
        bullet5xx = -1*bullet5xx
    if bullet5y > 524:
        bullet5yy = -1*bullet5yy
    if bullet5y < 1:
        bullet5yy = -1*bullet5yy

    if time1 == 400:
        bullet6 = "yes"
    if bullet6 == "yes":
        bullet6x += bullet6xx
        bullet6y += bullet6yy
    if bullet6x > 1064:
        bullet6xx = -1*bullet6xx
    if bullet6x < 1:
        bullet6xx = -1*bullet6xx
    if bullet6y > 524:
        bullet6yy = -1*bullet6yy
    if bullet6y < 1:
        bullet6yy = -1*bullet6yy

    if time1 == 420:
        bullet7 = "yes"
    if bullet7 == "yes":
        bullet7x += bullet7xx
        bullet7y += bullet7yy
    if bullet7x > 1064:
        bullet7xx = -1*bullet7xx
    if bullet7x < 1:
        bullet7xx = -1*bullet7xx
    if bullet7y > 524:
        bullet7yy = -1*bullet7yy
    if bullet7y < 1:
        bullet7yy = -1*bullet7yy

    if time1 == 440:
        bullet8 = "yes"
    if bullet8 == "yes":
        bullet8x += bullet8xx
        bullet8y += bullet8yy
    if bullet8x > 1064:
        bullet8xx = -1*bullet8xx
    if bullet8x < 1:
        bullet8xx = -1*bullet8xx
    if bullet8y > 524:
        bullet8yy = -1*bullet8yy
    if bullet8y < 1:
        bullet8yy = -1*bullet8yy

    if time1 == 460:
        bullet9 = "yes"
    if bullet9 == "yes":
        bullet9x += bullet9xx
        bullet9y += bullet9yy
    if bullet9x > 1064:
        bullet9xx = -1*bullet9xx
    if bullet9x < 1:
        bullet9xx = -1*bullet9xx
    if bullet9y > 524:
        bullet9yy = -1*bullet9yy
    if bullet9y < 1:
        bullet9yy = -1*bullet9yy

    if time1 == 480:
        bullet10 = "yes"
    if bullet10 == "yes":
        bullet10x += bullet10xx
        bullet10y += bullet10yy
    if bullet10x > 1064:
        bullet10xx = -1*bullet10xx
    if bullet10x < 1:
        bullet10xx = -1*bullet10xx
    if bullet10y > 524:
        bullet10yy = -1*bullet10yy
    if bullet10y < 1:
        bullet10yy = -1*bullet10yy

    if time1 == 500:
        bullet11 = "yes"
    if bullet11 == "yes":
        bullet11x += bullet11xx
        bullet11y += bullet11yy
    if bullet11x > 1064:
        bullet11xx = -1*bullet11xx
    if bullet11x < 1:
        bullet11xx = -1*bullet11xx
    if bullet11y > 524:
        bullet11yy = -1*bullet11yy
    if bullet11y < 1:
        bullet11yy = -1*bullet11yy

    if time1 == 520:
        bullet12 = "yes"
    if bullet12 == "yes":
        bullet12x += bullet12xx
        bullet12y += bullet12yy
    if bullet12x > 1064:
        bullet12xx = -1*bullet12xx
    if bullet12x < 1:
        bullet12xx = -1*bullet12xx
    if bullet12y > 524:
        bullet12yy = -1*bullet12yy
    if bullet12y < 1:
        bullet12yy = -1*bullet12yy

    pygame.draw.rect(screen, (0, 0, 0), (bullet1x, bullet1y, 15, 15))
    pygame.draw.rect(screen, (0, 0, 0), (bullet2x, bullet2y, 15, 15))
    pygame.draw.rect(screen, (0, 0, 0), (bullet3x, bullet3y, 15, 15))
    pygame.draw.rect(screen, (0, 0, 0), (bullet4x, bullet4y, 15, 15))
    pygame.draw.rect(screen, (0, 0, 0), (bullet5x, bullet5y, 15, 15))
    pygame.draw.rect(screen, (0, 0, 0), (bullet6x, bullet6y, 15, 15))
    pygame.draw.rect(screen, (0, 0, 0), (bullet7x, bullet7y, 15, 15))
    pygame.draw.rect(screen, (0, 0, 0), (bullet8x, bullet8y, 15, 15))
    pygame.draw.rect(screen, (0, 0, 0), (bullet9x, bullet9y, 15, 15))
    pygame.draw.rect(screen, (0, 0, 0), (bullet10x, bullet10y, 15, 15))
    pygame.draw.rect(screen, (0, 0, 0), (bullet11x, bullet11y, 15, 15))
    pygame.draw.rect(screen, (0, 0, 0), (bullet12x, bullet12y, 15, 15))

    time1 += 1

    stopwatch = font.render(str(time1), False, (0,0,0))

    screen.blit(stopwatch, (500,250))

    if mousex > 1064:
        mousex = 1064
    if mousey > 524:
        mousey = 524

    pygame.draw.rect(screen, (255, 255, 255), (mousex, mousey, 15, 15))

    if abs(mousex - bullet1x) <= 15:
        if abs(mousey - bullet1y) <= 15:
            print(time1)
            sys.exit()
    if abs(mousex - bullet2x) <= 15:
        if abs(mousey - bullet2y) <= 15:
            print(time1)
            sys.exit()
    if abs(mousex - bullet3x) <= 15:
        if abs(mousey - bullet3y) <= 15:
            print(time1)
            sys.exit()
    if abs(mousex - bullet4x) <= 15:
        if abs(mousey - bullet4y) <= 15:
            print(time1)
            sys.exit()
    if abs(mousex - bullet5x) <= 15:
        if abs(mousey - bullet5y) <= 15:
            print(time1)
            sys.exit()
    if abs(mousex - bullet6x) <= 15:
        if abs(mousey - bullet6y) <= 15:
            print(time1)
            sys.exit()
    if abs(mousex - bullet7x) <= 15:
        if abs(mousey - bullet7y) <= 15:
            print(time1)
            sys.exit()
    if abs(mousex - bullet8x) <= 15:
        if abs(mousey - bullet8y) <= 15:
            print(time1)
            sys.exit()
    if abs(mousex - bullet9x) <= 15:
        if abs(mousey - bullet9y) <= 15:
            print(time1)
            sys.exit()
    if abs(mousex - bullet10x) <= 15:
        if abs(mousey - bullet10y) <= 15:
            print(time1)
            sys.exit()
    if abs(mousex - bullet11x) <= 15:
        if abs(mousey - bullet11y) <= 15:
            print(time1)
            sys.exit()
    if abs(mousex - bullet12x) <= 15:
        if abs(mousey - bullet12y) <= 15:
            print(time1)
            sys.exit()

    pygame.display.flip()
    clock.tick(100)