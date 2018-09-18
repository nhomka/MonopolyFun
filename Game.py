from Dice import *
import time
import Board
from TileActions import perform_action
from Tile import Tile
from PreTurnActions import choose_preturn_action


class Game:

    player_turn = None
    player_list = None
    edition = None
    tile_rents = None

    def __init__(self, edition=0):
        self.player_turn = 0
        self.player_list = []
        self.board = Board.Board(edition)
        self.tile_rents = {}

    def take_turn(self):
        print("Turn number -", self.player_turn, "-")
        for player in self.player_list:
            if player.turn == self.player_turn % len(self.player_list):
                action_bool = True
                while action_bool:
                    print("Current player is -", player.name, "- Perform any pre-turn actions?")
                    get_input = input().capitalize()
                    if get_input == "Y":
                        # Print list of actions
                        choose_preturn_action(player)
                    else:
                        action_bool = False
                print("Current player is -", player.name, "- Roll?")

                get_input = input().capitalize()
                if get_input == "Y":
                    print("Rolling...")
                    time.sleep(.5)
                    roll = roll_for_move()
                    player.last_roll = roll
                    player.position = (player.position + roll) % 40

                    print("You rolled a -", roll, "- You are now at position:", player.position, "Name:",
                          self.board.tile_dict[player.position])
                    perform_action(player, self.tile_rents[str(player.position)])
                break
        self.player_turn += 1

    def establish_turn_order(self):
        turn_list = []
        for player in self.player_list:
            turn_list.append((player, roll_for_start()))

        turn_list.sort(key=lambda x: x[1])
        count = 0
        for item in turn_list:
            item[0].turn = count
            count += 1

    def initialize_board(self):
        self.board.create()
        self.tile_rents = self.board.tile_rents


player1 = Player.Player("player1")
player2 = Player.Player("player2")
player3 = Player.Player("player3")

game = Game()
game.player_list.append(player1)
game.player_list.append(player2)
game.player_list.append(player3)
game.initialize_board()
for p in game.player_list:
    print(p.name)

game.establish_turn_order()
for item in game.tile_rents:
    tile = game.tile_rents[item]
    print(item, tile.color)
    if tile.color == "orange":
        tile.owner = player1
        player1.owned_properties.append(tile)
        print(item, tile.color, tile.owner.name, player1.owned_properties)
for item in game.tile_rents:
    tile = game.tile_rents[item]
    if tile.color == "red":
        tile.owner = player2
        player2.owned_properties.append(tile)
for item in game.tile_rents:
    tile = game.tile_rents[item]
    if tile.color == "yellow":
        tile.owner = player3
        player3.owned_properties.append(tile)

while game.player_turn < 20:
    game.take_turn()
