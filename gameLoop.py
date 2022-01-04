import load
import pygame
import DisplayImages
import sys
import checkcondition as check
from time import time
import constantTerm
from random import randrange
pygame.init()
const = constantTerm.Const()
pTime = 0
cTime = 0
FPS = 90
fpsClock = pygame.time.Clock()

def HomePage(screen):
    while True:
        screen.blit(load.startingBackground, (0, 0))
        pygame.draw.rect(screen, (170, 170, 170), [300, 250, 209, 55])
        pygame.draw.rect(screen, (170, 170, 170), [30, 550, 81, 30])
        screen.blit(load.startText, (300, 250))
        screen.blit(load.end, (30, 550))
        screen.blit(load.createdText, load.createdText.get_rect(center=(400, 400)))
        # pygame.draw.rect(screen, (255, 255, 255), [300, 350, 79, 25])
        # screen.blit(load.levelText, (300, 350))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePosition = pygame.mouse.get_pos()
                if 300 <= mousePosition[0] <= 509 and 250 <= mousePosition[1] <= 305:
                    return True
                elif 30 <= mousePosition[0] <= 111 and 550 <= mousePosition[1] <= 580:
                    return False
                # elif 300 <= mousePosition[0] <= 379 and 350 <= mousePosition[1] <= 375:
                #     Levels(screen)
        pygame.display.update()


def Levels(screen):
    print("I am in levels")
    while True:
        screen.blit(load.startingBackground, (0, 0))
        screen.blit(load.level1, (300, 300))
        screen.blit(load.level2, (300, 330))
        screen.blit(load.level3, (300, 360))
        screen.blit(load.level4, (300, 390))
        screen.blit(load.level5, (300, 420))
        screen.blit(load.level6, (300, 450))
        pygame.draw.rect(screen, (100, 100, 100), [50, 50, 30, 30])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePosition = pygame.mouse.get_pos()
                if 50 <= mousePosition[0] <= 80 and 50 <= mousePosition[1] <= 80:
                    return
        pygame.display.update()


