import random

diceRoll = random.randint(1, 6)


class Player:

    last_roll = None
    position = None
    name = None
    turn = None
    bank = None
    in_jail = None
    jail_passes = None
    owned_properties = None

    def __init__(self, name):
        self.name = name
        self.last_roll = None
        self.position = 0
        self.bank = 1000
        self.in_jail = False
        self.jail_passes = 0
        self.owned_properties = []

    def get_properties_list(self):
        self.owned_properties = sorted(self.owned_properties, key=lambda x: x.color)
        return self.owned_properties

    def verify_set_owned(self, tile):
        if 0 < tile.position <= 5 or 35 < tile.position <= 39:
            total_count = 2
        else:
            total_count = 3

        owned_count = 0
        for item in self.owned_properties:
            if item.color == tile.color:
                owned_count += 1

        if total_count == owned_count:
            return owned_count
        else:
            return None

