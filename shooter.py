import pygame
import sys
import random
import math
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1000, 500), pygame.FULLSCREEN)
stopwatch = 0
mousedown = False

#which way
movingright = False
movingleft = False
movingup = False
movingdown = False

#ur position
x = 0
y = 0
xx = 0
yy = 0

#balls - [x, y, xx, yy, hitpoints, startinghitpoints, level, del, type]
ball = []

for cat in range(0, 50):
    thing2 = random.randint(10, 25)
    ball.append([random.randint(-1000, 1000), random.randint(-1000, 1000), random.randint(-20, 20)/10, random.randint(-20, 20)/10, thing2, thing2, 1, False, 1])
    thing2 = random.randint(1, 20)
    if 8 < thing2 < 14:
        ball[cat][6] = 2
    if 13 < thing2 < 17:
        ball[cat][6] = 3
    if 16 < thing2 < 19:
        ball[cat][6] = 4
    if thing2 == 19:
        ball[cat][6] = 5
    if thing2 == 20:
        thing4 = random.randint(1, 20)
        if thing4 < 12:
            ball[cat][6] = 6
        else:
            ball[cat][6] = 7

#bullets - [x, y, xx, yy, damage, del]
bullet = []

score = 0

pistolreload = 0
reload = 2
damage = 8

#text stuff
font = pygame.font.Font("freesansbold.ttf", 30)
def text(text, x, y):
    textblit = font.render(text, False, (255, 255, 255))
    screen.blit(textblit, (x, y))

lastdied = 0

