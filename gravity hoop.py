import pygame
import sys
import time
import pickle

#gravity formula: for a and b objects, axx += bmass * (bx - ax) / distance, same goes for yy and object b

pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((1080,540))

level = 1

filename = 'hooplevels'

slide = "levels"

levels = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

infile = open(filename,'rb')
levels = pickle.load(infile)
infile.close()

levels = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

ballx = 50
bally = 50
ballxx = 0
ballyy = 0
balldrag = False

play = False

hoopx = [200]
hoopy = [200]
hooppos = [2]
hoopdone = [0]
hoopdone1 = 0

blackholex = [200]
blackholey = [200]
blackholemass = [10]
blackholemove = [False]

wallx = [500]
wally = [500]
wallmove = [False]

bouncex = [250]
bouncey = [500]
bouncemove = [False]

whiteholex = []
whiteholey = []
whiteholemass = []
whiteholemove = []

arrowx = [100]
arrowy = [100]
arrowpos = [3]
arrowmove = [False]

mousedown = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            outfile = open(filename, 'wb')
            pickle.dump(levels, outfile)
            outfile.close()
            sys.exit()

    screen.fill((0, 0, 0))

    mousex, mousey = pygame.mouse.get_pos()

    if event.type == pygame.MOUSEBUTTONDOWN:
        mousedown = True
    if event.type == pygame.MOUSEBUTTONUP:
        mousedown = False

    if slide == "gameplay":
        hoopdone1 = 0
        ballx += ballxx
        bally += ballyy
        pygame.draw.rect(screen, (255, 255, 255), (1000, 0, 80, 540))
        pygame.draw.circle(screen, (255, 255, 255), (round(ballx), round(bally)), 10)
        if ballx - 10 < mousex < ballx + 10 and bally - 10 < mousey < bally + 10 and mousedown == True and ballxx == 0 and ballyy == 0:
            balldrag = True
        if balldrag == True:
            pygame.draw.line(screen, (255, 255, 255), (round(ballx), round(bally)), (mousex, mousey), 2)
            if mousedown == False:
                ballxx = (mousex - ballx)/50
                ballyy = (mousey - bally)/50
                balldrag = False
                play = True
        for cat in range(0, len(hoopx)):
            if hoopdone[cat] == 1:
                hoopdone1 += 1
            if hooppos[cat] == 1 and hoopdone[cat] == 0:
                pygame.draw.rect(screen, (255, 255, 255), (hoopx[cat] - 20, hoopy[cat] - 20, 3, 40))
                pygame.draw.rect(screen, (255, 255, 255), (hoopx[cat] + 17, hoopy[cat] - 20, 3, 40))
                pygame.draw.rect(screen, (100, 100, 255), (hoopx[cat] - 20, hoopy[cat] + 17, 40, 3))
                if ballyy > 0 and abs(ballyy) > abs(ballxx):
                    if hoopx[cat] - 15 <= ballx <= hoopx[cat] + 15:
                        if hoopy[cat] - 20 <= bally <= hoopy[cat] + 20:
                            hoopdone[cat] = 1
            if hooppos[cat] == 2 and hoopdone[cat] == 0:
                pygame.draw.rect(screen, (255, 255, 255), (hoopx[cat] - 20, hoopy[cat] - 20, 40, 3))
                pygame.draw.rect(screen, (255, 255, 255), (hoopx[cat] - 20, hoopy[cat] + 20, 40, 3))
                pygame.draw.rect(screen, (100, 100, 255), (hoopx[cat] - 20, hoopy[cat] - 17, 3, 40))
                if ballxx < 0 and abs(ballxx) > abs(ballyy):
                    if hoopx[cat] - 20 <= ballx <= hoopx[cat] + 20:
                        if hoopy[cat] - 15 <= bally <= hoopy[cat] + 15:
                            hoopdone[cat] = 1
            if hooppos[cat] == 3 and hoopdone[cat] == 0:
                pygame.draw.rect(screen, (255, 255, 255), (hoopx[cat] - 20, hoopy[cat] - 20, 3, 40))
                pygame.draw.rect(screen, (255, 255, 255), (hoopx[cat] + 17, hoopy[cat] - 20, 3, 40))
                pygame.draw.rect(screen, (100, 100, 255), (hoopx[cat] - 20, hoopy[cat] - 20, 40, 3))
                if ballyy < 0 and abs(ballyy) > abs(ballxx):
                    if hoopx[cat] - 15 <= ballx <= hoopx[cat] + 15:
                        if hoopy[cat] - 20 <= bally <= hoopy[cat] + 20:
                            hoopdone[cat] = 1
            if hooppos[cat] == 4 and hoopdone[cat] == 0:
                pygame.draw.rect(screen, (255, 255, 255), (hoopx[cat] - 20, hoopy[cat] - 20, 40, 3))
                pygame.draw.rect(screen, (255, 255, 255), (hoopx[cat] - 20, hoopy[cat] + 20, 40, 3))
                pygame.draw.rect(screen, (100, 100, 255), (hoopx[cat] + 17, hoopy[cat] - 20, 3, 40))
                if ballxx > 0 and abs(ballxx) > abs(ballyy):
                    if hoopx[cat] - 20 <= ballx <= hoopx[cat] + 20:
                        if hoopy[cat] - 15 <= bally <= hoopy[cat] + 15:
                            hoopdone[cat] = 1
            if hooppos[cat] == 1 and hoopdone[cat] == 1:
                pygame.draw.rect(screen, (0, 255, 0), (hoopx[cat] - 20, hoopy[cat] - 20, 3, 40))
                pygame.draw.rect(screen, (0, 255, 0), (hoopx[cat] + 17, hoopy[cat] - 20, 3, 40))
                pygame.draw.rect(screen, (0, 255, 0), (hoopx[cat] - 20, hoopy[cat] + 17, 40, 3))
            if hooppos[cat] == 2 and hoopdone[cat] == 1:
                pygame.draw.rect(screen, (0, 255, 0), (hoopx[cat] - 20, hoopy[cat] - 20, 40, 3))
                pygame.draw.rect(screen, (0, 255, 0), (hoopx[cat] - 20, hoopy[cat] + 20, 40, 3))
                pygame.draw.rect(screen, (0, 255, 0), (hoopx[cat] - 20, hoopy[cat] - 17, 3, 40))
            if hooppos[cat] == 3 and hoopdone[cat] == 1:
                pygame.draw.rect(screen, (0, 255, 0), (hoopx[cat] - 20, hoopy[cat] - 20, 3, 40))
                pygame.draw.rect(screen, (0, 255, 0), (hoopx[cat] + 17, hoopy[cat] - 20, 3, 40))
                pygame.draw.rect(screen, (0, 255, 0), (hoopx[cat] - 20, hoopy[cat] - 20, 40, 3))
            if hooppos[cat] == 4 and hoopdone[cat] == 1:
                pygame.draw.rect(screen, (0, 255, 0), (hoopx[cat] - 20, hoopy[cat] - 20, 40, 3))
                pygame.draw.rect(screen, (0, 255, 0), (hoopx[cat] - 20, hoopy[cat] + 20, 40, 3))
                pygame.draw.rect(screen, (0, 255, 0), (hoopx[cat] + 17, hoopy[cat] - 20, 3, 40))
        if hoopdone1 == len(hoopx):
            time.sleep(1)
            slide = "levels"
            levels[level - 1] = 1
        for cat in range(0, len(blackholex)):
            pygame.draw.circle(screen, (255, 255, 255), (blackholex[cat], blackholey[cat]), blackholemass[cat], 3)
            if play == True:
                distance = (blackholex[cat] - ballx) ** 2 + (blackholey[cat] - bally) ** 2
                ballxx += round(blackholemass[cat] * (blackholex[cat] - ballx) / (distance), 3)
                ballyy += round(blackholemass[cat] * (blackholey[cat] - bally) / (distance), 3)
        for cat in range(0, len(whiteholex)):
            pygame.draw.circle(screen, (255, 255, 255), (whiteholex[cat], whiteholey[cat]), whiteholemass[cat] * 2)
            if play == True:
                distance = (whiteholex[cat] - ballx) ** 2 + (whiteholey[cat] - bally) ** 2
                ballxx -= round(whiteholemass[cat] * (whiteholex[cat] - ballx) / (distance), 3)
                ballyy -= round(whiteholemass[cat] * (whiteholey[cat] - bally) / (distance), 3)
        for cat in range(0, len(wallx)):
            pygame.draw.rect(screen, (100, 100, 100), (wallx[cat] - 10, wally[cat] - 10, 20, 20))
            if wallx[cat] - 20 < ballx < wallx[cat] + 20 and wally[cat] - 20 < bally < wally[cat] + 20:
                if wallx[cat] - 10 < ballx < wallx[cat] + 10:
                    ballyy = -ballyy/3
                if wally[cat] - 10 < bally < wally[cat] + 10:
                    ballxx = -ballxx/3
        for cat in range(0, len(bouncex)):
            pygame.draw.rect(screen, (255, 0, 0), (bouncex[cat] - 10, bouncey[cat] - 10, 20, 20))
            if bouncex[cat] - 20 < ballx < bouncex[cat] + 20 and bouncey[cat] - 20 < bally < bouncey[cat] + 20:
                if bouncex[cat] - 10 < ballx < bouncex[cat] + 10:
                    ballyy = -ballyy*1.5
                if bouncey[cat] - 10 < bally < bouncey[cat] + 10:
                    ballxx = -ballxx*1.5
        for cat in range(0, len(arrowx)):
            pygame.draw.rect(screen, (100, 100, 100), (arrowx[cat] - 15, arrowy[cat] - 15, 30, 30))
            if arrowpos[cat] == 1:
                pygame.draw.polygon(screen, (255, 255, 255), ((arrowx[cat] + 10, arrowy[cat] + 10), (arrowx[cat] - 10, arrowy[cat] + 10), (arrowx[cat], arrowy[cat] - 10)))
            if arrowpos[cat] == 2:
                pygame.draw.polygon(screen, (255, 255, 255), ((arrowx[cat] - 10, arrowy[cat] - 10), (arrowx[cat] - 10, arrowy[cat] + 10), (arrowx[cat] + 10, arrowy[cat])))
            if arrowpos[cat] == 3:
                pygame.draw.polygon(screen, (255, 255, 255), ((arrowx[cat] + 10, arrowy[cat] - 10), (arrowx[cat] - 10, arrowy[cat] - 10), (arrowx[cat], arrowy[cat] + 10)))
            if arrowpos[cat] == 4:
                pygame.draw.polygon(screen, (255, 255, 255), ((arrowx[cat] + 10, arrowy[cat] + 10), (arrowx[cat] + 10, arrowy[cat] - 10), (arrowx[cat] - 10, arrowy[cat])))
            if arrowx[cat] - 15 < ballx < arrowx[cat] + 15 and arrowy[cat] - 15 < bally < arrowy[cat] + 15 and play == True:
                if arrowpos[cat] == 1:
                    ballyy -= 0.25
                if arrowpos[cat] == 2:
                    ballxx += 0.25
                if arrowpos[cat] == 3:
                    ballyy += 0.25
                if arrowpos[cat] == 4:
                    ballxx -= 0.25
        if play == False:
            for cat in range(0, len(blackholex)):
                if blackholex[cat] - blackholemass[cat] < mousex < blackholex[cat] + blackholemass[cat] and blackholemove[cat] == False\
                        and blackholey[cat] - blackholemass[cat] < mousey < blackholey[cat] + blackholemass[cat] and mousedown == True:
                    blackholemove[cat] = True
                if blackholemove[cat] == True:
                    blackholex[cat] = mousex
                    blackholey[cat] = mousey
                    if mousedown == False:
                        blackholemove[cat] = False
            for cat in range(0, len(whiteholex)):
                if whiteholex[cat] - whiteholemass[cat]*2 < mousex < whiteholex[cat] + whiteholemass[cat]*2 and whiteholemove[cat] == False \
                        and whiteholey[cat] - whiteholemass[cat]*2 < mousey < whiteholey[cat] + whiteholemass[cat]*2 and mousedown == True:
                    whiteholemove[cat] = True
                if whiteholemove[cat] == True:
                    whiteholex[cat] = mousex
                    whiteholey[cat] = mousey
                    if mousedown == False:
                        whiteholemove[cat] = False
            for cat in range(0, len(wallx)):
                if wallx[cat] - 10 < mousex < wallx[cat] + 10 and wallmove[cat] == False \
                        and wally[cat] - 10 < mousey < wally[cat] + 10 and mousedown == True:
                    wallmove[cat] = True
                if wallmove[cat] == True:
                    wallx[cat] = mousex
                    wally[cat] = mousey
                    if mousedown == False:
                        wallmove[cat] = False
            for cat in range(0, len(bouncex)):
                if bouncex[cat] - 10 < mousex < bouncex[cat] + 10 and bouncemove[cat] == False \
                        and bouncey[cat] - 10 < mousey < bouncey[cat] + 10 and mousedown == True:
                    bouncemove[cat] = True
                if bouncemove[cat] == True:
                    bouncex[cat] = mousex
                    bouncey[cat] = mousey
                    if mousedown == False:
                        bouncemove[cat] = False
            for cat in range(0, len(arrowx)):
                if arrowx[cat] - 10 < mousex < arrowx[cat] + 10 and arrowmove[cat] == False \
                        and arrowy[cat] - 10 < mousey < arrowy[cat] + 10 and mousedown == True:
                    arrowmove[cat] = True
                if arrowmove[cat] == True:
                    arrowx[cat] = mousex
                    arrowy[cat] = mousey
                    if mousedown == False:
                        arrowmove[cat] = False
                        if arrowpos[cat] == 1:
                            arrowpos[cat] = 2
                        elif arrowpos[cat] == 2:
                            arrowpos[cat] = 3
                        elif arrowpos[cat] == 3:
                            arrowpos[cat] = 4
                        elif arrowpos[cat] == 4:
                            arrowpos[cat] = 1
        if mousedown == True and mousex > 1000 and mousey < 270 or ballx > 1070 or ballx < 10 or bally > 530 or bally < 10:
            play = False
            ballxx = 0
            ballyy = 0
            for cat in range(0, len(hoopx)):
                hoopdone[cat] = 0
            if 1 <= level <= 3 or level == 6 or 8 <= level <= 12 or level == 14:
                ballx = 100
                bally = 100
            if 4 <= level <= 5 or level == 7 or level == 13:
                ballx = 250
                bally = 300

        for a in range(0, len(wallx)):
            for b in range(0, len(bouncex)):
                if bouncex[b] == wallx[a] and bouncey[b] == wally[a]:
                    wallmove[a] = 0
                    wallx[a] += 20
        for a in range(0, len(wallx)):
            for b in range(0, len(blackholex)):
                if blackholex[b] == wallx[a] and blackholey[b] == wally[a]:
                    wallmove[a] = 0
                    wallx[a] += 20
        for a in range(0, len(wallx)):
            for b in range(0, len(whiteholex)):
                if whiteholex[b] == wallx[a] and whiteholey[b] == wally[a]:
                    wallmove[a] = 0
                    wallx[a] += 20
        for a in range(0, len(wallx)):
            for b in range(0, len(arrowx)):
                if arrowx[b] == wallx[a] and arrowy[b] == wally[a]:
                    wallmove[a] = 0
                    wallx[a] += 20
        for a in range(0, len(bouncex)):
            for b in range(0, len(blackholex)):
                if blackholex[b] == bouncex[a] and blackholey[b] == bouncey[a]:
                    bouncemove[a] = 0
                    bouncex[a] += 20
        for a in range(0, len(bouncex)):
            for b in range(0, len(whiteholex)):
                if whiteholex[b] == bouncex[a] and whiteholey[b] == bouncey[a]:
                    bouncemove[a] = 0
                    bouncex[a] += 20
        for a in range(0, len(bouncex)):
            for b in range(0, len(arrowx)):
                if arrowx[b] == bouncex[a] and arrowy[b] == bouncey[a]:
                    bouncemove[a] = 0
                    bouncex[a] += 20
        for a in range(0, len(blackholex)):
            for b in range(0, len(whiteholex)):
                if whiteholex[b] == blackholex[a] and whiteholey[b] == blackholey[a]:
                    blackholemove[a] = 0
                    blackholex[a] += 20
        for a in range(0, len(blackholex)):
            for b in range(0, len(arrowx)):
                if arrowx[b] == blackholex[a] and arrowy[b] == blackholey[a]:
                    blackholemove[a] = 0
                    blackholex[a] += 20
        for a in range(0, len(whiteholex)):
            for b in range(0, len(arrowx)):
                if arrowx[b] == whiteholex[a] and arrowy[b] == whiteholey[a]:
                    whiteholemove[a] = 0
                    whiteholex[a] += 20
        for a in range(0, len(wallx)):
            for b in range(0, len(wallx)):
                if wallx[b] == wallx[a] and wally[b] == wally[a] and a != b:
                    wallmove[a] = 0
                    wallx[a] += 20
        for a in range(0, len(bouncex)):
            for b in range(0, len(bouncex)):
                if bouncex[b] == bouncex[a] and bouncey[b] == bouncey[a] and a != b:
                    bouncemove[a] = 0
                    bouncex[a] += 20
        for a in range(0, len(blackholex)):
            for b in range(0, len(blackholex)):
                if blackholex[b] == blackholex[a] and blackholey[b] == blackholey[a] and a != b:
                    blackholemove[a] = 0
                    blackholex[a] += 20
        for a in range(0, len(whiteholex)):
            for b in range(0, len(whiteholex)):
                if whiteholex[b] == whiteholex[a] and whiteholey[b] == whiteholey[a] and a != b:
                    whiteholemove[a] = 0
                    whiteholex[a] += 20
        for a in range(0, len(arrowx)):
            for b in range(0, len(arrowx)):
                if arrowx[b] == arrowx[a] and arrowy[b] == arrowy[a] and a != b:
                    arrowmove[a] = 0
                    arrowx[a] += 20

        if mousedown == True and mousex > 1000 and mousey > 270:
            slide = "levels"

    if slide == "levels":
        for cat in range(0, 10):
            for dog in range(0, 5):
                if levels[10*dog + cat] == 0:
                    pygame.draw.circle(screen, (255, 0, 0), (50 + cat * 105, 50 + 95 * dog), 25)
                else:
                    pygame.draw.circle(screen, (0, 255, 0), (50 + cat * 105, 50 + 95 * dog), 25)
                if mousedown == True and cat + dog != 0:
                    if 30 + cat * 105 <= mousex <= 70 + cat * 105 and 30 + dog * 95 <= mousey <= 70 + dog * 95:
                        if levels[10 * dog + cat - 1] != 0:
                            slide = "gameplay"
                            level = 10 * dog + cat + 1
                            play = False
                            if level == 2:
                                ballx = 100
                                bally = 100
                                ballxx = 0
                                ballyy = 0
                                hoopx = [500]
                                hoopy = [300]
                                hooppos = [3]
                                hoopdone = [0]
                                blackholex = [200]
                                blackholey = [200]
                                blackholemass = [10]
                                blackholemove = [False]
                                wallx = [200, 250, 300, 350, 400]
                                wally = [100, 100, 100, 100, 100]
                                wallmove = [False, False, False, False, False]
                                bouncex = []
                                bouncey = []
                                bouncemove = []
                                whiteholex = []
                                whiteholey = []
                                whiteholemass = []
                                whiteholemove = []
                                arrowx = []
                                arrowy = []
                                arrowpos = []
                                arrowmove = []
                            if level == 3:
                                ballx = 100
                                bally = 100
                                ballxx = 0
                                ballyy = 0
                                hoopx = [500, 600, 700]
                                hoopy = [300, 300, 300]
                                hooppos = [4, 4, 4]
                                hoopdone = [0, 0, 0]
                                blackholex = [200]
                                blackholey = [200]
                                blackholemass = [10]
                                blackholemove = [False]
                                wallx = [200, 250, 300, 350, 400]
                                wally = [100, 100, 100, 100, 100]
                                wallmove = [False, False, False, False, False]
                                bouncex = []
                                bouncey = []
                                bouncemove = []
                                whiteholex = []
                                whiteholey = []
                                whiteholemass = []
                                whiteholemove = []
                                arrowx = []
                                arrowy = []
                                arrowpos = []
                                arrowmove = []
                            if level == 4:
                                ballx = 250
                                bally = 300
                                ballxx = 0
                                ballyy = 0
                                hoopx = [500, 500]
                                hoopy = [500, 50]
                                hooppos = [4, 4]
                                hoopdone = [0, 0]
                                blackholex = [200]
                                blackholey = [200]
                                blackholemass = [10]
                                blackholemove = [False]
                                wallx = []
                                wally = []
                                wallmove = []
                                bouncex = [200, 250, 300]
                                bouncey = [150, 150, 150]
                                bouncemove = [False, False, False]
                                whiteholex = []
                                whiteholey = []
                                whiteholemass = []
                                whiteholemove = []
                                arrowx = []
                                arrowy = []
                                arrowpos = []
                                arrowmove = []
                            if level == 5:
                                ballx = 250
                                bally = 300
                                ballxx = 0
                                ballyy = 0
                                hoopx = [400]
                                hoopy = [500]
                                hooppos = [4]
                                hoopdone = [0]
                                blackholex = []
                                blackholey = []
                                blackholemass = []
                                blackholemove = []
                                wallx = []
                                wally = []
                                wallmove = []
                                bouncex = [200, 250, 300]
                                bouncey = [150, 150, 150]
                                bouncemove = [False, False, False]
                                whiteholex = [300]
                                whiteholey = [300]
                                whiteholemass = [10]
                                whiteholemove = [False]
                                arrowx = []
                                arrowy = []
                                arrowpos = []
                                arrowmove = []
                            if level == 7:
                                ballx = 250
                                bally = 300
                                ballxx = 0
                                ballyy = 0
                                hoopx = [500, 500, 700]
                                hoopy = [500, 50, 280]
                                hooppos = [4, 2, 1]
                                hoopdone = [0, 0, 0]
                                blackholex = [200]
                                blackholey = [200]
                                blackholemass = [10]
                                blackholemove = [False]
                                wallx = []
                                wally = []
                                wallmove = []
                                bouncex = [200, 250, 300]
                                bouncey = [150, 150, 150]
                                bouncemove = [False, False, False]
                                whiteholex = []
                                whiteholey = []
                                whiteholemass = []
                                whiteholemove = []
                                arrowx = []
                                arrowy = []
                                arrowpos = []
                                arrowmove = []
                            if level == 6:
                                ballx = 100
                                bally = 100
                                ballxx = 0
                                ballyy = 0
                                hoopx = [300, 350, 400, 450, 500, 550, 600, 650, 700, 750]
                                hoopy = [300, 300, 300, 300, 300, 300, 300, 300, 300, 300]
                                hooppos = [2, 2, 2, 2, 2, 4, 4, 4, 4, 4]
                                hoopdone = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                                blackholex = [200, 300]
                                blackholey = [200, 200]
                                blackholemass = [10, 15]
                                blackholemove = [False, False]
                                wallx = [200, 250, 300, 350, 400, 200, 250, 300, 350, 400]
                                wally = [100, 100, 100, 100, 100, 150, 150, 150, 150, 150]
                                wallmove = [False, False, False, False, False, False, False, False, False, False]
                                bouncex = [250]
                                bouncey = [200]
                                bouncemove = [False]
                                whiteholex = []
                                whiteholey = []
                                whiteholemass = []
                                whiteholemove = []
                                arrowx = []
                                arrowy = []
                                arrowpos = []
                                arrowmove = []
                            if level == 8:
                                ballx = 100
                                bally = 100
                                ballxx = 0
                                ballyy = 0
                                hoopx = [300, 350, 400, 450, 500, 550, 600, 650, 700, 750]
                                hoopy = [300, 300, 300, 300, 300, 300, 300, 300, 300, 300]
                                hooppos = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4]
                                hoopdone = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                                blackholex = []
                                blackholey = []
                                blackholemass = []
                                blackholemove = []
                                wallx = []
                                wally = []
                                wallmove = []
                                bouncex = []
                                bouncey = []
                                bouncemove = []
                                whiteholex = []
                                whiteholey = []
                                whiteholemass = []
                                whiteholemove = []
                                arrowx = [300, 350, 400, 450, 500, 550, 600, 650, 700, 750]
                                arrowy = [300, 300, 300, 300, 300, 300, 300, 300, 300, 300]
                                arrowpos = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
                                arrowmove = [False, False, False, False, False, False, False, False, False, False]
                            if level == 9:
                                ballx = 100
                                bally = 100
                                ballxx = 0
                                ballyy = 0
                                hoopx = [500]
                                hoopy = [500]
                                hooppos = [2]
                                hoopdone = [0]
                                blackholex = [250]
                                blackholey = [250]
                                blackholemass = [30]
                                blackholemove = [False]
                                wallx = []
                                wally = []
                                wallmove = []
                                bouncex = [200, 250, 300]
                                bouncey = [150, 150, 150]
                                bouncemove = [False, False, False]
                                whiteholex = [300]
                                whiteholey = [300]
                                whiteholemass = [10]
                                whiteholemove = [False]
                                arrowx = [250]
                                arrowy = [300]
                                arrowpos = [1]
                                arrowmove = [False]
                            if level == 10:
                                ballx = 100
                                bally = 100
                                ballxx = 0
                                ballyy = 0
                                hoopx = [500]
                                hoopy = [400]
                                hooppos = [3]
                                hoopdone = [0]
                                blackholex = []
                                blackholey = []
                                blackholemass = []
                                blackholemove = []
                                wallx = [200, 250, 300]
                                wally = [200, 200, 200]
                                wallmove = [False, False, False]
                                bouncex = [200, 250, 300]
                                bouncey = [150, 150, 150]
                                bouncemove = [False, False, False]
                                whiteholex = [300]
                                whiteholey = [300]
                                whiteholemass = [5]
                                whiteholemove = [False]
                                arrowx = [250]
                                arrowy = [300]
                                arrowpos = [1]
                                arrowmove = [False]
                            if level == 12:
                                ballx = 100
                                bally = 100
                                ballxx = 0
                                ballyy = 0
                                hoopx = [500, 500]
                                hoopy = [200, 400]
                                hooppos = [4, 4]
                                hoopdone = [0, 0]
                                blackholex = [100]
                                blackholey = [350]
                                blackholemass = [15]
                                blackholemove = [False]
                                wallx = [200, 250, 300, 200, 250, 300, 200, 250, 300, 200, 250, 300]
                                wally = [200, 200, 230, 230, 230, 200, 260, 260, 260, 290, 290, 290]
                                wallmove = [False, False, False, False, False, False, False, False, False, False, False, False]
                                bouncex = [200, 250, 300, 200, 250, 300, 200, 250, 300, 200, 250, 300]
                                bouncey = [320, 320, 350, 350, 350, 320, 380, 380, 380, 410, 410, 410]
                                bouncemove = [False, False, False, False, False, False, False, False, False, False, False,
                                            False]
                                whiteholex = []
                                whiteholey = []
                                whiteholemass = []
                                whiteholemove = []
                                arrowx = []
                                arrowy = []
                                arrowpos = []
                                arrowmove = []
                            if level == 11:
                                ballx = 100
                                bally = 100
                                ballxx = 0
                                ballyy = 0
                                hoopx = [500, 600, 100]
                                hoopy = [400, 400, 400]
                                hooppos = [2, 2, 4]
                                hoopdone = [0, 0, 0]
                                blackholex = []
                                blackholey = []
                                blackholemass = []
                                blackholemove = []
                                wallx = [200, 250, 300]
                                wally = [200, 200, 200]
                                wallmove = [False, False, False]
                                bouncex = [200, 250, 300]
                                bouncey = [150, 150, 150]
                                bouncemove = [False, False, False]
                                whiteholex = [300]
                                whiteholey = [300]
                                whiteholemass = [10]
                                whiteholemove = [False]
                                arrowx = [250]
                                arrowy = [300]
                                arrowpos = [1]
                                arrowmove = [False]
                            if level == 13:
                                ballx = 250
                                bally = 300
                                ballxx = 0
                                ballyy = 0
                                hoopx = [500, 500, 700]
                                hoopy = [500, 50, 280]
                                hooppos = [4, 4, 2]
                                hoopdone = [0, 0, 0]
                                blackholex = [200]
                                blackholey = [200]
                                blackholemass = [10]
                                blackholemove = [False]
                                wallx = []
                                wally = []
                                wallmove = []
                                bouncex = [200, 250]
                                bouncey = [150, 150]
                                bouncemove = [False, False]
                                whiteholex = [200]
                                whiteholey = [250]
                                whiteholemass = [4]
                                whiteholemove = [False]
                                arrowx = [200, 550, 300, 350, 400, 450, 500]
                                arrowy = [300, 300, 300, 300, 300, 300, 300]
                                arrowpos = [1, 1, 1, 1, 1, 1, 1]
                                arrowmove = [False, False, False, False, False, False, False]
                            if level == 14:
                                ballx = 100
                                bally = 100
                                ballxx = 0
                                ballyy = 0
                                hoopx = [500, 900, 900, 900, 900, 900, 900, 900, 900, 900]
                                hoopy = [100, 100, 150, 125, 106, 144, 119, 112, 128, 114]
                                hooppos = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4]
                                hoopdone = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                                blackholex = []
                                blackholey = []
                                blackholemass = []
                                blackholemove = []
                                wallx = []
                                wally = []
                                wallmove = []
                                bouncex = [200, 250]
                                bouncey = [150, 150]
                                bouncemove = [False, False]
                                whiteholex = [200]
                                whiteholey = [250]
                                whiteholemass = [5]
                                whiteholemove = [False]
                                arrowx = [200, 550, 300, 350, 400, 450, 500]
                                arrowy = [300, 300, 300, 300, 300, 300, 300]
                                arrowpos = [1, 1, 1, 1, 1, 1, 1]
                                arrowmove = [False, False, False, False, False, False, False]
                if mousedown == True and cat + dog == 0:
                    if 30 <= mousex <= 70 and 30 <= mousey <= 70:
                        slide = "gameplay"
                        level = 1
                        ballx = 100
                        bally = 100
                        ballxx = 0
                        ballyy = 0
                        hoopx = [300]
                        hoopy = [200]
                        hooppos = [1]
                        hoopdone = [0]
                        blackholex = [200]
                        blackholey = [200]
                        blackholemass = [10]
                        blackholemove = [False]
                        wallx = []
                        wally = []
                        wallmove = []
                        bouncex = []
                        bouncey = []
                        bouncemove = []
                        whiteholex = []
                        whiteholey = []
                        whiteholemass = []
                        whiteholemove = []
                        arrowx = []
                        arrowy = []
                        arrowpos = []
                        arrowmove = []
                        play = False

    pygame.display.flip()
    clock.tick(100)