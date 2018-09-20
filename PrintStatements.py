import time

class PrintStatements:
    turned_on = None

    def __init__(self, turned_on=False):
        self.turned_on = turned_on

    def turn_start_info(self, turn_number):
        if self.turned_on:
            print("Turn number -", turn_number, "-")

    def roll_info(self, roll, player_position, tile_dict):
        if self.turned_on:
            print("You rolled a -", roll, "- You are now at position:", player_position, "Name:",
                  tile_dict[player_position])

    def ask_pre_turn_action(self, player_name):
        if self.turned_on:
            print("Current player is -", player_name, "- Perform any pre-turn actions?")

    def ask_roll(self, player_name):
        if self.turned_on:
            print("Current player is -", player_name, "- Roll?")

    def rolling(self):
        if self.turned_on:
            print("Rolling...")
            time.sleep(.5)

    def waited_out_jail(self, player_name):
        if self.turned_on:
            print(player_name, "has been in jail for 3 turns and is now rolling for move.")

    def turns_jailed_ask_escape(self, player_name, turns_jailed):
        if self.turned_on:
            print(player_name, "has been in jail for", turns_jailed, "turns.  Use escape card?")

    def use_get_out_of_jail_success(self, player_name):
        if self.turned_on:
            print(player_name, "has used a get out of jail free card and left jail.")

    def use_get_out_of_jail_failure(self, player_name):
        if self.turned_on:
            print(player_name, "has no get out of jail free cards and is still in jail")

    def roll_for_doubles_success(self, player_name):
        if self.turned_on:
            print(player_name, "has rolled doubles and escaped jail.")

    def roll_for_doubles_failure(self, player_name):
        if self.turned_on:
            print(player_name, "remains in jail and will not roll for move.")



