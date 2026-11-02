import pygame
import sys
import random
import math
import pickle
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1000, 500))
stopwatch = 0
mousedown = True

filename = 'duel'

infile = open(filename,'rb')
block = pickle.load(infile)
infile.close()

# about your character
x = 0
y = 0
yy = 0

# place [x, y]

movingright = False
movingleft = False

onground = False

placing = False
placing2 = False

blah = True

boosttimer = 0

dclicktimer = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            outfile = open(filename, 'wb')
            pickle.dump(block, outfile)
            outfile.close()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                movingright = True
            if event.key == pygame.K_a:
                movingleft = True
            if event.key == pygame.K_w and onground == True:
                yy -= 5.5
            if event.key == pygame.K_SPACE:
                print("(" + str(round(x/50)) + ", " + str(round(y/50)) + ")")
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                movingright = False
            if event.key == pygame.K_a:
                movingleft = False
    screen.fill((0, 0, 0))
    mousex, mousey = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
        mousedown = True
    if event.type == pygame.MOUSEBUTTONUP:
        mousedown = False

    stopwatch += 1

    pygame.draw.rect(screen, (255, 255, 255), (485, 210, 30, 25))
    pygame.draw.rect(screen, (255, 255, 255), (485, 245, 30, 45))

    mouse_buttons = pygame.mouse.get_pressed()

    if placing == 1:
        placing = 2
    if mouse_buttons[2] and placing == 0:
        placing = 1
    if mouse_buttons[2]:
        True
    else:
        placing = 0

    for cat in range(0, 50):
        if ((round(y) + cat ) / 50) % 1 == 0:
            for dog in range(0, round(10)):
                pygame.draw.rect(screen, (255, 255, 255), (0, cat + dog*50 - 1, 1000, 1))
    for cat in range(0, 50):
        if ((round(x) + cat) / 50) % 1 == 0:
            for dog in range(0, round(20)):
                pygame.draw.rect(screen, (255, 255, 255), (cat + dog*50 - 1, 0, 1, 500))

    place = True
    if placing == 1:
        for cat in range(0, len(block)):
            if round((x + mousex - 500 - round(25)) / round(50)) == block[cat][0] and round((y + mousey - 250 - round(25)) / round(50)) == block[cat][1]:
                place = False
                del block[cat]
                break
        if mousex > 550 or mousex < 450 or mousey < 200 or mousey > 300:
            if place == True:
                block.append([round((x + mousex - 500 - round(25)) / round(50)), round((y + mousey - 250 - round(25)) / round(50))])

    if placing == 1:
        dclicktimer = 30
    dclicktimer -= 1

    yy += 0.1

    onground = False
    x = round(x, 3)
    y = round(y, 3)
    yy = round(yy, 3)
    if movingleft == True:
        x -= 3.5
    if movingright == True:
        x += 3.5
    y += yy
    for lol in range(0, 1):
        for cat in range(0, len(block)):
            if -100 < 50 * block[cat][0] - x + 500 < 1050 and -100 < 50 * block[cat][1] - y + 250 < 550:
                thing = round(50 * block[cat][0] - x + 500)
                thing2 = round(50 * block[cat][1] - y + 250)
                pygame.draw.rect(screen, (255, 255, 255), (thing, thing2, 50, 50))
                pygame.draw.rect(screen, (255, 255, 255), (thing + 15, thing2, 20, 50))
                pygame.draw.rect(screen, (255, 255, 255), (thing, thing2 + 15, 50, 20))
                pygame.draw.circle(screen, (255, 255, 255), (thing + 15, thing2 + 15), 15)
                pygame.draw.circle(screen, (255, 255, 255), (thing + 35, thing2 + 15), 15)
                pygame.draw.circle(screen, (255, 255, 255), (thing + 15, thing2 + 35), 15)
                pygame.draw.circle(screen, (255, 255, 255), (thing + 35, thing2 + 35), 15)
            if 440 < 50 * block[cat][0] - x + 500 < 445 and 165 < 50 * block[cat][
                1] - y + 250 < 285 and movingleft == True:
                x += 5
                blah = False
            if 510 < 50 * block[cat][0] - x + 500 < 515 and 165 < 50 * block[cat][
                1] - y + 250 < 285 and movingright == True:
                x -= 5
                blah = False
            if 440 < 50 * block[cat][0] - x + 500 < 510 and 255 < 50 * block[cat][1] - y + 250 < 290 and blah == True:
                onground = True
                if 50 * block[cat][1] - y + 250 < 289:
                    y -= 0.2
                yy = 0
            if 440 < 50 * block[cat][0] - x + 500 < 510 and 162 < 50 * block[cat][1] - y + 250 < 255 and blah == True:
                y += 0.1
                yy = 0

    boosttimer -= 1
    if mouse_buttons[0] and boosttimer <= 0:
        x += (mousex - 500)/20
        y += (mousey - 250)/20
        yy = 0
        boosttimer = 1

    if mouse_buttons[1] and onground == True and boosttimer <= 0:
        yy -= 20
        boosttimer = 10

    blah = True

    pygame.display.flip()
    clock.tick(100)