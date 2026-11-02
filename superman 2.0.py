import pygame

import sys

pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((1080,540))
stopwatch = 0

money = 2000
lives = 100

slide = "game"

upgrade1 = 0
upgrade2 = 0
upgrade3 = 0
upgrade4 = 0
upgrade5 = 0
upgrade6 = 0

delay1 = 0
delay2 = 0
delay3 = 0
delay4 = 0
delay5 = 0
delay6 = 0

enemyx = []
enemyy = []
enemyrank = []
enemyway = []
enemyhealth = []
enemyorig = []
enemystate = []
stuntimer = []

bulletx = []
bullety = []
bullethealth = []

gluex = []
gluey = []
gluehealth = []

gluebombx = []
gluebomby = []
gluebombdel = []

bombx = []
bomby = []
bombdel = []

maulerx = []
maulery = []
maulerdel = []

stunx = []
stuny = []

stunbombx = []
stunbomby = []
stunbombdel = []

def fire_bullet(x, y):
    bulletx.append(x)
    bullety.append(y)
    if upgrade3 <=3:
        bullethealth.append(1)
    elif upgrade3 <=6:
        bullethealth.append(2)
    elif upgrade3 <=8:
        bullethealth.append(4)
    if upgrade3 ==9:
        bullethealth.append(9)
def fire_glue(a, b):
    gluex.append(a)
    gluey.append(b)
def glue_bomb(g,h):
    gluebombx.append(g)
    gluebomby.append(h)
    gluebombdel.append("no")
def throw_bomb(c, d):
    bombx.append(c)
    bomby.append(d)
    bombdel.append("no")
def throw_stun(k,l):
    stunx.append(k)
    stuny.append(l)
def stun_bomb(h,j):
    stunbombx.append(h)
    stunbomby.append(j)
    stunbombdel.append("no")
def make_enemy(rank,health, locationx, locationy, way, state):
    enemyx.append(locationx)
    enemyy.append(locationy)
    enemyway.append(way)
    enemyrank.append(rank)
    enemyhealth.append(health)
    enemyorig.append(health)
    enemystate.append(state)
    stuntimer.append(0)
def delete_enemy(qyuyuy):
    del (enemyhealth[qyuyuy])
    del (enemyrank[qyuyuy])
    del (enemyx[qyuyuy])
    del (enemyy[qyuyuy])
    del (enemyway[qyuyuy])
    del (stuntimer[qyuyuy])
    del (enemyorig[qyuyuy])
    del (enemystate[qyuyuy])
