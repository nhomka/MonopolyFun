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
    in_game =  None

    def __init__(self, name):
        self.name = name
        self.last_roll = None
        self.position = 0
        self.bank = 1000
        self.in_jail = False
        self.turns_jailed = 0
        self.jail_passes = 0
        self.owned_properties = []
        self.in_game = True

    def sort_properties(self):
        self.owned_properties = sorted(self.owned_properties, key=lambda x: x.color)

    def get_properties_list(self):
        self.sort_properties()
        return self.owned_properties

    def use_jail_pass(self):
        if self.jail_passes >= 1:
            self.jail_passes -= 1
            self.in_jail = False
            self.turns_jailed = 0
            return True
        else:
            return False

    def leave_jail(self):
        self.in_jail = False
        self.turns_jailed = 0

    def get_mortgaged_properties_list(self):
        self.sort_properties()
        mortgaged_properties = [i for i in self.owned_properties if i.is_mortgaged]
        return mortgaged_properties

    def get_unmortgaged_properties_list(self):
        self.sort_properties()
        unmortgaged_properties = [i for i in self.owned_properties if not i.is_mortgaged]
        return unmortgaged_properties

    def get_empty_unmortgaged_properties_list(self):
        return [i for i in self.get_unmortgaged_properties_list() if i.houses == 0]

    def get_built_on_properties_list(self):
        color_list = []
        for i in self.get_properties_list():
            if i.houses >= 1 and i.color not in color_list:
                color_list.append((i.color, i.houses))
        return color_list

    def verify_set_owned(self, tile):
        if 0 < tile.position <= 5 or 35 < tile.position <= 39:
            total_count = 2
        else:
            total_count = 3

        owned_count = 0
        for item in self.owned_properties:
            if item.color == tile.color:
                if not item.is_mortgaged:
                    owned_count += 1

        if total_count == owned_count:
            return owned_count
        else:
            return None

    def get_total_assets(self):
        bank = self.bank
        houses = sum([(p.house_cost * p.houses)/2 for p in self.get_properties_list()])
        mortgages = sum([p.mortgage_price for p in self.get_unmortgaged_properties_list()])
        total_assets = bank + houses + mortgages
        return total_assets

    def liquefy_assets(self):
        print("Mortgage ('M') or Sell Houses ('H')?")
        get_input = input().capitalize()
        if get_input == 'M':
            print("The following properties can be mortgaged, enter comma separated list to mortgage")
            empty_unmortgaged_properties_list = self.get_empty_unmortgaged_properties_list()
            print(empty_unmortgaged_properties_list)
            list_input = input().split(',')
            for i in list_input:
                p = empty_unmortgaged_properties_list[i]
                self.bank += p.mortgage_price
                p.is_mortgaged = True
        elif get_input == 'H':
            print("The following property sets have houses that can be sold, enter color, # houses separated by comma")
            housed_properties_list = self.get_built_on_properties_list()
            print(housed_properties_list)
            list_input = input().split(',')
            color = list_input[0]
            num_houses = list_input[1]
            for i in self.get_properties_list():
                if i.color == color:
                    i.houses -= num_houses
                    sale_amount = (num_houses * i.house_cost)/2
                    self.bank += sale_amount
                    print(num_houses, "have been sold from", i.name, "for", sale_amount)

    def increase_bank(self, owed_money):
        if self.get_total_assets() < owed_money:
            self.in_game = False
            print(self.name, "is now out of the game")
        else:
            while self.bank < owed_money:
                self.liquefy_assets()

