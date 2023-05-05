
import random


class Appendage:
    color = (100, 100, 100)


class Eye(Appendage):
    color = (100, 100, 255)


class Mouth(Appendage):
    color = (100, 255, 100)


class Weapon(Appendage):
    color = (255, 100, 100)


class MoveChoices:
    WAIT = 0
    MOVE_FORWARD = 1
    MOVE_LEFT = 2
    MOVE_BACK = 3
    MOVE_RIGHT = 4
    ROTATE_LEFT = 5
    ROTATE_RIGHT = 6


class Creature:

    move = MoveChoices.WAIT

    def __init__(self, x, y, angle=0):
        self.x = x
        self.y = y
        self.angle = angle
        self.appendages = [Eye, Mouth, Weapon, Appendage]

    def choose_move(self):
        self.move = random.randint(0, 6)

    def apply_move(self):
        if self.move == MoveChoices.WAIT:
            pass
        elif self.move == MoveChoices.MOVE_FORWARD:
            self.x += 1
        elif self.move == MoveChoices.MOVE_LEFT:
            self.y += 1
        elif self.move == MoveChoices.MOVE_BACK:
            self.x -= 1
        elif self.move == MoveChoices.MOVE_RIGHT:
            self.y -= 1
        elif self.move == MoveChoices.ROTATE_LEFT:
            self.angle = (self.angle + 90) % 360
        elif self.move == MoveChoices.ROTATE_RIGHT:
            self.angle = (self.angle - 90) % 360
        else:
            raise Exception(f"illegal move applied: {self.move}")
