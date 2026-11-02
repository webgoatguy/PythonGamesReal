import pygame
import sys
import random
import math
pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((1500,1000))

grass_color = (126, 200, 80)

simspeed = 1

blobx = []
bloby = []
blobspeed = []
blobsize = []
blobsense = []
#does the blob see food? if so, which food?
blobsensed = []
#blob ate this number of food
blobate = []
blobenergy = []
#when random walking, every second they get a new destination
blobdestx = []
blobdesty = []
blobnumber = 20

foodx = []
foody = []
#food number that stays constant throughout the day (changes every nonexistent night)
foodnumber = 50
#food number that you can change and changes the actual observed foor number every nonexistent night
foodnumber2 = 50

#is the simulation speed going up, down?
simspeedup = False
simspeeddown = False

#is the food number going up, down?
foodup = False
fooddown = False

daytimer = 0
timer = 0

for a in range (0, blobnumber):
    blobx.append(random.randint(10, 990))
    bloby.append(random.randint(10, 990))
    blobspeed.append(50)
    blobsize.append(12)
    blobsense.append(250)
    blobsensed.append(False)
    blobate.append(0)
    blobenergy.append(500)
    blobdestx.append(blobx[a] + random.randint(-200, 200))
    blobdesty.append(bloby[a] + random.randint(-200, 200))

for b in range(0, foodnumber):
    foodx.append(random.randint(5, 995))
    foody.append(random.randint(5, 995))

