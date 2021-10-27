from random import randrange
import load


def randomPositionEnemy():
    return randrange(0, 750), randrange(0, 70)


def player(x_coordinates, y_coordinates):
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
def enemy(x_coordinates, y_coordinates, ENEMY_MOVEMENT):
    if x_coordinates > 800:
        x_coordinates = 0
        y_coordinates += 50  # constantTerm.ENEMY_MOVEMENT
    else:
        x_coordinates += ENEMY_MOVEMENT
    if y_coordinates > 600:
        print("YOU LOSE")
        return randomPositionEnemy()
    return x_coordinates, y_coordinates


def bullet(bullets, BULLET_MOVEMENT):
    if bullets.y < 0:
        bullets.set(0, 0, "ready")
        return
    bullets.set(bullets.x, bullets.y - BULLET_MOVEMENT)


def collision(level, enemies, totalBullet):
    for bullets in totalBullet:
        if bullets.state == "fire":
            if (enemies.x - bullets.x) ** 2 + (enemies.y - bullets.y) ** 2 < 200:
                enemies.set()
                totalBullet.remove(bullets)
                return True
            if level == 2 and 100 <= bullets.y <= 164 and (90 <= bullets.x <= 154 or 290 <= bullets.x <= 354 or
                                                           490 <= bullets.x <= 554 or 690 <= bullets.x <= 764):
                load.strike.play()
                bullets.state = "ready"

                # pygame.draw.rect(screen, (0, 0, 255), (100, 100, 75, 54))
    return False
