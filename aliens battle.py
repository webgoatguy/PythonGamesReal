import pygame
import sys
import random
import pickle
import math

pygame.init()

dietimer = 300

clock = pygame.time.Clock()

screen = pygame.display.set_mode((1080,540))

#__________________________________________________________________________________________________Sound settings
gunsounds = False
minesounds = False
shotgunsounds = False

shipx = 80
shipy = 40
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
missileradius = 150
missiler = []
missiletimer = 0
missileshrapnel = 0

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

shipx1 = 1000
shipy1 = 500
shipxx1 = 0
shipyy1 = 3
shiphit1 = 50

bulletx1 = []
bullety1 = []
bulletxx1 = []
bulletyy1 = []
bulletdel1 = []
bulletreload1 = 8
bullshotdamage1 = 4
shotgunacc1 = 60
shotgunreload1 = 100
shotgunbullets1 = 6

laserx1 = []
lasery1 = []
laserxx1 = []
laseryy1 = []
laserdel1 = []
laserreload1 = 60
laserdamage1 = 3
lasertimer1 = 0

missilex1 = []
missiley1 = []
missilexx1 = []
missileyy1 = []
missiledel1 = []
missilereload1 = 100
missiledamage1 = 4
missileradius1 = 150
missiler1 = []
missiletimer1 = 0
missileshrapnel1 = 0

minex1 = []
miney1 = []
minedel1 = []
miner1 = []
mineradius1 = 150
minedamage1 = 3
mineshrapnel1 = 0

lightning1x1 = []
lightning1y1 = []
lightning2x1 = []
lightning2y1 = []
lightningtimer1 = 0
lightreload1 = 200
lightdamage1 = 1

eshipx = []
eshipy = []
eshipxx = []
eshipyy = []
eshipdel = []
eshiphit = []
eshiphitt = []
eshiptype = []
eshipsum = []
lightstruck = []
lightstruck1 = []
eshipstuntimer = []

ebulletx = []
ebullety = []
ebulletxx = []
ebulletyy = []
ebulletdel = []

stopwatch = 0
minetimer = 0
shoottimer = 0
shotguntimer = 0
minetimer1 = 0
shoottimer1 = 0
shotguntimer1 = 0

shoot = False
dropmine = False
shoot1 = False
dropmine1 = False

aimturn = "?"
aimturn1 = "?"

aimturn2 = "?"

score = 0
score1 = 0

alientimer = 0

delay = [0,0,0,0,0,0,0,0,0,0,0,0]

slide = "main menu"

coins = 10000000
coins1 = 10000000

upgradebullets = 1
upgradeshotgun = 1
upgradelasers = 1
upgrademissiles = 1
upgrademines = 1
upgradelightning = 1
upgradebullets1 = 1
upgradeshotgun1 = 1
upgradelasers1 = 1
upgrademissiles1 = 1
upgrademines1 = 1
upgradelightning1 = 1

font = pygame.font.Font("freesansbold.ttf", 30)

explosionsound = pygame.mixer.Sound("images/Explosion+3.wav")
gunsound = pygame.mixer.Sound("images/gun+silencer.wav")
shotgunsound = pygame.mixer.Sound("images/shotgun+2.wav")