def game(screen, level):

    const.constant(level)
    ######### Creating multiple bullet enemy, and wall ################
    allBullet = [load.Bullet() for i in range(const.NO_OF_BULLET)]
    allEnemy = [load.Enemy() for j in range(const.NO_OF_ENEMY)]
    Stones = load.Stone()
    BulletCounter = 0
    ################## Coordinates of image to display ##############################
    player_x, player_y = 370, 480
    player_bullet_x, player_bullet_y = 20, 16

    ################## movement of Images by declared pixel ########################
    xSpeed = 0
    ySpeed = 0
    score = 0
    while True:
        ################# Displaying image in window #####################
        DisplayImages.displayImage(level, screen, allBullet, (player_x, player_y), allEnemy, score, Stones,
                                   const.NO_OF_BULLET - BulletCounter)
        if score == const.NO_OF_ENEMY:
            return "completed"
        if BulletCounter == const.NO_OF_BULLET:
            return "bullet"
        ############## pygame.events.get() capture all the events perform across the window ##############
        for events in pygame.event.get():
            ###### Checking if quit button is pressed or not (X) in window bar ##########
            if events.type == pygame.QUIT:
                sys.exit()

            ###### Checking if any key is pressed ######
            if events.type == pygame.KEYDOWN:
                ######## skip level #########
                if events.key == pygame.K_n:
                    return "completed"
                ######### increase bullets #############
                if events.key == pygame.K_m:
                    BulletCounter -= 5
                ##### Checking if left arrow is clicked ######
                if events.key == pygame.K_LEFT:
                    ## if clicked changing coordinates
                    xSpeed = -const.PLAYER_MOVEMENT
                ##### Checking if right arrow is clicked ######
                elif events.key == pygame.K_RIGHT:
                    ## if clicked changing coordinates
                    xSpeed = const.PLAYER_MOVEMENT
                ##### Checking if UP arrow is clicked ######
                elif events.key == pygame.K_UP:
                    ## if clicked changing coordinates
                    ySpeed = -const.PLAYER_MOVEMENT
                ##### Checking if Down arrow is clicked ######
                elif events.key == pygame.K_DOWN:
                    ## if clicked changing coordinates
                    ySpeed = const.PLAYER_MOVEMENT
                ##### checking if space Bar is clicked ########
                elif events.key == pygame.K_SPACE:
                    load.bulletSound.play()
                    allBullet[BulletCounter].set(player_x + player_bullet_x, player_y - player_bullet_y)
                    BulletCounter += 1
            ###### Checking if any key is released ######
            if events.type == pygame.KEYUP:
                ##### Checking which key is released #####
                if events.key == pygame.K_LEFT or events.key == pygame.K_RIGHT or events.key == pygame.K_DOWN \
                        or events.key == pygame.K_UP:
                    ### if found no change in coordinates ###
                    ySpeed = 0
                    xSpeed = 0
        ##### player condition to check if object is moving outside the screen #########
        player_x, player_y = check.player(player_x, player_y, xSpeed, ySpeed, level)

        ####### if bullet is fired then setting position and taking care of bullet outside the frame ############
        for bullet in allBullet:
            if bullet.state == "fire":
                check.bullet(bullet, const.BULLET_MOVEMENT)

        ##################### Checking Enemy strike ####################
        for enemy in allEnemy:
            if enemy.state == "Alive":
                ########## Checking enemy position ###########
                enemy.x, enemy.y = check.enemy(enemy.x, enemy.y, const.ENEMY_MOVEMENT_X, const.ENEMY_MOVEMENT_Y)
                ######### collision occurs ##########
                if check.bulletCollision(level, enemy, allBullet):
                    explosionSound = pygame.mixer.Sound("Music/explosion.wav")
                    explosionSound.play()
                    score += 1
                if check.playerCollision(enemy, player_x, player_y):
                    explosionSound = pygame.mixer.Sound("Music/explosion.wav")
                    explosionSound.play()
                    return "blast"
            if enemy.state == "shoot":
                if time() - enemy.killedTime < 0.15:
                    DisplayImages.displayBlast(screen, enemy.x, enemy.y)
                else:
                    allEnemy.remove(enemy)

        #################### checking stones ##################
        if Stones.state == "fall":
            if Stones.y > 650:
                Stones.y = 0
                Stones.x = randrange(0,800)
                Stones.state = "ready"
            if check.stone(Stones.x, Stones.y, player_x, player_y):
                return "blast"
            Stones.y += const.STONES_MOVEMENT_Y
        else:
            random = randrange(0, 1000)
            if random % 17 == 0:
                Stones.state = "fall"
        pygame.display.update()
        fpsClock.tick(FPS)


def completingLevels(screen, reason="completed"):
    running = True
    displayText = load.levels.render("Press p to play and q to quit", True, (200, 255, 255))
    text_rect = displayText.get_rect(center=(400, 400))
    if reason == "completed":
        displayText1 = load.startGame.render("Great", True, (200, 200, 200))
        displayText2 = load.startGame.render("you win", True, (200, 200, 200))
    elif reason == "bullet":
        displayText1 = load.startGame.render("Bullet Finished", True, (200, 200, 200))
        displayText2 = load.startGame.render("You lose", True, (200, 200, 200))
    elif reason == "blast":
        displayText1 = load.startGame.render("You were killed", True, (200, 200, 200))
        displayText2 = load.startGame.render("You lose", True, (200, 200, 200))
    text_rect1 = displayText1.get_rect(center=(400, 150))
    text_rect2 = displayText2.get_rect(center=(400, 300))

    while running:
        screen.blit(load.background, (0, 0))
        screen.blit(displayText, text_rect)
        screen.blit(displayText1, text_rect1)
        screen.blit(displayText2, text_rect2)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    running = False
                if event.key == pygame.K_q:
                    sys.exit()

        pygame.display.update()
