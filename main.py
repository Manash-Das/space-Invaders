import pygame
import load
import sys
import startingloop

pygame.init()

level = 0

########################## Create a window, naming title and setting an Icon ########################
pygame.display.set_caption("Space invaders")
pygame.display.set_icon(load.icon)
screen = pygame.display.set_mode((800, 600))

############################# music ##############################
pygame.mixer.music.load("Music/background.wav")
pygame.mixer.music.play(-1)

if not startingloop.HomePage(screen):
    sys.exit()

startingloop.game(screen)

level = startingloop.completingLevels(screen)
