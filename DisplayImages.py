import load
import pygame

pygame.init()
font = pygame.font.Font('font.ttf', 26)


##################   function to draw the all the images in their respective coordinates ############
def displayImage(level, screen, allBullet, playerCoordinate, allEnemy, score):
    screen.blit(load.background, (0, 0))
    screen.blit(load.spaceship, playerCoordinate)
    for bullets in allBullet:
        if bullets.state == "fire":
            screen.blit(load.bullet, (bullets.x, bullets.y))
    for enemies in allEnemy:
        if enemies.state == "Alive":
            screen.blit(load.enemy, (enemies.x, enemies.y))
    scoreValue = font.render(f"SCORE :{score}", True, (255, 255, 255))
    screen.blit(scoreValue, (10, 10))
    if level == 2:
        screen.blit(load.wall, (100, 100))
        screen.blit(load.wall, (300, 100))
        screen.blit(load.wall, (500, 100))
        screen.blit(load.wall, (700, 100))
def displayBlast(screen, x, y):
    screen.blit(load.blast, (x, y))
