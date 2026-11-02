import pygame
import sys
import math

pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((1080, 540))

clok = 100

objx = [0, 500, 800, 2000]
objy = [10, 100, 400, 800]
realx = [0, 40, 3, 1]
realy = [410, 400, 1, 1]
objxx = [0, 3, 2, -2]
objyy = [0, -3, 0, -3]
objmass = [1000, 500, 2000, 5000]
objradius = [10, 0, 4, 1]
posx = 0
posy = 0
postx = 0
posty = 0
dragscreen = False
dragstart = True
dragstartx = 0
dragstarty = 0
mousedown = False
pathx = []
pathy = []
pathdel = []
zoom = 0.1
pathdelete = []

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    mousex, mousey = pygame.mouse.get_pos()

    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, (150, 150, 150), (980, 0, 100, 540))
    pygame.draw.rect(screen, (255, 50, 50), (980, 490, 50, 50))
    pygame.draw.rect(screen, (50, 50, 255), (1030, 490, 50, 50))
    pygame.draw.rect(screen, (50, 50, 255), (980, 440, 50, 50))
    pygame.draw.rect(screen, (255, 50, 50), (1030, 440, 50, 50))

    for blooby in range (0,len(objx)):
        for booby in range (0, len(objx)):
            if blooby != booby:
                objxx[blooby] += round(objmass[booby]*(objx[booby] - objx[blooby]) / 1000000, 2)
                objyy[blooby] += round(objmass[booby]*(objy[booby] - objy[blooby]) / 1000000, 2)

        objradius[blooby] = round(zoom * objmass[blooby] / 100)
        pygame.draw.circle(screen, (255, 255, 255), (round(zoom*(realx[blooby] + posx)),
                                                     round(zoom*(realy[blooby] + posy))), objradius[blooby])

        objx[blooby] += objxx[blooby]
        objy[blooby] += objyy[blooby]
        realx[blooby] = round(objx[blooby])
        realy[blooby] = round(objy[blooby])

    for laggy in range (0, len(pathx)):
        pygame.draw.rect(screen, (255, 255, 255), (pathx[laggy], pathy[laggy], 1, 1))
        pathdel[laggy] -= 1

    for laddy in range(0, len(pathx)):
        if pathdel[laddy] == 0:
            pathdelete.append(laddy)

    for sheep in range(0, len(pathdelete)):
        del(pathx[sheep])
        del(pathy[sheep])
        del(pathdel[sheep])

    pathdelete = []

    if event.type == pygame.MOUSEBUTTONDOWN:
        mousedown = True
        if 980<=mousex<=1080:
            if mousex<=1030:
                if 490<=mousey<=540:
                    zoom = round(1.01*zoom, 4)
            if mousex>1030:
                if 490<=mousey<=540:
                    zoom = round(0.99*zoom, 4)
            if mousex<=1030:
                if 440<=mousey<490:
                    clok = round(1.01*clok, 4)
            if mousex>1030:
                if 440<=mousey<490:
                    clok = round(0.99*clok, 4)
    else:
        for blooy in range(0, len(objx)):
            pathx.append(round(zoom*(realx[blooy] + posx)))
            pathy.append(round(zoom*(realy[blooy] + posy)))
            pathdel.append(500)
    if event.type == pygame.MOUSEBUTTONUP:
        mousedown = False

    if mousedown == False:
        dragscreen = False
        dragstart = True
    else:
        dragscreen = True

    if dragscreen == True:
        if dragstart == True:
            dragstartx = mousex
            dragstarty = mousey
            for blopy in range(0, len(objx)):
                realx[blopy] += posx
                realy[blopy] += posy
                postx = posx
                posty = posy
            dragstart = False
        posx = postx + (mousex - dragstartx)
        posy = posty + (mousey - dragstarty)

    pygame.display.flip()
    clock.tick(clok)
