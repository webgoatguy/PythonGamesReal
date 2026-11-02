import pygame
import sys
import random

pygame.init()

dietimer = 300

clock = pygame.time.Clock()

screen = pygame.display.set_mode((1080,540))

shipx = 540
shipy = 450
shipxx = 0
shipyy = -3
shiphit = 200

bulletx = []
bullety = []
bulletxx = []
bulletyy = []
bulletdel = []

ebulletx = []
ebullety = []
ebulletxx = []
ebulletyy = []
ebulletdel = []

minex = []
miney = []
minedel = []
miner = []

eshipx = []
eshipy = []
eshipxx = []
eshipyy = []
eshipdel = []
eshiphit = []
eshiphitt = []
eshiptype = []
eshipsum = []

stopwatch = 0

#highscore = 12.4k, mean score ~100k

minetimer = 0
shoottimer = 0
quadshoottimer = 0

shoot = False
dropmine = False

aimturn = "?"
aimturn1 = "?"

alientimer = 0
bigalien = 0

font = pygame.font.Font("freesansbold.ttf", 32)

def make_eship(x, y, xx, yy, hitpoints, type):
    eshipx.append(x)
    eshipy.append(y)
    eshipxx.append(xx)
    eshipyy.append(yy)
    eshipdel.append(1)
    eshiphit.append(hitpoints)
    eshiphitt.append(hitpoints)
    eshiptype.append(type)
    eshipsum.append(abs(xx) + abs(yy))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                aimturn = "right"
            if event.key == pygame.K_a:
                aimturn = "left"
            if event.key == pygame.K_j:
                shoot = True
            if event.key == pygame.K_i:
                dropmine = True
            if event.key == pygame.K_o:
                print(stopwatch)
                sys.exit()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                aimturn = "?"
            if event.key == pygame.K_a:
                aimturn = "?"
            if event.key == pygame.K_j:
                shoot = False
            if event.key == pygame.K_i:
                dropmine = False

    scoretext = font.render(str(stopwatch), False, (255, 0, 255))

    alientimer -= 1
    bigalien -= 1

    if alientimer <= 0:
        choice = random.randint(1, 100)
        if stopwatch < 2000:
            if choice < 70:
                make_eship(0, random.randint(1, 540), random.randint(-6, 6)/4, random.randint(-6, 6)/4, random.randint(1, 3), "norm")
            elif choice < 90:
                make_eship(0, random.randint(1, 540), random.randint(-6, 6)/4, random.randint(-6, 6)/4, random.randint(1, 4), "split")
            else:
                make_eship(0, random.randint(1, 540), random.randint(-6, 6)/4, random.randint(-6, 6)/4, random.randint(1, 6), "splitt")
        elif stopwatch < 4000:
            if choice < 50:
                make_eship(0, random.randint(1, 540), random.randint(-6, 6)/4, random.randint(-6, 6)/4, random.randint(1, 3), "norm")
            elif choice < 70:
                make_eship(0, random.randint(1, 540), random.randint(-6, 6)/4, random.randint(-6, 6)/4, random.randint(1, 4), "split")
            elif choice < 85:
                make_eship(0, random.randint(1, 540), random.randint(-6, 6)/4, random.randint(-6, 6)/4, random.randint(1, 6), "splitt")
            elif choice < 95:
                make_eship(0, random.randint(1, 540), random.randint(-6, 6)/4, random.randint(-6, 6)/4, random.randint(1, 8), "splittt")
            else:
                make_eship(0, random.randint(1, 540), random.randint(-6, 6)/4, random.randint(-6, 6)/4, random.randint(1, 10), "splitttt")
        elif stopwatch < 6000:
            if choice < 30:
                make_eship(0, random.randint(1, 540), random.randint(-6, 6)/4, random.randint(-6, 6)/4, random.randint(1, 4), "split")
            elif choice < 60:
                make_eship(0, random.randint(1, 540), random.randint(-6, 6)/4, random.randint(-6, 6)/4, random.randint(1, 6), "splitt")
            elif choice < 70:
                make_eship(0, random.randint(1, 540), random.randint(-6, 6)/4, random.randint(-6, 6)/4, random.randint(1, 8), "splittt")
            elif choice < 80:
                make_eship(0, random.randint(1, 540), random.randint(-6, 6)/4, random.randint(-6, 6)/4, random.randint(1, 10), "splitttt")
            elif choice < 90:
                make_eship(0, random.randint(1, 540), random.randint(-6, 6)/4, random.randint(-6, 6)/4, random.randint(1, 12), "splittttt")
            else:
                make_eship(0, random.randint(1, 540), random.randint(-6, 6)/4, random.randint(-6, 6)/4, random.randint(1, 15), "splitttttt")
        elif stopwatch < 8000:
            if choice < 35:
                make_eship(0, random.randint(1, 540), random.randint(-6, 6)/4, random.randint(-6, 6)/4, random.randint(1, 6), "splitt")
            elif choice < 60:
                make_eship(0, random.randint(1, 540), random.randint(-6, 6)/4, random.randint(-6, 6)/4, random.randint(1, 8), "splittt")
            elif choice < 80:
                make_eship(0, random.randint(1, 540), random.randint(-6, 6)/4, random.randint(-6, 6)/4, random.randint(1, 10), "splitttt")
            elif choice < 88:
                make_eship(0, random.randint(1, 540), random.randint(-6, 6)/4, random.randint(-6, 6)/4, random.randint(1, 12), "splittttt")
            elif choice < 93:
                make_eship(0, random.randint(1, 540), random.randint(-6, 6)/4, random.randint(-6, 6)/4, random.randint(1, 15), "splitttttt")
            elif choice < 98:
                make_eship(0, random.randint(1, 540), random.randint(-6, 6)/4, random.randint(-6, 6)/4, random.randint(1, 18), "splittttttt")
            else:
                make_eship(0, random.randint(1, 540), random.randint(-6, 6)/4, random.randint(-6, 6)/4, random.randint(1, 24), "splitttttttt")
        else:
            if choice < 40:
                make_eship(0, random.randint(1, 540), random.randint(-6, 6)/4, random.randint(-6, 6)/4, random.randint(1, 8), "splittt")
            elif choice < 65:
                make_eship(0, random.randint(1, 540), random.randint(-6, 6)/4, random.randint(-6, 6)/4, random.randint(1, 10), "splitttt")
            elif choice < 76:
                make_eship(0, random.randint(1, 540), random.randint(-6, 6)/4, random.randint(-6, 6)/4, random.randint(1, 12), "splittttt")
            elif choice < 86:
                make_eship(0, random.randint(1, 540), random.randint(-6, 6)/4, random.randint(-6, 6)/4, random.randint(1, 15), "splitttttt")
            elif choice < 94:
                make_eship(0, random.randint(1, 540), random.randint(-6, 6)/4, random.randint(-6, 6)/4, random.randint(1, 18), "splittttttt")
            else:
                make_eship(0, random.randint(1, 540), random.randint(-6, 6)/4, random.randint(-6, 6)/4, random.randint(1, 24), "splitttttttt")
        alientimer = random.randint(1, 110)

    stopwatch += 1

    screen.fill((0, 0, 0))

    mousex, mousey = pygame.mouse.get_pos()

    if (stopwatch/100) % 1 == 0:
        if shiphit < 200:
            shiphit += 1.5

    shipx += shipxx
    shipy += shipyy

    if len(eshipx) > 80:
        eshipdel[0] = 0
        eshiphit[1] += 5
        eshiphitt[1] += 5
        eshiphit[2] += 5
        eshiphitt[2] += 5
        eshiphit[3] += 5
        eshiphitt[3] += 5
        eshiphit[4] += 5
        eshiphitt[4] += 5

    minetimer += 1
    shoottimer += 1
    quadshoottimer += 1

    if shoottimer > 6 or stopwatch > 2000 and shoottimer > 3:
        if shoot == True and stopwatch < 4000:
            bulletx.append(shipx)
            bullety.append(shipy)
            bulletxx.append(shipxx*5)
            bulletyy.append(shipyy*5)
            bulletdel.append(1)
            shoottimer = 0

    if shoottimer > 2 or stopwatch > 6000 and shoottimer > 1 or stopwatch > 8000 and shoottimer >= 1:
        if shoot == True and stopwatch > 4000:
            bulletx.append(shipx)
            bullety.append(shipy)
            bulletxx.append(shipxx*12)
            bulletyy.append(shipyy*12)
            bulletdel.append(1)
            shoottimer = 0

    if quadshoottimer > 50 or stopwatch > 4000 and quadshoottimer > 20 or stopwatch > 6000 and quadshoottimer > 12:
        if shoot == True and stopwatch > 2000:
            for cat in range(1, 10):
                bulletx.append(shipx)
                bullety.append(shipy)
                bulletxx.append(random.randint(round(50*shipxx -10), round(50*shipxx +10))/10)
                bulletyy.append(random.randint(round(50*shipyy -10), round(50*shipyy +10))/10)
                bulletdel.append(1)
            quadshoottimer = 0

    for cat in range(0, len(bulletx)):
        bulletx[cat] += bulletxx[cat]
        bullety[cat] += bulletyy[cat]
        pygame.draw.circle(screen, (255, 255, 255), (round(bulletx[cat]), round(bullety[cat])), 5)
        if bulletx[cat] > 1080:
            bulletdel[cat] = 0
        if bulletx[cat] < 0:
            bulletdel[cat] = 0
        if bullety[cat] > 540:
            bulletdel[cat] = 0
        if bullety[cat] < 0:
            bulletdel[cat] = 0
        for dog in range(0, len(eshipdel)):
            if abs(eshipx[dog] - bulletx[cat]) < 25 and abs(eshipy[dog] - bullety[cat]) < 25:
                bulletdel[cat] = 0
                choice = random.randint(1, 4)
                if stopwatch > 6000 and choice == 1:
                    bulletdel[cat] = 1
                eshiphit[dog] -= 1

    for dog in range(0, len(bulletx)):
        for cat in range(0, len(bulletx)):
            if bulletdel[cat] == 0:
                del bulletx[cat]
                del bullety[cat]
                del bulletxx[cat]
                del bulletyy[cat]
                del bulletdel[cat]
                break

    for cat in range(0, len(bulletx)):
        for dog in range(0, len(minex)):
            if abs(minex[dog] - bulletx[cat]) < 20 and abs(miney[dog] - bullety[cat]) < 20:
                bulletdel[cat] = 0
                minedel[dog] = 2

    for cat in range(0, len(minex)):
        if minedel[cat] == 2 or minedel[cat] == 3:
            if miner[cat] > 20:
                pygame.draw.circle(screen, (255, 0, 0), (round(minex[cat]), round(miney[cat])), miner[cat], 20)
            else:
                pygame.draw.circle(screen, (255, 0, 0), (round(minex[cat]), round(miney[cat])), miner[cat])
            for dog in range(0, len(eshipx)):
                if abs(eshipx[dog] - minex[cat]) <= miner[cat]:
                    if abs(eshipy[dog] - miney[cat]) <= miner[cat]:
                        eshiphit[dog] -= 1
            if abs(shipx - minex[cat]) <= miner[cat]:
                if abs(shipy - miney[cat]) <= miner[cat]:
                    shiphit -= 0.5
                    if stopwatch > 4000:
                        shiphit += 0.3
            miner[cat] += 10
            if stopwatch > 6000 and miner[cat] > 200:
                miner[cat] += 15
            if miner[cat] > 200 and stopwatch < 6000:
                minedel[cat] = 0
                if stopwatch > 4000:
                    for dog in range(0, 40):
                        randomx = random.randint(-9, 9)
                        randomy = random.randint(-9, 9)
                        bulletx.append(minex[cat])
                        bullety.append(miney[cat])
                        bulletxx.append(randomx)
                        bulletyy.append(randomy)
                        bulletdel.append(1)
            if stopwatch > 6000 and miner[cat] > 350:
                minedel[cat] = 0
                for dog in range(0, 100):
                        bulletx.append(minex[cat])
                        bullety.append(miney[cat])
                        bulletxx.append(random.randint(-9, 9))
                        bulletyy.append(random.randint(-9, 9))
                        bulletdel.append(1)

    for cat in range(0, len(minex)):
        if minedel[cat] == 0:
            del minex[cat]
            del miney[cat]
            del minedel[cat]
            del miner[cat]
            break

    if minetimer > 150 or stopwatch > 2000 and minetimer > 80 or stopwatch > 4000 and minetimer > 50 or stopwatch > 6000 and minetimer > 30:
        if dropmine == True:
            minex.append(shipx)
            miney.append(shipy)
            minedel.append(1)
            miner.append(1)
            minetimer = 0

    for cat in range(0, len(eshipdel)):
        for dog in range(0, len(eshipx)):
            if cat != dog and abs(eshipx[cat] - eshipx[dog]) < 32 and abs(eshipy[cat] - eshipy[dog]) < 32:
                if eshipx[cat] - eshipx[dog] < 0:
                    eshipx[cat] -= 2
                if eshipy[cat] - eshipy[dog] >= 0:
                    eshipy[cat] += 2
                if eshipx[dog] - eshipx[cat] < 0:
                    eshipx[dog] -= 2
                if eshipy[dog] - eshipy[cat] >= 0:
                    eshipy[dog] += 2
        for dog in range(0, len(minex)):
            if abs(eshipx[cat] - minex[dog]) < 40 and abs(eshipy[cat] - miney[dog]) < 40:
                minedel[dog] = 2
        if eshipx[cat] > 1080:
            eshipx[cat] = 0
        if eshipx[cat] < 0:
            eshipx[cat] = 1080
        if eshipy[cat] > 540:
            eshipy[cat] = 0
        if eshipy[cat] < 0:
            eshipy[cat] = 540
        pygame.draw.rect(screen, (255, 255, 255), (round(eshipx[cat]) - 25, round(eshipy[cat]) + 30, 50, 4))
        if eshiphit[cat] <= 0:
            eshipdel[cat] = 0
            if eshiptype[cat] == "split":
                make_eship(eshipx[cat], eshipy[cat] - 10, eshipxx[cat], eshipyy[cat], round(1+eshiphitt[cat]/2), "norm")
                make_eship(eshipx[cat], eshipy[cat] + 10, eshipxx[cat], eshipyy[cat], round(1+eshiphitt[cat]/2), "norm")
            if eshiptype[cat] == "splitt":
                make_eship(eshipx[cat], eshipy[cat] - 10, eshipxx[cat], eshipyy[cat], round(1+eshiphitt[cat]/2), "split")
                make_eship(eshipx[cat], eshipy[cat] + 10, eshipxx[cat], eshipyy[cat], round(1+eshiphitt[cat]/2), "split")
            if eshiptype[cat] == "splittt":
                make_eship(eshipx[cat], eshipy[cat] - 10, eshipxx[cat], eshipyy[cat], round(1+eshiphitt[cat]/2), "splitt")
                make_eship(eshipx[cat], eshipy[cat] + 10, eshipxx[cat], eshipyy[cat], round(1+eshiphitt[cat]/2), "splitt")
            if eshiptype[cat] == "splitttt":
                make_eship(eshipx[cat], eshipy[cat] - 10, eshipxx[cat], eshipyy[cat], round(1+eshiphitt[cat]/2), "splittt")
                make_eship(eshipx[cat], eshipy[cat] + 10, eshipxx[cat], eshipyy[cat], round(1+eshiphitt[cat]/2), "splittt")
            if eshiptype[cat] == "splittttt":
                make_eship(eshipx[cat], eshipy[cat] - 10, eshipxx[cat], eshipyy[cat], round(1+eshiphitt[cat]/2), "splitttt")
                make_eship(eshipx[cat], eshipy[cat] + 10, eshipxx[cat], eshipyy[cat], round(1+eshiphitt[cat]/2), "splitttt")
            if eshiptype[cat] == "splitttttt":
                make_eship(eshipx[cat], eshipy[cat] - 10, eshipxx[cat], eshipyy[cat], round(1+eshiphitt[cat]/2), "splittttt")
                make_eship(eshipx[cat], eshipy[cat] + 10, eshipxx[cat], eshipyy[cat], round(1+eshiphitt[cat]/2), "splittttt")
            if eshiptype[cat] == "splittttttt":
                make_eship(eshipx[cat], eshipy[cat] - 10, eshipxx[cat], eshipyy[cat], round(1+eshiphitt[cat]/2), "splitttttt")
                make_eship(eshipx[cat], eshipy[cat] + 10, eshipxx[cat], eshipyy[cat], round(1+eshiphitt[cat]/2), "splitttttt")
            if eshiptype[cat] == "splitttttttt":
                make_eship(eshipx[cat], eshipy[cat] - 10, eshipxx[cat], eshipyy[cat], round(1+eshiphitt[cat]/2), "splittttttt")
                make_eship(eshipx[cat], eshipy[cat] + 10, eshipxx[cat], eshipyy[cat], round(1+eshiphitt[cat]/2), "splittttttt")
        if (stopwatch / 150) % 1 == 0:
            ebulletx.append(eshipx[cat])
            ebullety.append(eshipy[cat])
            ebulletxx.append(eshipxx[cat]*4)
            ebulletyy.append(eshipyy[cat]*4)
            ebulletdel.append(1)
        pygame.draw.rect(screen, (255, 0, 0), (round(eshipx[cat]) - 25, round(eshipy[cat]) + 30, round(eshiphit[cat] * 50 / eshiphitt[cat]), 4))
        eshipx[cat] += eshipxx[cat]
        eshipy[cat] += eshipyy[cat]
        if eshiptype[cat] == "norm":
            pygame.draw.circle(screen, (255, 0, 0), (round(eshipx[cat]), round(eshipy[cat])), 15)
        if eshiptype[cat] == "split":
            pygame.draw.circle(screen, (0, 0, 255), (round(eshipx[cat]), round(eshipy[cat])), 20)
        if eshiptype[cat] == "splitt":
            pygame.draw.circle(screen, (100, 255, 100), (round(eshipx[cat]), round(eshipy[cat])), 20)
        if eshiptype[cat] == "splittt":
            pygame.draw.circle(screen, (255, 255, 0), (round(eshipx[cat]), round(eshipy[cat])), 20)
        if eshiptype[cat] == "splitttt":
            pygame.draw.circle(screen, (255, 100, 100), (round(eshipx[cat]), round(eshipy[cat])), 20)
        if eshiptype[cat] == "splittttt":
            pygame.draw.circle(screen, (100, 100, 100), (round(eshipx[cat]), round(eshipy[cat])), 20)
        if eshiptype[cat] == "splitttttt":
            pygame.draw.circle(screen, (255, 255, 255), (round(eshipx[cat]), round(eshipy[cat])), 20)
        if eshiptype[cat] == "splittttttt":
            pygame.draw.circle(screen, (100, 100, 255), (round(eshipx[cat]), round(eshipy[cat])), 25)
        if eshiptype[cat] == "splitttttttt":
            pygame.draw.circle(screen, (200, 0, 0), (round(eshipx[cat]), round(eshipy[cat])), 30)
        if eshipxx[cat] == 0:
            eshipxx[cat] += 0.01
        if eshipxx[cat] != 0 and (shipx - eshipx[cat]) != 0:
            if eshipxx[cat] > 0 and (shipx - eshipx[cat]) > 0 or (shipx - eshipx[cat]) < 0 and eshipxx[cat] < 0:
                if eshipyy[cat] / eshipxx[cat] < (shipy - eshipy[cat]) / (shipx - eshipx[cat]):
                    aimturn1 = "right"
                if eshipyy[cat] / eshipxx[cat] > (shipy - eshipy[cat]) / (shipx - eshipx[cat]):
                    aimturn1 = "left"
            if eshipxx[cat] > 0 and (shipx - eshipx[cat]) < 0 or (shipx - eshipx[cat]) > 0 and eshipxx[cat] < 0:
                if eshipyy[cat] / eshipxx[cat] < (shipy - eshipy[cat]) / (shipx - eshipx[cat]):
                    aimturn1 = "left"
                if eshipyy[cat] / eshipxx[cat] > (shipy - eshipy[cat]) / (shipx - eshipx[cat]):
                    aimturn1 = "right"
            if aimturn1 == "left":
                if eshipxx[cat] < 0 and eshipyy[cat] < 0:
                    eshipxx[cat] -= 0.05
                    eshipyy[cat] += 0.05
                if eshipxx[cat] < 0 and eshipyy[cat] >= 0:
                    eshipxx[cat] += 0.05
                    eshipyy[cat] += 0.05
                if eshipxx[cat] >= 0 and eshipyy[cat] < 0:
                    eshipxx[cat] -= 0.05
                    eshipyy[cat] -= 0.05
                if eshipxx[cat] >= 0 and eshipyy[cat] >= 0:
                    eshipxx[cat] += 0.05
                    eshipyy[cat] -= 0.05
            if aimturn1 == "right":
                if eshipxx[cat] < 0 and eshipyy[cat] < 0:
                    eshipxx[cat] += 0.05
                    eshipyy[cat] -= 0.05
                if eshipxx[cat] < 0 and eshipyy[cat] >= 0:
                    eshipxx[cat] -= 0.05
                    eshipyy[cat] -= 0.05
                if eshipxx[cat] >= 0 and eshipyy[cat] < 0:
                    eshipxx[cat] += 0.05
                    eshipyy[cat] += 0.05
                if eshipxx[cat] >= 0 and eshipyy[cat] >= 0:
                    eshipxx[cat] -= 0.05
                    eshipyy[cat] += 0.05

        eshipxx[cat] = round(eshipxx[cat], 4)
        eshipyy[cat] = round(eshipyy[cat], 4)
        if abs(eshipxx[cat]) + abs(eshipyy[cat]) > eshipsum[cat]:
            if eshipxx[cat] > 0:
                eshipxx[cat] -= 0.02
            if eshipxx[cat] < 0:
                eshipxx[cat] += 0.02
            if eshipyy[cat] > 0:
                eshipyy[cat] -= 0.02
            if eshipyy[cat] < 0:
                eshipyy[cat] += 0.02

    for dog in range(0, len(eshipdel)):
        for cat in range(0, len(eshipdel)):
            if eshipdel[cat] == 0:
                del eshipx[cat]
                del eshipy[cat]
                del eshipxx[cat]
                del eshipyy[cat]
                del eshipdel[cat]
                del eshiphit[cat]
                del eshiphitt[cat]
                del eshiptype[cat]
                del eshipsum[cat]
                break

    for cat in range(0, len(ebulletdel)):
        pygame.draw.circle(screen, (0, 255, 0), (round(ebulletx[cat]), round(ebullety[cat])), 4)
        ebulletx[cat] += ebulletxx[cat]
        ebullety[cat] += ebulletyy[cat]
        if ebulletx[cat] > 1080:
            ebulletdel[cat] = 0
        if ebulletx[cat] < 0:
            ebulletdel[cat] = 0
        if ebullety[cat] > 540:
            ebulletdel[cat] = 0
        if ebullety[cat] < 0:
            ebulletdel[cat] = 0
        if abs(shipx - ebulletx[cat]) < 25 and abs(shipy - ebullety[cat]) < 25:
            shiphit -= 1
            ebulletdel[cat] = 0

    for dog in range(0, len(ebulletdel)):
        for cat in range(0, len(ebulletdel)):
            if ebulletdel[cat] == 0:
                del ebulletx[cat]
                del ebullety[cat]
                del ebulletxx[cat]
                del ebulletyy[cat]
                del ebulletdel[cat]
                break

    for cat in range(0, len(minex)):
        if miner[cat] == 1:
            pygame.draw.circle(screen, (255, 255, 255), (round(minex[cat]), round(miney[cat])), 15)

    if aimturn == "left":
            if shipxx < 0 and shipyy < 0:
                shipxx -= 0.04
                shipyy += 0.04
            if shipxx < 0 and shipyy >= 0:
                shipxx += 0.04
                shipyy += 0.04
            if shipxx >= 0 and shipyy < 0:
                shipxx -= 0.04
                shipyy -= 0.04
            if shipxx >= 0 and shipyy >= 0:
                shipxx += 0.04
                shipyy -= 0.04
    if aimturn == "right":
            if shipxx < 0 and shipyy < 0:
                shipxx += 0.04
                shipyy -= 0.04
            if shipxx < 0 and shipyy >= 0:
                shipxx -= 0.04
                shipyy -= 0.04
            if shipxx >= 0 and shipyy < 0:
                shipxx += 0.04
                shipyy += 0.04
            if shipxx >= 0 and shipyy >= 0:
                shipxx -= 0.04
                shipyy += 0.04

    shipxx = round(shipxx, 2)
    shipyy = round(shipyy, 2)

    if abs(shipxx) + abs(shipyy) > 3:
        if shipxx > 0:
            shipxx -= 0.01
        if shipxx < 0:
            shipxx += 0.01
        if shipyy > 0:
            shipyy -= 0.01
        if shipyy < 0:
            shipyy += 0.01

    if shipx > 1080:
        shipx = 0
    if shipx < 0:
        shipx = 1080
    if shipy > 540:
        shipy = 0
    if shipy < 0:
        shipy = 540

    pygame.draw.circle(screen, (255, 0, 0), (round(shipx), round(shipy)), 20)
    pygame.draw.rect(screen, (255, 255, 255), (round(shipx) - 25, round(shipy) + 30, 50, 4))
    if shiphit > 0:
        pygame.draw.rect(screen, (255, 0, 0), (round(shipx) - 25, round(shipy) + 30, round(shiphit/4), 4))

    if shiphit <= 0:
        dietimer -= 1
        stopwatch -= 1
        pygame.draw.rect(screen, (255, 0, 255), (round(shipx) - 25, round(shipy) + 30, 50, 4))
        shiphit -= 1
        if dietimer <= 0:
            print(stopwatch)
            sys.exit()

    screen.blit(scoretext, (500, 250))

    pygame.display.flip()
    clock.tick(100)