import pygame
import sys
import random
import math

pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((1080,540))

stickman = pygame.image.load('images/bomber1.jpg')
stickman = pygame.transform.scale(stickman, (30, 50))

screenshow = 0

movingleft = False
movingright = False
onground = False

replay = False
duration = 0

jump = False

diedelay = 100

dur = 0

platformx = []
platformy = []

difficulty = 1000

stopwatch = 0

slows = []

slowdelay = 0

for a in range(0, difficulty):
    platformx.append(random.randint(500*a, 500*a + 500))
    platformy.append(random.randint(100, 500))

platformy[0] = random.randint(100, 300)

x = platformx[0] + 30
y = platformy[0] - 100
xx = 0
yy = 0

bombx = []
bomby = []
bombxx = []
bombyy = []
bombr = []

replayx = []
replayy = []
replaybombx = []
replaybomby = []
replayr = []
replayb = []
replays = []

mousedown = False

delay = 0

stopwatch1 = 0

slow = False

font = pygame.font.Font("freesansbold.ttf", 30)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                if replay == False:
                    movingright = True
                    d = True
            if event.key == pygame.K_a:
                if replay == False:
                    movingleft = True
                    a1 = True
            if event.key == pygame.K_w and onground == True:
                if replay == False:
                    jump = True
                    w = True
            if event.key == pygame.K_SPACE and slow == False:
                slow = True
            elif event.key == pygame.K_SPACE and slow == True:
                slow = False

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d and replay == False:
                movingright = False
            if event.key == pygame.K_a and replay == False:
                movingleft = False
    round(x)
    slowdelay += 1

    if replay == False:
        if slow == False:
            replayx.append(x)
            replayy.append(y)
            replays.append(0)
            if len(bombx) == 1:
                replaybombx.append(bombx[0])
                replaybomby.append(bomby[0])
                replayr.append(bombr[0])
                replayb.append(1)
            else:
                replaybombx.append(0)
                replaybomby.append(0)
                replayr.append(0)
                replayb.append(0)
            if stopwatch == 0:
                slows.append(0)
            else:
                slows.append(slows[round(stopwatch) - 1])
        if slow == True:
            replayx.append(x)
            replayy.append(y)
            replays.append(1)
            if len(bombx) == 1:
                replaybombx.append(bombx[0])
                replaybomby.append(bomby[0])
                replayr.append(bombr[0])
                replayb.append(1)
            else:
                replaybombx.append(0)
                replaybomby.append(0)
                replayr.append(0)
                replayb.append(0)
            if stopwatch == 0:
                slows.append(1)
            else:
                slows.append(slows[round(stopwatch) - 1] + 1)

    thingymabob = font.render(str(x), False, (0, 255, 0))
    thingymabob1 = font.render("Replay", False, (0, 255, 0))

    screen.fill((255, 255, 255))

    stopwatch += 1
    delay += 1
    stopwatch1 += 1

    if slow == True:
        stopwatch -= 0.9
        delay -= 0.9
        stopwatch1 -= 0.9

    if replay == True:
        if replays[round(stopwatch)] == 1:
            stopwatch += 9

    mousex, mousey = pygame.mouse.get_pos()

    onground = False

    if movingleft == True:
        x -= 3
        if slow == True:
            x += 2.7
    if movingright == True:
        x += 3
        if slow == True:
            x -= 2.7

    if x <= 15:
        x = 15
        xx = 0
    if y <= 30:
        yy = 0
        xx = 0
        y = 31
    if y >= 510:
        y = 511
        xx = 0
        yy = 0
        if replay == False:
            diedelay -= 1
        if diedelay <= 0:
            x = platformx[0] + 30
            y = platformy[0] - 100
            xx = 0
            yy = 0
            bombx = []
            bomby = []
            bombxx = []
            bombyy = []
            bombr = []
            diedelay = 100
            if replay == False:
                duration = stopwatch
                replay = True
            stopwatch = 0
            stopwatch1 = 0

    if onground == True and jump == False:
        yy = 0

    if jump == True:
        yy -= 5
        jump = False
        onground = False

    x += xx
    y += yy
    if slow == True:
        x -= xx * 0.9
        y -= yy * 0.9

    yy += 0.1
    if slow == True:
        yy -= 0.09

    screenshow = x - 200

    screen.blit(stickman, (x - 15 - screenshow, y - 25))

    if event.type == pygame.MOUSEBUTTONDOWN:
        mousedown = True

    if event.type == pygame.MOUSEBUTTONUP:
        mousedown = False

    for a in range(0, difficulty):
        pygame.draw.rect(screen, (0, 0, 0), (platformx[a] - screenshow, platformy[a], 60, 20))
        if platformy[a] - 25 <= y <= platformy[a] - 5:
            if platformx[a] <= x <= platformx[a] + 60:
                if yy >= 0:
                    onground = True
                    y = platformy[a] - 25
                yy = 0
                xx = 0
        if platformy[a] - 5 <= y <= platformy[a] + 45:
            if platformx[a] <= x <= platformx[a] + 60:
                y = platformy[a] + 46
                yy = 0

    if mousedown == True and len(bombx) == 0:
        if (x - screenshow - mousex) != 0:
            bombx.append(x)
            bomby.append(y)
            ratio = (y - mousey) / (x - screenshow - mousex)
            if (y - mousey) < 0 and (x - screenshow - mousex) < 0:
                bombyy.append(round(ratio * math.sqrt(100 / (ratio ** 2 + 1)) + yy, 3))
                bombxx.append(round(math.sqrt(100 / (ratio ** 2 + 1)) + xx, 3))
            if (y - mousey) >= 0 and (x - screenshow - mousex) >= 0:
                bombyy.append(-round(ratio * math.sqrt(100 / (ratio ** 2 + 1)) + yy, 3))
                bombxx.append(-round(math.sqrt(100 / (ratio ** 2 + 1)) + xx, 3))
            if (x - screenshow - mousex) < 0 and (y - mousey) >= 0:
                bombyy.append(round(ratio * math.sqrt(100 / (ratio ** 2 + 1)) + yy, 3))
                bombxx.append(round(math.sqrt(100 / (ratio ** 2 + 1)) + xx, 3))
            if (x - screenshow - mousex) >= 0 and (y - mousey) < 0:
                bombyy.append(-round(ratio * math.sqrt(100 / (ratio ** 2 + 1)) + yy, 3))
                bombxx.append(-round(math.sqrt(100 / (ratio ** 2 + 1)) + xx, 3))
            bombr.append(10)

    if len(bombx) == 0:
        delay = 0

    elif mousedown == True and len(bombx) >= 1 and delay >= 20:
        if bombr[0] == 10:
            bombr[0] = 11

    if len(bombx) == 1:
        if bombr[0] != 10:
            bombr[0] += 30
            if slow == True:
                bombr[0] -= 27
            if bombr[0] >= 200:
                bombx = []
                bomby = []
                bombxx = []
                bombyy = []
                bombr = []
                delay = 0

    if len(bombx) == 1:
        if bombr[0] != 10 and x - bombx[0] != 0:
            if (x - bombx[0]) ** 2 + (y - bomby[0]) ** 2 <= bombr[0] ** 2:
                ratio = (y - bomby[0]) / (x - bombx[0])
                if (y - bomby[0]) < 0 and (x - bombx[0]) < 0:
                    yy -= (round(ratio * math.sqrt(100 / (ratio ** 2 + 1)), 3))
                    xx -= (round(math.sqrt(100 / (ratio ** 2 + 1)), 3))
                if (y - bomby[0]) >= 0 and (x - bombx[0]) >= 0:
                    yy -= (-round(ratio * math.sqrt(100 / (ratio ** 2 + 1)), 3))
                    xx -= (-round(math.sqrt(100 / (ratio ** 2 + 1)), 3))
                if (x - bombx[0]) < 0 and (y - bomby[0]) >= 0:
                    yy -= (round(ratio * math.sqrt(100 / (ratio ** 2 + 1)), 3))
                    xx -= (round(math.sqrt(100 / (ratio ** 2 + 1)), 3))
                if (x - bombx[0]) >= 0 and (y - bomby[0]) < 0:
                    yy -= (-round(ratio * math.sqrt(100 / (ratio ** 2 + 1)), 3))
                    xx -= (-round(math.sqrt(100 / (ratio ** 2 + 1)), 3))
                if slow == True:
                    if (y - bomby[0]) < 0 and (x - bombx[0]) < 0:
                        yy += (round(ratio * math.sqrt(90 / (ratio ** 2 + 1)), 3))
                        xx += (round(math.sqrt(90 / (ratio ** 2 + 1)), 3))
                    if (y - bomby[0]) >= 0 and (x - bombx[0]) >= 0:
                        yy += (-round(ratio * math.sqrt(90 / (ratio ** 2 + 1)), 3))
                        xx += (-round(math.sqrt(90 / (ratio ** 2 + 1)), 3))
                    if (x - bombx[0]) < 0 and (y - bomby[0]) >= 0:
                        yy += (round(ratio * math.sqrt(90 / (ratio ** 2 + 1)), 3))
                        xx += (round(math.sqrt(90 / (ratio ** 2 + 1)), 3))
                    if (x - bombx[0]) >= 0 and (y - bomby[0]) < 0:
                        yy += (-round(ratio * math.sqrt(90 / (ratio ** 2 + 1)), 3))
                        xx += (-round(math.sqrt(90 / (ratio ** 2 + 1)), 3))

    for a in range(0, len(bombx)):
        pygame.draw.circle(screen, (255, 0, 0), (round(bombx[a] - screenshow), round(bomby[a])), round(bombr[a]), 10)
        if replay == False:
            if delay >= 20:
                pygame.draw.circle(screen, (0, 255, 0), (round(bombx[a] - screenshow), round(bomby[a])), 5)
            if bombr[a] == 10:
                bombx[a] += bombxx[a]
                bomby[a] += bombyy[a]
                bombyy[a] += 0.1
                if slow == True:
                    bombx[a] -= bombxx[a] * 0.9
                    bomby[a] -= bombyy[a] * 0.9
                    bombyy[a] -= 0.09
                for b in range(0, difficulty):
                    if platformx[b] - 10 <= bombx[a] <= platformx[b] + 70 and platformy[b] <= bomby[a] <= platformy[
                        b] + 20:
                        bombxx[a] = -bombxx[a]
                    if platformx[b] <= bombx[a] <= platformx[b] + 60 and platformy[b] - 10 <= bomby[a] <= platformy[
                        b] + 30:
                        bombyy[a] = -bombyy[a]
                    if bombx[a] < 10:
                        bombxx[a] = -bombxx[a]
                        bombx[a] = 10
                    if bomby[a] < 10:
                        bombyy[a] = -bombyy[a]
                        bomby[a] = 10
                    if bomby[a] > 530:
                        bombyy[a] = -bombyy[a]
                        bomby[a] = 530

    pygame.draw.rect(screen, (50, 255, 50), (500 * difficulty - screenshow, 0, 1000, 540))

    screen.blit(thingymabob, (20, 20))

    if x >= 500 * difficulty - 15:
        xx = 0
        yy = 0

    if x >= 500 * difficulty + 1000:
        replay = True
        duration = stopwatch
        stopwatch = 0
        stopwatch1 = 0
        x = platformx[0] + 30
        y = platformy[0] - 100
        xx = 0
        yy = 0
        bombx = []
        bomby = []
        bombxx = []
        bombyy = []
        bombr = []

    if replay == True:
        pygame.draw.rect(screen, (0, 255, 0), (1000, 0, 80, 80))
        pygame.draw.rect(screen, (0, 255, 0), (50, 500, 980, 10))
        pygame.draw.circle(screen, (255, 0, 0), (round(50 + 980*(stopwatch1) / duration), 505), 15)
        if mousedown == True and mousex > 1000 and mousey < 80:
            replay = False
            replayx = []
            replayy = []
            replaybombx = []
            replaybomby = []
            replayr = []
            replayb = []
            replays = []
            x = platformx[0] + 30
            y = platformy[0] - 100
            xx = 0
            yy = 0
            bombx = []
            bomby = []
            bombxx = []
            bombyy = []
            bombr = []
            duration = 0
        if stopwatch + 1 >= len(replayx):
            bombx = []
            bomby = []
            bombxx = []
            bombyy = []
            bombr = []
            stopwatch = 0
            stopwatch1 = 0
        if replay == True:
            xx = 0
            yy = 0
            x = replayx[round(stopwatch)]
            y = replayy[round(stopwatch)]
            if replayb[round(stopwatch)] == 1:
                if len(bombx) == 0:
                    bombx.append(replaybombx[round(stopwatch)])
                    bomby.append(replaybomby[round(stopwatch)])
                    bombr.append(replayr[round(stopwatch)])
                else:
                    bombx[0] = replaybombx[round(stopwatch)]
                    bomby[0] = replaybomby[round(stopwatch)]
                    bombr[0] = replayr[round(stopwatch)]

    if replay == True:
        screen.blit(thingymabob1, (20, 50))

    pygame.display.flip()
    clock.tick(100)