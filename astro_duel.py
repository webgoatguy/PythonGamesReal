import pygame
import sys
import random
import math

pygame.init()

dietimer = 300

clock = pygame.time.Clock()

screen = pygame.display.set_mode((1200,1000))

font = pygame.font.Font("freesansbold.ttf", 32)

ship1x = 50
ship1y = 50
ship1xx = 1.5
ship1yy = 1.5

ship2x = 1150
ship2y = 950
ship2xx = -1.5
ship2yy = -1.5

boost1 = 1
boost2 = 1

wintimer = 0

turn1 = "?"
turn2 = "?"

ammo1 = 3
ammo2 = 3

bullet1x = []
bullet1y = []
bullet1xx = []
bullet1yy = []

bullet2x = []
bullet2y = []
bullet2xx = []
bullet2yy = []

shoot1 = False
shoot2 = False

shootstop1 = False
shootstop2 = False

stopwatch = 0

win1 = 0
win2 = 0
win11 = 0
win22 = 0

wallx = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
wally = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
wallxx = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
wallyy = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

powerupx = []
powerupy = []
poweruptype = []

powerup1 = "none"
powerup2 = "none"

poweruptimer1 = 0
poweruptimer2 = 0

boosttimer1 = -1
boosttimer2 = -1

mine1x = []
mine1y = []
mine2x = []
mine2y = []

asteroidx = []
asteroidy = []
asteroid = []

replay = False

ship1xr = []
ship1yr = []
ship1xxr = []
ship1yyr = []

ship2xr = []
ship2yr = []
ship2xxr = []
ship2yyr = []

powerupxr = []
powerupyr = []
poweruptyper = []

bullet1xr = []
bullet1yr = []
bullet2xr = []
bullet2yr = []

mine1xr = []
mine1yr = []
mine2xr = []
mine2yr = []

asteroidxr = []
asteroidyr = []
asteroidr = []

powerup1r = []
powerup2r = []

laserx = []
lasery = []
laserxx = []
laseryy = []
lasertimer = []

bot = True

