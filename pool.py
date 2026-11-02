import pygame
import sys
import random
import math
import time

pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((1080,540))

drag = False

ball = 1

ballhit = False

ballx = [750,800,800,850,850,850,900,900,900,900,950,950,950,950,950,340]
bally = [270,300,240,330,270,210,360,300,240,180,390,330,270,210,150,270]
ballxx = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
ballyy = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
ballxxx = [1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000]
ballyyy = [1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000]
ballcolor1 = []
ballcolor2 = []
ballcolor3 = []
ballglue1 = []
ballglue2 = []
ballgluedelay1 = []
ballgluedelay2 = []
ballexist = ["yes","yes","yes","yes","yes","yes","yes","yes","yes","yes","yes","yes","yes","yes","yes","yes"]
ballmove = ["no","no","no","no","no","no","no","no","no","no","no","no","no","no","no","no"]

for sdfbdsjfh in range(0,16):
    ballcolor1.append(random.randint(100,200))
    ballcolor2.append(random.randint(100, 200))
    ballcolor3.append(random.randint(100, 150))

font = pygame.font.Font("freesansbold.ttf", 32)

move = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    mousex, mousey = pygame.mouse.get_pos()

    screen.fill((100, 0, 250))

    for boopedy in range(0, 16):
        for boopidy in range(0, 16):
            if boopidy > boopedy:
                if math.sqrt((ballx[boopidy]-ballx[boopedy])**2+(bally[boopidy]-bally[boopedy])**2) < 28:
                    if ballexist[boopedy] == "yes" and ballexist[boopidy] == "yes":
                        if bally[boopidy] != bally[boopedy] and ballx[boopedy] != ballx[boopidy]:
                            replace1 = ballxxx[boopedy]
                            replace2 = ballyyy[boopedy]
                            replace3 = ballxxx[boopidy]
                            replace4 = ballyyy[boopidy]
                            if len(ballglue1) != 0:
                                for cnn in range(0, len(ballglue1)):
                                    if ballglue1[cnn] != boopedy and ballglue2[cnn] != boopidy:
                                        ballxxx[boopedy] = round(
                                12 * math.sqrt(abs(replace4 * replace3)) / (ballx[boopedy] - ballx[boopidy]), 3)
                                        ballyyy[boopedy] = round(
                                12 * math.sqrt(abs(replace3 * replace4)) / (bally[boopedy] - bally[boopidy]), 3)
                                        ballxxx[boopidy] = round(
                                12 * math.sqrt(abs(replace2 * replace1)) / (ballx[boopidy] - ballx[boopedy]), 3)
                                        ballyyy[boopidy] = round(
                                12 * math.sqrt(abs(replace1 * replace2)) / (bally[boopidy] - bally[boopedy]), 3)
                                    if ballglue1[cnn] == boopedy:
                                        if ballglue2[cnn] == boopidy:
                                            ballglue1.append[boopedy]
                                            ballglue2.append[boopidy]
                                            ballgluedelay1.append[10]
                                            ballgluedelay2.append[10]
                            else:
                                ballxxx[boopedy] = round(
                                12 * math.sqrt(abs(replace4 * replace3)) / (ballx[boopedy] - ballx[boopidy]), 3)
                                ballyyy[boopedy] = round(
                                12 * math.sqrt(abs(replace3 * replace4)) / (bally[boopedy] - bally[boopidy]), 3)
                                ballxxx[boopidy] = round(
                                12 * math.sqrt(abs(replace2 * replace1)) / (ballx[boopidy] - ballx[boopedy]), 3)
                                ballyyy[boopidy] = round(
                                12 * math.sqrt(abs(replace1 * replace2)) / (bally[boopidy] - bally[boopedy]), 3)

                            ballx[boopedy] += round((ballx[boopedy] - ballx[boopidy]) / random.randint(2,10))
                            bally[boopedy] += round((bally[boopedy] - bally[boopidy]) / random.randint(2,10))
                            ballx[boopidy] += round((ballx[boopidy] - ballx[boopedy]) / random.randint(2,10))
                            bally[boopidy] += round((bally[boopidy] - bally[boopedy]) / random.randint(2,10))

                        ballxx[boopedy] = 0
                        ballyy[boopedy] = 0
                        ballxx[boopidy] = 0
                        ballyy[boopidy] = 0

        for qwer in range(0, len(ballgluedelay1)):
            ballgluedelay1[qwer] -= 1
            ballgluedelay2[qwer] -= 1
            if ballgluedelay1[qwer] == 0:
                del(ballgluedelay1[qwer])
                del(ballgluedelay2[qwer])
                del(ballglue1[qwer])
                del(ballglue2[qwer])

        if ballexist[boopedy] == "yes":
            pygame.draw.circle(screen, (ballcolor1[boopedy], ballcolor2[boopedy], ballcolor3[boopedy]),
                                       (ballx[boopedy], bally[boopedy]), 14)
        if ballxxx[boopedy] > 0:
            ballxx[boopedy] += 1
            while ballxx[boopedy] > ballxxx[boopedy]:
                ballx[boopedy] += 1
                ballxx[boopedy] -= ballxxx[boopedy]
        if ballxxx[boopedy] < 0:
            ballxx[boopedy] -= 1
            while ballxx[boopedy] < ballxxx[boopedy]:
                ballx[boopedy] -= 1
                ballxx[boopedy] -= ballxxx[boopedy]
        if ballyyy[boopedy] > 0:
            ballyy[boopedy] += 1
            while ballyy[boopedy] > ballyyy[boopedy]:
                bally[boopedy] += 1
                ballyy[boopedy] -= ballyyy[boopedy]
        if ballyyy[boopedy] < 0:
            ballyy[boopedy] -= 1
            while ballyy[boopedy] < ballyyy[boopedy]:
                bally[boopedy] -= 1
                ballyy[boopedy] -= ballyyy[boopedy]
        if bally[boopedy] <= 24 and ballx[boopedy] >= 50 and ballx[boopedy] <= 510:
            ballyyy[boopedy] = -1 * ballyyy[boopedy]
            ballyy[boopedy] = -1 * ballyy[boopedy]
            bally[boopedy] = 31
        if bally[boopedy] <= 24 and ballx[boopedy] >= 570 and ballx[boopedy] <= 1030:
            ballyyy[boopedy] = -1*ballyyy[boopedy]
            ballyy[boopedy] = -1 * ballyy[boopedy]
            bally[boopedy] = 31
        if bally[boopedy] >= 516 and ballx[boopedy] >= 50 and ballx[boopedy] <= 510:
            ballyyy[boopedy] = -1 * ballyyy[boopedy]
            ballyy[boopedy] = -1 * ballyy[boopedy]
            bally[boopedy] = 509
        if bally[boopedy] >= 516 and ballx[boopedy] >= 570 and ballx[boopedy] <= 1030:
            ballyyy[boopedy] = -1*ballyyy[boopedy]
            ballyy[boopedy] = -1 * ballyy[boopedy]
            bally[boopedy] = 509
        if ballx[boopedy] <= 24 and bally[boopedy] >= 50 and bally[boopedy] <= 490:
            ballxxx[boopedy] = -1*ballxxx[boopedy]
            ballxx[boopedy] = -1 * ballxx[boopedy]
            ballx[boopedy] = 31
        if ballx[boopedy] >= 1056 and bally[boopedy] <= 490 and bally[boopedy] >= 50:
            ballxxx[boopedy] = -1*ballxxx[boopedy]
            ballxx[boopedy] = -1 * ballxx[boopedy]
            ballx[boopedy] = 1049
        if bally[boopedy] < 24 and ballx[boopedy] > 509 and ballx[boopedy] < 571:
            if ballexist[boopedy] == "yes":
                ballexist[boopedy] = "no"
                ballxxx[boopedy] = 1000
                ballyyy[boopedy] = 1000
                if boopedy == 4:
                    time.sleep(2)
                    sys.exit()
                else:
                    if ball == 1:
                        ball = 3
                    if ball == 2:
                        ball = 1
                    if ball == 3:
                        ball = 2
            if boopedy == 15:
                ballexist[15] = "yes"
                ballx[15] = 340
                bally[15] = 270
        if bally[boopedy] > 510 and ballx[boopedy] > 509 and ballx[boopedy] < 571:
            if ballexist[boopedy] == "yes":
                ballexist[boopedy] = "no"
                ballxxx[boopedy] = 1000
                ballyyy[boopedy] = 1000
                if boopedy == 4:
                    time.sleep(2)
                    sys.exit()
                else:
                    if ball == 1:
                        ball = 3
                    if ball == 2:
                        ball = 1
                    if ball == 3:
                        ball = 2
            if boopedy == 15:
                ballexist[15] = "yes"
                ballx[15] = 340
                bally[15] = 270
        if ballx[boopedy] < 10 and bally[boopedy] < 50:
            if ballexist[boopedy] == "yes":
                ballexist[boopedy] = "no"
                ballxxx[boopedy] = 1000
                ballyyy[boopedy] = 1000
                if boopedy == 4:
                    time.sleep(2)
                    sys.exit()
                else:
                    if ball == 1:
                        ball = 3
                    if ball == 2:
                        ball = 1
                    if ball == 3:
                        ball = 2
            if boopedy == 15:
                ballexist[15] = "yes"
                ballx[15] = 340
                bally[15] = 270
        if ballx[boopedy] < 50 and bally[boopedy] < 10:
            if ballexist[boopedy] == "yes":
                ballexist[boopedy] = "no"
                ballxxx[boopedy] = 1000
                ballyyy[boopedy] = 1000
                if boopedy == 4:
                    time.sleep(2)
                    sys.exit()
                else:
                    if ball == 1:
                        ball = 3
                    if ball == 2:
                        ball = 1
                    if ball == 3:
                        ball = 2
            if boopedy == 15:
                ballexist[15] = "yes"
                ballx[15] = 340
                bally[15] = 270
        if ballx[boopedy] < 10 and bally[boopedy] > 490:
            if ballexist[boopedy] == "yes":
                ballexist[boopedy] = "no"
                ballxxx[boopedy] = 1000
                ballyyy[boopedy] = 1000
                if boopedy == 4:
                    time.sleep(2)
                    sys.exit()
                else:
                    if ball == 1:
                        ball = 3
                    if ball == 2:
                        ball = 1
                    if ball == 3:
                        ball = 2
            if boopedy == 15:
                ballexist[15] = "yes"
                ballx[15] = 340
                bally[15] = 270
        if ballx[boopedy] < 50 and bally[boopedy] > 530:
            if ballexist[boopedy] == "yes":
                ballexist[boopedy] = "no"
                ballxxx[boopedy] = 1000
                ballyyy[boopedy] = 1000
                if boopedy == 4:
                    time.sleep(2)
                    sys.exit()
                else:
                    if ball == 1:
                        ball = 3
                    if ball == 2:
                        ball = 1
                    if ball == 3:
                        ball = 2
            if boopedy == 15:
                ballexist[15] = "yes"
                ballx[15] = 340
                bally[15] = 270
        if ballx[boopedy] > 1070 and bally[boopedy] < 50:
            if ballexist[boopedy] == "yes":
                ballexist[boopedy] = "no"
                ballxxx[boopedy] = 1000
                ballyyy[boopedy] = 1000
                if boopedy == 4:
                    time.sleep(2)
                    sys.exit()
                else:
                    if ball == 1:
                        ball = 3
                    if ball == 2:
                        ball = 1
                    if ball == 3:
                        ball = 2
            if boopedy == 15:
                ballexist[15] = "yes"
                ballx[15] = 340
                bally[15] = 270
        if ballx[boopedy] > 1030 and bally[boopedy] < 10:
            if ballexist[boopedy] == "yes":
                ballexist[boopedy] = "no"
                ballxxx[boopedy] = 1000
                ballyyy[boopedy] = 1000
                if boopedy == 4:
                    time.sleep(2)
                    sys.exit()
                else:
                    if ball == 1:
                        ball = 3
                    if ball == 2:
                        ball = 1
                    if ball == 3:
                        ball = 2
            if boopedy == 15:
                ballexist[15] = "yes"
                ballx[15] = 340
                bally[15] = 270
        if ballx[boopedy] > 1030 and bally[boopedy] > 530:
            if ballexist[boopedy] == "yes":
                ballexist[boopedy] = "no"
                ballxxx[boopedy] = 1000
                ballyyy[boopedy] = 1000
                if boopedy == 4:
                    time.sleep(2)
                    sys.exit()
                else:
                    if ball == 1:
                        ball = 3
                    if ball == 2:
                        ball = 1
                    if ball == 3:
                        ball = 2
            if boopedy == 15:
                ballexist[15] = "yes"
                ballx[15] = 340
                bally[15] = 270
        if ballx[boopedy] > 1070 and bally[boopedy] > 490:
            if ballexist[boopedy] == "yes":
                ballexist[boopedy] = "no"
                ballxxx[boopedy] = 1000
                ballyyy[boopedy] = 1000
                if boopedy == 4:
                    time.sleep(2)
                    sys.exit()
                else:
                    if ball == 1:
                        ball = 3
                    if ball == 2:
                        ball = 1
                    if ball == 3:
                        ball = 2
            if boopedy == 15:
                ballexist[15] = "yes"
                ballx[15] = 340
                bally[15] = 270
        ballxxx[boopedy] = round(81 * ballxxx[boopedy] / 80, 4)
        ballyyy[boopedy] = round(81 * ballyyy[boopedy] / 80, 4)
        if ballxxx[boopedy] > 400:
            ballxxx[boopedy] = 400
            ballxx[boopedy] = 0
        if ballyyy[boopedy] > 400:
            ballyyy[boopedy] = 400
            ballyy[boopedy] = 0
        if ballxxx[boopedy] < -400:
            ballxxx[boopedy] = -400
            ballxx[boopedy] = 0
        if ballyyy[boopedy] < -400:
            ballyyy[boopedy] = -400
            ballyy[boopedy] = 0
        if ballxxx[boopedy] == -400 or ballxxx[boopedy] == 400:
            if ballyyy[boopedy] == -400 or ballyyy[boopedy] == 400:
                ballmove[boopedy] = "no"
        if ballxxx[boopedy] != -400 and ballxxx[boopedy] != 400:
            ballmove[boopedy] = "yes"
        if ballyyy[boopedy] != -400 and ballyyy[boopedy] != 400:
            ballmove[boopedy] = "yes"
        if ballmove[boopedy] == "no":
            move += 1
        if move == 16:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if abs(mousex - ballx[15]) < 7:
                    if abs(mousey - bally[15]) < 7:
                        drag = True
                        move = 0
    ballmove = ["no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no", "no"]

    if ballexist[4] == "yes":
        pygame.draw.circle(screen, (0, 0, 0), (ballx[4], bally[4]), 14)
    if ballexist[15] == "yes":
        pygame.draw.circle(screen, (255, 255, 255), (ballx[15], bally[15]), 14)
    if ballexist[2] == "yes":
        pygame.draw.circle(screen, (255, 255, 255), (ballx[2], bally[2]), 9)
    if ballexist[1] == "yes":
        pygame.draw.circle(screen, (255, 255, 255), (ballx[1], bally[1]), 9)
    if ballexist[11] == "yes":
        pygame.draw.circle(screen, (255, 255, 255), (ballx[11], bally[11]), 9)
    if ballexist[12] == "yes":
        pygame.draw.circle(screen, (255, 255, 255), (ballx[12], bally[12]), 9)
    if ballexist[13] == "yes":
        pygame.draw.circle(screen, (255, 255, 255), (ballx[13], bally[13]), 9)
    if ballexist[6] == "yes":
        pygame.draw.circle(screen, (255, 255, 255), (ballx[6], bally[6]), 9)
    if ballexist[9] == "yes":
        pygame.draw.circle(screen, (255, 255, 255), (ballx[9], bally[9]), 9)
    pygame.draw.rect(screen, (255,255,255), (50,0,460, 10))
    pygame.draw.rect(screen, (255, 255, 255), (570, 0, 460, 10))
    pygame.draw.rect(screen, (255, 255, 255), (50, 530, 460, 10))
    pygame.draw.rect(screen, (255, 255, 255), (570, 530, 460, 10))
    pygame.draw.rect(screen, (255, 255, 255), (1070, 50, 10, 440))
    pygame.draw.rect(screen, (255, 255, 255), (0, 50, 10, 440))
    if ball == 1:
        pygame.draw.rect(screen, (255, 255, 0), (0, 50, 10, 440))
    if ball == 2:
        pygame.draw.rect(screen, (255, 255, 0), (1070, 50, 10, 440))
    if move != 16:
        pygame.draw.rect(screen, (0,0,0), (50, 0, 460, 10))
        pygame.draw.rect(screen, (0,0,0), (570, 0, 460, 10))
        pygame.draw.rect(screen, (0,0,0), (50, 530, 460, 10))
        pygame.draw.rect(screen, (0,0,0), (570, 530, 460, 10))

    if drag == True:
        pygame.draw.line(screen, (255, 255, 255), (mousex, mousey), (ballx[15], bally[15]), 3)
        if event.type == pygame.MOUSEBUTTONUP:
            if mousex != ballx[15] and mousey != bally[15]:
                drag = False
                ballxxx[15] = round(-20/(mousex - ballx[15]),3)
                ballyyy[15] = round(-20/(mousey - bally[15]),3)
                ballxx[15] = 0
                ballyy[15] = 0

    move =0

    pygame.display.flip()
    clock.tick(100)

ballx[boopedy] += round((ballx[boopedy] - ballx[boopidy]) / 10)
bally[boopedy] += round((bally[boopedy] - bally[boopidy]) / 10)
ballx[boopidy] += round((ballx[boopidy] - ballx[boopedy]) / 10)
bally[boopidy] += round((bally[boopidy] - bally[boopedy]) / 10)