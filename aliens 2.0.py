import pygame
import sys
import random

pygame.init()

dietimer = 300

clock = pygame.time.Clock()

screen = pygame.display.set_mode((1080,540))

#__________________________________________________________________________________________________Sound settings
gunsounds = True
minesounds = True
shotgunsounds = True

highscore = 0

shipx = 540
shipy = 450
shipxx = 0
shipyy = -3
shiphit = 100

bulletx = []
bullety = []
bulletxx = []
bulletyy = []
bulletdel = []
bulletreload = 8
bullshotdamage = 4
shotgunacc = 60
shotgunreload = 100
shotgunbullets = 6

ebulletx = []
ebullety = []
ebulletxx = []
ebulletyy = []
ebulletdel = []

minex = []
miney = []
minedel = []
miner = []
mineradius = 150
minedamage = 3
mineshrapnel = 10

lightning1x = []
lightning1y = []
lightning2x = []
lightning2y = []
lightningtimer = 0
lightreload = 200
lightdamage = 1

eshipx = []
eshipy = []
eshipxx = []
eshipyy = []
eshipdel = []
eshiphit = []
eshiphitt = []
eshiptype = []
eshipsum = []
lightstruck = []

stopwatch = 0
minetimer = 0
shoottimer = 0
shotguntimer = 0

shoot = False
dropmine = False

aimturn = "?"
aimturn1 = "?"

score = 0

alientimer = 0

delay = [0,0,0,0,0,0,0,0,0,0]

slide = "upgrades"

coins = 1000

font = pygame.font.Font("freesansbold.ttf", 32)

explosionsound = pygame.mixer.Sound("images/Explosion+3.wav")
gunsound = pygame.mixer.Sound("images/gun+silencer.wav")
shotgunsound = pygame.mixer.Sound("images/shotgun+2.wav")

