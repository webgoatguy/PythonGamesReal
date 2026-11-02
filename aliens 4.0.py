win = False
leveltimer = 300
leveldelay = 20

import pygame
import sys
import random
import pickle
import math

pygame.init()

stars = 0
wait = 0

dietimer = 300

clock = pygame.time.Clock()

screen = pygame.display.set_mode((1080,540), pygame.FULLSCREEN)

#__________________________________________________________________________________________________Sound settings
gunsounds = False
minesounds = False
shotgunsounds = False

filename = 'pickles'
filename1 = 'pickles1'

highscorenorm = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

levels = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

quit = False

infile = open(filename,'rb')
highscorenorm = pickle.load(infile)
infile.close()

infile1 = open(filename1,'rb')
levels = pickle.load(infile1)
infile1.close()

if True:
    shipx = 540
    shipy = 450
    shipxx = 0
    shipyy = -3
    shiphit = 50
    bulletx = []
    bullety = []
    bulletxx = []
    bulletyy = []
    bulletdel = []
    bulletreload = 8
    bullshotdamage = 4
    shotgunacc = 60
    shotgunreload = 100
    shotgunbullets = 6
    ebulletx = []
    ebullety = []
    ebulletxx = []
    ebulletyy = []
    ebulletdel = []
    minex = []
    miney = []
    minedel = []
    miner = []
    mineradius = 150
    minedamage = 3
    mineshrapnel = 0
    lightning1x = []
    lightning1y = []
    lightning2x = []
    lightning2y = []
    lightningtimer = 0
    lightreload = 200
    lightdamage = 1
    eshipx = []
    eshipy = []
    eshipxx = []
    eshipyy = []
    eshipdel = []
    eshiphit = []
    eshiphitt = []
    eshiptype = []
    eshipsum = []
    eshipstuntimer = []
    lightstruck = []
    stopwatch = 0
    minetimer = 0
    shoottimer = 0
    shotguntimer = 0
    shoot = False
    dropmine = False
    aimturn = "?"
    aimturn1 = "?"
    score = 0
    alientimer = 0
    delay = [0, 0, 0, 0, 0, 0]
    slide = "main menu"
    coins = 1000
    upgradebullets = 1
    upgradeshotgun = 1
    upgradelasers = 1
    upgrademissiles = 1
    upgrademines = 1
    upgradelightning = 1
    laserx = []
    lasery = []
    laserxx = []
    laseryy = []
    laserdel = []
    laserreload = 60
    laserdamage = 3
    lasertimer = 0
    missilex = []
    missiley = []
    missilexx = []
    missileyy = []
    missiledel = []
    missilereload = 100
    missiledamage = 4
    missileradius = 100
    missileshrapnel = 0
    missiler = []
    missiletimer = 0
    level = "?"

font = pygame.font.Font("freesansbold.ttf", 30)
bigfont = pygame.font.Font("freesansbold.ttf", 130)

explosionsound = pygame.mixer.Sound("images/Explosion+3.wav")
gunsound = pygame.mixer.Sound("images/gun+silencer.wav")
shotgunsound = pygame.mixer.Sound("images/shotgun+2.wav")

mode = "medium"

level = "?"

def make_eship(x, y, xx, yy, hitpoints, type):
    eshipx.append(x)
    eshipy.append(y)
    eshipxx.append(xx)
    eshipyy.append(yy)
    eshipdel.append(1)
    eshiphit.append(hitpoints)
    eshiphitt.append(hitpoints)
    eshiptype.append(type)
    lightstruck.append(0)
    eshipsum.append(abs(xx) + abs(yy))
    eshipstuntimer.append(0)

