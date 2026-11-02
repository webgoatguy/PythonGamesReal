import pygame
import sys
import random
import math
pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((1500,1000))

simspeed = 3
simspeedup = False
simspeeddown = False
carrycapacityup = False
carrycapacitydown = False

blobx = []
bloby = []
blobrep = []
blobdie = []
blobmut = []
blobdestx = []
blobdesty = []
blobsize = []
blobnumber = 20
carrycapacity = 50
#which blobs should die?
die = []
#blob size goes from (radius) of 10 to 30
#blob speed = blob size(chance every 10 frames to get a new destination)
#death chance: 5-30, replication chance: 5-30
#amount when reproduce: floor of (death chance / 5)
#mutation rate: 10-50

for a in range(0, blobnumber):
    blobx.append(random.randint(200, 800))
    bloby.append(random.randint(200, 800))
    blobrep.append(random.randint(10, 30))
    blobdie.append(random.randint(10, 30))
    blobmut.append(random.randint(30, 50))
    blobdestx.append(random.randint(blobx[a]-300, blobx[a]+300))
    blobdesty.append(random.randint(bloby[a]-300, bloby[a]+300))
    blobsize.append(random.randint(10, 20))
    # blobx.append(random.randint(200, 800))
    # bloby.append(random.randint(200, 800))
    # blobrep.append(random.randint(5, 30))
    # blobdie.append(random.randint(5, 30))
    # blobmut.append(random.randint(10, 50))
    # blobdestx.append(random.randint(blobx[a] - 300, blobx[a] + 300))
    # blobdesty.append(random.randint(bloby[a] - 300, bloby[a] + 300))
    # blobsize.append(random.randint(10, 30))

font = pygame.font.Font("freesansbold.ttf", 30)

