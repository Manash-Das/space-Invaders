from time import time
from random import randrange
import pygame
############################## loading required Images   #############################
pygame.init()
startingBackground = pygame.image.load("Images/starting background.jpg")
bullet = pygame.image.load("Images/bullet.png")
icon = pygame.image.load("Images/shooterJetIcon.png")
spaceship = pygame.image.load("Images/space-ship.png")
enemy = pygame.image.load("Images/ufo.png")
background = pygame.image.load("Images/background image.jpg")
blast = pygame.image.load("Images/blast.png")
sound = pygame.image.load("Images/sound.png")
mute = pygame.image.load("Images/mute.png")
wall = pygame.image.load("Images/wall.png")
hor_line = pygame.image.load("Images/horizontal line.png")


############################ loading text ####################################
startGame = pygame.font.Font("font.ttf", 64)
startText = startGame.render("START", True, (255, 255, 255))
exitGame = pygame.font.Font("font.ttf", 32)
end = exitGame.render("EXIT", True, (255, 255, 255))
levelCompleted = startGame.render("level completed", True, (255, 255, 255))
levels = pygame.font.Font("font.ttf", 24)
levelText = levels.render("Levels", True, (0, 255, 255))

######### Different Levels ########
level1 = levels.render("Levels 1", True, (255, 255, 255))
level2 = levels.render("Levels 2", True, (255, 255, 255))
level3 = levels.render("Levels 3", True, (255, 255, 255))
level4 = levels.render("Levels 4", True, (255, 255, 255))
level5 = levels.render("Levels 5", True, (255, 255, 255))
level6 = levels.render("Levels 6", True, (255, 255, 255))

############## Loading musics ##################
strike = pygame.mixer.Sound("Music/striking bullet and wall.mp3")
bulletSound = pygame.mixer.Sound("Music/laser.wav")

######################### Bullets Class ###########################
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


########################## Enemy Class #######################

class Enemy:
    def __init__(self):
        self.x, self.y = randomPositionEnemy()
        self.state = "Alive"
        self.killedTime = 0

    def set(self, state="shoot"):
        self.state = state
        self.killedTime = time()

class Wall:
    def __init__(self):
        self.x = 0
        self.y = 0

    def set(self, x, y):
        self.x = x
        self.y = y
