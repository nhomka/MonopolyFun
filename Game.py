from Dice import *
import Board
from TileActions import perform_action
from Tile import Tile
from PreTurnActions import choose_preturn_action
import Cards
from PrintStatements import PrintStatements as PS


class Game:

    player_turn = None
    player_list = None
    edition = None
    tile_rents = None
    cards = None

    def __init__(self, edition=0):
        self.player_turn = 0
        self.player_list = []
        self.board = Board.Board(edition)
        self.tile_rents = {}
        self.PS = None

    def take_turn(self):
        self.PS.turn_start_info(self.player_turn)
        for player in self.player_list:
            if player.turn == self.player_turn % len(self.player_list):
                self.pre_turn_actions(player)

                if input().capitalize() == "Y":
                    self.PS.rolling()
                    if player.in_jail:
                        if player.turns_jailed == 3:
                            self.PS.waited_out_jail(player.name)
                            player.leave_jail()
                        else:
                            self.PS.turns_jailed_ask_escape(player.name, player.turns_jailed)
                            if input().capitalize() == 'Y':
                                if player.use_jail_pass():
                                    self.PS.use_get_out_of_jail_success(player.name)
                                else:
                                    player.turns_jailed += 1
                                    self.PS.use_get_out_of_jail_failure(player.name)
                            else:
                                if roll_for_jail():
                                    player.leave_jail()
                                    self.PS.roll_for_doubles_success(player.name)
                                else:
                                    player.turns_jailed += 1
                                    self.PS.roll_for_doubles_failure(player.name)
                    if not player.in_jail:
                        roll = roll_for_move()
                        player.last_roll = roll
                        player.position = (player.position + roll) % 40
                        self.PS.roll_info(roll, player.position, self.board.tile_dict)
                        perform_action(player, self.tile_rents[str(player.position)], game)
                break
        self.player_turn += 1

    def pre_turn_actions(self, player):
        action_bool = True
        while action_bool:
            self.PS.ask_pre_turn_action(player.name)
            if input().capitalize() == "Y":
                # Print list of actions
                choose_preturn_action(player, game.player_list)
            else:
                action_bool = False
        self.PS.ask_roll(player.name)

    def establish_turn_order(self):
        turn_list = []
        for player in self.player_list:
            turn_list.append((player, roll_for_start()))

        turn_list.sort(key=lambda x: x[1])
        count = 0
        for l in turn_list:
            l[0].turn = count
            count += 1

    def initialize_board(self):
        self.board.create()
        self.tile_rents = self.board.tile_rents
        self.cards = Cards.Cards()
        self.cards.initialize_card_set()
        self.PS = PS(True)


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

while game.player_turn < 30:
    game.take_turn()