mode = "medium"

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
    lightstruck1.append(0)
    eshipsum.append(abs(xx) + abs(yy))
    eshipstuntimer.append(0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                aimturn = "right"
            if event.key == pygame.K_a:
                aimturn = "left"
            if event.key == pygame.K_j:
                shoot = True
            if event.key == pygame.K_i:
                dropmine = True
            if event.key == pygame.K_s:
                aimturn1 = "left"
            if event.key == pygame.K_f:
                aimturn1 = "right"
            if event.key == pygame.K_k:
                shoot1 = True
            if event.key == pygame.K_o:
                dropmine1 = True
            if event.key == pygame.K_SPACE and slide == "upgrades":
                slide = "gameplay"
            elif event.key == pygame.K_SPACE and slide == "gameplay":
                slide = "upgrades"
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                aimturn = "?"
            if event.key == pygame.K_a:
                aimturn = "?"
            if event.key == pygame.K_j:
                shoot = False
            if event.key == pygame.K_i:
                dropmine = False
            if event.key == pygame.K_s:
                aimturn1 = "?"
            if event.key == pygame.K_f:
                aimturn1 = "?"
            if event.key == pygame.K_k:
                shoot1 = False
            if event.key == pygame.K_o:
                dropmine1 = False

    if lightningtimer <= 0:
        lightning1x = []
        lightning1y = []
        lightning2x = []
        lightning2y = []
        
    if lightningtimer1 <= 0:
        lightning1x1 = []
        lightning1y1 = []
        lightning2x1 = []
        lightning2y1 = []

    screen.fill((0, 0, 0))

    mousex, mousey = pygame.mouse.get_pos()

    #____________________________________________________________________________________________________________________________________________ Text
    scoretext = font.render(str(score), False, (255, 0, 255))
    cointext1 = font.render("Coins:", False, (255, 0, 255))
    cointext = font.render(str(coins), False, (255, 0, 255))
    scoretext1 = font.render(str(score1), False, (255, 0, 255))
    cointext2 = font.render(str(coins1), False, (255, 0, 255))
    bullet = font.render("Main gun:", False, (255, 255, 255))
    bullet2 = font.render("2 Shoots faster 150", False, (255, 255, 255))
    bullet3 = font.render("3 Bullets deal more damage (includes shotgun, shrapnel) 400", False, (255, 255, 255))
    bullet4 = font.render("4 Shoots from twin guns 600", False, (255, 255, 255))
    bullet5 = font.render("5 Bullets travel really fast 250", False, (255, 255, 255))
    bullet6 = font.render("6 Faster reload 500", False, (255, 255, 255))
    bullet7 = font.render("7 Shoots from triple guns 1250", False, (255, 255, 255))
    bullet8 = font.render("8 Bullets deal even more damage 2000", False, (255, 255, 255))
    shotgun = font.render("Shotgun:", False, (255, 255, 255))
    shotgun2 = font.render("2 More bullets per shot 200", False, (255, 255, 255))
    shotgun3 = font.render("3 Faster reload 250", False, (255, 255, 255))
    shotgun4 = font.render("4 More accuracy 50", False, (255, 255, 255))
    shotgun5 = font.render("5 Even more bullets per shot 600", False, (255, 255, 255))
    shotgun6 = font.render("6 Even faster reload 1000", False, (255, 255, 255))
    shotgun7 = font.render("7 Bullets travel really fast 250", False, (255, 255, 255))
    shotgun8 = font.render("8 Even more bullets per shot 1000", False, (255, 255, 255))
    shotgun9 = font.render("9 Bullets get knockback (includes main gun, shrapnel) 2500", False, (255, 255, 255))
    laser = font.render("Lasers:", False, (255, 255, 255))
    laser2 = font.render("2 Shoots faster 100", False, (255, 255, 255))
    laser3 = font.render("3 Shoots from twin guns 350", False, (255, 255, 255))
    laser4 = font.render("4 Lasers do more damage 200", False, (255, 255, 255))
    laser5 = font.render("5 Faster reload 300", False, (255, 255, 255))
    laser6 = font.render("6 Even faster reload 500", False, (255, 255, 255))
    laser7 = font.render("7 Lasers deal even more damage 800", False, (255, 255, 255))
    laser8 = font.render("8 Shoots from quadruple guns 1800", False, (255, 255, 255))
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
    lightning9 = font.render("9 Lightning can hit same ship five times 3000", False, (255, 255, 255))
    maxupgrades = font.render("Max upgrades", False, (255, 255, 255))
    easy = font.render("Easy mode", False, (100, 255, 100))
    medium = font.render("Medium mode", False, (255, 255, 0))
    hard = font.render("Hard mode", False, (255, 150, 0))
    extreme = font.render("Extreme mode", False, (200, 0, 0))
    mainmenu = font.render("Main menu", False, (255, 255, 255))
    specialtext = font.render("Special modes:", False, (255, 255, 255))
    onelife = font.render("One life", False, (255, 255, 255))
    halfcash = font.render("Half cash", False, (255, 255, 255))
    explosions = font.render("Explosions only", False, (255, 255, 255))
    triplemode = font.render("Triple mode", False, (255, 255, 255))

    if slide == "main menu":
        if event.type == pygame.MOUSEBUTTONDOWN and 20 < mousey < 50:
            mode = "easy"
            slide = "upgrades"
            delay = [20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]
        if event.type == pygame.MOUSEBUTTONDOWN and 50 < mousey < 80:
            mode = "medium"
            slide = "upgrades"
            delay = [20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]
        if event.type == pygame.MOUSEBUTTONDOWN and 80 < mousey < 110:
            mode = "hard"
            slide = "upgrades"
            delay = [20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]
        if event.type == pygame.MOUSEBUTTONDOWN and 110 < mousey < 140:
            mode = "extreme"
            slide = "upgrades"
            delay = [20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]
        if event.type == pygame.MOUSEBUTTONDOWN and 170 < mousey < 200:
            mode = "one life"
            slide = "upgrades"
            delay = [20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]
            shiphit = 1
            shiphit1 = 1
        if event.type == pygame.MOUSEBUTTONDOWN and 200 < mousey < 230:
            mode = "half cash"
            slide = "upgrades"
            delay = [20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]
            coins = 500
            coins1 = 500
        if event.type == pygame.MOUSEBUTTONDOWN and 230 < mousey < 260:
            mode = "explosions only"
            slide = "upgrades"
            delay = [20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]
        if event.type == pygame.MOUSEBUTTONDOWN and 260 < mousey < 290:
            mode = "triple"
            slide = "upgrades"
            delay = [20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]
        screen.blit(easy, (20, 20))
        screen.blit(medium, (20, 50))
        screen.blit(hard, (20, 80))
        screen.blit(extreme, (20, 110))
        screen.blit(onelife, (20, 170))
        screen.blit(halfcash, (20, 200))
        screen.blit(explosions, (20, 230))
        screen.blit(triplemode, (20, 260))
        screen.blit(specialtext, (20, 140))

    #____________________________________________________________________________________________________________________________________________ screen is on upgrades
    if slide == "upgrades":
        for cat in range(0, 12):
            delay[cat] -= 1

        #____________________________________________________________________________________________________________________________________________ detecting clicking for upgrading
        if event.type == pygame.MOUSEBUTTONDOWN and 20 < mousey < 50 and delay[0] < 0:
            upgradebullets += 1
            delay[0] = 20
            if upgradebullets == 2:
                coins -= 150
                if coins < 0:
                    coins += 150
                    
                    upgradebullets -= 1
            if upgradebullets == 3:
                coins -= 400
                if coins < 0:
                    coins += 400
                    
                    upgradebullets -= 1
            if upgradebullets == 4:
                coins -= 600
                if coins < 0:
                    coins += 600
                    
                    upgradebullets -= 1
            if upgradebullets == 5:
                coins -= 250
                if coins < 0:
                    coins += 250
                    
                    upgradebullets -= 1
            if upgradebullets == 6:
                coins -= 500
                if coins < 0:
                    coins += 500
                    
                    upgradebullets -= 1
            if upgradebullets == 7:
                coins -= 1250
                if coins < 0:
                    coins += 1250
                    
                    upgradebullets -= 1
            if upgradebullets == 8:
                coins -= 2000
                if coins < 0:
                    coins += 2000
                    
                    upgradebullets -= 1
        if event.type == pygame.MOUSEBUTTONDOWN and 50 < mousey < 80 and delay[1] < 0:
            upgradeshotgun += 1
            delay[1] = 20
            if upgradeshotgun == 2:
                coins -= 200
                if coins < 0:
                    coins += 200
                    
                    upgradeshotgun -= 1
            if upgradeshotgun == 3:
                coins -= 250
                if coins < 0:
                    coins += 250
                    
                    upgradeshotgun -= 1
            if upgradeshotgun == 4:
                coins -= 50
                if coins < 0:
                    coins += 50
                    
                    upgradeshotgun -= 1
            if upgradeshotgun == 5:
                coins -= 600
                if coins < 0:
                    coins += 600
                    
                    upgradeshotgun -= 1
            if upgradeshotgun == 6:
                coins -= 1000
                if coins < 0:
                    coins += 1000
                    
                    upgradeshotgun -= 1
            if upgradeshotgun == 7:
                coins -= 250
                if coins < 0:
                    coins += 250
                    
                    upgradeshotgun -= 1
            if upgradeshotgun == 8:
                coins -= 1000
                if coins < 0:
                    coins += 1000
                    
                    upgradeshotgun -= 1
            if upgradeshotgun == 9:
                coins -= 2500
                if coins < 0:
                    coins += 2500
                    
                    upgradeshotgun -= 1
        if event.type == pygame.MOUSEBUTTONDOWN and 80 < mousey < 110 and delay[2] < 0:
            upgradelasers += 1
            delay[2] = 20
            if upgradelasers == 2:
                coins -= 100
                if coins < 0:
                    coins += 100
                    
                    upgradelasers -= 1
            if upgradelasers == 3:
                coins -= 350
                if coins < 0:
                    coins += 350
                    
                    upgradelasers -= 1
            if upgradelasers == 4:
                coins -= 200
                if coins < 0:
                    coins += 200
                    
                    upgradelasers -= 1
            if upgradelasers == 5:
                coins -= 300
                if coins < 0:
                    coins += 300
                    
                    upgradelasers -= 1
            if upgradelasers == 6:
                coins -= 500
                if coins < 0:
                    coins += 500
                    
                    upgradelasers -= 1
            if upgradelasers == 7:
                coins -= 800
                if coins < 0:
                    coins += 800
                    
                    upgradelasers -= 1
            if upgradelasers == 8:
                coins -= 1800
                if coins < 0:
                    coins += 1800
                    
                    upgradelasers -= 1
        if event.type == pygame.MOUSEBUTTONDOWN and 110 < mousey < 140 and delay[3] < 0:
            upgrademissiles += 1
            delay[3] = 20
            if upgrademissiles == 2:
                coins -= 150
                if coins < 0:
                    coins += 150
                    
                    upgrademissiles -= 1
            if upgrademissiles == 3:
                coins -= 200
                if coins < 0:
                    coins += 200
                    
                    upgrademissiles -= 1
            if upgrademissiles == 4:
                coins -= 500
                if coins < 0:
                    coins += 500
                    
                    upgrademissiles -= 1
            if upgrademissiles == 5:
                coins -= 1000
                if coins < 0:
                    coins += 1000
                    
                    upgrademissiles -= 1
            if upgrademissiles == 6:
                coins -= 700
                if coins < 0:
                    coins += 700
                    
                    upgrademissiles -= 1
            if upgrademissiles == 7:
                coins -= 200
                if coins < 0:
                    coins += 200
                    
                    upgrademissiles -= 1
            if upgrademissiles == 8:
                coins -= 1200
                if coins < 0:
                    coins += 1200
                    
                    upgrademissiles -= 1
            if upgrademissiles == 9:
                coins -= 2400
                if coins < 0:
                    coins += 2400
                    
                    upgrademissiles -= 1
        if event.type == pygame.MOUSEBUTTONDOWN and 140 < mousey < 170 and delay[4] < 0:
            upgrademines += 1
            delay[4] = 20
            if upgrademines == 2:
                coins -= 200
                if coins < 0:
                    coins += 200
                    
                    upgrademines -= 1
            if upgrademines == 3:
                coins -= 400
                if coins < 0:
                    coins += 400
                    
                    upgrademines -= 1
            if upgrademines == 4:
                coins -= 400
                if coins < 0:
                    coins += 400
                    
                    upgrademines -= 1
            if upgrademines == 5:
                coins -= 600
                if coins < 0:
                    coins += 600
                    
                    upgrademines -= 1
            if upgrademines == 6:
                coins -= 500
                if coins < 0:
                    coins += 500
                    
                    upgrademines -= 1
            if upgrademines == 7:
                coins -= 800
                if coins < 0:
                    coins += 800
                    
                    upgrademines -= 1
            if upgrademines == 8:
                coins -= 1500
                if coins < 0:
                    coins += 1500
                    
                    upgrademines -= 1
            if upgrademines == 9:
                coins -= 2000
                if coins < 0:
                    coins += 2000
                    
                    upgrademines -= 1
        if event.type == pygame.MOUSEBUTTONDOWN and 170 < mousey < 200 and delay[5] < 0:
            upgradelightning += 1
            delay[5] = 20
            if upgradelightning == 2:
                coins -= 300
                if coins < 0:
                    coins += 300
                    
                    upgradelightning -= 1
            if upgradelightning == 3:
                coins -= 400
                if coins < 0:
                    coins += 400
                    
                    upgradelightning -= 1
            if upgradelightning == 4:
                coins -= 200
                if coins < 0:
                    coins += 200
                    
                    upgradelightning -= 1
            if upgradelightning == 5:
                coins -= 800
                if coins < 0:
                    coins += 800
                    
                    upgradelightning -= 1
            if upgradelightning == 6:
                coins -= 500
                if coins < 0:
                    coins += 500
                    
                    upgradelightning -= 1
            if upgradelightning == 7:
                coins -= 1000
                if coins < 0:
                    coins += 1000
                    
                    upgradelightning -= 1
            if upgradelightning == 8:
                coins -= 2000
                if coins < 0:
                    coins += 1200
                    
                    upgradelightning -= 1
            if upgradelightning == 9:
                coins -= 3000
                if coins < 0:
                    coins += 3000
                    
                    upgradelightning -= 1
        if event.type == pygame.MOUSEBUTTONDOWN and 200 < mousey < 230 and delay[6] < 0:
            upgradebullets1 += 1
            delay[6] = 20
            if upgradebullets1 == 2:
                coins1 -= 150
                if coins1 < 0:
                    coins1 += 150
                    
                    upgradebullets1 -= 1
            if upgradebullets1 == 3:
                coins1 -= 400
                if coins1 < 0:
                    coins1 += 400
                    
                    upgradebullets1 -= 1
            if upgradebullets1 == 4:
                coins1 -= 600
                if coins1 < 0:
                    coins1 += 600
                    
                    upgradebullets1 -= 1
            if upgradebullets1 == 5:
                coins1 -= 250
                if coins1 < 0:
                    coins1 += 250
                    
                    upgradebullets1 -= 1
            if upgradebullets1 == 6:
                coins1 -= 500
                if coins1 < 0:
                    coins1 += 500
                    
                    upgradebullets1 -= 1
            if upgradebullets1 == 7:
                coins1 -= 1250
                if coins1 < 0:
                    coins1 += 1250
                    
                    upgradebullets1 -= 1
            if upgradebullets1 == 8:
                coins1 -= 2000
                if coins1 < 0:
                    coins1 += 2000
                    
                    upgradebullets1 -= 1
        if event.type == pygame.MOUSEBUTTONDOWN and 230 < mousey < 260 and delay[7] < 0:
            upgradeshotgun1 += 1
            delay[7] = 20
            if upgradeshotgun1 == 2:
                coins1 -= 200
                if coins1 < 0:
                    coins1 += 200
                    
                    upgradeshotgun1 -= 1
            if upgradeshotgun1 == 3:
                coins1 -= 250
                if coins1 < 0:
                    coins1 += 250
                    
                    upgradeshotgun1 -= 1
            if upgradeshotgun1 == 4:
                coins1 -= 50
                if coins1 < 0:
                    coins1 += 50
                    
                    upgradeshotgun1 -= 1
            if upgradeshotgun1 == 5:
                coins1 -= 600
                if coins1 < 0:
                    coins1 += 600
                    
                    upgradeshotgun1 -= 1
            if upgradeshotgun1 == 6:
                coins1 -= 1000
                if coins1 < 0:
                    coins1 += 1000
                    
                    upgradeshotgun1 -= 1
            if upgradeshotgun1 == 7:
                coins1 -= 250
                if coins1 < 0:
                    coins1 += 250
                    
                    upgradeshotgun1 -= 1
            if upgradeshotgun1 == 8:
                coins1 -= 1000
                if coins1 < 0:
                    coins1 += 1000
                    
                    upgradeshotgun1 -= 1
            if upgradeshotgun1 == 9:
                coins1 -= 2500
                if coins1 < 0:
                    coins1 += 2500
                    
                    upgradeshotgun1 -= 1
        if event.type == pygame.MOUSEBUTTONDOWN and 260 < mousey < 290 and delay[8] < 0:
            upgradelasers1 += 1
            delay[8] = 20
            if upgradelasers1 == 2:
                coins1 -= 100
                if coins1 < 0:
                    coins1 += 100
                    delay[8] = 0
                    upgradelasers1 -= 1
            if upgradelasers1 == 3:
                coins1 -= 350
                if coins1 < 0:
                    coins1 += 350
                    
                    upgradelasers1 -= 1
            if upgradelasers1 == 4:
                coins1 -= 200
                if coins1 < 0:
                    coins1 += 200
                    
                    upgradelasers1 -= 1
            if upgradelasers1 == 5:
                coins1 -= 300
                if coins1 < 0:
                    coins1 += 300
                    
                    upgradelasers1 -= 1
            if upgradelasers1 == 6:
                coins1 -= 500
                if coins1 < 0:
                    coins1 += 500
                    
                    upgradelasers1 -= 1
            if upgradelasers1 == 7:
                coins1 -= 800
                if coins1 < 0:
                    coins1 += 800
                    
                    upgradelasers1 -= 1
            if upgradelasers1 == 8:
                coins1 -= 1800
                if coins1 < 0:
                    coins1 += 1800
                    
                    upgradelasers1 -= 1
        if event.type == pygame.MOUSEBUTTONDOWN and 290 < mousey < 320 and delay[3] < 0:
            upgrademissiles1 += 1
            delay[3] = 20
            if upgrademissiles1 == 2:
                coins1 -= 150
                if coins1 < 0:
                    coins1 += 150
                    
                    upgrademissiles1 -= 1
            if upgrademissiles1 == 3:
                coins1 -= 200
                if coins1 < 0:
                    coins1 += 200
                    
                    upgrademissiles1 -= 1
            if upgrademissiles1 == 4:
                coins1 -= 500
                if coins1 < 0:
                    coins1 += 500
                    
                    upgrademissiles1 -= 1
            if upgrademissiles1 == 5:
                coins1 -= 1000
                if coins1 < 0:
                    coins1 += 1000
                    upgrademissiles1 -= 1
            if upgrademissiles1 == 6:
                coins1 -= 700
                if coins1 < 0:
                    coins1 += 700
                    upgrademissiles1 -= 1
            if upgrademissiles1 == 7:
                coins1 -= 200
                if coins1 < 0:
                    coins1 += 200
                    upgrademissiles1 -= 1
            if upgrademissiles1 == 8:
                coins1 -= 1200
                if coins1 < 0:
                    coins1 += 1200
                    upgrademissiles1 -= 1
            if upgrademissiles1 == 9:
                coins1 -= 2400
                if coins1 < 0:
                    coins1 += 2400
                    upgrademissiles1 -= 1
        if event.type == pygame.MOUSEBUTTONDOWN and 320 < mousey < 351 and delay[4] < 0:
            upgrademines1 += 1
            delay[4] = 20
            if upgrademines1 == 2:
                coins1 -= 200
                if coins1 < 0:
                    coins1 += 200
                    upgrademines1 -= 1
            if upgrademines1 == 3:
                coins1 -= 400
                if coins1 < 0:
                    coins1 += 400
                    upgrademines1 -= 1
            if upgrademines1 == 4:
                coins1 -= 400
                if coins1 < 0:
                    coins1 += 400
                    upgrademines1 -= 1
            if upgrademines1 == 5:
                coins1 -= 600
                if coins1 < 0:
                    coins1 += 600
                    upgrademines1 -= 1
            if upgrademines1 == 6:
                coins1 -= 500
                if coins1 < 0:
                    coins1 += 500
                    upgrademines1 -= 1
            if upgrademines1 == 7:
                coins1 -= 800
                if coins1 < 0:
                    coins1 += 800
                    upgrademines1 -= 1
            if upgrademines1 == 8:
                coins1 -= 1500
                if coins1 < 0:
                    coins1 += 1500
                    upgrademines1 -= 1
            if upgrademines1 == 9:
                coins1 -= 2000
                if coins1 < 0:
                    coins1 += 2000
                    upgrademines1 -= 1
        if event.type == pygame.MOUSEBUTTONDOWN and 351 < mousey < 380 and delay[5] < 0:
            upgradelightning1 += 1
            delay[5] = 20
            if upgradelightning1 == 2:
                coins1 -= 300
                if coins1 < 0:
                    coins1 += 300
                    upgradelightning1 -= 1
            if upgradelightning1 == 3:
                coins1 -= 400
                if coins1 < 0:
                    coins1 += 400
                    upgradelightning1 -= 1
            if upgradelightning1 == 4:
                coins1 -= 200
                if coins1 < 0:
                    coins1 += 200
                    upgradelightning1 -= 1
            if upgradelightning1 == 5:
                coins1 -= 800
                if coins1 < 0:
                    coins1 += 800
                    upgradelightning1 -= 1
            if upgradelightning1 == 6:
                coins1 -= 500
                if coins1 < 0:
                    coins1 += 500
                    upgradelightning1 -= 1
            if upgradelightning1 == 7:
                coins1 -= 1000
                if coins1 < 0:
                    coins1 += 1000
                    upgradelightning1 -= 1
            if upgradelightning1 == 8:
                coins1 -= 2000
                if coins1 < 0:
                    coins1 += 1200
                    upgradelightning1 -= 1
            if upgradelightning1 == 9:
                coins1 -= 3000
                if coins1 < 0:
                    coins1 += 3000
                    upgradelightning1 -= 1
        if event.type == pygame.MOUSEBUTTONDOWN and 900 < mousex < 1050 and 500 < mousey < 540:
            slide = "main menu"
            shipx = 80
            shipy = 40
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
            shipx1 = 1000
            shipy1 = 500
            shipxx1 = 0
            shipyy1 = 3
            shiphit1 = 50
            bulletx1 = []
            bullety1 = []
            bulletxx1 = []
            bulletyy1 = []
            bulletdel1 = []
            bulletreload1 = 8
            bullshotdamage1 = 4
            shotgunacc1 = 60
            shotgunreload1 = 100
            shotgunbullets1 = 6
            laserx1 = []
            lasery1 = []
            laserxx1 = []
            laseryy1 = []
            laserdel1 = []
            laserreload1 = 60
            laserdamage1 = 3
            lasertimer1 = 0
            missilex1 = []
            missiley1 = []
            missilexx1 = []
            missileyy1 = []
            missiledel1 = []
            missilereload1 = 100
            missiledamage1 = 4
            missileradius1 = 150
            missiler1 = []
            missiletimer1 = 0
            missileshrapnel1 = 0
            minex1 = []
            miney1 = []
            minedel1 = []
            miner1 = []
            mineradius1 = 150
            minedamage1 = 3
            mineshrapnel1 = 0
            lightning1x1 = []
            lightning1y1 = []
            lightning2x1 = []
            lightning2y1 = []
            lightningtimer1 = 0
            lightreload1 = 200
            lightdamage1 = 1
            eshipx = []
            eshipy = []
            eshipxx = []
            eshipyy = []
            eshipdel = []
            eshiphit = []
            eshiphitt = []
            eshiptype = []
            eshipsum = []
            lightstruck = []
            stopwatch = 0
            minetimer = 0
            shoottimer = 0
            shotguntimer = 0
            shoot = False
            dropmine = False
            shoot1 = False
            dropmine1 = False
            aimturn = "?"
            aimturn1 = "?"
            aimturn2 = "?"
            score = 0
            score1 = 0
            alientimer = 0
            delay = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            slide = "main menu"
            coins = 1000
            coins1 = 1000
            upgradebullets = 1
            upgradeshotgun = 1
            upgradelasers = 1
            upgrademissiles = 1
            upgrademines = 1
            upgradelightning = 1
            upgradebullets1 = 1
            upgradeshotgun1 = 1
            upgradelasers1 = 1
            upgrademissiles1 = 1
            upgrademines1 = 1
            upgradelightning1 = 1
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
        #____________________________________________________________________________________________________________________________________________ Blitting text for upgrades
        screen.blit(cointext1, (100, 500))
        screen.blit(cointext, (200, 500))
        screen.blit(cointext1, (800, 470))
        screen.blit(cointext2, (900, 470))
        if mode == "easy":
            screen.blit(easy, (20, 470))
        if mode == "medium":
            screen.blit(medium, (20, 470))
        if mode == "hard":
            screen.blit(hard, (20, 470))
        if mode == "extreme":
            screen.blit(extreme, (20, 470))
        if mode == "one life":
            screen.blit(onelife, (20, 470))
        if mode == "half cash":
            screen.blit(halfcash, (20, 470))
        if mode == "explosions only":
            screen.blit(explosions, (20, 470))
        if mode == "triple":
            screen.blit(triplemode, (20, 470))
        screen.blit(bullet, (20, 20))
        screen.blit(shotgun, (20, 50))
        screen.blit(laser, (20, 80))
        screen.blit(missile, (20, 110))
        screen.blit(mine, (20, 140))
        screen.blit(lightning, (20, 170))
        screen.blit(bullet, (20, 200))
        screen.blit(shotgun, (20, 230))
        screen.blit(laser, (20, 260))
        screen.blit(missile, (20, 290))
        screen.blit(mine, (20, 320))
        screen.blit(lightning, (20, 350))
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
        if upgradebullets >= 8:
            screen.blit(maxupgrades, (180, 20))
            bullshotdamage = 8
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
        if upgradelasers >= 8:
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

        if upgradebullets1 == 1:
            screen.blit(bullet2, (180, 200))
        if upgradebullets1 == 2:
            screen.blit(bullet3, (180, 200))
            bulletreload1 = 6
        if upgradebullets1 == 3:
            screen.blit(bullet4, (180, 200))
            bullshotdamage1 = 5
        if upgradebullets1 == 4:
            screen.blit(bullet5, (180, 200))
        if upgradebullets1 == 5:
            screen.blit(bullet6, (180, 200))
        if upgradebullets1 == 6:
            screen.blit(bullet7, (180, 200))
            bulletreload1 = 4
        if upgradebullets1 == 7:
            screen.blit(bullet8, (180, 200))
        if upgradebullets1 >= 8:
            screen.blit(maxupgrades, (180, 200))
            bullshotdamage1 = 8
        if upgradeshotgun1 == 1:
            screen.blit(shotgun2, (180, 230))
        if upgradeshotgun1 == 2:
            screen.blit(shotgun3, (180, 230))
            shotgunbullets1 = 9
        if upgradeshotgun1 == 3:
            screen.blit(shotgun4, (180, 230))
            shotgunreload1 = 75
        if upgradeshotgun1 == 4:
            screen.blit(shotgun5, (180, 230))
            shotgunacc1 = 30
        if upgradeshotgun1 == 5:
            screen.blit(shotgun6, (180, 230))
            shotgunbullets1 = 15
        if upgradeshotgun1 == 6:
            screen.blit(shotgun7, (180, 230))
            shotgunreload1 = 50
        if upgradeshotgun1 == 7:
            screen.blit(shotgun8, (180, 230))
        if upgradeshotgun1 == 8:
            screen.blit(shotgun9, (180, 230))
            shotgunbullets1 = 30
        if upgradeshotgun1 >= 9:
            screen.blit(maxupgrades, (180, 230))
        if upgradelasers1 == 1:
            screen.blit(laser2, (180, 260))
        if upgradelasers1 == 2:
            screen.blit(laser3, (180, 260))
            laserreload1 = 45
        if upgradelasers1 == 3:
            screen.blit(laser4, (180, 260))
        if upgradelasers1 == 4:
            screen.blit(laser5, (180, 260))
            laserdamage1 = 4
        if upgradelasers1 == 5:
            screen.blit(laser6, (180, 260))
            laserreload1 = 30
        if upgradelasers1 == 6:
            screen.blit(laser7, (180, 260))
            laserreload1 = 20
        if upgradelasers1 == 7:
            screen.blit(laser8, (180, 260))
            laserdamage1 = 6
        if upgradelasers1 >= 8:
            screen.blit(maxupgrades, (180, 260))
        if upgrademissiles1 == 1:
            screen.blit(missile2, (180, 290))
        if upgrademissiles1 == 2:
            screen.blit(missile3, (180, 290))
            missilereload1 = 75
        if upgrademissiles1 == 3:
            screen.blit(missile4, (180, 290))
            missileradius1 = 200
        if upgrademissiles1 == 4:
            screen.blit(missile5, (180, 290))
            missileshrapnel1 = 20
        if upgrademissiles1 == 5:
            screen.blit(missile6, (180, 290))
        if upgrademissiles1 == 6:
            screen.blit(missile7, (180, 290))
            missileradius1 = 280
        if upgrademissiles1 == 7:
            screen.blit(missile8, (180, 290))
        if upgrademissiles1 == 8:
            screen.blit(missile9, (180, 290))
            missilereload1 = 45
        if upgrademissiles1 >= 9:
            screen.blit(maxupgrades, (180, 290))
            missileradius1 = 375
            missileshrapnel1 = 60
        if upgrademines1 == 1:
            screen.blit(mine2, (180, 320))
        if upgrademines1 == 2:
            screen.blit(mine3, (180, 320))
            mineradius1 = 240
        if upgrademines1 == 3:
            screen.blit(mine4, (180, 320))
            mineshrapnel1 = 20
        if upgrademines1 == 4:
            screen.blit(mine5, (180, 320))
            minedamage1 = 4
        if upgrademines1 == 5:
            screen.blit(mine6, (180, 320))
        if upgrademines1 == 6:
            screen.blit(mine7, (180, 320))
            mineradius1 = 330
        if upgrademines1 == 7:
            screen.blit(mine8, (180, 320))
            mineshrapnel1 = 60
        if upgrademines1 == 8:
            screen.blit(mine9, (180, 320))
            mineradius1 = 500
        if upgrademines1 >= 9:
            screen.blit(maxupgrades, (180, 320))
            minedamage1 = 7
        if upgradelightning1 == 1:
            screen.blit(lightning2, (180, 350))
        if upgradelightning1 == 2:
            screen.blit(lightning3, (180, 350))
            lightdamage1 = 1.6
        if upgradelightning1 == 3:
            screen.blit(lightning4, (180, 350))
            lightreload1 = 135
        if upgradelightning1 == 4:
            screen.blit(lightning5, (180, 350))
        if upgradelightning1 == 5:
            screen.blit(lightning6, (180, 350))
        if upgradelightning1 == 6:
            screen.blit(lightning7, (180, 350))
        if upgradelightning1 == 7:
            screen.blit(lightning8, (180, 350))
            lightreload1 = 75
        if upgradelightning1 == 8:
            screen.blit(lightning9, (180, 350))
            lightdamage1 = 3
        if upgradelightning1 >= 9:
            screen.blit(maxupgrades, (180, 350))

    if slide == "gameplay":
        alientimer -= 1

        #____________________________________________________________________________________________________________________________________________ creating enemies
        if alientimer <= 0:
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
            elif stopwatch < 9000:
                if choice < 40:
                    make_eship(0, random.randint(1, 540), random.randint(-6, 6) / 4, random.randint(-6, 6) / 4,
                               random.randint(1, 150), "splitttt")
                elif choice < 65:
                    make_eship(0, random.randint(1, 540), random.randint(-6, 6) / 4, random.randint(-6, 6) / 4,
                               random.randint(1, 190), "splittttt")
                elif choice < 80:
                    make_eship(0, random.randint(1, 540), random.randint(-6, 6) / 4, random.randint(-6, 6) / 4,
                               random.randint(1, 250), "splitttttt")
                elif choice < 91:
                    make_eship(0, random.randint(1, 540), random.randint(-6, 6) / 4, random.randint(-6, 6) / 4,
                               random.randint(1, 300), "splittttttt")
                else:
                    make_eship(0, random.randint(1, 540), random.randint(-6, 6) / 4, random.randint(-6, 6) / 4,
                               random.randint(1, 380), "splitttttttt")
            else:
                if choice < 50:
                    make_eship(0, random.randint(1, 540), random.randint(-6, 6) / 4, random.randint(-6, 6) / 4,
                               random.randint(1, 180+round(stopwatch/30)), "splitttttt")
                elif choice < 80:
                    make_eship(0, random.randint(1, 540), random.randint(-6, 6) / 4, random.randint(-6, 6) / 4,
                               random.randint(1, 240+round(stopwatch/30)), "splittttttt")
                else:
                    make_eship(0, random.randint(1, 540), random.randint(-6, 6) / 4, random.randint(-6, 6) / 4,
                               random.randint(1, 340+round(stopwatch/30)), "splitttttttt")
            alientimer = random.randint(1, 100)

        #____________________________________________________________________________________________________________________________________________ stopwatches, timers

        stopwatch += 1
        lightningtimer -= 1
        minetimer += 1
        shoottimer += 1
        shotguntimer += 1
        missiletimer += 1
        lasertimer += 1
        lightningtimer1 -= 1
        minetimer1 += 1
        shoottimer1 += 1
        shotguntimer1 += 1
        missiletimer1 += 1
        lasertimer1 += 1

        if (stopwatch / 100) % 1 == 0:
            if shiphit < 50 and mode != "one life":
                shiphit += 1
            if shiphit1 < 50 and mode != "one life":
                shiphit1 += 1

        if (stopwatch / 10) % 1 == 0:
            score += 1
            score1 += 1

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
                    laserx.append(shipx)
                    lasery.append(shipy)
                    laserxx.append(shipxx * 5)
                    laseryy.append(shipyy * 5)
                    laserdel.append(1)
                if 3 <= upgradelasers <= 7:
                    laserx.append(shipx)
                    lasery.append(shipy - 10)
                    laserxx.append(shipxx * 5)
                    laseryy.append(shipyy * 5)
                    laserdel.append(1)
                    laserx.append(shipx)
                    lasery.append(shipy + 10)
                    laserxx.append(shipxx * 5)
                    laseryy.append(shipyy * 5)
                    laserdel.append(1)
                if upgradelasers >= 8:
                    laserx.append(shipx)
                    lasery.append(shipy - 15)
                    laserxx.append(shipxx * 5)
                    laseryy.append(shipyy * 5)
                    laserdel.append(1)
                    laserx.append(shipx + 15)
                    lasery.append(shipy)
                    laserxx.append(shipxx * 5)
                    laseryy.append(shipyy * 5)
                    laserdel.append(1)
                    laserx.append(shipx - 15)
                    lasery.append(shipy)
                    laserxx.append(shipxx * 5)
                    laseryy.append(shipyy * 5)
                    laserdel.append(1)
                    laserx.append(shipx)
                    lasery.append(shipy + 15)
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

        if shoottimer1 >= bulletreload1:
            if shoot1 == True:
                if upgradebullets1 <= 3:
                    bulletx1.append(shipx1)
                    bullety1.append(shipy1)
                    bulletxx1.append(shipxx1 * 5)
                    bulletyy1.append(shipyy1 * 5)
                    bulletdel1.append(1)
                if upgradebullets1 >= 7:
                    bulletx1.append(shipx1)
                    bullety1.append(shipy1)
                    bulletxx1.append(shipxx1 * 12)
                    bulletyy1.append(shipyy1 * 12)
                    bulletdel1.append(1)
                if upgradebullets1 == 4:
                    bulletx1.append(shipx1)
                    bullety1.append(shipy1 - 10)
                    bulletxx1.append(shipxx1 * 5)
                    bulletyy1.append(shipyy1 * 5)
                    bulletdel1.append(1)
                    bulletx1.append(shipx1)
                    bullety1.append(shipy1 + 10)
                    bulletxx1.append(shipxx1 * 5)
                    bulletyy1.append(shipyy1 * 5)
                    bulletdel1.append(1)
                if upgradebullets1 >= 5:
                    bulletx1.append(shipx1)
                    bullety1.append(shipy1 - 10)
                    bulletxx1.append(shipxx1 * 12)
                    bulletyy1.append(shipyy1 * 12)
                    bulletdel1.append(1)
                    bulletx1.append(shipx1)
                    bullety1.append(shipy1 + 10)
                    bulletxx1.append(shipxx1 * 12)
                    bulletyy1.append(shipyy1 * 12)
                    bulletdel1.append(1)
                if gunsounds == True:
                    pygame.mixer.Sound.play(gunsound)
                shoottimer1 = 0

        if lasertimer1 >= laserreload1:
            if shoot1 == True:
                if upgradelasers1 <= 2:
                    laserx1.append(shipx1)
                    lasery1.append(shipy1)
                    laserxx1.append(shipxx1 * 5)
                    laseryy1.append(shipyy1 * 5)
                    laserdel1.append(1)
                if 3 <= upgradelasers1 <= 7:
                    laserx1.append(shipx1)
                    lasery1.append(shipy1 - 10)
                    laserxx1.append(shipxx1 * 5)
                    laseryy1.append(shipyy1 * 5)
                    laserdel1.append(1)
                    laserx1.append(shipx1)
                    lasery1.append(shipy1 + 10)
                    laserxx1.append(shipxx1 * 5)
                    laseryy1.append(shipyy1 * 5)
                    laserdel1.append(1)
                if upgradelasers1 >= 8:
                    laserx1.append(shipx1)
                    lasery1.append(shipy1 - 15)
                    laserxx1.append(shipxx1 * 5)
                    laseryy1.append(shipyy1 * 5)
                    laserdel1.append(1)
                    laserx1.append(shipx1 + 15)
                    lasery1.append(shipy1)
                    laserxx1.append(shipxx1 * 5)
                    laseryy1.append(shipyy1 * 5)
                    laserdel1.append(1)
                    laserx1.append(shipx1 - 15)
                    lasery1.append(shipy1)
                    laserxx1.append(shipxx1 * 5)
                    laseryy1.append(shipyy1 * 5)
                    laserdel1.append(1)
                    laserx1.append(shipx1)
                    lasery1.append(shipy1 + 15)
                    laserxx1.append(shipxx1 * 5)
                    laseryy1.append(shipyy1 * 5)
                    laserdel1.append(1)
                lasertimer1 = 0

        if missiletimer1 >= missilereload1:
            if shoot1 == True:
                if upgrademissiles1 <= 4:
                    missilex1.append(shipx1)
                    missiley1.append(shipy1)
                    missilexx1.append(shipxx1 * 5)
                    missileyy1.append(shipyy1 * 5)
                    missiledel1.append(1)
                    missiler1.append(1)
                if 5 <= upgrademissiles1 <= 6:
                    missilex1.append(shipx1+10)
                    missiley1.append(shipy1+10)
                    missilexx1.append(shipxx1 * 5)
                    missileyy1.append(shipyy1 * 5)
                    missiledel1.append(1)
                    missiler1.append(1)
                    missilex1.append(shipx1 - 10)
                    missiley1.append(shipy1 - 10)
                    missilexx1.append(shipxx1 * 5)
                    missileyy1.append(shipyy1 * 5)
                    missiledel1.append(1)
                    missiler1.append(1)
                if upgrademissiles1 >= 7:
                    missilex1.append(shipx1 + 10)
                    missiley1.append(shipy1 + 10)
                    missilexx1.append(shipxx1 * 12)
                    missileyy1.append(shipyy1 * 12)
                    missiledel1.append(1)
                    missiler1.append(1)
                    missilex1.append(shipx1 - 10)
                    missiley1.append(shipy1 - 10)
                    missilexx1.append(shipxx1 * 12)
                    missileyy1.append(shipyy1 * 12)
                    missiledel1.append(1)
                    missiler1.append(1)
                missiletimer1 = 0

        if shotguntimer1 >= shotgunreload1:
            if shoot1 == True:
                for cat in range(0, shotgunbullets1):
                    if upgradeshotgun1 <= 6:
                        bulletx1.append(shipx1)
                        bullety1.append(shipy1)
                        bulletxx1.append(random.randint(round(50 * shipxx1 - shotgunacc1), round(50 * shipxx1 + shotgunacc1)) / 10)
                        bulletyy1.append(random.randint(round(50 * shipyy1 - shotgunacc1), round(50 * shipyy1 + shotgunacc1)) / 10)
                        bulletdel1.append(1)
                    if upgradeshotgun1 >= 7:
                        bulletx1.append(shipx1)
                        bullety1.append(shipy1)
                        bulletxx1.append(random.randint(round(120 * shipxx1 - shotgunacc1), round(120 * shipxx1 + shotgunacc1)) / 10)
                        bulletyy1.append(random.randint(round(120 * shipyy1 - shotgunacc1), round(120 * shipyy1 + shotgunacc1)) / 10)
                        bulletdel1.append(1)
                if shotgunsounds == True:
                    pygame.mixer.Sound.play(shotgunsound)
                shotguntimer1 = 0


        if minetimer1 > 30:
            if dropmine1 == True:
                minex1.append(shipx1)
                miney1.append(shipy1)
                minedel1.append(1)
                miner1.append(1)
                minetimer1 = 0

        for cat in range(0, len(eshipx)):
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
                if 6 <= upgradelightning <= 8:
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
                if upgradelightning >= 9:
                    for monkey in range(0, 5):
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

            if (stopwatch / lightreload1) % 1 == 0 and mode != "explosions only" and shoot1 == True:
                lightningtimer1 = 10
                if abs(eshipx[cat] - shipx1) < 200 and abs(eshipy[cat] - shipy1) < 200 or upgradelightning1 >= 4 and abs(
                        eshipx[cat] - shipx1) < 350 and abs(eshipy[cat] - shipy1) < 350:
                    lightning1x1.append(shipx1)
                    lightning1y1.append(shipy1)
                    lightning2x1.append(eshipx[cat])
                    lightning2y1.append(eshipy[cat])
                    lightstruck1[cat] += 1
                if upgradelightning1 <= 5:
                    for dog in range(0, len(eshipx)):
                        if cat != dog and lightstruck1[cat] >= 1:
                            if abs(eshipx[cat] - eshipx[dog]) < 200 and abs(
                                    eshipy[cat] - eshipy[dog]) < 200 or upgradelightning1 >= 4 and abs(
                                    eshipx[cat] - eshipx[dog]) < 350 and abs(eshipy[cat] - eshipy[dog]) < 350:
                                lightning1x1.append(eshipx[dog])
                                lightning1y1.append(eshipy[dog])
                                lightning2x1.append(eshipx[cat])
                                lightning2y1.append(eshipy[cat])
                                lightstruck1[dog] += 1
                if 6 <= upgradelightning1 <= 8:
                    for monkey in range(0, 2):
                        for dog in range(0, len(eshipx)):
                            if cat != dog and lightstruck1[cat] >= 1:
                                if abs(eshipx[cat] - eshipx[dog]) < 200 and abs(
                                        eshipy[cat] - eshipy[dog]) < 200 or upgradelightning1 >= 4 and abs(
                                        eshipx[cat] - eshipx[dog]) < 350 and abs(eshipy[cat] - eshipy[dog]) < 350:
                                    lightning1x1.append(eshipx[dog])
                                    lightning1y1.append(eshipy[dog])
                                    lightning2x1.append(eshipx[cat])
                                    lightning2y1.append(eshipy[cat])
                                    lightstruck1[dog] += 1
                if upgradelightning1 >= 9:
                    for monkey in range(0, 5):
                        for dog in range(0, len(eshipx)):
                            if cat != dog and lightstruck1[cat] >= 1:
                                if abs(eshipx[cat] - eshipx[dog]) < 200 and abs(
                                        eshipy[cat] - eshipy[dog]) < 200 or upgradelightning1 >= 4 and abs(
                                        eshipx[cat] - eshipx[dog]) < 350 and abs(eshipy[cat] - eshipy[dog]) < 350:
                                    lightning1x1.append(eshipx[dog])
                                    lightning1y1.append(eshipy[dog])
                                    lightning2x1.append(eshipx[cat])
                                    lightning2y1.append(eshipy[cat])
                                    lightstruck1[dog] += 1
        for cat in range(0, len(eshipx)):
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
            if (stopwatch / 200) % 1 == 0 and mode == "easy":
                ebulletx.append(eshipx[cat])
                ebullety.append(eshipy[cat])
                ebulletxx.append(eshipxx[cat] * 3)
                ebulletyy.append(eshipyy[cat] * 3)
                ebulletdel.append(1)
            if mode == "medium" or mode == "one life" or mode == "half cash" or mode == "explosions only" or mode == "triple":
                if (stopwatch / 150) % 1 == 0:
                    ebulletx.append(eshipx[cat])
                    ebullety.append(eshipy[cat])
                    ebulletxx.append(eshipxx[cat] * 4)
                    ebulletyy.append(eshipyy[cat] * 4)
                    ebulletdel.append(1)
            if (stopwatch / 125) % 1 == 0 and mode == "hard":
                ebulletx.append(eshipx[cat])
                ebullety.append(eshipy[cat])
                ebulletxx.append(eshipxx[cat] * 5)
                ebulletyy.append(eshipyy[cat] * 5)
                ebulletdel.append(1)
            if (stopwatch / 100) % 1 == 0 and mode == "extreme":
                ebulletx.append(eshipx[cat])
                ebullety.append(eshipy[cat])
                ebulletxx.append(eshipxx[cat] * 7)
                ebulletyy.append(eshipyy[cat] * 7)
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

        for cat in range(0, len(bulletx1)):
            bulletx1[cat] += bulletxx1[cat]
            bullety1[cat] += bulletyy1[cat]

        for cat in range(0, len(laserx1)):
            laserx1[cat] += laserxx1[cat]
            lasery1[cat] += laseryy1[cat]

        for cat in range(0, len(missilex1)):
            if missiledel1[cat] == 1:
                missilex1[cat] += missilexx1[cat]
                missiley1[cat] += missileyy1[cat]

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
                if random.randint(1, 2) == 2:
                    if eshipxx[cat] > 0 and (shipx - eshipx[cat]) > 0 or (shipx - eshipx[cat]) < 0 and eshipxx[cat] < 0:
                        if eshipyy[cat] / eshipxx[cat] < (shipy - eshipy[cat]) / (shipx - eshipx[cat]):
                            aimturn2 = "right"
                        if eshipyy[cat] / eshipxx[cat] > (shipy - eshipy[cat]) / (shipx - eshipx[cat]):
                            aimturn2 = "left"
                    if eshipxx[cat] > 0 and (shipx - eshipx[cat]) < 0 or (shipx - eshipx[cat]) > 0 and eshipxx[cat] < 0:
                        if eshipyy[cat] / eshipxx[cat] < (shipy - eshipy[cat]) / (shipx - eshipx[cat]):
                            aimturn2 = "left"
                        if eshipyy[cat] / eshipxx[cat] > (shipy - eshipy[cat]) / (shipx - eshipx[cat]):
                            aimturn2 = "right"
                else:
                    if eshipxx[cat] > 0 and (shipx1 - eshipx[cat]) > 0 or (shipx1 - eshipx[cat]) < 0 and eshipxx[cat] < 0:
                        if eshipyy[cat] / eshipxx[cat] < (shipy1 - eshipy[cat]) / (shipx1 - eshipx[cat]):
                            aimturn2 = "right"
                        if eshipyy[cat] / eshipxx[cat] > (shipy1 - eshipy[cat]) / (shipx1 - eshipx[cat]):
                            aimturn2 = "left"
                    if eshipxx[cat] > 0 and (shipx - eshipx[cat]) < 0 or (shipx - eshipx[cat]) > 0 and eshipxx[cat] < 0:
                        if eshipyy[cat] / eshipxx[cat] < (shipy1 - eshipy[cat]) / (shipx1 - eshipx[cat]):
                            aimturn2 = "left"
                        if eshipyy[cat] / eshipxx[cat] > (shipy1 - eshipy[cat]) / (shipx1 - eshipx[cat]):
                            aimturn2 = "right"
                if aimturn2 == "left":
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
                if aimturn2 == "right":
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

        if aimturn1 == "left":
            if shipxx1 < 0 and shipyy1 < 0:
                shipxx1 -= 0.04
                shipyy1 += 0.04
            if shipxx1 < 0 and shipyy1 >= 0:
                shipxx1 += 0.04
                shipyy1 += 0.04
            if shipxx1 >= 0 and shipyy1 < 0:
                shipxx1 -= 0.04
                shipyy1 -= 0.04
            if shipxx1 >= 0 and shipyy1 >= 0:
                shipxx1 += 0.04
                shipyy1 -= 0.04
        if aimturn1 == "right":
            if shipxx1 < 0 and shipyy1 < 0:
                shipxx1 += 0.04
                shipyy1 -= 0.04
            if shipxx1 < 0 and shipyy1 >= 0:
                shipxx1 -= 0.04
                shipyy1 -= 0.04
            if shipxx1 >= 0 and shipyy1 < 0:
                shipxx1 += 0.04
                shipyy1 += 0.04
            if shipxx1 >= 0 and shipyy1 >= 0:
                shipxx1 -= 0.04
                shipyy1 += 0.04

        shipxx1 = round(shipxx1, 2)
        shipyy1 = round(shipyy1, 2)

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

        if abs(shipxx1) + abs(shipyy1) > 3:
            if shipxx1 > 0:
                shipxx1 -= 0.01
            if shipxx1 < 0:
                shipxx1 += 0.01
            if shipyy1 > 0:
                shipyy1 -= 0.01
            if shipyy1 < 0:
                shipyy1 += 0.01

        shipx1 += shipxx1
        shipy1 += shipyy1
        if shipx1 > 1080:
            shipx1 = 0
        if shipx1 < 0:
            shipx1 = 1080
        if shipy1 > 540:
            shipy1 = 0
        if shipy1 < 0:
            shipy1 = 540

        #_______________________________________________________________________________________________________________________________________Collisions, damage, deletion

        for cat in range(0, 5):
            if len(eshipx) > 50:
                eshipdel[0] = 0
                shiphit -= 0.05
                shiphit1 -= 0.05

        for cat in range(0, len(bulletx)):
            for dog in range(0, len(eshipdel)):
                if abs(eshipx[dog] - bulletx[cat]) < 25 and abs(eshipy[dog] - bullety[cat]) < 25:
                    bulletdel[cat] = 0
                    eshiphit[dog] -= bullshotdamage
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
                    if eshiphit[dog] <= 0:
                        eshipdel[dog] = 0


        for cat in range(0, len(bulletx1)):
            for dog in range(0, len(eshipdel)):
                if abs(eshipx[dog] - bulletx1[cat]) < 25 and abs(eshipy[dog] - bullety1[cat]) < 25:
                    bulletdel1[cat] = 0
                    eshiphit[dog] -= bullshotdamage1
                    if upgradeshotgun1 >= 9 and (shipx1 - eshipx[dog]) != 0:
                        ratio2 = (shipy1 - eshipy[dog]) / (shipx1 - eshipx[dog])
                        if (eshipy[dog] - shipy1) < 0 and (eshipx[dog] - shipx1) < 0:
                            eshipy[dog] -= (round(ratio2 * math.sqrt(300 / (ratio2 ** 2 + 1)), 3))
                            eshipx[dog] -= (round(math.sqrt(300 / (ratio2 ** 2 + 1)), 3))
                        if (eshipy[dog] - shipy1) >= 0 and (eshipx[dog] - shipx1) >= 0:
                            eshipy[dog] -= (-round(ratio2 * math.sqrt(300 / (ratio2 ** 2 + 1)), 3))
                            eshipx[dog] -= (-round(math.sqrt(300 / (ratio2 ** 2 + 1)), 3))
                        if (eshipx[dog] - shipx1) < 0 and (eshipy[dog] - shipy1) >= 0:
                            eshipy[dog] -= (round(ratio2 * math.sqrt(300 / (ratio2 ** 2 + 1)), 3))
                            eshipx[dog] -= (round(math.sqrt(300 / (ratio2 ** 2 + 1)), 3))
                        if (eshipx[dog] - shipx1) >= 0 and (eshipy[dog] - shipy1) < 0:
                            eshipy[dog] -= (-round(ratio2 * math.sqrt(300 / (ratio2 ** 2 + 1)), 3))
                            eshipx[dog] -= (-round(math.sqrt(300 / (ratio2 ** 2 + 1)), 3))
                    if eshiphit[dog] <= 0:
                        eshipdel[dog] = 2

        for cat in range(0, len(laserx)):
            for dog in range(0, len(eshipdel)):
                if abs(eshipx[dog] - laserx[cat]) < 25 and abs(eshipy[dog] - lasery[cat]) < 25:
                    eshiphit[dog] -= laserdamage
                    if eshiphit[dog] <= 0:
                        eshipdel[dog] = 0

        for cat in range(0, len(missilex)):
            for dog in range(0, len(eshipdel)):
                if abs(eshipx[dog] - missilex[cat]) < 25 and abs(eshipy[dog] - missiley[cat]) < 25:
                    missiledel[cat] = 2

        for cat in range(0, len(laserx1)):
            for dog in range(0, len(eshipdel)):
                if abs(eshipx[dog] - laserx1[cat]) < 25 and abs(eshipy[dog] - lasery1[cat]) < 25:
                    eshiphit[dog] -= laserdamage1
                    if eshiphit[dog] <= 0:
                        eshipdel[dog] = 2

        for cat in range(0, len(missilex1)):
            for dog in range(0, len(eshipdel)):
                if abs(eshipx[dog] - missilex1[cat]) < 25 and abs(eshipy[dog] - missiley1[cat]) < 25:
                    missiledel1[cat] = 2

        for cat in range(0, len(eshipdel)):
            for dog in range(0, len(minex)):
                if abs(eshipx[cat] - minex[dog]) < 40 and abs(eshipy[cat] - miney[dog]) < 40:
                    minedel[dog] = 2
            for dog in range(0, len(minex1)):
                if abs(eshipx[cat] - minex1[dog]) < 40 and abs(eshipy[cat] - miney1[dog]) < 40:
                    minedel1[dog] = 2
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

        for cat in range(0, len(missilex1)):
            if missilex1[cat] > 1080 and missiledel1[cat] == 1:
                missiledel1[cat] = 2
            if missilex1[cat] < 0 and missiledel1[cat] == 1:
                missiledel1[cat] = 2
            if missiley1[cat] > 540 and missiledel1[cat] == 1:
                missiledel1[cat] = 2
            if missiley1[cat] < 0 and missiledel1[cat] == 1:
                missiledel1[cat] = 2

        for cat in range(0, len(bulletx)):
            if abs(bulletx[cat] - shipx1) < 24 and abs(bullety[cat] - shipy1) < 24:
                bulletdel[cat] = 0
                shiphit1 -= bullshotdamage/5

        for cat in range(0, len(bulletx1)):
            if abs(bulletx1[cat] - shipx) < 24 and abs(bullety1[cat] - shipy) < 24:
                bulletdel1[cat] = 0
                shiphit -= bullshotdamage1/5

        for cat in range(0, len(laserx)):
            if abs(laserx[cat] - shipx1) < 24 and abs(lasery[cat] - shipy1) < 24:
                shiphit1 -= laserdamage / 5

        for cat in range(0, len(laserx1)):
            if abs(laserx1[cat] - shipx) < 24 and abs(lasery1[cat] - shipy) < 24:
                shiphit -= laserdamage1 / 5

        for cat in range(0, len(missilex)):
            if abs(missilex[cat] - shipx1) < 24 and abs(missiley[cat] - shipy1) < 24:
                missiledel[cat] = 2

        for cat in range(0, len(missilex1)):
            if abs(missilex1[cat] - shipx) < 24 and abs(missiley1[cat] - shipy) < 24:
                missiledel1[cat] = 2

        for cat in range(0, len(minex)):
            if abs(minex[cat] - shipx1) < 24 and abs(miney[cat] - shipy1) < 24:
                minedel[cat] = 2

        for cat in range(0, len(minex1)):
            if abs(minex1[cat] - shipx) < 24 and abs(miney1[cat] - shipy) < 24:
                minedel1[cat] = 2

        for cat in range(0, len(minex)):
            if minedel[cat] == 2:
                for dog in range(0, len(eshipx)):
                    if abs(eshipx[dog] - minex[cat]) <= miner[cat]:
                        if abs(eshipy[dog] - miney[cat]) <= miner[cat]:
                            eshiphit[dog] -= minedamage
                            if eshiphit[dog] <= 0:
                                eshipdel[dog] = 0
                if abs(shipx - minex[cat]) <= miner[cat]:
                    if abs(shipy - miney[cat]) <= miner[cat]:
                        shiphit -= 0.3
                        if upgrademines >= 5:
                            shiphit += 0.2
                if abs(shipx1 - minex[cat]) <= miner[cat]:
                    if abs(shipy1 - miney[cat]) <= miner[cat]:
                        shiphit1 -= 0.5
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
                            if eshiphit[dog] <= 0:
                                eshipdel[dog] = 0
                if abs(shipx - missilex[cat]) <= missiler[cat]:
                    if abs(shipy - missiley[cat]) <= missiler[cat]:
                        shiphit -= 0.1
                if abs(shipx1 - missilex[cat]) <= missiler[cat]:
                    if abs(shipy1 - missiley[cat]) <= missiler[cat]:
                        shiphit1 -= 0.15
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

        for cat in range(0, len(minex1)):
            if minedel1[cat] == 2:
                for dog in range(0, len(eshipx)):
                    if abs(eshipx[dog] - minex1[cat]) <= miner1[cat]:
                        if abs(eshipy[dog] - miney1[cat]) <= miner1[cat]:
                            eshiphit[dog] -= minedamage1
                            if eshiphit[dog] <= 0:
                                eshipdel[dog] = 2
                if abs(shipx1 - minex1[cat]) <= miner1[cat]:
                    if abs(shipy1 - miney1[cat]) <= miner1[cat]:
                        shiphit1 -= 0.3
                        if upgrademines1 >= 5:
                            shiphit1 += 0.2
                if abs(shipx - minex1[cat]) <= miner1[cat]:
                    if abs(shipy - miney1[cat]) <= miner1[cat]:
                        shiphit -= 0.5
                miner1[cat] += 25
                if miner1[cat] > mineradius1:
                    minedel1[cat] = 0
                    #________________________________________________________________________________________________This part is really for making shrapnel.
                    if minesounds == True:
                        pygame.mixer.Sound.play(explosionsound)
                    for dog in range(0, mineshrapnel1):
                        randomx = random.randint(-9, 9)
                        randomy = random.randint(-9, 9)
                        bulletx1.append(minex1[cat])
                        bullety1.append(miney1[cat])
                        bulletxx1.append(randomx)
                        bulletyy1.append(randomy)
                        bulletdel1.append(1)

        for cat in range(0, len(missilex1)):
            if missiledel1[cat] == 2:
                for dog in range(0, len(eshipx)):
                    if abs(eshipx[dog] - missilex1[cat]) <= missiler1[cat]:
                        if abs(eshipy[dog] - missiley1[cat]) <= missiler1[cat]:
                            eshiphit[dog] -= missiledamage1
                            if eshiphit[dog] <= 0:
                                eshipdel[dog] = 2
                if abs(shipx1 - missilex1[cat]) <= missiler1[cat]:
                    if abs(shipy1 - missiley1[cat]) <= missiler1[cat]:
                        shiphit1 -= 0.1
                if abs(shipx - missilex1[cat]) <= missiler1[cat]:
                    if abs(shipy - missiley1[cat]) <= missiler1[cat]:
                        shiphit -= 0.15
                missiler1[cat] += 25
                if missiler1[cat] > missileradius1:
                    missiledel1[cat] = 0
                    #________________________________________________________________________________________________This part is really for making shrapnel.
                    if minesounds == True:
                        pygame.mixer.Sound.play(explosionsound)
                    for dog in range(0, missileshrapnel1):
                        randomx = random.randint(-9, 9)
                        randomy = random.randint(-9, 9)
                        bulletx1.append(missilex1[cat])
                        bullety1.append(missiley1[cat])
                        bulletxx1.append(randomx)
                        bulletyy1.append(randomy)
                        bulletdel1.append(1)

        for cat in range(0, len(eshipdel)):
            while lightstruck[cat] >= 1 and upgradelightning <= 4:
                eshiphit[cat] -= lightdamage
                lightstruck[cat] -= 1
                if eshiphit[cat] <= 0:
                    eshipdel[cat] = 0
            while lightstruck[cat] >= 1 and 5 <= upgradelightning <= 8:
                eshiphit[cat] -= lightdamage
                lightstruck[cat] -= 1
                if eshiphit[cat] <= 0:
                    eshipdel[cat] = 0
                if upgradelightning != 5:
                    eshipstuntimer[cat] = 20
            while lightstruck[cat] >= 1 and upgradelightning >= 9:
                eshiphit[cat] -= lightdamage
                lightstruck[cat] -= 1
                eshipstuntimer[cat] = 30
                if eshiphit[cat] <= 0:
                    eshipdel[cat] = 0

        for cat in range(0, len(eshipdel)):
            while lightstruck1[cat] >= 1 and upgradelightning1 <= 4:
                eshiphit[cat] -= lightdamage1
                lightstruck1[cat] -= 1
                if eshiphit[cat] <= 0:
                    eshipdel[cat] = 2
            while lightstruck1[cat] >= 1 and 5 <= upgradelightning1 <= 8:
                eshiphit[cat] -= lightdamage1
                lightstruck1[cat] -= 1
                if eshiphit[cat] <= 0:
                    eshipdel[cat] = 2
                if upgradelightning1 != 5:
                    eshipstuntimer[cat] = 20
            while lightstruck1[cat] >= 1 and upgradelightning1 >= 9:
                eshiphit[cat] -= lightdamage1
                lightstruck1[cat] -= 1
                eshipstuntimer[cat] = 30
                if eshiphit[cat] <= 0:
                    eshipdel[cat] = 2

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

        for cat in range(0, len(bulletx1)):
            if bulletx1[cat] > 1080:
                bulletdel1[cat] = 0
            if bulletx1[cat] < 0:
                bulletdel1[cat] = 0
            if bullety1[cat] > 540:
                bulletdel1[cat] = 0
            if bullety1[cat] < 0:
                bulletdel1[cat] = 0

        for cat in range(0, len(laserx1)):
            if laserx1[cat] > 1080:
                laserdel1[cat] = 0
            if laserx1[cat] < 0:
                laserdel1[cat] = 0
            if lasery1[cat] > 540:
                laserdel1[cat] = 0
            if lasery1[cat] < 0:
                laserdel1[cat] = 0

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
            if abs(shipx1 - ebulletx[cat]) < 25 and abs(shipy1 - ebullety[cat]) < 25:
                shiphit1 -= 1
                ebulletdel[cat] = 0

        for cat in range(0, len(eshipdel)):
            if eshiphit[cat] <= 0:
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
                if eshiptype[cat] == "splittt" and stopwatch < 9000:
                    make_eship(eshipx[cat], eshipy[cat] - 10, eshipxx[cat], eshipyy[cat], round(1 + eshiphitt[cat] / 2),
                               "splitt")
                    make_eship(eshipx[cat], eshipy[cat] + 10, eshipxx[cat], eshipyy[cat], round(1 + eshiphitt[cat] / 2),
                               "splitt")
                    if mode == "triple":
                        make_eship(eshipx[cat], eshipy[cat] + 10, eshipxx[cat], eshipyy[cat],
                                   round(1 + eshiphitt[cat] / 2),
                                   "splitt")
                if eshiptype[cat] == "splitttt":
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

        for dog in range(0, len(eshipdel)):
            for cat in range(0, len(eshipdel)):
                if eshipdel[cat] == 0:
                    if shiphit > 0:
                        score += eshiphitt[cat]
                        coins += eshiphitt[cat]
                        if stopwatch > 3000:
                            coins -= eshiphitt[cat]/2
                        if stopwatch > 4500:
                            coins -= eshiphitt[cat]/4
                        if mode == "half cash":
                            if stopwatch <= 3000:
                                coins -= eshiphitt[cat]/2
                            if 3000 < stopwatch <= 4500:
                                coins -= eshiphitt[cat] / 4
                            if stopwatch > 4500:
                                coins -= eshiphitt[cat] / 8
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
                    del lightstruck1[cat]
                    del eshipstuntimer[cat]
                    break

        for dog in range(0, len(eshipdel)):
            for cat in range(0, len(eshipdel)):
                if eshipdel[cat] == 2:
                    if shiphit1 > 0:
                        score1 += eshiphitt[cat]
                        coins1 += eshiphitt[cat]
                        if stopwatch > 3000:
                            coins1 -= eshiphitt[cat]/2
                        if stopwatch > 4500:
                            coins1 -= eshiphitt[cat]/4
                        if mode == "half cash":
                            if stopwatch <= 3000:
                                coins1 -= eshiphitt[cat]/2
                            if 3000 < stopwatch <= 4500:
                                coins1 -= eshiphitt[cat] / 4
                            if stopwatch > 4500:
                                coins1 -= eshiphitt[cat] / 8
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
                    del lightstruck1[cat]
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

        for dog in range(0, len(bulletx1)):
            for cat in range(0, len(bulletx1)):
                if bulletdel1[cat] == 0:
                    del bulletx1[cat]
                    del bullety1[cat]
                    del bulletxx1[cat]
                    del bulletyy1[cat]
                    del bulletdel1[cat]
                    break

        for dog in range(0, len(laserx1)):
            for cat in range(0, len(laserx1)):
                if laserdel1[cat] == 0:
                    del laserx1[cat]
                    del lasery1[cat]
                    del laserxx1[cat]
                    del laseryy1[cat]
                    del laserdel1[cat]
                    break

        for dog in range(0, len(missilex1)):
            for cat in range(0, len(missilex1)):
                if missiledel1[cat] == 0:
                    del missilex1[cat]
                    del missiley1[cat]
                    del missilexx1[cat]
                    del missileyy1[cat]
                    del missiledel1[cat]
                    del missiler1[cat]
                    break

        for dog in range(0, len(minex1)):
            for cat in range(0, len(minex1)):
                if minedel1[cat] == 0:
                    del minex1[cat]
                    del miney1[cat]
                    del minedel1[cat]
                    del miner1[cat]
                    break

        #____________________________________________________________________________________________________________________________________________drawing

        screen.blit(scoretext, (100, 250))
        screen.blit(cointext, (100, 230))
        screen.blit(scoretext1, (900, 250))
        screen.blit(cointext2, (900, 230))

        for cat in range(0, len(lightning1x)):
            if lightningtimer <= 10:
                pygame.draw.line(screen,
                                 (5 + 25 * lightningtimer, 5 + 25 * lightningtimer, 5 + 25 * lightningtimer),
                                 (lightning1x[cat], lightning1y[cat]),
                                 (lightning2x[cat], lightning2y[cat]), 6)

        for cat in range(0, len(bulletx)):
            pygame.draw.circle(screen, (255, 255, 255), (round(bulletx[cat]), round(bullety[cat])), 5)

        for cat in range(0, len(laserx)):
            pygame.draw.line(screen, (255, 0, 0), (round(laserx[cat]), round(lasery[cat])),
                                 (round(laserx[cat] - 4 * laserxx[cat]), round(lasery[cat] - 4 * laseryy[cat])), 6)

        for cat in range(0, len(missilex)):
            pygame.draw.circle(screen, (255, 0, 0), (round(missilex[cat]), round(missiley[cat])), 8)

        coins = round(coins)

        pygame.draw.circle(screen, (255, 0, 0), (round(shipx), round(shipy)), 20)
        pygame.draw.rect(screen, (255, 255, 255), (round(shipx) - 25, round(shipy) + 30, 50, 4))
        if shiphit > 0:
            pygame.draw.rect(screen, (255, 0, 0), (round(shipx) - 25, round(shipy) + 30, round(shiphit), 4))

        for cat in range(0, len(minex)):
            if miner[cat] == 1:
                pygame.draw.circle(screen, (255, 255, 255), (round(minex[cat]), round(miney[cat])), 15)
            if minedel[cat] == 2:
                if miner[cat] > 20:
                    pygame.draw.circle(screen, (255, 0, 0), (round(minex[cat]), round(miney[cat])), round(miner[cat]), 20)
                else:
                    pygame.draw.circle(screen, (255, 0, 0), (round(minex[cat]), round(miney[cat])), round(miner[cat]))

        for cat in range(0, len(missilex)):
            if missiler[cat] == 1:
                pygame.draw.circle(screen, (255, 0, 0), (round(missilex[cat]), round(missiley[cat])), 8)
            if missiledel[cat] == 2:
                if missiler[cat] > 20:
                    pygame.draw.circle(screen, (255, 0, 0), (round(missilex[cat]), round(missiley[cat])), round(missiler[cat]), 20)
                else:
                    pygame.draw.circle(screen, (255, 0, 0), (round(missilex[cat]), round(missiley[cat])), round(missiler[cat]))

        for cat in range(0, len(lightning1x1)):
            if lightningtimer1 <= 10:
                pygame.draw.line(screen,
                                 (5 + 25 * lightningtimer1, 5 + 25 * lightningtimer1, 5 + 25 * lightningtimer1),
                                 (lightning1x1[cat], lightning1y1[cat]),
                                 (lightning2x1[cat], lightning2y1[cat]), 6)

        for cat in range(0, len(bulletx1)):
            pygame.draw.circle(screen, (255, 255, 255), (round(bulletx1[cat]), round(bullety1[cat])), 5)

        for cat in range(0, len(laserx1)):
            pygame.draw.line(screen, (255, 0, 0), (round(laserx1[cat]), round(lasery1[cat])),
                             (round(laserx1[cat] - 4 * laserxx1[cat]), round(lasery1[cat] - 4 * laseryy1[cat])), 6)

        for cat in range(0, len(missilex1)):
            pygame.draw.circle(screen, (255, 0, 0), (round(missilex1[cat]), round(missiley1[cat])), 8)

        coins1 = round(coins1)

        pygame.draw.circle(screen, (255, 255, 0), (round(shipx1), round(shipy1)), 20)
        pygame.draw.rect(screen, (255, 255, 255), (round(shipx1) - 25, round(shipy1) + 30, 50, 4))
        if shiphit1 > 0:
            pygame.draw.rect(screen, (255, 0, 0), (round(shipx1) - 25, round(shipy1) + 30, round(shiphit1), 4))

        for cat in range(0, len(minex1)):
            if miner1[cat] == 1:
                pygame.draw.circle(screen, (255, 255, 255), (round(minex1[cat]), round(miney1[cat])), 15)
            if minedel1[cat] == 2:
                if miner1[cat] > 20:
                    pygame.draw.circle(screen, (255, 0, 0), (round(minex1[cat]), round(miney1[cat])), round(miner1[cat]),
                                       20)
                else:
                    pygame.draw.circle(screen, (255, 0, 0), (round(minex1[cat]), round(miney1[cat])), round(miner1[cat]))

        for cat in range(0, len(missilex1)):
            if missiler1[cat] == 1:
                pygame.draw.circle(screen, (255, 0, 0), (round(missilex1[cat]), round(missiley1[cat])), 8)
            if missiledel1[cat] == 2:
                if missiler1[cat] > 20:
                    pygame.draw.circle(screen, (255, 0, 0), (round(missilex1[cat]), round(missiley1[cat])),
                                       round(missiler1[cat]), 20)
                else:
                    pygame.draw.circle(screen, (255, 0, 0), (round(missilex1[cat]), round(missiley1[cat])),
                                       round(missiler1[cat]))

        for cat in range(0, len(ebulletdel)):
            pygame.draw.circle(screen, (0, 255, 0), (round(ebulletx[cat]), round(ebullety[cat])), 4)

        for cat in range(0, len(eshipdel)):
            pygame.draw.rect(screen, (255, 255, 255), (round(eshipx[cat]) - 25, round(eshipy[cat]) + 30, 50, 4))

            pygame.draw.rect(screen, (255, 0, 0), (
                round(eshipx[cat]) - 25, round(eshipy[cat]) + 30, round(eshiphit[cat] * 50 / eshiphitt[cat]), 4))
            if eshiptype[cat] == "norm":
                pygame.draw.circle(screen, (255, 0, 0), (round(eshipx[cat]), round(eshipy[cat])), 15)
            if eshiptype[cat] == "split":
                pygame.draw.circle(screen, (0, 0, 255), (round(eshipx[cat]), round(eshipy[cat])), 20)
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
                pygame.draw.circle(screen, (100, 100, 255), (round(eshipx[cat]), round(eshipy[cat])), 25)
            if eshiptype[cat] == "splitttttttt":
                pygame.draw.circle(screen, (200, 0, 0), (round(eshipx[cat]), round(eshipy[cat])), 30)

        #____________________________________________________________________________________________________________________________________________game over
        if shiphit <= 0 and 0 == 1:
            dietimer -= 1
            stopwatch -= 1
            pygame.draw.rect(screen, (255, 0, 255), (round(shipx) - 25, round(shipy) + 30, 50, 4))
            shiphit -= 1
            if dietimer == 298:
                score1 += 3000
                if mode == "one life":
                    score1 -= 2600
            if dietimer <= 0:
                shipx = 80
                shipy = 40
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
                shipx1 = 1000
                shipy1 = 500
                shipxx1 = 0
                shipyy1 = 3
                shiphit1 = 50
                bulletx1 = []
                bullety1 = []
                bulletxx1 = []
                bulletyy1 = []
                bulletdel1 = []
                bulletreload1 = 8
                bullshotdamage1 = 4
                shotgunacc1 = 60
                shotgunreload1 = 100
                shotgunbullets1 = 6
                laserx1 = []
                lasery1 = []
                laserxx1 = []
                laseryy1 = []
                laserdel1 = []
                laserreload1 = 60
                laserdamage1 = 3
                lasertimer1 = 0
                missilex1 = []
                missiley1 = []
                missilexx1 = []
                missileyy1 = []
                missiledel1 = []
                missilereload1 = 100
                missiledamage1 = 4
                missileradius1 = 150
                missiler1 = []
                missiletimer1 = 0
                missileshrapnel1 = 0
                minex1 = []
                miney1 = []
                minedel1 = []
                miner1 = []
                mineradius1 = 150
                minedamage1 = 3
                mineshrapnel1 = 0
                lightning1x1 = []
                lightning1y1 = []
                lightning2x1 = []
                lightning2y1 = []
                lightningtimer1 = 0
                lightreload1 = 200
                lightdamage1 = 1
                eshipx = []
                eshipy = []
                eshipxx = []
                eshipyy = []
                eshipdel = []
                eshiphit = []
                eshiphitt = []
                eshiptype = []
                eshipsum = []
                lightstruck = []
                stopwatch = 0
                minetimer = 0
                shoottimer = 0
                shotguntimer = 0
                shoot = False
                dropmine = False
                shoot1 = False
                dropmine1 = False
                aimturn = "?"
                aimturn1 = "?"
                aimturn2 = "?"
                score = 0
                score1 = 0
                alientimer = 0
                delay = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                slide = "main menu"
                coins = 1000
                coins1 = 1000
                upgradebullets = 1
                upgradeshotgun = 1
                upgradelasers = 1
                upgrademissiles = 1
                upgrademines = 1
                upgradelightning = 1
                upgradebullets1 = 1
                upgradeshotgun1 = 1
                upgradelasers1 = 1
                upgrademissiles1 = 1
                upgrademines1 = 1
                upgradelightning1 = 1
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
                dietimer = 300

        if shiphit1 <= 0 and shiphit <= 0:
            dietimer -= 1
            stopwatch -= 1
            pygame.draw.rect(screen, (255, 0, 255), (round(shipx1) - 25, round(shipy1) + 30, 50, 4))
            shiphit1 -= 1
            if dietimer == 298:
                score += 3000
                if mode == "one life":
                    score -= 2600
            if dietimer <= 0:
                shipx = 80
                shipy = 40
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
                shipx1 = 1000
                shipy1 = 500
                shipxx1 = 0
                shipyy1 = 3
                shiphit1 = 50
                bulletx1 = []
                bullety1 = []
                bulletxx1 = []
                bulletyy1 = []
                bulletdel1 = []
                bulletreload1 = 8
                bullshotdamage1 = 4
                shotgunacc1 = 60
                shotgunreload1 = 100
                shotgunbullets1 = 6
                laserx1 = []
                lasery1 = []
                laserxx1 = []
                laseryy1 = []
                laserdel1 = []
                laserreload1 = 60
                laserdamage1 = 3
                lasertimer1 = 0
                missilex1 = []
                missiley1 = []
                missilexx1 = []
                missileyy1 = []
                missiledel1 = []
                missilereload1 = 100
                missiledamage1 = 4
                missileradius1 = 150
                missiler1 = []
                missiletimer1 = 0
                missileshrapnel1 = 0
                minex1 = []
                miney1 = []
                minedel1 = []
                miner1 = []
                mineradius1 = 150
                minedamage1 = 3
                mineshrapnel1 = 0
                lightning1x1 = []
                lightning1y1 = []
                lightning2x1 = []
                lightning2y1 = []
                lightningtimer1 = 0
                lightreload1 = 200
                lightdamage1 = 1
                eshipx = []
                eshipy = []
                eshipxx = []
                eshipyy = []
                eshipdel = []
                eshiphit = []
                eshiphitt = []
                eshiptype = []
                eshipsum = []
                lightstruck = []
                stopwatch = 0
                minetimer = 0
                shoottimer = 0
                shotguntimer = 0
                shoot = False
                dropmine = False
                shoot1 = False
                dropmine1 = False
                aimturn = "?"
                aimturn1 = "?"
                aimturn2 = "?"
                score = 0
                score1 = 0
                alientimer = 0
                delay = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                slide = "main menu"
                coins = 1000
                coins1 = 1000
                upgradebullets = 1
                upgradeshotgun = 1
                upgradelasers = 1
                upgrademissiles = 1
                upgrademines = 1
                upgradelightning = 1
                upgradebullets1 = 1
                upgradeshotgun1 = 1
                upgradelasers1 = 1
                upgrademissiles1 = 1
                upgrademines1 = 1
                upgradelightning1 = 1
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
            buletyy = []
            bulletdel = []
            laserx1 = []
            lasery1 = []
            laserxx1 = []
            laseryy1 = []
            laserdel1 = []
            bulletx1 = []
            bullety1 = []
            bulletxx1 = []
            bulletyy1 = []
            bulletdel1 = []

    pygame.display.flip()
    clock.tick(100)