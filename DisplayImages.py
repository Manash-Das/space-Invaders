import load
import pygame

pygame.init()
font26 = pygame.font.Font('font.ttf', 26)
font18 = pygame.font.Font('font.ttf', 20)


##################   function to draw the all the images in their respective coordinates ############
def displayImage(level, screen, allBullet, playerCoordinate, allEnemy, score, Stones, noOfBullet ):
    screen.blit(load.background, (0, 0))
    screen.blit(load.spaceship, playerCoordinate)
    for bullets in allBullet:
        if bullets.state == "fire":
            screen.blit(load.bullet, (bullets.x, bullets.y))

    if Stones.state == "fall":
        screen.blit(load.STONE, (Stones.x, Stones.y))

    for enemies in allEnemy:
        if enemies.state == "Alive":
            screen.blit(load.enemy, (enemies.x, enemies.y))
    score = font26.render(f"SCORE :{score}", True, (255, 255, 255))
    BulletLeft = font18.render(f"Bullet :{noOfBullet}", True, (255, 255, 255))
    EnemyLeft = font18.render(f"Enemy :{len(allEnemy)}", True, (255, 255, 255))
    screen.blit(score, (10, 10))
    screen.blit(BulletLeft, (690, 10))
    screen.blit(EnemyLeft, (690, 35))

    if level == 2:
        screen.blit(load.wall, (100, 100))
        screen.blit(load.wall, (300, 100))
        screen.blit(load.wall, (500, 100))
        screen.blit(load.wall, (700, 100))
    elif level == 3:
        screen.blit(load.wall, (150, 150))
        screen.blit(load.wall, (350, 350))
        screen.blit(load.wall, (550, 150))

    elif level == 4:
        screen.blit(load.wall, (200, 100))
        screen.blit(load.wall, (400, 250))
        screen.blit(load.wall, (600, 400))
        # screen.blit(load.wall, (800, 600))

def displayBlast(screen, x, y):
    screen.blit(load.blast, (x, y))
