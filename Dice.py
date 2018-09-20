import random
import Player


def roll_for_move():
    return random.randint(1, 6) + random.randint(1, 6)


def roll_for_jail():
    roll1 = random.randint(1, 6)
    roll2 = random.randint(1, 6)
    print(roll1, roll2)
    if roll1 == roll2:
        return True
    else:
        return False


def roll_for_start():
    return roll_for_move() + roll_for_move()


def draw_random_card(card_list):
    return random.randint(0, len(card_list)-1)
