import pygame
from random import randrange
from numpy import arange

########################## initialise the pygame###################
pygame.init()
############################## Title name #############################
pygame.display.set_caption("Space invaders")
############################## setting Icon ################
icon = pygame.image.load("shooterJetIcon.png")
pygame.display.set_icon(icon)
############################## loading player spaceship   #############################
playerSpaceship = pygame.image.load("space-ship.png")
############################### player spaceship coordinate ########################
player_x_coordinates, player_y_coordinates = 370, 480
############################### loading enemies ####################################
enemyImg = pygame.image.load("ufo.png")
############################## loading background #####################
backgroundImg = pygame.image.load("background image.jpg")
############################## loading Bullet ############
bulletImg = pygame.image.load("bullet.png")
bullet_x = 0
bullet_y = 0
############################## enemyImg coordinates ##########################


def randomPositionEnemy():
    return randrange(0, 800), randrange(0, 70)


enemy_x_coordinates, enemy_y_coordinates = randomPositionEnemy()

############################### Create a window ##########################################
screen = pygame.display.set_mode((800, 600))


##################   function to draw the player in the respective coordinates ############
def player():
    screen.blit(playerSpaceship, (player_x_coordinates, player_y_coordinates))


##################   function to draw the enemyImg in the respective coordinates ############
def enemy():
    screen.blit(enemyImg, (enemy_x_coordinates, enemy_y_coordinates))


def background():
    screen.blit(backgroundImg, (0, 0))


def bullet():
    screen.blit(bulletImg, (bullet_x_coordinates, bullet_y_coordinates))


############## For pressing key changing value of x coordinates and y coordinates is initialized ##############
xChange = 0
yChange = 0

###################### Movement of spaceship by 0.5 pixel is declared ####################
movingIndex = 0.5


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
        y_coordinates += movingIndex + 10
    else:
        x_coordinates += movingIndex + 0.7
    if y_coordinates > 600:
        print("YOU LOSE")
        return randomPositionEnemy()
    return x_coordinates, y_coordinates


# def checkBlast(player_x_range, player_y_range, enemy_x_range, enemy_y_range):
#     print(player_x_range, player_y_range, enemy_x_range, enemy_y_range)
#     if player_x_range == enemy_x_range:
#         print("boom")
#     if player_y_range == enemy_y_range:
#         print("boom")


######################## LOOP TO DISPLAY GAME SCREEN ################################
running = True
while running:
    ################# Filling color in the window in RGB format #####################
    screen.fill((0, 255, 255))
    background()
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
                xChange = -movingIndex
            ##### Checking if right arrow is clicked ######
            elif event.key == pygame.K_RIGHT:
                ## if clicked changing coordinates
                xChange = movingIndex
            ##### Checking if UP arrow is clicked ######
            elif event.key == pygame.K_UP:
                ## if clicked changing coordinates
                yChange = -movingIndex
            ##### Checking if Down arrow is clicked ######
            elif event.key == pygame.K_DOWN:
                ## if clicked changing coordinates
                yChange = movingIndex
        ###### Checking if any key is released ######
        if event.type == pygame.KEYUP:
            ##### Checking which key is released #####
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_DOWN or \
                    event.key == pygame.K_UP:
                ### if found no change in coordinates ###
                yChange = 0
                xChange = 0

    ##### player condition to check if object is moving outside the screen #########
    player_x_coordinates, player_y_coordinates = playerCondition(player_x_coordinates + xChange,
                                                                 player_y_coordinates + yChange)
    ########## Checking enemy position ###########
    enemy_x_coordinates, enemy_y_coordinates = enemyCondition(enemy_x_coordinates, enemy_y_coordinates)
    ####### updating the position of spaceship and enemy as per the change in coordinates #######
    # checkBlast(player_x_coordinates, player_y_coordinates, enemy_x_coordinates, enemy_y_coordinates)
    player()
    enemy()
    ####### This will update all the changes made in the screen
    pygame.display.update()
