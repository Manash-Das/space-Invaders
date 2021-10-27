import load
import pygame
import DisplayImages
import sys
import constantTerm
import checkcondition as check
from time import time
def HomePage(screen):
    while True:
        screen.blit(load.startingBackground, (0, 0))
        pygame.draw.rect(screen, (170, 170, 170), [300, 250, 209, 55])
        pygame.draw.rect(screen, (170, 170, 170), [30, 550, 81, 30])
        screen.blit(load.startText, (300, 250))
        screen.blit(load.end, (30, 550))
        pygame.draw.rect(screen, (255, 255, 255), [300, 350, 79, 25])
        screen.blit(load.levelText, (300, 350))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePosition = pygame.mouse.get_pos()
                if 300 <= mousePosition[0] <= 509 and 250 <= mousePosition[1] <= 305:
                    return True
                elif 30 <= mousePosition[0] <= 111 and 550 <= mousePosition[1] <= 580:
                    return False
                elif 300 <= mousePosition[0] <= 379 and 350 <= mousePosition[1] <= 375:
                    Levels(screen)
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

def game(screen):
    ######### Creating multiple bullet and enemy ################
    allBullet = [load.Bullet() for i in range(100)]
    allEnemy = [load.Enemy() for j in range(10)]
    BulletCounter = 0
    ################## Coordinates of image to display ##############################
    player_x, player_y = 370, 480
    player_bullet_x, player_bullet_y = 20, 16

    ################## movement of Images by declared pixel ########################
    xChange = 0
    yChange = 0
    run = True
    score = 0
    while run:
        ################# Displaying image in window #####################
        DisplayImages.displayImage(screen, allBullet, (player_x, player_y), allEnemy, score)
        if score == 10:
            break
        ############## pygame.events.get() capture all the events perform across the window ##############
        for events in pygame.event.get():
            ###### Checking if quit button is pressed or not (X) in window bar ##########
            if events.type == pygame.QUIT:
                sys.exit()
            ###### Checking if any key is pressed ######
            if events.type == pygame.KEYDOWN:
                ##### Checking if left arrow is clicked ######
                if events.key == pygame.K_LEFT:
                    ## if clicked changing coordinates
                    xChange = -constantTerm.PLAYERMOVEMENT
                ##### Checking if right arrow is clicked ######
                elif events.key == pygame.K_RIGHT:
                    ## if clicked changing coordinates
                    xChange = constantTerm.PLAYERMOVEMENT
                ##### Checking if UP arrow is clicked ######
                elif events.key == pygame.K_UP:
                    ## if clicked changing coordinates
                    yChange = -constantTerm.PLAYERMOVEMENT
                ##### Checking if Down arrow is clicked ######
                elif events.key == pygame.K_DOWN:
                    ## if clicked changing coordinates
                    yChange = constantTerm.PLAYERMOVEMENT
                ##### checking if space Bar is clicked ########
                elif events.key == pygame.K_SPACE:
                    bulletSound = pygame.mixer.Sound("Music/laser.wav")
                    bulletSound.play()
                    allBullet[BulletCounter].set(player_x + player_bullet_x, player_y - player_bullet_y)
                    BulletCounter += 1
            ###### Checking if any key is released ######
            if events.type == pygame.KEYUP:
                ##### Checking which key is released #####
                if events.key == pygame.K_LEFT or events.key == pygame.K_RIGHT or events.key == pygame.K_DOWN or \
                        events.key == pygame.K_UP:
                    ### if found no change in coordinates ###
                    yChange = 0
                    xChange = 0

        ##### player condition to check if object is moving outside the screen #########
        player_x, player_y = check.player(player_x + xChange, player_y + yChange)

        ####### if bullet is fired then setting position and taking care of bullet outside the frame ############
        for bullet in allBullet:
            if bullet.state == "fire":
                check.bullet(bullet)

        for enemy in allEnemy:
            if enemy.state == "Alive":
                ########## Checking enemy position ###########
                enemy.x, enemy.y = check.enemy(enemy.x, enemy.y)

                ######### collision occurs ##########
                if check.collision(enemy, allBullet):
                    explosionSound = pygame.mixer.Sound("Music/explosion.wav")
                    explosionSound.play()
                    score += 1
            if enemy.state == "shoot":
                if time() - enemy.killedTime < 0.1:
                    DisplayImages.displayBlast(screen, enemy.x, enemy.y)
                else:
                    allEnemy.remove(enemy)

        pygame.display.update()

def completingLevels(screen):
    running = True
    while running:
        screen.blit(load.background, (0, 0))
        screen.blit(load.overText, (200, 200))
        for event in pygame.event.get():
            if event.type == pygame.K_SPACE or event.type == pygame.QUIT:
                running = False
        pygame.display.update()
