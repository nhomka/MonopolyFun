import Auctions
import Board
import Cards
from Dice import *
from PreTurnActions import choose_preturn_action, pre_turn_jail_action
from PrintStatements import PrintStatements as PS
from TileActions import perform_action, go_to_jail_action



class Game:

    player_turn = None
    player_list = None
    edition = None
    tile_rents = None
    cards = None
    actual_turn = None

    def __init__(self, edition=0):
        self.player_turn = 0
        self.player_list = []
        self.board = Board.Board(edition)
        self.tile_rents = {}
        self.PS = None
        self.actual_turn = 0

    def take_turn(self):
        self.PS.turn_start_info(self.player_turn)
        for player in self.player_list:
            if not player.in_game:
                if len(player.get_properties_list() > 0):
                    bidder_list = self.player_list
                    bidder_list.remove(player)
                    for space in player.owned_properties:
                        Auctions.auction_property_from_bank(bidder_list, space, self.actual_turn)
            if player.turn == self.player_turn % len(self.player_list) and player.in_game:
                self.pre_turn_actions(player)

                if input().capitalize() == "Y":
                    self.PS.rolling()
                    jail_roll = None
                    if player.in_jail:
                        jail_roll = pre_turn_jail_action(player, self.PS)
                    if not player.in_jail:
                        doubles = 0
                        while 0 <= doubles < 3:
                            if jail_roll:
                                doubles = -1
                                roll_list = jail_roll
                            else:
                                roll_list = roll_for_move()
                                if roll_list[0] == roll_list[1]:
                                    doubles += 1
                                else:
                                    doubles = -1
                                if doubles == 3:
                                    self.PS.go_to_jail_3_doubles(player.name)
                                    go_to_jail_action(player)
                                    break
                            roll = sum(roll_list)
                            player.last_roll = roll
                            player.position = (player.position + roll) % 40
                            self.PS.roll_info(roll, player.position, self.board.tile_dict)
                            perform_action(player, self.tile_rents[str(player.position)], game)
                            self.actual_turn += 1

        self.player_turn += 1

    def pre_turn_actions(self, player):
        action_bool = True
        while action_bool:
            self.PS.ask_pre_turn_action(player.name)
            if input().capitalize() == "Y":
                # Print list of actions
                choose_preturn_action(player, self.player_list, self.player_turn)
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

    def check_game_active(self):
        player_count = 0
        winner = None
        for p in self.player_list:
            if p.in_game:
                player_count += 1
                winner = p

        if player_count < 2:
            self.PS.game_won(winner.name)
            return False

        else:
            return True

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

while game.player_turn < 50 and game.check_game_active():
    game.take_turn()
