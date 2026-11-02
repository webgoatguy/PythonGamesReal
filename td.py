import pygame
import sys
import random
import pickle
import math
import heapq

pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((1000,500))

font = pygame.font.Font("freesansbold.ttf", 20)

filename = "td_mapx"
filename1 = "td_mapy"

enemy = []
enemyspeed = []
enemydel = []
enemyhit = []
enemyhitt = []
enemysplit = []
enemytype = []
enemystate = []
stuntimer = []
backtimer = []

bulletx = []
bullety = []
bulletxx = []
bulletyy = []
bulletdamage = []
bulletdel = []
laserx = []
lasery = []
laserxx = []
laseryy = []
laserdamage = []
laserdel = []
magicx = []
magicy = []
magicxx = []
magicyy = []
magicdamage = []
magicp = []
#(pierce)
magicdel = []
bombx = []
bomby = []
bombxx = []
bombyy = []
bombradius = []
bombr = []
bombdamage = []
bombdel = []

basicx = []
basicy = []
basicra = []
basicdam = []
basicre = []
basicshot = []
basicup = []
wizardx = []
wizardy = []
wizardra = []
wizarddam = []
wizardre = []
wizardshot = []
wizardup = []
cannonx = []
cannony = []
cannonra = []
cannondam = []
cannonre = []
cannonshot = []
cannonup = []
lasertx = []
laserty = []
lasertra = []
lasertdam = []
lasertre = []
lasertshot = []
lasertup = []
machinex = []
machiney = []
machinera = []
machinedam = []
machinespr = []
machinere = []
machineshot = []
machineup = []
minigunx = []
miniguny = []
minigunre = []
minigundam = []
minigunspr = []
minigunup = []

dragging = "none"

grave = []
gravesplit = []
gravehealth = []
gravetimer = []
gravedel = []

stopwatch = 10000

lives = 100
money = 500

infile = open(filename,'rb')
mapx = pickle.load(infile)
infile.close()
infile1 = open(filename1,'rb')
mapy = pickle.load(infile1)
infile1.close()

mousedown = False

inrange = False

def spawn_enemy(spot, hitpoints, split_type, type, stun, back):
    enemy.append(spot)
    enemydel.append(0)
    enemyhit.append(hitpoints/4)
    enemyhitt.append(hitpoints/4)
    enemystate.append("normal")
    enemysplit.append(split_type)
    enemytype.append(type)
    stuntimer.append(stun)
    backtimer.append(back)
    if type == "normal":
        enemyspeed.append(0.75)
    if type == "fast":
        enemyspeed.append(1.8)
    if type == "immune":
        enemyspeed.append(0.7)
    if type == "immune2":
        enemyspeed.append(0.7)
    if type == "strong":
        enemyspeed.append(0.6)
    if type == "zombie":
        enemyspeed.append(0.55)
    if type == "necro":
        enemyspeed.append(0.3)
    if type == "healthy":
        enemyspeed.append(1.1)

