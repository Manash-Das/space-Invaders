from random import randrange
import load


def randomPositionEnemy():
    return randrange(0, 750, 5), randrange(0, 70, 5)


def player(x_coordinates, y_coordinates, change_x, change_y, level):
    x_coordinates, y_coordinates = x_coordinates + change_x, y_coordinates + change_y

    if level == 2 and ((36 <= x_coordinates <= 164)
                       or (236 <= x_coordinates <= 364)
                       or (436 <= x_coordinates <= 564)
                       or (636 <= x_coordinates <= 764)) \
            and (32 <= y_coordinates <= 164):
        return x_coordinates - change_x, y_coordinates - change_y

    if level == 3 and (((90 <= x_coordinates <= 208 or 490 <= x_coordinates <= 608) and 90 <= y_coordinates <= 213)
                       or (290 <= x_coordinates <= 410 and 290 <= y_coordinates <= 413)):
        return x_coordinates - change_x, y_coordinates - change_y
    if x_coordinates >= 740:
        return 740, y_coordinates
    if x_coordinates < 0:
        return 0, y_coordinates
    if y_coordinates > 536:
        return x_coordinates, 536
    if y_coordinates < 0:
        return x_coordinates, 0
    else:
        return x_coordinates, y_coordinates


############### Tracking enemy movement and restricting to move #############
def enemy(x_coordinates, y_coordinates, move_x, move_y):
    if x_coordinates > 800:
        x_coordinates = 0
        y_coordinates += move_y
    else:
        x_coordinates += move_x
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
                bullets.set(0, 0)
                return True
            if level == 2 and 100 <= bullets.y <= 164 and (90 <= bullets.x <= 158 or 290 <= bullets.x <= 358 or
                                                           490 <= bullets.x <= 558 or 690 <= bullets.x <= 758):
                load.strike.play()
                bullets.state = "ready"

            if level == 3 and (((138 <= bullets.x <= 205 or 538 <= bullets.x <= 605) and 150 <= bullets.y <= 214)
                               or (338 <= bullets.x <= 405 and 340 <= bullets.y <= 414)):
                load.strike.play()
                bullets.state = "ready"

    return False
