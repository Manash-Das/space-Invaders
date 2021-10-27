from random import randrange
enemyChange = 1
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
def enemy(x_coordinates, y_coordinates):
    if x_coordinates > 800:
        x_coordinates = 0
        y_coordinates += enemyChange + 3
    else:
        x_coordinates += enemyChange
    if y_coordinates > 600:
        print("YOU LOSE")
        return randomPositionEnemy()
    return x_coordinates, y_coordinates


def bullet(bullets):
    if bullets.y < 0:
        bullets.set(0, 0, "ready")
        return
    bullets.set(bullets.x, bullets.y - 1)


def collision(enemies, totalBullet):
    for bullets in totalBullet:
        if bullets.state == "fire" and (enemies.x - bullets.x) ** 2 + (enemies.y - bullets.y) ** 2 < 200:
            enemies.set()
            totalBullet.remove(bullets)
            return True
    return False