aimturn = "?"
breakv = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            outfile = open(filename, 'wb')
            pickle.dump(mapx, outfile)
            outfile.close()
            outfile1 = open(filename1, 'wb')
            pickle.dump(mapy, outfile1)
            outfile1.close()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                dragging = "none"

    lives_text = font.render("lives:" + str(round(lives)), False, (255, 0, 0))

    stopwatch += 1

    mousex, mousey = pygame.mouse.get_pos()

    if event.type == pygame.MOUSEBUTTONDOWN:
        mousedown = True
    if event.type == pygame.MOUSEBUTTONUP:
        mousedown = False

    screen.fill((0, 255, 0))

    if stopwatch == 500 or stopwatch == 700 or stopwatch == 800 or stopwatch == 850:
        spawn_enemy(0, 100, "normal", "normal", 0, 0)
    if stopwatch == 1000 or stopwatch == 1100:
        spawn_enemy(0, 90, "normal", "fast", 0, 0)
    if stopwatch == 1300:
        spawn_enemy(0, 150, "split", "normal", 0, 0)
    if stopwatch == 1500:
        spawn_enemy(0, 100, "split", "fast", 0, 0)
    for cat in range(0, 10):
        if stopwatch == 1700 + cat*50:
            spawn_enemy(0, 100, "normal", "normal", 0, 0)
    if stopwatch == 2400:
        spawn_enemy(0, 200, "splitt", "normal", 0, 0)
    for cat in range(0, 3):
        if stopwatch == 2600 + cat*30:
            spawn_enemy(0, 400, "normal", "strong", 0, 0)
    for cat in range(0, 30):
        if stopwatch == 2800 + cat:
            spawn_enemy(0, 10, "normal", "fast", 0, 0)
    for cat in range(0, 10):
        if stopwatch == 3000 + cat*50:
            spawn_enemy(0, 120, "split", "normal", 0, 0)
    if stopwatch == 3600:
        spawn_enemy(0, 200, "splittt", "normal", 0, 0)
    if stopwatch == 3850:
        spawn_enemy(0, 500, "splitt", "strong", 0, 0)
    if stopwatch == 4000:
        spawn_enemy(0, 200, "normal", "immune2", 0, 0)
    if stopwatch == 4300:
        spawn_enemy(0, 150, "splitttt", "normal", 0, 0)
    for cat in range(0, 20):
        if stopwatch == 4800 + cat*60:
            spawn_enemy(0, 100, "splitt", "normal", 0, 0)
    for cat in range(0, 15):
        if stopwatch == 4800 + cat*80:
            spawn_enemy(0, 80, "split", "fast", 0, 0)
    for cat in range(0, 10):
        if stopwatch == 4800 + cat*100:
            spawn_enemy(0, 300, "normal", "strong", 0, 0)
    if stopwatch == 6000:
        spawn_enemy(0, 100, "normal", "immune", 0, 0)
    for cat in range(0, 10):
        if stopwatch == 6400 + cat*40:
            spawn_enemy(0, 50, "normal", "immune2", 0, 0)
    for cat in range(0, 10):
        if stopwatch == 6420 + cat*40:
            spawn_enemy(0, 50, "normal", "immune", 0, 0)
    for cat in range(0, 5):
        if stopwatch == 7000 + cat*200:
            spawn_enemy(0, 300, "splitt", "healthy", 0, 0)
    for cat in range(0, 100):
        if stopwatch == 7400 + cat:
            spawn_enemy(0, 50, "split", "fast", 0, 0)
    for cat in range(0, 10):
        if stopwatch == 8000 + cat*500:
            spawn_enemy(0, 1000 + cat*250, "normal", "strong", 0, 0)
    for cat in range(0, 40):
        if stopwatch == 10000 + cat*100:
            spawn_enemy(0, 150 + cat*20, "split", "fast", 0, 0)
    for cat in range(0, 10):
        if stopwatch == 8500 + cat*50:
            spawn_enemy(0, 300, "normal", "zombie", 0, 0)
    if stopwatch == 9200:
        spawn_enemy(0, 200, "splitt", "zombie", 0, 0)
    if stopwatch == 9800:
        spawn_enemy(0, 200, "splitt", "zombie", 0, 0)
    if stopwatch == 10500:
        spawn_enemy(0, 200, "splittt", "zombie", 0, 0)
    for cat in range(0, 6):
        if stopwatch == 11200 + cat*30:
            spawn_enemy(0, 100, "splitttt", "fast", 0, 0)
    if stopwatch == 12500:
        spawn_enemy(0, 500, "normal", "necro", 0, 0)
    if stopwatch == 13200:
        spawn_enemy(0, 1250, "split", "necro", 0, 0)
    if stopwatch == 14000 or stopwatch == 17000 or stopwatch == 17100 or stopwatch == 17200:
        spawn_enemy(0, -2000 + stopwatch/4, "splitt", "necro", 0, 0)
    for cat in range(0, 5):
        if stopwatch == 16000 + cat*30:
            spawn_enemy(0, 400, "splitt", "normal", 0, 0)
            spawn_enemy(0, 300, "splitt", "fast", 0, 0)
            spawn_enemy(0, 1500, "splitt", "strong", 0, 0)
            spawn_enemy(0, 450, "splitt", "immune", 0, 0)
            spawn_enemy(0, 450, "splitt", "immune2", 0, 0)
            spawn_enemy(0, 600, "splitt", "healthy", 0, 0)

    for cat in range(0, len(mapx)):
        pygame.draw.circle(screen, (200, 100, 0), (mapx[cat], mapy[cat]), 20)

    pygame.draw.rect(screen, (255, 255, 255), (900, 0, 100, 500))
    pygame.draw.rect(screen, (255, 255, 255), (0, 480, 1000, 20))

    if dragging == "basic":
        pygame.draw.rect(screen, (200, 200, 200), (mousex - 25, mousey - 25, 50, 50))
        pygame.draw.circle(screen, (120, 120, 120), (mousex, mousey), 16)
        pygame.draw.rect(screen, (120, 120, 120), (mousex - 8, mousey - 32, 16, 32))
    if dragging == "wizard":
        pygame.draw.rect(screen, (0, 0, 0), (mousex - 25, mousey - 25, 50, 50))
        pygame.draw.circle(screen, (0, 0, 255), (mousex, mousey), 16)
        pygame.draw.rect(screen, (0, 0, 255), (mousex - 8, mousey - 32, 16, 32))
    if dragging == "machine gun":
        pygame.draw.rect(screen, (200, 200, 200), (mousex - 25, mousey - 25, 50, 50))
        pygame.draw.circle(screen, (120, 120, 120), (mousex, mousey), 16)
        pygame.draw.polygon(screen, (120, 120, 120), (
            (mousex + 15, mousey - 32), (mousex - 15, mousey - 32),
            (mousex - 8, mousey), (mousex + 8, mousey)))
    if dragging == "minigun":
        pygame.draw.rect(screen, (50, 50, 50), (mousex - 25, mousey - 25, 50, 50))
        pygame.draw.circle(screen, (120, 120, 120), (mousex, mousey), 16)
        pygame.draw.polygon(screen, (120, 120, 120), (
            (mousex + 15, mousey - 32), (mousex - 15, mousey - 32),
            (mousex - 8, mousey), (mousex + 8, mousey)))
    if dragging == "laser":
        pygame.draw.rect(screen, (200, 200, 200), (mousex - 25, mousey - 25, 50, 50))
        pygame.draw.circle(screen, (255, 0, 0), (mousex, mousey), 16)
        pygame.draw.rect(screen, (255, 0, 0), (mousex - 8, mousey - 32, 16, 32))
    if dragging == "cannon":
        pygame.draw.rect(screen, (200, 200, 200), (mousex - 25, mousey - 25, 50, 50))
        pygame.draw.circle(screen, (0, 0, 0), (mousex, mousey), 20)
        pygame.draw.rect(screen, (0, 0, 0), (mousex - 12, mousey - 32, 24, 32))

    pygame.draw.rect(screen, (200, 200, 200), (900, 0, 50, 50))
    pygame.draw.circle(screen, (120, 120, 120), (925, 25), 16)
    pygame.draw.rect(screen, (120, 120, 120), (917, -7, 16, 32))

    pygame.draw.rect(screen, (0, 0, 0), (950, 0, 50, 50))
    pygame.draw.circle(screen, (0, 0, 255), (975, 25), 16)
    pygame.draw.rect(screen, (0, 0, 255), (967, -7, 16, 32))

    pygame.draw.rect(screen, (200, 200, 200), (950, 50, 50, 50))
    pygame.draw.circle(screen, (120, 120, 120), (975, 75), 16)
    pygame.draw.polygon(screen, (120, 120, 120), ((990, 43), (960, 43), (967, 75), (983, 75)))

    pygame.draw.rect(screen, (50, 50, 50), (900, 50, 50, 50))
    pygame.draw.circle(screen, (120, 120, 120), (925, 75), 16)
    pygame.draw.polygon(screen, (120, 120, 120), ((940, 43), (910, 43), (917, 75), (933, 75)))

    pygame.draw.rect(screen, (200, 200, 200), (900, 100, 50, 50))
    pygame.draw.circle(screen, (255, 0, 0), (925, 125), 16)
    pygame.draw.rect(screen, (255, 0, 0), (917, 93, 16, 32))

    pygame.draw.rect(screen, (200, 200, 200), (950, 100, 50, 50))
    pygame.draw.circle(screen, (0, 0, 0), (975, 125), 20)
    pygame.draw.rect(screen, (0, 0, 0), (963, 93, 24, 32))

    if mousedown == True and mousex > 900 and dragging == "none":
        if mousex < 950 and mousey < 50:
            dragging = "basic"
        if mousex > 950 and mousey < 50:
            dragging = "wizard"
        if mousex < 950 and 50 < mousey < 100:
            dragging = "minigun"
        if mousex > 950 and 50 < mousey < 100:
            dragging = "machine gun"
        if mousex < 950 and 100 < mousey < 150:
            dragging = "laser"
        if mousex > 950 and 100 < mousey < 150:
            dragging = "cannon"

    if mousex < 900 and dragging != "none":
        for cat in range(0, len(mapx)):
            if mapx[cat] - 40 <= mousex <= mapx[cat] + 40 and mapy[cat] - 40 <= mousey <= mapy[cat] + 40:
                pygame.draw.rect(screen, (255, 0, 0), (mousex - 25, mousey - 25, 50, 50))
                breakv = True
        for cat in range(0, len(basicx)):
            if basicx[cat] - 40 <= mousex <= basicx[cat] + 40 and basicy[cat] - 40 <= mousey <= basicy[cat] + 40:
                pygame.draw.rect(screen, (255, 0, 0), (mousex - 25, mousey - 25, 50, 50))
                breakv = True
        for cat in range(0, len(wizardx)):
            if wizardx[cat] - 40 <= mousex <= wizardx[cat] + 40 and wizardy[cat] - 40 <= mousey <= wizardy[cat] + 40:
                pygame.draw.rect(screen, (255, 0, 0), (mousex - 25, mousey - 25, 50, 50))
                breakv = True
        for cat in range(0, len(machinex)):
            if machinex[cat] - 40 <= mousex <= machinex[cat] + 40 and machiney[cat] - 40 <= mousey <= machiney[cat] + 40:
                pygame.draw.rect(screen, (255, 0, 0), (mousex - 25, mousey - 25, 50, 50))
                breakv = True
        for cat in range(0, len(minigunx)):
            if minigunx[cat] - 40 <= mousex <= minigunx[cat] + 40 and miniguny[cat] - 40 <= mousey <= miniguny[cat] + 40:
                pygame.draw.rect(screen, (255, 0, 0), (mousex - 25, mousey - 25, 50, 50))
                breakv = True
        for cat in range(0, len(lasertx)):
            if lasertx[cat] - 40 <= mousex <= lasertx[cat] + 40 and laserty[cat] - 40 <= mousey <= laserty[cat] + 40:
                pygame.draw.rect(screen, (255, 0, 0), (mousex - 25, mousey - 25, 50, 50))
                breakv = True
        for cat in range(0, len(cannonx)):
            if cannonx[cat] - 40 <= mousex <= cannonx[cat] + 40 and cannony[cat] - 40 <= mousey <= cannony[cat] + 40:
                pygame.draw.rect(screen, (255, 0, 0), (mousex - 25, mousey - 25, 50, 50))
                breakv = True
        if dragging == "basic" and mousedown == False and breakv == False:
            basicx.append(mousex)
            basicy.append(mousey)
            basicdam.append(10)
            basicre.append(15)
            basicra.append(150)
            basicshot.append(1)
            basicup.append(1)
        if dragging == "laser" and mousedown == False and breakv == False:
            lasertx.append(mousex)
            laserty.append(mousey)
            lasertdam.append(6)
            lasertre.append(15)
            lasertra.append(100)
            lasertshot.append(1)
            lasertup.append(1)
        if dragging == "wizard" and mousedown == False and breakv == False:
            wizardx.append(mousex)
            wizardy.append(mousey)
            wizarddam.append(4)
            wizardre.append(20)
            wizardra.append(100)
            wizardshot.append(1)
            wizardup.append(1)
        if dragging == "machine gun" and mousedown == False and breakv == False:
            machinex.append(mousex)
            machiney.append(mousey)
            machinedam.append(9)
            machinere.append(6)
            machinera.append(150)
            machineshot.append(1)
            machineup.append(1)
            machinespr.append(10)
        if dragging == "minigun" and mousedown == False and breakv == False:
            minigunx.append(mousex)
            miniguny.append(mousey)
            minigundam.append(9)
            minigunre.append(6)
            minigunup.append(1)
            minigunspr.append(10)
        if dragging == "cannon" and mousedown == False and breakv == False:
            cannonx.append(mousex)
            cannony.append(mousey)
            cannondam.append(2.5)
            cannonre.append(60)
            cannonra.append(150)
            cannonshot.append(1)
            cannonup.append(1)
        if breakv == True:
            breakv = False
        if mousedown == False:
            dragging = "none"

    for cat in range(0, len(bulletx)):
        bulletx[cat] += bulletxx[cat]
        bullety[cat] += bulletyy[cat]
        pygame.draw.circle(screen, (0, 0, 0), (round(bulletx[cat]), round(bullety[cat])), 4)
        if bulletx[cat] > 900 or bulletx[cat] < 0 or bullety[cat] < 0 or bullety[cat] > 475:
            bulletdel[cat] = 1
        for dog in range(0, len(enemy)):
            if -20 <= mapx[round(enemy[dog])] - bulletx[cat] <= 20 and -20 <= mapy[round(enemy[dog])] - bullety[cat] <= 20 and enemytype[dog] != "immune":
                enemyhit[dog] -= bulletdamage[cat]
            if -20 <= mapx[round(enemy[dog])] - bulletx[cat] <= 20 and -20 <= mapy[round(enemy[dog])] - bullety[cat] <= 20:
                bulletdel[cat] = 1

    for cat in range(0, len(bombx)):
        if bombdel[cat] == 0:
            bombx[cat] += bombxx[cat]
            bomby[cat] += bombyy[cat]
        pygame.draw.circle(screen, (255, 0, 0), (round(bombx[cat]), round(bomby[cat])), round(bombr[cat]), 10)
        if bombx[cat] > 900 or bombx[cat] < 0 or bomby[cat] < 0 or bomby[cat] > 475:
            bombdel[cat] = 1
        for dog in range(0, len(enemy)):
            if -20 <= mapx[round(enemy[dog])] - bombx[cat] <= 20 and -20 <= mapy[round(enemy[dog])] - bomby[cat] <= 20:
                bombdel[cat] = 1
        if bombdel[cat] == 1:
            bombr[cat] += bombradius[cat]/20
            for dog in range(0, len(enemy)):
                if -5 - bombr[cat] <= mapx[round(enemy[dog])] - bombx[cat] <= 5 + bombr[cat] and -5 - bombr[cat] <= mapy[round(enemy[dog])] - bomby[cat] <= 5 + bombr[cat]:
                    enemyhit[dog] -= bombdamage[cat]
                    print(1)
            if bombr[cat] >= bombradius[cat]:
                bombdel[cat] = 2

    for cat in range(0, len(laserx)):
        laserx[cat] += laserxx[cat]
        lasery[cat] += laseryy[cat]
        pygame.draw.line(screen, (255, 0, 0), (round(laserx[cat]), round(lasery[cat])), (round(laserx[cat] - laserxx[cat]*5), round(lasery[cat] - laseryy[cat]*5)), 4)
        if laserx[cat] > 900 or laserx[cat] < 0 or lasery[cat] < 0 or lasery[cat] > 475:
            laserdel[cat] = 1
        for dog in range(0, len(enemy)):
            if -20 <= mapx[round(enemy[dog])] - laserx[cat] <= 20 and -20 <= mapy[round(enemy[dog])] - lasery[cat] <= 20 and enemytype[dog] == "immune2":
                laserdel[cat] = 1
                for monkey in range(0, 10):
                    pygame.draw.line(screen, (255, 255, 150), (laserx[cat]+laserxx[cat], lasery[cat]+laseryy[cat]),
                                     (laserx[cat]+laserxx[cat] + random.randint(-20, 20), lasery[cat]+laseryy[cat]+ random.randint(-20, 20)), 3)
            if -20 <= mapx[round(enemy[dog])] - laserx[cat] <= 20 and -20 <= mapy[round(enemy[dog])] - lasery[cat] <= 20:
                enemyhit[dog] -= laserdamage[cat]
                backtimer[dog] = 0

    for cat in range(0, len(magicx)):
        magicx[cat] += magicxx[cat]
        magicy[cat] += magicyy[cat]
        pygame.draw.circle(screen, (150, 170, 255), (round(magicx[cat]), round(magicy[cat])), 10)
        pygame.draw.polygon(screen, (150, 170, 255), (
            (round(magicx[cat]) - round(magicyy[cat]/1.5), round(magicy[cat]) + round(magicxx[cat]/1.5)),
            (round(magicx[cat]) + round(magicyy[cat]/1.5), round(magicy[cat]) - round(magicxx[cat]/1.5)),
            (round(magicx[cat]) - 2 * round(magicxx[cat]), round(magicy[cat]) - 2 * round(magicyy[cat]))))
        if magicx[cat] > 900 or magicx[cat] < 0 or magicy[cat] < 0 or magicy[cat] > 500:
            magicp[cat] -= 0.2
        for dog in range(0, len(enemy)):
            if -20 <= mapx[round(enemy[dog])] - magicx[cat] <= 20 and -20 <= mapy[round(enemy[dog])] - magicy[cat] <= 20 and enemytype[dog] == "immune2":
                magicdel[cat] = 1
                for monkey in range(0, 10):
                    pygame.draw.line(screen, (255, 255, 150), (magicx[cat]+magicxx[cat], magicy[cat]+magicyy[cat]),
                                     (magicx[cat]+magicxx[cat] + random.randint(-20, 20), magicy[cat]+magicyy[cat]+ random.randint(-20, 20)), 3)
            if -20 <= mapx[round(enemy[dog])] - magicx[cat] <= 20 and -20 <= mapy[round(enemy[dog])] - magicy[cat] <= 20 and enemytype[dog] != "immune2":
                enemyhit[dog] -= magicdamage[cat]
                magicp[cat] -= 1
        if len(enemy) != 0:
            if (mapx[round(max(enemy))] - magicx[cat]) != 0:
                if magicxx[cat] > 0 and (mapx[round(max(enemy))] - magicx[cat]) > 0 or (
                        mapx[round(max(enemy))] - magicx[cat]) < 0 and magicxx[
                    cat] < 0:
                    if magicyy[cat] / magicxx[cat] < (mapy[round(max(enemy))] - magicy[cat]) / (
                            mapx[round(max(enemy))] - magicx[cat]):
                        aimturn = "right"
                    if magicyy[cat] / magicxx[cat] > (mapy[round(max(enemy))] - magicy[cat]) / (
                            mapx[round(max(enemy))] - magicx[cat]):
                        aimturn = "left"
                if magicxx[cat] > 0 and (mapx[round(max(enemy))] - magicx[cat]) < 0 or (
                        mapx[round(max(enemy))] - magicx[cat]) > 0 and magicxx[
                    cat] < 0:
                    if magicyy[cat] / magicxx[cat] < (mapy[round(max(enemy))] - magicy[cat]) / (
                            mapx[round(max(enemy))] - magicx[cat]):
                        aimturn = "left"
                    if magicyy[cat] / magicxx[cat] > (mapy[round(max(enemy))] - magicy[cat]) / (
                            mapx[round(max(enemy))] - magicx[cat]):
                        aimturn = "right"
                if aimturn == "left":
                    if magicxx[cat] < 0 and magicyy[cat] < 0:
                        magicxx[cat] -= 1.5
                        magicyy[cat] += 1.5
                    if magicxx[cat] < 0 and magicyy[cat] > 0:
                        magicxx[cat] += 1.5
                        magicyy[cat] += 1.5
                    if magicxx[cat] > 0 and magicyy[cat] < 0:
                        magicxx[cat] -= 1.5
                        magicyy[cat] -= 1.5
                    if magicxx[cat] > 0 and magicyy[cat] > 0:
                        magicxx[cat] += 1.5
                        magicyy[cat] -= 1.5
                if aimturn == "right":
                    if magicxx[cat] < 0 and magicyy[cat] < 0:
                        magicxx[cat] += 1.5
                        magicyy[cat] -= 1.5
                    if magicxx[cat] < 0 and magicyy[cat] > 0:
                        magicxx[cat] -= 1.5
                        magicyy[cat] -= 1.5
                    if magicxx[cat] > 0 and magicyy[cat] < 0:
                        magicxx[cat] += 1.5
                        magicyy[cat] += 1.5
                    if magicxx[cat] > 0 and magicyy[cat] > 0:
                        magicxx[cat] -= 1.5
                        magicyy[cat] += 1.5
        if magicp[cat] <= 0:
            magicdel[cat] = 1
        if abs(magicxx[cat]) + abs(magicyy[cat]) > 20:
            if magicxx[cat] < 0:
                magicxx[cat] += 0.1
            else:
                magicxx[cat] -= 0.1
            if magicyy[cat] < 0:
                magicyy[cat] += 0.1
            else:
                magicyy[cat] -= 0.1

    for cat in range(0, len(basicx)):
        pygame.draw.rect(screen, (200, 200, 200), (basicx[cat] - 25, basicy[cat] - 25, 50, 50))
        pygame.draw.circle(screen, (120, 120, 120), (basicx[cat], basicy[cat]), 16)
        pygame.draw.circle(screen, (120, 120, 120), (basicx[cat], basicy[cat]), basicra[cat], 1)
        if len(enemy) == 0:
            pygame.draw.rect(screen, (120, 120, 120), (basicx[cat] - 8, basicy[cat] - 32, 16, 32))
        if len(enemy) != 0:
            xdistance = (basicx[cat] - mapx[round(basicshot[cat])])
            ydistance = (basicy[cat] - mapy[round(basicshot[cat])])
            distance = math.sqrt((mapx[round(basicshot[cat])] - basicx[cat]) ** 2 + (mapy[round(basicshot[cat])] - basicy[cat]) ** 2)
            pygame.draw.polygon(screen, (120, 120, 120), ((basicx[cat] + round(ydistance * 8 / distance), basicy[cat] - round(xdistance * 8 / distance)),
                        (basicx[cat] - round(ydistance * 8 / distance), basicy[cat] + round(xdistance * 8 / distance)),
                        (basicx[cat] - round(ydistance * 8 / distance) - round(xdistance * 30 / distance),
                        basicy[cat] + round(xdistance * 8 / distance) - round(ydistance * 30 / distance)), (basicx[cat] + round(ydistance * 8 / distance) -
                        round(xdistance*30/distance), basicy[cat] - round(xdistance * 8 / distance) - round(ydistance*30/distance))))
        for dog in range(0, len(enemy)):
            if (basicx[cat] - mapx[round(enemy[dog])])**2 + (basicy[cat] - mapy[round(enemy[dog])])**2 <= basicra[cat]**2:
                inrange = True
                break
        if inrange == True and (stopwatch / basicre[cat]) % 1 == 0 and len(enemy) != 0:
            value = 0
            while True:
                value += 1
                if (basicx[cat] - mapx[round(heapq.nlargest(value, enemy)[value - 1])])**2 + (basicy[cat] - mapy[round(heapq.nlargest(value, enemy)[value - 1])])**2 <= basicra[cat]**2:
                    basicshot[cat] = round(heapq.nlargest(value, enemy)[value - 1])
                    break
            distance = math.sqrt((mapx[round(basicshot[cat])] - basicx[cat]) ** 2 + (mapy[round(basicshot[cat])] - basicy[cat]) ** 2)
            if distance != 0:
                bulletx.append(basicx[cat])
                bullety.append(basicy[cat])
                bulletdel.append(0)
                bulletdamage.append(basicdam[cat])
                bulletxx.append(10 * (mapx[round(basicshot[cat])] - basicx[cat]) / distance)
                bulletyy.append(10 * (mapy[round(basicshot[cat])] - basicy[cat]) / distance)
        inrange = False

    for cat in range(0, len(lasertx)):
        pygame.draw.rect(screen, (200, 200, 200), (lasertx[cat] - 25, laserty[cat] - 25, 50, 50))
        pygame.draw.circle(screen, (255, 0, 0), (lasertx[cat], laserty[cat]), 16)
        pygame.draw.circle(screen, (255, 0, 0), (lasertx[cat], laserty[cat]), lasertra[cat], 1)
        if len(enemy) == 0:
            pygame.draw.rect(screen, (255, 0, 0), (lasertx[cat] - 8, laserty[cat] - 32, 16, 32))
        if len(enemy) != 0:
            xdistance = (lasertx[cat] - mapx[round(lasertshot[cat])])
            ydistance = (laserty[cat] - mapy[round(lasertshot[cat])])
            distance = math.sqrt((mapx[round(lasertshot[cat])] - lasertx[cat]) ** 2 + (mapy[round(lasertshot[cat])] - laserty[cat]) ** 2)
            if distance != 0:
                pygame.draw.polygon(screen, (255, 0, 0), ((lasertx[cat] + round(ydistance * 8 / distance), laserty[cat] - round(xdistance * 8 / distance)),
                        (lasertx[cat] - round(ydistance * 8 / distance), laserty[cat] + round(xdistance * 8 / distance)),
                        (lasertx[cat] - round(ydistance * 8 / distance) - round(xdistance * 30 / distance),
                        laserty[cat] + round(xdistance * 8 / distance) - round(ydistance * 30 / distance)), (lasertx[cat] + round(ydistance * 8 / distance) -
                        round(xdistance*30/distance), laserty[cat] - round(xdistance * 8 / distance) - round(ydistance*30/distance))))
        for dog in range(0, len(enemy)):
            if (lasertx[cat] - mapx[round(enemy[dog])])**2 + (laserty[cat] - mapy[round(enemy[dog])])**2 <= lasertra[cat]**2:
                inrange = True
                break
        if inrange == True and (stopwatch / lasertre[cat]) % 1 == 0 and len(enemy) != 0:
            value = 0
            while True:
                value += 1
                if (lasertx[cat] - mapx[round(heapq.nlargest(value, enemy)[value - 1])])**2 + (laserty[cat] - mapy[round(heapq.nlargest(value, enemy)[value - 1])])**2 <= lasertra[cat]**2:
                    lasertshot[cat] = round(heapq.nlargest(value, enemy)[value - 1])
                    break
            distance = math.sqrt((mapx[round(lasertshot[cat])] - lasertx[cat]) ** 2 + (mapy[round(lasertshot[cat])] - laserty[cat]) ** 2)
            if distance != 0:
                laserx.append(lasertx[cat])
                lasery.append(laserty[cat])
                laserdel.append(0)
                laserdamage.append(lasertdam[cat])
                laserxx.append(10 * (mapx[round(lasertshot[cat])] - lasertx[cat]) / distance)
                laseryy.append(10 * (mapy[round(lasertshot[cat])] - laserty[cat]) / distance)
        inrange = False

    for cat in range(0, len(wizardx)):
        pygame.draw.rect(screen, (0, 0, 0), (wizardx[cat] - 25, wizardy[cat] - 25, 50, 50))
        pygame.draw.circle(screen, (0, 0, 255), (wizardx[cat], wizardy[cat]), 16)
        pygame.draw.circle(screen, (0, 0, 255), (wizardx[cat], wizardy[cat]), wizardra[cat], 1)
        if len(enemy) == 0:
            pygame.draw.rect(screen, (0, 0, 255), (wizardx[cat] - 8, wizardy[cat] - 32, 16, 32))
        if len(enemy) != 0:
            xdistance = (wizardx[cat] - mapx[round(wizardshot[cat])])
            ydistance = (wizardy[cat] - mapy[round(wizardshot[cat])])
            distance = math.sqrt((mapx[round(wizardshot[cat])] - wizardx[cat]) ** 2 + (mapy[round(wizardshot[cat])] - wizardy[cat]) ** 2)
            if distance != 0:
                pygame.draw.polygon(screen, (0, 0, 255), ((wizardx[cat] + round(ydistance * 8 / distance), wizardy[cat] - round(xdistance * 8 / distance)),
                        (wizardx[cat] - round(ydistance * 8 / distance), wizardy[cat] + round(xdistance * 8 / distance)),
                        (wizardx[cat] - round(ydistance * 8 / distance) - round(xdistance * 30 / distance),
                        wizardy[cat] + round(xdistance * 8 / distance) - round(ydistance * 30 / distance)), (wizardx[cat] + round(ydistance * 8 / distance) -
                        round(xdistance*30/distance), wizardy[cat] - round(xdistance * 8 / distance) - round(ydistance*30/distance))))
        for dog in range(0, len(enemy)):
            if (wizardx[cat] - mapx[round(enemy[dog])])**2 + (wizardy[cat] - mapy[round(enemy[dog])])**2 <= wizardra[cat]**2:
                inrange = True
                break
        if inrange == True and (stopwatch / wizardre[cat]) % 1 == 0 and len(enemy) != 0:
            value = 0
            while True:
                value += 1
                if (wizardx[cat] - mapx[round(heapq.nlargest(value, enemy)[value - 1])])**2 + (wizardy[cat] - mapy[round(heapq.nlargest(value, enemy)[value - 1])])**2 <= wizardra[cat]**2:
                    wizardshot[cat] = round(heapq.nlargest(value, enemy)[value - 1])
                    break
            distance = math.sqrt((mapx[round(wizardshot[cat])] - wizardx[cat]) ** 2 + (mapy[round(wizardshot[cat])] - wizardy[cat]) ** 2)
            if distance != 0:
                magicx.append(wizardx[cat])
                magicy.append(wizardy[cat])
                magicdel.append(0)
                magicdamage.append(wizarddam[cat])
                magicxx.append(15 * (mapx[round(wizardshot[cat])] - wizardx[cat]) / distance)
                magicyy.append(15 * (mapy[round(wizardshot[cat])] - wizardy[cat]) / distance)
                magicp.append(10)
        inrange = False

    for cat in range(0, len(cannonx)):
        pygame.draw.rect(screen, (200, 200, 200), (cannonx[cat] - 25, cannony[cat] - 25, 50, 50))
        pygame.draw.circle(screen, (0, 0, 0), (cannonx[cat], cannony[cat]), 20)
        pygame.draw.circle(screen, (0, 0, 0), (cannonx[cat], cannony[cat]), cannonra[cat], 1)
        if len(enemy) == 0:
            pygame.draw.rect(screen, (0, 0, 0), (cannonx[cat] - 12, cannony[cat] - 32, 24, 32))
        if len(enemy) != 0:
            xdistance = (cannonx[cat] - mapx[round(cannonshot[cat])])
            ydistance = (cannony[cat] - mapy[round(cannonshot[cat])])
            distance = math.sqrt((mapx[round(cannonshot[cat])] - cannonx[cat]) ** 2 + (mapy[round(cannonshot[cat])] - cannony[cat]) ** 2)
            if distance != 0:
                pygame.draw.polygon(screen, (0, 0, 0), ((cannonx[cat] + round(ydistance * 12 / distance), cannony[cat] - round(xdistance * 12 / distance)),
                        (cannonx[cat] - round(ydistance * 12 / distance), cannony[cat] + round(xdistance * 12 / distance)),
                        (cannonx[cat] - round(ydistance * 12 / distance) - round(xdistance * 30 / distance),
                        cannony[cat] + round(xdistance * 12 / distance) - round(ydistance * 30 / distance)), (cannonx[cat] + round(ydistance * 12 / distance) -
                        round(xdistance*30/distance), cannony[cat] - round(xdistance * 12 / distance) - round(ydistance*30/distance))))
        for dog in range(0, len(enemy)):
            if (cannonx[cat] - mapx[round(enemy[dog])])**2 + (cannony[cat] - mapy[round(enemy[dog])])**2 <= cannonra[cat]**2:
                inrange = True
                break
        if inrange == True and (stopwatch / cannonre[cat]) % 1 == 0 and len(enemy) != 0:
            value = 0
            while True:
                value += 1
                if (cannonx[cat] - mapx[round(heapq.nlargest(value, enemy)[value - 1])])**2 + (cannony[cat] - mapy[round(heapq.nlargest(value, enemy)[value - 1])])**2 <= cannonra[cat]**2:
                    cannonshot[cat] = round(heapq.nlargest(value, enemy)[value - 1])
                    break
            distance = math.sqrt((mapx[round(cannonshot[cat])] - cannonx[cat]) ** 2 + (mapy[round(cannonshot[cat])] - cannony[cat]) ** 2)
            if distance != 0:
                bombx.append(cannonx[cat])
                bomby.append(cannony[cat])
                bombdel.append(0)
                bombdamage.append(cannondam[cat])
                bombxx.append(15 * (mapx[round(cannonshot[cat])] - cannonx[cat]) / distance)
                bombyy.append(15 * (mapy[round(cannonshot[cat])] - cannony[cat]) / distance)
                bombr.append(10)
                bombradius.append(100)
        inrange = False

    for cat in range(0, len(minigunx)):
        pygame.draw.rect(screen, (50, 50, 50), (minigunx[cat] - 25, miniguny[cat] - 25, 50, 50))
        pygame.draw.circle(screen, (120, 120, 120), (minigunx[cat], miniguny[cat]), 16)
        distance = math.sqrt((mousex - minigunx[cat]) ** 2 + (mousey - miniguny[cat]) ** 2)
        if distance != 0:
            xdistance = (minigunx[cat] - mousex)
            ydistance = (miniguny[cat] - mousey)
            pygame.draw.polygon(screen, (120, 120, 120), ((minigunx[cat] + round(ydistance * 8 / distance), miniguny[cat] - round(xdistance * 8 / distance)),
                        (minigunx[cat] - round(ydistance * 8 / distance), miniguny[cat] + round(xdistance * 8 / distance)),
                        (minigunx[cat] - round(ydistance * 16 / distance) - round(xdistance * 30 / distance),
                        miniguny[cat] + round(xdistance * 16 / distance) - round(ydistance * 30 / distance)), (minigunx[cat] + round(ydistance * 16 / distance) -
                        round(xdistance*30/distance), miniguny[cat] - round(xdistance * 16 / distance) - round(ydistance*30/distance))))
        if (stopwatch / minigunre[cat]) % 1 == 0:
            distance = math.sqrt((mousex - minigunx[cat]) ** 2 + (mousey - miniguny[cat]) ** 2)
            if distance != 0:
                bulletx.append(minigunx[cat])
                bullety.append(miniguny[cat])
                bulletdel.append(0)
                bulletdamage.append(minigundam[cat])
                bulletxx.append(10 * (mousex - minigunx[cat]) / distance + random.randint(-minigunspr[cat], minigunspr[cat])/10)
                bulletyy.append(10 * (mousey - miniguny[cat]) / distance + random.randint(-minigunspr[cat], minigunspr[cat])/10)
        inrange = False
        
    for cat in range(0, len(machinex)):
        pygame.draw.rect(screen, (200, 200, 200), (machinex[cat] - 25, machiney[cat] - 25, 50, 50))
        pygame.draw.circle(screen, (120, 120, 120), (machinex[cat], machiney[cat]), 16)
        pygame.draw.circle(screen, (120, 120, 120), (machinex[cat], machiney[cat]), machinera[cat], 1)
        if len(enemy) == 0:
            pygame.draw.polygon(screen, (120, 120, 120), ((machinex[cat] + 15, machiney[cat] - 32), (machinex[cat] - 15, machiney[cat] - 32), (machinex[cat] - 8, machiney[cat]), (machinex[cat] + 8, machiney[cat])))
        if len(enemy) != 0:
            xdistance = (machinex[cat] - mapx[round(machineshot[cat])])
            ydistance = (machiney[cat] - mapy[round(machineshot[cat])])
            distance = math.sqrt((mapx[round(machineshot[cat])] - machinex[cat]) ** 2 + (mapy[round(machineshot[cat])] - machiney[cat]) ** 2)
            pygame.draw.polygon(screen, (120, 120, 120), ((machinex[cat] + round(ydistance * 8 / distance), machiney[cat] - round(xdistance * 8 / distance)),
                        (machinex[cat] - round(ydistance * 8 / distance), machiney[cat] + round(xdistance * 8 / distance)),
                        (machinex[cat] - round(ydistance * 16 / distance) - round(xdistance * 30 / distance),
                        machiney[cat] + round(xdistance * 16 / distance) - round(ydistance * 30 / distance)), (machinex[cat] + round(ydistance * 16 / distance) -
                        round(xdistance*30/distance), machiney[cat] - round(xdistance * 16 / distance) - round(ydistance*30/distance))))
        for dog in range(0, len(enemy)):
            if (machinex[cat] - mapx[round(enemy[dog])])**2 + (machiney[cat] - mapy[round(enemy[dog])])**2 <= machinera[cat]**2:
                inrange = True
                break
        if inrange == True and (stopwatch / machinere[cat]) % 1 == 0 and len(enemy) != 0:
            value = 0
            while True:
                value += 1
                if (machinex[cat] - mapx[round(heapq.nlargest(value, enemy)[value - 1])])**2 + (machiney[cat] - mapy[round(heapq.nlargest(value, enemy)[value - 1])])**2 <= machinera[cat]**2:
                    machineshot[cat] = round(heapq.nlargest(value, enemy)[value - 1])
                    break
            bulletx.append(machinex[cat])
            bullety.append(machiney[cat])
            bulletdel.append(0)
            bulletdamage.append(machinedam[cat])
            distance = math.sqrt((mapx[round(machineshot[cat])] - machinex[cat]) ** 2 + (mapy[round(machineshot[cat])] - machiney[cat]) ** 2)
            if distance != 0:
                bulletxx.append(10 * (mapx[round(machineshot[cat])] - machinex[cat]) / distance + random.randint(-machinespr[cat], machinespr[cat])/10)
                bulletyy.append(10 * (mapy[round(machineshot[cat])] - machiney[cat]) / distance + random.randint(-machinespr[cat], machinespr[cat])/10)
        inrange = False

    for dog in range(0, len(bulletx)):
        for cat in range(0, len(bulletx)):
            if bulletdel[cat] == 1:
                del bulletx[cat]
                del bullety[cat]
                del bulletxx[cat]
                del bulletyy[cat]
                del bulletdamage[cat]
                del bulletdel[cat]
                break

    for dog in range(0, len(laserx)):
        for cat in range(0, len(laserx)):
            if laserdel[cat] == 1:
                del laserx[cat]
                del lasery[cat]
                del laserxx[cat]
                del laseryy[cat]
                del laserdamage[cat]
                del laserdel[cat]
                break

    for dog in range(0, len(magicx)):
        for cat in range(0, len(magicx)):
            if magicdel[cat] == 1:
                del magicx[cat]
                del magicy[cat]
                del magicxx[cat]
                del magicyy[cat]
                del magicdamage[cat]
                del magicdel[cat]
                del magicp[cat]
                break

    for dog in range(0, len(bombx)):
        for cat in range(0, len(bombx)):
            if bombdel[cat] == 2:
                del bombx[cat]
                del bomby[cat]
                del bombxx[cat]
                del bombyy[cat]
                del bombdamage[cat]
                del bombdel[cat]
                del bombr[cat]
                del bombradius[cat]
                break

    if round(lives) <= 0:
        enemy = []
        enemyspeed = []
        enemydel = []
        enemyhit = []
        enemyhitt = []
        enemysplit = []
        enemytype = []
        enemystate = []
        stuntimer = []
        backtimer = []
        bulletx = []
        bullety = []
        bulletxx = []
        bulletyy = []
        bulletdamage = []
        bulletdel = []
        laserx = []
        lasery = []
        laserxx = []
        laseryy = []
        laserdamage = []
        laserdel = []
        magicx = []
        magicy = []
        magicxx = []
        magicyy = []
        magicdamage = []
        magicp = []
        magicdel = []
        bombx = []
        bomby = []
        bombxx = []
        bombyy = []
        bombradius = []
        bombr = []
        bombdamage = []
        bombdel = []
        basicx = []
        basicy = []
        basicra = []
        basicdam = []
        basicre = []
        basicshot = []
        basicup = []
        wizardx = []
        wizardy = []
        wizardra = []
        wizarddam = []
        wizardre = []
        wizardshot = []
        wizardup = []
        cannonx = []
        cannony = []
        cannonra = []
        cannondam = []
        cannonre = []
        cannonshot = []
        cannonup = []
        lasertx = []
        laserty = []
        lasertra = []
        lasertdam = []
        lasertre = []
        lasertshot = []
        lasertup = []
        machinex = []
        machiney = []
        machinera = []
        machinedam = []
        machinespr = []
        machinere = []
        machineshot = []
        machineup = []
        minigunx = []
        miniguny = []
        minigunre = []
        minigundam = []
        minigunspr = []
        minigunup = []
        grave = []
        gravesplit = []
        gravehealth = []
        gravetimer = []
        gravedel = []
        stopwatch = 0
        lives = 100
        money = 500
        inrange = False

    for cat in range(0, len(grave)):
        pygame.draw.circle(screen, (80, 80, 80), (mapx[round(grave[cat])], mapy[round(grave[cat])] - 50), 18)
        pygame.draw.rect(screen, (80, 80, 80), (mapx[round(grave[cat])] - 18, mapy[round(grave[cat])] - 50, 36, 50))
        gravetimer[cat] -= 1
        if gravetimer[cat] <= 0:
            gravedel[cat] = 1
        if (gravetimer[cat] / 50) % 1 == 0 and gravetimer[cat] <= 200:
            choice = random.randint(1, 100)
            if choice <= 75:
                spawn_enemy(grave[cat], gravehealth[cat], gravesplit[cat], "normal", 0, 0)
            elif choice <= 80:
                spawn_enemy(grave[cat], gravehealth[cat]*4, gravesplit[cat], "strong", 0, 0)
            elif choice <= 85:
                spawn_enemy(grave[cat], gravehealth[cat]*1.4, gravesplit[cat], "healthy", 0, 0)
            elif choice <= 90:
                spawn_enemy(grave[cat], gravehealth[cat]*0.7, gravesplit[cat], "fast", 0, 0)
            elif choice <= 95:
                spawn_enemy(grave[cat], gravehealth[cat], gravesplit[cat], "immune2", 0, 0)
            else:
                spawn_enemy(grave[cat], gravehealth[cat], gravesplit[cat], "immune", 0, 0)

    for dog in range(0, len(grave)):
        for cat in range(0, len(grave)):
            if gravedel[cat] == 1:
                del grave[cat]
                del gravedel[cat]
                del gravehealth[cat]
                del gravesplit[cat]
                del gravetimer[cat]
                break

    if len(enemy) >= 100:
        for cat in range(0, len(enemy) - 100):
            choice = random.randint(0, len(enemy) - 101)
            enemydel[choice] = 1
            for dog in range(0, len(enemy)):
                enemyhit[dog] += enemyhit[choice]/50
                enemyhitt[dog] += enemyhit[choice]/50

    for cat in range(0, len(enemy)):
        stuntimer[cat] -= 1
        backtimer[cat] -= 1
        if enemytype[cat] == "normal":
            if enemyhit[cat] > 100 + stopwatch / 12:
                enemyhit[cat] = 100 + stopwatch / 12
                enemyhitt[cat] = 100 + stopwatch / 12
        if enemytype[cat] == "fast":
            if enemyhit[cat] > 80 + stopwatch / 16:
                enemyhit[cat] = 80 + stopwatch / 16
                enemyhitt[cat] = 80 + stopwatch / 16
        if enemytype[cat] == "immune":
            if enemyhit[cat] > 110 + stopwatch / 11:
                enemyhit[cat] = 110 + stopwatch / 11
                enemyhitt[cat] = 110 + stopwatch / 11
        if enemytype[cat] == "immune2":
            if enemyhit[cat] > 110 + stopwatch / 11:
                enemyhit[cat] = 110 + stopwatch / 11
                enemyhitt[cat] = 110 + stopwatch / 11
        if enemytype[cat] == "healthy":
            if enemyhit[cat] > 150 + stopwatch / 8:
                enemyhit[cat] = 150 + stopwatch / 8
                enemyhitt[cat] = 150 + stopwatch / 8
        if enemytype[cat] == "strong":
            if enemyhit[cat] > 250 + stopwatch / 5:
                enemyhit[cat] = 250 + stopwatch / 5
                enemyhitt[cat] = 250 + stopwatch / 5
        if enemytype[cat] == "zombie":
            if enemyhit[cat] > 90 + stopwatch / 14:
                enemyhit[cat] = 90 + stopwatch / 14
                enemyhitt[cat] = 90 + stopwatch / 14
        if enemytype[cat] == "necro":
            if enemyhit[cat] > 150 + stopwatch / 7:
                enemyhit[cat] = 150 + stopwatch / 7
                enemyhitt[cat] = 150 + stopwatch / 7
        if enemyhit[cat] < enemyhitt[cat]:
            if enemytype[cat] != "zombie" and enemytype[cat] != "necro" and enemytype[cat] != "healthy":
                enemyhit[cat] += 0.1
                enemyhit[cat] += enemyhitt[cat]/3000
            if enemytype[cat] == "healthy":
                enemyhit[cat] += 0.6
                enemyhit[cat] += enemyhitt[cat]/600
        if enemyhit[cat] <= 0:
            enemydel[cat] = 1
            if enemytype[cat] == "zombie":
                grave.append(enemy[cat])
                gravesplit.append(enemysplit[cat])
                gravehealth.append(enemyhitt[cat])
                gravetimer.append(random.randint(9, 20) * 50)
                gravedel.append(0)
            if enemytype[cat] == "necro":
                for dog in range(0, 3):
                    grave.append(enemy[cat] - 10 + 10 * dog)
                    gravesplit.append(enemysplit[cat])
                    gravehealth.append(enemyhitt[cat])
                    gravetimer.append(random.randint(9, 30) * 50)
                    gravedel.append(0)
            if enemysplit[cat] == "normal":
                enemydel[cat] = 1
            if enemysplit[cat] == "split":
                spawn_enemy(enemy[cat] - random.randint(8, 10), enemyhitt[cat], "normal", enemytype[cat], stuntimer[cat], backtimer[cat])
                spawn_enemy(enemy[cat] + random.randint(8, 10), enemyhitt[cat], "normal", enemytype[cat], stuntimer[cat], backtimer[cat])
            if enemysplit[cat] == "splitt":
                spawn_enemy(enemy[cat] + random.randint(8, 10), enemyhitt[cat], "split", enemytype[cat], stuntimer[cat], backtimer[cat])
            if enemysplit[cat] == "splittt":
                spawn_enemy(enemy[cat] - random.randint(15, 17), enemyhitt[cat], "splitt", enemytype[cat], stuntimer[cat], backtimer[cat])
                spawn_enemy(enemy[cat], enemyhitt[cat], "splitt", enemytype[cat], stuntimer[cat], backtimer[cat])
                spawn_enemy(enemy[cat] + random.randint(15, 17), enemyhitt[cat], "splitt", enemytype[cat], stuntimer[cat], backtimer[cat])
            if enemysplit[cat] == "splitttt":
                spawn_enemy(enemy[cat] - random.randint(8, 10), enemyhitt[cat], "splittt", enemytype[cat], stuntimer[cat], backtimer[cat])
                spawn_enemy(enemy[cat] + random.randint(8, 10), enemyhitt[cat], "splittt", enemytype[cat], stuntimer[cat], backtimer[cat])
                spawn_enemy(enemy[cat] - random.randint(28, 30), enemyhitt[cat], "splittt", enemytype[cat], stuntimer[cat], backtimer[cat])
                spawn_enemy(enemy[cat] + random.randint(28, 30), enemyhitt[cat], "splittt", enemytype[cat], stuntimer[cat], backtimer[cat])

    for cat in range(0, len(enemy)):
        if enemy[cat] + 1 >= len(mapx):
            lives -= enemyhit[cat]/50
            lives -= 1
            enemydel[cat] = 1
            enemy[cat] = len(mapx) - 1
        if enemy[cat] + 1 < 2:
            enemy[cat] = 2

    for dog in range(0, len(enemy)):
        for cat in range(0, len(enemy)):
            if enemydel[cat] == 1:
                del enemy[cat]
                del enemydel[cat]
                del enemyhit[cat]
                del enemyhitt[cat]
                del enemysplit[cat]
                del enemytype[cat]
                del enemystate[cat]
                del stuntimer[cat]
                del backtimer[cat]
                del enemyspeed[cat]
                break

    for cat in range(0, len(enemy)):
        if stuntimer[cat] < 0 and backtimer[cat] < 0:
            enemy[cat] += enemyspeed[cat]
        if backtimer[cat] >= 0:
            enemy[cat] -= enemyspeed[cat]
        if enemy[cat] + 1 >= len(mapx):
            lives -= enemyhit[cat]/50
            lives -= 1
            enemydel[cat] = 1
            enemy[cat] = len(mapx) - 1
        if enemyhit[cat] >= enemyhitt[cat]:
            enemyhit[cat] = enemyhitt[cat]
        pygame.draw.circle(screen, (255, 255, 255), (mapx[round(enemy[cat])], mapy[round(enemy[cat])]), 15)
        pygame.draw.rect(screen, (255, 255, 255), (mapx[round(enemy[cat])] - 18, mapy[round(enemy[cat])] + 20, 30, 3))
        if stuntimer[cat] > 0:
            pygame.draw.circle(screen, (255, 255, 255), (mapx[round(enemy[cat])], mapy[round(enemy[cat])] - 18), 2)
            pygame.draw.circle(screen, (255, 255, 255), (mapx[round(enemy[cat])] - 5, mapy[round(enemy[cat])] - 16), 2)
            pygame.draw.circle(screen, (255, 255, 255), (mapx[round(enemy[cat])] + 5, mapy[round(enemy[cat])] - 16), 2)
        if backtimer[cat] > 0:
            pygame.draw.circle(screen, (255, 255, 255), (mapx[round(enemy[cat])], mapy[round(enemy[cat])] - 18), 2)
            pygame.draw.circle(screen, (255, 255, 255), (mapx[round(enemy[cat])] - 5, mapy[round(enemy[cat])] - 16), 2)
            pygame.draw.circle(screen, (255, 255, 255), (mapx[round(enemy[cat])] + 5, mapy[round(enemy[cat])] - 16), 2)
            pygame.draw.circle(screen, (255, 255, 255), (mapx[round(enemy[cat])] - 10, mapy[round(enemy[cat])] - 13), 2)
            pygame.draw.circle(screen, (255, 255, 255), (mapx[round(enemy[cat])] + 10, mapy[round(enemy[cat])] - 13), 2)
        if enemyhitt[cat] != 0:
            pygame.draw.rect(screen, (255, 0, 0), (
mapx[round(enemy[cat])] - 18, mapy[round(enemy[cat])] + 20, 36 * enemyhit[cat] / enemyhitt[cat], 3))
        if (stopwatch / 120) % 1 == 0:
            if enemytype[cat] == "necro":
                spawn_enemy(enemy[cat], enemyhit[cat]/4, enemysplit[cat], "zombie", stuntimer[cat], backtimer[cat])
        if enemy[cat] + 2 >= len(mapx):
            lives -= enemyhit[cat]/50
            lives -= 1
            enemydel[cat] = 1
            enemy[cat] = len(mapx) - 1
        if enemytype[cat] == "immune":
            pygame.draw.circle(screen, (255, 150, 200), (mapx[round(enemy[cat])], mapy[round(enemy[cat])]), 15)
        if enemytype[cat] == "immune2":
            pygame.draw.circle(screen, (255, 150, 200), (mapx[round(enemy[cat])], mapy[round(enemy[cat])]), 15)
            pygame.draw.rect(screen, (255, 0, 0), (mapx[round(enemy[cat])] - 10, mapy[round(enemy[cat])] - 1, 20, 2))
        if enemytype[cat] == "fast":
            pygame.draw.circle(screen, (255, 255, 0), (mapx[round(enemy[cat])], mapy[round(enemy[cat])]), 15)
        if enemytype[cat] == "strong":
            pygame.draw.circle(screen, (0, 0, 255), (mapx[round(enemy[cat])], mapy[round(enemy[cat])]), 15)
        if enemytype[cat] == "zombie":
            pygame.draw.circle(screen, (80, 80, 80), (mapx[round(enemy[cat])], mapy[round(enemy[cat])]), 15)
        if enemytype[cat] == "necro":
            pygame.draw.circle(screen, (80, 80, 80), (mapx[round(enemy[cat])], mapy[round(enemy[cat])]), 25)
        if enemytype[cat] == "healthy":
            pygame.draw.circle(screen, (0, 255, 0), (mapx[round(enemy[cat])], mapy[round(enemy[cat])]), 15)
        if enemysplit[cat] == "split":
            pygame.draw.circle(screen, (0, 0, 0), (mapx[round(enemy[cat])], mapy[round(enemy[cat])]), 3)
        if enemysplit[cat] == "splitt":
            pygame.draw.circle(screen, (0, 0, 0), (mapx[round(enemy[cat])] - 4, mapy[round(enemy[cat])]), 3)
            pygame.draw.circle(screen, (0, 0, 0), (mapx[round(enemy[cat])] + 4, mapy[round(enemy[cat])]), 3)
        if enemysplit[cat] == "splittt":
            pygame.draw.circle(screen, (0, 0, 0), (mapx[round(enemy[cat])] - 4, mapy[round(enemy[cat])] + 2), 3)
            pygame.draw.circle(screen, (0, 0, 0), (mapx[round(enemy[cat])], mapy[round(enemy[cat])] - 3), 3)
            pygame.draw.circle(screen, (0, 0, 0), (mapx[round(enemy[cat])] + 4, mapy[round(enemy[cat])] + 2), 3)
        if enemysplit[cat] == "splitttt":
            pygame.draw.circle(screen, (0, 0, 0), (mapx[round(enemy[cat])] - 4, mapy[round(enemy[cat])] + 4), 3)
            pygame.draw.circle(screen, (0, 0, 0), (mapx[round(enemy[cat])] - 4, mapy[round(enemy[cat])] - 4), 3)
            pygame.draw.circle(screen, (0, 0, 0), (mapx[round(enemy[cat])] + 4, mapy[round(enemy[cat])] - 4), 3)
            pygame.draw.circle(screen, (0, 0, 0), (mapx[round(enemy[cat])] + 4, mapy[round(enemy[cat])] + 4), 3)

    screen.blit(lives_text, (10, 10))

    pygame.display.flip()
    clock.tick(100)