for cat in range(0, 20):
    wallx[cat] = random.randint(2, 8)*100
    wally[cat] = random.randint(0, 11)*100
    if random.randint(1, 2) == 1:
        wallxx[cat] = 21
        wallyy[cat] = random.randint(1, 5)*100+1
    else:
        wallxx[cat] = random.randint(1, 5)*100+1
        wallyy[cat] = 21
    while wallx[cat] + wallxx[cat] > 950 or wally[cat] + wallyy[cat] > 1150:
        wallx[cat] = random.randint(2, 8)*100
        wally[cat] = random.randint(0, 11)*100
        if random.randint(1, 2) == 1:
            wallxx[cat] = 21
            wallyy[cat] = random.randint(1, 5)*100+1
        else:
            wallxx[cat] = random.randint(1, 5)*100+1
            wallyy[cat] = 21

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                turn1 = "right"
            if event.key == pygame.K_LEFT:
                turn1 = "left"
            if event.key == pygame.K_UP:
                shoot1 = True
            if event.key == pygame.K_a:
                turn2 = "left"
            if event.key == pygame.K_d:
                turn2 = "right"
            if event.key == pygame.K_w:
                shoot2 = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                turn1 = "?"
            if event.key == pygame.K_LEFT:
                turn1 = "?"
            if event.key == pygame.K_UP:
                shootstop1 = True
            if event.key == pygame.K_a:
                turn2 = "?"
            if event.key == pygame.K_d:
                turn2 = "?"
            if event.key == pygame.K_w:
                shootstop2 = True

    poweruptimer1 = 1000
    poweruptimer2 = 1000

    screen.fill((0, 0, 0))

    poweruptimer1 -= 1
    poweruptimer2 -= 1

    if wintimer > 0:
        wintimer -= 1
    if wintimer < 0:
        wintimer += 1

    if wintimer > 1:
        ship2x = -100
        ship2y = -100
    if wintimer < -1:
        ship1x = -100
        ship1y = -100

    if wintimer == 1:
        win1 += 1
        ship1x = 50
        ship1y = 50
        ship1xx = 2
        ship1yy = 2
        stopwatch = 0
        ship2x = 1150
        ship2y = 950
        ship2xx = -2
        ship2yy = -2
        ammo1 = 3
        ammo2 = 3
        bullet1x = []
        bullet1y = []
        bullet1xx = []
        bullet1yy = []
        bullet2x = []
        bullet2y = []
        bullet2xx = []
        bullet2yy = []
        asteroidx = []
        asteroidy = []
        asteroid = []
        powerupx = []
        powerupy = []
        poweruptype = []
        powerup1 = "none"
        powerup2 = "none"
        poweruptimer1 = 0
        poweruptimer2 = 0
        wintimer = 0
        for cat in range(0, 20):
            wallx[cat] = random.randint(0, 11) * 100
            wally[cat] = random.randint(0, 9) * 100
            if random.randint(1, 2) == 1:
                wallxx[cat] = 21
                wallyy[cat] = random.randint(1, 5) * 100 + 1
            else:
                wallxx[cat] = random.randint(1, 5) * 100 + 1
                wallyy[cat] = 21
            while wallx[cat] + wallxx[cat] > 950 or wally[cat] + wallyy[cat] > 1150:
                wallx[cat] = random.randint(0, 11) * 100
                wally[cat] = random.randint(0, 9) * 100
                if random.randint(1, 2) == 1:
                    wallxx[cat] = 21
                    wallyy[cat] = random.randint(1, 5) * 100 + 1
                else:
                    wallxx[cat] = random.randint(1, 5) * 100 + 1
                    wallyy[cat] = 21
    if wintimer == -1:
        win2 += 1
        ship1x = 50
        ship1y = 50
        ship1xx = 2
        ship1yy = 2
        stopwatch = 0
        ship2x = 1150
        ship2y = 950
        ship2xx = -2
        ship2yy = -2
        ammo1 = 3
        ammo2 = 3
        bullet1x = []
        bullet1y = []
        bullet1xx = []
        bullet1yy = []
        bullet2x = []
        bullet2y = []
        bullet2xx = []
        bullet2yy = []
        asteroidx = []
        asteroidy = []
        asteroid = []
        powerupx = []
        powerupy = []
        poweruptype = []
        powerup1 = "none"
        powerup2 = "none"
        poweruptimer1 = 0
        poweruptimer2 = 0
        wintimer = 0
        for cat in range(0, 20):
            wallx[cat] = random.randint(0, 11) * 100
            wally[cat] = random.randint(0, 9) * 100
            if random.randint(1, 2) == 1:
                wallxx[cat] = 21
                wallyy[cat] = random.randint(1, 5) * 100 + 1
            else:
                wallxx[cat] = random.randint(1, 5) * 100 + 1
                wallyy[cat] = 21
            while wallx[cat] + wallxx[cat] > 950 or wally[cat] + wallyy[cat] > 1150:
                wallx[cat] = random.randint(0, 11) * 100
                wally[cat] = random.randint(0, 9) * 100
                if random.randint(1, 2) == 1:
                    wallxx[cat] = 21
                    wallyy[cat] = random.randint(1, 5) * 100 + 1
                else:
                    wallxx[cat] = random.randint(1, 5) * 100 + 1
                    wallyy[cat] = 21

    for cat in range(0, len(laserx)):
        if lasertimer[cat] > 1:
            pygame.draw.line(screen, (6*lasertimer[cat], 8*lasertimer[cat], 10*lasertimer[cat]), (laserx[cat], lasery[cat]), (laserx[cat] + 1000 * laserxx[cat], lasery[cat] + 1000 * laseryy[cat]), 10)
            lasertimer[cat] -= 1
            for dog in range(0, 250):
                if ship2x - 25 <= laserx[cat] + 4 * dog * laserxx[cat] <= ship2x + 25 and ship2y - 25 <= lasery[cat] + 4 * dog * laseryy[cat] <= ship2y + 25 and lasertimer[cat] > 20:
                    wintimer = 200
        if lasertimer[cat] < -1:
            pygame.draw.line(screen, (-6*lasertimer[cat], -8*lasertimer[cat], -10*lasertimer[cat]), (laserx[cat], lasery[cat]), (laserx[cat] + 1000 * laserxx[cat], lasery[cat] + 1000 * laseryy[cat]), 10)
            lasertimer[cat] += 1
            for dog in range(0, 250):
                if ship1x - 25 <= laserx[cat] + 4 * dog * laserxx[cat] <= ship1x + 25 and ship1y - 25 <= lasery[cat] + 4 * dog * laseryy[cat] <= ship1y + 25 and lasertimer[cat] < -20:
                    wintimer = -200
        if lasertimer[cat] > 1:
            pygame.draw.line(screen, (6*lasertimer[cat], 8*lasertimer[cat], 10*lasertimer[cat]), (round(laserx[cat]), round(lasery[cat])), (round(laserx[cat] + 1000 * laserxx[cat]), round(lasery[cat] + 1000 * laseryy[cat])), 10)
        if lasertimer[cat] < -1:
            pygame.draw.line(screen, (-6*lasertimer[cat], -8*lasertimer[cat], -10*lasertimer[cat]), (round(laserx[cat]), round(lasery[cat])), (round(laserx[cat] + 1000 * laserxx[cat]), round(lasery[cat] + 1000 * laseryy[cat])), 10)
        if -2 <= lasertimer[cat] <= 2:
            del laserx[cat]
            del lasery[cat]
            del laserxx[cat]
            del laseryy[cat]
            del lasertimer[cat]
            break

    if replay == False:
        ship1xr.append(ship1x)
        ship1yr.append(ship1y)
        ship1xxr.append(ship1xx)
        ship1yyr.append(ship1yy)
        ship2xr.append(ship2x)
        ship2yr.append(ship2y)
        ship2xxr.append(ship2xx)
        ship2yyr.append(ship2yy)
        powerupxr.append(powerupx)
        powerupyr.append(powerupy)
        poweruptyper.append(poweruptype)
        bullet1xr.append(bullet1x)
        bullet1yr.append(bullet1y)
        bullet2xr.append(bullet2x)
        bullet2yr.append(bullet2y)
        mine1xr.append(mine1x)
        mine1yr.append(mine1y)
        mine2xr.append(mine2x)
        mine2yr.append(mine2y)
        asteroidxr.append(asteroidx)
        asteroidyr.append(asteroidy)
        asteroidr.append(asteroid)
        powerup1r.append(powerup1)
        powerup2r.append(powerup2)

    if replay == True:
        ship1x = ship1xr[stopwatch]
        ship1xx = ship1xxr[stopwatch]
        ship1y = ship1yr[stopwatch]
        ship1yy = ship1yyr[stopwatch]
        ship2x = ship2xr[stopwatch]
        ship2xx = ship2xxr[stopwatch]
        ship2y = ship2yr[stopwatch]
        ship2yy = ship2yyr[stopwatch]
        powerupx = powerupxr[stopwatch]
        powerupy = powerupyr[stopwatch]
        poweruptype = poweruptyper[stopwatch]
        bullet1x = bullet1xr[stopwatch]
        bullet1y = bullet1yr[stopwatch]
        bullet2x = bullet2xr[stopwatch]
        bullet2y = bullet2yr[stopwatch]
        mine1x = mine1xr[stopwatch]
        mine1y = mine1yr[stopwatch]
        mine2x = mine2xr[stopwatch]
        mine2y = mine2yr[stopwatch]
        asteroidx = asteroidxr[stopwatch]
        asteroidy = asteroidyr[stopwatch]
        asteroid = asteroidr[stopwatch]
        powerup1 = powerup1r[stopwatch]
        powerup2 = powerup2r[stopwatch]

    if (stopwatch / 750) % 1 == 0:
        asteroidx.append(random.randint(5, 11)*100 + 50)
        asteroidy.append(random.randint(0, 9)*100 + 50)
        asteroid.append(random.randint(1, 3))

    if powerup2 == "shield":
        poweruptimer2 = 1000
        
    if stopwatch == 1:
            asteroidx.append(random.randint(5, 11) * 100 + 50)
            asteroidy.append(random.randint(0, 9) * 100 + 50)
            asteroid.append(random.randint(1, 3))
            powerupx.append(random.randint(0, 11) * 100 + 50)
            powerupy.append(random.randint(0, 9) * 100 + 50)
            choice = random.randint(1, 10)
            if choice == 1:
                poweruptype.append("spreadshot")
            if choice == 2:
                poweruptype.append("twin guns")
            if choice == 3:
                poweruptype.append("laser beam")
            if choice == 4:
                poweruptype.append("jousters")
            if choice == 5:
                poweruptype.append("shield")
            if choice == 6:
                poweruptype.append("big bullets")
            if choice == 7:
                poweruptype.append("ghost")
            if choice == 8:
                poweruptype.append("laser bullets")
            if choice == 9:
                poweruptype.append("mine")
            if choice == 10:
                poweruptype.append("aimbot")
            
    if (stopwatch / 2000) % 1 == 0:
        powerupx.append(random.randint(0, 11)*100 + 50)
        powerupy.append(random.randint(0, 9)*100 + 50)
        choice = random.randint(1, 10)
        if choice == 1:
            poweruptype.append("spreadshot")
        if choice == 2:
            poweruptype.append("twin guns")
        if choice == 3:
            poweruptype.append("laser beam")
        if choice == 4:
            poweruptype.append("jousters")
        if choice == 5:
            poweruptype.append("shield")
        if choice == 6:
            poweruptype.append("big bullets")
        if choice == 7:
            poweruptype.append("ghost")
        if choice == 8:
            poweruptype.append("laser bullets")
        if choice == 9:
            poweruptype.append("mine")
        if choice == 10:
            poweruptype.append("aimbot")

    score1text = font.render(str(win1), False, (0, 255, 0))
    score2text = font.render(str(win2), False, (255, 0, 0))

    stopwatch += 1

    for cat in range(0, len(asteroidx)):
        asteroidx[cat] = round(asteroidx[cat])
        asteroidy[cat] = round(asteroidy[cat])
        pygame.draw.circle(screen, (100, 100, 100), (round(asteroidx[cat]), round(asteroidy[cat])), asteroid[cat]*10)
        for dog in range(0, len(bullet1x)):
            if bullet1x[dog] - asteroid[cat]*10 - 10 < asteroidx[cat] < bullet1x[dog] + asteroid[cat]*10 + 10 and bullet1y[dog] - asteroid[cat] * 10 - 10< asteroidy[cat] < bullet1y[dog] + 10 + asteroid[cat] * 10:
                del bullet1x[dog]
                del bullet1y[dog]
                del bullet1xx[dog]
                del bullet1yy[dog]
                asteroid[cat] -= 1
                break
        for dog in range(0, len(bullet2x)):
            if bullet2x[dog] - asteroid[cat]*10 - 10 < asteroidx[cat] < bullet2x[dog] + asteroid[cat]*10 +10 and bullet2y[dog] - asteroid[cat] * 10 - 10< asteroidy[cat] < bullet2y[dog] + asteroid[cat] * 10+ 10:
                del bullet2x[dog]
                del bullet2y[dog]
                del bullet2xx[dog]
                del bullet2yy[dog]
                asteroid[cat] -= 1
                break
        if asteroid[cat] <= 0:
            if random.randint(1, 2) == 2:
                powerupx.append(asteroidx[cat])
                powerupy.append(asteroidy[cat])
                choice = random.randint(1, 10)
                if choice == 1:
                    poweruptype.append("spreadshot")
                if choice == 2:
                    poweruptype.append("twin guns")
                if choice == 3:
                    poweruptype.append("laser beam")
                if choice == 4:
                    poweruptype.append("jousters")
                if choice == 5:
                    poweruptype.append("shield")
                if choice == 6:
                    poweruptype.append("big bullets")
                if choice == 7:
                    poweruptype.append("ghost")
                if choice == 8:
                    poweruptype.append("laser bullets")
                if choice == 9:
                    poweruptype.append("mine")
                if choice == 10:
                    poweruptype.append("aimbot")
                if random.randint(1, 2) == 2:
                    powerupx.append(asteroidx[cat] + 100)
                    powerupy.append(asteroidy[cat])
                    choice = random.randint(1, 10)
                    if choice == 1:
                        poweruptype.append("spreadshot")
                    if choice == 2:
                        poweruptype.append("twin guns")
                    if choice == 3:
                        poweruptype.append("laser beam")
                    if choice == 4:
                        poweruptype.append("jousters")
                    if choice == 5:
                        poweruptype.append("shield")
                    if choice == 6:
                        poweruptype.append("big bullets")
                    if choice == 7:
                        poweruptype.append("ghost")
                    if choice == 8:
                        poweruptype.append("laser bullets")
                    if choice == 9:
                        poweruptype.append("mine")
                    if choice == 10:
                        poweruptype.append("aimbot")
                    if random.randint(1, 2) == 2:
                        powerupx.append(asteroidx[cat] - 100)
                        powerupy.append(asteroidy[cat])
                        choice = random.randint(1, 10)
                        if choice == 1:
                            poweruptype.append("spreadshot")
                        if choice == 2:
                            poweruptype.append("twin guns")
                        if choice == 3:
                            poweruptype.append("laser beam")
                        if choice == 4:
                            poweruptype.append("jousters")
                        if choice == 5:
                            poweruptype.append("shield")
                        if choice == 6:
                            poweruptype.append("big bullets")
                        if choice == 7:
                            poweruptype.append("ghost")
                        if choice == 8:
                            poweruptype.append("laser bullets")
                        if choice == 9:
                            poweruptype.append("mine")
                        if choice == 10:
                            poweruptype.append("aimbot")
            del asteroid[cat]
            del asteroidx[cat]
            del asteroidy[cat]
            break

    for cat in range(0, len(powerupx)):
        powerupx[cat] = round(powerupx[cat])
        powerupy[cat] = round(powerupy[cat])
        pygame.draw.rect(screen, (255, 255, 255), (powerupx[cat] - 20, powerupy[cat] - 20, 40, 40))
        if poweruptype[cat] == "spreadshot":
            pygame.draw.circle(screen, (0, 0, 0), (powerupx[cat]+14, powerupy[cat]), 3)
            pygame.draw.circle(screen, (0, 0, 0), (powerupx[cat]-14, powerupy[cat]), 3)
            pygame.draw.circle(screen, (0, 0, 0), (powerupx[cat], powerupy[cat]+15), 3)
            pygame.draw.circle(screen, (0, 0, 0), (powerupx[cat], powerupy[cat]-15), 3)
            pygame.draw.circle(screen, (0, 0, 0), (powerupx[cat]+11, powerupy[cat]-7), 3)
            pygame.draw.circle(screen, (0, 0, 0), (powerupx[cat]+11, powerupy[cat]+7), 3)
            pygame.draw.circle(screen, (0, 0, 0), (powerupx[cat]+6, powerupy[cat]-12), 3)
            pygame.draw.circle(screen, (0, 0, 0), (powerupx[cat]+6, powerupy[cat]+12), 3)
            pygame.draw.circle(screen, (0, 0, 0), (powerupx[cat]-6, powerupy[cat]-12), 3)
            pygame.draw.circle(screen, (0, 0, 0), (powerupx[cat]-6, powerupy[cat]+12), 3)
            pygame.draw.circle(screen, (0, 0, 0), (powerupx[cat]-11, powerupy[cat]-7), 3)
            pygame.draw.circle(screen, (0, 0, 0), (powerupx[cat]-11, powerupy[cat]+7), 3)
        if poweruptype[cat] == "twin guns":
            pygame.draw.circle(screen, (0, 0, 0), (powerupx[cat] - 7, powerupy[cat]), 3)
            pygame.draw.circle(screen, (0, 0, 0), (powerupx[cat] + 7, powerupy[cat]), 3)
        if poweruptype[cat] == "laser beam":
            pygame.draw.rect(screen, (150, 200, 255), (powerupx[cat] - 2, powerupy[cat] - 18, 3, 36))
        if poweruptype[cat] == "jousters":
            pygame.draw.rect(screen, (60, 255, 60), (powerupx[cat] - 14, powerupy[cat] - 14, 4, 28))
            pygame.draw.rect(screen, (60, 255, 60), (powerupx[cat] + 10, powerupy[cat] - 14, 4, 28))
        if poweruptype[cat] == "shield":
            pygame.draw.polygon(screen, (150, 200, 255), ((powerupx[cat] - 15, powerupy[cat]), (powerupx[cat] + 10, powerupy[cat] - 10), (powerupx[cat] + 10, powerupy[cat] + 10)))
        if poweruptype[cat] == "big bullets":
            pygame.draw.circle(screen, (0, 0, 0), (powerupx[cat], powerupy[cat]), 15)
        if poweruptype[cat] == "ghost":
            pygame.draw.polygon(screen, (200, 200, 200), ((powerupx[cat] - 10, powerupy[cat]), (powerupx[cat] + 10, powerupy[cat] - 10), (powerupx[cat] + 10, powerupy[cat] + 10)))
        if poweruptype[cat] == "laser bullets":
            pygame.draw.circle(screen, (255, 0, 0), (powerupx[cat], powerupy[cat]), 4)
        if poweruptype[cat] == "mine":
            pygame.draw.circle(screen, (255, 0, 0), (powerupx[cat], powerupy[cat]), 15)
        if poweruptype[cat] == "aimbot":
            pygame.draw.polygon(screen, (0, 200, 0), ((powerupx[cat] - 8, powerupy[cat]), (powerupx[cat] + 5, powerupy[cat] - 5), (powerupx[cat] + 5, powerupy[cat] + 5)))
        if ship1x - 30 < powerupx[cat] < ship1x + 30 and ship1y - 30 < powerupy[cat] < ship1y + 30:
            powerup1 = poweruptype[cat]
            poweruptimer1 = 1000
            del powerupx[cat]
            del powerupy[cat]
            del poweruptype[cat]
            break
        if ship2x - 30 < powerupx[cat] < ship2x + 30 and ship2y - 30 < powerupy[cat] < ship2y + 30:
            powerup2 = poweruptype[cat]
            poweruptimer2 = 1000
            del powerupx[cat]
            del powerupy[cat]
            del poweruptype[cat]
            break

    screen.blit(score1text, (550, 30))
    screen.blit(score2text, (550, 60))

    if (stopwatch / 100) % 1 == 0 and ammo1 < 3:
        ammo1 += 1

    if (stopwatch / 100) % 1 == 0 and ammo2 < 3:
        ammo2 += 1

    ship1x += ship1xx*boost1
    ship1y += ship1yy*boost1

    ship2x += ship2xx*boost2
    ship2y += ship2yy*boost2

    for cat in range(0, 20):
        pygame.draw.rect(screen, (0, 0, 255), (wallx[cat], wally[cat], wallxx[cat], wallyy[cat]))
        if wallyy[cat] == 21:
            if wallx[cat] < ship1x < wallx[cat] + wallxx[cat] and wally[cat] + 10 <= ship1y <= wally[cat] + 20 and powerup1 != "ghost":
                ship1y = wally[cat] + 21
            if wallx[cat] < ship1x < wallx[cat] + wallxx[cat] and wally[cat] <= ship1y <= wally[cat] + 10 and powerup1 != "ghost":
                ship1y = wally[cat]
            if wallx[cat] < ship2x < wallx[cat] + wallxx[cat] and wally[cat] + 10 <= ship2y <= wally[cat] + 20 and powerup2 != "ghost":
                ship2y = wally[cat] + 21
            if wallx[cat] < ship2x < wallx[cat] + wallxx[cat] and wally[cat] <= ship2y <= wally[cat] + 10 and powerup2 != "ghost":
                ship2y = wally[cat]
        if wallxx[cat] == 21:
            if wally[cat] < ship1y < wally[cat] + wallyy[cat] and wallx[cat] + 10 <= ship1x <= wallx[cat] + 20 and powerup1 != "ghost":
                ship1x = wallx[cat] + 21
            if wally[cat] < ship1y < wally[cat] + wallyy[cat] and wallx[cat] <= ship1x <= wallx[cat] + 10 and powerup1 != "ghost":
                ship1x = wallx[cat]
            if wally[cat] < ship2y < wally[cat] + wallyy[cat] and wallx[cat] + 10 <= ship2x <= wallx[cat] + 20 and powerup2 != "ghost":
                ship2x = wallx[cat] + 21
            if wally[cat] < ship2y < wally[cat] + wallyy[cat] and wallx[cat] <= ship2x <= wallx[cat] + 10 and powerup2 != "ghost":
                ship2x = wallx[cat]

    if abs(ship1xx) + abs(ship1yy) > 3:
        if ship1xx < 0:
            ship1xx += 0.05
        if ship1yy < 0:
            ship1yy += 0.05
        if ship1xx > 0:
            ship1xx -= 0.05
        if ship1yy > 0:
            ship1yy -= 0.05

    if abs(ship2xx) + abs(ship2yy) > 3:
        if ship2xx < 0:
            ship2xx += 0.05
        if ship2yy < 0:
            ship2yy += 0.05
        if ship2xx > 0:
            ship2xx -= 0.05
        if ship2yy > 0:
            ship2yy -= 0.05

    boosttimer1 -= 1
    boosttimer2 -= 1

    if boost1 > 1:
        boost1 -= 0.02
    if boost2 > 1:
        boost2 -= 0.02

    if shoot1 == True and ammo1 != 0:
        if powerup1 != "twin guns" and powerup1 != "mine":
            bullet1x.append(ship1x)
            bullet1y.append(ship1y)
            bullet1xx.append(ship1xx*4)
            bullet1yy.append(ship1yy * 4)
        if len(mine1x) == 1:
            for monkey in range(0, 40):
                bullet1x.append(mine1x[0])
                bullet1y.append(mine1y[0])
                bullet1xx.append(random.randint(-50, 50)/5)
                bullet1yy.append(random.randint(-50, 50)/5)
                while not 70 < bullet1xx[len(bullet1xx) - 1]**2 + bullet1yy[len(bullet1yy) - 1]**2 < 120:
                    del bullet1xx[len(bullet1xx) - 1]
                    del bullet1yy[len(bullet1yy) - 1]
                    bullet1xx.append(random.randint(-50, 50) / 5)
                    bullet1yy.append(random.randint(-50, 50) / 5)
            del mine1x[0]
            del mine1y[0]
        if powerup1 == "spreadshot":
            for cat in range(0, 16):
                bullet1x.append(ship1x)
                bullet1y.append(ship1y)
            bullet1xx.append(10)
            bullet1yy.append(0)
            bullet1xx.append(-10)
            bullet1yy.append(0)
            bullet1xx.append(0)
            bullet1yy.append(10)
            bullet1xx.append(0)
            bullet1yy.append(-10)
            bullet1xx.append(7)
            bullet1yy.append(7)
            bullet1xx.append(7)
            bullet1yy.append(-7)
            bullet1xx.append(-7)
            bullet1yy.append(-7)
            bullet1xx.append(-7)
            bullet1yy.append(7)
            bullet1xx.append(9)
            bullet1yy.append(4)
            bullet1xx.append(9)
            bullet1yy.append(-4)
            bullet1xx.append(-9)
            bullet1yy.append(-4)
            bullet1xx.append(-9)
            bullet1yy.append(4)
            bullet1xx.append(4)
            bullet1yy.append(9)
            bullet1xx.append(4)
            bullet1yy.append(-9)
            bullet1xx.append(-4)
            bullet1yy.append(-9)
            bullet1xx.append(-4)
            bullet1yy.append(9)
            poweruptimer1 = 0
        if powerup1 == "mine":
            mine1x.append(ship1x)
            mine1y.append(ship1y)
            poweruptimer1 = 0
            powerup1 = "none"
        if powerup1 == "twin guns":
            bullet1x.append(ship1x - ship1yy*5)
            bullet1y.append(ship1y - ship1xx*5)
            bullet1xx.append(ship1xx*4)
            bullet1yy.append(ship1yy * 4)
            bullet1x.append(ship1x + ship1yy*5)
            bullet1y.append(ship1y + ship1xx*5)
            bullet1xx.append(ship1xx * 4)
            bullet1yy.append(ship1yy * 4)
        if powerup1 == "laser beam":
            laserx.append(ship1x)
            lasery.append(ship1y)
            laserxx.append(ship1xx)
            laseryy.append(ship1yy)
            lasertimer.append(25)
            poweruptimer1 = 0
        ship1x -= ship1xx * 5
        ship1y -= ship1yy * 5
        ammo1 -= 1
        shootstop1 = False
        if boosttimer1 >= 0:
            boost1 = 2.5
            boosttimer1 = 0
        if abs(ship1xx) + abs(ship1yy) <= 3:
            boosttimer1 = 30

    if powerup1 == "jousters":
        ship1x += ship1xx * 0.5 * boost1
        ship1y += ship1yy * 0.5 * boost1
    if powerup2 == "jousters":
        ship2x += ship2xx * 0.5 * boost1
        ship2y += ship2yy * 0.5 * boost1

    if powerup1 == "mine":
        poweruptimer1 = 1000
    if powerup2 == "mine":
        poweruptimer2 = 1000

    if powerup1 == "jousters" and ship1x - 24 <= ship2x <= ship1x + 24 and ship1y - 24 <= ship2y <= ship1y + 24:
        wintimer = 200
    if powerup2 == "jousters" and ship1x - 24 <= ship2x <= ship1x + 24 and ship1y - 24 <= ship2y <= ship1y + 24:
        wintimer = -200

    for cat in range(0, len(mine1x)):
        pygame.draw.circle(screen, (0, 255, 0), (round(mine1x[cat]), round(mine1y[cat])), 20)

    for cat in range(0, len(mine2x)):
        pygame.draw.circle(screen, (255, 0, 0), (round(mine2x[cat]), round(mine2y[cat])), 20)
        for dog in range(0, len(bullet2x)):
            if bullet2x[dog] - 25 <= mine2x[cat] <= bullet2x[dog] + 25 and bullet2y[dog] - 25 <= mine2y[cat] <= bullet2y[dog] + 25:
                for monkey in range(0, 40):
                    bullet2x.append(mine2x[cat])
                    bullet2y.append(mine2y[cat])
                    bullet2xx.append(random.randint(-50, 50)/5)
                    bullet2yy.append(random.randint(-50, 50)/5)
                    while not 70 < bullet2xx[len(bullet2xx) - 2]**2 + bullet2yy[len(bullet2yy) - 2]**2 < 220:
                        del bullet2xx[len(bullet2xx) - 2]
                        del bullet2yy[len(bullet2yy) - 2]
                        bullet2xx.append(random.randint(-50, 50) / 5)
                        bullet2yy.append(random.randint(-50, 50) / 5)
                del mine2x[cat]
                del mine2y[cat]
            break

    if shoot2 == True and ammo2 != 0:
        if powerup2 != "twin guns" and powerup2 != "mine":
            bullet2x.append(ship2x)
            bullet2y.append(ship2y)
            bullet2xx.append(ship2xx*4)
            bullet2yy.append(ship2yy * 4)
        if len(mine2x) == 1:
            for monkey in range(0, 40):
                bullet2x.append(mine2x[0])
                bullet2y.append(mine2y[0])
                bullet2xx.append(random.randint(-50, 50)/5)
                bullet2yy.append(random.randint(-50, 50)/5)
                while not 70 < bullet2xx[len(bullet2xx) - 2]**2 + bullet2yy[len(bullet2yy) - 2]**2 < 220:
                    del bullet2xx[len(bullet2xx) - 2]
                    del bullet2yy[len(bullet2yy) - 2]
                    bullet2xx.append(random.randint(-50, 50) / 5)
                    bullet2yy.append(random.randint(-50, 50) / 5)
            del mine2x[0]
            del mine2y[0]
        if powerup2 == "spreadshot":
            for cat in range(0, 16):
                bullet2x.append(ship2x)
                bullet2y.append(ship2y)
            bullet2xx.append(10)
            bullet2yy.append(0)
            bullet2xx.append(-10)
            bullet2yy.append(0)
            bullet2xx.append(0)
            bullet2yy.append(10)
            bullet2xx.append(0)
            bullet2yy.append(-10)
            bullet2xx.append(7)
            bullet2yy.append(7)
            bullet2xx.append(7)
            bullet2yy.append(-7)
            bullet2xx.append(-7)
            bullet2yy.append(-7)
            bullet2xx.append(-7)
            bullet2yy.append(7)
            bullet2xx.append(9)
            bullet2yy.append(4)
            bullet2xx.append(9)
            bullet2yy.append(-4)
            bullet2xx.append(-9)
            bullet2yy.append(-4)
            bullet2xx.append(-9)
            bullet2yy.append(4)
            bullet2xx.append(4)
            bullet2yy.append(9)
            bullet2xx.append(4)
            bullet2yy.append(-9)
            bullet2xx.append(-4)
            bullet2yy.append(-9)
            bullet2xx.append(-4)
            bullet2yy.append(9)
            poweruptimer2 = 0
        if powerup2 == "twin guns":
            bullet2x.append(ship2x - ship2yy*5)
            bullet2y.append(ship2y - ship2xx*5)
            bullet2xx.append(ship2xx*4)
            bullet2yy.append(ship2yy * 4)
            bullet2x.append(ship2x + ship2yy*5)
            bullet2y.append(ship2y + ship2xx*5)
            bullet2xx.append(ship2xx * 4)
            bullet2yy.append(ship2yy * 4)
        if powerup2 == "mine":
            mine2x.append(ship2x)
            mine2y.append(ship2y)
            poweruptimer2 = 0
            powerup2 = "none"
        if powerup2 == "laser beam":
            laserx.append(ship2x)
            lasery.append(ship2y)
            laserxx.append(ship2xx)
            laseryy.append(ship2yy)
            lasertimer.append(-25)
            poweruptimer2 = 0
        ship2x -= ship2xx * 3
        ship2y -= ship2yy * 3
        ammo2 -= 1
        shootstop2 = False
        if boosttimer2 >= 0:
            boost2 = 2.5
            boosttimer2 = 0
        if abs(ship2xx) + abs(ship2yy) <= 3:
            boosttimer2 = 30

    for dog in range(0, 20):
        for monkey in range(0, 10):
            for cat in range(0, len(bullet1x)):
                if wallx[dog] <= bullet1x[cat] <= wallx[dog] + wallxx[dog] and wally[dog] <= bullet1y[cat] <= wally[dog] + wallyy[dog]:
                    if powerup1 != "laser bullets":
                        del bullet1x[cat]
                        del bullet1y[cat]
                        del bullet1xx[cat]
                        del bullet1yy[cat]
                        break

    for cat in range(0, len(bullet1x)):
        pygame.draw.circle(screen, (0, 255, 0), (round(bullet1x[cat]), round(bullet1y[cat])), 6)
        if powerup1 == "aimbot":
            if bullet1xx[cat] != 0 and (ship2x - bullet1x[cat]) != 0:
                if bullet1xx[cat] > 0 and (ship2x - bullet1x[cat]) > 0 or (ship2x - bullet1x[cat]) < 0 and bullet1xx[
                    cat] < 0:
                    if bullet1yy[cat] / bullet1xx[cat] < (ship2y - bullet1y[cat]) / (ship2x - bullet1x[cat]):
                        aimturn = "right"
                    if bullet1yy[cat] / bullet1xx[cat] > (ship2y - bullet1y[cat]) / (ship2x - bullet1x[cat]):
                        aimturn = "left"
                if bullet1xx[cat] > 0 and (ship2x - bullet1x[cat]) < 0 or (ship2x - bullet1x[cat]) > 0 and bullet1xx[
                    cat] < 0:
                    if bullet1yy[cat] / bullet1xx[cat] < (ship2y - bullet1y[cat]) / (ship2x - bullet1x[cat]):
                        aimturn = "left"
                    if bullet1yy[cat] / bullet1xx[cat] > (ship2y - bullet1y[cat]) / (ship2x - bullet1x[cat]):
                        aimturn = "right"
                if aimturn == "left":
                    if bullet1xx[cat] < 0 and bullet1yy[cat] < 0:
                        bullet1xx[cat] -= 0.5
                        bullet1yy[cat] += 0.5
                    if bullet1xx[cat] < 0 and bullet1yy[cat] > 0:
                        bullet1xx[cat] += 0.5
                        bullet1yy[cat] += 0.5
                    if bullet1xx[cat] > 0 and bullet1yy[cat] < 0:
                        bullet1xx[cat] -= 0.5
                        bullet1yy[cat] -= 0.5
                    if bullet1xx[cat] > 0 and bullet1yy[cat] > 0:
                        bullet1xx[cat] += 0.5
                        bullet1yy[cat] -= 0.5
                if aimturn == "right":
                    if bullet1xx[cat] < 0 and bullet1yy[cat] < 0:
                        bullet1xx[cat] += 0.5
                        bullet1yy[cat] -= 0.5
                    if bullet1xx[cat] < 0 and bullet1yy[cat] > 0:
                        bullet1xx[cat] -= 0.5
                        bullet1yy[cat] -= 0.5
                    if bullet1xx[cat] > 0 and bullet1yy[cat] < 0:
                        bullet1xx[cat] += 0.5
                        bullet1yy[cat] += 0.5
                    if bullet1xx[cat] > 0 and bullet1yy[cat] > 0:
                        bullet1xx[cat] -= 0.5
                        bullet1yy[cat] += 0.5
        if powerup1 == "big bullets":
            pygame.draw.circle(screen, (0, 255, 0), (round(bullet1x[cat]), round(bullet1y[cat])), 15)
        if replay == False:
            bullet1x[cat] += bullet1xx[cat]
            bullet1y[cat] += bullet1yy[cat]
        if bullet1x[cat] > 1200 or bullet1x[cat] < 0 or bullet1y[cat] > 1200 or bullet1y[cat] < 0:
            del bullet1x[cat]
            del bullet1xx[cat]
            del bullet1y[cat]
            del bullet1yy[cat]
            break
        if bullet1x[cat] - 16 < ship2x < bullet1x[cat] + 16 and bullet1y[cat] - 16 < ship2y < bullet1y[cat] + 16 and powerup2 != "shield":
            wintimer = 200
        if bullet1x[cat] - 42 < ship2x < bullet1x[cat] + 42 and bullet1y[cat] - 42 < ship2y < bullet1y[cat] + 42 and powerup1 == "big bullets":
            wintimer = 200
        if bullet1x[cat] - 16 < ship2x < bullet1x[cat] + 16 and bullet1y[cat] - 16 < ship2y < bullet1y[cat] + 16 and powerup2 == "shield":
            poweruptimer2 = 0
            powerup2 = "none"
            del bullet1x[cat]
            del bullet1y[cat]
            del bullet1xx[cat]
            del bullet1yy[cat]
            break

    for dog in range(0, 20):
        for monkey in range(0, 10):
            for cat in range(0, len(bullet2x)):
                if wallx[dog] <= bullet2x[cat] <= wallx[dog] + wallxx[dog] and wally[dog] <= bullet2y[cat] <= wally[dog] + wallyy[dog]:
                    if powerup2 != "laser bullets":
                        del bullet2x[cat]
                        del bullet2y[cat]
                        del bullet2xx[cat]
                        del bullet2yy[cat]
                        break

    for cat in range(0, len(bullet2x)):
        if powerup2 == "aimbot":
            if bullet2xx[cat] != 0 and (ship1x - bullet2x[cat]) != 0:
                if bullet2xx[cat] > 0 and (ship1x - bullet2x[cat]) > 0 or (ship1x - bullet2x[cat]) < 0 and bullet2xx[
                    cat] < 0:
                    if bullet2yy[cat] / bullet2xx[cat] < (ship1y - bullet2y[cat]) / (ship1x - bullet2x[cat]):
                        aimturn = "right"
                    if bullet2yy[cat] / bullet2xx[cat] > (ship1y - bullet2y[cat]) / (ship1x - bullet2x[cat]):
                        aimturn = "left"
                if bullet2xx[cat] > 0 and (ship1x - bullet2x[cat]) < 0 or (ship1x - bullet2x[cat]) > 0 and bullet2xx[
                    cat] < 0:
                    if bullet2yy[cat] / bullet2xx[cat] < (ship1y - bullet2y[cat]) / (ship1x - bullet2x[cat]):
                        aimturn = "left"
                    if bullet2yy[cat] / bullet2xx[cat] > (ship1y - bullet2y[cat]) / (ship1x - bullet2x[cat]):
                        aimturn = "right"
                if aimturn == "left":
                    if bullet2xx[cat] < 0 and bullet2yy[cat] < 0:
                        bullet2xx[cat] -= 0.5
                        bullet2yy[cat] += 0.5
                    if bullet2xx[cat] < 0 and bullet2yy[cat] > 0:
                        bullet2xx[cat] += 0.5
                        bullet2yy[cat] += 0.5
                    if bullet2xx[cat] > 0 and bullet2yy[cat] < 0:
                        bullet2xx[cat] -= 0.5
                        bullet2yy[cat] -= 0.5
                    if bullet2xx[cat] > 0 and bullet2yy[cat] > 0:
                        bullet2xx[cat] += 0.5
                        bullet2yy[cat] -= 0.5
                if aimturn == "right":
                    if bullet2xx[cat] < 0 and bullet2yy[cat] < 0:
                        bullet2xx[cat] += 0.5
                        bullet2yy[cat] -= 0.5
                    if bullet2xx[cat] < 0 and bullet2yy[cat] > 0:
                        bullet2xx[cat] -= 0.5
                        bullet2yy[cat] -= 0.5
                    if bullet2xx[cat] > 0 and bullet2yy[cat] < 0:
                        bullet2xx[cat] += 0.5
                        bullet2yy[cat] += 0.5
                    if bullet2xx[cat] > 0 and bullet2yy[cat] > 0:
                        bullet2xx[cat] -= 0.5
                        bullet2yy[cat] += 0.5
        pygame.draw.circle(screen, (255, 0, 0), (round(bullet2x[cat]), round(bullet2y[cat])), 6)
        if powerup2 == "big bullets":
            pygame.draw.circle(screen, (255, 0, 0), (round(bullet2x[cat]), round(bullet2y[cat])), 15)
        if replay == False:
            bullet2x[cat] += bullet2xx[cat]
            bullet2y[cat] += bullet2yy[cat]
        if bullet2x[cat] > 1200 or bullet2x[cat] < 0 or bullet2y[cat] > 1200 or bullet2y[cat] < 0:
            del bullet2x[cat]
            del bullet2xx[cat]
            del bullet2y[cat]
            del bullet2yy[cat]
            break
        if bullet2x[cat] - 16 < ship1x < bullet2x[cat] + 16 and bullet2y[cat] - 16 < ship1y < bullet2y[cat] + 16 and powerup1 != "shield":
            wintimer = -200
        if bullet2x[cat] - 42 < ship1x < bullet2x[cat] + 42 and bullet2y[cat] - 42 < ship1y < bullet2y[cat] + 42 and powerup2 == "big bullets":
            wintimer = -200
        if bullet2x[cat] - 16 < ship1x < bullet2x[cat] + 16 and bullet2y[cat] - 16 < ship1y < bullet2y[cat] + 16 and powerup1 == "shield":
            poweruptimer1 = 0
            powerup1 = "none"
            del bullet2x[cat]
            del bullet2y[cat]
            del bullet2xx[cat]
            del bullet2yy[cat]
            break

    if wintimer == 0:
        if ship1x > 1200:
            ship1x = 0
        if ship1y > 1000:
            ship1y = 0
        if ship2x > 1200:
            ship2x = 0
        if ship2y > 1000:
            ship2y = 0
        if ship1x < 0:
            ship1x = 1200
        if ship1y < 0:
            ship1y = 1000
        if ship2x < 0:
            ship2x = 1200
        if ship2y < 0:
            ship2y = 1000

    if turn1 == "left":
        if ship1xx < 0 and ship1yy < 0:
            ship1xx -= 0.05
            ship1yy += 0.05
        if ship1xx < 0 and ship1yy >= 0:
            ship1xx += 0.05
            ship1yy += 0.05
        if ship1xx >= 0 and ship1yy < 0:
            ship1xx -= 0.05
            ship1yy -= 0.05
        if ship1xx >= 0 and ship1yy >= 0:
            ship1xx += 0.05
            ship1yy -= 0.05
    if turn1 == "right":
        if ship1xx < 0 and ship1yy < 0:
            ship1xx += 0.05
            ship1yy -= 0.05
        if ship1xx < 0 and ship1yy >= 0:
            ship1xx -= 0.05
            ship1yy -= 0.05
        if ship1xx >= 0 and ship1yy < 0:
            ship1xx += 0.05
            ship1yy += 0.05
        if ship1xx >= 0 and ship1yy >= 0:
            ship1xx -= 0.05
            ship1yy += 0.05

    if turn2 == "left":
        if ship2xx < 0 and ship2yy < 0:
            ship2xx -= 0.05
            ship2yy += 0.05
        if ship2xx < 0 and ship2yy >= 0:
            ship2xx += 0.05
            ship2yy += 0.05
        if ship2xx >= 0 and ship2yy < 0:
            ship2xx -= 0.05
            ship2yy -= 0.05
        if ship2xx >= 0 and ship2yy >= 0:
            ship2xx += 0.05
            ship2yy -= 0.05
    if turn2 == "right":
        if ship2xx < 0 and ship2yy < 0:
            ship2xx += 0.05
            ship2yy -= 0.05
        if ship2xx < 0 and ship2yy >= 0:
            ship2xx -= 0.05
            ship2yy -= 0.05
        if ship2xx >= 0 and ship2yy < 0:
            ship2xx += 0.05
            ship2yy += 0.05
        if ship2xx >= 0 and ship2yy >= 0:
            ship2xx -= 0.05
            ship2yy += 0.05

    if poweruptimer1 < 0:
        powerup1 = "none"
    if poweruptimer2 < 0:
        powerup2 = "none"

    shoot1 = False
    shoot2 = False

    counter1 = ship1xx ** 2 + ship1yy ** 2
    counter2 = ship2xx ** 2 + ship2yy ** 2

    if powerup1 == "shield":
        poweruptimer1 = 1000
        pygame.draw.polygon(screen, (100, 100, 255), (
            ((ship1x + ship1xx * 4.5 * 9 / counter1), (ship1y + ship1yy * 3.66 * 9 / counter1)),
            ((ship1x - ship1xx * 6 - ship1yy * 7.5 * 9 / counter1), (ship1y - ship1yy * 6 + ship1xx * 7.5 * 9 / counter1)),
            ((ship1x - ship1xx * 6 + ship1yy * 7.5 * 9 / counter1), (ship1y - ship1yy * 6 - ship1xx * 7.5 * 9 / counter1))))

    if powerup2 == "shield":
        poweruptimer = 1000
        pygame.draw.polygon(screen, (100, 100, 255), (
            ((ship2x + ship2xx * 4.5 * 9 / counter2), (ship2y + ship2yy * 4.5 * 9 / counter2)),
            ((ship2x - ship2xx * 6 - ship2yy * 7.5 * 9 / counter2), (ship2y - ship2yy * 6 + ship2xx * 7.5 * 9 / counter2)),
            ((ship2x - ship2xx * 6 + ship2yy * 7.5 * 9 / counter2), (ship2y - ship2yy * 6 - ship2xx * 7.5 * 9 / counter2))))

    if powerup1 == "jousters":
        poweruptimer1 = 1000
        pygame.draw.line(screen, (60, 255, 60), ((ship1x - ship1xx * 4 - ship1yy * 5 * 9 / counter1), (ship1y - ship1yy * 4 + ship1xx * 5 * 9 / counter1)), ((ship1x + ship1xx * 4 - ship1yy * 5 * 9 / counter1), (ship1y + ship1yy * 4 + ship1xx * 5 * 9 / counter1)), 4)
        pygame.draw.line(screen, (60, 255, 60), ((ship1x - ship1xx * 4 + ship1yy * 5 * 9 / counter1), (ship1y - ship1yy * 4 - ship1xx * 5 * 9 / counter1)), ((ship1x + ship1xx * 4 + ship1yy * 5 * 9 / counter1), (ship1y + ship1yy * 4 - ship1xx * 5 * 9 / counter1)), 4)

    if powerup2 == "jousters":
        poweruptimer2 = 1000
        pygame.draw.line(screen, (60, 255, 60), ((ship2x - ship2xx * 4 - ship2yy * 5 * 9 / counter2), (ship2y - ship2yy * 4 + ship2xx * 5 * 9 / counter2)), ((ship2x + ship2xx * 4 - ship2yy * 5 * 9 / counter2), (ship2y + ship2yy * 4 + ship2xx * 5 * 9 / counter2)), 4)
        pygame.draw.line(screen, (60, 255, 60), ((ship2x - ship2xx * 4 + ship2yy * 5 * 9 / counter2), (ship2y - ship2yy * 4 - ship2xx * 5 * 9 / counter2)), ((ship2x + ship2xx * 4 + ship2yy * 5 * 9 / counter2), (ship2y + ship2yy * 4 - ship2xx * 5 * 9 / counter2)), 4)

    pygame.draw.polygon(screen, (0, 255, 0), (
        ((ship1x + ship1xx * 3 * 9 / counter1), (ship1y + ship1yy * 3 * 9 / counter1)),
        ((ship1x - ship1xx * 4 - ship1yy * 5 * 9 / counter1), (ship1y - ship1yy * 4 + ship1xx * 5 * 9 / counter1)),
        ((ship1x - ship1xx * 4 + ship1yy * 5 * 9 / counter1), (ship1y - ship1yy * 4 - ship1xx * 5 * 9 / counter1))))

    pygame.draw.polygon(screen, (255, 0, 0), (
        ((ship2x + ship2xx * 3 * 9 / counter2), (ship2y + ship2yy * 3 * 9 / counter2)),
        ((ship2x - ship2xx * 4 - ship2yy * 5 * 9 / counter2), (ship2y - ship2yy * 4 + ship2xx * 5 * 9 / counter2)),
        ((ship2x - ship2xx * 4 + ship2yy * 5 * 9 / counter2), (ship2y - ship2yy * 4 - ship2xx * 5 * 9 / counter2))))

    if ammo1 >= 1:
        pygame.draw.circle(screen, (255, 255, 255), (round(ship1x - ship1xx * 6 - ship1yy * 3 * 9 / counter1), round(ship1y - ship1yy * 6 + ship1xx * 3 * 9 / counter1)), 4)
    if ammo1 >= 2:
        pygame.draw.circle(screen, (255, 255, 255), (round(ship1x - ship1xx * 6), round(ship1y - ship1yy * 6)), 4)
    if ammo1 >= 3:
        pygame.draw.circle(screen, (255, 255, 255), (round(ship1x - ship1xx * 6 + ship1yy * 3 * 9 / counter1), round(ship1y - ship1yy * 6 - ship1xx * 3 * 9 / counter1)), 4)

    if ammo2 >= 1:
        pygame.draw.circle(screen, (255, 255, 255), (round(ship2x - ship2xx * 6 - ship2yy * 3 * 9 / counter2), round(ship2y - ship2yy * 6 + ship2xx * 3 * 9 / counter2)), 4)
    if ammo2 >= 2:
        pygame.draw.circle(screen, (255, 255, 255), (round(ship2x - ship2xx * 6), round(ship2y - ship2yy * 6)), 4)
    if ammo2 >= 3:
        pygame.draw.circle(screen, (255, 255, 255), (round(ship2x - ship2xx * 6 + ship2yy * 3 * 9 / counter2), round(ship2y - ship2yy * 6 - ship2xx * 3 * 9 / counter2)), 4)

    if stopwatch + 1 >= len(ship1xr) and replay == True:
        replay = False
        for cat in range(0, 20):
            wallx[cat] = random.randint(0, 11) * 100
            wally[cat] = random.randint(0, 9) * 100
            if random.randint(1, 2) == 1:
                wallxx[cat] = 21
                wallyy[cat] = random.randint(1, 5) * 100 + 1
            else:
                wallxx[cat] = random.randint(1, 5) * 100 + 1
                wallyy[cat] = 21
            while wallx[cat] + wallxx[cat] > 950 or wally[cat] + wallyy[cat] > 1150:
                wallx[cat] = random.randint(0, 11) * 100
                wally[cat] = random.randint(0, 9) * 100
                if random.randint(1, 2) == 1:
                    wallxx[cat] = 21
                    wallyy[cat] = random.randint(1, 5) * 100 + 1
                else:
                    wallxx[cat] = random.randint(1, 5) * 100 + 1
                    wallyy[cat] = 21
        ship1x = 50
        ship1y = 50
        ship1xx = 2
        ship1yy = 2
        ship2x = 1150
        ship2y = 950
        ship2xx = -2
        ship2yy = -2
        ammo1 = 3
        ammo2 = 3
        bullet1x = []
        bullet1y = []
        bullet1xx = []
        bullet1yy = []
        bullet2x = []
        bullet2y = []
        bullet2xx = []
        bullet2yy = []
        asteroidx = []
        asteroidy = []
        asteroid = []
        powerupx = []
        powerupy = []
        poweruptype = []
        stopwatch = 0
        powerup1 = "none"
        powerup2 = "none"
        poweruptimer1 = 0
        poweruptimer2 = 0
        ship1xr = []
        ship1yr = []
        ship1xxr = []
        ship1yyr = []
        powerup1r = []
        powerup2r = []
        ship2xr = []
        ship2yr = []
        ship2xxr = []
        ship2yyr = []

        powerupxr = []
        powerupyr = []
        poweruptyper = []

        bullet1xr = []
        bullet1yr = []

        bullet2xr = []
        bullet2yr = []

        mine1xr = []
        mine1yr = []
        mine2xr = []
        mine2yr = []

        asteroidxr = []
        asteroidyr = []
        asteroidr = []

    replay = False

    if win11 != win1:
        stopwatch = 0
        win11 += 1
    if win22 != win2:
        stopwatch = 0
        win22 += 1

    pygame.display.flip()
    clock.tick(100)