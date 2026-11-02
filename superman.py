import pygame

import sys

pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((1080,540))
stopwatch = 4000

money = 4000
lives = 100

upgrade1 = 0
upgrade2 = 0
upgrade3 = 0

delay1 = 0
delay2 = 0
delay3 = 0

enemyx = []
enemyy = []
enemyrank = []
enemyway = []
enemyhealth = []

bulletx = []
bullety = []

laserx = []
lasery = []
laserhealth = []

bombx = []
bomby = []
bombdel = []

maulerx = []
maulery = []
maulerdel = []


def fire_bullet(x, y):
    bulletx.append(x)
    bullety.append(y)


def fire_laser(a, b):
    laserx.append(a)
    lasery.append(b)
    laserhealth.append(10)


def throw_bomb(c, d):
    bombx.append(c)
    bomby.append(d)
    bombdel.append("no")


def delete_enemy(qyuyuy):
    del (enemyhealth[qyuyuy])
    del (enemyrank[qyuyuy])
    del (enemyx[qyuyuy])
    del (enemyy[qyuyuy])
    del (enemyway[qyuyuy])
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    mousex, mousey = pygame.mouse.get_pos()

    screen.fill((140, 140, 140))

    stopwatch += 1

    if upgrade1 == 0 and (stopwatch / 100) % 1 == 0:
        fire_bullet(mousex, mousey)
    if upgrade1 == 1 and (stopwatch / 50) % 1 == 0:
        fire_bullet(mousex, mousey)
    if upgrade1 == 2 and (stopwatch / 30) % 1 == 0:
        fire_bullet(mousex, mousey)
    if upgrade1 == 3 and (stopwatch / 20) % 1 == 0:
        fire_bullet(mousex, mousey)
    if upgrade1 == 4 and (stopwatch / 17) % 1 == 0:
        fire_bullet(mousex, mousey)
    if upgrade1 == 5 and (stopwatch / 8) % 1 == 0:
        fire_bullet(mousex, mousey)
    if upgrade1 == 6 and (stopwatch / 4) % 1 == 0:
        fire_bullet(mousex, mousey)
    if upgrade1 == 7 and (stopwatch / 20) % 1 == 0:
        fire_laser(mousex + 8, mousey)
    if upgrade1 == 8 and (stopwatch / 20) % 1 == 0:
        fire_laser(mousex + 3, mousey)
        fire_laser(mousex + 13, mousey)
    if upgrade1 == 9 and (stopwatch / 10) % 1 == 0:
        fire_laser(mousex +3, mousey)
        fire_laser(mousex + 13, mousey)
    if upgrade1 == 10 and (stopwatch / 5) % 1 == 0:
        fire_laser(mousex + 3, mousey)
        fire_laser(mousex + 13, mousey)
    if upgrade2 == 1 and (stopwatch / 200) % 1 == 0:
        throw_bomb(mousex, mousey)
    if upgrade2 == 2 and (stopwatch / 200) % 1 == 0:
        throw_bomb(mousex, mousey)
    if upgrade2 == 3 and (stopwatch / 200) % 1 == 0:
        throw_bomb(mousex, mousey)
    if upgrade2 == 4 and (stopwatch / 120) % 1 == 0:
        throw_bomb(mousex, mousey)
    if upgrade2 == 5 and (stopwatch / 150) % 1 == 0:
        throw_bomb(mousex - 14, mousey)
        throw_bomb(mousex + 14, mousey)
    if upgrade2 == 6 and (stopwatch / 80) % 1 == 0:
        throw_bomb(mousex - 14, mousey)
        throw_bomb(mousex + 14, mousey)
    if upgrade2 == 7 and (stopwatch / 50) % 1 == 0:
        throw_bomb(mousex - 14, mousey)
        throw_bomb(mousex + 14, mousey)
    if upgrade2 == 8 and (stopwatch / 30) % 1 == 0:
        throw_bomb(mousex - 14, mousey)
        throw_bomb(mousex + 14, mousey)
    if upgrade2 == 9 and (stopwatch / 25) % 1 == 0:
        throw_bomb(mousex, mousey)
    if upgrade2 == 10 and (stopwatch / 15) % 1 == 0:
        throw_bomb(mousex, mousey)
    if upgrade3 == 1 and (stopwatch / 50) % 1 == 0:
        money += 1
    if upgrade3 == 2 and (stopwatch / 25) % 1 == 0:
        money += 1
    if upgrade3 == 3 and (stopwatch / 12) % 1 == 0:
        money += 1
    if upgrade3 == 4 and (stopwatch / 6) % 1 == 0:
        money += 1
    if upgrade3 == 5 and (stopwatch / 200) % 1 == 0:
        lives += 10
        money += 100
    if upgrade3 == 6 and (stopwatch / 100) % 1 == 0:
        lives += 10
        money += 60
    if upgrade3 == 7 and (stopwatch / 50) % 1 == 0:
        lives += 10
        money += 35
    if upgrade3 == 8 and (stopwatch / 25) % 1 == 0:
        lives += 10
        money += 20
    if upgrade3 == 9 and (stopwatch / 12) % 1 == 0:
        lives += 10
        money += 12
    if upgrade3 == 10 and (stopwatch / 5) % 1 == 0:
        lives += 10
        money += 8

    if stopwatch == 400:
        enemyx.append(200)
        enemyy.append(-20)
        enemyway.append("down")
        enemyrank.append("white")
        enemyhealth.append(10)
    for klkl in range(0, 40):
        if stopwatch == klkl + 1150:
            enemyx.append(200)
            enemyy.append(-20)
            enemyway.append("down")
            enemyrank.append("red")
            enemyhealth.append(1)
    for klkl in range(0, 50):
        if stopwatch == klkl + 2450:
            enemyx.append(200)
            enemyy.append(-20)
            enemyway.append("down")
            enemyrank.append("green")
            enemyhealth.append(1)
    for klkl in range(0, 100):
        if stopwatch == 20 * klkl + 3400:
            enemyx.append(200)
            enemyy.append(-20)
            enemyway.append("down")
            enemyrank.append("red")
            enemyhealth.append(1)
    for klkl in range(0, 2):
        if stopwatch == klkl + 3800:
            enemyx.append(200)
            enemyy.append(-20)
            enemyway.append("down")
            enemyrank.append("pink")
            enemyhealth.append(1)
    for klkl in range(0, 5):
        if stopwatch == klkl + 4200:
            enemyx.append(200)
            enemyy.append(-20)
            enemyway.append("down")
            enemyrank.append("yellow")
            enemyhealth.append(1)
    if stopwatch == 5400:
        enemyx.append(200)
        enemyy.append(-20)
        enemyway.append("down")
        enemyrank.append("red")
        enemyhealth.append(20)
    for klkl in range(0, 20):
        if stopwatch == klkl + 6300:
            enemyx.append(200)
            enemyy.append(-20)
            enemyway.append("down")
            enemyrank.append("yellow")
            enemyhealth.append(1)
    for klkl in range(0, 25):
        if stopwatch == klkl + 7200:
            enemyx.append(200)
            enemyy.append(-20)
            enemyway.append("down")
            enemyrank.append("red")
            enemyhealth.append(1)
    for klkl in range(0, 25):
        if stopwatch == klkl + 7200:
            enemyx.append(200)
            enemyy.append(-20)
            enemyway.append("down")
            enemyrank.append("blue")
            enemyhealth.append(1)
    for klkl in range(0, 25):
        if stopwatch == 2*klkl + 7300:
            enemyx.append(200)
            enemyy.append(-20)
            enemyway.append("down")
            enemyrank.append("green")
            enemyhealth.append(1)
            money += 20
    for klkl in range(0, 50):
        if stopwatch == 30 * klkl + 8600:
            enemyx.append(200)
            enemyy.append(-20)
            enemyway.append("down")
            enemyrank.append("red")
            enemyhealth.append(1)
    for klkl in range(0, 40):
        if stopwatch == 40 * klkl + 8655:
            enemyx.append(200)
            enemyy.append(-20)
            enemyway.append("down")
            enemyrank.append("blue")
            enemyhealth.append(1)
    for klkl in range(0, 30):
        if stopwatch == 50 * klkl + 8710:
            enemyx.append(200)
            enemyy.append(-20)
            enemyway.append("down")
            enemyrank.append("green")
            enemyhealth.append(1)
    for klkl in range(0, 4):
        if stopwatch == 600 * klkl + 11200:
            enemyx.append(200)
            enemyy.append(-20)
            enemyway.append("down")
            enemyrank.append("white")
            enemyhealth.append(5 + 3 * klkl)
            money += 100
    for klkl in range(0, 45):
        if stopwatch == 60 * klkl + 15200:
            enemyx.append(200)
            enemyy.append(-20)
            enemyway.append("down")
            enemyrank.append("red")
            enemyhealth.append(1)
    if stopwatch == 15600:
        enemyx.append(200)
        enemyy.append(-20)
        enemyway.append("down")
        enemyrank.append("white")
        enemyhealth.append(5)
    for klkl in range(0, 3):
        if stopwatch == 30 * klkl + 16000:
            enemyx.append(200)
            enemyy.append(-20)
            enemyway.append("down")
            enemyrank.append("black")
            enemyhealth.append(3)
    for klkl in range(0, 18):
        if stopwatch == 4 * klkl + 17000:
            enemyx.append(200)
            enemyy.append(-20)
            enemyway.append("down")
            enemyrank.append("yellow")
            enemyhealth.append(2)
    if stopwatch == 19200:
        enemyx.append(200)
        enemyy.append(-20)
        enemyway.append("down")
        enemyrank.append("moab")
        enemyhealth.append(1)
    for klkl in range(0, 8):
        if stopwatch == 10 * klkl + 20800:
            enemyx.append(200)
            enemyy.append(-20)
            enemyway.append("down")
            enemyrank.append("black")
            enemyhealth.append(1)
    for klkl in range(0, 50):
        if stopwatch == 10 * klkl + 20700:
            enemyx.append(200)
            enemyy.append(-20)
            enemyway.append("down")
            enemyrank.append("red")
            enemyhealth.append(2)
            money += 15
    if stopwatch == 22100:
        enemyx.append(200)
        enemyy.append(-20)
        enemyway.append("down")
        enemyrank.append("moab")
        enemyhealth.append(20)
    for klkl in range(0, 20):
        if stopwatch == 4 * klkl + 23500:
            enemyx.append(200)
            enemyy.append(-20)
            enemyway.append("down")
            enemyrank.append("black")
            enemyhealth.append(1)
            money += 300
    if stopwatch == 24800:
        enemyx.append(200)
        enemyy.append(-20)
        enemyway.append("down")
        enemyrank.append("moab")
        enemyhealth.append(1)
    if stopwatch == 24820:
        enemyx.append(200)
        enemyy.append(-20)
        enemyway.append("down")
        enemyrank.append("moab")
        enemyhealth.append(1)
    if stopwatch == 24840:
        enemyx.append(200)
        enemyy.append(-20)
        enemyway.append("down")
        enemyrank.append("moab")
        enemyhealth.append(1)
    if stopwatch == 25700:
        enemyx.append(200)
        enemyy.append(-20)
        enemyway.append("down")
        enemyrank.append("moab")
        enemyhealth.append(40)
    for klkl in range(0, 17):
        if stopwatch == 8 * klkl + 26900:
            enemyx.append(200)
            enemyy.append(-20)
            enemyway.append("down")
            enemyrank.append("black")
            enemyhealth.append(5)
            money += 160
    if stopwatch == 28100:
        enemyx.append(200)
        enemyy.append(-20)
        enemyway.append("down")
        enemyrank.append("moab")
        enemyhealth.append(1)
    if stopwatch == 28120:
        enemyx.append(200)
        enemyy.append(-20)
        enemyway.append("down")
        enemyrank.append("moab")
        enemyhealth.append(1)
    if stopwatch == 28140:
        enemyx.append(200)
        enemyy.append(-20)
        enemyway.append("down")
        enemyrank.append("moab")
        enemyhealth.append(1)
    if stopwatch == 28160:
        enemyx.append(200)
        enemyy.append(-20)
        enemyway.append("down")
        enemyrank.append("moab")
        enemyhealth.append(1)
    if stopwatch == 28180:
        enemyx.append(200)
        enemyy.append(-20)
        enemyway.append("down")
        enemyrank.append("moab")
        enemyhealth.append(1)
    if stopwatch == 29350:
        enemyx.append(1100)
        enemyy.append(80)
        enemyway.append("left")
        enemyrank.append("moab")
        enemyhealth.append(10)
    for klkl in range(0, 100):
        if stopwatch == 50 * klkl + 30500:
            enemyx.append(200)
            enemyy.append(-20)
            enemyway.append("down")
            enemyrank.append("blue")
            enemyhealth.append(1)
            money += 20
    for klkl in range(0, 4):
        if stopwatch == 1000 * klkl + 31000:
            enemyx.append(200)
            enemyy.append(-20)
            enemyway.append("down")
            enemyrank.append("moab")
            enemyhealth.append(1)
            money += 200
    for klkl in range(0, 100):
        if stopwatch == 2*klkl + 36000:
            enemyx.append(200)
            enemyy.append(-20)
            enemyway.append("down")
            enemyrank.append("pink")
            enemyhealth.append(1)
            money += 100
    for klkl in range(0, 120):
        if stopwatch == 2 * klkl + 36900:
            enemyx.append(200)
            enemyy.append(-20)
            enemyway.append("down")
            enemyrank.append("pink")
            enemyhealth.append(1)
    for klkl in range(0, 200):
        if stopwatch == klkl + 38100:
            enemyx.append(200)
            enemyy.append(-20)
            enemyway.append("down")
            enemyrank.append("pink")
            enemyhealth.append(1)
    for klkl in range(0, 10):
        if stopwatch == 10 * klkl + 39400:
            enemyx.append(200)
            enemyy.append(-20)
            enemyway.append("down")
            enemyrank.append("moab")
            enemyhealth.append(1)
            money += 500
    if stopwatch == 41000:
        enemyx.append(200)
        enemyy.append(-20)
        enemyway.append("down")
        enemyrank.append("moab")
        enemyhealth.append(60)
        money += 5000
    if stopwatch == 42400:
        enemyx.append(200)
        enemyy.append(-20)
        enemyway.append("down")
        enemyrank.append("bfb")
        enemyhealth.append(20)
        money += 20000
    for klkl in range(0, 10):
        if stopwatch == 30 * klkl + 43500:
            enemyx.append(200)
            enemyy.append(-20)
            enemyway.append("down")
            enemyrank.append("moab")
            enemyhealth.append(1)
            money += 2000
    for klkl in range(0, 50):
        if stopwatch == 15 * klkl + 44600:
            enemyx.append(200)
            enemyy.append(-20)
            enemyway.append("down")
            enemyrank.append("red")
            enemyhealth.append(1)
    for klkl in range(0, 42):
        if stopwatch == 20 * klkl + 44655:
            enemyx.append(200)
            enemyy.append(-20)
            enemyway.append("down")
            enemyrank.append("blue")
            enemyhealth.append(1)
    for klkl in range(0, 34):
        if stopwatch == 30 * klkl + 44710:
            enemyx.append(200)
            enemyy.append(-20)
            enemyway.append("down")
            enemyrank.append("green")
            enemyhealth.append(1)
    for klkl in range(0, 26):
        if stopwatch == 40 * klkl + 44764:
            enemyx.append(200)
            enemyy.append(-20)
            enemyway.append("down")
            enemyrank.append("yellow")
            enemyhealth.append(1)
    for klkl in range(0, 18):
        if stopwatch == 50 * klkl + 44812:
            enemyx.append(200)
            enemyy.append(-20)
            enemyway.append("down")
            enemyrank.append("pink")
            enemyhealth.append(1)
    for klkl in range(0, 10):
        if stopwatch == 60 * klkl + 44867:
            enemyx.append(200)
            enemyy.append(-20)
            enemyway.append("down")
            enemyrank.append("black")
            enemyhealth.append(1)
            money += 3000
    for klkl in range(0, 5):
        if stopwatch == 60 * klkl + 44913:
            enemyx.append(200)
            enemyy.append(-20)
            enemyway.append("down")
            enemyrank.append("white")
            enemyhealth.append(1)
    for klkl in range(0, 2):
        if stopwatch == 60 * klkl + 44989:
            enemyx.append(200)
            enemyy.append(-20)
            enemyway.append("down")
            enemyrank.append("moab")
            enemyhealth.append(1)
    for klkl in range(0, 25):
        if stopwatch == klkl + 47200:
            enemyx.append(200)
            enemyy.append(-20)
            enemyway.append("down")
            enemyrank.append("moab")
            enemyhealth.append(1)
            money += 1000
    if stopwatch == 48500:
        enemyx.append(200)
        enemyy.append(-20)
        enemyway.append("down")
        enemyrank.append("bfb")
        enemyhealth.append(100)

    if money >= 120 * 2 ** upgrade1:
        pygame.draw.rect(screen, (255, 255, 255), (10, 10, 20, 20))
        if event.type == pygame.MOUSEBUTTONDOWN and mousex < 31 and mousex > 9 and mousey < 31 and mousey > 9:
            delay1 += 1
    if money < 120 * 2 ** upgrade1:
        pygame.draw.rect(screen, (255, 30, 30), (10, 10, 20, 20))
    if money >= 140 * 2 ** upgrade2:
        pygame.draw.rect(screen, (255, 255, 255), (40, 10, 20, 20))
        if event.type == pygame.MOUSEBUTTONDOWN and mousex < 61 and mousex > 39 and mousey < 31 and mousey > 9:
            delay2 += 1
    if money < 140 * 2 ** upgrade2:
        pygame.draw.rect(screen, (255, 30, 30), (40, 10, 20, 20))
    if money >= 110 * 2 ** upgrade3:
        pygame.draw.rect(screen, (255, 255, 255), (70, 10, 20, 20))
        if event.type == pygame.MOUSEBUTTONDOWN and mousex < 91 and mousex > 69 and mousey < 31 and mousey > 9:
            delay3 += 1
    if money < 110 * 2 ** upgrade3:
        pygame.draw.rect(screen, (255, 30, 30), (70, 10, 20, 20))
    if delay1 > 6:
        money -= 110 * 2 ** upgrade1
        upgrade1 += 1
        delay1 = 0
    if delay2 > 6:
        money -= 150 * 2 ** upgrade2
        upgrade2 += 1
        delay2 = 0
    if delay3 > 6:
        money -= 100 * 2 ** upgrade3
        upgrade3 += 1
        delay3 = 0
    if upgrade1 >= 10:
        upgrade1 = 10
    if upgrade2 >= 10:
        upgrade2 = 10
    if upgrade3 >= 10:
        upgrade3 = 10

    for qwqw in range(0, len(bulletx)):
        pygame.draw.rect(screen, (255, 255, 255), (bulletx[qwqw] - 10, bullety[qwqw], 20, 20))

    for wqwq in range(0, len(bulletx)):
        bullety[wqwq] = bullety[wqwq] - 5

    for qrqr in range(0, len(laserx)):
        pygame.draw.rect(screen, (255, 30, 30), (laserx[qrqr] - 10, lasery[qrqr] - 20, 5, 40))

    for qtqt in range(0, len(laserx)):
        lasery[qtqt] = lasery[qtqt] - 5

    for zv in range(0, len(bombx)):
        pygame.draw.rect(screen, (0, 0, 0), (bombx[zv] - 10, bomby[zv] - 20, 20, 20))

    for qwq in range(0, len(bombx)):
        bomby[qwq] = bomby[qwq] - 4

    for ghgh in range(len(bulletx), 0, -1):
        if bullety[ghgh - 1] < -15:
            del (bulletx[ghgh - 1])
            del (bullety[ghgh - 1])
    for dfdf in range(len(laserx), 0, -1):
        if lasery[dfdf - 1] < -30:
            del (laserx[dfdf - 1])
            del (lasery[dfdf - 1])
    for adad in range(len(bombx), 0, -1):
        if bomby[adad - 1] < -15:
            del (bombx[adad - 1])
            del (bomby[adad - 1])

    for gh in range(0, len(enemyx)):
        if enemyx[gh] <= 200 and enemyy[gh] >= 400:
            enemyway[gh] = "right"
        if enemyy[gh] >= 400 and enemyx[gh] >= 900:
            enemyway[gh] = "up"
        if enemyy[gh] <= 100 and enemyx[gh] >= 900:
            enemyway[gh] = "left"
        if enemyy[gh] <= 100 and enemyx[gh] <= 400 and enemyx[gh] >= 201:
            enemyway[gh] = "down"

    for hh in range(0, len(enemyx)):
        if enemyy[hh] >= 550:
            if enemyrank[hh] == "red":
                lives -= 1
            if enemyrank[hh] == "blue":
                lives -= 2
            if enemyrank[hh] == "green":
                lives -= 4
            if enemyrank[hh] == "yellow":
                lives -= 7
            if enemyrank[hh] == "pink":
                lives -= 19
            if enemyrank[hh] == "black":
                lives -= 48
            if enemyrank[hh] == "white":
                lives -= 116
            if enemyrank[hh] == "moab":
                lives -= 600
            if enemyrank[hh] == "bfb":
                lives -= 2600
            delete_enemy(hh)
            break

    for g in range(0, len(enemyx)):
        if enemyway[g] == "down":
            enemyy[g] += 2
        if enemyway[g] == "up":
            enemyy[g] -= 2
        if enemyway[g] == "right":
            enemyx[g] += 2
        if enemyway[g] == "left":
            enemyx[g] -= 2
        if enemyrank[g] == "red":
            pygame.draw.rect(screen, (255, 30, 30), (enemyx[g], enemyy[g], 20, 20))
        if enemyrank[g] == "blue":
            pygame.draw.rect(screen, (30, 30, 255), (enemyx[g], enemyy[g], 20, 20))
        if enemyrank[g] == "green":
            pygame.draw.rect(screen, (30, 255, 30), (enemyx[g], enemyy[g], 20, 20))
        if enemyrank[g] == "yellow":
            pygame.draw.rect(screen, (200, 255, 30), (enemyx[g], enemyy[g], 20, 20))
        if enemyrank[g] == "pink":
            pygame.draw.rect(screen, (255, 130, 130), (enemyx[g], enemyy[g], 20, 20))
        if enemyrank[g] == "black":
            pygame.draw.rect(screen, (0, 0, 0), (enemyx[g], enemyy[g], 20, 20))
        if enemyrank[g] == "white":
            pygame.draw.rect(screen, (255, 255, 255), (enemyx[g], enemyy[g], 20, 20))
        if enemyrank[g] == "moab":
            pygame.draw.rect(screen, (100, 150, 255), (enemyx[g] - 10, enemyy[g] - 10, 40, 40))
        if enemyrank[g] == "bfb":
            pygame.draw.rect(screen, (255, 0 ,0), (enemyx[g] - 20, enemyy[g] - 20, 60, 60))

    if upgrade1 <= 6:
        for qwe in range(len(enemyx) - 1, -1, -1):
            for qwer in range(len(bulletx) - 1, -1, -1):
                if abs(bulletx[qwer] - enemyx[qwe]) < 21:
                    if abs(bullety[qwer] - enemyy[qwe]) < 21:
                        enemyhealth[qwe] -= 1
                        del (bulletx[qwer])
                        del (bullety[qwer])
                        if enemyhealth[qwe] <= 0:
                            money += 1
                            if enemyrank[qwe] == "red":
                                delete_enemy(qwe)
                                break
                            if enemyrank[qwe] == "blue":
                                enemyx.append(enemyx[qwe])
                                enemyy.append(enemyy[qwe])
                                enemyway.append(enemyway[qwe])
                                enemyrank.append("red")
                                enemyhealth.append(int(enemyhealth[qwe] + 1))
                                delete_enemy(qwe)
                                break
                            if enemyrank[qwe] == "green":
                                enemyx.append(enemyx[qwe])
                                enemyy.append(enemyy[qwe])
                                enemyway.append(enemyway[qwe])
                                enemyrank.append("blue")
                                enemyhealth.append(int(enemyhealth[qwe] + 1))
                                delete_enemy(qwe)
                                break
                            if enemyrank[qwe] == "yellow":
                                enemyx.append(enemyx[qwe])
                                enemyy.append(enemyy[qwe])
                                enemyway.append(enemyway[qwe])
                                enemyrank.append("green")
                                enemyhealth.append(int(enemyhealth[qwe] + 1))
                                delete_enemy(qwe)
                                break
                            if enemyrank[qwe] == "pink":
                                if enemyway[qwe] == "right" or enemyway[qwe] == "left":
                                    enemyx.append(enemyx[qwe] - 10)
                                    enemyy.append(enemyy[qwe])
                                    enemyway.append(enemyway[qwe])
                                    enemyrank.append("yellow")
                                    enemyhealth.append(int(enemyhealth[qwe] + 1))
                                    enemyx.append(enemyx[qwe] + 10)
                                    enemyy.append(enemyy[qwe])
                                    enemyway.append(enemyway[qwe])
                                    enemyrank.append("yellow")
                                    enemyhealth.append(int(enemyhealth[qwe] + 1))
                                if enemyway[qwe] == "up" or enemyway[qwe] == "down":
                                    enemyx.append(enemyx[qwe])
                                    enemyy.append(enemyy[qwe] + 10)
                                    enemyway.append(enemyway[qwe])
                                    enemyrank.append("yellow")
                                    enemyhealth.append(int(enemyhealth[qwe] + 1))
                                    enemyx.append(enemyx[qwe])
                                    enemyy.append(enemyy[qwe] - 10)
                                    enemyway.append(enemyway[qwe])
                                    enemyrank.append("yellow")
                                    enemyhealth.append(int(enemyhealth[qwe] + 1))
                                delete_enemy(qwe)
                                break
                            if enemyrank[qwe] == "black":
                                if enemyway[qwe] == "right" or enemyway[qwe] == "left":
                                    enemyx.append(enemyx[qwe] - 10)
                                    enemyy.append(enemyy[qwe])
                                    enemyway.append(enemyway[qwe])
                                    enemyrank.append("pink")
                                    enemyhealth.append(int(enemyhealth[qwe] + 1))
                                    enemyx.append(enemyx[qwe] + 10)
                                    enemyy.append(enemyy[qwe])
                                    enemyway.append(enemyway[qwe])
                                    enemyrank.append("pink")
                                    enemyhealth.append(int(enemyhealth[qwe] + 1))
                                if enemyway[qwe] == "up" or enemyway[qwe] == "down":
                                    enemyx.append(enemyx[qwe])
                                    enemyy.append(enemyy[qwe] + 10)
                                    enemyway.append(enemyway[qwe])
                                    enemyrank.append("pink")
                                    enemyhealth.append(int(enemyhealth[qwe] + 1))
                                    enemyx.append(enemyx[qwe])
                                    enemyy.append(enemyy[qwe] - 10)
                                    enemyway.append(enemyway[qwe])
                                    enemyrank.append("pink")
                                    enemyhealth.append(int(enemyhealth[qwe] + 1))
                                delete_enemy(qwe)
                                break
                            if enemyrank[qwe] == "white":
                                if enemyway[qwe] == "right" or enemyway[qwe] == "left":
                                    enemyx.append(enemyx[qwe] - 10)
                                    enemyy.append(enemyy[qwe])
                                    enemyway.append(enemyway[qwe])
                                    enemyrank.append("black")
                                    enemyhealth.append(int(enemyhealth[qwe] + 1))
                                    enemyx.append(enemyx[qwe] + 10)
                                    enemyy.append(enemyy[qwe])
                                    enemyway.append(enemyway[qwe])
                                    enemyrank.append("black")
                                    enemyhealth.append(int(enemyhealth[qwe] + 1))
                                if enemyway[qwe] == "up" or enemyway[qwe] == "down":
                                    enemyx.append(enemyx[qwe])
                                    enemyy.append(enemyy[qwe] + 10)
                                    enemyway.append(enemyway[qwe])
                                    enemyrank.append("black")
                                    enemyhealth.append(int(enemyhealth[qwe] + 1))
                                    enemyx.append(enemyx[qwe])
                                    enemyy.append(enemyy[qwe] - 10)
                                    enemyway.append(enemyway[qwe])
                                    enemyrank.append("black")
                                    enemyhealth.append(int(enemyhealth[qwe] + 1))
                                delete_enemy(qwe)
                                break
                            if enemyrank[qwe] == "moab":
                                if enemyway[qwe] == "right" or enemyway[qwe] == "left":
                                    enemyx.append(enemyx[qwe] - 10)
                                    enemyy.append(enemyy[qwe])
                                    enemyway.append(enemyway[qwe])
                                    enemyrank.append("white")
                                    enemyhealth.append(int(enemyhealth[qwe] + 1))
                                    enemyx.append(enemyx[qwe] + 10)
                                    enemyy.append(enemyy[qwe])
                                    enemyway.append(enemyway[qwe])
                                    enemyrank.append("white")
                                    enemyhealth.append(int(enemyhealth[qwe] + 1))
                                    enemyx.append(enemyx[qwe] - 30)
                                    enemyy.append(enemyy[qwe])
                                    enemyway.append(enemyway[qwe])
                                    enemyrank.append("white")
                                    enemyhealth.append(int(enemyhealth[qwe] + 1))
                                    enemyx.append(enemyx[qwe] + 30)
                                    enemyy.append(enemyy[qwe])
                                    enemyway.append(enemyway[qwe])
                                    enemyrank.append("white")
                                    enemyhealth.append(int(enemyhealth[qwe] + 1))
                                if enemyway[qwe] == "up" or enemyway[qwe] == "down":
                                    enemyx.append(enemyx[qwe])
                                    enemyy.append(enemyy[qwe] + 10)
                                    enemyway.append(enemyway[qwe])
                                    enemyrank.append("white")
                                    enemyhealth.append(int(enemyhealth[qwe] + 1))
                                    enemyx.append(enemyx[qwe])
                                    enemyy.append(enemyy[qwe] - 10)
                                    enemyway.append(enemyway[qwe])
                                    enemyrank.append("white")
                                    enemyhealth.append(int(enemyhealth[qwe] + 1))
                                    enemyx.append(enemyx[qwe])
                                    enemyy.append(enemyy[qwe] + 30)
                                    enemyway.append(enemyway[qwe])
                                    enemyrank.append("white")
                                    enemyhealth.append(int(enemyhealth[qwe] + 1))
                                    enemyx.append(enemyx[qwe])
                                    enemyy.append(enemyy[qwe] - 30)
                                    enemyway.append(enemyway[qwe])
                                    enemyrank.append("white")
                                    enemyhealth.append(int(enemyhealth[qwe] + 1))
                                delete_enemy(qwe)
                                break
                            if enemyrank[qwe] == "bfb":
                                if enemyway[qwe] == "right" or enemyway[qwe] == "left":
                                    enemyx.append(enemyx[qwe] - 10)
                                    enemyy.append(enemyy[qwe])
                                    enemyway.append(enemyway[qwe])
                                    enemyrank.append("moab")
                                    enemyhealth.append(int(enemyhealth[qwe] + 1))
                                    enemyx.append(enemyx[qwe] + 10)
                                    enemyy.append(enemyy[qwe])
                                    enemyway.append(enemyway[qwe])
                                    enemyrank.append("moab")
                                    enemyhealth.append(int(enemyhealth[qwe] + 1))
                                    enemyx.append(enemyx[qwe] - 30)
                                    enemyy.append(enemyy[qwe])
                                    enemyway.append(enemyway[qwe])
                                    enemyrank.append("moab")
                                    enemyhealth.append(int(enemyhealth[qwe] + 1))
                                    enemyx.append(enemyx[qwe] + 30)
                                    enemyy.append(enemyy[qwe])
                                    enemyway.append(enemyway[qwe])
                                    enemyrank.append("moab")
                                    enemyhealth.append(int(enemyhealth[qwe] + 1))
                                if enemyway[qwe] == "up" or enemyway[qwe] == "down":
                                    enemyx.append(enemyx[qwe])
                                    enemyy.append(enemyy[qwe] + 10)
                                    enemyway.append(enemyway[qwe])
                                    enemyrank.append("moab")
                                    enemyhealth.append(int(enemyhealth[qwe] + 1))
                                    enemyx.append(enemyx[qwe])
                                    enemyy.append(enemyy[qwe] - 10)
                                    enemyway.append(enemyway[qwe])
                                    enemyrank.append("moab")
                                    enemyhealth.append(int(enemyhealth[qwe] + 1))
                                    enemyx.append(enemyx[qwe])
                                    enemyy.append(enemyy[qwe] + 30)
                                    enemyway.append(enemyway[qwe])
                                    enemyrank.append("moab")
                                    enemyhealth.append(int(enemyhealth[qwe] + 1))
                                    enemyx.append(enemyx[qwe])
                                    enemyy.append(enemyy[qwe] - 30)
                                    enemyway.append(enemyway[qwe])
                                    enemyrank.append("moab")
                                    enemyhealth.append(int(enemyhealth[qwe] + 1))
                                delete_enemy(qwe)
                                break
                        break
    if upgrade1 >= 7:
        for er in range(len(enemyx) - 1, -1, -1):
            for et in range(len(laserx) - 1, -1, -1):
                if 6 < laserx[et] - enemyx[er] < 21:
                    if abs(lasery[et] - enemyy[er]) < 31:
                        enemyhealth[er] -= 1
                        laserhealth[et] -= 1
                        if laserhealth[et] <= 0:
                            del (laserx[et])
                            del (lasery[et])
                            del (laserhealth[et])
                        if enemyhealth[er] <= 0:
                            money += 1
                            if enemyrank[er] == "red":
                                delete_enemy(er)
                                break
                            if enemyrank[er] == "blue":
                                enemyx.append(enemyx[er])
                                enemyy.append(enemyy[er])
                                enemyway.append(enemyway[er])
                                enemyrank.append("red")
                                enemyhealth.append(1)
                                delete_enemy(er)
                                break
                            if enemyrank[er] == "green":
                                enemyx.append(enemyx[er])
                                enemyy.append(enemyy[er])
                                enemyway.append(enemyway[er])
                                enemyrank.append("blue")
                                enemyhealth.append(1)
                                delete_enemy(er)
                                break
                            if enemyrank[er] == "yellow":
                                enemyx.append(enemyx[er])
                                enemyy.append(enemyy[er])
                                enemyway.append(enemyway[er])
                                enemyrank.append("green")
                                enemyhealth.append(2)
                                delete_enemy(er)
                                break
                            if enemyrank[er] == "pink":
                                if enemyway[er] == "right" or enemyway[er] == "left":
                                    enemyx.append(enemyx[er] - 10)
                                    enemyy.append(enemyy[er])
                                    enemyway.append(enemyway[er])
                                    enemyrank.append("yellow")
                                    enemyhealth.append(3)
                                    enemyx.append(enemyx[er] + 10)
                                    enemyy.append(enemyy[er])
                                    enemyway.append(enemyway[er])
                                    enemyrank.append("yellow")
                                    enemyhealth.append(3)
                                if enemyway[er] == "up" or enemyway[er] == "down":
                                    enemyx.append(enemyx[er])
                                    enemyy.append(enemyy[er] + 10)
                                    enemyway.append(enemyway[er])
                                    enemyrank.append("yellow")
                                    enemyhealth.append(3)
                                    enemyx.append(enemyx[er])
                                    enemyy.append(enemyy[er] - 10)
                                    enemyway.append(enemyway[er])
                                    enemyrank.append("yellow")
                                    enemyhealth.append(3)
                                delete_enemy(er)
                                break
                            if enemyrank[er] == "black":
                                if enemyway[er] == "right" or enemyway[er] == "left":
                                    enemyx.append(enemyx[er] - 10)
                                    enemyy.append(enemyy[er])
                                    enemyway.append(enemyway[er])
                                    enemyrank.append("pink")
                                    enemyhealth.append(int(enemyhealth[er] + 1))
                                    enemyx.append(enemyx[er] + 10)
                                    enemyy.append(enemyy[er])
                                    enemyway.append(enemyway[er])
                                    enemyrank.append("pink")
                                    enemyhealth.append(int(enemyhealth[er] + 1))
                                if enemyway[er] == "up" or enemyway[er] == "down":
                                    enemyx.append(enemyx[er])
                                    enemyy.append(enemyy[er] + 10)
                                    enemyway.append(enemyway[er])
                                    enemyrank.append("pink")
                                    enemyhealth.append(int(enemyhealth[er] + 1))
                                    enemyx.append(enemyx[er])
                                    enemyy.append(enemyy[er] - 10)
                                    enemyway.append(enemyway[er])
                                    enemyrank.append("pink")
                                    enemyhealth.append(int(enemyhealth[er] + 1))
                                delete_enemy(er)
                                break
                            if enemyrank[er] == "white":
                                if enemyway[er] == "right" or enemyway[er] == "left":
                                    enemyx.append(enemyx[er] - 10)
                                    enemyy.append(enemyy[er])
                                    enemyway.append(enemyway[er])
                                    enemyrank.append("black")
                                    enemyhealth.append(int(enemyhealth[er] + 1))
                                    enemyx.append(enemyx[er] + 10)
                                    enemyy.append(enemyy[er])
                                    enemyway.append(enemyway[er])
                                    enemyrank.append("black")
                                    enemyhealth.append(int(enemyhealth[er] + 1))
                                if enemyway[er] == "up" or enemyway[er] == "down":
                                    enemyx.append(enemyx[er])
                                    enemyy.append(enemyy[er] + 10)
                                    enemyway.append(enemyway[er])
                                    enemyrank.append("black")
                                    enemyhealth.append(int(enemyhealth[er] + 1))
                                    enemyx.append(enemyx[er])
                                    enemyy.append(enemyy[er] - 10)
                                    enemyway.append(enemyway[er])
                                    enemyrank.append("black")
                                    enemyhealth.append(int(enemyhealth[er] + 1))
                                delete_enemy(er)
                                break
                            if enemyrank[er] == "moab":
                                if enemyway[er] == "right" or enemyway[er] == "left":
                                    enemyx.append(enemyx[er] - 10)
                                    enemyy.append(enemyy[er])
                                    enemyway.append(enemyway[er])
                                    enemyrank.append("white")
                                    enemyhealth.append(int(enemyhealth[er] + 1))
                                    enemyx.append(enemyx[er] + 10)
                                    enemyy.append(enemyy[er])
                                    enemyway.append(enemyway[er])
                                    enemyrank.append("white")
                                    enemyhealth.append(int(enemyhealth[er] + 1))
                                    enemyx.append(enemyx[er] - 30)
                                    enemyy.append(enemyy[er])
                                    enemyway.append(enemyway[er])
                                    enemyrank.append("white")
                                    enemyhealth.append(int(enemyhealth[er] + 1))
                                    enemyx.append(enemyx[er] + 30)
                                    enemyy.append(enemyy[er])
                                    enemyway.append(enemyway[er])
                                    enemyrank.append("white")
                                    enemyhealth.append(int(enemyhealth[er] + 1))
                                if enemyway[er] == "up" or enemyway[er] == "down":
                                    enemyx.append(enemyx[er])
                                    enemyy.append(enemyy[er] + 10)
                                    enemyway.append(enemyway[er])
                                    enemyrank.append("white")
                                    enemyhealth.append(int(enemyhealth[er] + 1))
                                    enemyx.append(enemyx[er])
                                    enemyy.append(enemyy[er] - 10)
                                    enemyway.append(enemyway[er])
                                    enemyrank.append("white")
                                    enemyhealth.append(int(enemyhealth[er] + 1))
                                    enemyx.append(enemyx[er])
                                    enemyy.append(enemyy[er] + 30)
                                    enemyway.append(enemyway[er])
                                    enemyrank.append("white")
                                    enemyhealth.append(int(enemyhealth[er] + 1))
                                    enemyx.append(enemyx[er])
                                    enemyy.append(enemyy[er] - 30)
                                    enemyway.append(enemyway[er])
                                    enemyrank.append("white")
                                    enemyhealth.append(int(enemyhealth[er] + 1))
                                delete_enemy(er)
                                break
                            if enemyrank[er] == "bfb":
                                if enemyway[er] == "right" or enemyway[er] == "left":
                                    enemyx.append(enemyx[er] - 10)
                                    enemyy.append(enemyy[er])
                                    enemyway.append(enemyway[er])
                                    enemyrank.append("moab")
                                    enemyhealth.append(int(enemyhealth[er] + 1))
                                    enemyx.append(enemyx[er] + 10)
                                    enemyy.append(enemyy[er])
                                    enemyway.append(enemyway[er])
                                    enemyrank.append("moab")
                                    enemyhealth.append(int(enemyhealth[er] + 1))
                                    enemyx.append(enemyx[er] - 30)
                                    enemyy.append(enemyy[er])
                                    enemyway.append(enemyway[er])
                                    enemyrank.append("moab")
                                    enemyhealth.append(int(enemyhealth[er] + 1))
                                    enemyx.append(enemyx[er] + 30)
                                    enemyy.append(enemyy[er])
                                    enemyway.append(enemyway[er])
                                    enemyrank.append("moab")
                                    enemyhealth.append(int(enemyhealth[er] + 1))
                                if enemyway[er] == "up" or enemyway[er] == "down":
                                    enemyx.append(enemyx[er])
                                    enemyy.append(enemyy[er] + 10)
                                    enemyway.append(enemyway[er])
                                    enemyrank.append("moab")
                                    enemyhealth.append(int(enemyhealth[er] + 1))
                                    enemyx.append(enemyx[er])
                                    enemyy.append(enemyy[er] - 10)
                                    enemyway.append(enemyway[er])
                                    enemyrank.append("moab")
                                    enemyhealth.append(int(enemyhealth[er] + 1))
                                    enemyx.append(enemyx[er])
                                    enemyy.append(enemyy[er] + 30)
                                    enemyway.append(enemyway[er])
                                    enemyrank.append("moab")
                                    enemyhealth.append(int(enemyhealth[er] + 1))
                                    enemyx.append(enemyx[er])
                                    enemyy.append(enemyy[er] - 30)
                                    enemyway.append(enemyway[er])
                                    enemyrank.append("moab")
                                    enemyhealth.append(int(enemyhealth[er] + 1))
                                delete_enemy(er)
                                break
                        break
    for af in range(len(enemyx) - 1, -1, -1):
        for ag in range(len(bombx) - 1, -1, -1):
            if upgrade2 == 1:
                if abs(bombx[ag] - enemyx[af]) < 31:
                    if abs(bomby[ag] - enemyy[af]) < 31:
                        enemyhealth[af] -= 1
                        bombdel[ag] = "yes"
            if upgrade2 == 2:
                if abs(bombx[ag] - enemyx[af]) < 41:
                    if abs(bomby[ag] - enemyy[af]) < 41:
                        enemyhealth[af] -= 1
                        bombdel[ag] = "yes"
            if upgrade2 >= 3 and upgrade3 <= 8:
                if abs(bombx[ag] - enemyx[af]) < 61:
                    if abs(bomby[ag] - enemyy[af]) < 61:
                        enemyhealth[af] -= 1
                        bombdel[ag] = "yes"
            if upgrade2 >= 9:
                if abs(bombx[ag] - enemyx[af]) < 121:
                    if abs(bomby[ag] - enemyy[af]) < 121:
                        enemyhealth[af] -= 1
                        bombdel[ag] = "yes"
            if enemyhealth[af] <= 0:
                money += 1
                if enemyrank[af] == "red":
                    delete_enemy(af)
                    break
                if enemyrank[af] == "blue":
                    enemyx.append(enemyx[af])
                    enemyy.append(enemyy[af])
                    enemyway.append(enemyway[af])
                    enemyrank.append("red")
                    enemyhealth.append(1)
                    delete_enemy(af)
                    break
                if enemyrank[af] == "green":
                    enemyx.append(enemyx[af])
                    enemyy.append(enemyy[af])
                    enemyway.append(enemyway[af])
                    enemyrank.append("blue")
                    enemyhealth.append(1)
                    delete_enemy(af)
                    break
                if enemyrank[af] == "yellow":
                    enemyx.append(enemyx[af])
                    enemyy.append(enemyy[af])
                    enemyway.append(enemyway[af])
                    enemyrank.append("green")
                    enemyhealth.append(2)
                    delete_enemy(af)
                if enemyrank[af] == "pink":
                    if enemyway[af] == "right" or enemyway[af] == "left":
                        enemyx.append(enemyx[af] - 10)
                        enemyy.append(enemyy[af])
                        enemyway.append(enemyway[af])
                        enemyrank.append("yellow")
                        enemyhealth.append(3)
                        enemyx.append(enemyx[af] + 10)
                        enemyy.append(enemyy[af])
                        enemyway.append(enemyway[af])
                        enemyrank.append("yellow")
                        enemyhealth.append(3)
                    if enemyway[af] == "up" or enemyway[af] == "down":
                        enemyx.append(enemyx[af])
                        enemyy.append(enemyy[af] + 10)
                        enemyway.append(enemyway[af])
                        enemyrank.append("yellow")
                        enemyhealth.append(3)
                        enemyx.append(enemyx[af])
                        enemyy.append(enemyy[af] - 10)
                        enemyway.append(enemyway[af])
                        enemyrank.append("yellow")
                        enemyhealth.append(3)
                    delete_enemy(af)
                    break
                if enemyrank[af] == "black":
                    if enemyway[af] == "right" or enemyway[af] == "left":
                        enemyx.append(enemyx[af] - 10)
                        enemyy.append(enemyy[af])
                        enemyway.append(enemyway[af])
                        enemyrank.append("pink")
                        enemyhealth.append(int(enemyhealth[af] + 1))
                        enemyx.append(enemyx[af] + 10)
                        enemyy.append(enemyy[af])
                        enemyway.append(enemyway[af])
                        enemyrank.append("pink")
                        enemyhealth.append(int(enemyhealth[af] + 1))
                    if enemyway[af] == "up" or enemyway[af] == "down":
                        enemyx.append(enemyx[af])
                        enemyy.append(enemyy[af] + 10)
                        enemyway.append(enemyway[af])
                        enemyrank.append("pink")
                        enemyhealth.append(int(enemyhealth[af] + 1))
                        enemyx.append(enemyx[af])
                        enemyy.append(enemyy[af] - 10)
                        enemyway.append(enemyway[af])
                        enemyrank.append("pink")
                        enemyhealth.append(int(enemyhealth[af] + 1))
                    delete_enemy(af)
                    break
                if enemyrank[af] == "white":
                    if enemyway[af] == "right" or enemyway[af] == "left":
                        enemyx.append(enemyx[af] - 10)
                        enemyy.append(enemyy[af])
                        enemyway.append(enemyway[af])
                        enemyrank.append("black")
                        enemyhealth.append(int(enemyhealth[af] + 1))
                        enemyx.append(enemyx[af] + 10)
                        enemyy.append(enemyy[af])
                        enemyway.append(enemyway[af])
                        enemyrank.append("black")
                        enemyhealth.append(int(enemyhealth[af] + 1))
                    if enemyway[af] == "up" or enemyway[af] == "down":
                        enemyx.append(enemyx[af])
                        enemyy.append(enemyy[af] + 10)
                        enemyway.append(enemyway[af])
                        enemyrank.append("black")
                        enemyhealth.append(int(enemyhealth[af] + 1))
                        enemyx.append(enemyx[af])
                        enemyy.append(enemyy[af] - 10)
                        enemyway.append(enemyway[af])
                        enemyrank.append("black")
                        enemyhealth.append(int(enemyhealth[af] + 1))
                    delete_enemy(af)
                    break
                if enemyrank[af] == "moab":
                    if enemyway[af] == "right" or enemyway[af] == "left":
                        enemyx.append(enemyx[af] - 10)
                        enemyy.append(enemyy[af])
                        enemyway.append(enemyway[af])
                        enemyrank.append("white")
                        enemyhealth.append(int(enemyhealth[af] + 1))
                        enemyx.append(enemyx[af] + 10)
                        enemyy.append(enemyy[af])
                        enemyway.append(enemyway[af])
                        enemyrank.append("white")
                        enemyhealth.append(int(enemyhealth[af] + 1))
                        enemyx.append(enemyx[af] - 30)
                        enemyy.append(enemyy[af])
                        enemyway.append(enemyway[af])
                        enemyrank.append("white")
                        enemyhealth.append(int(enemyhealth[af] + 1))
                        enemyx.append(enemyx[af] + 30)
                        enemyy.append(enemyy[af])
                        enemyway.append(enemyway[af])
                        enemyrank.append("white")
                        enemyhealth.append(int(enemyhealth[af] + 1))
                    if enemyway[af] == "up" or enemyway[af] == "down":
                        enemyx.append(enemyx[af])
                        enemyy.append(enemyy[af] + 10)
                        enemyway.append(enemyway[af])
                        enemyrank.append("white")
                        enemyhealth.append(int(enemyhealth[af] + 1))
                        enemyx.append(enemyx[af])
                        enemyy.append(enemyy[af] - 10)
                        enemyway.append(enemyway[af])
                        enemyrank.append("white")
                        enemyhealth.append(int(enemyhealth[af] + 1))
                        enemyx.append(enemyx[af])
                        enemyy.append(enemyy[af] + 30)
                        enemyway.append(enemyway[af])
                        enemyrank.append("white")
                        enemyhealth.append(int(enemyhealth[af] + 1))
                        enemyx.append(enemyx[af])
                        enemyy.append(enemyy[af] - 30)
                        enemyway.append(enemyway[af])
                        enemyrank.append("white")
                        enemyhealth.append(int(enemyhealth[af] + 1))
                    delete_enemy(af)
                    break
                if enemyrank[af] == "bfb":
                    if enemyway[af] == "right" or enemyway[af] == "left":
                        enemyx.append(enemyx[af] - 10)
                        enemyy.append(enemyy[af])
                        enemyway.append(enemyway[af])
                        enemyrank.append("moab")
                        enemyhealth.append(int(enemyhealth[af] + 1))
                        enemyx.append(enemyx[af] + 10)
                        enemyy.append(enemyy[af])
                        enemyway.append(enemyway[af])
                        enemyrank.append("moab")
                        enemyhealth.append(int(enemyhealth[af] + 1))
                        enemyx.append(enemyx[af] - 30)
                        enemyy.append(enemyy[af])
                        enemyway.append(enemyway[af])
                        enemyrank.append("moab")
                        enemyhealth.append(int(enemyhealth[af] + 1))
                        enemyx.append(enemyx[af] + 30)
                        enemyy.append(enemyy[af])
                        enemyway.append(enemyway[af])
                        enemyrank.append("moab")
                        enemyhealth.append(int(enemyhealth[af] + 1))
                    if enemyway[af] == "up" or enemyway[af] == "down":
                        enemyx.append(enemyx[af])
                        enemyy.append(enemyy[af] + 10)
                        enemyway.append(enemyway[af])
                        enemyrank.append("moab")
                        enemyhealth.append(int(enemyhealth[af] + 1))
                        enemyx.append(enemyx[af])
                        enemyy.append(enemyy[af] - 10)
                        enemyway.append(enemyway[af])
                        enemyrank.append("moab")
                        enemyhealth.append(int(enemyhealth[af] + 1))
                        enemyx.append(enemyx[af])
                        enemyy.append(enemyy[af] + 30)
                        enemyway.append(enemyway[af])
                        enemyrank.append("moab")
                        enemyhealth.append(int(enemyhealth[af] + 1))
                        enemyx.append(enemyx[af])
                        enemyy.append(enemyy[af] - 30)
                        enemyway.append(enemyway[af])
                        enemyrank.append("moab")
                        enemyhealth.append(int(enemyhealth[af] + 1))
                    delete_enemy(af)
                    break
            break

    for dd in range(len(bombdel) - 1, -1, -1):
        if bombdel[dd] == "yes":
            del (bombdel[dd])
            del (bombx[dd])
            del (bomby[dd])

    pygame.draw.rect(screen, (255, 255, 255), (mousex - 20, mousey - 30, 40, 60))

    font = pygame.font.Font("freesansbold.ttf", 32)
    live = font.render(str(lives), False, (0, 0, 0))
    screen.blit(live, (500, 20))
    moneys = font.render(str(money), False, (0, 0, 0))
    screen.blit(moneys, (800, 20))
    up1 = font.render(str(upgrade1), False, (0, 0, 0))
    screen.blit(up1, (10, 30))
    up2 = font.render(str(upgrade2), False, (0, 0, 0))
    screen.blit(up2, (40, 30))
    up3 = font.render(str(upgrade3), False, (0, 0, 0))
    screen.blit(up3, (70, 30))

    if lives <= 0:
        money = 3200

        upgrade1 = 0
        upgrade2 = 0
        upgrade3 = 0

        delay1 = 0
        delay2 = 0
        delay3 = 0

        enemyx = []
        enemyy = []
        enemyrank = []
        enemyway = []
        enemyhealth = []

        bulletx = []
        bullety = []

        laserx = []
        lasery = []
        laserhealth = []

        bombx = []
        bomby = []
        bombdel = []

        maulerx = []
        maulery = []
        maulerdel = []
        stopwatch -= 1
        if event.type == pygame.MOUSEBUTTONDOWN:
            lives = 100
            print(stopwatch)
            stopwatch = 0
        stopwach = font.render(str(stopwatch), False, (0, 0, 0))
        screen.blit(stopwach, (510, 260))

    pygame.display.flip()
    clock.tick(100)