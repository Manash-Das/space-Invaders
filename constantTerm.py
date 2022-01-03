# PLAYER_MOVEMENT = 1
# ENEMY_MOVEMENT = 0.6
# BULLET_MOVEMENT = 1.5
# BLAST_MOVEMENT = 0
class Const:
    def __init__(self):
        self.STONES_MOVEMENT_Y = 0
        self.BLAST_TIME = 0
        self.PLAYER_MOVEMENT = 0
        self.ENEMY_MOVEMENT_X = 0
        self.ENEMY_MOVEMENT_Y = 0
        self.BULLET_MOVEMENT = 0
        self.NO_OF_ENEMY = 0
        self.NO_OF_BULLET = 0
        self.NO_OF_wall = 0
        self.NO_OF_STONE = 0

    def constant(self, level):
        if level == 1:
            self.PLAYER_MOVEMENT = 2.5
            self.ENEMY_MOVEMENT_X = 2
            self.ENEMY_MOVEMENT_Y = 5
            self.BULLET_MOVEMENT = 3
            self.NO_OF_ENEMY = 10
            self.NO_OF_BULLET = 30

        elif level == 2:
            self.PLAYER_MOVEMENT = 2.5
            self.ENEMY_MOVEMENT_X = 2
            self.ENEMY_MOVEMENT_Y = 7
            self.BULLET_MOVEMENT = 3
            self.NO_OF_ENEMY = 20
            self.NO_OF_BULLET = 35

        elif level == 3:
            self.PLAYER_MOVEMENT = 2.5
            self.ENEMY_MOVEMENT_X = 3
            self.ENEMY_MOVEMENT_Y = 9
            self.BULLET_MOVEMENT = 3
            self.NO_OF_ENEMY = 30
            self.NO_OF_BULLET = 40

        elif level == 4:
            self.PLAYER_MOVEMENT = 2.5
            self.ENEMY_MOVEMENT_X = 3
            self.ENEMY_MOVEMENT_Y = 10
            self.BULLET_MOVEMENT = 3
            self.NO_OF_ENEMY = 35
            self.NO_OF_BULLET = 45
            self.NO_OF_STONE = 3
            self.STONES_MOVEMENT_Y = 2

        elif level == 5:
            self.PLAYER_MOVEMENT = 2.5
            self.ENEMY_MOVEMENT_X = 3
            self.ENEMY_MOVEMENT_Y = 10
            self.BULLET_MOVEMENT = 3
            self.NO_OF_ENEMY = 35
            self.NO_OF_BULLET = 45
            self.NO_OF_STONE = 5