def make_eship(x, y, xx, yy, hitpoints, type):
    eshipx.append(x)
    eshipy.append(y)
    eshipxx.append(xx)
    eshipyy.append(yy)
    eshipdel.append(1)
    eshiphit.append(hitpoints)
    eshiphitt.append(hitpoints)
    eshiptype.append(type)
    lightstruck.append(0)
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
                print(score)
                sys.exit()
            if event.key == pygame.K_SPACE and slide == "upgrades":
                slide = "gameplay"
            elif event.key == pygame.K_SPACE and slide == "gameplay":
                slide = "upgrades"
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                aimturn = "?"
            if event.key == pygame.K_a:
                aimturn = "?"
            if event.key == pygame.K_j:
                shoot = False
            if event.key == pygame.K_i:
                dropmine = False

    if lightningtimer <= 0:
        lightning1x = []
        lightning1y = []
        lightning2x = []
        lightning2y = []

    screen.fill((0, 0, 0))

    mousex, mousey = pygame.mouse.get_pos()

    scoretext = font.render(str(score), False, (255, 0, 255))
    cointext1 = font.render("Coins:", False, (255, 0, 255))
    highscoretext = font.render(str(highscore), False, (255, 0, 255))
    highscoretext1 = font.render("Highscore:", False, (255, 0, 255))
    cointext = font.render(str(coins), False, (255, 0, 255))
    bulletretext = font.render("Main gun reload: Every", False, (255, 0, 255))
    bulletretext1 = font.render(str(bulletreload/100), False, (255, 0, 255))
    bulletretext2 = font.render("seconds, Click to upgrade for $150", False, (255, 0, 255))
    bulletdamtext = font.render("All bullets, shrapnel damage:", False, (255, 0, 255))
    bulletdamtext1 = font.render(str(bullshotdamage), False, (255, 0, 255))
    bulletdamtext2 = font.render("damage, Click to upgrade for $400", False, (255, 0, 255))
    shotgunretext = font.render("Shotgun reload: Every", False, (255, 0, 255))
    shotgunretext1 = font.render(str(shotgunreload / 100), False, (255, 0, 255))
    shotgunretext2 = font.render("seconds, Click to upgrade for $250", False, (255, 0, 255))
    shotacctext = font.render("Shotgun accuracy:", False, (255, 0, 255))
    shotacctext1 = font.render(str(shotgunacc), False, (255, 0, 255))
    shotacctext2 = font.render("pixels, Click to upgrade for $80", False, (255, 0, 255))
    shotbulltext = font.render("Shotgun bullets:", False, (255, 0, 255))
    shotbulltext1 = font.render(str(shotgunbullets), False, (255, 0, 255))
    shotbulltext2 = font.render("bullets, Click to upgrade for $150", False, (255, 0, 255))
    mineratext = font.render("Mine explosion radius:", False, (255, 0, 255))
    mineratext1 = font.render(str(mineradius), False, (255, 0, 255))
    mineratext2 = font.render("pixels, Click to upgrade for $300", False, (255, 0, 255))
    minedamtext = font.render("Mine damage:", False, (255, 0, 255))
    minedamtext1 = font.render(str(minedamage), False, (255, 0, 255))
    minedamtext2 = font.render("damage, Click to upgrade for $250", False, (255, 0, 255))
    mineshraptext = font.render("Mine shrapnel:", False, (255, 0, 255))
    mineshraptext1 = font.render(str(mineshrapnel), False, (255, 0, 255))
    mineshraptext2 = font.render("bullets, Click to upgrade for $50", False, (255, 0, 255))
    lightdamtext = font.render("Lightning damage:", False, (255, 0, 255))
    lightdamtext1 = font.render(str(lightdamage), False, (255, 0, 255))
    lightdamtext2 = font.render("damage, Click to upgrade for $250", False, (255, 0, 255))
    lightretext = font.render("Lightning reload: Every", False, (255, 0, 255))
    lightretext1 = font.render(str(lightreload/100), False, (255, 0, 255))
    lightretext2 = font.render("seconds, Click to upgrade for $200", False, (255, 0, 255))

    if slide == "upgrades":
        for cat in range(0, 10):
            delay[cat] -= 1
        if event.type == pygame.MOUSEBUTTONDOWN and 20 < mousey < 50 and delay[0] <= 0 and coins >= 150:
            coins -= 150
            delay[0] = 15
            bulletreload = round(0.8*bulletreload, 1)
            if bulletreload < 1:
                bulletreload = 1
                coins += 150
        if event.type == pygame.MOUSEBUTTONDOWN and 50 < mousey < 80 and delay[1] <= 0 and coins >= 400:
            coins -= 400
            delay[1] = 15
            bullshotdamage += 1
        if event.type == pygame.MOUSEBUTTONDOWN and 80 < mousey < 110 and delay[2] <= 0 and coins >= 250:
            coins -= 250
            delay[2] = 15
            shotgunreload = round(0.75 * shotgunreload, 1)
            if shotgunreload < 1:
                shotgunreload = 1
                coins += 250
        if event.type == pygame.MOUSEBUTTONDOWN and 110 < mousey < 140 and delay[3] <= 0 and coins >= 80:
            coins -= 80
            delay[3] = 15
            shotgunacc = round(0.6 * shotgunacc, 1)
            if shotgunacc < 2:
                shotgunacc = 2
                coins += 80
        if event.type == pygame.MOUSEBUTTONDOWN and 140 < mousey < 170 and delay[4] <= 0 and coins >= 150:
            coins -= 150
            delay[4] = 15
            shotgunbullets += 2
            if shotgunbullets > 80:
                shotgunbullets = 80
                coins += 150
        if event.type == pygame.MOUSEBUTTONDOWN and 170 < mousey < 200 and delay[5] <= 0 and coins >= 300:
            coins -= 300
            delay[5] = 15
            mineradius += 20
            if mineradius > 600:
                mineradius = 600
                coins += 300
        if event.type == pygame.MOUSEBUTTONDOWN and 200 < mousey < 230 and delay[6] <= 0 and coins >= 250:
            coins -= 250
            delay[6] = 15
            minedamage += 1
        if event.type == pygame.MOUSEBUTTONDOWN and 230 < mousey < 260 and delay[7] <= 0 and coins >= 50:
            coins -= 50
            delay[7] = 15
            mineshrapnel += 1
        if event.type == pygame.MOUSEBUTTONDOWN and 260 < mousey < 290 and delay[8] <= 0 and coins >= 250:
            coins -= 250
            delay[8] = 15
            lightdamage += 0.5
        if event.type == pygame.MOUSEBUTTONDOWN and 290 < mousey < 320 and delay[9] <= 0 and coins >= 200:
            coins -= 200
            delay[9] = 15
            lightreload = round(0.85 * lightreload)
            if lightreload < 11:
                lightreload = 11
                coins += 200

        screen.blit(cointext1, (450, 500))
        screen.blit(cointext, (550, 500))
        screen.blit(highscoretext1, (410, 470))
        screen.blit(highscoretext, (590, 470))
        screen.blit(bulletretext, (20, 20))
        screen.blit(bulletretext1, (390, 20))
        screen.blit(bulletretext2, (480, 20))
        screen.blit(bulletdamtext, (20, 50))
        screen.blit(bulletdamtext1, (490, 50))
        screen.blit(bulletdamtext2, (530, 50))
        screen.blit(shotgunretext, (20, 80))
        screen.blit(shotgunretext1, (380, 80))
        screen.blit(shotgunretext2, (460, 80))
        screen.blit(shotacctext, (20, 110))
        screen.blit(shotacctext1, (320, 110))
        screen.blit(shotacctext2, (370, 110))
        screen.blit(shotbulltext, (20, 140))
        screen.blit(shotbulltext1, (290, 140))
        screen.blit(shotbulltext2, (350, 140))
        screen.blit(mineratext, (20, 170))
        screen.blit(mineratext1, (380, 170))
        screen.blit(mineratext2, (460, 170))
        screen.blit(minedamtext, (20, 200))
        screen.blit(minedamtext1, (250, 200))
        screen.blit(minedamtext2, (300, 200))
        screen.blit(mineshraptext, (20, 230))
        screen.blit(mineshraptext1, (260, 230))
        screen.blit(mineshraptext2, (340, 230))
        screen.blit(lightdamtext, (20, 260))
        screen.blit(lightdamtext1, (330, 260))
        screen.blit(lightdamtext2, (390, 260))
        screen.blit(lightretext, (20, 290))
        screen.blit(lightretext1, (400, 290))
        screen.blit(lightretext2, (480, 290))
        if score > highscore:
            highscore = score

    if slide == "gameplay":
        alientimer -= 1

        if shiphit > 0:
            score += 1

        if alientimer <= 0:
            choice = random.randint(1, 100)
            if stopwatch < 1500:
                if choice < 70:
                    make_eship(0, random.randint(1, 540), random.randint(-6, 6) / 4, random.randint(-6, 6) / 4,
                               random.randint(1, 30), "norm")
                elif choice < 90:
                    make_eship(0, random.randint(1, 540), random.randint(-6, 6) / 4, random.randint(-6, 6) / 4,
                               random.randint(1, 40), "split")
                else:
                    make_eship(0, random.randint(1, 540), random.randint(-6, 6) / 4, random.randint(-6, 6) / 4,
                               random.randint(1, 60), "splitt")
            elif stopwatch < 3000:
                if choice < 50:
                    make_eship(0, random.randint(1, 540), random.randint(-6, 6) / 4, random.randint(-6, 6) / 4,
                               random.randint(1, 30), "norm")
                elif choice < 70:
                    make_eship(0, random.randint(1, 540), random.randint(-6, 6) / 4, random.randint(-6, 6) / 4,
                               random.randint(1, 40), "split")
                elif choice < 85:
                    make_eship(0, random.randint(1, 540), random.randint(-6, 6) / 4, random.randint(-6, 6) / 4,
                               random.randint(1, 60), "splitt")
                elif choice < 95:
                    make_eship(0, random.randint(1, 540), random.randint(-6, 6) / 4, random.randint(-6, 6) / 4,
                               random.randint(1, 80), "splittt")
                else:
                    make_eship(0, random.randint(1, 540), random.randint(-6, 6) / 4, random.randint(-6, 6) / 4,
                               random.randint(1, 100), "splitttt")
            elif stopwatch < 4500:
                if choice < 30:
                    make_eship(0, random.randint(1, 540), random.randint(-6, 6) / 4, random.randint(-6, 6) / 4,
                               random.randint(1, 60), "split")
                elif choice < 60:
                    make_eship(0, random.randint(1, 540), random.randint(-6, 6) / 4, random.randint(-6, 6) / 4,
                               random.randint(1, 70), "splitt")
                elif choice < 70:
                    make_eship(0, random.randint(1, 540), random.randint(-6, 6) / 4, random.randint(-6, 6) / 4,
                               random.randint(1, 100), "splittt")
                elif choice < 80:
                    make_eship(0, random.randint(1, 540), random.randint(-6, 6) / 4, random.randint(-6, 6) / 4,
                               random.randint(1, 120), "splitttt")
                elif choice < 90:
                    make_eship(0, random.randint(1, 540), random.randint(-6, 6) / 4, random.randint(-6, 6) / 4,
                               random.randint(1, 150), "splittttt")
                else:
                    make_eship(0, random.randint(1, 540), random.randint(-6, 6) / 4, random.randint(-6, 6) / 4,
                               random.randint(1, 180), "splitttttt")
            elif stopwatch < 6000:
                if choice < 35:
                    make_eship(0, random.randint(1, 540), random.randint(-6, 6) / 4, random.randint(-6, 6) / 4,
                               random.randint(1, 75), "splitt")
                elif choice < 60:
                    make_eship(0, random.randint(1, 540), random.randint(-6, 6) / 4, random.randint(-6, 6) / 4,
                               random.randint(1, 105), "splittt")
                elif choice < 80:
                    make_eship(0, random.randint(1, 540), random.randint(-6, 6) / 4, random.randint(-6, 6) / 4,
                               random.randint(1, 130), "splitttt")
                elif choice < 88:
                    make_eship(0, random.randint(1, 540), random.randint(-6, 6) / 4, random.randint(-6, 6) / 4,
                               random.randint(1, 160), "splittttt")
                elif choice < 93:
                    make_eship(0, random.randint(1, 540), random.randint(-6, 6) / 4, random.randint(-6, 6) / 4,
                               random.randint(1, 200), "splitttttt")
                elif choice < 98:
                    make_eship(0, random.randint(1, 540), random.randint(-6, 6) / 4, random.randint(-6, 6) / 4,
                               random.randint(1, 240), "splittttttt")
                else:
                    make_eship(0, random.randint(1, 540), random.randint(-6, 6) / 4, random.randint(-6, 6) / 4,
                               random.randint(1, 310), "splitttttttt")
            elif stopwatch < 7500:
                if choice < 40:
                    make_eship(0, random.randint(1, 540), random.randint(-6, 6) / 4, random.randint(-6, 6) / 4,
                               random.randint(1, 120), "splittt")
                elif choice < 70:
                    make_eship(0, random.randint(1, 540), random.randint(-6, 6) / 4, random.randint(-6, 6) / 4,
                               random.randint(1, 150), "splitttt")
                elif choice < 82:
                    make_eship(0, random.randint(1, 540), random.randint(-6, 6) / 4, random.randint(-6, 6) / 4,
                               random.randint(1, 180), "splittttt")
                elif choice < 88:
                    make_eship(0, random.randint(1, 540), random.randint(-6, 6) / 4, random.randint(-6, 6) / 4,
                               random.randint(1, 225), "splitttttt")
                elif choice < 95:
                    make_eship(0, random.randint(1, 540), random.randint(-6, 6) / 4, random.randint(-6, 6) / 4,
                               random.randint(1, 270), "splittttttt")
                else:
                    make_eship(0, random.randint(1, 540), random.randint(-6, 6) / 4, random.randint(-6, 6) / 4,
                               random.randint(1, 350), "splitttttttt")
            elif stopwatch < 9000:
                if choice < 40:
                    make_eship(0, random.randint(1, 540), random.randint(-6, 6) / 4, random.randint(-6, 6) / 4,
                               random.randint(1, 150), "splitttt")
                elif choice < 65:
                    make_eship(0, random.randint(1, 540), random.randint(-6, 6) / 4, random.randint(-6, 6) / 4,
                               random.randint(1, 190), "splittttt")
                elif choice < 80:
                    make_eship(0, random.randint(1, 540), random.randint(-6, 6) / 4, random.randint(-6, 6) / 4,
                               random.randint(1, 250), "splitttttt")
                elif choice < 91:
                    make_eship(0, random.randint(1, 540), random.randint(-6, 6) / 4, random.randint(-6, 6) / 4,
                               random.randint(1, 300), "splittttttt")
                else:
                    make_eship(0, random.randint(1, 540), random.randint(-6, 6) / 4, random.randint(-6, 6) / 4,
                               random.randint(1, 380), "splitttttttt")
            else:
                if choice < 50:
                    make_eship(0, random.randint(1, 540), random.randint(-6, 6) / 4, random.randint(-6, 6) / 4,
                               random.randint(1, 270), "splitttttt")
                elif choice < 80:
                    make_eship(0, random.randint(1, 540), random.randint(-6, 6) / 4, random.randint(-6, 6) / 4,
                               random.randint(1, 330), "splittttttt")
                else:
                    make_eship(0, random.randint(1, 540), random.randint(-6, 6) / 4, random.randint(-6, 6) / 4,
                               random.randint(1, 430), "splitttttttt")
            alientimer = random.randint(1, 110)

        if stopwatch > 11000:
            shiphit -= 0.1

        for cat in range(0, len(lightning1x)):
            if lightningtimer <= 10:
                pygame.draw.line(screen,
                                 (5 + 25 * lightningtimer, 5 + 25 * lightningtimer, 5 + 25 * lightningtimer),
                                 (lightning1x[cat], lightning1y[cat]),
                                 (lightning2x[cat], lightning2y[cat]), 6)

        stopwatch += 1
        lightningtimer -= 1

        if (stopwatch / 100) % 1 == 0:
            if shiphit < 200:
                shiphit += 1.5

        shipx += shipxx
        shipy += shipyy

        minetimer += 1
        shoottimer += 1
        shotguntimer += 1

        if shoottimer >= bulletreload:
            if shoot == True:
                bulletx.append(shipx)
                bullety.append(shipy)
                bulletxx.append(shipxx * 5)
                bulletyy.append(shipyy * 5)
                bulletdel.append(1)
                shoottimer = 0
                if gunsounds == True:
                    pygame.mixer.Sound.play(gunsound)

        if shotguntimer >= shotgunreload:
            if shoot == True:
                for cat in range(0, shotgunbullets):
                    bulletx.append(shipx)
                    bullety.append(shipy)
                    bulletxx.append(random.randint(round(50 * shipxx - shotgunacc), round(50 * shipxx + shotgunacc)) / 10)
                    bulletyy.append(random.randint(round(50 * shipyy - shotgunacc), round(50 * shipyy + shotgunacc)) / 10)
                    bulletdel.append(1)
                if shotgunsounds == True:
                    pygame.mixer.Sound.play(shotgunsound)
                shotguntimer = 0

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
                    eshiphit[dog] -= bullshotdamage

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
            if minedel[cat] == 2:
                if miner[cat] > 20:
                    pygame.draw.circle(screen, (255, 0, 0), (round(minex[cat]), round(miney[cat])), round(miner[cat]), 20)
                else:
                    pygame.draw.circle(screen, (255, 0, 0), (round(minex[cat]), round(miney[cat])), round(miner[cat]))
                for dog in range(0, len(eshipx)):
                    if abs(eshipx[dog] - minex[cat]) <= miner[cat]:
                        if abs(eshipy[dog] - miney[cat]) <= miner[cat]:
                            eshiphit[dog] -= 3*minedamage
                if abs(shipx - minex[cat]) <= miner[cat]:
                    if abs(shipy - miney[cat]) <= miner[cat]:
                        shiphit -= 0.25
                miner[cat] += 25
                if miner[cat] > mineradius:
                    minedel[cat] = 0
                    if minesounds == True:
                        pygame.mixer.Sound.play(explosionsound)
                    for dog in range(0, mineshrapnel):
                        randomx = random.randint(-9, 9)
                        randomy = random.randint(-9, 9)
                        bulletx.append(minex[cat])
                        bullety.append(miney[cat])
                        bulletxx.append(randomx)
                        bulletyy.append(randomy)
                        bulletdel.append(1)

        for cat in range(0, len(minex)):
            if minedel[cat] == 0:
                del minex[cat]
                del miney[cat]
                del minedel[cat]
                del miner[cat]
                break

        if minetimer > 30:
            if dropmine == True:
                minex.append(shipx)
                miney.append(shipy)
                minedel.append(1)
                miner.append(1)
                minetimer = 0

        for cat in range(0, len(eshipdel)):
            if (stopwatch / lightreload) % 1 == 0:
                lightningtimer = 10
                if abs(eshipx[cat] - shipx) < 250 and abs(eshipy[cat] - shipy) < 250:
                    lightning1x.append(shipx)
                    lightning1y.append(shipy)
                    lightning2x.append(eshipx[cat])
                    lightning2y.append(eshipy[cat])
                    lightstruck[cat] = 1
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
                if cat != dog and lightstruck[cat] == 1 and lightstruck[dog] == 0:
                    if abs(eshipx[cat] - eshipx[dog]) < 250 and abs(eshipy[cat] - eshipy[dog]) < 250:
                        lightning1x.append(eshipx[dog])
                        lightning1y.append(eshipy[dog])
                        lightning2x.append(eshipx[cat])
                        lightning2y.append(eshipy[cat])
                        lightstruck[dog] = 1

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
                if eshiptype[cat] == "split" and stopwatch < 5000:
                    make_eship(eshipx[cat], eshipy[cat] - 10, eshipxx[cat], eshipyy[cat], round(1 + eshiphitt[cat] / 2),
                               "norm")
                    make_eship(eshipx[cat], eshipy[cat] + 10, eshipxx[cat], eshipyy[cat], round(1 + eshiphitt[cat] / 2),
                               "norm")
                if eshiptype[cat] == "splitt" and stopwatch < 7500:
                    make_eship(eshipx[cat], eshipy[cat] - 10, eshipxx[cat], eshipyy[cat], round(1 + eshiphitt[cat] / 2),
                               "split")
                    make_eship(eshipx[cat], eshipy[cat] + 10, eshipxx[cat], eshipyy[cat], round(1 + eshiphitt[cat] / 2),
                               "split")
                if eshiptype[cat] == "splittt" and stopwatch < 9000:
                    make_eship(eshipx[cat], eshipy[cat] - 10, eshipxx[cat], eshipyy[cat], round(1 + eshiphitt[cat] / 2),
                               "splitt")
                    make_eship(eshipx[cat], eshipy[cat] + 10, eshipxx[cat], eshipyy[cat], round(1 + eshiphitt[cat] / 2),
                               "splitt")
                if eshiptype[cat] == "splitttt":
                    make_eship(eshipx[cat], eshipy[cat] - 10, eshipxx[cat], eshipyy[cat], round(1 + eshiphitt[cat] / 2),
                               "splittt")
                    make_eship(eshipx[cat], eshipy[cat] + 10, eshipxx[cat], eshipyy[cat], round(1 + eshiphitt[cat] / 2),
                               "splittt")
                if eshiptype[cat] == "splittttt":
                    make_eship(eshipx[cat], eshipy[cat] - 10, eshipxx[cat], eshipyy[cat], round(1 + eshiphitt[cat] / 2),
                               "splitttt")
                    make_eship(eshipx[cat], eshipy[cat] + 10, eshipxx[cat], eshipyy[cat], round(1 + eshiphitt[cat] / 2),
                               "splitttt")
                if eshiptype[cat] == "splitttttt":
                    make_eship(eshipx[cat], eshipy[cat] - 10, eshipxx[cat], eshipyy[cat], round(1 + eshiphitt[cat] / 2),
                               "splittttt")
                    make_eship(eshipx[cat], eshipy[cat] + 10, eshipxx[cat], eshipyy[cat], round(1 + eshiphitt[cat] / 2),
                               "splittttt")
                if eshiptype[cat] == "splittttttt":
                    make_eship(eshipx[cat], eshipy[cat] - 10, eshipxx[cat], eshipyy[cat], round(1 + eshiphitt[cat] / 2),
                               "splitttttt")
                    make_eship(eshipx[cat], eshipy[cat] + 10, eshipxx[cat], eshipyy[cat], round(1 + eshiphitt[cat] / 2),
                               "splitttttt")
                if eshiptype[cat] == "splitttttttt":
                    make_eship(eshipx[cat], eshipy[cat] - 10, eshipxx[cat], eshipyy[cat], round(1 + eshiphitt[cat] / 2),
                               "splittttttt")
                    make_eship(eshipx[cat], eshipy[cat] + 10, eshipxx[cat], eshipyy[cat], round(1 + eshiphitt[cat] / 2),
                               "splittttttt")
            if (stopwatch / 150) % 1 == 0:
                ebulletx.append(eshipx[cat])
                ebullety.append(eshipy[cat])
                ebulletxx.append(eshipxx[cat] * 4)
                ebulletyy.append(eshipyy[cat] * 4)
                ebulletdel.append(1)
            pygame.draw.rect(screen, (255, 0, 0), (
            round(eshipx[cat]) - 25, round(eshipy[cat]) + 30, round(eshiphit[cat] * 50 / eshiphitt[cat]), 4))
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

        for cat in range(0, len(eshipdel)):
            if lightstruck[cat] == 1:
                eshiphit[cat] -= lightdamage
                lightstruck[cat] = 0

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

        for dog in range(0, len(eshipdel)):
            for cat in range(0, len(eshipdel)):
                if eshipdel[cat] == 0:
                    if shiphit > 0:
                        score += eshiphitt[cat]
                        coins += eshiphitt[cat]
                        if stopwatch > 3000:
                            coins -= eshiphitt[cat]/2
                        if stopwatch > 3000:
                            coins -= eshiphitt[cat]/4
                    del eshipx[cat]
                    del eshipy[cat]
                    del eshipxx[cat]
                    del eshipyy[cat]
                    del eshipdel[cat]
                    del eshiphit[cat]
                    del eshiphitt[cat]
                    del eshiptype[cat]
                    del eshipsum[cat]
                    del lightstruck[cat]
                    break

        for dog in range(0, len(ebulletdel)):
            for cat in range(0, len(ebulletdel)):
                if ebulletdel[cat] == 0:
                    del ebulletx[cat]
                    del ebullety[cat]
                    del ebulletxx[cat]
                    del ebulletyy[cat]
                    del ebulletdel[cat]
                    break

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
            pygame.draw.rect(screen, (255, 0, 0), (round(shipx) - 25, round(shipy) + 30, round(shiphit / 2), 4))

        if shiphit <= 0:
            dietimer -= 1
            stopwatch -= 1
            pygame.draw.rect(screen, (255, 0, 255), (round(shipx) - 25, round(shipy) + 30, 50, 4))
            shiphit -= 1
            if dietimer <= 0:
                print(score)

                if score > highscore:
                    highscore = score

                shipx = 540
                shipy = 450
                shipxx = 0
                shipyy = -3
                shiphit = 100

                bulletx = []
                bullety = []
                bulletxx = []
                bulletyy = []
                bulletdel = []
                bulletreload = 8
                bullshotdamage = 4
                shotgunacc = 60
                shotgunreload = 100
                shotgunbullets = 6

                ebulletx = []
                ebullety = []
                ebulletxx = []
                ebulletyy = []
                ebulletdel = []

                minex = []
                miney = []
                minedel = []
                miner = []
                mineradius = 150
                minedamage = 3
                mineshrapnel = 10

                lightning1x = []
                lightning1y = []
                lightning2x = []
                lightning2y = []
                lightningtimer = 0
                lightreload = 200
                lightdamage = 1

                eshipx = []
                eshipy = []
                eshipxx = []
                eshipyy = []
                eshipdel = []
                eshiphit = []
                eshiphitt = []
                eshiptype = []
                eshipsum = []
                lightstruck = []

                stopwatch = 0
                minetimer = 0
                shoottimer = 0
                shotguntimer = 0

                shoot = False
                dropmine = False

                aimturn = "?"
                aimturn1 = "?"

                score = 0

                alientimer = 0

                delay = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

                slide = "upgrades"

                coins = 1000

        screen.blit(scoretext, (500, 250))
        screen.blit(cointext, (500, 230))
        coins = round(coins)

    pygame.display.flip()
    clock.tick(100)