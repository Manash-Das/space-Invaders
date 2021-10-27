import pygame
import load
import sys
import gameLoop
pygame.init()

level = 1
########################## Create a window, naming title and setting an Icon ########################
pygame.display.set_caption("Space invaders")
pygame.display.set_icon(load.icon)
screen = pygame.display.set_mode((800, 600))

############################# music ##############################
pygame.mixer.music.load("Music/background.wav")
pygame.mixer.music.play(-1)

if not gameLoop.HomePage(screen):
    sys.exit()


while level < 3:
    gameLoop.game(screen, level)
    gameLoop.completingLevels(screen)
    level = level + 1

