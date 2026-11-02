import pygame

import sys

import math

import time

import random

pygame.init()

aimbot = False

aimturn = "dunno"

highscore = 0

stickarrow = True

clock = pygame.time.Clock()

screen = pygame.display.set_mode((1080,540))

font = pygame.font.Font("freesansbold.ttf", 32)
tinyfont = pygame.font.Font("freesansbold.ttf", 16)

autofire = True

nonbotx = 200
nonboty = 500
nonbotyy = 0
botx = 1000
boty = 100
movingright = False
movingleft = False
jump = False
onground = True

powerupx = random.randint(50, 850)
powerupy = random.randint(50, 490)
#1 is tripleshot, 2 is knockback, 3 is lasers, 4 is freeze, 5 is reload smaller, 6 is perma knockback
#7 is damage(15000), 8 is aimbot
powertype = random.randint(1, 8)
poweruptimer = 0

permaknock = 0

stopwatch = 0

slide = "menu"

bg1 = 100
bg2 = 255
bg3 = 0
bg11 = False
bg22 = False
bg33 = False

arrowx = []
arrowy = []
arrowxx = []
arrowyy = []
arrowstate = []
arrowdelete = []

stickarrowx = []
stickarrowy = []
stickarrowxx = []
stickarrowyy = []

reload = 400

earrowx = []
earrowy = []
earrowxx = []
earrowyy = []
earrowstate = []

damage = 0

