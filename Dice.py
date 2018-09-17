import random
import Player


def roll_for_move():
    return random.randint(1, 6) + random.randint(1, 6)


def roll_for_start():
    return roll_for_move() + roll_for_move()