timer = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                simspeedup = True
            if event.key == pygame.K_a:
                simspeeddown = True
            if event.key == pygame.K_e:
                carrycapacityup = True
            if event.key == pygame.K_q:
                carrycapacitydown = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                simspeedup = False
            if event.key == pygame.K_a:
                simspeeddown = False
            if event.key == pygame.K_e:
                carrycapacityup = False
            if event.key == pygame.K_q:
                carrycapacitydown = False

    if simspeed >= 3:
        if simspeedup == True:
            simspeed += 0.025
        if simspeeddown == True:
            simspeed -= 0.025
    elif simspeed >= 1:
        if simspeedup == True:
            simspeed += 0.015
        if simspeeddown == True:
            simspeed -= 0.015
    else:
        if simspeedup == True:
            simspeed += 0.005
        if simspeeddown == True:
            simspeed -= 0.005
    if carrycapacity >= 50:
        if carrycapacityup == True:
            carrycapacity += 0.3
        if carrycapacitydown == True:
            carrycapacity -= 0.3
    else:
        if carrycapacityup == True:
            carrycapacity += 0.2
        if carrycapacitydown == True:
            carrycapacity -= 0.2

    screen.fill((0, 0, 0))

    if simspeed < 0.1:
        simspeed = 0.1
    if simspeed > 10:
        simspeed = 10
    if carrycapacity < 20:
        carrycapacity = 20
    if carrycapacity > 100:
        carrycapacity = 100

    #make blobs move
    for a in range(0, blobnumber):
        blobx[a] -= (blobx[a] - blobdestx[a]) * simspeed / 50
        bloby[a] -= (bloby[a] - blobdesty[a]) * simspeed / 50

    #carrying capacity
    if blobnumber > carrycapacity:
        for a in range(0, round(blobnumber - carrycapacity)):
            die.append(random.randint(0, blobnumber-1))

    #draw blobs
    for a in range(0, blobnumber):
        pygame.draw.circle(screen, (round(blobrep[a]*8+10), round(blobdie[a]*8+10), round(blobmut[a]*5)), (round(blobx[a]), round(bloby[a])), round(blobsize[a]))

    text1 = font.render("Sim. speed: (Use A and D)", False, (0, 255, 0))
    text2 = font.render(str(round(simspeed, 2)), False, (0, 255, 0))
    screen.blit(text1, (1010, 940))
    screen.blit(text2, (1440, 940))
    text3 = font.render("Carrying Capacity: (Q and E)", False, (0, 255, 0))
    text4 = font.render(str(round(carrycapacity)), False, (0, 255, 0))
    screen.blit(text3, (1010, 970))
    screen.blit(text4, (1440, 970))
    if len(blobx) != 0:
        text5 = font.render("Average death rate %:", False, (0, 255, 0))
        text6 = font.render(str(round(sum(blobdie) / blobnumber, 2)), False, (0, 255, 0))
        screen.blit(text5, (1010, 910))
        screen.blit(text6, (1420, 910))
        text7 = font.render("Avg. reproduction rate %:", False, (0, 255, 0))
        text8 = font.render(str(round(sum(blobrep) / blobnumber, 2)), False, (0, 255, 0))
        screen.blit(text7, (1010, 880))
        screen.blit(text8, (1420, 880))
        text9 = font.render("Average blob size %:", False, (0, 255, 0))
        text10 = font.render(str(round(sum(blobsize) / blobnumber, 2)), False, (0, 255, 0))
        screen.blit(text9, (1010, 850))
        screen.blit(text10, (1420, 850))
        text11 = font.render("Average mutation rate %:", False, (0, 255, 0))
        text12 = font.render(str(round(sum(blobmut) / blobnumber, 2)), False, (0, 255, 0))
        screen.blit(text11, (1010, 820))
        screen.blit(text12, (1420, 820))
    text13 = font.render("# of blobs:", False, (0, 255, 0))
    text14 = font.render(str(blobnumber), False, (0, 255, 0))
    screen.blit(text13, (1010, 790))
    screen.blit(text14, (1420, 790))

    for b in range(0, 10):
        timer += simspeed/10
        if timer >= 10:
            timer = 0
            for a in range(0, blobnumber):
                if random.randint(1, 100) <= blobsize[a]:
                    #set new destination
                    blobdestx[a] = random.randint(round(blobx[a] - 300), round(blobx[a] + 300))
                    blobdesty[a] = random.randint(round(bloby[a] - 300), round(bloby[a] + 300))
                #reproduce or die?
                if random.randint(1, 100) <= round(blobrep[a]/3, 1):
                    #reproduce
                    for c in range(0, (blobdie[a]//50)+2):
                        blobnumber += 1
                        blobx.append(round(blobx[a]))
                        bloby.append(round(bloby[a]))
                        if random.randint(1, 100) <= blobmut[a]:
                            blobrep.append(round(blobrep[a] + random.randint(-2, 2)))
                        else:
                            blobrep.append(blobrep[a])
                        if random.randint(1, 100) <= blobmut[a]:
                            blobdie.append(round(blobdie[a] + random.randint(-2, 2)))
                        else:
                            blobdie.append(blobdie[a])
                        if random.randint(1, 100) <= blobmut[a]:
                            blobsize.append(round(blobsize[a] + random.randint(-10, 10)/10, 1))
                        else:
                            blobsize.append(blobsize[a])
                        if random.randint(1, 100) <= blobmut[a]:
                            blobmut.append(round(blobmut[a] + random.randint(-3, 3)))
                        else:
                            blobmut.append(blobmut[a])
                        blobdestx.append(random.randint(round(blobx[a] - 100), round(blobx[a] + 100)))
                        blobdesty.append(random.randint(round(bloby[a] - 100), round(bloby[a] + 100)))
                if random.randint(1, 100) <= blobdie[a]:
                    #die
                    die.append(a)
            #other limits
            for a in range(0, blobnumber):
                if blobx[a] > 1000 - blobsize[a]:
                    blobx[a] = 1000 - blobsize[a]
                if blobx[a] < blobsize[a]:
                    blobx[a] = blobsize[a]
                if bloby[a] > 1000 - blobsize[a]:
                    bloby[a] = 1000 - blobsize[a]
                if bloby[a] < blobsize[a]:
                    bloby[a] = blobsize[a]
                if blobmut[a] > 50:
                    blobmut[a] = 50
                if blobmut[a] < 10:
                    blobmut[a] = 10
                if blobrep[a] > 30:
                    blobrep[a] = 30
                if blobrep[a] < 5:
                    blobrep[a] = 5
                if blobdie[a] > 30:
                    blobdie[a] = 30
                if blobdie[a] < 5:
                    blobdie[a] = 5
                if blobsize[a] > 30:
                    blobsize[a] = 30
                if blobsize[a] < 10:
                    blobsize[a] = 10
                if blobdestx[a] > 1000 - blobsize[a]:
                    blobdestx[a] = 1000 - blobsize[a]
                if blobdestx[a] < blobsize[a]:
                    blobdestx[a] = blobsize[a]
                if blobdesty[a] > 1000 - blobsize[a]:
                    blobdesty[a] = 1000 - blobsize[a]
                if blobdesty[a] < blobsize[a]:
                    blobdesty[a] = blobsize[a]

    print(len(die))

    for b in range(0, len(die)):
        if len(die) != 0 and len(die) < round(carrycapacity/2):
            blobnumber -= 1
            del blobx[die[0]-b]
            del bloby[die[0]-b]
            del blobdestx[die[0]-b]
            del blobdesty[die[0]-b]
            del blobsize[die[0]-b]
            del blobmut[die[0]-b]
            del blobdie[die[0]-b]
            del blobrep[die[0]-b]
        if len(die) > round(carrycapacity/2)-1:
            for a in range(0, len(die)):
                if len(blobx) != 0:
                    blobnumber -= 1
                    del blobx[0]
                    del bloby[0]
                    del blobdestx[0]
                    del blobdesty[0]
                    del blobsize[0]
                    del blobmut[0]
                    del blobdie[0]
                    del blobrep[0]
            die = []
    die = []

    pygame.display.flip()
    clock.tick(100)