leftclick = False
rightclick = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or quit == True:
            outfile = open(filename, 'wb')
            pickle.dump(highscorenorm, outfile)
            outfile.close()
            outfile1 = open(filename1, 'wb')
            pickle.dump(levels, outfile1)
            outfile1.close()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                aimturn = "right"
            if event.key == pygame.K_a:
                aimturn = "left"
            if event.key == pygame.K_LEFT:
                aimturn = "left"
            if event.key == pygame.K_RIGHT:
                aimturn = "right"
            if event.key == pygame.K_SPACE and slide == "upgrades":
                slide = "gameplay"
            elif event.key == pygame.K_SPACE and slide == "gameplay":
                slide = "upgrades"
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                aimturn = "?"
            if event.key == pygame.K_a:
                aimturn = "?"
            if event.key == pygame.K_LEFT:
                aimturn = "?"
            if event.key == pygame.K_RIGHT:
                aimturn = "?"

    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
            leftclick = True
        if event.button == 3:
            rightclick = True
    if event.type == pygame.MOUSEBUTTONUP:
        if event.button == 1:
            leftclick = False
        if event.button == 3:
            rightclick = False

    if leftclick == True:
        shoot = True
    else:
        shoot = False
    if rightclick == True:
        dropmine = True
    else:
        dropmine = False

    if lightningtimer <= 0:
        lightning1x = []
        lightning1y = []
        lightning2x = []
        lightning2y = []

    screen.fill((round(255 * (300 - dietimer)/300), round(255 * (300 - leveltimer)/300), 0))

    mousex, mousey = pygame.mouse.get_pos()

    #____________________________________________________________________________________________________________________________________________ Text
    quittext = font.render("Quit game", False, (255, 0, 0))
    scoretext0 = font.render("Score:", False, (255, 255, 255))
    scoretext = font.render(str(score), False, (255, 255, 255))
    cointext1 = font.render("Coins:", False, (255, 255, 255))
    stopwatchtext1 = font.render("Survived for", False, (255, 255, 255))
    stopwatchtext2 = font.render(str(stopwatch//6000), False, (255, 255, 255))
    stopwatchtext3 = font.render(":", False, (255, 255, 255))
    stopwatchtext4 = font.render(str(round((stopwatch/100)-(stopwatch//6000), 2)), False, (255, 255, 255))
    howtoplay1 = font.render("Press A or left arrow to turn left, D or right arrow to turn right", False, (255, 255, 255))
    howtoplay2 = font.render("Left click to shoot, right click to place mine", False, (255, 255, 255))
    howtoplay3 = font.render("Press space to switch between upgrades and gameplay", False, (255, 255, 255))
    highscorenormtext = font.render(str(highscorenorm[0]), False, (255, 255, 255))
    highscorenormtext1 = font.render("High score:", False, (255, 255, 255))
    highscorenormtext2 = font.render(str(highscorenorm[1]), False, (255, 255, 255))
    highscorenormtext4 = font.render(str(highscorenorm[2]), False, (255, 255, 255))
    highscorenormtext6 = font.render(str(highscorenorm[3]), False, (255, 255, 255))
    highscorenormtext8 = font.render(str(highscorenorm[4]), False, (255, 255, 255))
    highscorenormtext10 = font.render(str(highscorenorm[5]), False, (255, 255, 255))
    highscorenormtext12 = font.render(str(highscorenorm[6]), False, (255, 255, 255))
    highscorenormtext14 = font.render(str(highscorenorm[7]), False, (255, 255, 255))
    killcounter = font.render(str(highscorenorm[8]), False, (255, 255, 255))
    damagecounter = font.render(str(highscorenorm[9]), False, (255, 255, 255))
    moneycounter = font.render(str(highscorenorm[10]), False, (255, 255, 255))
    killcounter1 = font.render("Enemies killed:", False, (255, 255, 255))
    damagecounter1 = font.render("Damage dealt:", False, (255, 255, 255))
    moneycounter1 = font.render("Coins earned:", False, (255, 255, 255))
    cointext = font.render(str(coins), False, (255, 255, 255))
    bullet = font.render("Main gun:", False, (255, 255, 255))
    bullet2 = font.render("2 Shoots faster 150", False, (255, 255, 255))
    bullet3 = font.render("3 Bullets deal more damage (includes shotgun, shrapnel) 300", False, (255, 255, 255))
    bullet4 = font.render("4 Shoots from twin guns 500", False, (255, 255, 255))
    bullet5 = font.render("5 Bullets travel really fast 200", False, (255, 255, 255))
    bullet6 = font.render("6 Faster reload 400", False, (255, 255, 255))
    bullet7 = font.render("7 Shoots from triple guns 1000", False, (255, 255, 255))
    bullet8 = font.render("8 Bullets deal even more damage 1500", False, (255, 255, 255))
    bullet9 = font.render("9 Bullets can deflect enemy bullets 500", False, (255, 255, 255))
    shotgun = font.render("Shotgun:", False, (255, 255, 255))
    shotgun2 = font.render("2 More bullets per shot 200", False, (255, 255, 255))
    shotgun3 = font.render("3 Faster reload 200", False, (255, 255, 255))
    shotgun4 = font.render("4 More accuracy 50", False, (255, 255, 255))
    shotgun5 = font.render("5 Even more bullets per shot 500", False, (255, 255, 255))
    shotgun6 = font.render("6 Even faster reload 800", False, (255, 255, 255))
    shotgun7 = font.render("7 Bullets travel really fast 300", False, (255, 255, 255))
    shotgun8 = font.render("8 Even more bullets per shot 800", False, (255, 255, 255))
    shotgun9 = font.render("9 Bullets get knockback (includes main gun, shrapnel) 5000", False, (255, 255, 255))
    laser = font.render("Lasers:", False, (255, 255, 255))
    laser2 = font.render("2 Shoots faster 100", False, (255, 255, 255))
    laser3 = font.render("3 Shoots from twin guns 350", False, (255, 255, 255))
    laser4 = font.render("4 Lasers do more damage 200", False, (255, 255, 255))
    laser5 = font.render("5 Faster reload 300", False, (255, 255, 255))
    laser6 = font.render("6 Even faster reload 500", False, (255, 255, 255))
    laser7 = font.render("7 Lasers deal even more damage 800", False, (255, 255, 255))
    laser8 = font.render("8 Shoots from quadruple guns 1800", False, (255, 255, 255))
    laser9 = font.render("9 Ray of destruction 4500", False, (255, 255, 255))
    missile = font.render("Missiles:", False, (255, 255, 255))
    missile2 = font.render("2 Shoots faster 150", False, (255, 255, 255))
    missile3 = font.render("3 Bigger explosion 200", False, (255, 255, 255))
    missile4 = font.render("4 Explosions yield shrapnel 500", False, (255, 255, 255))
    missile5 = font.render("5 Two missiles every shot 1000", False, (255, 255, 255))
    missile6 = font.render("6 Even bigger explosion 700", False, (255, 255, 255))
    missile7 = font.render("7 Missiles travel much faster 200", False, (255, 255, 255))
    missile8 = font.render("8 Faster reload 1200", False, (255, 255, 255))
    missile9 = font.render("9 Gigantic explosion, more shrapnel pieces 2400", False, (255, 255, 255))
    mine = font.render("Mines:", False, (255, 255, 255))
    mine2 = font.render("2 Bigger blast 200", False, (255, 255, 255))
    mine3 = font.render("3 Explosions yield shrapnel 400", False, (255, 255, 255))
    mine4 = font.render("4 More damage towards enemies 400", False, (255, 255, 255))
    mine5 = font.render("5 Less damage from mines to your ship 600", False, (255, 255, 255))
    mine6 = font.render("6 Bigger explosion 500", False, (255, 255, 255))
    mine7 = font.render("7 More shrapnel 800", False, (255, 255, 255))
    mine8 = font.render("8 Gigantic explosion 1500", False, (255, 255, 255))
    mine9 = font.render("9 Much more damage 2000", False, (255, 255, 255))
    lightning = font.render("Lightning:", False, (255, 255, 255))
    lightning2 = font.render("2 More damage 300", False, (255, 255, 255))
    lightning3 = font.render("3 Faster reload 400", False, (255, 255, 255))
    lightning4 = font.render("4 Lightning spreads more easily 200", False, (255, 255, 255))
    lightning5 = font.render("5 Lightning can hit same ship twice 800", False, (255, 255, 255))
    lightning6 = font.render("6 Lightning stuns enemy ships 500", False, (255, 255, 255))
    lightning7 = font.render("7 Faster reload 1000", False, (255, 255, 255))
    lightning8 = font.render("8 More damage 1200", False, (255, 255, 255))
    lightning9 = font.render("9 Insane damage 3000", False, (255, 255, 255))
    maxupgrades = font.render("Max upgrades", False, (255, 255, 255))
    easy = font.render("Easy mode", False, (100, 255, 100))
    medium = font.render("Medium mode", False, (255, 255, 0))
    hard = font.render("Hard mode", False, (255, 150, 0))
    extreme = font.render("Extreme mode", False, (200, 0, 0))
    mainmenu = font.render("Main menu", False, (255, 255, 255))
    onelife = font.render("One life", False, (255, 255, 255))
    halfcash = font.render("Half cash", False, (255, 255, 255))
    explosions = font.render("Explosions only", False, (255, 255, 255))
    triplemode = font.render("Triple mode", False, (255, 255, 255))
    leveltext = font.render("Levels", False, (255, 255, 255))
    leveldonetext = bigfont.render("Level Completed", False, (0, 255, 0))

    if slide == "main menu":
        dietimer = 300
        leveltimer = 300
        if score > highscorenorm[0]:
            highscorenorm[0] = score
        if score > highscorenorm[1]:
            highscorenorm[1] = score
        if score > highscorenorm[2]:
            highscorenorm[2] = score
        if score > highscorenorm[3]:
            highscorenorm[3] = score
        if score > highscorenorm[4]:
            highscorenorm[4] = score
        if score > highscorenorm[5]:
            highscorenorm[5] = score
        if score > highscorenorm[6]:
            highscorenorm[6] = score
        if score > highscorenorm[7]:
            highscorenorm[7] = score
        screen.blit(highscorenormtext1, (300, 20))
        screen.blit(highscorenormtext, (480, 20))
        screen.blit(highscorenormtext1, (300, 50))
        screen.blit(highscorenormtext2, (480, 50))
        screen.blit(highscorenormtext1, (300, 80))
        screen.blit(highscorenormtext4, (480, 80))
        screen.blit(highscorenormtext1, (300, 110))
        screen.blit(highscorenormtext6, (480, 110))
        screen.blit(highscorenormtext1, (300, 140))
        screen.blit(highscorenormtext8, (480, 140))
        screen.blit(highscorenormtext1, (300, 170))
        screen.blit(highscorenormtext10, (480, 170))
        screen.blit(highscorenormtext1, (300, 200))
        screen.blit(highscorenormtext12, (480, 200))
        screen.blit(highscorenormtext1, (300, 230))
        screen.blit(highscorenormtext14, (480, 230))
        screen.blit(killcounter1, (20, 300))
        screen.blit(killcounter, (300, 300))
        screen.blit(damagecounter1, (20, 330))
        screen.blit(damagecounter, (300, 330))
        screen.blit(moneycounter1, (20, 360))
        screen.blit(moneycounter, (300, 360))
        screen.blit(howtoplay1, (20, 407))
        screen.blit(howtoplay2, (20, 437))
        screen.blit(howtoplay3, (20, 467))
        if event.type == pygame.MOUSEBUTTONDOWN and 20 < mousey < 50:
            mode = "easy"
            slide = "upgrades"
            delay = [20, 20, 20, 20, 20, 20]
        if event.type == pygame.MOUSEBUTTONDOWN and 50 < mousey < 80:
            mode = "medium"
            slide = "upgrades"
            delay = [20, 20, 20, 20, 20, 20]
        if event.type == pygame.MOUSEBUTTONDOWN and 80 < mousey < 110:
            mode = "hard"
            slide = "upgrades"
            delay = [20, 20, 20, 20, 20, 20]
        if event.type == pygame.MOUSEBUTTONDOWN and 110 < mousey < 140:
            mode = "extreme"
            slide = "upgrades"
            delay = [20, 20, 20, 20, 20, 20]
        if event.type == pygame.MOUSEBUTTONDOWN and 140 < mousey < 170:
            mode = "one life"
            slide = "upgrades"
            delay = [20, 20, 20, 20, 20, 20]
            shiphit = 1
        if event.type == pygame.MOUSEBUTTONDOWN and 170 < mousey < 200:
            mode = "half cash"
            slide = "upgrades"
            delay = [20, 20, 20, 20, 20, 20]
            coins = 500
        if event.type == pygame.MOUSEBUTTONDOWN and 200 < mousey < 230:
            mode = "explosions only"
            slide = "upgrades"
            delay = [20, 20, 20, 20, 20, 20]
        if event.type == pygame.MOUSEBUTTONDOWN and 230 < mousey < 260:
            mode = "triple"
            slide = "upgrades"
            delay = [20, 20, 20, 20, 20, 20]
        if event.type == pygame.MOUSEBUTTONDOWN and 260 < mousey < 290:
            slide = "levels"
            leveldelay = 20
        if event.type == pygame.MOUSEBUTTONDOWN and 510 < mousey < 540 and 25 < mousex < 180:
            quit = True
        screen.blit(quittext, (20, 510))
        screen.blit(easy, (20, 20))
        screen.blit(medium, (20, 50))
        screen.blit(hard, (20, 80))
        screen.blit(extreme, (20, 110))
        screen.blit(onelife, (20, 140))
        screen.blit(halfcash, (20, 170))
        screen.blit(explosions, (20, 200))
        screen.blit(triplemode, (20, 230))
        screen.blit(leveltext, (20, 260))

    if slide == "levels":
        leveldelay -= 1
        for cat in range(0, 10):
            for dog in range(0, 5):
                if levels[10*dog + cat] == 0:
                    pygame.draw.rect(screen, (255, 0, 0), (25 + cat * 105, 25 + 95 * dog, 50, 50))
                else:
                    pygame.draw.rect(screen, (0, 255, 0), (25 + cat * 105, 25 + 95 * dog, 50, 50))
                generaltext = font.render(str(10*dog + cat + 1), False, (255, 255, 255))
                screen.blit(generaltext, (34 + cat * 105, 37 + 95 * dog))
                if event.type == pygame.MOUSEBUTTONDOWN and cat + dog != 0:
                    if 30 + cat * 105 <= mousex <= 70 + cat * 105 and 30 + dog * 95 <= mousey <= 70 + dog * 95:
                        if leveldelay <= 0:
                            slide = "gameplay"
                            level = 10 * dog + cat + 1
                            delay = [20, 20, 20, 20, 20, 20]
                            stopwatch = 0
                if event.type == pygame.MOUSEBUTTONDOWN and cat + dog == 0:
                    if 30 <= mousex <= 70 and 30 <= mousey <= 70:
                        slide = "gameplay"
                        level = 1
                        delay = [20, 20, 20, 20, 20, 20]
        screen.blit(mainmenu, (410, 500))
        if event.type == pygame.MOUSEBUTTONDOWN and 410 < mousex < 560 and 500 < mousey < 540:
            slide = "main menu"

    #____________________________________________________________________________________________________________________________________________ screen is on upgrades
    if slide == "upgrades":
        for cat in range(0, 6):
            delay[cat] -= 1

        #____________________________________________________________________________________________________________________________________________ detecting clicking for upgrading
        if event.type == pygame.MOUSEBUTTONDOWN and 20 < mousey < 50 and delay[0] < 0:
            upgradebullets += 1
            delay[0] = 20
            if upgradebullets == 2:
                coins -= 150
                if coins < 0:
                    coins += 150
                    delay[0] = 0
                    upgradebullets -= 1
            if upgradebullets == 3:
                coins -= 300
                if coins < 0:
                    coins += 300
                    delay[0] = 0
                    upgradebullets -= 1
            if upgradebullets == 4:
                coins -= 500
                if coins < 0:
                    coins += 500
                    delay[0] = 0
                    upgradebullets -= 1
            if upgradebullets == 5:
                coins -= 200
                if coins < 0:
                    coins += 200
                    delay[0] = 0
                    upgradebullets -= 1
            if upgradebullets == 6:
                coins -= 400
                if coins < 0:
                    coins += 400
                    delay[0] = 0
                    upgradebullets -= 1
            if upgradebullets == 7:
                coins -= 1000
                if coins < 0:
                    coins += 1000
                    delay[0] = 0
                    upgradebullets -= 1
            if upgradebullets == 8:
                coins -= 1500
                if coins < 0:
                    coins += 1500
                    delay[0] = 0
                    upgradebullets -= 1
            if upgradebullets == 9:
                coins -= 500
                if coins < 0:
                    coins += 500
                    delay[0] = 0
                    upgradebullets -= 1
        if event.type == pygame.MOUSEBUTTONDOWN and 50 < mousey < 80 and delay[1] < 0:
            upgradeshotgun += 1
            delay[1] = 20
            if upgradeshotgun == 2:
                coins -= 200
                if coins < 0:
                    coins += 200
                    delay[0] = 0
                    upgradeshotgun -= 1
            if upgradeshotgun == 3:
                coins -= 200
                if coins < 0:
                    coins += 200
                    delay[0] = 0
                    upgradeshotgun -= 1
            if upgradeshotgun == 4:
                coins -= 50
                if coins < 0:
                    coins += 50
                    delay[0] = 0
                    upgradeshotgun -= 1
            if upgradeshotgun == 5:
                coins -= 500
                if coins < 0:
                    coins += 500
                    delay[0] = 0
                    upgradeshotgun -= 1
            if upgradeshotgun == 6:
                coins -= 800
                if coins < 0:
                    coins += 800
                    delay[0] = 0
                    upgradeshotgun -= 1
            if upgradeshotgun == 7:
                coins -= 300
                if coins < 0:
                    coins += 300
                    delay[0] = 0
                    upgradeshotgun -= 1
            if upgradeshotgun == 8:
                coins -= 800
                if coins < 0:
                    coins += 800
                    delay[0] = 0
                    upgradeshotgun -= 1
            if upgradeshotgun == 9:
                coins -= 5000
                if coins < 0:
                    coins += 5000
                    delay[0] = 0
                    upgradeshotgun -= 1
        if event.type == pygame.MOUSEBUTTONDOWN and 80 < mousey < 110 and delay[2] < 0:
            upgradelasers += 1
            delay[2] = 20
            if upgradelasers == 2:
                coins -= 100
                if coins < 0:
                    coins += 100
                    delay[0] = 0
                    upgradelasers -= 1
            if upgradelasers == 3:
                coins -= 350
                if coins < 0:
                    coins += 350
                    delay[0] = 0
                    upgradelasers -= 1
            if upgradelasers == 4:
                coins -= 200
                if coins < 0:
                    coins += 200
                    delay[0] = 0
                    upgradelasers -= 1
            if upgradelasers == 5:
                coins -= 300
                if coins < 0:
                    coins += 300
                    delay[0] = 0
                    upgradelasers -= 1
            if upgradelasers == 6:
                coins -= 500
                if coins < 0:
                    coins += 500
                    delay[0] = 0
                    upgradelasers -= 1
            if upgradelasers == 7:
                coins -= 800
                if coins < 0:
                    coins += 800
                    delay[0] = 0
                    upgradelasers -= 1
            if upgradelasers == 8:
                coins -= 1800
                if coins < 0:
                    coins += 1800
                    delay[0] = 0
                    upgradelasers -= 1
            if upgradelasers == 9:
                coins -= 4500
                if coins < 0:
                    coins += 4500
                    delay[0] = 0
                    upgradelasers -= 1
        if event.type == pygame.MOUSEBUTTONDOWN and 110 < mousey < 140 and delay[3] < 0:
            upgrademissiles += 1
            delay[3] = 20
            if upgrademissiles == 2:
                coins -= 150
                if coins < 0:
                    coins += 150
                    delay[0] = 0
                    upgrademissiles -= 1
            if upgrademissiles == 3:
                coins -= 200
                if coins < 0:
                    coins += 200
                    delay[0] = 0
                    upgrademissiles -= 1
            if upgrademissiles == 4:
                coins -= 500
                if coins < 0:
                    coins += 500
                    delay[0] = 0
                    upgrademissiles -= 1
            if upgrademissiles == 5:
                coins -= 1000
                if coins < 0:
                    coins += 1000
                    delay[0] = 0
                    upgrademissiles -= 1
            if upgrademissiles == 6:
                coins -= 700
                if coins < 0:
                    coins += 700
                    delay[0] = 0
                    upgrademissiles -= 1
            if upgrademissiles == 7:
                coins -= 200
                if coins < 0:
                    coins += 200
                    delay[0] = 0
                    upgrademissiles -= 1
            if upgrademissiles == 8:
                coins -= 1200
                if coins < 0:
                    coins += 1200
                    delay[0] = 0
                    upgrademissiles -= 1
            if upgrademissiles == 9:
                coins -= 2400
                if coins < 0:
                    coins += 2400
                    delay[0] = 0
                    upgrademissiles -= 1
        if event.type == pygame.MOUSEBUTTONDOWN and 140 < mousey < 170 and delay[4] < 0:
            upgrademines += 1
            delay[4] = 20
            if upgrademines == 2:
                coins -= 200
                if coins < 0:
                    coins += 200
                    delay[0] = 0
                    upgrademines -= 1
            if upgrademines == 3:
                coins -= 400
                if coins < 0:
                    coins += 400
                    delay[0] = 0
                    upgrademines -= 1
            if upgrademines == 4:
                coins -= 400
                if coins < 0:
                    coins += 400
                    delay[0] = 0
                    upgrademines -= 1
            if upgrademines == 5:
                coins -= 600
                if coins < 0:
                    coins += 600
                    delay[0] = 0
                    upgrademines -= 1
            if upgrademines == 6:
                coins -= 500
                if coins < 0:
                    coins += 500
                    delay[0] = 0
                    upgrademines -= 1
            if upgrademines == 7:
                coins -= 800
                if coins < 0:
                    coins += 800
                    delay[0] = 0
                    upgrademines -= 1
            if upgrademines == 8:
                coins -= 1500
                if coins < 0:
                    coins += 1500
                    delay[0] = 0
                    upgrademines -= 1
            if upgrademines == 9:
                coins -= 2000
                if coins < 0:
                    coins += 2000
                    delay[0] = 0
                    upgrademines -= 1
        if event.type == pygame.MOUSEBUTTONDOWN and 170 < mousey < 200 and delay[5] < 0:
            upgradelightning += 1
            delay[5] = 20
            if upgradelightning == 2:
                coins -= 300
                if coins < 0:
                    coins += 300
                    delay[0] = 0
                    upgradelightning -= 1
            if upgradelightning == 3:
                coins -= 400
                if coins < 0:
                    coins += 400
                    delay[0] = 0
                    upgradelightning -= 1
            if upgradelightning == 4:
                coins -= 200
                if coins < 0:
                    coins += 200
                    delay[0] = 0
                    upgradelightning -= 1
            if upgradelightning == 5:
                coins -= 800
                if coins < 0:
                    coins += 800
                    delay[0] = 0
                    upgradelightning -= 1
            if upgradelightning == 6:
                coins -= 500
                if coins < 0:
                    coins += 500
                    delay[0] = 0
                    upgradelightning -= 1
            if upgradelightning == 7:
                coins -= 1000
                if coins < 0:
                    coins += 1000
                    delay[0] = 0
                    upgradelightning -= 1
            if upgradelightning == 8:
                coins -= 1200
                if coins < 0:
                    coins += 1200
                    delay[0] = 0
                    upgradelightning -= 1
            if upgradelightning == 9:
                coins -= 3000
                if coins < 0:
                    coins += 3000
                    delay[0] = 0
                    upgradelightning -= 1
        if event.type == pygame.MOUSEBUTTONDOWN and 900 < mousex < 1050 and 500 < mousey < 540:
            if level == "?":
                if score > highscorenorm[0] and mode == "easy":
                    highscorenorm[0] = score
                if score > highscorenorm[1] and mode == "medium":
                    highscorenorm[1] = score
                if score > highscorenorm[2] and mode == "hard":
                    highscorenorm[2] = score
                if score > highscorenorm[3] and mode == "extreme":
                    highscorenorm[3] = score
                if score > highscorenorm[4] and mode == "one life":
                    highscorenorm[4] = score
                if score > highscorenorm[5] and mode == "half cash":
                    highscorenorm[5] = score
                if score > highscorenorm[6] and mode == "explosions only":
                    highscorenorm[6] = score
                if score > highscorenorm[7] and mode == "triple":
                    highscorenorm[7] = score
            shipx = 540
            shipy = 450
            shipxx = 0
            shipyy = -3
            shiphit = 50
            bulletx = []
            bullety = []
            bulletxx = []
            bulletyy = []
            bulletdel = []
            bulletreload = 8
            bullshotdamage = 4
            shotgunacc = 60
            shotgunreload = 100
            shotgunbullets = 6
            ebulletx = []
            ebullety = []
            ebulletxx = []
            ebulletyy = []
            ebulletdel = []
            minex = []
            miney = []
            minedel = []
            miner = []
            mineradius = 150
            minedamage = 3
            mineshrapnel = 0
            lightning1x = []
            lightning1y = []
            lightning2x = []
            lightning2y = []
            lightningtimer = 0
            lightreload = 200
            lightdamage = 1
            eshipx = []
            eshipy = []
            eshipxx = []
            eshipyy = []
            eshipdel = []
            eshiphit = []
            eshiphitt = []
            eshiptype = []
            eshipsum = []
            eshipstuntimer = []
            lightstruck = []
            stopwatch = 0
            minetimer = 0
            shoottimer = 0
            shotguntimer = 0
            shoot = False
            dropmine = False
            aimturn = "?"
            aimturn1 = "?"
            score = 0
            alientimer = 0
            delay = [0, 0, 0, 0, 0, 0]
            slide = "main menu"
            coins = 1000
            upgradebullets = 1
            upgradeshotgun = 1
            upgradelasers = 1
            upgrademissiles = 1
            upgrademines = 1
            upgradelightning = 1
            laserx = []
            lasery = []
            laserxx = []
            laseryy = []
            laserdel = []
            laserreload = 60
            laserdamage = 3
            lasertimer = 0
            missilex = []
            missiley = []
            missilexx = []
            missileyy = []
            missiledel = []
            missilereload = 100
            missiledamage = 4
            missileradius = 100
            missileshrapnel = 0
            missiler = []
            missiletimer = 0
            level = "?"

        #____________________________________________________________________________________________________________________________________________ Blitting text for upgrades
        screen.blit(cointext1, (450, 500))
        screen.blit(cointext, (550, 500))
        screen.blit(stopwatchtext1, (20, 500))
        screen.blit(stopwatchtext2, (210, 500))
        screen.blit(stopwatchtext3, (250, 500))
        screen.blit(stopwatchtext4, (260, 500))
        if mode == "easy":
            screen.blit(highscorenormtext1, (410, 470))
            screen.blit(highscorenormtext, (590, 470))
            screen.blit(easy, (20, 470))
        if mode == "medium":
            screen.blit(highscorenormtext1, (410, 470))
            screen.blit(highscorenormtext2, (590, 470))
            screen.blit(medium, (20, 470))
        if mode == "hard":
            screen.blit(highscorenormtext1, (410, 470))
            screen.blit(highscorenormtext4, (590, 470))
            screen.blit(hard, (20, 470))
        if mode == "extreme":
            screen.blit(highscorenormtext1, (410, 470))
            screen.blit(highscorenormtext6, (590, 470))
            screen.blit(extreme, (20, 470))
        if mode == "one life":
            screen.blit(highscorenormtext1, (410, 470))
            screen.blit(highscorenormtext8, (590, 470))
            screen.blit(onelife, (20, 470))
        if mode == "half cash":
            screen.blit(highscorenormtext1, (410, 470))
            screen.blit(highscorenormtext10, (590, 470))
            screen.blit(halfcash, (20, 470))
        if mode == "explosions only":
            screen.blit(highscorenormtext1, (410, 470))
            screen.blit(highscorenormtext12, (590, 470))
            screen.blit(explosions, (20, 470))
        if mode == "triple":
            screen.blit(highscorenormtext1, (410, 470))
            screen.blit(highscorenormtext14, (590, 470))
            screen.blit(triplemode, (20, 470))
        screen.blit(bullet, (20, 20))
        screen.blit(shotgun, (20, 50))
        screen.blit(laser, (20, 80))
        screen.blit(missile, (20, 110))
        screen.blit(mine, (20, 140))
        screen.blit(lightning, (20, 170))
        screen.blit(mainmenu, (900, 500))
        if upgradebullets == 1:
            screen.blit(bullet2, (180, 20))
        if upgradebullets == 2:
            screen.blit(bullet3, (180, 20))
            bulletreload = 6
        if upgradebullets == 3:
            screen.blit(bullet4, (180, 20))
            bullshotdamage = 5
        if upgradebullets == 4:
            screen.blit(bullet5, (180, 20))
        if upgradebullets == 5:
            screen.blit(bullet6, (180, 20))
        if upgradebullets == 6:
            screen.blit(bullet7, (180, 20))
            bulletreload = 4
        if upgradebullets == 7:
            screen.blit(bullet8, (180, 20))
        if upgradebullets == 8:
            screen.blit(bullet9, (180, 20))
            bullshotdamage = 8
        if upgradebullets >= 9:
            screen.blit(maxupgrades, (180, 20))
            upgradebullets = 9
        if upgradeshotgun == 1:
            screen.blit(shotgun2, (180, 50))
        if upgradeshotgun == 2:
            screen.blit(shotgun3, (180, 50))
            shotgunbullets = 9
        if upgradeshotgun == 3:
            screen.blit(shotgun4, (180, 50))
            shotgunreload = 75
        if upgradeshotgun == 4:
            screen.blit(shotgun5, (180, 50))
            shotgunacc = 30
        if upgradeshotgun == 5:
            screen.blit(shotgun6, (180, 50))
            shotgunbullets = 15
        if upgradeshotgun == 6:
            screen.blit(shotgun7, (180, 50))
            shotgunreload = 50
        if upgradeshotgun == 7:
            screen.blit(shotgun8, (180, 50))
        if upgradeshotgun == 8:
            screen.blit(shotgun9, (180, 50))
            shotgunbullets = 30
        if upgradeshotgun >= 9:
            screen.blit(maxupgrades, (180, 50))
        if upgradelasers == 1:
            screen.blit(laser2, (180, 80))
        if upgradelasers == 2:
            screen.blit(laser3, (180, 80))
            laserreload = 45
        if upgradelasers == 3:
            screen.blit(laser4, (180, 80))
        if upgradelasers == 4:
            screen.blit(laser5, (180, 80))
            laserdamage = 4
        if upgradelasers == 5:
            screen.blit(laser6, (180, 80))
            laserreload = 30
        if upgradelasers == 6:
            screen.blit(laser7, (180, 80))
            laserreload = 20
        if upgradelasers == 7:
            screen.blit(laser8, (180, 80))
            laserdamage = 6
        if upgradelasers == 8:
            screen.blit(laser9, (180, 80))
        if upgradelasers >= 9:
            screen.blit(maxupgrades, (180, 80))
        if upgrademissiles == 1:
            screen.blit(missile2, (180, 110))
        if upgrademissiles == 2:
            screen.blit(missile3, (180, 110))
            missilereload = 75
        if upgrademissiles == 3:
            screen.blit(missile4, (180, 110))
            missileradius = 200
        if upgrademissiles == 4:
            screen.blit(missile5, (180, 110))
            missileshrapnel = 20
        if upgrademissiles == 5:
            screen.blit(missile6, (180, 110))
        if upgrademissiles == 6:
            screen.blit(missile7, (180, 110))
            missileradius = 280
        if upgrademissiles == 7:
            screen.blit(missile8, (180, 110))
        if upgrademissiles == 8:
            screen.blit(missile9, (180, 110))
            missilereload = 45
        if upgrademissiles >= 9:
            screen.blit(maxupgrades, (180, 110))
            missileradius = 375
            missileshrapnel = 60
        if upgrademines == 1:
            screen.blit(mine2, (180, 140))
        if upgrademines == 2:
            screen.blit(mine3, (180, 140))
            mineradius = 240
        if upgrademines == 3:
            screen.blit(mine4, (180, 140))
            mineshrapnel = 20
        if upgrademines == 4:
            screen.blit(mine5, (180, 140))
            minedamage = 4
        if upgrademines == 5:
            screen.blit(mine6, (180, 140))
        if upgrademines == 6:
            screen.blit(mine7, (180, 140))
            mineradius = 330
        if upgrademines == 7:
            screen.blit(mine8, (180, 140))
            mineshrapnel = 60
        if upgrademines == 8:
            screen.blit(mine9, (180, 140))
            mineradius = 500
        if upgrademines >= 9:
            screen.blit(maxupgrades, (180, 140))
            minedamage = 7
        if upgradelightning == 1:
            screen.blit(lightning2, (180, 170))
        if upgradelightning == 2:
            screen.blit(lightning3, (180, 170))
            lightdamage = 1.6
        if upgradelightning == 3:
            screen.blit(lightning4, (180, 170))
            lightreload = 135
        if upgradelightning == 4:
            screen.blit(lightning5, (180, 170))
        if upgradelightning == 5:
            screen.blit(lightning6, (180, 170))
        if upgradelightning == 6:
            screen.blit(lightning7, (180, 170))
        if upgradelightning == 7:
            screen.blit(lightning8, (180, 170))
            lightreload = 75
        if upgradelightning == 8:
            screen.blit(lightning9, (180, 170))
            lightdamage = 3
        if upgradelightning >= 9:
            screen.blit(maxupgrades, (180, 170))

    if slide == "gameplay":
        alientimer -= 1

        if shiphit > 0:
            score += 1

        if level == 1:
            mode = "medium"
            coins = 0
            upgradebullets = 9
            upgradelasers = 9
            if stopwatch == 0:
                make_eship(0, 0, 1, 1, 250, "splitttttttt")
            if len(eshipx) == 0 and shiphit > 0:
                if shiphit > 0:
                    levels[0] = 1
                win = True

        if level == 2:
            mode = "medium"
            for cat in range(0, 50):
                if stopwatch == cat * 30:
                    make_eship(270, 0, 3, 0, 10, "splitttt")
            if stopwatch == 0:
                coins = 10000
            if len(eshipx) == 0 and stopwatch >= 1500:
                if shiphit > 0:
                    levels[1] = 1
                win = True

        if level == 3:
            coins = 0
            mode = "triple"
            if stopwatch == 0:
                make_eship(0, 270, 2, 0, 25, "splittttt")
            if len(eshipx) == 0:
                if shiphit > 0:
                    levels[2] = 1
                win = True

        if level == 4:
            mode = "medium"
            coins = 0
            mode = "explosions only"
            if stopwatch == 0:
                make_eship(1080, 270, -3, 0, 100, "splitttttttt")
            if len(eshipx) == 0:
                if shiphit > 0:
                    levels[3] = 1
                win = True

        if level == 5:
            coins = 10000000
            mode = "triple"
            if stopwatch == 0:
                make_eship(1080, 270, 1, 0, 100, "splittttttt")
            if len(eshipx) == 0:
                if shiphit > 0:
                    levels[4] = 1
                win = True

        if level == 6:
            mode = "medium"
            if stopwatch == 0:
                make_eship(1080, 270, -5, 0, 100, "splitt")
                shiphit = 3
                mode = "one life"
            if len(eshipx) == 0:
                if shiphit > 0:
                    levels[5] = 1
                win = True


        if level == 7:
            mode = "medium"
            coins = 8000
            if stopwatch == 0:
                make_eship(1080, 540, -1, 0, 100, "splitttttttt")
                make_eship(1080, 540, -1, 0, 100, "splitttttttt")
                make_eship(1080, 540, -1, 0, 100, "splitttttttt")
                make_eship(1080, 540, -1, 0, 100, "splitttttttt")
                shiphit = 10
            if len(eshipx) == 0:
                win = True
                if shiphit > 0:
                    levels[6] = 1

        if level == 8:
            mode = "medium"
            if stopwatch == 0:
                make_eship(1080, 540, -10, 0, 100, "splittttt")
                make_eship(1080, 540, -10, 0, 100, "splitttttt")
                make_eship(1080, 540, -10, 0, 100, "splittttttt")
                make_eship(1080, 540, -10, 0, 100, "splitttttttt")
                shiphit = 12
                coins = 5000
            if len(eshipx) == 0:
                if shiphit > 0:
                    levels[7] = 1
                win = True

        if level == 9:
            coins = 0
            mode = "explosions only"
            if stopwatch == 0:
                make_eship(1080, 540, -10, 0, 100, "splitttttttt")
            if len(eshipx) == 0:
                if shiphit > 0:
                    levels[8] = 1
                win = True

        if level == 10:
            mode = "medium"
            if stopwatch == 0:
                make_eship(1080, 540, -30, 0, 100, "splitttttttt")
                shiphit = 15
                coins = 10000
            if len(eshipx) == 0:
                if shiphit > 0:
                    levels[9] = 1
                win = True


        if level == 11:
            coins = 0
            mode = "triple"
            if stopwatch == 0:
                make_eship(1080, 540, -1, 1, 100, "splittttt")
                shiphit = 20
            if len(eshipx) == 0:
                if shiphit > 0:
                    levels[10] = 1
                win = True


        if level == 12:
            for cat in range(0, 20):
                if stopwatch == cat * 100:
                    make_eship(270, 0, 5, 0, 10, "splitttttt")
            if stopwatch == 0:
                coins = 15000
                mode = "medium"
            if len(eshipx) == 0 and stopwatch >= 2000:
                if shiphit > 0:
                    levels[11] = 1
                win = True

        if level == 13:
            for cat in range(0, 20):
                if stopwatch == cat:
                    make_eship(270, 0, 5, 0, 10, "splittt")
            if stopwatch == 0:
                coins = 1000
                shiphit = 10
                mode = "extreme"
            if len(eshipx) == 0 and stopwatch >= 20:
                if shiphit > 0:
                    levels[12] = 1
                win = True

        if level == 14:
            for cat in range(0, 20):
                if stopwatch == cat * 5:
                    make_eship(0, 0, 5, 5, 10, "splittttt")
            if stopwatch == 0:
                coins = 15000
                mode = "easy"
            if len(eshipx) == 0 and stopwatch >= 100:
                if shiphit > 0:
                    levels[13] = 1
                win = True

        if level == 15:
            if stopwatch == 0:
                make_eship(1080, 270, -5, 0, 100, "splittt")
                shiphit = 2
                mode = "one life"
            if len(eshipx) == 0:
                if shiphit > 0:
                    levels[14] = 1
                win = True

        if level == 16:
            if stopwatch == 0:
                make_eship(1080, 270, -10, 0, 60, "splitt")
                make_eship(1080, 270, -10, 0, 50, "splitt")
                make_eship(1080, 270, -10, 0, 75, "splitt")
                shiphit = 5
                mode = "one life"
            if len(eshipx) == 0:
                if shiphit > 0:
                    levels[15] = 1
                win = True

        if level == 17:
            for cat in range(0, 20):
                if stopwatch == cat * 5:
                    make_eship(0, 0, stopwatch / 40, stopwatch / 40, stopwatch, "splitttt")
            if stopwatch == 0:
                coins = 2000
                mode = "easy"
            if len(eshipx) == 0 and stopwatch >= 100:
                if shiphit > 0:
                    levels[16] = 1
                win = True

        if level == 18:
            for cat in range(0, 2):
                if stopwatch == cat * 5:
                    make_eship(0, 0, stopwatch / 40, stopwatch / 40, stopwatch, "splitttttttt")
            if stopwatch == 0:
                coins = 2000
                mode = "easy"
            if len(eshipx) == 0 and stopwatch >= 100:
                if shiphit > 0:
                    levels[17] = 1
                win = True

        if level == 19:
            mode = "medium"
            for cat in range(0, 2):
                if stopwatch == cat * 5:
                    make_eship(0, 0, 5, 5, 10, "splitttt")
            if stopwatch == 0:
                coins = 2000
                shiphit = 2
                mode = "one life"
            if len(eshipx) == 0 and stopwatch >= 100:
                if shiphit > 0:
                    levels[18] = 1
                win = True


        if level == 20:
            mode = "medium"
            for cat in range(0, 50):
                if stopwatch == cat * 30:
                    make_eship(270, 0, 3, 0, 10, "splitttttt")
            if stopwatch == 0:
                coins = 15000
            if len(eshipx) == 0 and stopwatch >= 1500:
                if shiphit > 0:
                    levels[19] = 1
                win = True


        if level == 21:
            mode = "medium"
            for cat in range(0, 20):
                if stopwatch == cat * 100:
                    make_eship(0, 6, 6, 0, 10, "splittttt")
            if stopwatch == 0:
                coins = 1000
            if len(eshipx) == 0 and stopwatch >= 2000:
                if shiphit > 0:
                    levels[20] = 1
                win = True


        if level == 22:
            coins = 0
            mode = "explosions only"
            if stopwatch == 0:
                make_eship(1080, 540, -6, 0, 30, "splitttttt")
                make_eship(1080, 540, -6, 0, 20, "splitttttt")
                make_eship(1080, 540, -6, 0, 10, "splitttttt")
                make_eship(1080, 540, -6, 0, 40, "splitttttt")
                make_eship(1080, 540, -6, 0, 50, "splitttttt")
                make_eship(1080, 540, -6, 0, 60, "splitttttt")
            if len(eshipx) == 0:
                if shiphit > 0:
                    levels[21] = 1
                win = True


        if level == 23:
            mode = "one life"
            if stopwatch == 0:
                make_eship(0, 0, 1, 1, 1, "splitttttt")
                make_eship(0, 0, 1, 1, 1, "splittttt")
                shiphit = 1
            if len(eshipx) == 0 and shiphit > 0:
                if shiphit > 0:
                    levels[22] = 1
                win = True


        if level == 24:
            mode = "one life"
            if stopwatch == 0:
                for cat in range(0, 49):
                    make_eship(0, 0, 0.8, 0.4, 1, "split")
                shiphit = 0.01
                stopwatch = 4500
            if len(eshipx) == 0 and shiphit > 0:
                if shiphit > 0:
                    levels[23] = 1
                win = True

        if level == 25:
            mode = "triple"
            if stopwatch == 0:
                make_eship(0, 0, 3, 3, 1000, "split")
                make_eship(0, 0, 3, 3, 1000, "split")
                make_eship(0, 0, 3, 3, 1000, "split")
                make_eship(0, 0, 3, 3, 1000, "split")
                coins = 5000
                shiphit = 10
            if len(eshipx) == 0 and shiphit > 0:
                if shiphit > 0:
                    levels[24] = 1
                win = True

        if level == 26:
            mode = "one life"
            if stopwatch == 0:
                make_eship(0, 0, 10, 10, 300, "split")
                coins = 10000
                shiphit = 1
            if len(eshipx) == 0 and shiphit > 0:
                if shiphit > 0:
                    levels[25] = 1
                win = True

        if level == 27:
            mode = "one life"
            if stopwatch == 0:
                make_eship(0, 0, 1, 1, 300, "splitttttt")
                coins = 10000
                shiphit = 1
            if len(eshipx) == 0 and shiphit > 0:
                if shiphit > 0:
                    levels[26] = 1
                win = True

        if level == 28:
            upgrademissiles = 9
            mode = "one life"
            if stopwatch == 0:
                make_eship(0, 0, 1, 1, 1000, "splitttttttt")
                shiphit = 8
            if len(eshipx) == 0 and shiphit > 0:
                if shiphit > 0:
                    levels[27] = 1
                win = True

        if level == 29:
            mode = "one life"
            if stopwatch == 0:
                make_eship(0, 0, 1, 1, 400, "splittttttt")
                shiphit = 1
                coins = 12000
            if len(eshipx) == 0 and shiphit > 0:
                if shiphit > 0:
                    levels[28] = 1
                win = True

        if level == 30:
            mode = "medium"
            for cat in range(0, 50):
                if stopwatch == cat * 30:
                    make_eship(270, 0, 4, 0, 10, "splittttt")
            if stopwatch == 0:
                coins = 8000
            if len(eshipx) == 0 and stopwatch >= 1500:
                if shiphit > 0:
                    levels[29] = 1
                win = True

        if level == 31:
            mode = "extreme"
            if stopwatch == 0:
                make_eship(0, 0, 1, 1, 100, "splitttttttt")
                make_eship(0, 0, 1, 1, 100, "splittttttt")
                make_eship(0, 0, 1, 1, 100, "splitttttt")
                make_eship(0, 0, 1, 1, 100, "splittttt")
                make_eship(0, 0, 1, 1, 100, "splitttt")
                make_eship(0, 0, 1, 1, 100, "splittt")
                make_eship(0, 0, 1, 1, 100, "splitt")
                make_eship(0, 0, 1, 1, 100, "split")
                make_eship(0, 0, 1, 1, 100, "norm")
                coins = 9000
            if len(eshipx) == 0 and shiphit > 0:
                if shiphit > 0:
                    levels[30] = 1
                win = True

        if level == 32:
            mode = "triple"
            if stopwatch == 0:
                make_eship(0, 0, 1, 1, 100, "splitttttttt")
                coins = 8000
            if len(eshipx) == 0 and shiphit > 0:
                if shiphit > 0:
                    levels[31] = 1
                win = True

        if level == 33:
            mode = "medium"
            if stopwatch == 0:
                make_eship(0, 0, 2, 2, 100, "splitttttttt")
                make_eship(0, 0, 3, 3, 11, "norm")
                make_eship(0, 0, 3, 3, 11, "norm")
                make_eship(0, 0, 3, 3, 11, "norm")
                make_eship(0, 0, 3, 3, 11, "norm")
                make_eship(0, 0, 3, 3, 11, "norm")
                make_eship(0, 0, 3, 3, 11, "norm")
                make_eship(0, 0, 3, 3, 11, "norm")
                make_eship(0, 0, 3, 3, 11, "norm")
                make_eship(0, 0, 3, 3, 11, "norm")
                make_eship(0, 0, 3, 3, 11, "norm")
                make_eship(0, 0, 3, 3, 11, "norm")
                make_eship(0, 0, 3, 3, 11, "norm")
                make_eship(0, 0, 3, 3, 11, "norm")
                make_eship(0, 0, 3, 3, 11, "norm")
                make_eship(0, 0, 3, 3, 11, "norm")
                coins = 2000
                shiphit = 30
            if len(eshipx) == 0 and shiphit > 0:
                if shiphit > 0:
                    levels[32] = 1
                win = True

        if level == 34:
            mode = "medium"
            upgradelasers = 9
            if stopwatch == 0:
                make_eship(0, 0, 1, 1, 1000, "splitttttttt")
                make_eship(0, 0, 1, 1, 1000, "splitttttttt")
                make_eship(0, 0, 1, 1, 1000, "splitttttttt")
                make_eship(0, 0, 1, 1, 1000, "splitttttttt")
                coins = 0
            if len(eshipx) == 0 and shiphit > 0:
                if shiphit > 0:
                    levels[33] = 1
                win = True

        if level == 35:
            mode = "medium"
            if stopwatch == 0:
                make_eship(0, 0, 1, 1, 100, "splitttttttt")
                make_eship(220, 0, 1, 1, 100, "splitttttttt")
                make_eship(330, 0, 1, 1, 100, "splitttttttt")
                make_eship(550, 0, 1, 1, 100, "splitttttttt")
                make_eship(770, 0, 1, 1, 100, "splitttttttt")
                make_eship(880, 0, 1, 1, 100, "splitttttttt")
                make_eship(0, 110, 1, 1, 100, "splitttttttt")
                make_eship(0, 330, 1, 1, 100, "splitttttttt")
                make_eship(0, 440, 1, 1, 100, "splitttttttt")
                coins = 10000
            if len(eshipx) == 0 and shiphit > 0:
                if shiphit > 0:
                    levels[34] = 1
                win = True

        if level == 36:
            mode = "extreme"
            if stopwatch == 0:
                make_eship(0, 0, 1, 1, 100, "splitttttttt")
                make_eship(0, 0, 1, 1, 100, "split")
                make_eship(0, 0, 1, 1, 100, "splitt")
                make_eship(0, 0, 1, 1, 100, "split")
                make_eship(0, 0, 1, 1, 100, "splitttt")
                make_eship(0, 0, 1, 1, 100, "splittt")
                make_eship(0, 0, 1, 1, 100, "splitttt")
                make_eship(0, 0, 1, 1, 100, "splitt")
                make_eship(0, 0, 1, 1, 100, "splitttt")
                make_eship(0, 0, 1, 1, 100, "split")
                make_eship(0, 0, 1, 1, 100, "splitt")
                make_eship(0, 0, 1, 1, 100, "splitt")
                make_eship(0, 0, 1, 1, 100, "splitt")
                make_eship(0, 0, 1, 1, 100, "splittttt")
                make_eship(0, 0, 1, 1, 100, "splittt")
                make_eship(0, 0, 1, 1, 100, "splitttt")
                coins = 3000
            if len(eshipx) == 0 and shiphit > 0:
                if shiphit > 0:
                    levels[35] = 1
                win = True

        if level == 37:
            mode = "hard"
            if stopwatch == 0:
                make_eship(540, 270, 0, 0, 1000, "splitttttttt")
            if len(eshipx) >= 1:
                if eshiptype[0] == "splitttttttt":
                    eshipxx[0] = 0
                    eshipyy[0] = 0
                    eshipx[0] = 540
                    eshipy[0] = 270
                if eshiptype[0] == "splitttttttt" and (stopwatch % 180) == 0:
                    make_eship(500, 230, -1, -1, 10, "splittt")
                    make_eship(500, 310, -1, 1, 10, "splittt")
                    make_eship(580, 230, 1, -1, 10, "splittt")
                    make_eship(580, 310, 1, 1, 10, "splittt")
            if len(eshipx) == 0 and shiphit > 0:
                if shiphit > 0:
                    levels[36] = 1
                win = True

        if level == 38:
            mode = "medium"
            if stopwatch == 0:
                make_eship(540, 270, 0, 0, 2000, "splitttttttt")
            if len(eshipx) == 0 and shiphit > 0:
                if shiphit > 0:
                    levels[37] = 1
                win = True

        if level == 39:
            mode = "triple"
            if stopwatch == 0:
                make_eship(540, 270, 0, 0, 300, "splitttttttt")
            if len(eshipx) >= 1:
                if eshiptype[0] == "splitttttttt":
                    eshipxx[0] = 0
                    eshipyy[0] = 0
                    eshipx[0] = 540
                    eshipy[0] = 270
                if eshiptype[0] == "splitttttttt" and (stopwatch % 10) == 0:
                    make_eship(540, 270, random.randint(-5, 5)/10, random.randint(-5, 5)/10, 20, "norm")
            if len(eshipx) == 0 and shiphit > 0:
                if shiphit > 0:
                    levels[38] = 1
                win = True

        if level == 40:
            mode = "one life"
            if stopwatch == 0:
                for cat in range(0, 49):
                    make_eship(0, 0, 0.8, 0.4, 1, "split")
                shiphit = 0.01
                stopwatch = 4000
            if len(eshipx) == 0 and shiphit > 0:
                if shiphit > 0:
                    levels[39] = 1
                win = True

        if level == 41:
            mode = "medium"
            for cat in range(0, 50):
                if stopwatch == cat * 5:
                    make_eship(0, 0, 6, 6, 10, "splittttt")
            if stopwatch == 0:
                coins = 15000
            if len(eshipx) == 0 and stopwatch >= 250:
                if shiphit > 0:
                    levels[40] = 1
                win = True

        if level == 42:
            mode = "triple"
            if stopwatch == 0:
                make_eship(0, 0, 1, 1, 100, "splittttttt")
                make_eship(0, 0, 1, 1, 100, "splittttttt")
                make_eship(0, 0, 1, 1, 100, "splittttttt")
                make_eship(0, 0, 1, 1, 100, "splitttttt")
                make_eship(0, 0, 1, 1, 100, "splittttt")
                make_eship(0, 0, 1, 1, 100, "splitttt")
                make_eship(0, 0, 1, 1, 100, "splittt")
                make_eship(0, 0, 1, 1, 100, "splitt")
                make_eship(0, 0, 1, 1, 100, "split")
                make_eship(0, 0, 1, 1, 100, "norm")
                coins = 9000
            if len(eshipx) == 0 and shiphit > 0:
                if shiphit > 0:
                    levels[41] = 1
                win = True

        if level == 43:
            mode = "triple"
            if len(minex) >= 10:
                minedel[0] = 0
            if stopwatch == 0:
                make_eship(540, 270, 0, 0, 300, "splitttttttt")
                shiphit = 100
            if len(eshipx) >= 1:
                if eshiptype[0] == "splitttttttt":
                    eshipxx[0] = 0
                    eshipyy[0] = 0
                    eshipx[0] = 540
                    eshipy[0] = 270
                if eshiptype[0] == "splitttttttt" and (stopwatch % 50) == 0:
                    make_eship(500, 230, -5, -5, 10, "norm")
                    make_eship(500, 310, -5, 5, 10, "norm")
                    make_eship(580, 230, 5, -5, 10, "norm")
                    make_eship(580, 310, 5, 5, 10, "norm")
            if len(eshipx) == 0 and shiphit > 0:
                if shiphit > 0:
                    levels[42] = 1
                win = True

        if level == 44:
            mode = "hard"
            for cat in range(0, 75):
                if stopwatch == cat * 20:
                    make_eship(270, 0, 6, 0, 10, "splittttt")
            if stopwatch == 0:
                coins = 6000
                shiphit = 80
            if len(eshipx) == 0 and stopwatch >= 1500:
                if shiphit > 0:
                    levels[43] = 1
                win = True

        if level == 45:
            mode = "one life"
            if stopwatch == 0:
                for cat in range(0, 49):
                    make_eship(0, 0, 0.8, 0.4, 1, "split")
                shiphit = 0.01
                stopwatch = 3000
            if len(eshipx) == 0 and shiphit > 0:
                if shiphit > 0:
                    levels[44] = 1
                win = True

        if level == 46:
            coins = 0
            mode = "explosions only"
            if stopwatch == 0:
                make_eship(0, 0, 4, 3, 110, "splitttttttt")
                make_eship(0, 0, 3, 3, 95, "splittttttt")
                make_eship(0, 0, 2, 5, 80, "splitttttt")
                make_eship(0, 0, 3, 3, 60, "splittttt")
                make_eship(0, 0, 1, 6, 40, "splitttt")
                make_eship(0, 0, 3, 5, 22, "splittt")
                make_eship(0, 0, 4, 3, 12, "splitt")
                make_eship(0, 0, 2, 4, 8, "split")
                make_eship(0, 0, 1, 5, 4, "norm")
            if len(eshipx) == 0:
                if shiphit > 0:
                    levels[45] = 1
                win = True

        if level == 47:
            mode = "medium"
            coins = 0
            upgradebullets = 8
            if stopwatch == 0:
                make_eship(0, 0, 1, 1, 1000, "splitttttttt")
                make_eship(0, 0, 1, 1, 1000, "splitttttttt")
                make_eship(0, 0, 1, 1, 1000, "splitttttttt")
            stopwatch += 1
            if len(eshipx) == 0 and shiphit > 0:
                if shiphit > 0:
                    levels[46] = 1
                win = True

        if level == 48:
            mode = "medium"
            coins = 0
            shiphit -= 0.1
            if stopwatch == 0:
                make_eship(0, 0, 10, 10, 1, "splitttttttt")
            stopwatch += 1
            if len(eshipx) == 0 and shiphit > 0:
                if shiphit > 0:
                    levels[47] = 1
                win = True

        if level == 49:
            mode = "triple"
            if stopwatch == 0:
                make_eship(1080, 540, -6, 0, 1, "splitttttttt")
                make_eship(1080, 540, -6, 0, 10, "splitttttt")
                make_eship(1080, 540, -6, 0, 10, "splitttttt")
                make_eship(1080, 540, -6, 0, 100, "splitttt")
                make_eship(1080, 540, -6, 0, 100, "splitttt")
                make_eship(1080, 540, -6, 0, 100, "splitttt")
                make_eship(1080, 540, -6, 0, 100, "splitttt")
                make_eship(1080, 540, -6, 0, 1000, "splitt")
                make_eship(1080, 540, -6, 0, 1000, "splitt")
                make_eship(1080, 540, -6, 0, 1000, "splitt")
                make_eship(1080, 540, -6, 0, 1000, "splitt")
                make_eship(1080, 540, -6, 0, 1000, "splitt")
                make_eship(1080, 540, -6, 0, 1000, "splitt")
                make_eship(1080, 540, -6, 0, 1000, "splitt")
                make_eship(1080, 540, -6, 0, 1000, "splitt")
                shiphit = 120
            stopwatch = 1
            if len(eshipx) == 0:
                if shiphit > 0:
                    levels[48] = 1
                win = True

        if level == 50:
            coins = 0
            mode = "one life"
            if stopwatch == 0:
                make_eship(0, 0, 1, 1, 1, "splitttttttt")
                make_eship(0, 0, 1, 1, 10, "splitttttttt")
                make_eship(0, 0, 1, 1, 100, "splitttttttt")
                shiphit = 1
            stopwatch += 4
            if len(eshipx) == 0 and shiphit > 0:
                if shiphit > 0:
                    levels[49] = 1
                win = True

        if level != "?" and win == True:
            leveltimer -= 1
            screen.blit(leveldonetext, (20, 150))

        if leveltimer == 0:
            shipx = 540
            shipy = 450
            shipxx = 0
            shipyy = -3
            shiphit = 50
            bulletx = []
            bullety = []
            bulletxx = []
            bulletyy = []
            bulletdel = []
            bulletreload = 8
            bullshotdamage = 4
            shotgunacc = 60
            shotgunreload = 100
            shotgunbullets = 6
            ebulletx = []
            ebullety = []
            ebulletxx = []
            ebulletyy = []
            ebulletdel = []
            minex = []
            miney = []
            minedel = []
            miner = []
            mineradius = 150
            minedamage = 3
            mineshrapnel = 0
            lightning1x = []
            lightning1y = []
            lightning2x = []
            lightning2y = []
            lightningtimer = 0
            lightreload = 200
            lightdamage = 1
            eshipx = []
            eshipy = []
            eshipxx = []
            eshipyy = []
            eshipdel = []
            eshiphit = []
            eshiphitt = []
            eshiptype = []
            eshipsum = []
            eshipstuntimer = []
            lightstruck = []
            stopwatch = 0
            minetimer = 0
            shoottimer = 0
            shotguntimer = 0
            shoot = False
            dropmine = False
            aimturn = "?"
            aimturn1 = "?"
            score = 0
            alientimer = 0
            delay = [0, 0, 0, 0, 0, 0]
            mode = "medium"
            coins = 1000
            upgradebullets = 1
            upgradeshotgun = 1
            upgradelasers = 1
            upgrademissiles = 1
            upgrademines = 1
            upgradelightning = 1
            laserx = []
            lasery = []
            laserxx = []
            laseryy = []
            laserdel = []
            laserreload = 60
            laserdamage = 3
            lasertimer = 0
            missilex = []
            missiley = []
            missilexx = []
            missileyy = []
            missiledel = []
            missilereload = 100
            missiledamage = 4
            missileradius = 100
            missileshrapnel = 0
            missiler = []
            missiletimer = 0
            level = "?"
            slide = "main menu"
            win = False
            dietimer = 300
            leveltimer = 300

        #____________________________________________________________________________________________________________________________________________ creating enemies
        if alientimer <= 0 and level == "?":
            choice = random.randint(1, 100)
            if stopwatch < 1500:
                if choice < 70:
                    make_eship(0, random.randint(1, 540), random.randint(-6, 6) / 4, random.randint(-6, 6) / 4,
                               random.randint(1, 30), "norm")
                elif choice < 90:
                    make_eship(0, random.randint(1, 540), random.randint(-6, 6) / 4, random.randint(-6, 6) / 4,
                               random.randint(1, 40), "split")
                else:
                    make_eship(0, random.randint(1, 540), random.randint(-6, 6) / 4, random.randint(-6, 6) / 4,
                               random.randint(1, 60), "splitt")
            elif stopwatch < 3000:
                if choice < 50:
                    make_eship(0, random.randint(1, 540), random.randint(-6, 6) / 4, random.randint(-6, 6) / 4,
                               random.randint(1, 30), "norm")
                elif choice < 70:
                    make_eship(0, random.randint(1, 540), random.randint(-6, 6) / 4, random.randint(-6, 6) / 4,
                               random.randint(1, 40), "split")
                elif choice < 85:
                    make_eship(0, random.randint(1, 540), random.randint(-6, 6) / 4, random.randint(-6, 6) / 4,
                               random.randint(1, 60), "splitt")
                elif choice < 95:
                    make_eship(0, random.randint(1, 540), random.randint(-6, 6) / 4, random.randint(-6, 6) / 4,
                               random.randint(1, 80), "splittt")
                else:
                    make_eship(0, random.randint(1, 540), random.randint(-6, 6) / 4, random.randint(-6, 6) / 4,
                               random.randint(1, 100), "splitttt")
            elif stopwatch < 4500:
                if choice < 30:
                    make_eship(0, random.randint(1, 540), random.randint(-6, 6) / 4, random.randint(-6, 6) / 4,
                               random.randint(1, 60), "split")
                elif choice < 60:
                    make_eship(0, random.randint(1, 540), random.randint(-6, 6) / 4, random.randint(-6, 6) / 4,
                               random.randint(1, 70), "splitt")
                elif choice < 70:
                    make_eship(0, random.randint(1, 540), random.randint(-6, 6) / 4, random.randint(-6, 6) / 4,
                               random.randint(1, 100), "splittt")
                elif choice < 80:
                    make_eship(0, random.randint(1, 540), random.randint(-6, 6) / 4, random.randint(-6, 6) / 4,
                               random.randint(1, 120), "splitttt")
                elif choice < 90:
                    make_eship(0, random.randint(1, 540), random.randint(-6, 6) / 4, random.randint(-6, 6) / 4,
                               random.randint(1, 150), "splittttt")
                else:
                    make_eship(0, random.randint(1, 540), random.randint(-6, 6) / 4, random.randint(-6, 6) / 4,
                               random.randint(1, 180), "splitttttt")
            elif stopwatch < 6000:
                if choice < 35:
                    make_eship(0, random.randint(1, 540), random.randint(-6, 6) / 4, random.randint(-6, 6) / 4,
                               random.randint(1, 75), "splitt")
                elif choice < 60:
                    make_eship(0, random.randint(1, 540), random.randint(-6, 6) / 4, random.randint(-6, 6) / 4,
                               random.randint(1, 105), "splittt")
                elif choice < 80:
                    make_eship(0, random.randint(1, 540), random.randint(-6, 6) / 4, random.randint(-6, 6) / 4,
                               random.randint(1, 130), "splitttt")
                elif choice < 88:
                    make_eship(0, random.randint(1, 540), random.randint(-6, 6) / 4, random.randint(-6, 6) / 4,
                               random.randint(1, 160), "splittttt")
                elif choice < 93:
                    make_eship(0, random.randint(1, 540), random.randint(-6, 6) / 4, random.randint(-6, 6) / 4,
                               random.randint(1, 200), "splitttttt")
                elif choice < 98:
                    make_eship(0, random.randint(1, 540), random.randint(-6, 6) / 4, random.randint(-6, 6) / 4,
                               random.randint(1, 240), "splittttttt")
                else:
                    make_eship(0, random.randint(1, 540), random.randint(-6, 6) / 4, random.randint(-6, 6) / 4,
                               random.randint(1, 310), "splitttttttt")
            elif stopwatch < 7500:
                if choice < 40:
                    make_eship(0, random.randint(1, 540), random.randint(-6, 6) / 4, random.randint(-6, 6) / 4,
                               random.randint(1, 120), "splittt")
                elif choice < 70:
                    make_eship(0, random.randint(1, 540), random.randint(-6, 6) / 4, random.randint(-6, 6) / 4,
                               random.randint(1, 150), "splitttt")
                elif choice < 82:
                    make_eship(0, random.randint(1, 540), random.randint(-6, 6) / 4, random.randint(-6, 6) / 4,
                               random.randint(1, 180), "splittttt")
                elif choice < 88:
                    make_eship(0, random.randint(1, 540), random.randint(-6, 6) / 4, random.randint(-6, 6) / 4,
                               random.randint(1, 225), "splitttttt")
                elif choice < 95:
                    make_eship(0, random.randint(1, 540), random.randint(-6, 6) / 4, random.randint(-6, 6) / 4,
                               random.randint(1, 270), "splittttttt")
                else:
                    make_eship(0, random.randint(1, 540), random.randint(-6, 6) / 4, random.randint(-6, 6) / 4,
                               random.randint(1, 350), "splitttttttt")
            elif stopwatch < 10000:
                if choice < 40:
                    make_eship(0, random.randint(1, 540), random.randint(-6, 6) / 4, random.randint(-6, 6) / 4,
                               random.randint(100, 200), "splitttt")
                elif choice < 65:
                    make_eship(0, random.randint(1, 540), random.randint(-6, 6) / 4, random.randint(-6, 6) / 4,
                               random.randint(100, 300), "splittttt")
                elif choice < 80:
                    make_eship(0, random.randint(1, 540), random.randint(-6, 6) / 4, random.randint(-6, 6) / 4,
                               random.randint(100, 400), "splitttttt")
                elif choice < 91:
                    make_eship(0, random.randint(1, 540), random.randint(-6, 6) / 4, random.randint(-6, 6) / 4,
                               random.randint(200, 600), "splittttttt")
                else:
                    make_eship(0, random.randint(1, 540), random.randint(-6, 6) / 4, random.randint(-6, 6) / 4,
                               random.randint(250, 1000), "splitttttttt")
            elif stopwatch < 15000:
                if choice < 50:
                    make_eship(0, random.randint(1, 540), random.randint(-6, 6) / 4, random.randint(-6, 6) / 4,
                               random.randint(3, 8)*100, "splitttttt")
                elif choice < 80:
                    make_eship(0, random.randint(1, 540), random.randint(-6, 6) / 4, random.randint(-6, 6) / 4,
                               random.randint(5, 12)*100, "splittttttt")
                else:
                    make_eship(0, random.randint(1, 540), random.randint(-6, 6) / 4, random.randint(-6, 6) / 4,
                               random.randint(10, 20)*100, "splitttttttt")
            else:
                if random.randint(1, 10) == 1:
                    make_eship(0, random.randint(1, 540), random.randint(-10, 10) / 4, random.randint(-10, 10) / 4,
                           random.randint(10, round((stopwatch / 120)**2/200))*100, "splitttttttt")
            alientimer = random.randint(20, 80)

        #____________________________________________________________________________________________________________________________________________ stopwatches, timers

        stopwatch += 1
        lightningtimer -= 1
        minetimer += 1
        shoottimer += 1
        shotguntimer += 1
        missiletimer += 1
        lasertimer += 1

        if (stopwatch / 100) % 1 == 0:
            if shiphit < 50 and mode != "one life":
                if stopwatch < 10000:
                    shiphit += 1
                elif stopwatch < 15000:
                    shiphit += 0.5
                elif stopwatch < 20000:
                    shiphit += 0.25

        #____________________________________________________________________________________________________________________________________________ Shooting stuff
        if shoottimer >= bulletreload:
            if shoot == True:
                if upgradebullets <= 3:
                    bulletx.append(shipx)
                    bullety.append(shipy)
                    bulletxx.append(shipxx * 5)
                    bulletyy.append(shipyy * 5)
                    bulletdel.append(1)
                if upgradebullets >= 7:
                    bulletx.append(shipx)
                    bullety.append(shipy)
                    bulletxx.append(shipxx * 12)
                    bulletyy.append(shipyy * 12)
                    bulletdel.append(1)
                if upgradebullets == 4:
                    bulletx.append(shipx)
                    bullety.append(shipy - 10)
                    bulletxx.append(shipxx * 5)
                    bulletyy.append(shipyy * 5)
                    bulletdel.append(1)
                    bulletx.append(shipx)
                    bullety.append(shipy + 10)
                    bulletxx.append(shipxx * 5)
                    bulletyy.append(shipyy * 5)
                    bulletdel.append(1)
                if upgradebullets >= 5:
                    bulletx.append(shipx)
                    bullety.append(shipy - 10)
                    bulletxx.append(shipxx * 12)
                    bulletyy.append(shipyy * 12)
                    bulletdel.append(1)
                    bulletx.append(shipx)
                    bullety.append(shipy + 10)
                    bulletxx.append(shipxx * 12)
                    bulletyy.append(shipyy * 12)
                    bulletdel.append(1)
                if gunsounds == True:
                    pygame.mixer.Sound.play(gunsound)
                shoottimer = 0

        if lasertimer >= laserreload:
            if shoot == True:
                if upgradelasers <= 2:
                    laserx.append(shipx + shipxx*10)
                    lasery.append(shipy + shipyy*10)
                    laserxx.append(shipxx * 5)
                    laseryy.append(shipyy * 5)
                    laserdel.append(1)
                if 3 <= upgradelasers <= 7:
                    laserx.append(shipx + shipxx*10)
                    lasery.append(shipy - 10 + shipyy*10)
                    laserxx.append(shipxx * 5)
                    laseryy.append(shipyy * 5)
                    laserdel.append(1)
                    laserx.append(shipx + shipxx*10)
                    lasery.append(shipy + 10 + shipyy*10)
                    laserxx.append(shipxx * 5)
                    laseryy.append(shipyy * 5)
                    laserdel.append(1)
                if upgradelasers == 8:
                    laserx.append(shipx + shipxx*10)
                    lasery.append(shipy - 15 + shipyy*10)
                    laserxx.append(shipxx * 5) #nfajhwefkjhberjbf
                    laseryy.append(shipyy * 5)
                    laserdel.append(1)
                    laserx.append(shipx + 15 + shipxx*10)
                    lasery.append(shipy + shipyy*10)
                    laserxx.append(shipxx * 5)
                    laseryy.append(shipyy * 5)
                    laserdel.append(1)
                    laserx.append(shipx - 15 + shipxx*10)
                    lasery.append(shipy + shipyy*10)
                    laserxx.append(shipxx * 5)
                    laseryy.append(shipyy * 5)
                    laserdel.append(1)
                    laserx.append(shipx + shipxx*10)
                    lasery.append(shipy + 15 + shipyy*10)
                    laserxx.append(shipxx * 5)
                    laseryy.append(shipyy * 5)
                    laserdel.append(1)
                lasertimer = 0

        if missiletimer >= missilereload:
            if shoot == True:
                if upgrademissiles <= 4:
                    missilex.append(shipx)
                    missiley.append(shipy)
                    missilexx.append(shipxx * 5)
                    missileyy.append(shipyy * 5)
                    missiledel.append(1)
                    missiler.append(1)
                if 5 <= upgrademissiles <= 6:
                    missilex.append(shipx+10)
                    missiley.append(shipy+10)
                    missilexx.append(shipxx * 5)
                    missileyy.append(shipyy * 5)
                    missiledel.append(1)
                    missiler.append(1)
                    missilex.append(shipx-10)
                    missiley.append(shipy-10)
                    missilexx.append(shipxx * 5)
                    missileyy.append(shipyy * 5)
                    missiledel.append(1)
                    missiler.append(1)
                if upgrademissiles >= 7:
                    missilex.append(shipx+10)
                    missiley.append(shipy+10)
                    missilexx.append(shipxx * 12)
                    missileyy.append(shipyy * 12)
                    missiledel.append(1)
                    missiler.append(1)
                    missilex.append(shipx-10)
                    missiley.append(shipy-10)
                    missilexx.append(shipxx * 12)
                    missileyy.append(shipyy * 12)
                    missiledel.append(1)
                    missiler.append(1)
                missiletimer = 0

        if shotguntimer >= shotgunreload:
            if shoot == True:
                for cat in range(0, shotgunbullets):
                    if upgradeshotgun <= 6:
                        bulletx.append(shipx)
                        bullety.append(shipy)
                        bulletxx.append(random.randint(round(50 * shipxx - shotgunacc), round(50 * shipxx + shotgunacc)) / 10)
                        bulletyy.append(random.randint(round(50 * shipyy - shotgunacc), round(50 * shipyy + shotgunacc)) / 10)
                        bulletdel.append(1)
                    if upgradeshotgun >= 7:
                        bulletx.append(shipx)
                        bullety.append(shipy)
                        bulletxx.append(random.randint(round(120 * shipxx - shotgunacc), round(120 * shipxx + shotgunacc)) / 10)
                        bulletyy.append(random.randint(round(120 * shipyy - shotgunacc), round(120 * shipyy + shotgunacc)) / 10)
                        bulletdel.append(1)
                if shotgunsounds == True:
                    pygame.mixer.Sound.play(shotgunsound)
                shotguntimer = 0


        if minetimer > 30:
            if dropmine == True:
                minex.append(shipx)
                miney.append(shipy)
                minedel.append(1)
                miner.append(1)
                minetimer = 0

        #_____________________________________________________________________________ Enemy ships splitting
        for cat in range(0, len(eshipx)):
            if eshiphit[cat] <= 0:
                eshipdel[cat] = 0
                highscorenorm[8] += 1
                if eshiptype[cat] == "split" and stopwatch < 5000:
                    make_eship(eshipx[cat], eshipy[cat] - 10, eshipxx[cat], eshipyy[cat], round(1 + eshiphitt[cat] / 2),
                               "norm")
                    make_eship(eshipx[cat], eshipy[cat] + 10, eshipxx[cat], eshipyy[cat], round(1 + eshiphitt[cat] / 2),
                               "norm")
                    if mode == "triple":
                        make_eship(eshipx[cat], eshipy[cat] + 10, eshipxx[cat], eshipyy[cat],
                                   round(1 + eshiphitt[cat] / 2),
                                   "norm")
                if eshiptype[cat] == "splitt" and stopwatch < 7500:
                    make_eship(eshipx[cat], eshipy[cat] - 10, eshipxx[cat], eshipyy[cat], round(1 + eshiphitt[cat] / 2),
                               "split")
                    make_eship(eshipx[cat], eshipy[cat] + 10, eshipxx[cat], eshipyy[cat], round(1 + eshiphitt[cat] / 2),
                               "split")
                    if mode == "triple":
                        make_eship(eshipx[cat], eshipy[cat] + 10, eshipxx[cat], eshipyy[cat],
                                   round(1 + eshiphitt[cat] / 2),
                                   "split")
                if eshiptype[cat] == "splittt" and stopwatch < 10000:
                    make_eship(eshipx[cat], eshipy[cat] - 10, eshipxx[cat], eshipyy[cat], round(1 + eshiphitt[cat] / 2),
                               "splitt")
                    make_eship(eshipx[cat], eshipy[cat] + 10, eshipxx[cat], eshipyy[cat], round(1 + eshiphitt[cat] / 2),
                               "splitt")
                    if mode == "triple":
                        make_eship(eshipx[cat], eshipy[cat] + 10, eshipxx[cat], eshipyy[cat],
                                   round(1 + eshiphitt[cat] / 2),
                                   "splitt")
                if eshiptype[cat] == "splitttt" and stopwatch < 15000:
                    make_eship(eshipx[cat], eshipy[cat] - 10, eshipxx[cat], eshipyy[cat], round(1 + eshiphitt[cat] / 2),
                               "splittt")
                    make_eship(eshipx[cat], eshipy[cat] + 10, eshipxx[cat], eshipyy[cat], round(1 + eshiphitt[cat] / 2),
                               "splittt")
                    if mode == "triple":
                        make_eship(eshipx[cat], eshipy[cat] + 10, eshipxx[cat], eshipyy[cat],
                                   round(1 + eshiphitt[cat] / 2),
                                   "splittt")
                if eshiptype[cat] == "splittttt":
                    make_eship(eshipx[cat], eshipy[cat] - 10, eshipxx[cat], eshipyy[cat], round(1 + eshiphitt[cat] / 2),
                               "splitttt")
                    make_eship(eshipx[cat], eshipy[cat] + 10, eshipxx[cat], eshipyy[cat], round(1 + eshiphitt[cat] / 2),
                               "splitttt")
                    if mode == "triple":
                        make_eship(eshipx[cat], eshipy[cat] + 10, eshipxx[cat], eshipyy[cat],
                                   round(1 + eshiphitt[cat] / 2),
                                   "splitttt")
                if eshiptype[cat] == "splitttttt":
                    make_eship(eshipx[cat], eshipy[cat] - 10, eshipxx[cat], eshipyy[cat], round(1 + eshiphitt[cat] / 2),
                               "splittttt")
                    make_eship(eshipx[cat], eshipy[cat] + 10, eshipxx[cat], eshipyy[cat], round(1 + eshiphitt[cat] / 2),
                               "splittttt")
                    if mode == "triple":
                        make_eship(eshipx[cat], eshipy[cat] + 10, eshipxx[cat], eshipyy[cat],
                                   round(1 + eshiphitt[cat] / 2),
                                   "splittttt")
                if eshiptype[cat] == "splittttttt":
                    make_eship(eshipx[cat], eshipy[cat] - 10, eshipxx[cat], eshipyy[cat], round(1 + eshiphitt[cat] / 2),
                               "splitttttt")
                    make_eship(eshipx[cat], eshipy[cat] + 10, eshipxx[cat], eshipyy[cat], round(1 + eshiphitt[cat] / 2),
                               "splitttttt")
                    if mode == "triple":
                        make_eship(eshipx[cat], eshipy[cat] + 10, eshipxx[cat], eshipyy[cat],
                                   round(1 + eshiphitt[cat] / 2),
                                   "splitttttt")
                if eshiptype[cat] == "splitttttttt":
                    make_eship(eshipx[cat], eshipy[cat] - 10, eshipxx[cat], eshipyy[cat], round(1 + eshiphitt[cat] / 2),
                               "splittttttt")
                    make_eship(eshipx[cat], eshipy[cat] + 10, eshipxx[cat], eshipyy[cat], round(1 + eshiphitt[cat] / 2),
                               "splittttttt")
                    if mode == "triple":
                        make_eship(eshipx[cat], eshipy[cat] + 10, eshipxx[cat], eshipyy[cat],
                                   round(1 + eshiphitt[cat] / 2),
                                   "splittttttt")

            #_____________________________________________________________________________________lightning
            if (stopwatch / lightreload) % 1 == 0 and mode != "explosions only" and shoot == True:
                lightningtimer = 10
                if abs(eshipx[cat] - shipx) < 200 and abs(eshipy[cat] - shipy) < 200 or upgradelightning >= 4 and abs(
                        eshipx[cat] - shipx) < 350 and abs(eshipy[cat] - shipy) < 350:
                    lightning1x.append(shipx)
                    lightning1y.append(shipy)
                    lightning2x.append(eshipx[cat])
                    lightning2y.append(eshipy[cat])
                    lightstruck[cat] += 1
                if upgradelightning <= 5:
                    for dog in range(0, len(eshipx)):
                        if cat != dog and lightstruck[cat] >= 1:
                            if abs(eshipx[cat] - eshipx[dog]) < 200 and abs(
                                    eshipy[cat] - eshipy[dog]) < 200 or upgradelightning >= 4 and abs(
                                eshipx[cat] - eshipx[dog]) < 350 and abs(eshipy[cat] - eshipy[dog]) < 350:
                                lightning1x.append(eshipx[dog])
                                lightning1y.append(eshipy[dog])
                                lightning2x.append(eshipx[cat])
                                lightning2y.append(eshipy[cat])
                                lightstruck[dog] += 1
                if 6 <= upgradelightning <= 9:
                    for monkey in range(0, 2):
                        for dog in range(0, len(eshipx)):
                            if cat != dog and lightstruck[cat] >= 1:
                                if abs(eshipx[cat] - eshipx[dog]) < 200 and abs(
                                        eshipy[cat] - eshipy[dog]) < 200 or upgradelightning >= 4 and abs(
                                    eshipx[cat] - eshipx[dog]) < 350 and abs(eshipy[cat] - eshipy[dog]) < 350:
                                    lightning1x.append(eshipx[dog])
                                    lightning1y.append(eshipy[dog])
                                    lightning2x.append(eshipx[cat])
                                    lightning2y.append(eshipy[cat])
                                    lightstruck[dog] += 1

            for dog in range(0, len(eshipx)):
                if cat != dog and abs(eshipx[cat] - eshipx[dog]) < 32 and abs(eshipy[cat] - eshipy[dog]) < 32:
                    if eshipx[cat] - eshipx[dog] < 0:
                        eshipx[cat] -= 2
                    if eshipy[cat] - eshipy[dog] >= 0:
                        eshipy[cat] += 2
                    if eshipx[dog] - eshipx[cat] < 0:
                        eshipx[dog] -= 2
                    if eshipy[dog] - eshipy[cat] >= 0:
                        eshipy[dog] += 2

            #___________________________________________________________________________________Shooting enemy bullets
            if (stopwatch / 150) % 1 == 0 and mode == "easy":
                ebulletx.append(eshipx[cat])
                ebullety.append(eshipy[cat])
                ebulletxx.append(eshipxx[cat] * 3)
                ebulletyy.append(eshipyy[cat] * 3)
                ebulletdel.append(1)
            if mode == "medium" or mode == "one life" or mode == "half cash" or mode == "explosions only" or mode == "triple":
                if (stopwatch / 125) % 1 == 0:
                    ebulletx.append(eshipx[cat])
                    ebullety.append(eshipy[cat])
                    ebulletxx.append(eshipxx[cat] * 4)
                    ebulletyy.append(eshipyy[cat] * 4)
                    ebulletdel.append(1)
            if (stopwatch / 100) % 1 == 0 and mode == "hard":
                ebulletx.append(eshipx[cat])
                ebullety.append(eshipy[cat])
                ebulletxx.append(eshipxx[cat] * 5)
                ebulletyy.append(eshipyy[cat] * 5)
                ebulletdel.append(1)
            if (stopwatch / 75) % 1 == 0 and mode == "extreme":
                ebulletx.append(eshipx[cat])
                ebullety.append(eshipy[cat])
                ebulletxx.append(eshipxx[cat] * 6)
                ebulletyy.append(eshipyy[cat] * 6)
                ebulletdel.append(1)

        #____________________________________________________________________________________________________________________________________________ movement
        for cat in range(0, len(bulletx)):
            bulletx[cat] += bulletxx[cat]
            bullety[cat] += bulletyy[cat]

        for cat in range(0, len(laserx)):
            laserx[cat] += laserxx[cat]
            lasery[cat] += laseryy[cat]

        for cat in range(0, len(missilex)):
            if missiledel[cat] == 1:
                missilex[cat] += missilexx[cat]
                missiley[cat] += missileyy[cat]

        #__________________________________________________________enemy ship aimbot (to your ship)
        for cat in range(0, len(eshipx)):
            eshipstuntimer[cat] -= 1
            if eshipstuntimer[cat] <= 0:
                eshipx[cat] += eshipxx[cat]
                eshipy[cat] += eshipyy[cat]
                eshipstuntimer[cat] = 0
            if eshipxx[cat] == 0:
                eshipxx[cat] += 0.01
            if eshipxx[cat] != 0 and (shipx - eshipx[cat]) != 0:
                if eshipxx[cat] > 0 and (shipx - eshipx[cat]) > 0 or (shipx - eshipx[cat]) < 0 and eshipxx[cat] < 0:
                    if eshipyy[cat] / eshipxx[cat] < (shipy - eshipy[cat]) / (shipx - eshipx[cat]):
                        aimturn1 = "right"
                    if eshipyy[cat] / eshipxx[cat] > (shipy - eshipy[cat]) / (shipx - eshipx[cat]):
                        aimturn1 = "left"
                if eshipxx[cat] > 0 and (shipx - eshipx[cat]) < 0 or (shipx - eshipx[cat]) > 0 and eshipxx[cat] < 0:
                    if eshipyy[cat] / eshipxx[cat] < (shipy - eshipy[cat]) / (shipx - eshipx[cat]):
                        aimturn1 = "left"
                    if eshipyy[cat] / eshipxx[cat] > (shipy - eshipy[cat]) / (shipx - eshipx[cat]):
                        aimturn1 = "right"
                if aimturn1 == "left":
                    if eshipxx[cat] < 0 and eshipyy[cat] < 0:
                        eshipxx[cat] -= 0.05
                        eshipyy[cat] += 0.05
                    if eshipxx[cat] < 0 and eshipyy[cat] >= 0:
                        eshipxx[cat] += 0.05
                        eshipyy[cat] += 0.05
                    if eshipxx[cat] >= 0 and eshipyy[cat] < 0:
                        eshipxx[cat] -= 0.05
                        eshipyy[cat] -= 0.05
                    if eshipxx[cat] >= 0 and eshipyy[cat] >= 0:
                        eshipxx[cat] += 0.05
                        eshipyy[cat] -= 0.05
                if aimturn1 == "right":
                    if eshipxx[cat] < 0 and eshipyy[cat] < 0:
                        eshipxx[cat] += 0.05
                        eshipyy[cat] -= 0.05
                    if eshipxx[cat] < 0 and eshipyy[cat] >= 0:
                        eshipxx[cat] -= 0.05
                        eshipyy[cat] -= 0.05
                    if eshipxx[cat] >= 0 and eshipyy[cat] < 0:
                        eshipxx[cat] += 0.05
                        eshipyy[cat] += 0.05
                    if eshipxx[cat] >= 0 and eshipyy[cat] >= 0:
                        eshipxx[cat] -= 0.05
                        eshipyy[cat] += 0.05

            eshipxx[cat] = round(eshipxx[cat], 4)
            eshipyy[cat] = round(eshipyy[cat], 4)
            if abs(eshipxx[cat]) + abs(eshipyy[cat]) > eshipsum[cat]:
                if eshipxx[cat] > 0:
                    eshipxx[cat] -= 0.02
                if eshipxx[cat] < 0:
                    eshipxx[cat] += 0.02
                if eshipyy[cat] > 0:
                    eshipyy[cat] -= 0.02
                if eshipyy[cat] < 0:
                    eshipyy[cat] += 0.02

            #___________________________________________________________________________________________ End aimbot for enemy ships
            if eshipx[cat] > 1080:
                eshipx[cat] = 0
            if eshipx[cat] < 0:
                eshipx[cat] = 1080
            if eshipy[cat] > 540:
                eshipy[cat] = 0
            if eshipy[cat] < 0:
                eshipy[cat] = 540

        #_________________________________________________________________________________Your movement(left, right)
        if aimturn == "left":
            if shipxx < 0 and shipyy < 0:
                shipxx -= 0.04
                shipyy += 0.04
            if shipxx < 0 and shipyy >= 0:
                shipxx += 0.04
                shipyy += 0.04
            if shipxx >= 0 and shipyy < 0:
                shipxx -= 0.04
                shipyy -= 0.04
            if shipxx >= 0 and shipyy >= 0:
                shipxx += 0.04
                shipyy -= 0.04
        if aimturn == "right":
            if shipxx < 0 and shipyy < 0:
                shipxx += 0.04
                shipyy -= 0.04
            if shipxx < 0 and shipyy >= 0:
                shipxx -= 0.04
                shipyy -= 0.04
            if shipxx >= 0 and shipyy < 0:
                shipxx += 0.04
                shipyy += 0.04
            if shipxx >= 0 and shipyy >= 0:
                shipxx -= 0.04
                shipyy += 0.04

        shipxx = round(shipxx, 2)
        shipyy = round(shipyy, 2)

        if abs(shipxx) + abs(shipyy) > 3:
            if shipxx > 0:
                shipxx -= 0.01
            if shipxx < 0:
                shipxx += 0.01
            if shipyy > 0:
                shipyy -= 0.01
            if shipyy < 0:
                shipyy += 0.01

        shipx += shipxx
        shipy += shipyy
        if shipx > 1080:
            shipx = 0
        if shipx < 0:
            shipx = 1080
        if shipy > 540:
            shipy = 0
        if shipy < 0:
            shipy = 540

        #_______________________________________________________________________________________________________________________________________Collisions, damage, deletion

        for cat in range(0, 5):
            if len(eshipx) > 50:
                eshipdel[49] = 0

        if upgradelasers >= 9:
            for cat in range(0, 50):
                for dog in range(0, len(eshipdel)):
                    if eshipx[dog] - 25 <= shipx + 10 * cat * shipxx <= eshipx[dog] + 25:
                        if eshipy[dog] - 25 <= shipy + 10 * cat * shipyy <= eshipy[dog] + 25:
                            eshiphit[dog] -= 8
                            highscorenorm[9] += 8

        for cat in range(0, len(bulletx)):
            for dog in range(0, len(ebulletdel)):
                if abs(ebulletx[dog] - bulletx[cat]) < 12 and abs(ebullety[dog] - bullety[cat]) < 12 and upgradebullets >= 9:
                    bulletdel[cat] = 0

        for cat in range(0, len(bulletx)):
            for dog in range(0, len(eshipdel)):
                if abs(eshipx[dog] - bulletx[cat]) < 25 and abs(eshipy[dog] - bullety[cat]) < 25:
                    bulletdel[cat] = 0
                    eshiphit[dog] -= bullshotdamage
                    highscorenorm[9] += bullshotdamage
                    if upgradeshotgun >= 9 and (shipx - eshipx[dog]) != 0:
                        ratio2 = (shipy - eshipy[dog]) / (shipx - eshipx[dog])
                        if (eshipy[dog] - shipy) < 0 and (eshipx[dog] - shipx) < 0:
                            eshipy[dog] -= (round(ratio2 * math.sqrt(300 / (ratio2 ** 2 + 1)), 3))
                            eshipx[dog] -= (round(math.sqrt(300 / (ratio2 ** 2 + 1)), 3))
                        if (eshipy[dog] - shipy) >= 0 and (eshipx[dog] - shipx) >= 0:
                            eshipy[dog] -= (-round(ratio2 * math.sqrt(300 / (ratio2 ** 2 + 1)), 3))
                            eshipx[dog] -= (-round(math.sqrt(300 / (ratio2 ** 2 + 1)), 3))
                        if (eshipx[dog] - shipx) < 0 and (eshipy[dog] - shipy) >= 0:
                            eshipy[dog] -= (round(ratio2 * math.sqrt(300 / (ratio2 ** 2 + 1)), 3))
                            eshipx[dog] -= (round(math.sqrt(300 / (ratio2 ** 2 + 1)), 3))
                        if (eshipx[dog] - shipx) >= 0 and (eshipy[dog] - shipy) < 0:
                            eshipy[dog] -= (-round(ratio2 * math.sqrt(300 / (ratio2 ** 2 + 1)), 3))
                            eshipx[dog] -= (-round(math.sqrt(300 / (ratio2 ** 2 + 1)), 3))

        for cat in range(0, len(laserx)):
            for dog in range(0, len(eshipdel)):
                if abs(eshipx[dog] - laserx[cat]) < 25 and abs(eshipy[dog] - lasery[cat]) < 25:
                    eshiphit[dog] -= laserdamage
                    highscorenorm[9] += laserdamage

        for cat in range(0, len(missilex)):
            for dog in range(0, len(eshipdel)):
                if abs(eshipx[dog] - missilex[cat]) < 25 and abs(eshipy[dog] - missiley[cat]) < 25:
                    missiledel[cat] = 2

        for cat in range(0, len(bulletx)):
            for dog in range(0, len(minex)):
                if abs(minex[dog] - bulletx[cat]) < 20 and abs(miney[dog] - bullety[cat]) < 20:
                    bulletdel[cat] = 0
                    minedel[dog] = 2

        for cat in range(0, len(eshipdel)):
            for dog in range(0, len(minex)):
                if abs(eshipx[cat] - minex[dog]) < 40 and abs(eshipy[cat] - miney[dog]) < 40:
                    minedel[dog] = 2
            if eshipx[cat] > 1080:
                eshipx[cat] = 0
            if eshipx[cat] < 0:
                eshipx[cat] = 1080
            if eshipy[cat] > 540:
                eshipy[cat] = 0
            if eshipy[cat] < 0:
                eshipy[cat] = 540

        for cat in range(0, len(missilex)):
            if missilex[cat] > 1080 and missiledel[cat] == 1:
                missiledel[cat] = 2
            if missilex[cat] < 0 and missiledel[cat] == 1:
                missiledel[cat] = 2
            if missiley[cat] > 540 and missiledel[cat] == 1:
                missiledel[cat] = 2
            if missiley[cat] < 0 and missiledel[cat] == 1:
                missiledel[cat] = 2

        for cat in range(0, len(minex)):
            if minedel[cat] == 2:
                for dog in range(0, len(eshipx)):
                    if abs(eshipx[dog] - minex[cat]) <= miner[cat]:
                        if abs(eshipy[dog] - miney[cat]) <= miner[cat]:
                            eshiphit[dog] -= minedamage
                            highscorenorm[9] += minedamage
                if abs(shipx - minex[cat]) <= miner[cat]:
                    if abs(shipy - miney[cat]) <= miner[cat]:
                        if upgrademines <= 5:
                            shiphit += 0.25
                miner[cat] += 25
                if miner[cat] > mineradius:
                    minedel[cat] = 0
                    #________________________________________________________________________________________________This part is really for making shrapnel.
                    if minesounds == True:
                        pygame.mixer.Sound.play(explosionsound)
                    for dog in range(0, mineshrapnel):
                        randomx = random.randint(-9, 9)
                        randomy = random.randint(-9, 9)
                        bulletx.append(minex[cat])
                        bullety.append(miney[cat])
                        bulletxx.append(randomx)
                        bulletyy.append(randomy)
                        bulletdel.append(1)

        for cat in range(0, len(missilex)):
            if missiledel[cat] == 2:
                for dog in range(0, len(eshipx)):
                    if abs(eshipx[dog] - missilex[cat]) <= missiler[cat]:
                        if abs(eshipy[dog] - missiley[cat]) <= missiler[cat]:
                            eshiphit[dog] -= missiledamage
                            highscorenorm[9] += missiledamage
                missiler[cat] += 25
                if missiler[cat] > missileradius:
                    missiledel[cat] = 0
                    #________________________________________________________________________________________________This part is really for making shrapnel.
                    if minesounds == True:
                        pygame.mixer.Sound.play(explosionsound)
                    for dog in range(0, missileshrapnel):
                        randomx = random.randint(-9, 9)
                        randomy = random.randint(-9, 9)
                        bulletx.append(missilex[cat])
                        bullety.append(missiley[cat])
                        bulletxx.append(randomx)
                        bulletyy.append(randomy)
                        bulletdel.append(1)

        for cat in range(0, len(eshipdel)):
            while lightstruck[cat] >= 1 and upgradelightning <= 4:
                eshiphit[cat] -= lightdamage
                highscorenorm[9] += lightdamage
                lightstruck[cat] -= 1
            while lightstruck[cat] >= 1 and 5 <= upgradelightning <= 8:
                eshiphit[cat] -= lightdamage
                lightstruck[cat] -= 1
                highscorenorm[9] += lightdamage
                if upgradelightning != 5:
                    eshipstuntimer[cat] = 20
            while lightstruck[cat] >= 1 and upgradelightning >= 9:
                eshiphit[cat] -= lightdamage*3
                highscorenorm[9] += lightdamage*3
                lightstruck[cat] -= 1
                eshipstuntimer[cat] = 20

        #__________________________________________________________________________________________________deletion

        for cat in range(0, len(bulletx)):
            if bulletx[cat] > 1080:
                bulletdel[cat] = 0
            if bulletx[cat] < 0:
                bulletdel[cat] = 0
            if bullety[cat] > 540:
                bulletdel[cat] = 0
            if bullety[cat] < 0:
                bulletdel[cat] = 0

        for cat in range(0, len(laserx)):
            if laserx[cat] > 1080:
                laserdel[cat] = 0
            if laserx[cat] < 0:
                laserdel[cat] = 0
            if lasery[cat] > 540:
                laserdel[cat] = 0
            if lasery[cat] < 0:
                laserdel[cat] = 0

        for cat in range(0, len(ebulletdel)):
            ebulletx[cat] += ebulletxx[cat]
            ebullety[cat] += ebulletyy[cat]
            if ebulletx[cat] > 1080:
                ebulletdel[cat] = 0
            if ebulletx[cat] < 0:
                ebulletdel[cat] = 0
            if ebullety[cat] > 540:
                ebulletdel[cat] = 0
            if ebullety[cat] < 0:
                ebulletdel[cat] = 0
            if abs(shipx - ebulletx[cat]) < 25 and abs(shipy - ebullety[cat]) < 25:
                shiphit -= 1
                ebulletdel[cat] = 0

        for dog in range(0, len(eshipdel)):
            for cat in range(0, len(eshipdel)):
                if eshipdel[cat] == 0:
                    if shiphit > 0:
                        if stopwatch < 3000:
                            score += eshiphitt[cat]
                            coins += eshiphitt[cat]
                        elif stopwatch < 4500:
                            score += eshiphitt[cat]/2
                            coins += eshiphitt[cat]/2
                        elif stopwatch < 7500:
                            score += eshiphitt[cat]/5
                            coins += eshiphitt[cat]/5
                        elif stopwatch < 10000:
                            score += 3*eshiphitt[cat]/20
                            coins += 3*eshiphitt[cat]/20
                        elif stopwatch < 15000:
                            score += eshiphitt[cat]/20
                            coins += eshiphitt[cat]/20
                        else:
                            score += eshiphitt[cat] / 50
                            coins += eshiphitt[cat] / 50
                        if mode == "half cash":
                            if stopwatch < 3000:
                                score += eshiphitt[cat]/2
                                coins += eshiphitt[cat]/2
                            elif stopwatch < 4500:
                                score += eshiphitt[cat] / 4
                                coins += eshiphitt[cat] / 4
                            elif stopwatch < 7500:
                                score += eshiphitt[cat] / 10
                                coins += eshiphitt[cat] / 10
                            elif stopwatch < 10000:
                                score += 3 * eshiphitt[cat] / 40
                                coins += 3 * eshiphitt[cat] / 40
                            elif stopwatch < 15000:
                                score += eshiphitt[cat] / 40
                                coins += eshiphitt[cat] / 40
                            else:
                                score += eshiphitt[cat] / 50
                                coins += eshiphitt[cat] / 50
                    score = round(score)
                    del eshipx[cat]
                    del eshipy[cat]
                    del eshipxx[cat]
                    del eshipyy[cat]
                    del eshipdel[cat]
                    del eshiphit[cat]
                    del eshiphitt[cat]
                    del eshiptype[cat]
                    del eshipsum[cat]
                    del lightstruck[cat]
                    del eshipstuntimer[cat]
                    break

        for dog in range(0, len(ebulletdel)):
            for cat in range(0, len(ebulletdel)):
                if ebulletdel[cat] == 0:
                    del ebulletx[cat]
                    del ebullety[cat]
                    del ebulletxx[cat]
                    del ebulletyy[cat]
                    del ebulletdel[cat]
                    break

        for dog in range(0, len(bulletx)):
            for cat in range(0, len(bulletx)):
                if bulletdel[cat] == 0:
                    del bulletx[cat]
                    del bullety[cat]
                    del bulletxx[cat]
                    del bulletyy[cat]
                    del bulletdel[cat]
                    break

        for dog in range(0, len(laserx)):
            for cat in range(0, len(laserx)):
                if laserdel[cat] == 0:
                    del laserx[cat]
                    del lasery[cat]
                    del laserxx[cat]
                    del laseryy[cat]
                    del laserdel[cat]
                    break

        for dog in range(0, len(missilex)):
            for cat in range(0, len(missilex)):
                if missiledel[cat] == 0:
                    del missilex[cat]
                    del missiley[cat]
                    del missilexx[cat]
                    del missileyy[cat]
                    del missiledel[cat]
                    del missiler[cat]
                    break

        for dog in range(0, len(minex)):
            for cat in range(0, len(minex)):
                if minedel[cat] == 0:
                    del minex[cat]
                    del miney[cat]
                    del minedel[cat]
                    del miner[cat]
                    break

        #____________________________________________________________________________________________________________________________________________drawing
        for cat in range(0, len(lightning1x)):
            if lightningtimer <= 10:
                pygame.draw.line(screen,
                                 (5 + 25 * lightningtimer, 5 + 25 * lightningtimer, 5 + 25 * lightningtimer),
                                 (lightning1x[cat], lightning1y[cat]),
                                 (lightning2x[cat], lightning2y[cat]), 6)

        if upgradelasers >= 9:
            pygame.draw.line(screen, (255, 100, 100), (round(shipx), round(shipy)),
                             (round(shipx + 500 * shipxx), round(shipy + 500 * shipyy)), 20)

        for cat in range(0, len(bulletx)):
            if abs(bulletxx[cat]) < 2 and abs(bulletyy[cat]) < 2:
                bulletdel[cat] = 0
            pygame.draw.circle(screen, (255, 255, 255), (round(bulletx[cat]), round(bullety[cat])), 5)

        for cat in range(0, len(laserx)):
            pygame.draw.line(screen, (255, 125, 50), (round(laserx[cat]), round(lasery[cat])),
                                 (round(laserx[cat] - 4 * laserxx[cat]), round(lasery[cat] - 4 * laseryy[cat])), 6)

        for cat in range(0, len(missilex)):
            pygame.draw.circle(screen, (255, 50, 0), (round(missilex[cat]), round(missiley[cat])), 8)

        screen.blit(scoretext0, (10, 40))
        screen.blit(scoretext, (110, 40))
        screen.blit(cointext1, (10, 10))
        screen.blit(cointext, (110, 10))
        screen.blit(stopwatchtext1, (20, 500))
        screen.blit(stopwatchtext2, (210, 500))
        screen.blit(stopwatchtext3, (240, 500))
        screen.blit(stopwatchtext4, (250, 500))
        coins = round(coins)

        counter1 = (shipxx ** 2 + shipyy ** 2)/1.5
        pygame.draw.polygon(screen, (0, 255, 0), (
            ((shipx + shipxx * 3 * 9 / counter1), (shipy + shipyy * 3 * 9 / counter1)),
            ((shipx - shipxx * 4 - shipyy * 5 * 9 / counter1), (shipy - shipyy * 4 + shipxx * 5 * 9 / counter1)),
            ((shipx - shipxx * 4 + shipyy * 5 * 9 / counter1), (shipy - shipyy * 4 - shipxx * 5 * 9 / counter1))))
        pygame.draw.rect(screen, (255, 255, 255), (round(shipx) - 25, round(shipy) + 30, 50, 4))
        if shiphit > 0:
            pygame.draw.rect(screen, (255, 0, 0), (round(shipx) - 25, round(shipy) + 30, round(shiphit), 4))

        for cat in range(0, len(minex)):
            if miner[cat] == 1:
                pygame.draw.circle(screen, (255, 200, 50), (round(minex[cat]), round(miney[cat])), 15)
            if minedel[cat] == 2:
                if miner[cat] > 20:
                    pygame.draw.circle(screen, (255, 0, 0), (round(minex[cat]), round(miney[cat])), round(miner[cat]), 20)
                else:
                    pygame.draw.circle(screen, (255, 0, 0), (round(minex[cat]), round(miney[cat])), round(miner[cat]))

        for cat in range(0, len(missilex)):
            if missiler[cat] == 1:
                pygame.draw.circle(screen, (255, 0, 0), (round(missilex[cat]), round(missiley[cat])), 10)
            if missiledel[cat] == 2:
                if missiler[cat] > 20:
                    pygame.draw.circle(screen, (255, 0, 0), (round(missilex[cat]), round(missiley[cat])), round(missiler[cat]), 20)
                else:
                    pygame.draw.circle(screen, (255, 0, 0), (round(missilex[cat]), round(missiley[cat])), round(missiler[cat]))

        for cat in range(0, len(ebulletdel)):
            if abs(ebulletxx[cat]) < 2 and abs(ebulletyy[cat]) < 2:
                ebulletdel[cat] = 0
            pygame.draw.circle(screen, (255, 50, 50), (round(ebulletx[cat]), round(ebullety[cat])), 4)

        for cat in range(0, len(eshipdel)):
            if eshiptype[cat] != "splitttttttt":
                pygame.draw.rect(screen, (255, 255, 255), (round(eshipx[cat]) - 25, round(eshipy[cat]) + 30, 50, 4))
                pygame.draw.rect(screen, (255, 0, 0), (
                    round(eshipx[cat]) - 25, round(eshipy[cat]) + 30, round(eshiphit[cat] * 50 / eshiphitt[cat]), 4))
            if eshiptype[cat] == "splitttttttt":
                pygame.draw.rect(screen, (255, 255, 255), (round(eshipx[cat]) - 50, round(eshipy[cat]) + 55, 100, 4))
                pygame.draw.rect(screen, (255, 0, 0), (
                    round(eshipx[cat]) - 50, round(eshipy[cat]) + 55, round(eshiphit[cat] * 100 / eshiphitt[cat]), 4))
            if eshiptype[cat] == "norm":
                pygame.draw.circle(screen, (255, 0, 0), (round(eshipx[cat]), round(eshipy[cat])), 15)
            if eshiptype[cat] == "split":
                pygame.draw.circle(screen, (0, 0, 255), (round(eshipx[cat]), round(eshipy[cat])), 18)
            if eshiptype[cat] == "splitt":
                pygame.draw.circle(screen, (100, 255, 100), (round(eshipx[cat]), round(eshipy[cat])), 20)
            if eshiptype[cat] == "splittt":
                pygame.draw.circle(screen, (255, 255, 0), (round(eshipx[cat]), round(eshipy[cat])), 20)
            if eshiptype[cat] == "splitttt":
                pygame.draw.circle(screen, (255, 100, 100), (round(eshipx[cat]), round(eshipy[cat])), 20)
            if eshiptype[cat] == "splittttt":
                pygame.draw.circle(screen, (100, 100, 100), (round(eshipx[cat]), round(eshipy[cat])), 20)
            if eshiptype[cat] == "splitttttt":
                pygame.draw.circle(screen, (255, 255, 255), (round(eshipx[cat]), round(eshipy[cat])), 20)
            if eshiptype[cat] == "splittttttt":
                pygame.draw.circle(screen, (100, 100, 255), (round(eshipx[cat]), round(eshipy[cat])), 30)
            if eshiptype[cat] == "splitttttttt":
                pygame.draw.circle(screen, (200, 0, 0), (round(eshipx[cat]), round(eshipy[cat])), 50)

        #____________________________________________________________________________________________________________________________________________game over
        if shiphit <= 0:
            dietimer -= 1
            if (stopwatch % 5) != 0:
                stopwatch -= 1
            pygame.draw.rect(screen, (255, 255, 0), (round(shipx) - 25, round(shipy) + 30, 50, 4))
            shiphit -= 1
            if dietimer <= 0:
                if level == "?":
                    if score > highscorenorm[0] and mode == "easy":
                        highscorenorm[0] = score
                    if score > highscorenorm[1] and mode == "medium":
                        highscorenorm[1] = score
                    if score > highscorenorm[2] and mode == "hard":
                        highscorenorm[2] = score
                    if score > highscorenorm[3] and mode == "extreme":
                        highscorenorm[3] = score
                    if score > highscorenorm[4] and mode == "one life":
                        highscorenorm[4] = score
                    if score > highscorenorm[5] and mode == "half cash":
                        highscorenorm[5] = score
                    if score > highscorenorm[6] and mode == "explosions only":
                        highscorenorm[6] = score
                    if score > highscorenorm[7] and mode == "triple":
                        highscorenorm[7] = score
                shipx = 540
                shipy = 450
                shipxx = 0
                shipyy = -3
                shiphit = 50
                bulletx = []
                bullety = []
                bulletxx = []
                bulletyy = []
                bulletdel = []
                bulletreload = 8
                bullshotdamage = 4
                shotgunacc = 60
                shotgunreload = 100
                shotgunbullets = 6
                ebulletx = []
                ebullety = []
                ebulletxx = []
                ebulletyy = []
                ebulletdel = []
                minex = []
                miney = []
                minedel = []
                miner = []
                mineradius = 150
                minedamage = 3
                mineshrapnel = 0
                lightning1x = []
                lightning1y = []
                lightning2x = []
                lightning2y = []
                lightningtimer = 0
                lightreload = 200
                lightdamage = 1
                eshipx = []
                eshipy = []
                eshipxx = []
                eshipyy = []
                eshipdel = []
                eshiphit = []
                eshiphitt = []
                eshiptype = []
                eshipsum = []
                eshipstuntimer = []
                lightstruck = []
                stopwatch = 0
                minetimer = 0
                shoottimer = 0
                shotguntimer = 0
                shoot = False
                dropmine = False
                aimturn = "?"
                aimturn1 = "?"
                score = 0
                alientimer = 0
                delay = [0, 0, 0, 0, 0, 0]
                slide = "main menu"
                coins = 1000
                upgradebullets = 1
                upgradeshotgun = 1
                upgradelasers = 1
                upgrademissiles = 1
                upgrademines = 1
                upgradelightning = 1
                laserx = []
                lasery = []
                laserxx = []
                laseryy = []
                laserdel = []
                laserreload = 60
                laserdamage = 3
                lasertimer = 0
                missilex = []
                missiley = []
                missilexx = []
                missileyy = []
                missiledel = []
                missilereload = 100
                missiledamage = 4
                missileradius = 100
                missileshrapnel = 0
                missiler = []
                missiletimer = 0
                level = "?"
                dietimer = 300

        if mode == "explosions only":
            laserx = []
            lasery = []
            laserxx = []
            laseryy = []
            laserdel = []
            bulletx = []
            bullety = []
            bulletxx = []
            bulletyy = []
            bulletdel = []

    highscorenorm[10] = round(highscorenorm[10])
    highscorenorm[9] = round(highscorenorm[9])
    highscorenorm[8] = round(highscorenorm[8])

    pygame.display.flip()
    clock.tick(100)