boost = False
superboost = False
hyperboost = False

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
                movingup = True
            if event.key == pygame.K_s:
                movingdown = True
            if event.key == pygame.K_SPACE and score >= 1:
                boost = True
            if event.key == pygame.K_v and score >= 10:
                superboost = True
            if event.key == pygame.K_b and score >= 100:
                hyperboost = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                movingright = False
            if event.key == pygame.K_a:
                movingleft = False
            if event.key == pygame.K_w:
                movingup = False
            if event.key == pygame.K_s:
                movingdown = False
            if event.key == pygame.K_SPACE:
                boost = False
            if event.key == pygame.K_v:
                superboost = False
            if event.key == pygame.K_b:
                hyperboost = False

    screen.fill((0, 0, 0))
    mousex, mousey = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
        mousedown = True
    if event.type == pygame.MOUSEBUTTONUP:
        mousedown = False
    stopwatch += 1

    pygame.draw.circle(screen, (255, 255, 255), (500, 250), 20)

    pistolreload -= 1

    text(str(score), 10, 10)

    x += xx
    y += yy

    if score < 1:
        boost = False
    if score < 10:
        superboost = False
    if score < 100:
        hyperboost = False

    if boost == True:
        score -= 1
    if superboost == True:
        score -= 10
    if hyperboost == True:
        score -= 100

    if xx > 0:
        xx -= 0.05
    if xx < 0:
        xx += 0.05
    if movingright == False and movingleft == False:
        if -0.25 < xx < 0.25:
            xx = 0
    if yy > 0:
        yy -= 0.05
    if yy < 0:
        yy += 0.05
    if movingdown == False and movingup == False:
        if -0.25 < yy < 0.25:
            yy = 0

    if movingright == True and xx < 4:
        xx += 0.15
    if movingleft == True and xx > -4:
        xx -= 0.15
    if movingdown == True and yy < 4:
        yy += 0.15
    if movingup == True and yy > -4:
        yy -= 0.15

    for cat in range(0, 50):
        if ((round(y) + cat) / 50) % 1 == 0:
            for dog in range(0, 10):
                pygame.draw.rect(screen, (255, 255, 255), (0, cat + dog*50 - 1, 1000, 1))
    for cat in range(0, 50):
        if ((round(x) + cat) / 50) % 1 == 0:
            for dog in range(0, 20):
                pygame.draw.rect(screen, (255, 255, 255), (cat + dog*50 - 1, 0, 1, 500))

    if mousedown == True and pistolreload < 0:
        thing = math.sqrt((mousex - 500)**2 + (mousey - 250)**2)
        if hyperboost == True:
            for a in range(0, 7):
                bullet.append([x, y, (mousex - 500)*10/thing + random.randint(-30, 30)/20 + xx, (mousey - 250)*10/thing + random.randint(-30, 30)/20 + yy, damage*50, False])
        if superboost == True:
            for a in range(0, 5):
                bullet.append([x, y, (mousex - 500)*10/thing + random.randint(-20, 20)/20 + xx, (mousey - 250)*10/thing + random.randint(-20, 20)/20 + yy, damage*10, False])
        if boost == True:
            for a in range(0, 3):
                bullet.append([x, y, (mousex - 500)*10/thing + random.randint(-15, 15)/20 + xx, (mousey - 250)*10/thing + random.randint(-15, 15)/20 + yy, damage*3, False])
        else:
            bullet.append([x, y, (mousex - 500) * 10 / thing + random.randint(-10, 10) / 20 + xx,
                           (mousey - 250) * 10 / thing + random.randint(-10, 10) / 20 + yy, damage, False])
        pistolreload = reload

    pygame.draw.rect(screen, (255, 255, 255), (-1550 - x, -1800 - y, 4100, 50))
    pygame.draw.rect(screen, (255, 255, 255), (-1550 - x, -1800 - y, 50, 4100))
    pygame.draw.rect(screen, (255, 255, 255), (-1550 - x, 2250 - y, 4100, 50))
    pygame.draw.rect(screen, (255, 255, 255), (2500 - x, -1800 - y, 50, 4100))

    for cat in range(0, len(bullet)):
        bullet[cat][0] += bullet[cat][2]
        bullet[cat][1] += bullet[cat][3]
        if bullet[cat][4] == damage:
            pygame.draw.circle(screen, (255, 255, 255), (round(bullet[cat][0] - x + 500), round(bullet[cat][1] - y + 250)), 4)
        if bullet[cat][4] == damage*3:
            pygame.draw.circle(screen, (255, 255, 0), (round(bullet[cat][0] - x + 500), round(bullet[cat][1] - y + 250)), 4)
        if bullet[cat][4] == damage*10:
            pygame.draw.circle(screen, (255, 200, 0), (round(bullet[cat][0] - x + 500), round(bullet[cat][1] - y + 250)), 4)
        if bullet[cat][4] == damage*50:
            pygame.draw.circle(screen, (255, 0, 0), (round(bullet[cat][0] - x + 500), round(bullet[cat][1] - y + 250)), 4)
        if bullet[cat][0] > x + 600 or bullet[cat][0] < x - 600 or bullet[cat][1] > y + 300 or bullet[cat][1] < y - 300:
            bullet[cat][5] = True
        if bullet[cat][0] > 1000 or bullet[cat][0] < -1000 or bullet[cat][1] > 1000 or bullet[cat][1] < -1000:
            bullet[cat][5] = True

    if x > 1000:
        x = 1000
        xx = -xx
    if x < -1000:
        x = -1000
        xx = -xx
    if y > 1000:
        y = 1000
        yy = -yy
    if y < -1000:
        y = -1000
        yy = -yy

    if len(ball) > 100:
        for cat in range(0, 10):
            del ball[0]
        print(1)

    if len(ball) < 50:
        thing2 = random.randint(10, 25)
        thing5 = random.randint(1, 10)
        ball.append([random.randint(-1000, 1000), random.randint(-1000, 1000), random.randint(-15, 15) / 10,
                     random.randint(-20, 20) / 10, thing2, thing2, 1, False, 1])
        thing2 = random.randint(1, 20)
        if 8 < thing2 < 14:
            ball[len(ball) - 1][6] = 2
        if 13 < thing2 < 17:
            ball[len(ball) - 1][6] = 3
        if 16 < thing2 < 19:
            ball[len(ball) - 1][6] = 4
        if thing2 == 19:
            ball[len(ball) - 1][6] = 5
        if thing2 == 20:
            thing4 = random.randint(1, 20)
            if thing4 < 12:
                ball[len(ball) - 1][6] = 6
            else:
                ball[len(ball) - 1][6] = 7

    for cat in range(0, len(ball)):
        ball[cat][0] += ball[cat][2]
        ball[cat][1] += ball[cat][3]
        if ball[cat][0] - 600 < x < ball[cat][0] + 600 and ball[cat][1] - 350 < y < ball[cat][1] + 350:
            pygame.draw.circle(screen, (0, 200, 200), (round(ball[cat][0] - x + 500), round(ball[cat][1] - y + 250)), 4*ball[cat][6]+10)
            pygame.draw.rect(screen, (255, 255, 255), (round(ball[cat][0] - x + 460), round(ball[cat][1] - y + 200), 80, 4))
            pygame.draw.rect(screen, (255, 0, 0), (round(ball[cat][0] - x + 460), round(ball[cat][1] - y + 200), 80*ball[cat][4]/ball[cat][5], 4))
            text(str(ball[cat][8]), round(ball[cat][0] - x + 490), round(ball[cat][1] - y + 237))
            for dog in range(0, len(bullet)):
                    if ball[cat][0] - 50 < bullet[dog][0] < ball[cat][0] + 50 and ball[cat][1] - 50 < bullet[dog][1] < \
                            ball[cat][1] + 50:
                        radius1 = 4 * ball[cat][6] + 10
                        radius2 = 4
                        if (ball[cat][0] - bullet[dog][0]) ** 2 + (ball[cat][1] - bullet[dog][1]) ** 2 < (
                                radius1 + radius2) ** 2:
                            energy1 = radius1 * math.sqrt(ball[cat][2] ** 2 + ball[cat][3] ** 2)
                            energy2 = radius2 * math.sqrt(bullet[dog][2] ** 2 + bullet[dog][3] ** 2)
                            bullet[dog][5] = True
                            ball[cat][4] -= bullet[dog][4]
        if ball[cat][0] > 1000:
            ball[cat][2] = -ball[cat][2]
            ball[cat][0] = 1000
        if ball[cat][0] < -1000:
            ball[cat][2] = -ball[cat][2]
            ball[cat][0] = -1000
        if ball[cat][1] > 1000:
            ball[cat][3] = -ball[cat][3]
            ball[cat][1] = 1000
        if ball[cat][1] < -1000:
            ball[cat][3] = -ball[cat][3]
            ball[cat][1] = -1000
        for dog in range(0, len(ball)):
            if cat != dog:
                if ball[cat][0] - 50 < ball[dog][0] < ball[cat][0] + 50 and ball[cat][1] - 50 < ball[dog][1] < ball[cat][1] + 50:
                    radius1 = 4*ball[cat][6] + 10
                    radius2 = 4*ball[dog][6] + 10
                    if (ball[cat][0] - ball[dog][0])**2 + (ball[cat][1] - ball[dog][1])**2 < (radius1 + radius2)**2:
                        while (ball[cat][0] - ball[dog][0])**2 + (ball[cat][1] - ball[dog][1])**2 < (radius1 + radius2)**2:
                            ball[cat][0] += (ball[cat][0] - ball[dog][0])/40
                            ball[cat][1] += (ball[cat][1] - ball[dog][1])/40
                            ball[dog][0] -= (ball[cat][0] - ball[dog][0]) / 40
                            ball[dog][1] -= (ball[cat][1] - ball[dog][1]) / 40
                        energy1 = radius1 * math.sqrt(ball[cat][2]**2 + ball[cat][3]**2)
                        energy2 = radius2 * math.sqrt(ball[dog][2]**2 + ball[dog][3]**2)
                        ball[cat][2] = (ball[cat][0] - ball[dog][0])*energy2/radius1/40
                        ball[cat][3] = (ball[cat][1] - ball[dog][1])*energy2/radius1/40
                        ball[dog][2] = (ball[dog][0] - ball[cat][0])*energy1/radius2/40
                        ball[dog][3] = (ball[dog][1] - ball[cat][1])*energy1/radius2/40
        if ball[cat][0] - 50 < x < ball[cat][0] + 50 and ball[cat][1] - 50 < y < ball[cat][1] + 50:
            radius1 = 4*ball[cat][6] + 10
            radius2 = 20
            if (ball[cat][0] - x)**2 + (ball[cat][1] - y)**2 < (radius1 + radius2)**2:
                while (ball[cat][0] - x)**2 + (ball[cat][1] - y)**2 < (radius1 + radius2)**2:
                    ball[cat][0] += (ball[cat][0] - x)/50
                    ball[cat][1] += (ball[cat][1] - y)/50
                    x -= (ball[cat][0] - x) / 50
                    y -= (ball[cat][1] - y) / 50
                energy1 = radius1 * math.sqrt(ball[cat][2]**2 + ball[cat][3]**2)
                energy2 = radius2 * math.sqrt(xx**2 + yy**2)
                ball[cat][2] = (ball[cat][0] - x)*energy2/radius1/50
                ball[cat][3] = (ball[cat][1] - y)*energy2/radius1/50
                xx = (x - ball[cat][0])*energy1/radius2/50
                yy = (y - ball[cat][1])*energy1/radius2/50
        if ball[cat][2] > 10 or ball[cat][2] < -10:
            ball[cat][2] = 0.99*ball[cat][2]
        if ball[cat][3] > 10 or ball[cat][3] < -10:
            ball[cat][3] = 0.99*ball[cat][3]
        if -1 < ball[cat][2] < 1:
            ball[cat][2] = 1.01*ball[cat][2]
        if -1 < ball[cat][3] < 1:
            ball[cat][3] = 1.01*ball[cat][3]
        if ball[cat][4] <= 0:
            ball[cat][7] = True

    for dog in range(0, 50):
        for cat in range(0, len(bullet)):
            if bullet[cat][5] == True:
                del bullet[cat]
                break

    for dog in range(0, 10):
        for cat in range(0, len(ball)):
            if ball[cat][7] == True:
                score += round(math.sqrt(ball[cat][8] ** 5))
                if ball[cat][6] > 1:
                    if random.randint(1, 3) == 3:
                        thing6 = ball[cat][8] + round(random.randint(2, 12) / 10)
                        thing2 = random.randint(10 * round((2*thing6 / 3 + 1) ** 2), round(25 * (2*thing6 / 3 + 1) ** 2))
                        thing5 = random.randint(1, 10)
                        ball.append(
                            [random.randint(-1000, 1000), random.randint(-1000, 1000), random.randint(-15, 15) / 10,
                             random.randint(-20, 20) / 10, thing2, thing2, 1, False, thing6])
                        thing2 = random.randint(1, 20)
                        if 8 < thing2 < 14:
                            ball[len(ball) - 1][6] = 2
                        if 13 < thing2 < 17:
                            ball[len(ball) - 1][6] = 3
                        if 16 < thing2 < 19:
                            ball[len(ball) - 1][6] = 4
                        if thing2 == 19:
                            ball[len(ball) - 1][6] = 5
                        if thing2 == 20:
                            thing4 = random.randint(1, 20)
                            if thing4 < 12:
                                ball[len(ball) - 1][6] = 6
                            else:
                                ball[len(ball) - 1][6] = 7
                    thing3 = random.randint(70, 110) / 100
                    ball.append([ball[cat][0] + random.randint(-20, 20), ball[cat][1] + random.randint(-20, 20),
                                 ball[cat][2] + random.randint(-10, 10) / 10,
                                 ball[cat][3] + random.randint(-10, 10) / 10, round(ball[cat][5] * thing3, 1),
                                 round(ball[cat][5] * thing3, 1), ball[cat][6] - 1, False, ball[cat][8]])
                    ball.append([ball[cat][0] - random.randint(-20, 20), ball[cat][1] - random.randint(-20, 20),
                                 ball[cat][2] - random.randint(-10, 10) / 10,
                                 ball[cat][3] - random.randint(-10, 10) / 10, round(ball[cat][5] * thing3, 1),
                                 round(ball[cat][5] * thing3, 1), ball[cat][6] - 1, False, ball[cat][8]])
                    radius1 = 4 * ball[len(ball) - 1][6] + 10
                    radius2 = 4 * ball[len(ball) - 2][6] + 10
                    while (ball[len(ball) - 1][0] - ball[len(ball) - 2][0]) ** 2 + (
                            ball[len(ball) - 1][1] - ball[len(ball) - 2][1]) ** 2 < (radius1 + radius2) ** 2:
                        ball[len(ball) - 1][0] += (ball[len(ball) - 1][0] - ball[len(ball) - 2][0]) / 50
                        ball[len(ball) - 1][1] += (ball[len(ball) - 1][1] - ball[len(ball) - 2][1]) / 50
                        ball[len(ball) - 2][0] -= (ball[len(ball) - 1][0] - ball[len(ball) - 2][0]) / 50
                        ball[len(ball) - 2][1] -= (ball[len(ball) - 1][1] - ball[len(ball) - 2][1]) / 50
                        ball[len(ball) - 1][0] += random.randint(-1, 1)
                        ball[len(ball) - 1][1] += random.randint(-1, 1)
                        ball[len(ball) - 2][0] -= random.randint(-1, 1)
                        ball[len(ball) - 2][1] -= random.randint(-1, 1)
                    ball[len(ball) - 1][2] = (ball[len(ball) - 1][0] - ball[len(ball) - 2][0]) / 50
                    ball[len(ball) - 1][3] = (ball[len(ball) - 1][1] - ball[len(ball) - 2][1]) / 50
                    ball[len(ball) - 2][2] = -(ball[len(ball) - 1][0] - ball[len(ball) - 2][0]) / 50
                    ball[len(ball) - 2][3] = -(ball[len(ball) - 1][1] - ball[len(ball) - 2][1]) / 50
                    lastdied = ball[cat][8]
                del ball[cat]
                break

    pygame.display.flip()
    clock.tick(100)