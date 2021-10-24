import pygame
from random import randrange
from numpy import arange

############################## loading required Images   #############################
icon = pygame.image.load("shooterJetIcon.png")
playerSpaceship = pygame.image.load("space-ship.png")
enemyImg = pygame.image.load("ufo.png")
backgroundImg = pygame.image.load("background image.jpg")
bulletImg = pygame.image.load("bullet.png")


def randomPositionEnemy():
    return randrange(0, 800), randrange(0, 70)


################## Coordinates of image to display ###############################
player_x, player_y = 370, 480
enemy_x, enemy_y = randomPositionEnemy()
bullet_x, bullet_y, bulletState = 370, 464, "ready"
player_bullet_x, player_bullet_y = 20, 16
################## movement of Images by declared pixel ########################
playerChange = 0.5
enemyChange = 0.3
bulletChange = 0.8


##################   function to draw the all the images in their respective coordinates ############
def displayImage(playerCoordinate, enemyCoordinates, bulletCoordinates):
    screen.blit(backgroundImg, (0, 0))
    screen.blit(playerSpaceship, playerCoordinate)
    screen.blit(enemyImg, enemyCoordinates)
    print(bulletState)
    if bulletState == "fire":
        screen.blit(bulletImg, bulletCoordinates)


##################### Tracking player movement and restricting to move #############
def playerCondition(x_coordinates, y_coordinates):
    if x_coordinates >= 736:
        x_coordinates = 736
    elif x_coordinates < 0:
        x_coordinates = 0
    if y_coordinates > 536:
        y_coordinates = 536
    elif y_coordinates < 0:
        y_coordinates = 0
    return x_coordinates, y_coordinates


##################### Tracking enemy movement and restricting to move #############
def enemyCondition(x_coordinates, y_coordinates):
    if x_coordinates > 800:
        x_coordinates = 0
        y_coordinates += enemyChange
    else:
        x_coordinates += enemyChange
    if y_coordinates > 600:
        print("YOU LOSE")
        return randomPositionEnemy()
    return x_coordinates, y_coordinates


def movingBullet(y):
    if y < 0:
        global bulletState
        bulletState = "ready"
        return 0
    return y-1


########################## initialise the pygame###################
pygame.init()
########################## Create a window, naming title and setting an Icon ########################
pygame.display.set_caption("Space invaders")
pygame.display.set_icon(icon)
screen = pygame.display.set_mode((800, 600))


######################## LOOP TO DISPLAY GAME SCREEN ################################
xChange = 0
yChange = 0
running = True
while running:
    ################# Displaying image in window #####################
    displayImage((player_x, player_y),
                 (enemy_x, enemy_y),
                 (bullet_x, bullet_y))
    ############## pygame.event.get() capture all the event perform across the window ##############
    for event in pygame.event.get():
        ###### Checking if quit button is pressed or not (X) in window bar ##########
        if event.type == pygame.QUIT:
            running = False
        ###### Checking if any key is pressed ######
        if event.type == pygame.KEYDOWN:
            ##### Checking if left arrow is clicked ######
            if event.key == pygame.K_LEFT:
                ## if clicked changing coordinates
                xChange = -playerChange
            ##### Checking if right arrow is clicked ######
            elif event.key == pygame.K_RIGHT:
                ## if clicked changing coordinates
                xChange = playerChange
            ##### Checking if UP arrow is clicked ######
            elif event.key == pygame.K_UP:
                ## if clicked changing coordinates
                yChange = -playerChange
            ##### Checking if Down arrow is clicked ######
            elif event.key == pygame.K_DOWN:
                ## if clicked changing coordinates
                yChange = playerChange
            elif event.key == pygame.K_SPACE:
                bulletState = "fire"
                bullet_x, bullet_y = player_bullet_x + player_x, player_y - player_bullet_y
        ###### Checking if any key is released ######
        if event.type == pygame.KEYUP:
            ##### Checking which key is released #####
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_DOWN or \
                    event.key == pygame.K_UP:
                ### if found no change in coordinates ###
                yChange = 0
                xChange = 0

    ##### player condition to check if object is moving outside the screen #########
    player_x, player_y = playerCondition(player_x + xChange,
                                         player_y + yChange)
    ########## Checking enemy position ###########
    enemy_x, enemy_y = enemyCondition(enemy_x, enemy_y)
    ####### This will update all the changes made in the screen
    if bulletState == "fire":
        bullet_y = movingBullet(bullet_y)
    pygame.display.update()
