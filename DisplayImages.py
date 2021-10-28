import load
import pygame

pygame.init()
font26 = pygame.font.Font('font.ttf', 26)
font18 = pygame.font.Font('font.ttf', 20)


##################   function to draw the all the images in their respective coordinates ############
def displayImage(level, screen, allBullet, playerCoordinate, allEnemy, score, noOfBullet, noOfEnemy):
    screen.blit(load.background, (0, 0))
    screen.blit(load.spaceship, playerCoordinate)
    for bullets in allBullet:
        if bullets.state == "fire":
            screen.blit(load.bullet, (bullets.x, bullets.y))
    for enemies in allEnemy:
        if enemies.state == "Alive":
            screen.blit(load.enemy, (enemies.x, enemies.y))
    score = font26.render(f"SCORE :{score}", True, (255, 255, 255))
    BulletLeft = font18.render(f"Bullet :{noOfBullet}", True, (255, 255, 255))
    EnemyLeft = font18.render(f"Enemy :{noOfEnemy}", True, (255, 255, 255))
    screen.blit(score, (10, 10))
    screen.blit(BulletLeft, (690, 10))
    screen.blit(EnemyLeft, (690, 35))

    if level == 2:
        screen.blit(load.wall, (100, 100))
        screen.blit(load.wall, (300, 100))
        screen.blit(load.wall, (500, 100))
        screen.blit(load.wall, (700, 100))
    elif level == 3:
        screen.blit(load.wall, (100, 100))
        screen.blit(load.wall, (300, 500))
        pygame.draw.line(screen, (25, 0, 255), (200, 300), (300, 400), 10)


def displayBlast(screen, x, y):
    screen.blit(load.blast, (x, y))
