# PLAYER_MOVEMENT = 1
# ENEMY_MOVEMENT = 0.6
# BULLET_MOVEMENT = 1.5
# BLAST_MOVEMENT = 0
class Const:
    def __init__(self):
        self.PLAYER_MOVEMENT = 0
        self.ENEMY_MOVEMENT_X = 0
        self.ENEMY_MOVEMENT_Y = 0
        self.BULLET_MOVEMENT = 0
        self.NO_OF_ENEMY = 0
        self.NO_OF_BULLET = 0
        self.NO_OF_wall = 0

    def constant(self, level):
        if level == 1:
            self.PLAYER_MOVEMENT = 2
            self.ENEMY_MOVEMENT_X = 3
            self.ENEMY_MOVEMENT_Y = 3
            self.BULLET_MOVEMENT = 4
            self.NO_OF_ENEMY = 10
            self.NO_OF_BULLET = 30
            self.NO_OF_wall = 0

        if level == 2:
            self.PLAYER_MOVEMENT = 3
            self.ENEMY_MOVEMENT_X = 2
            self.ENEMY_MOVEMENT_Y = 4
            self.BULLET_MOVEMENT = 4
            self.NO_OF_ENEMY = 20
            self.NO_OF_BULLET = 35
            self.NO_OF_wall = 3

        if level == 3:
            self.PLAYER_MOVEMENT = 3
            self.ENEMY_MOVEMENT_X = 3
            self.ENEMY_MOVEMENT_Y = 2
            self.BULLET_MOVEMENT = 4
            self.NO_OF_ENEMY = 30
            self.NO_OF_BULLET = 40
            self.NO_OF_wall = 4

        if level == 4:
            self.PLAYER_MOVEMENT = 0.8
            self.ENEMY_MOVEMENT_X = 0.4
            self.ENEMY_MOVEMENT_Y = 1
            self.BULLET_MOVEMENT = 4
            self.NO_OF_ENEMY = 35
            self.NO_OF_BULLET = 45