font = pygame.font.Font("freesansbold.ttf", 30)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                simspeedup = True
            if event.key == pygame.K_a:
                simspeeddown = True
            if event.key == pygame.K_q:
                fooddown = True
            if event.key == pygame.K_e:
                foodup = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                simspeedup = False
            if event.key == pygame.K_a:
                simspeeddown = False
            if event.key == pygame.K_q:
                fooddown = False
            if event.key == pygame.K_e:
                foodup = False

    if simspeed >= 1:
        if simspeedup == True:
            simspeed += 0.0125
        if simspeeddown == True:
            simspeed -= 0.0125
    else:
        if simspeedup == True:
            simspeed += 0.0025
        if simspeeddown == True:
            simspeed -= 0.0025
    if foodnumber2 >= 50:
        if foodup == True:
            foodnumber2 += 0.6
        if fooddown == True:
            foodnumber2 -= 0.6
    else:
        if foodup == True:
            foodnumber2 += 0.15
        if fooddown == True:
            foodnumber2 -= 0.15

    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, grass_color, (0, 0, 1000, 1000))

    #limit sense, speed, size, x, y, foodnumber, simspeed
    for a in range (0, blobnumber):
        if blobsense[a] > 250:
            blobsense[a] = 250
        if blobsense[a] < 50:
            blobsense[a] = 50
        if blobspeed[a] > 100:
            blobspeed[a] = 100
        if blobspeed[a] < 20:
            blobspeed[a] = 20
        if blobsize[a] > 15:
            blobsize[a] = 15
        if blobsize[a] < 5:
            blobsize[a] = 5
        if blobx[a] > 1000 - blobsize[a]:
            blobx[a] = 1000 - blobsize[a]
        if blobx[a] < blobsize[a]:
            blobx[a] = blobsize[a]
        if bloby[a] > 1000 - blobsize[a]:
            bloby[a] = 1000 - blobsize[a]
        if bloby[a] < blobsize[a]:
            bloby[a] = blobsize[a]
        if timer == 0:
            if blobdestx[a] > 1000 - blobsize[a]:
                blobdestx[a] = 1000 - blobsize[a]
            if blobdestx[a] < blobsize[a]:
                blobdestx[a] = blobsize[a]
            if blobdesty[a] > 1000 - blobsize[a]:
                blobdesty[a] = 1000 - blobsize[a]
            if blobdesty[a] < blobsize[a]:
                blobdesty[a] = blobsize[a]
        if simspeed < 0.1:
            simspeed = 0.1
        if simspeed > 5:
            simspeed = 5
        if foodnumber2 > 100:
            foodnumber2 = 100
        if foodnumber2 < 10:
            foodnumber2 = 10

    #determine if the blob sees food, or eats it
    if timer == 10 or timer == 20 or timer == 30 or timer == 40 or timer == 0:
        for a in range(0, blobnumber):
            for b in range(0, round(foodnumber)):
                for c in range(1, 4):
                    if foodx[b] != -1:
                        if (blobx[a] - foodx[b])**2 + (bloby[a] - foody[b])**2 <= (blobsense[a]**2)*c/3:
                            blobsensed[a] = b

    #make blobs move
    for a in range(0, blobnumber):
        if blobsensed[a] == False:
            blobx[a] -= (blobx[a] - blobdestx[a])*simspeed*blobspeed[a]/1000
            bloby[a] -= (bloby[a] - blobdesty[a])*simspeed*blobspeed[a]/1000
        elif blobsensed[a] >= 0:
            if blobx[a] - foodx[blobsensed[a]] > 0:
                blobx[a] -= blobspeed[a]*simspeed/10
            elif blobx[a] - foodx[blobsensed[a]] < 0:
                blobx[a] += blobspeed[a]*simspeed/10
            if bloby[a] - foody[blobsensed[a]] > 0:
                bloby[a] -= blobspeed[a]*simspeed/10
            elif bloby[a] - foody[blobsensed[a]] < 0:
                bloby[a] += blobspeed[a]*simspeed/10
            if ((blobx[a] - foodx[blobsensed[a]])**2 + (bloby[a] - foody[blobsensed[a]])**2) <= ((blobsize[a] + 5)**2)+2.5*simspeed**3:
                foodx[blobsensed[a]] = -1
                foody[blobsensed[a]] = -1
                blobsensed[a] = False
                blobenergy[a] += 200
                blobate[a] += 1
                break

    #draw blobs
    for a in range(0, blobnumber):
        pygame.draw.circle(screen, (blobsense[a], blobsense[a], blobsense[a]), (round(blobx[a]), round(bloby[a])), round(blobsize[a]))

    #draw food
    for b in range(0, round(foodnumber)):
        if foodx[b] != -1:
            pygame.draw.circle(screen, (255, 255, 255), (foodx[b], foody[b]), 5)

    text1 = font.render("Sim. speed: (Use A and D)", False, (0, 255, 0))
    text2 = font.render(str(round(simspeed, 2)), False, (0, 255, 0))
    text3 = font.render("Food per day: (Use Q and E)", False, (0, 255, 0))
    text4 = font.render(str(round(foodnumber2)), False, (0, 255, 0))
    screen.blit(text1, (1010, 10))
    screen.blit(text2, (1425, 10))
    screen.blit(text3, (1010, 40))
    screen.blit(text4, (1425, 40))

    for a in range(0, blobnumber):
        blobenergy[a] -= round(simspeed*(blobspeed[a]**2)*(blobsize[a]**3)/2000000, 3)
        if blobenergy[a] <= 0:
            del blobx[a]
            del bloby[a]
            del blobenergy[a]
            del blobate[a]
            del blobsense[a]
            del blobsize[a]
            del blobspeed[a]
            del blobdestx[a]
            del blobdesty[a]
            blobnumber -= 1
            break

    #draw graph
    pygame.draw.rect(screen, (255, 255, 255), (1010, 110, 480, 480))
    pygame.draw.rect(screen, (0, 0, 0), (1015, 115, 470, 470))
    for a in range(0, blobnumber):
        pygame.draw.circle(screen, (blobsense[a], blobsense[a], blobsense[a]), (890 + 6*blobspeed[a], round(825 - 48*blobsize[a])), round(blobsize[a]))

    for a in range(0, blobnumber):
        if blobsensed[a] != False:
            if blobsensed[a] >= 0:
                if foodx[blobsensed[a]] == -1:
                    blobsensed[a] = False

    daytimer += simspeed
    timer += simspeed
    if timer >= 50:
        blobdestx = []
        blobdesty = []
        timer = 0
        for a in range(0, blobnumber):
            blobdestx.append(blobx[a] + random.randint(-200, 200))
            blobdesty.append(bloby[a] + random.randint(-200, 200))
    if daytimer >= 500:
        daytimer = 0
        foodx = []
        foody = []
        foodnumber = round(foodnumber2)
        for b in range(0, round(foodnumber)):
            foodx.append(random.randint(5, 995))
            foody.append(random.randint(5, 995))
        for a in range(0, blobnumber):
            blobsensed[a] = False
            if blobate[a] >= 5:
                blobx.append(blobx[a] + random.randint(-30, 30))
                bloby.append(bloby[a] + random.randint(-30, 30))
                blobate.append(0)
                blobenergy.append(500)
                blobnumber += 1
                blobsensed.append(False)
                blobdestx.append(blobx[a] + random.randint(-200, 200))
                blobdesty.append(bloby[a] + random.randint(-200, 200))
                if random.randint(1, 5) == 1:
                    blobspeed.append(blobspeed[a] + random.randint(-5, 5))
                else:
                    blobspeed.append(blobspeed[a])
                if random.randint(1, 5) == 1:
                    blobsense.append(blobsense[a] + random.randint(-8, 8))
                else:
                    blobsense.append(blobsense[a])
                if random.randint(1, 5) == 1:
                    blobsize.append(blobsize[a] + random.randint(-5, 5)/10)
                else:
                    blobsize.append(blobsize[a])
    pygame.display.flip()
    clock.tick(100)