shoot1 = False
shootup = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                movingright = True
            if event.key == pygame.K_a:
                movingleft = True
            if event.key == pygame.K_w:
                jump = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                movingright = False
            if event.key == pygame.K_a:
                movingleft = False
            if event.key == pygame.K_w:
                jump = False

    screen.fill((bg1, bg2, bg3))

    highscoretext = font.render("High score:", False, (0, 0, 0))
    begintext = font.render("Click here to begin", False, (0, 0, 0))
    autotext = font.render("Auto fire:", False, (0, 0, 0))
    colortext = font.render("Bg color:", False, (0, 0, 0))
    highscoretext1 = font.render(str(highscore), False, (0, 0, 0))

    mousex, mousey = pygame.mouse.get_pos()

    if slide == "menu":
        screen.blit(highscoretext, (350, 200))
        screen.blit(begintext, (400, 100))
        screen.blit(autotext, (450, 300))
        screen.blit(colortext, (100, 410))
        screen.blit(highscoretext1, (550, 200))
        pygame.draw.rect(screen, (0, 0, 255), (250, 375, 512, 10))
        pygame.draw.rect(screen, (0, 0, 255), (250, 425, 512, 10))
        pygame.draw.rect(screen, (0, 0, 255), (250, 475, 512, 10))
        pygame.draw.rect(screen, (255, 0, 255), (250+2*bg1, 365, 10, 30))
        pygame.draw.rect(screen, (255, 0, 255), (250+2*bg2, 415, 10, 30))
        pygame.draw.rect(screen, (255, 0, 255), (250+2*bg3, 465, 10, 30))
        if event.type == pygame.MOUSEBUTTONDOWN and 250+2*bg1<mousex<260+2*bg1 and 365<mousey<395:
            bg11 = True
        if event.type == pygame.MOUSEBUTTONDOWN and 250+2*bg2<mousex<260+2*bg2 and 415<mousey<445:
            bg22 = True
        if event.type == pygame.MOUSEBUTTONDOWN and 250+2*bg3<mousex<260+2*bg3 and 465<mousey<495:
            bg33 = True
        if event.type == pygame.MOUSEBUTTONUP and 220<mousex<780 and 350<mousey<510:
            bg11 = False
            bg22 = False
            bg33 = False
        if bg11 == True and 250<mousex<762:
            bg1 = (mousex-250)/2
        if bg22 == True and 250<mousex<762:
            bg2 = (mousex-250)/2
        if bg33 == True and 250<mousex<762:
            bg3 = (mousex-250)/2
        if autofire == True:
            pygame.draw.rect(screen, (0, 0, 255), (600, 300, 30, 30))
        if autofire == False:
            pygame.draw.rect(screen, (255, 0, 0), (600, 300, 30, 30))
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 600<mousex<630:
                if 300<mousey<330:
                    if autofire == True:
                        autofire = False
                    else:
                        autofire = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            if 400 < mousex < 700:
                if 100<mousey<140:
                    slide = "game"

    if slide == "game":
        mousex = random.randint(mousex - 10, mousex + 10)
        mousey = random.randint(mousey - 10, mousey + 10)

        if poweruptimer == 1000 and powertype == 5:
            reload = round(1.5 * reload)

        if poweruptimer == 1000 and powertype == 6:
            permaknock += 1

        if poweruptimer == 1000 and powertype == 7:
            damage += 15000

        if poweruptimer == 1000 and powertype == 8:
            aimbot = True

        stopwatch += 1

        poweruptimer -= 1

        if movingright == True:
            nonbotx += 5
        if movingleft == True:
            nonbotx -= 5
        if jump == True and onground == True:
            nonbotyy = -7
            jump = False

        onground = False

        score = font.render("Score:", False, (0, 0, 0))
        score1 = font.render(str(damage), False, (0, 0, 0))

        if nonboty >= 500 and nonbotyy >= 0:
            onground = True
            nonbotyy = 0
            nonboty = 500
        if nonboty >= 380 and nonbotyy >= 0 and nonbotx >= 900 and nonboty <= 400:
            onground = True
            nonbotyy = 0
            nonboty = 380
        if nonbotx >= 900 and nonboty >= 400:
            nonbotx = 900
        if nonbotx >= 1070:
            nonbotx = 1070
        if nonbotx <= 10:
            nonbotx = 10
        if nonboty <= 20:
            nonboty = 20
        if nonboty >= 220 and nonbotyy >= 0 and nonbotx >= 600 and nonboty <= 240 and nonbotx <= 650:
            onground = True
            nonbotyy = 0
            nonboty = 220
        if nonboty >= 280 and nonbotyy >= 0 and nonbotx >= 250 and nonboty <= 300 and nonbotx <= 300:
            onground = True
            nonbotyy = 0
            nonboty = 280
        if nonboty >= 80 and nonbotyy >= 0 and nonbotx >= 150 and nonboty <= 100 and nonbotx <= 200:
            onground = True
            nonbotyy = 0
            nonboty = 80
        if nonboty >= 160 and nonbotyy >= 0 and nonbotx >= 0 and nonboty <= 180 and nonbotx <= 100:
            onground = True
            nonbotyy = 0
            nonboty = 160
        if nonboty >= 160 and nonbotyy >= 0 and nonbotx >= 900 and nonboty <= 180 and nonbotx <= 1080:
            onground = True
            nonbotyy = 0
            nonboty = 160
        if nonboty >= 20 and nonbotyy >= 0 and nonbotx >= 300 and nonboty <= 40 and nonbotx <= 750:
            onground = True
            nonbotyy = 0
            nonboty = 20
        if nonboty >= 499 and nonbotyy >= 0 and nonbotx >= 400 and nonboty <= 540 and nonbotx <= 450:
            onground = False
            nonbotyy = -11.35

        if onground == False:
            nonbotyy += 0.15

        if event.type == pygame.MOUSEBUTTONUP:
            shootup = True
            shoot1 = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            shoot1 = True

        if shoot1 == True or autofire == True:
        #if event.type == pygame.MOUSEBUTTONDOWN and shootup == True:
            if nonbotx != mousex:
                arrowx.append(nonbotx)
                arrowy.append(nonboty)
                ratio = (nonboty - mousey) / (nonbotx - mousex)
                if (nonboty - mousey) < 0 and (nonbotx - mousex) < 0:
                    arrowyy.append(round(ratio * math.sqrt(400 / (ratio ** 2 + 1)), 3))
                    arrowxx.append(round(math.sqrt(400 / (ratio ** 2 + 1)), 3))
                if (nonboty - mousey) >= 0 and (nonbotx - mousex) >= 0:
                    arrowyy.append(-round(ratio * math.sqrt(400 / (ratio ** 2 + 1)), 3))
                    arrowxx.append(-round(math.sqrt(400 / (ratio ** 2 + 1)), 3))
                if (nonbotx - mousex) < 0 and (nonboty - mousey) >= 0:
                    arrowyy.append(round(ratio * math.sqrt(400 / (ratio ** 2 + 1)), 3))
                    arrowxx.append(round(math.sqrt(400 / (ratio ** 2 + 1)), 3))
                if (nonbotx - mousex) >= 0 and (nonboty - mousey) < 0:
                    arrowyy.append(-round(ratio * math.sqrt(400 / (ratio ** 2 + 1)), 3))
                    arrowxx.append(-round(math.sqrt(400 / (ratio ** 2 + 1)), 3))
                arrowstate.append(1)
                arrowdelete.append(1)
                if powertype == 1 and poweruptimer > 0:
                    arrowx.append(nonbotx)
                    arrowy.append(nonboty - 10)
                    ratio = (nonboty - mousey) / (nonbotx - mousex)
                    if (nonboty - mousey) < 0 and (nonbotx - mousex) < 0:
                        arrowyy.append(round(ratio * math.sqrt(400 / (ratio ** 2 + 1)), 3))
                        arrowxx.append(round(math.sqrt(400 / (ratio ** 2 + 1)), 3))
                    if (nonboty - mousey) >= 0 and (nonbotx - mousex) >= 0:
                        arrowyy.append(-round(ratio * math.sqrt(400 / (ratio ** 2 + 1)), 3))
                        arrowxx.append(-round(math.sqrt(400 / (ratio ** 2 + 1)), 3))
                    if (nonbotx - mousex) < 0 and (nonboty - mousey) >= 0:
                        arrowyy.append(round(ratio * math.sqrt(400 / (ratio ** 2 + 1)), 3))
                        arrowxx.append(round(math.sqrt(400 / (ratio ** 2 + 1)), 3))
                    if (nonbotx - mousex) >= 0 and (nonboty - mousey) < 0:
                        arrowyy.append(-round(ratio * math.sqrt(400 / (ratio ** 2 + 1)), 3))
                        arrowxx.append(-round(math.sqrt(400 / (ratio ** 2 + 1)), 3))
                    arrowstate.append(1)
                    arrowdelete.append(1)
                    arrowx.append(nonbotx)
                    arrowy.append(nonboty + 10)
                    ratio = (nonboty - mousey) / (nonbotx - mousex)
                    if (nonboty - mousey) < 0 and (nonbotx - mousex) < 0:
                        arrowyy.append(round(ratio * math.sqrt(400 / (ratio ** 2 + 1)), 3))
                        arrowxx.append(round(math.sqrt(400 / (ratio ** 2 + 1)), 3))
                    if (nonboty - mousey) >= 0 and (nonbotx - mousex) >= 0:
                        arrowyy.append(-round(ratio * math.sqrt(400 / (ratio ** 2 + 1)), 3))
                        arrowxx.append(-round(math.sqrt(400 / (ratio ** 2 + 1)), 3))
                    if (nonbotx - mousex) < 0 and (nonboty - mousey) >= 0:
                        arrowyy.append(round(ratio * math.sqrt(400 / (ratio ** 2 + 1)), 3))
                        arrowxx.append(round(math.sqrt(400 / (ratio ** 2 + 1)), 3))
                    if (nonbotx - mousex) >= 0 and (nonboty - mousey) < 0:
                        arrowyy.append(-round(ratio * math.sqrt(400 / (ratio ** 2 + 1)), 3))
                        arrowxx.append(-round(math.sqrt(400 / (ratio ** 2 + 1)), 3))
                    arrowstate.append(1)
                    arrowdelete.append(1)
                shootup = False

        if (stopwatch / round(reload)) % 1 == 0:
            if nonbotx != botx:
                earrowx.append(botx)
                earrowy.append(boty)
                ratio3 = (nonboty - boty) / (nonbotx - botx)
                if (nonboty - boty) < 0 and (nonbotx - botx) < 0:
                    earrowyy.append(-round(ratio3 * math.sqrt(200 / (ratio3 ** 2 + 1)), 3))
                    earrowxx.append(-round(math.sqrt(200 / (ratio3 ** 2 + 1)), 3))
                if (nonboty - boty) >= 0 and (nonbotx - botx) >= 0:
                    earrowyy.append(round(ratio3 * math.sqrt(200 / (ratio3 ** 2 + 1)), 3))
                    earrowxx.append(round(math.sqrt(200 / (ratio3 ** 2 + 1)), 3))
                if (nonbotx - botx) < 0 and (nonboty - boty) >= 0:
                    earrowyy.append(-round(ratio3 * math.sqrt(200 / (ratio3 ** 2 + 1)), 3))
                    earrowxx.append(-round(math.sqrt(200 / (ratio3 ** 2 + 1)), 3))
                if (nonbotx - botx) >= 0 and (nonboty - boty) < 0:
                    earrowyy.append(round(ratio3 * math.sqrt(200 / (ratio3 ** 2 + 1)), 3))
                    earrowxx.append(round(math.sqrt(200 / (ratio3 ** 2 + 1)), 3))
                earrowstate.append(1)

        if (stopwatch / 100) % 1 == 0 and reload >= 1:
            reload = round(0.97 * reload, 3)

        if powerupx < nonbotx < powerupx + 50 and poweruptimer <= 0:
            if powerupy < nonboty < powerupy + 50:
                poweruptimer = 1000

        if poweruptimer == 0:
            powerupx = random.randint(0, 850)
            powerupy = random.randint(0, 490)
            powertype = random.randint(1, 8)
            aimbot = False

        ratio2 = (nonboty - boty) / (nonbotx - botx)
        if (nonboty - boty) < 0 and (nonbotx - botx) < 0:
            boty -= (round(ratio2 * math.sqrt(75 / reload / (ratio2 ** 2 + 1)), 3))
            botx -= (round(math.sqrt(75 / reload / (ratio2 ** 2 + 1)), 3))
        if (nonboty - boty) >= 0 and (nonbotx - botx) >= 0:
            boty -= (-round(ratio2 * math.sqrt(75 / reload / (ratio2 ** 2 + 1)), 3))
            botx -= (-round(math.sqrt(75 / reload / (ratio2 ** 2 + 1)), 3))
        if (nonbotx - botx) < 0 and (nonboty - boty) >= 0:
            boty -= (round(ratio2 * math.sqrt(75 / reload / (ratio2 ** 2 + 1)), 3))
            botx -= (round(math.sqrt(75 / reload / (ratio2 ** 2 + 1)), 3))
        if (nonbotx - botx) >= 0 and (nonboty - boty) < 0:
            boty -= (-round(ratio2 * math.sqrt(75 / reload / (ratio2 ** 2 + 1)), 3))
            botx -= (-round(math.sqrt(75 / reload / (ratio2 ** 2 + 1)), 3))
        if poweruptimer > 0 and powertype == 4:
            if (nonboty - boty) < 0 and (nonbotx - botx) < 0:
                boty += (round(ratio2 * math.sqrt(75 / reload / (ratio2 ** 2 + 1)), 3))
                botx += (round(math.sqrt(75 / reload / (ratio2 ** 2 + 1)), 3))
            if (nonboty - boty) >= 0 and (nonbotx - botx) >= 0:
                boty += (-round(ratio2 * math.sqrt(75 / reload / (ratio2 ** 2 + 1)), 3))
                botx += (-round(math.sqrt(75 / reload / (ratio2 ** 2 + 1)), 3))
            if (nonbotx - botx) < 0 and (nonboty - boty) >= 0:
                boty += (round(ratio2 * math.sqrt(75 / reload / (ratio2 ** 2 + 1)), 3))
                botx += (round(math.sqrt(75 / reload / (ratio2 ** 2 + 1)), 3))
            if (nonbotx - botx) >= 0 and (nonboty - boty) < 0:
                boty += (-round(ratio2 * math.sqrt(75 / reload / (ratio2 ** 2 + 1)), 3))
                botx += (-round(math.sqrt(75 / reload / (ratio2 ** 2 + 1)), 3))

        nonboty += nonbotyy

        tripletext = tinyfont.render("triple", False, (0, 0, 0))
        knocktext = tinyfont.render("knockback", False, (0, 0, 0))
        laserstext = tinyfont.render("lasers", False, (0, 0, 0))
        freezetext = tinyfont.render("freeze", False, (0, 0, 0))
        reloadtext = tinyfont.render("reload", False, (0, 0, 0))
        permatext = tinyfont.render("perma", False, (0, 0, 0))
        damagetext = tinyfont.render("damage", False, (0, 0, 0))
        aimbottext = tinyfont.render("aimbot", False, (0, 0, 0))

        for dog in range(0, len(arrowx)):
            if poweruptimer > 0 and powertype != 3 and powertype != 8 or poweruptimer <= 0:
                if arrowy[dog] >= 520:
                    arrowstate[dog] = 0
                if arrowy[dog] >= 400 and arrowx[dog] >= 900 and arrowy[dog] <= 420:
                    arrowstate[dog] = 0
                if arrowx[dog] >= 920 and arrowy[dog] >= 420:
                    arrowstate[dog] = 0
                if arrowx[dog] >= 1080:
                    arrowstate[dog] = 0
                if arrowx[dog] <= 0:
                    arrowstate[dog] = 0
                if arrowy[dog] <= 0:
                    arrowstate[dog] = 0
                if arrowy[dog] >= 240 and arrowx[dog] >= 600 and arrowy[dog] <= 260 and arrowx[dog] <= 650:
                    arrowstate[dog] = 0
                if arrowy[dog] >= 300 and arrowx[dog] >= 250 and arrowy[dog] <= 320 and arrowx[dog] <= 300:
                    arrowstate[dog] = 0
                if arrowy[dog] >= 100 and arrowx[dog] >= 150 and arrowy[dog] <= 120 and arrowx[dog] <= 200:
                    arrowstate[dog] = 0
                if arrowy[dog] >= 180 and arrowx[dog] >= 0 and arrowy[dog] <= 200 and arrowx[dog] <= 100:
                    arrowstate[dog] = 0
                if arrowy[dog] >= 180 and arrowx[dog] >= 900 and arrowy[dog] <= 200 and arrowx[dog] <= 1080:
                    arrowstate[dog] = 0
                if arrowy[dog] >= 40 and arrowx[dog] >= 300 and arrowy[dog] <= 60 and arrowx[dog] <= 750:
                    arrowstate[dog] = 0
            if arrowy[dog] >= boty - 20 and arrowx[dog] >= botx - 10 and arrowy[dog] <= boty + 20 and arrowx[
                dog] <= botx + 10 and \
                arrowstate[dog] == 1:
                damage += round(math.sqrt((nonbotx - botx) ** 2 + (nonboty - boty) ** 2) / 100)
                if powertype != 3 or poweruptimer <= 0:
                    stickarrowx.append(arrowx[dog] - botx)
                    stickarrowy.append(arrowy[dog] - boty)
                    stickarrowxx.append(arrowxx[dog])
                    stickarrowyy.append(arrowyy[dog])
                    arrowdelete[dog] = 0
                if powertype == 3:
                    damage += round(math.sqrt((nonbotx - botx) ** 2 + (nonboty - boty) ** 2) / 100)
                if poweruptimer > 0 and powertype == 2:
                    ratio2 = (nonboty - boty) / (nonbotx - botx)
                    if (nonboty - boty) < 0 and (nonbotx - botx) < 0:
                        boty += (round(ratio2 * math.sqrt(100 / (ratio2 ** 2 + 1)), 3))
                        botx += (round(math.sqrt(100 / (ratio2 ** 2 + 1)), 3))
                    if (nonboty - boty) >= 0 and (nonbotx - botx) >= 0:
                        boty += (-round(ratio2 * math.sqrt(100 / (ratio2 ** 2 + 1)), 3))
                        botx += (-round(math.sqrt(100 / (ratio2 ** 2 + 1)), 3))
                    if (nonbotx - botx) < 0 and (nonboty - boty) >= 0:
                        boty += (round(ratio2 * math.sqrt(100 / (ratio2 ** 2 + 1)), 3))
                        botx += (round(math.sqrt(100 / (ratio2 ** 2 + 1)), 3))
                    if (nonbotx - botx) >= 0 and (nonboty - boty) < 0:
                        boty += (-round(ratio2 * math.sqrt(100 / (ratio2 ** 2 + 1)), 3))
                        botx += (-round(math.sqrt(100 / (ratio2 ** 2 + 1)), 3))
                    damage += round(math.sqrt((nonbotx - botx) ** 2 + (nonboty - boty) ** 2) / 10)
                if (nonboty - boty) < 0 and (nonbotx - botx) < 0:
                    boty += (round(ratio2 * math.sqrt(1.5*permaknock / (ratio2 ** 2 + 1)), 3))
                    botx += (round(math.sqrt(1.5*permaknock / (ratio2 ** 2 + 1)), 3))
                if (nonboty - boty) >= 0 and (nonbotx - botx) >= 0:
                    boty += (-round(ratio2 * math.sqrt(1.5*permaknock / (ratio2 ** 2 + 1)), 3))
                    botx += (-round(math.sqrt(1.5*permaknock / (ratio2 ** 2 + 1)), 3))
                if (nonbotx - botx) < 0 and (nonboty - boty) >= 0:
                    boty += (round(ratio2 * math.sqrt(1.5*permaknock / (ratio2 ** 2 + 1)), 3))
                    botx += (round(math.sqrt(1.5*permaknock / (ratio2 ** 2 + 1)), 3))
                if (nonbotx - botx) >= 0 and (nonboty - boty) < 0:
                    boty += (-round(ratio2 * math.sqrt(1.5*permaknock / (ratio2 ** 2 + 1)), 3))
                    botx += (-round(math.sqrt(1.5*permaknock / (ratio2 ** 2 + 1)), 3))
            if arrowy[dog] >= boty - 20 and arrowx[dog] >= botx - 10 and arrowy[dog] <= boty - 10 and arrowx[
                dog] <= botx + 10 and \
                    arrowstate[dog] == 1:
                damage += round(math.sqrt((nonbotx - botx) ** 2 + (nonboty - boty) ** 2) / 40)

            if arrowstate[dog] == 1:
                arrowx[dog] += arrowxx[dog]
                arrowy[dog] += arrowyy[dog]
                # gravity used to be 0.07
                arrowyy[dog] += 0.07
            pygame.draw.line(screen, (255, 0, 0), (round(arrowx[dog]), round(arrowy[dog])),
                             (round(arrowx[dog] - 2.5 * arrowxx[dog]), round(arrowy[dog] - 2.5 * arrowyy[dog])), 3)
        for dog in range(0, len(stickarrowx)):
            pygame.draw.line(screen, (255, 0, 0), (round(stickarrowx[dog] + botx), round(stickarrowy[dog]) + boty), (
            round(botx + stickarrowx[dog] - 2.5 * stickarrowxx[dog]),
            round(boty + stickarrowy[dog] - 2.5 * stickarrowyy[dog])), 3)
        for dog in range(0, len(earrowx)):
            if earrowy[dog] >= 520:
                earrowstate[dog] = 0
            if earrowy[dog] >= 400 and earrowx[dog] >= 900 and earrowy[dog] <= 420:
                earrowstate[dog] = 0
            if earrowx[dog] >= 900 and earrowy[dog] >= 420:
                earrowstate[dog] = 0
            if earrowx[dog] >= 1080:
                earrowstate[dog] = 0
            if earrowx[dog] <= 0:
                earrowstate[dog] = 0
            if earrowy[dog] <= 0:
                earrowstate[dog] = 0
            if earrowy[dog] >= 240 and earrowx[dog] >= 600 and earrowy[dog] <= 260 and earrowx[dog] <= 650:
                earrowstate[dog] = 0
            if earrowy[dog] >= 300 and earrowx[dog] >= 250 and earrowy[dog] <= 320 and earrowx[dog] <= 300:
                earrowstate[dog] = 0
            if earrowy[dog] >= 100 and earrowx[dog] >= 150 and earrowy[dog] <= 120 and earrowx[dog] <= 200:
                earrowstate[dog] = 0
            if earrowy[dog] >= 180 and earrowx[dog] >= 0 and earrowy[dog] <= 200 and earrowx[dog] <= 100:
                earrowstate[dog] = 0
            if earrowy[dog] >= 180 and earrowx[dog] >= 900 and earrowy[dog] <= 200 and earrowx[dog] <= 1080:
                earrowstate[dog] = 0
            if earrowy[dog] >= 40 and earrowx[dog] >= 300 and earrowy[dog] <= 60 and earrowx[dog] <= 750:
                earrowstate[dog] = 0
            if earrowy[dog] >= nonboty - 20 and earrowx[dog] >= nonbotx - 10 and earrowy[dog] <= nonboty + 20 and \
                    earrowx[dog] <= nonbotx + 10:
                if earrowstate[dog] == 1:
                    time.sleep(2)
                    slide = "menu"
                    if damage > highscore:
                        highscore = damage
                    nonbotx = 200
                    nonboty = 500
                    nonbotyy = 0
                    botx = 1000
                    boty = 100
                    movingright = False
                    movingleft = False
                    jump = False
                    onground = True

                    aimbot = False

                    powerupx = random.randint(50, 850)
                    powerupy = random.randint(50, 490)
                    powertype = random.randint(1, 5)
                    poweruptimer = 0

                    stopwatch = 0

                    slide = "menu"

                    permaknock = 0

                    arrowx = []
                    arrowy = []
                    arrowxx = []
                    arrowyy = []
                    arrowstate = []
                    arrowdelete = []

                    stickarrowx = []
                    stickarrowy = []
                    stickarrowxx = []
                    stickarrowyy = []

                    reload = 400

                    earrowx = []
                    earrowy = []
                    earrowxx = []
                    earrowyy = []
                    earrowstate = []

                    damage = 0

                    shoot1 = False
                    shootup = False

                    break
            if earrowstate[dog] == 1:
                earrowx[dog] += earrowxx[dog]
                earrowy[dog] += earrowyy[dog]
                earrowyy[dog] += 0.05
            pygame.draw.line(screen, (0, 0, 0), (round(earrowx[dog]), round(earrowy[dog])),
                             (round(earrowx[dog] - 3 * earrowxx[dog]), round(earrowy[dog] - 3 * earrowyy[dog])), 5)
        pygame.draw.rect(screen, (255, 0, 255), (round(nonbotx) - 10, round(nonboty) - 20, 20, 40))
        pygame.draw.rect(screen, (0, 0, 0), (round(botx) - 10, round(boty) - 20, 20, 40))
        pygame.draw.rect(screen, (0, 0, 255), (round(botx) - 10, round(boty) - 20, 20, 10))
        pygame.draw.rect(screen, (255, 255, 255), (0, 520, 1080, 20))
        pygame.draw.rect(screen, (255, 255, 255), (910, 400, 170, 170))
        pygame.draw.rect(screen, (255, 255, 255), (600, 240, 50, 20))
        pygame.draw.rect(screen, (255, 255, 255), (250, 300, 50, 20))
        pygame.draw.rect(screen, (255, 255, 255), (150, 100, 50, 20))
        pygame.draw.rect(screen, (255, 255, 255), (0, 180, 100, 20))
        pygame.draw.rect(screen, (255, 255, 255), (900, 180, 180, 20))
        pygame.draw.rect(screen, (255, 255, 255), (300, 40, 450, 20))
        pygame.draw.rect(screen, (255, 0, 0), (400, 520, 50, 20))
        if poweruptimer <= 0:
            pygame.draw.rect(screen, (255, 100, 0), (powerupx, powerupy, 50, 50))
            if powertype == 1:
                screen.blit(tripletext, (powerupx, powerupy+16))
            if powertype == 2:
                screen.blit(knocktext, (powerupx - 15, powerupy+16))
            if powertype == 3:
                screen.blit(laserstext, (powerupx, powerupy+16))
            if powertype == 4:
                screen.blit(freezetext, (powerupx, powerupy+16))
            if powertype == 5:
                screen.blit(reloadtext, (powerupx, powerupy+16))
            if powertype == 6:
                screen.blit(permatext, (powerupx, powerupy+10))
                screen.blit(knocktext, (powerupx - 15, powerupy+30))
            if powertype == 7:
                screen.blit(damagetext, (powerupx, powerupy+16))
            if powertype == 8:
                screen.blit(aimbottext, (powerupx, powerupy+16))

        # aimbot
        if aimbot == True:
            for dog in range(0, len(arrowx)):
                if arrowstate[dog] == 1 and arrowxx[dog] != 0 and (botx - arrowx[dog]) != 0:
                    if arrowxx[dog] > 0 and (botx - arrowx[dog]) > 0 or (botx - arrowx[dog]) < 0 and arrowxx[dog] < 0:
                        if arrowyy[dog] / arrowxx[dog] < (boty - arrowy[dog]) / (botx - arrowx[dog]):
                            aimturn = "right"
                        if arrowyy[dog] / arrowxx[dog] > (boty - arrowy[dog]) / (botx - arrowx[dog]):
                            aimturn = "left"
                    if arrowxx[dog] > 0 and (botx - arrowx[dog]) < 0 or (botx - arrowx[dog]) > 0 and arrowxx[dog] < 0:
                        if arrowyy[dog] / arrowxx[dog] < (boty - arrowy[dog]) / (botx - arrowx[dog]):
                            aimturn = "left"
                        if arrowyy[dog] / arrowxx[dog] > (boty - arrowy[dog]) / (botx - arrowx[dog]):
                            aimturn = "right"
                    if aimturn == "left":
                        if arrowxx[dog] < 0 and arrowyy[dog] < 0:
                            arrowxx[dog] -= 0.5
                            arrowyy[dog] += 0.5
                        if arrowxx[dog] < 0 and arrowyy[dog] > 0:
                            arrowxx[dog] += 0.5
                            arrowyy[dog] += 0.5
                        if arrowxx[dog] > 0 and arrowyy[dog] < 0:
                            arrowxx[dog] -= 0.5
                            arrowyy[dog] -= 0.5
                        if arrowxx[dog] > 0 and arrowyy[dog] > 0:
                            arrowxx[dog] += 0.5
                            arrowyy[dog] -= 0.5
                    if aimturn == "right":
                        if arrowxx[dog] < 0 and arrowyy[dog] < 0:
                            arrowxx[dog] += 0.5
                            arrowyy[dog] -= 0.5
                        if arrowxx[dog] < 0 and arrowyy[dog] > 0:
                            arrowxx[dog] -= 0.5
                            arrowyy[dog] -= 0.5
                        if arrowxx[dog] > 0 and arrowyy[dog] < 0:
                            arrowxx[dog] += 0.5
                            arrowyy[dog] += 0.5
                        if arrowxx[dog] > 0 and arrowyy[dog] > 0:
                            arrowxx[dog] -= 0.5
                            arrowyy[dog] += 0.5

        for dog in range(0, len(arrowx)):
            if arrowdelete[dog] == 0:
                del arrowdelete[dog]
                del arrowx[dog]
                del arrowxx[dog]
                del arrowy[dog]
                del arrowyy[dog]
                del arrowstate[dog]
                break

        for dog in range(0, len(arrowx)):
            if arrowdelete[dog] == 0:
                del arrowdelete[dog]
                del arrowx[dog]
                del arrowxx[dog]
                del arrowy[dog]
                del arrowyy[dog]
                del arrowstate[dog]
                break

        for dog in range(0, len(arrowx)):
            if arrowdelete[dog] == 0:
                del arrowdelete[dog]
                del arrowx[dog]
                del arrowxx[dog]
                del arrowy[dog]
                del arrowyy[dog]
                del arrowstate[dog]
                break

        screen.blit(score, (400, 0))
        screen.blit(score1, (510, 2))

        for dog in range(0, 10):
            if len(arrowx) > 500:
                del arrowx[0]
                del arrowy[0]
                del arrowxx[0]
                del arrowyy[0]
                del arrowstate[0]
                del arrowdelete[0]
        for dog in range(0, 10):
            if len(stickarrowx) > 200:
                del stickarrowx[0]
                del stickarrowy[0]
                del stickarrowxx[0]
                del stickarrowyy[0]

        if len(earrowx) > 100:
            del earrowx[0]
            del earrowy[0]
            del earrowxx[0]
            del earrowyy[0]
            del earrowstate[0]

    pygame.display.flip()
    clock.tick(100)