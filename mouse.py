import pygame

import sys

pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((1080,540))

screenshow = "no"

draw = "no"

words = [1,1,1,1,1,1,1,1,1,1,1,1]

font = pygame.font.Font("freesansbold.ttf", 400)

word = 1

worddelay = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    mousex, mousey = pygame.mouse.get_pos()

    if mousey > 470:
        if event.type == pygame.MOUSEBUTTONDOWN:
            screenshow = "yes"

    if screenshow == "yes":
        screen.fill((0,0,0))
        word += 1
        screenshow = "no"
        print(word)

    if word >= 13:
        word = 1
        words[0] = 1
        words[1] = 1
        words[2] = 1
        words[3] = 1
        words[4] = 1
        words[5] = 1
        words[6] = 1
        words[7] = 1
        words[8] = 1
        words[9] = 1
        words[10] = 1
        words[11] = 1

    if word == 1 and words[0] == 1:
        anyi = font.render("Anyi", False, (255,255,255))
        screen.blit(anyi, (60, 60))
        words[0] = 0
    if word == 2 and words[1] == 1:
        fun = font.render("fun", False, (255,255,255))
        screen.blit(fun, (60, 60))
        words[1] = 0
    if word == 3 and words[2] == 1:
        good = font.render("good", False, (255,255,255))
        screen.blit(good, (60, 60))
        words[2] = 0
    if word == 4 and words[3] == 1:
        each = font.render("EACH", False, (255,255,255))
        screen.blit(each, (60, 60))
        words[3] = 0
    if word == 5 and words[4] == 1:
        nice = font.render("nice", False, (255,255,255))
        screen.blit(nice, (60, 60))
        words[4] = 0
    if word == 6 and words[5] == 1:
        get = font.render("Get", False, (255,255,255))
        screen.blit(get, (60, 60))
        words[5] = 0
    if word == 7 and words[6] == 1:
        cool = font.render("COOL", False, (255,255,255))
        screen.blit(cool, (60, 60))
        words[6] = 0
    if word == 8 and words[7] == 1:
        book = font.render("book", False, (255,255,255))
        screen.blit(fun, (60, 60))
        words[7] = 0
    if word == 9 and words[8] == 1:
        numbers = font.render(str(123), False, (255,255,255))
        screen.blit(numbers, (60, 60))
        words[8] = 0
    if word == 10 and words[9] == 1:
        numbers2 = font.render(str(456), False, (255,255,255))
        screen.blit(numbers2, (60, 60))
        words[9] = 0
    if word == 11 and words[10] == 1:
        numbers3 = font.render(str(7890), False, (255,255,255))
        screen.blit(numbers3, (60, 60))
        words[10] = 0
    if word == 12 and words[11] == 1:
        line = font.render("LINE", False, (255,255,255))
        screen.blit(line, (60, 60))
        words[11] = 0

    if event.type == pygame.MOUSEBUTTONDOWN:
        draw = "yes"
    if event.type == pygame.MOUSEBUTTONUP:
        draw = "no"
    if draw == "yes":
        pygame.draw.circle(screen, (0,0,0), (mousex, mousey), 50)

    pygame.display.flip()
    clock.tick(200)