font = pygame.font.Font("freesansbold.ttf", 32)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    mousex, mousey = pygame.mouse.get_pos()

    screen.fill((140, 140, 140))

    if slide == "game":
        if upgrade1 == 1 and (stopwatch/200) % 1 == 0:
            lives += 1
        if upgrade1 == 2 and (stopwatch/100) % 1 == 0:
            lives += 1
        if upgrade1 == 3 and (stopwatch/50) % 1 == 0:
            lives += 1
        if upgrade1 == 4 and (stopwatch/25) % 1 == 0:
            lives += 1
        if upgrade1 == 5 and (stopwatch/13) % 1 == 0:
            lives += 1
        if upgrade1 == 6 and (stopwatch/7) % 1 == 0:
            lives += 1
        if upgrade1 == 7 and (stopwatch/4) % 1 == 0:
            lives += 1
        if upgrade1 == 8 and (stopwatch/2) % 1 == 0:
            lives += 1
        if upgrade2 == 1 and (stopwatch/80) % 1 == 0:
            money += 1
        if upgrade2 == 2 and (stopwatch/40) % 1 == 0:
            money += 1
        if upgrade2 == 3 and (stopwatch/20) % 1 == 0:
            money += 1
        if upgrade2 == 4 and (stopwatch/10) % 1 == 0:
            money += 1
        if upgrade2 == 5 and (stopwatch/5) % 1 == 0:
            money += 1
        if upgrade2 == 6 and (stopwatch/3) % 1 == 0:
            money += 1
        if upgrade2 == 7 and (stopwatch/3) % 1 == 0:
            money += 2
        if upgrade2 == 8 and (stopwatch/3) % 1 == 0:
            money += 4
        if upgrade3 == 1 and (stopwatch/100) % 1 == 0:
            fire_bullet(mousex, mousey)
        if upgrade3 == 2 and (stopwatch/50) % 1 == 0:
            fire_bullet(mousex, mousey)
        if upgrade3 == 3 and (stopwatch/25) % 1 == 0:
            fire_bullet(mousex, mousey)
        if upgrade3 == 4 and (stopwatch/25) % 1 == 0:
            fire_bullet(mousex, mousey)
        if upgrade3 == 5 and (stopwatch/13) % 1 == 0:
            fire_bullet(mousex, mousey)
        if upgrade3 == 6 and (stopwatch/7) % 1 == 0:
            fire_bullet(mousex, mousey)
        if upgrade3 == 7 and (stopwatch/7) % 1 == 0:
            fire_bullet(mousex, mousey)
        if upgrade3 == 8 and (stopwatch/4) % 1 == 0:
            fire_bullet(mousex, mousey)
        if upgrade3 == 9 and (stopwatch/4) % 1 == 0:
            fire_bullet(mousex, mousey)
        if upgrade4 == 1 and (stopwatch/200) % 1 == 0:
            throw_bomb(mousex, mousey)
        if upgrade4 == 2 and (stopwatch/200) % 1 == 0:
            throw_bomb(mousex, mousey)
        if upgrade4 == 3 and (stopwatch/200) % 1 == 0:
            throw_bomb(mousex, mousey)
        if upgrade4 == 4 and (stopwatch/100) % 1 == 0:
            throw_bomb(mousex, mousey)
        if upgrade4 == 5 and (stopwatch/50) % 1 == 0:
            throw_bomb(mousex, mousey)
        if upgrade4 == 6 and (stopwatch/25) % 1 == 0:
            throw_bomb(mousex, mousey)
        if upgrade4 == 7 and (stopwatch/25) % 1 == 0:
            throw_bomb(mousex, mousey)
        if upgrade4 == 8 and (stopwatch/13) % 1 == 0:
            throw_bomb(mousex, mousey)
        if upgrade4 == 9 and (stopwatch/18) % 1 == 0:
            throw_bomb(mousex, mousey)
        if upgrade5 == 1 and (stopwatch/300) % 1 == 0:
            fire_glue(mousex, mousey)
        if upgrade5 == 2 and (stopwatch/150) % 1 == 0:
            fire_glue(mousex, mousey)
        if upgrade5 == 3 and (stopwatch/75) % 1 == 0:
            fire_glue(mousex, mousey)
        if upgrade5 == 4 and (stopwatch/75) % 1 == 0:
            fire_glue(mousex, mousey)
        if upgrade5 == 5 and (stopwatch/38) % 1 == 0:
            fire_glue(mousex, mousey)
        if upgrade5 == 6 and (stopwatch/20) % 1 == 0:
            fire_glue(mousex, mousey)
        if upgrade5 == 7 and (stopwatch/20) % 1 == 0:
            fire_glue(mousex, mousey)
        if upgrade5 == 8 and (stopwatch/10) % 1 == 0:
            fire_glue(mousex, mousey)
        if upgrade5 == 9 and (stopwatch/25) % 1 == 0:
            glue_bomb(mousex, mousey)
        if upgrade6 == 1 and (stopwatch/200) % 1 == 0:
            throw_stun(mousex, mousey)
        if upgrade6 == 2 and (stopwatch/100) % 1 == 0:
            throw_stun(mousex, mousey)
        if upgrade6 == 3 and (stopwatch/100) % 1 == 0:
            throw_stun(mousex, mousey)
        if upgrade6 == 4 and (stopwatch/200) % 1 == 0:
            stun_bomb(mousex, mousey)
        if upgrade6 == 5 and (stopwatch/100) % 1 == 0:
            stun_bomb(mousex, mousey)
        if upgrade6 == 6 and (stopwatch/100) % 1 == 0:
            stun_bomb(mousex, mousey)
        if upgrade6 == 7 and (stopwatch/100) % 1 == 0:
            stun_bomb(mousex, mousey)
        if upgrade6 == 8 and (stopwatch/50) % 1 == 0:
            stun_bomb(mousex, mousey)
        if upgrade6 == 9 and (stopwatch/50) % 1 == 0:
            stun_bomb(mousex, mousey)

    if event.type == pygame.MOUSEBUTTONDOWN:
        slide = "upgrades"
    if slide == "upgrades":
        if event.type == pygame.MOUSEBUTTONDOWN:
            if mousex < 100:
                if mousey < 20:
                    slide = "game"

    if slide == "game":
        stopwatch += 1

    for s in range(0,3):
        if stopwatch == 20*s+400:
            make_enemy("pink", 2, 200, -20, "down", "normal")
    if stopwatch == 1000:
        make_enemy("white", 1, 200, -20, "down", "normal")
    for s in range(0,50):
        if stopwatch == 40*s+2000:
            make_enemy("red", 1, 200, -20, "down", "normal")
    for s in range(0,30):
        if stopwatch == 50*s+2200:
            make_enemy("blue", 1, 200, -20, "down", "normal")
    for s in range(0,20):
        if stopwatch == 60*s+2400:
            make_enemy("green", 1, 200, -20, "down", "normal")
    for s in range(0,2):
        if stopwatch == 4*s+4000:
            make_enemy("white", 1, 200, -20, "down", "normal")
            money += 2000
    for s in range(0,50):
        if stopwatch == 40*s+5500:
            make_enemy("red", 1, 200, -20, "down", "fast")
            money += 40
    for s in range(0,30):
        if stopwatch == 50*s+5700:
            make_enemy("green", 1, 200, -20, "down", "normal")
    for s in range(0,13):
        if stopwatch == 100*s+5900:
            make_enemy("black", 1, 200, -20, "down", "normal")
            money += 300
    for s in range(0,5):
        if stopwatch == 5*s+7200:
            make_enemy("white", 5, 200, -20, "down", "normal")
            money += 2000
    for s in range(0,20):
        if stopwatch == 10*s+8500:
            make_enemy("black", 1, 200, -20, "down", "normal")
    for s in range(0,10):
        if stopwatch == 5*s+9800:
            make_enemy("white", 1, 200, -20, "down", "normal")
    if stopwatch == 11000 or stopwatch == 11200:
        make_enemy("moab", 10, 200, -20, "down", "normal")
    for s in range(0,30):
        if stopwatch == 10*s+12300:
            make_enemy("pink", 1, 200, -20, "down", "fast")
    for s in range(0,400):
        if stopwatch == s+13000:
            make_enemy("red", 1, 200, -20, "down", "superfast")
            money += 10
    for s in range(0,100):
        if stopwatch == 30*s+14200:
            make_enemy("yellow", 1, 200, -20, "down", "superfast")
    for s in range(0,150):
        if stopwatch == s+14700:
            make_enemy("pink", 1, 200, -20, "down", "fast")
    for s in range(0,120):
        if stopwatch == s+15700:
            make_enemy("black", 1, 200, -20, "down", "normal")
    for s in range(0,100):
        if stopwatch == s+16700:
            make_enemy("white", 1, 200, -20, "down", "glue")
    if stopwatch == 19500:
        make_enemy("bfb", 100, 200, -20, "down", "normal")
    for s in range(0,10):
        if stopwatch == 20*s+20500:
            make_enemy("moab", 1, 200, -20, "down", "normal")
    if stopwatch == 21500:
        make_enemy("bfb", 20, 200, -20, "down", "fast")
    for s in range(0,20):
        if stopwatch == 50*s+22200:
            make_enemy("moab", 1, 200, -20, "down", "normal")
    for s in range(0,20):
        if stopwatch == 10*s+24000:
            make_enemy("bfb", 1, 200, -20, "down", "normal")
    if stopwatch == 25000:
        make_enemy("moab", 200, 200, -20, "down", "normal")
    if stopwatch == 25500:
        make_enemy("bfb", 200, 200, -20, "down", "glue")
    for s in range(0,50):
        if stopwatch == s+26300:
            make_enemy("white", 1, 200, -20, "down", "superfast")

    if slide == "game":
        for qwqw in range(0, len(bulletx)):
            pygame.draw.rect(screen, (255, 255, 255), (bulletx[qwqw] - 10, bullety[qwqw], 20, 20))
            bullety[qwqw] = bullety[qwqw] - 5
        for zv in range(0, len(bombx)):
            pygame.draw.rect(screen, (0, 0, 0), (bombx[zv] - 10, bomby[zv] - 20, 20, 20))
            bomby[zv] = bomby[zv] - 4
        for err in range(0, len(gluex)):
            pygame.draw.rect(screen, (200,255,30), (gluex[err] - 10, gluey[err], 20, 20))
            gluey[err] = gluey[err] - 5
        for add in range(0, len(stunx)):
            pygame.draw.rect(screen, (20,50,255), (stunx[add] - 10, stuny[add] - 20, 20, 20))
            stuny[add] = stuny[add] - 6
        for ah in range(0, len(gluebombx)):
            pygame.draw.rect(screen, (200,255,30), (gluebombx[ah] - 10, gluebomby[ah] - 20, 20, 20))
            gluebomby[ah] = gluebomby[ah] - 4
        for aj in range(0, len(stunbombx)):
            pygame.draw.rect(screen, (20,50,255), (stunbombx[aj] - 10, stunbomby[aj] - 20, 20, 20))
            stunbomby[aj] = stunbomby[aj] - 7
        for ghgh in range(len(bulletx), 0, -1):
            if bullety[ghgh - 1] < -15:
                del (bulletx[ghgh - 1])
                del (bullety[ghgh - 1])
        for adad in range(len(bombx), 0, -1):
            if bomby[adad - 1] < -15:
                del (bombx[adad - 1])
                del (bomby[adad - 1])
                del (bombdel[adad - 1])
        for aff in range(len(gluey), 0, -1):
            if gluey[aff - 1] < -15:
                del (gluex[aff - 1])
                del (gluey[aff - 1])
        for addd in range(len(stuny), 0, -1):
            if stuny[addd - 1] < -15:
                del (stunx[addd - 1])
                del (stuny[addd - 1])
        for agg in range(len(gluebombx), 0, -1):
            if gluebomby[agg - 1] < -15:
                del (gluebombx[agg - 1])
                del (gluebomby[agg - 1])
                del (gluebombdel[agg - 1])
        for assa in range(len(stunbombx), 0, -1):
            if stunbomby[assa - 1] < -15:
                del (stunbombx[assa - 1])
                del (stunbomby[assa - 1])
                del (stunbombdel[assa - 1])

    for gh in range(0, len(enemyx)):
        if enemystate[gh] == "normal" or enemystate[gh] == "glue" or enemystate[gh] == "gluee" or enemystate[gh] == "glueee" or enemystate[gh] == "fast" or enemystate[gh] == "superfast":
            if enemyx[gh] <= 200 and enemyy[gh] >= 430:
                enemyway[gh] = "right"
            if enemyy[gh] >= 430 and enemyx[gh] >= 500 and enemyx[gh] <= 799:
                enemyway[gh] = "up"
            if enemyy[gh] <= 100 and enemyx[gh] >= 500:
                enemyway[gh] = "right"
            if enemyy[gh] <= 100 and enemyx[gh] >= 800 and enemyx[gh] <= 900:
                enemyway[gh] = "down"
            if enemyy[gh] >= 300 and enemyx[gh] >= 800:
                enemyway[gh] = "left"

    if slide == "upgrades":
        u1 = font.render(str(upgrade1), False, (0, 0, 0))
        screen.blit(u1, (300, 30))
        u2 = font.render(str(upgrade2), False, (0, 0, 0))
        screen.blit(u2, (300, 110))
        u3 = font.render(str(upgrade3), False, (0, 0, 0))
        screen.blit(u3, (300, 190))
        u4 = font.render(str(upgrade4), False, (0, 0, 0))
        screen.blit(u4, (300, 270))
        u5 = font.render(str(upgrade5), False, (0, 0, 0))
        screen.blit(u5, (300, 350))
        u6 = font.render(str(upgrade6), False, (0, 0, 0))
        screen.blit(u6, (300, 430))
        m1 = font.render(str(90*2**upgrade1), False, (0, 0, 0))
        screen.blit(m1, (100, 30))
        m2 = font.render(str(70*2**upgrade2), False, (0, 0, 0))
        screen.blit(m2, (100, 110))
        m3 = font.render(str(60*2**upgrade3), False, (0, 0, 0))
        screen.blit(m3, (100, 190))
        m4 = font.render(str(85*2**upgrade4), False, (0, 0, 0))
        screen.blit(m4, (100, 270))
        m5 = font.render(str(45*2**upgrade5), False, (0, 0, 0))
        screen.blit(m5, (100, 350))
        m6 = font.render(str(50*2**upgrade6), False, (0, 0, 0))
        screen.blit(m6, (100, 430))
        if money >= 90*2**upgrade1:
            pygame.draw.rect(screen, (255, 255, 255), (200, 20, 60, 60))
            if 200<=mousex<=260:
                if 20<=mousey<=80:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        delay1 += 1
        else:
            pygame.draw.rect(screen, (255, 50,50), (200, 20, 60, 60))
        if money >= 70*2**upgrade2:
            pygame.draw.rect(screen, (255, 255, 255), (200, 100, 60, 60))
            if 200<=mousex<=260:
                if 100<=mousey<=160:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        delay2 += 1
        else:
            pygame.draw.rect(screen, (255, 50,50), (200, 100, 60, 60))
        if money >= 60*2**upgrade3:
            pygame.draw.rect(screen, (255, 255, 255), (200, 180, 60, 60))
            if 200<=mousex<=260:
                if 180<=mousey<=240:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        delay3 += 1
        else:
            pygame.draw.rect(screen, (255, 50,50), (200, 180, 60, 60))
        if money >= 85*2**upgrade4:
            pygame.draw.rect(screen, (255, 255, 255), (200, 260, 60, 60))
            if 200<=mousex<=260:
                if 260<=mousey<=340:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        delay4 += 1
        else:
            pygame.draw.rect(screen, (255, 50,50), (200, 260, 60, 60))
        if money >= 45*2**upgrade5:
            pygame.draw.rect(screen, (255, 255, 255), (200, 340, 60, 60))
            if 200<=mousex<=260:
                if 360<=mousey<=420:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        delay5 += 1
        else:
            pygame.draw.rect(screen, (255, 50,50), (200, 340, 60, 60))
        if money >= 50*2**upgrade6:
            pygame.draw.rect(screen, (255, 255, 255), (200, 420, 60, 60))
            if 200<=mousex<=260:
                if 440<=mousey<=500:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        delay6 += 1
        else:
            pygame.draw.rect(screen, (255, 50,50), (200, 420, 60, 60))

    for hh in range(0, len(enemyx)):
        if enemyx[hh] <= -30:
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

    if slide == "game":
        for g in range(0, len(enemyx)):
            if enemystate[g] == "normal":
                if enemyway[g] == "down":
                    enemyy[g] += 4
                if enemyway[g] == "up":
                    enemyy[g] -= 4
                if enemyway[g] == "right":
                    enemyx[g] += 4
                if enemyway[g] == "left":
                    enemyx[g] -= 4
            if enemystate[g] == "fast":
                if enemyway[g] == "down":
                    enemyy[g] += 8
                if enemyway[g] == "up":
                    enemyy[g] -= 8
                if enemyway[g] == "right":
                    enemyx[g] += 8
                if enemyway[g] == "left":
                    enemyx[g] -= 8
            if enemystate[g] == "superfast":
                if enemyway[g] == "down":
                    enemyy[g] += 20
                if enemyway[g] == "up":
                    enemyy[g] -= 20
                if enemyway[g] == "right":
                    enemyx[g] += 20
                if enemyway[g] == "left":
                    enemyx[g] -= 20
            if enemystate[g] == "glue":
                if enemyway[g] == "down":
                    enemyy[g] += 3
                if enemyway[g] == "up":
                    enemyy[g] -= 3
                if enemyway[g] == "right":
                    enemyx[g] += 3
                if enemyway[g] == "left":
                    enemyx[g] -= 3
            if enemystate[g] == "gluee":
                if enemyway[g] == "down":
                    enemyy[g] += 2
                if enemyway[g] == "up":
                    enemyy[g] -= 2
                if enemyway[g] == "right":
                    enemyx[g] += 2
                if enemyway[g] == "left":
                    enemyx[g] -= 2
            if enemystate[g] == "glueee":
                if enemyway[g] == "down":
                    enemyy[g] += 1
                if enemyway[g] == "up":
                    enemyy[g] -= 1
                if enemyway[g] == "right":
                    enemyx[g] += 1
                if enemyway[g] == "left":
                    enemyx[g] -= 1
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

    if upgrade3 >= 1:
        for qwe in range(len(enemyx) - 1, -1, -1):
            for qwer in range(len(bulletx) - 1, -1, -1):
                if abs(bulletx[qwer] - enemyx[qwe]) < 21:
                    if abs(bullety[qwer] - enemyy[qwe]) < 21:
                        enemyhealth[qwe] -= 1
                        bullethealth[qwer]-= 1
                        if bullethealth[qwer]<= 0:
                            del bulletx[qwer]
                            del bullety[qwer]
                            del bullethealth[qwer]
                        if enemyhealth[qwe] <= 0:
                            money += 1
                            if enemyrank[qwe] == "red":
                                delete_enemy(qwe)
                                break
                            if enemyrank[qwe] == "blue":
                                make_enemy("red", int(enemyorig[qwe]/2 + 1), enemyx[qwe], enemyy[qwe], enemyway[qwe], enemystate[qwe])
                                delete_enemy(qwe)
                                break
                            if enemyrank[qwe] == "green":
                                make_enemy("blue", int(enemyorig[qwe] / 2 + 1), enemyx[qwe], enemyy[qwe], enemyway[qwe], enemystate[qwe])
                                delete_enemy(qwe)
                                break
                            if enemyrank[qwe] == "yellow":
                                make_enemy("green", int(enemyorig[qwe] / 2 + 1), enemyx[qwe], enemyy[qwe], enemyway[qwe], enemystate[qwe])
                                delete_enemy(qwe)
                                break
                            if enemyrank[qwe] == "pink":
                                if enemyway[qwe] == "right" or enemyway[qwe] == "left":
                                    make_enemy("yellow", int(enemyorig[qwe] / 2 + 1), enemyx[qwe]-10, enemyy[qwe],
                                               enemyway[qwe], enemystate[qwe])
                                    make_enemy("yellow", int(enemyorig[qwe] / 2 + 1), enemyx[qwe]+10, enemyy[qwe],
                                               enemyway[qwe], enemystate[qwe])
                                if enemyway[qwe] == "up" or enemyway[qwe] == "down":
                                    make_enemy("yellow", int(enemyorig[qwe] / 2 + 1), enemyx[qwe], enemyy[qwe]-10,
                                               enemyway[qwe], enemystate[qwe])
                                    make_enemy("yellow", int(enemyorig[qwe] / 2 + 1), enemyx[qwe], enemyy[qwe]+10,
                                               enemyway[qwe], enemystate[qwe])
                                delete_enemy(qwe)
                                break
                            if enemyrank[qwe] == "black":
                                if enemyway[qwe] == "right" or enemyway[qwe] == "left":
                                    make_enemy("pink", int(enemyorig[qwe] / 2 + 1), enemyx[qwe]-10, enemyy[qwe],
                                               enemyway[qwe], enemystate[qwe])
                                    make_enemy("pink", int(enemyorig[qwe] / 2 + 1), enemyx[qwe]+10, enemyy[qwe],
                                               enemyway[qwe], enemystate[qwe])
                                if enemyway[qwe] == "up" or enemyway[qwe] == "down":
                                    make_enemy("pink", int(enemyorig[qwe] / 2 + 1), enemyx[qwe], enemyy[qwe]-10,
                                               enemyway[qwe], enemystate[qwe])
                                    make_enemy("pink", int(enemyorig[qwe] / 2 + 1), enemyx[qwe], enemyy[qwe]+10,
                                               enemyway[qwe], enemystate[qwe])
                                delete_enemy(qwe)
                                break
                            if enemyrank[qwe] == "white":
                                if enemyway[qwe] == "right" or enemyway[qwe] == "left":
                                    make_enemy("black", int(enemyorig[qwe] / 2 + 1), enemyx[qwe]-10, enemyy[qwe],
                                               enemyway[qwe], enemystate[qwe])
                                    make_enemy("black", int(enemyorig[qwe] / 2 + 1), enemyx[qwe]+10, enemyy[qwe],
                                               enemyway[qwe], enemystate[qwe])
                                if enemyway[qwe] == "up" or enemyway[qwe] == "down":
                                    make_enemy("black", int(enemyorig[qwe] / 2 + 1), enemyx[qwe], enemyy[qwe]-10,
                                               enemyway[qwe], enemystate[qwe])
                                    make_enemy("black", int(enemyorig[qwe] / 2 + 1), enemyx[qwe], enemyy[qwe]+10,
                                               enemyway[qwe], enemystate[qwe])
                                delete_enemy(qwe)
                                break
                            if enemyrank[qwe] == "moab":
                                if enemyway[qwe] == "right" or enemyway[qwe] == "left":
                                    make_enemy("white", int(enemyorig[qwe] / 2 + 1), enemyx[qwe]-10, enemyy[qwe],
                                               enemyway[qwe], enemystate[qwe])
                                    make_enemy("white", int(enemyorig[qwe] / 2 + 1), enemyx[qwe]+10, enemyy[qwe],
                                               enemyway[qwe], enemystate[qwe])
                                    make_enemy("white", int(enemyorig[qwe] / 2 + 1), enemyx[qwe] - 30, enemyy[qwe],
                                               enemyway[qwe], enemystate[qwe])
                                    make_enemy("white", int(enemyorig[qwe] / 2 + 1), enemyx[qwe] + 30, enemyy[qwe],
                                               enemyway[qwe], enemystate[qwe])
                                if enemyway[qwe] == "up" or enemyway[qwe] == "down":
                                    make_enemy("white", int(enemyorig[qwe] / 2 + 1), enemyx[qwe], enemyy[qwe]-10,
                                               enemyway[qwe], enemystate[qwe])
                                    make_enemy("white", int(enemyorig[qwe] / 2 + 1), enemyx[qwe], enemyy[qwe]+10,
                                               enemyway[qwe], enemystate[qwe])
                                    make_enemy("white", int(enemyorig[qwe] / 2 + 1), enemyx[qwe], enemyy[qwe]+30,
                                               enemyway[qwe], enemystate[qwe])
                                    make_enemy("white", int(enemyorig[qwe] / 2 + 1), enemyx[qwe], enemyy[qwe]-30,
                                               enemyway[qwe], enemystate[qwe])
                                delete_enemy(qwe)
                                break
                            if enemyrank[qwe] == "bfb":
                                if enemyway[qwe] == "right" or enemyway[qwe] == "left":
                                    make_enemy("moab", int(enemyorig[qwe] / 2 + 1), enemyx[qwe]-10, enemyy[qwe],
                                               enemyway[qwe], enemystate[qwe])
                                    make_enemy("moab", int(enemyorig[qwe] / 2 + 1), enemyx[qwe]+10, enemyy[qwe],
                                               enemyway[qwe], enemystate[qwe])
                                    make_enemy("moab", int(enemyorig[qwe] / 2 + 1), enemyx[qwe] - 30, enemyy[qwe],
                                               enemyway[qwe], enemystate[qwe])
                                    make_enemy("moab", int(enemyorig[qwe] / 2 + 1), enemyx[qwe] + 30, enemyy[qwe],
                                               enemyway[qwe], enemystate[qwe])
                                if enemyway[qwe] == "up" or enemyway[qwe] == "down":
                                    make_enemy("moab", int(enemyorig[qwe] / 2 + 1), enemyx[qwe], enemyy[qwe]-10,
                                               enemyway[qwe], enemystate[qwe])
                                    make_enemy("moab", int(enemyorig[qwe] / 2 + 1), enemyx[qwe], enemyy[qwe]+10,
                                               enemyway[qwe], enemystate[qwe])
                                    make_enemy("moab", int(enemyorig[qwe] / 2 + 1), enemyx[qwe], enemyy[qwe]+30,
                                               enemyway[qwe], enemystate[qwe])
                                    make_enemy("moab", int(enemyorig[qwe] / 2 + 1), enemyx[qwe], enemyy[qwe]-30,
                                               enemyway[qwe], enemystate[qwe])
                                delete_enemy(qwe)
                                break
                        break

    for af in range(len(enemyx) - 1, -1, -1):
        for ag in range(len(bombx) - 1, -1, -1):
            if upgrade4 == 1:
                if abs(bombx[ag] - enemyx[af]) < 21:
                    if abs(bomby[ag] - enemyy[af]) < 21:
                        enemyhealth[af] -= 1
                        bombdel[ag] = "yes"
                        pygame.draw.circle(screen, (255, 50, 50), (bombx[ag], bomby[ag]), 25)
            if upgrade4 == 2:
                if abs(bombx[ag] - enemyx[af]) < 31:
                    if abs(bomby[ag] - enemyy[af]) < 31:
                        enemyhealth[af] -= 1
                        bombdel[ag] = "yes"
                        pygame.draw.circle(screen, (255, 50, 50), (bombx[ag], bomby[ag]), 35)
            if upgrade4 >= 3 and upgrade4 <= 6:
                if abs(bombx[ag] - enemyx[af]) < 46:
                    if abs(bomby[ag] - enemyy[af]) < 46:
                        enemyhealth[af] -= 1
                        bombdel[ag] = "yes"
                        pygame.draw.circle(screen, (255, 50, 50), (bombx[ag], bomby[ag]), 50)
            if upgrade4 == 7 or upgrade4 == 8:
                if abs(bombx[ag] - enemyx[af]) < 66:
                    if abs(bomby[ag] - enemyy[af]) < 66:
                        enemyhealth[af] -= 1
                        bombdel[ag] = "yes"
                        pygame.draw.circle(screen, (255,50,50), (bombx[ag], bomby[ag]), 70)
            if upgrade4 == 9:
                if abs(bombx[ag] - enemyx[af]) < 66:
                    if abs(bomby[ag] - enemyy[af]) < 66:
                        enemyhealth[af] -= 1
                        pygame.draw.circle(screen, (255,50,50), (bombx[ag], bomby[ag]), 70)
                        if enemyrank[af] == "moab" or enemyrank[af] == "bfb":
                            enemyhealth[af] -= 9
            if enemyhealth[af] <= 0:
                money += 1
                if enemyrank[af] == "red":
                    delete_enemy(af)
                    break
                if enemyrank[af] == "blue":
                    make_enemy("red", int(enemyorig[af] / 2 + 1), enemyx[af], enemyy[af], enemyway[af],
                               enemystate[af])
                    delete_enemy(af)
                    break
                if enemyrank[af] == "green":
                    make_enemy("blue", int(enemyorig[af] / 2 + 1), enemyx[af], enemyy[af], enemyway[af],
                               enemystate[af])
                    delete_enemy(af)
                    break
                if enemyrank[af] == "yellow":
                    make_enemy("green", int(enemyorig[af] / 2 + 1), enemyx[af], enemyy[af], enemyway[af],
                               enemystate[af])
                    delete_enemy(af)
                    break
                if enemyrank[af] == "pink":
                    if enemyway[af] == "right" or enemyway[af] == "left":
                        make_enemy("yellow", int(enemyorig[af] / 2 + 1), enemyx[af] - 10, enemyy[af],
                                   enemyway[af], enemystate[af])
                        make_enemy("yellow", int(enemyorig[af] / 2 + 1), enemyx[af] + 10, enemyy[af],
                                   enemyway[af], enemystate[af])
                    if enemyway[af] == "up" or enemyway[af] == "down":
                        make_enemy("yellow", int(enemyorig[af] / 2 + 1), enemyx[af], enemyy[af] - 10,
                                   enemyway[af], enemystate[af])
                        make_enemy("yellow", int(enemyorig[af] / 2 + 1), enemyx[af], enemyy[af] + 10,
                                   enemyway[af], enemystate[af])
                    delete_enemy(af)
                    break
                if enemyrank[af] == "black":
                    if enemyway[af] == "right" or enemyway[af] == "left":
                        make_enemy("pink", int(enemyorig[af] / 2 + 1), enemyx[af] - 10, enemyy[af],
                                   enemyway[af], enemystate[af])
                        make_enemy("pink", int(enemyorig[af] / 2 + 1), enemyx[af] + 10, enemyy[af],
                                   enemyway[af], enemystate[af])
                    if enemyway[af] == "up" or enemyway[af] == "down":
                        make_enemy("pink", int(enemyorig[af] / 2 + 1), enemyx[af], enemyy[af] - 10,
                                   enemyway[af], enemystate[af])
                        make_enemy("pink", int(enemyorig[af] / 2 + 1), enemyx[af], enemyy[af] + 10,
                                   enemyway[af], enemystate[af])
                    delete_enemy(af)
                    break
                if enemyrank[af] == "white":
                    if enemyway[af] == "right" or enemyway[af] == "left":
                        make_enemy("black", int(enemyorig[af] / 2 + 1), enemyx[af] - 10, enemyy[af],
                                   enemyway[af], enemystate[af])
                        make_enemy("black", int(enemyorig[af] / 2 + 1), enemyx[af] + 10, enemyy[af],
                                   enemyway[af], enemystate[af])
                    if enemyway[af] == "up" or enemyway[af] == "down":
                        make_enemy("black", int(enemyorig[af] / 2 + 1), enemyx[af], enemyy[af] - 10,
                                   enemyway[af], enemystate[af])
                        make_enemy("black", int(enemyorig[af] / 2 + 1), enemyx[af], enemyy[af] + 10,
                                   enemyway[af], enemystate[af])
                    delete_enemy(af)
                    break
                if enemyrank[af] == "moab":
                    if enemyway[af] == "right" or enemyway[af] == "left":
                        make_enemy("white", int(enemyorig[af] / 2 + 1), enemyx[af] - 10, enemyy[af],
                                   enemyway[af], enemystate[af])
                        make_enemy("white", int(enemyorig[af] / 2 + 1), enemyx[af] + 10, enemyy[af],
                                   enemyway[af], enemystate[af])
                        make_enemy("white", int(enemyorig[af] / 2 + 1), enemyx[af] - 30, enemyy[af],
                                   enemyway[af], enemystate[af])
                        make_enemy("white", int(enemyorig[af] / 2 + 1), enemyx[af] + 30, enemyy[af],
                                   enemyway[af], enemystate[af])
                    if enemyway[af] == "up" or enemyway[af] == "down":
                        make_enemy("white", int(enemyorig[af] / 2 + 1), enemyx[af], enemyy[af] - 10,
                                   enemyway[af], enemystate[af])
                        make_enemy("white", int(enemyorig[af] / 2 + 1), enemyx[af], enemyy[af] + 10,
                                   enemyway[af], enemystate[af])
                        make_enemy("white", int(enemyorig[af] / 2 + 1), enemyx[af], enemyy[af] + 30,
                                   enemyway[af], enemystate[af])
                        make_enemy("white", int(enemyorig[af] / 2 + 1), enemyx[af], enemyy[af] - 30,
                                   enemyway[af], enemystate[af])
                    delete_enemy(af)
                    break
                if enemyrank[af] == "bfb":
                    if enemyway[af] == "right" or enemyway[af] == "left":
                        make_enemy("moab", int(enemyorig[af] / 2 + 1), enemyx[af] - 10, enemyy[af],
                                   enemyway[af], enemystate[af])
                        make_enemy("moab", int(enemyorig[af] / 2 + 1), enemyx[af] + 10, enemyy[af],
                                   enemyway[af], enemystate[af])
                        make_enemy("moab", int(enemyorig[af] / 2 + 1), enemyx[af] - 30, enemyy[af],
                                   enemyway[af], enemystate[af])
                        make_enemy("moab", int(enemyorig[af] / 2 + 1), enemyx[af] + 30, enemyy[af],
                                   enemyway[af], enemystate[af])
                    if enemyway[af] == "up" or enemyway[af] == "down":
                        make_enemy("moab", int(enemyorig[af] / 2 + 1), enemyx[af], enemyy[af] - 10,
                                   enemyway[af], enemystate[af])
                        make_enemy("moab", int(enemyorig[af] / 2 + 1), enemyx[af], enemyy[af] + 10,
                                   enemyway[af], enemystate[af])
                        make_enemy("moab", int(enemyorig[af] / 2 + 1), enemyx[af], enemyy[af] + 30,
                                   enemyway[af], enemystate[af])
                        make_enemy("moab", int(enemyorig[af] / 2 + 1), enemyx[af], enemyy[af] - 30,
                                   enemyway[af], enemystate[af])
                    delete_enemy(af)
                    break
            break

    if upgrade5 >= 1:
        for ahh in range(len(enemyx) - 1, -1, -1):
            for ajj in range(len(gluex) - 1, -1, -1):
                if abs(gluex[ajj] - enemyx[ahh]) < 21:
                    if abs(gluey[ajj] - enemyy[ahh]) < 21:
                        if upgrade5 <= 3:
                            enemystate[ahh] = "glue"
                            if enemyrank[ahh] == "moab":
                                enemystate[ahh] = "normal"
                            if enemyrank[ahh] == "bfb":
                                enemystate = "normal"
                        elif upgrade5 <= 6:
                            enemystate[ahh] = "gluee"
                            if enemyrank[ahh] == "moab":
                                enemystate[ahh] = "glue"
                            if enemyrank[ahh] == "bfb":
                                enemystate[ahh] = "normal"
                        elif upgrade5 <= 8:
                            enemystate[ahh] = "glueee"
                            if enemyrank[ahh] == "moab":
                                enemystate[ahh] = "gluee"
                            if enemyrank[ahh] == "bfb":
                                enemystate[ahh] = "glue"
                        del gluex[ajj]
                        del gluey[ajj]
                        break

    if upgrade6 >= 1 and upgrade6 <= 3:
        for asd in range(len(enemyx) - 1, -1, -1):
            for asdf in range(len(stunx) - 1, -1, -1):
                if abs(stunx[asdf] - enemyx[asd]) < 21:
                    if abs(stuny[asdf] - enemyy[asd]) < 21:
                        enemystate[asd] = "stunned"
                        if upgrade6 <= 2:
                            stuntimer[asd] = 100
                            if enemyrank[asd] == "moab":
                                stuntimer[asd] = 20
                            if enemyrank[asd] == "bfb":
                                stuntimer[asd] = 0
                        if upgrade6 == 3:
                            stuntimer[asd] = 200
                            if enemyrank[asd] == "moab":
                                stuntimer[asd] = 60
                            if enemyrank[asd] == "bfb":
                                stuntimer[asd] = 20
                        del stunx[asdf]
                        del stuny[asdf]
                        break

    for vbb in range(len(enemyx) - 1, -1, -1):
        for vnn in range(len(gluebombx) - 1, -1, -1):
            if abs(gluebombx[vnn] - enemyx[vbb]) < 31:
                if abs(gluebomby[vnn] - enemyy[vbb]) < 31:
                    gluebombdel[vnn] = "yes"
                    enemystate[vbb] = "glueee"
                    if enemyrank[vbb] == "moab":
                        enemystate[vbb] = "gluee"
                    if enemyrank[vbb] == "bfb":
                        enemystate[vbb] = "glue"
                    pygame.draw.circle(screen, (200,255,50), (gluebombx[vnn], gluebomby[vnn]), 35)

    for vv in range(len(enemyx) - 1, -1, -1):
        for vvv in range(len(stunbombx) - 1, -1, -1):
            if upgrade6 == 4 or upgrade6 == 5:
                if abs(stunbombx[vvv] - enemyx[vv]) < 28:
                    if abs(stunbomby[vvv] - enemyy[vv]) < 28:
                        enemystate[vv] = "stunned"
                        stuntimer[vv] = 200
                        if enemyrank == "moab":
                            stuntimer[vv] = 60
                        if enemyrank == "bfb":
                            stuntimer[vv] = 20
                        stunbombdel[vvv] = "yes"
                        pygame.draw.circle(screen, (50,50,255), (stunbombx[vvv], stunbomby[vvv]), 34)
            if upgrade6 == 6 or upgrade6 == 7:
                if abs(stunbombx[vvv] - enemyx[vv]) < 36:
                    if abs(stunbomby[vvv] - enemyy[vv]) < 36:
                        enemystate[vv] = "stunned"
                        if upgrade6 == 6:
                            stuntimer[vv] = 200
                            if enemyrank == "moab":
                                stuntimer[vv] = 60
                            if enemyrank == "bfb":
                                stuntimer[vv] = 20
                        if upgrade6 == 7:
                            stuntimer[vv] = 300
                            if enemyrank[vv] == "moab":
                                stuntimer[vv] = 150
                            if enemyrank[vv] == "bfb":
                                stuntimer[vv] = 50
                        stunbombdel[vvv] = "yes"
                        pygame.draw.circle(screen, (50,50,255), (stunbombx[vvv], stunbomby[vvv]), 42)
            if upgrade6 == 8 or upgrade6 == 9:
                if abs(stunbombx[vvv] - enemyx[vv]) < 46:
                    if abs(stunbomby[vvv] - enemyy[vv]) < 46:
                        enemystate[vv] = "stunned"
                        stuntimer[vv] = 300
                        if enemyrank[vv] == "moab":
                            stuntimer[vv] = 150
                        if enemyrank[vv] == "bfb":
                            stuntimer[vv] = 50
                        stunbombdel[vvv] = "yes"
                        pygame.draw.circle(screen, (50,50,255), (stunbombx[vvv], stunbomby[vvv]), 54)

    for dd in range(len(bombdel) - 1, -1, -1):
        if bombdel[dd] == "yes":
            del (bombdel[dd])
            del (bombx[dd])
            del (bomby[dd])
    for ddd in range(len(gluebombdel) - 1, -1, -1):
        if gluebombdel[ddd] == "yes":
            del (gluebombdel[ddd])
            del (gluebombx[ddd])
            del (gluebomby[ddd])
    for dddd in range(len(stunbombdel) - 1, -1, -1):
        if stunbombdel[dddd] == "yes":
            del (stunbombdel[dddd])
            del (stunbombx[dddd])
            del (stunbomby[dddd])

    pygame.draw.rect(screen, (255, 255, 255), (mousex - 20, mousey - 30, 40, 60))
    live = font.render(str(lives), False, (0, 0, 0))
    screen.blit(live, (500, 20))
    moneys = font.render(str(money), False, (0, 0, 0))
    screen.blit(moneys, (800, 20))

    for stunt in range(0,len(stuntimer)):
        if enemystate[stunt] == "stunned":
            stuntimer[stunt] -= 1
            if stuntimer[stunt]<= 0:
                stuntimer[stunt] = 0
                enemystate[stunt] = "normal"

    if lives <= 0:
        money = 2000

        upgrade1 = 0
        upgrade2 = 0
        upgrade3 = 0
        upgrade4 = 0
        upgrade5 = 0
        upgrade6 = 0

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
            slide = "game"
        stopwach = font.render(str(stopwatch), False, (0, 0, 0))
        screen.blit(stopwach, (510, 260))

    if delay1 >= 7:
        money -= 90 * 2 ** upgrade1
        upgrade1 += 1
        delay1 = 0
    if delay2 >= 7:
        money -= 70 * 2 ** upgrade2
        upgrade2 += 1
        delay2 = 0
    if delay3 >= 7:
        money -= 60 * 2 ** upgrade3
        upgrade3 += 1
        delay3 = 0
    if delay4 >= 7:
        money -= 85 * 2 ** upgrade4
        upgrade4 += 1
        delay4 = 0
    if delay5 >= 7:
        money -= 45 * 2 ** upgrade5
        upgrade5 += 1
        delay5 = 0
    if delay6 >= 7:
        money -= 50 * 2 ** upgrade6
        upgrade6 += 1
        delay6 = 0

    pygame.display.flip()
    clock.tick(70)