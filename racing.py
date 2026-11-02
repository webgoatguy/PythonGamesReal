import pygame
import math
import sys
import random
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1000,500))
stopwatch = 0

starting = 0

carx = 0
cary = 0
carxx = 0
caryy = 0

screenx = -500
screeny = 250

mousedown = False

drift = 0
#max: 100
speed = 50

maxspeed = speed

mousexx = 0
mouseyy = 0

x = []
y = []
xx = []
yy = []
px = []
py = []
pxx = []
pyy = []
cx = []
cy = []
cxx = []
cyy = []
cd = []

stuf = [0, 0, 0, 0, 0]

bruh = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    mousex, mousey = pygame.mouse.get_pos()

    if stopwatch == 0:
        x.append(-100)
        y.append(-100)
        x.append(-100)
        y.append(-100)
        x.append(-100)
        y.append(100)
        xx.append(25)
        yy.append(225)
        xx.append(1400)
        xx.append(1000)
        yy.append(25)
        yy.append(25)
        for cat in range(0, 10):
            xx.append(25)
            yy.append(100)
            xx.append(25)
            yy.append(100)
            x.append(1300 - 50*cat)
            y.append(-100 + 50*cat)
            x.append(875 - 50 * cat)
            y.append(100 + 50 * cat)
            xx.append(25)
            yy.append(100)
            xx.append(25)
            yy.append(100)
            x.append(2300 - 50 * cat)
            y.append(-100 + 50 * cat)
            x.append(2475 - 50 * cat)
            y.append(100 + 50 * cat)
            xx.append(100)
            yy.append(25)
            xx.append(100)
            yy.append(25)
            x.append(1300 - 50 * cat)
            y.append(-100 + 50 * cat)
            x.append(875 - 50 * cat)
            y.append(100 + 50 * cat)
            xx.append(100)
            yy.append(25)
            xx.append(100)
            yy.append(25)
            x.append(2300 - 50 * cat)
            y.append(-100 + 50 * cat)
            x.append(2475 - 50 * cat)
            y.append(100 + 50 * cat)
        xx.append(25)
        xx.append(25)
        yy.append(225)
        yy.append(225)
        x.append(400)
        x.append(2000)
        y.append(600)
        y.append(600)
        xx.append(1000)
        xx.append(2625)
        yy.append(25)
        yy.append(25)
        x.append(850)
        x.append(-600)
        y.append(400)
        y.append(800)
        for cat in range(0, 20):
            xx.append(25)
            yy.append(300)
            x.append(875 + cat * 50)
            y.append(random.randint(0, 1) * 100 + 425)
        x.append(2375)
        y.append(-2275)
        xx.append(25)
        yy.append(2200)
        x.append(2975)
        y.append(-2075)
        xx.append(50)
        yy.append(2250)
        x.append(2550)
        y.append(100)
        xx.append(500)
        yy.append(25)
        for cat in range(0, 11):
            x.append(2400)
            y.append(-2200 + 200*cat)
            xx.append(200)
            yy.append(60)
            x.append(2575)
            y.append(-2200 + 200 * cat)
            xx.append(25)
            yy.append(75)
        for cat in range(0, 5):
            x.append(random.randint(0, 3) * 200 + 2400)
            y.append(-2200 + 450 * cat)
            xx.append(200)
            yy.append(25)
            x.append(random.randint(0, 3) * 200 + 2575)
            y.append(-2200 + 450 * cat)
            xx.append(50)
            yy.append(150)
        x.append(2375)
        y.append(-2275)
        xx.append(1025)
        yy.append(25)
        x.append(3375)
        y.append(-2275)
        xx.append(25)
        yy.append(2475)
        for cat in range(0, 25):
            thing3 = random.randint(1, 18)
            if thing3 < 4:
                px.append(3025)
            if thing3 > 15:
                px.append(3350)
            if 3 < thing3 < 16:
                px.append((thing3 - 2) * 25 + 3000)
            py.append(random.randint(1, 50)*40 - 2200)
            pxx.append(25)
            pyy.append(25)
        cx.append(3000)
        cy.append(0)
        cxx.append(400)
        cyy.append(25)
        cd.append(0)
        for cat in range(0, 20):
            px.append(2800-cat*25)
            py.append(600)
            pxx.append(25)
            pyy.append(25)
        for cat in range(0, 20):
            px.append(2800+cat*25)
            py.append(600)
            pxx.append(25)
            pyy.append(25)
        xx.append(25)
        yy.append(1000)
        x.append(3300)
        y.append(175)
        xx.append(4200)
        yy.append(25)
        x.append(-800)
        y.append(1100)
        xx.append(100)
        yy.append(25)
        x.append(3300)
        y.append(175)
        px.append(-575)
        py.append(825)
        pxx.append(2500)
        pyy.append(200)
        cxx.append(25)
        cyy.append(300)
        cx.append(-600)
        cy.append(800)
        cd.append(0)
        for cat in range(0, 12):
            pxx.append(25)
            pyy.append(800)
            px.append(-3000 + cat * 200)
            py.append(random.randint(0, 1) * 200 + 100)
            if cat == 11:
                pxx.append(25)
                pyy.append(675)
                #bookmark 1
                #700
                px.append(-3000 + cat * 200 + 200)
                py.append(100)
        px.append(-3000)
        py.append(100)
        pxx.append(2400)
        pyy.append(25)
        px.append(-3000)
        py.append(1100)
        pxx.append(2400)
        pyy.append(25)

    if (stopwatch / 45) % 1 == 0:
        if bruh == 0:
            bruh = 1
        elif bruh == 1:
            bruh = 2
        elif bruh == 2:
            bruh = 3
        elif bruh == 3:
            bruh = 0

    if bruh == 0:
        py[65] = 825
    if bruh == 1 or bruh == 3:
        py[65] = -10000
    if bruh == 2:
        py[65] = 900

    for cat in range(0, 20):
        if px[25+cat] == 2800 - cat*25 and py[25+cat] != 600 - cat*25:
            py[25+cat] -= cat*5/2
        if px[25+cat] == 2800 + cat*25 and py[25+cat] != 600 + cat*25:
            py[25+cat] += cat*5/2
        if py[25+cat] == 600 - cat*25 and px[25+cat] != 2800 + cat*25:
            px[25+cat] += cat*5/2
        if py[25+cat] == 600 + cat*25 and px[25+cat] != 2800 - cat*25:
            px[25+cat] -= cat*5/2
    for cat in range(0, 20):
        if px[45+cat] == 2800 - cat*25 and py[45+cat] != 600 + cat*25:
            py[45+cat] += cat/2
        if px[45+cat] == 2800 + cat*25 and py[45+cat] != 600 - cat*25:
            py[45+cat] -= cat/2
        if py[45+cat] == 600 - cat*25 and px[45+cat] != 2800 - cat*25:
            px[45+cat] -= cat/2
        if py[45+cat] == 600 + cat*25 and px[45+cat] != 2800 + cat*25:
            px[45+cat] += cat/2

    for cat in range(0, 11):
        y[cat*2+110] += 20
        y[cat * 2 + 111] += 20
        if y[cat*2+110] >= -100:
            y[cat*2+110] = -2250
            y[cat * 2 + 111] = -2250

    for cat in range(0, 5):
        x[cat*2+132] -= 12
        x[cat * 2 + 133] -= 12
        if x[cat*2+132] <= 2250:
            x[cat*2+132] = 2800
            x[cat*2+133] = 2975

    if mousex == mousexx and mousey == mouseyy:
        maxspeed += 0.3
    else:
        if maxspeed > speed:
            maxspeed -= 0.75
    if maxspeed < speed:
        maxspeed = speed
    if maxspeed > speed*2:
        maxspeed = speed*2

    screen.fill((50, 50, 50))

    pygame.draw.rect(screen, (200, 200, 200), (0, 0, starting*10, 500))

    if event.type == pygame.MOUSEBUTTONDOWN:
        mousedown = True
    if event.type == pygame.MOUSEBUTTONUP:
        mousedown = False

    stopwatch += 1

    starting -= 1

    if starting > 0:
        carx = 0
        cary = 0
        carxx = 0
        caryy = 0
        for dog in range(0, len(cx)):
            if cd[dog] == 1:
                carx = cx[dog] + cxx[dog] / 2
                cary = cy[dog] + cyy[dog] / 2
                carxx = 0
                caryy = 0

    screenx = carx - 500
    screeny = cary - 250

    for dog in range(0, 10):
        carx += carxx/10
        cary += caryy/10
        for cat in range(0, len(x)):
            if x[cat] - 500 <= carx <= x[cat] + xx[cat] + 500 and y[cat] - 250 <= cary <= y[cat] + yy[cat] + 250:
                pygame.draw.rect(screen, (255, 255, 255), (x[cat] - screenx, y[cat] - screeny, xx[cat], yy[cat]))
                if x[cat] <= carx <= x[cat] + xx[cat] and y[cat] <= cary <= y[cat] + yy[cat]:
                    carxx = round(0.97 * carxx, 3)
                    caryy = round(0.97 * caryy, 3)
                    if carx >= x[cat] + xx[cat] / 2 and cary >= y[cat] + yy[cat] / 2:
                        if abs(carx - x[cat] - xx[cat]) <= abs(cary - y[cat] - yy[cat]):
                            carx = x[cat] + xx[cat]
                        else:
                            cary = y[cat] + yy[cat]
                    if carx >= x[cat] + xx[cat] / 2 and cary <= y[cat] + yy[cat] / 2:
                        if abs(carx - x[cat] - xx[cat]) <= abs(cary - y[cat] - yy[cat]):
                            carx = x[cat] + xx[cat]
                        else:
                            cary = y[cat]
                    if carx <= x[cat] + xx[cat] / 2 and cary <= y[cat] + yy[cat] / 2:
                        if abs(carx - x[cat] - xx[cat]) <= abs(cary - y[cat] - yy[cat]):
                            carx = x[cat]
                        else:
                            cary = y[cat]
                    if carx <= x[cat] + xx[cat] / 2 and cary >= y[cat] + yy[cat] / 2:
                        if abs(carx - x[cat] - xx[cat]) <= abs(cary - y[cat] - yy[cat]):
                            carx = x[cat]
                        else:
                            cary = y[cat] + yy[cat]
        for cat in range(0, len(px)):
            if px[cat] - 500 <= carx <= px[cat] + pxx[cat] + 500 and py[cat] - 250 <= cary <= py[cat] + pyy[cat] + 250:
                pygame.draw.rect(screen, (255, 0, 0), (px[cat] - screenx, py[cat] - screeny, pxx[cat], pyy[cat]))
                if px[cat] <= carx <= px[cat] + pxx[cat] and py[cat] <= cary <= py[cat] + pyy[cat]:
                    carx = 0
                    cary = 0
                    carxx = 0
                    caryy = 0
                    starting = 100
                    for dog in range(0, len(cx)):
                        if cd[dog] == 1:
                            carx = cx[dog] + cxx[dog]/2
                            cary = cy[dog] + cyy[dog]/2
                            carxx = 0
                            caryy = 0
        for cat in range(0, len(cx)):
            if cx[cat] - 500 <= carx <= cx[cat] + cxx[cat] + 500 and cy[cat] - 250 <= cary <= cy[cat] + cyy[cat] + 250:
                pygame.draw.rect(screen, (0, 255, 0), (cx[cat] - screenx, cy[cat] - screeny, cxx[cat], cyy[cat]))
                if cx[cat] <= carx <= cx[cat] + cxx[cat] and cy[cat] <= cary <= cy[cat] + cyy[cat]:
                    cd[cat] = 1

    if mousex == 500 and mousey == 250:
        mousex = 501

    thing2 = math.sqrt((mousex - 500)**2 + (mousey - 250)**2)/100
    thing = math.sqrt(((mousex - carx)/thing2)**2 + ((mousey - cary)/thing2)**2)/5

    while carxx**2 + caryy**2 > maxspeed*2:
        carxx = round(0.98*carxx, 3)
        caryy = round(0.98 * caryy, 3)
    if mousedown == True:
        carxx += round(((mousex - carx + screenx) / thing2) * 15) / (1000 + drift * 100)
        caryy += round(((mousey - cary + screeny) / thing2) * 15) / (1000 + drift * 100)
        carxx = round((1.048 - math.sqrt(drift)/250) * carxx, 3)
        caryy = round((1.048 - math.sqrt(drift)/250) * caryy, 3)
    else:
        carxx = round((0.97 + math.sqrt(drift)/400) * carxx, 3)
        caryy = round((0.97 + math.sqrt(drift)/400) * caryy, 3)
    thing2 = math.sqrt((mousex - 500)**2 + (mousey - 250)**2)/5
    thing = math.sqrt(((mousex - carx)/thing2)**2 + ((mousey - cary)/thing2)**2)/5
    pygame.draw.polygon(screen, (200, 200, 200), (
        (round(500 + ((mousex - 500)/thing2) * 3.5 - ((mousey - 250)/thing2) * 2.8 ), round(250 + ((mousey - 250)/thing2) * 3.5 + ((mousex - 500)/thing2) * 2.8)),
        (round(500 + ((mousex - 500)/thing2) * 3.5 + ((mousey - 250)/thing2) * 2.8 ), round(250 + ((mousey - 250)/thing2) * 3.5 - ((mousex - 500)/thing2) * 2.8)),
        (round(500 + ((mousex - 500)/thing2) * 2 + ((mousey - 250)/thing2) * 2.8 ), round(250 + ((mousey - 250)/thing2) * 2 - ((mousex - 500)/thing2) * 2.8)),
        (round(500 + ((mousex - 500)/thing2) * 2 - ((mousey - 250)/thing2) * 2.8 ), round(250 + ((mousey - 250)/thing2) * 2 + ((mousex - 500)/thing2) * 2.8))))
    pygame.draw.polygon(screen, (200, 200, 200), (
        (round(500 - ((mousex - 500)/thing2) * 3.5 + ((mousey - 250)/thing2) * 2.8 ), round(250 - ((mousey - 250)/thing2) * 3.5 - ((mousex - 500)/thing2) * 2.8)),
        (round(500 - ((mousex - 500)/thing2) * 3.5 - ((mousey - 250)/thing2) * 2.8 ), round(250 - ((mousey - 250)/thing2) * 3.5 + ((mousex - 500)/thing2) * 2.8)),
        (round(500 - ((mousex - 500)/thing2) * 2 - ((mousey - 250)/thing2) * 2.8 ), round(250 - ((mousey - 250)/thing2) * 2 + ((mousex - 500)/thing2) * 2.8)),
        (round(500 - ((mousex - 500)/thing2) * 2 + ((mousey - 250)/thing2) * 2.8 ), round(250 - ((mousey - 250)/thing2) * 2 - ((mousex - 500)/thing2) * 2.8))))
    pygame.draw.polygon(screen, (255, 0, 0), ((round(500 + ((mousex - 500)/thing2) * 4 - ((mousey - 250)/thing2) * 2 ), round(250 + ((mousey - 250)/thing2) * 4 + ((mousex - 500)/thing2) * 2)),
(round(500 + ((mousex - 500)/thing2) * 4 + ((mousey - 250)/thing2) * 2 ), round(250 + ((mousey - 250)/thing2) * 4 - ((mousex - 500)/thing2) * 2)),
(round(500 - ((mousex - 500)/thing2) * 4 + ((mousey - 250)/thing2) * 2 ), round(250 - ((mousey - 250)/thing2) * 4 - ((mousex - 500)/thing2) * 2)),
(round(500 - ((mousex - 500)/thing2) * 4 - ((mousey - 250)/thing2) * 2 ), round(250 - ((mousey - 250)/thing2) * 4 + ((mousex - 500)/thing2) * 2))))

    mousexx = mousex
    mouseyy = mousey

    clock.tick(100)
    pygame.display.flip()