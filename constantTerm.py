# PLAYER_MOVEMENT = 1
# ENEMY_MOVEMENT = 0.6
# BULLET_MOVEMENT = 1.5
# BLAST_MOVEMENT = 0
class Const:
    def __init__(self):
        self.PLAYER_MOVEMENT = 0
        self.ENEMY_MOVEMENT = 0
        self.BULLET_MOVEMENT = 0
        self.NO_OF_ENEMY = 0
        self.NO_OF_BULLET = 0

    def constant(self, level):
        if level == 1:
            self.PLAYER_MOVEMENT = 0.8
            self.ENEMY_MOVEMENT = 0.4
            self.BULLET_MOVEMENT = 2
            self.NO_OF_ENEMY = 10
            self.NO_OF_BULLET = 50

        if level == 2:
            self.PLAYER_MOVEMENT = 1
            self.ENEMY_MOVEMENT = 0.6
            self.BULLET_MOVEMENT = 2
            self.NO_OF_ENEMY = 15
            self.NO_OF_BULLET = 50

        if level == 3:
            self.PLAYER_MOVEMENT = 1.3
            self.ENEMY_MOVEMENT = 0.8
            self.BULLET_MOVEMENT = 2
            self.NO_OF_ENEMY = 20
            self.NO_OF_BULLET = 50

        if level == 4:
            self.PLAYER_MOVEMENT = 0.8
            self.ENEMY_MOVEMENT = 1
            self.BULLET_MOVEMENT = 2
            self.NO_OF_ENEMY = 25
            self.NO_OF_BULLET = 50

