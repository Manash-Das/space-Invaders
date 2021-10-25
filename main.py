import pygame
from random import randrange
from time import time

########################## initialise the pygame###################
pygame.init()


class Bullet:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.state = "ready"

    def set(self, x, y, state="fire"):
        self.x = x
        self.y = y
        self.state = state


def randomPositionEnemy():
    return randrange(0, 750), randrange(0, 70)


class Enemy:
    def __init__(self):
        self.x, self.y = randomPositionEnemy()
        self.state = "Alive"
        self.killedTime = 0

    def set(self, state="shoot"):
        self.state = state
        self.killedTime = time()

    def display(self):
        print(self.x, self.y, self.state)


######### Creating multiple bullet and enemy ################
totalBullet = [Bullet() for i in range(100)]
totalEnemy = [Enemy() for j in range(10)]

############################## loading required Images   #############################
bulletImg = pygame.image.load("bullet.png")
icon = pygame.image.load("shooterJetIcon.png")
playerSpaceship = pygame.image.load("space-ship.png")
enemyImg = pygame.image.load("ufo.png")
backgroundImg = pygame.image.load("background image.jpg")
blastImg = pygame.image.load("blast.png")

################## Coordinates of image to display ##############################
player_x, player_y = 370, 480
player_bullet_x, player_bullet_y = 20, 16

################## movement of Images by declared pixel ########################
playerChange = 1
enemyChange = 0.3
bulletChange = 1
blastCounter = 0
BulletCounter = 0
score = 0
font = pygame.font.Font('freesansbold.ttf', 26)
text_x, text_y = 10, 10


##################   function to draw the all the images in their respective coordinates ############
def displayImage(playerCoordinate):
    screen.blit(backgroundImg, (0, 0))
    screen.blit(playerSpaceship, playerCoordinate)
    for bullets in totalBullet:
        if bullets.state == "fire":
            screen.blit(bulletImg, (bullets.x, bullets.y))
    for enemies in totalEnemy:
        if enemies.state == "Alive":
            screen.blit(enemyImg, (enemies.x, enemies.y))
    scoreValue = font.render(f"SCORE :{score}", True, (255, 255, 255))
    screen.blit(scoreValue, (10, 10))


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
        y_coordinates += enemyChange + 3
    else:
        x_coordinates += enemyChange
    if y_coordinates > 600:
        print("YOU LOSE")
        return randomPositionEnemy()
    return x_coordinates, y_coordinates


def bulletCondition(bullets):
    if bullets.y < 0:
        bullets.set(0, 0, "ready")
        return
    bullets.set(bullets.x, bullets.y - 1)


def collision(enemies):
    for bullets in totalBullet:
        if bullets.state == "fire" and (enemies.x - bullets.x) ** 2 + (enemies.y - bullets.y) ** 2 < 200:
            enemies.set()
            return True
    return False


def displayBlast(x, y):
    screen.blit(blastImg, (x, y))


########################## Create a window, naming title and setting an Icon ########################
pygame.display.set_caption("Space invaders")
pygame.display.set_icon(icon)
screen = pygame.display.set_mode((800, 600))

############################# music ##############################
pygame.mixer.music.load("background.wav")
pygame.mixer.music.play(-1)

######################## LOOP TO DISPLAY GAME SCREEN ################################
xChange = 0
yChange = 0
running = True
while running:
    ################# Displaying image in window #####################
    displayImage((player_x, player_y))
    if score == 10:
        running = False
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
            ##### checking if space Bar is clicked ########
            elif event.key == pygame.K_SPACE:
                bulletSound = pygame.mixer.Sound("laser.wav")
                bulletSound.play()

                totalBullet[BulletCounter].set(player_x + player_bullet_x, player_y - player_bullet_y)
                BulletCounter += 1
        ###### Checking if any key is released ######
        if event.type == pygame.KEYUP:
            ##### Checking which key is released #####
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_DOWN or \
                    event.key == pygame.K_UP:
                ### if found no change in coordinates ###
                yChange = 0
                xChange = 0

    ##### player condition to check if object is moving outside the screen #########
    player_x, player_y = playerCondition(player_x + xChange, player_y + yChange)

    ####### if bullet is fired then setting position and taking care of bullet outside the frame ############
    for bullet in totalBullet:
        if bullet.state == "fire":
            bulletCondition(bullet)

    for enemy in totalEnemy:
        if enemy.state == "Alive":
            ########## Checking enemy position ###########
            enemy.x, enemy.y = enemyCondition(enemy.x, enemy.y)

            ######### collision occurs ##########
            if collision(enemy):
                explosionSound = pygame.mixer.Sound("explosion.wav")
                explosionSound.play()
                score += 1
                print(score)
        if enemy.state == "shoot":
            if time() - enemy.killedTime < 0.1:
                displayBlast(enemy.x, enemy.y)
            else:
                enemy.state = "Killed"

    pygame.display.update()

gameOverFont = pygame.font.Font("freesansbold.ttf", 64)
overText = gameOverFont.render("You Win", True, (255, 255, 255))

running = True
while running:
    screen.blit(backgroundImg, (0, 0))
    screen.blit(overText, (200, 200))
    for event in pygame.event.get():
        if event.type == pygame.K_SPACE or event.type == pygame.QUIT:
            running = False
    pygame.display.update()
