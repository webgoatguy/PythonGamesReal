import pygame
import sys
import random
import pickle
import math

pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((1200,1000))

font = pygame.font.Font("freesansbold.ttf", 32)
#I reccommend this font, and the 32 part is the size. Adjust as needed. you can even create another font size
tinyfont = pygame.font.Font("freesansbold.ttf", 10)

x_pos = 300
y_pos = 300

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            #This just means that if a key is being pressed down in this frame:
            if event.key == pygame.K_0:
                #if the key being pressed is 0: (this can detect multiple keys at once)
                #blah blah blah happens
                print(1)
            if event.key == pygame.K_z:
                #if the key being pressed is z:
                #blah blah blah happens
                print(2)
        elif event.type == pygame.KEYUP:
            #This just means that if a key is NOT being pressed down in this frame:
            if event.key == pygame.K_0:
                #if that key is 0: (this can detect multiple keys at once)
                print(1)

    screen.fill((255, 0, 150))
    #fill the screen

    #pygame.draw.rect(screen, (color in rbe), (x - position, y - position, x - dimension, y - dimension))

    #pygame.draw.circle(screen, (color in rbe), (x - pos, y - pos), radius, width is you need it (optional))

    #pygame.draw.polygon(screen, (color in rbe), ((x - pos, y - pos), (another point), (and another point), (and as much as you want)), and width of the polygon if you want it(optional))

    #pygame.draw.line(screen, (color), (x - pos, y - pos), (same with second point), width of line)

    #REMEMBER ABOUT THE PARENTHESES! CHECK THAT EACH PAIR MATCH UP!

    #AND ALSO TO DRAW THESE STUFF AFTER THE screen.fill!

    #TEXT

    #so you already put the text before.
    #now make a text message:
    message1 = font.render("Hello!", False, (255, 255, 255))
    #and another one using the tinyfont that we made earlier
    message2 = tinyfont.render("Hello!?", False, (255, 255, 255))
    #and another one with another color:
    message3 = tinyfont.render("This is stupid", False, (0, 0, 0))
    # and another one with a number:
    message4 = tinyfont.render(str(69), False, (0, 0, 0))
    # and another one with a number variable:
    message5 = tinyfont.render(str(x_pos), False, (0, 255, 0))

    # and then is putting the text on the screen.

    screen.blit(message1, (100, 100))
    #                      x, y pos
    # and another message somewhere else:
    screen.blit(message2, (250, 100))
    # you can use the same message multiple times:
    screen.blit(message1, (250, 200))

    pygame.display.flip()
    clock.tick(100)