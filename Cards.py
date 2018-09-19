import Dice

class Cards:
    unused_chance_cards = []
    used_chance_cards = []
    unused_cc_cards = []
    used_cc_cards = []
    chance_card_dict = {}
    cc_card_dict = {}
    edition = 0

    def __init__(self, edition=0):
        self.initialize_card_set(edition)

    def initialize_card_set(self):
        if self.edition == 0:
            self.chance_card_dict = {
                1:  self.Card('M', None, 'RR', "Advance token to the nearest Railroad and pay owner "
                                               "Twice the Rental to which he/she is otherwise entitled.\n"
                                               "If Railroad is UNOWNED, you may buy it from the Bank. "
                                               "If you pass Go, collect $200."),
                2:  self.Card('BP', 150, None, "Your building and loan matures.\n Collect $150."),
                3:  self.Card('M', None, 'Illinois', "Advance to Illinois Ave.\n If you pass Go, collect $200."),
                4:  self.Card('PH', None, None, "Make general repairs on all your property.\n "
                                                "For each house pay $25, for each hotel pay $100."),
                5:  self.Card('M', None, 'St. Charles', "Advance to St. Charles Place.\n "
                                                        "If you pass Go, collect $200."),
                6:  self.Card('BP', 50, None, "Bank pays you dividend of $50."),
                7:  self.Card('M', None, 'Reading', "Take a ride on the reading.\n If you pass Go, collect $200."),
                8:  self.Card('PB', 15, None, "Pay poor tax of $15."),
                9:  self.Card('M', None, 'Back3', "Go back 3 spaces."),
                10: self.Card('PA', 50, None, "You have been elected Chairman of the Board.\n Pay each player $50."),
                11: self.Card('M', None, 'RR', "Advance token to the nearest Railroad and pay owner "
                                               "Twice the Rental to which he/she is otherwise entitled.\n"
                                               "If Railroad is UNOWNED, you may buy it from the Bank.  "
                                               "If you pass Go, collect $200."),
                12: self.Card('M', None, 'Jail', "Go directly to jail.\n Do not pass go, do not collect $200."),
                13: self.Card('M', None, 'Go', "Advance to Go.  Collect $200."),
                14: self.Card('JF', None, None, "This card may be kept until needed, or sold.\n Get out of jail free."),
                15: self.Card('M', None, 'Boardwalk', "Take a walk on the Boardwalk!\n "
                                                      "Advance token to Boardwalk.  If you pass Go, collect $200.")
            }
            self.cc_card_dict = {
                1:  self.Card('BP', 25, None, "Receive for services $25."),
                2:  self.Card('BP', 45, None, "From sale of stock you get $45."),
                3:  self.Card('PB', 150, None, "Pay school tax of $150."),
                4:  self.Card('PH', None, None, "You are assessed for street repairs.\n "
                                                "For each house pay $40, for each hotel pay $115."),
                5:  self.Card('PB', 50, None, "Doctor's fee, pay $50."),
                6:  self.Card('BP', 100, None, "You inherit $100."),
                7:  self.Card('BP', 200, None, "Bank error in your favor, collect $200."),
                8:  self.Card('PB', 100, None, "Pay hospital $100."),
                9:  self.Card('BP', 10, None, "You have won second prize in a beauty contest.  Collect $10."),
                10: self.Card('AP', 50, None, "Grand Opera Opening.\n "
                                              "Collect $50 from every player for opening night seats."),
                11: self.Card('M', None, 'Go', "Advance to go.  Collect $200."),
                12: self.Card('M', None, 'Jail', "Go directly to jail.\n Do not pass go, do not collect $200."),
                13: self.Card('BP', 20, None, "Income tax refund.  Collect $20."),
                14: self.Card('JF', None, None, "This card may be kept until needed, or sold.\n Get out of jail free."),
                15: self.Card('BP', 100, None, "Life insurance matures, collect $100.")
            }

            for item in self.chance_card_dict:
                self.unused_chance_cards.append(item)

            for item in self.cc_card_dict:
                self.unused_cc_cards.append(item)

    def draw_cc_card(self, game):
        card_draw = Dice.draw_random_card(game.cards.unused_cc_cards)
        card_int = game.cards.unused_cc_cards[card_draw]
        game.cards.unused_cc_cards.remove(card_int)
        card = game.cards.cc_card_dict[card_int]
        if card.action != 'JF':
            game.cards.used_cc_cards.append(card_int)
        return card

    def draw_chance_card(self, game):
        card_draw = Dice.draw_random_card(game.cards.unused_chance_cards)
        card_int = game.cards.unused_chance_cards[card_draw]
        game.cards.unused_cc_cards.remove(card_int)
        card = game.cards.chance_card_dict[card_int]
        if card.action != 'JF':
            game.cards.used_cc_cards.append(card_int)
        return card

    class Card:
        action = None
        amount = None
        destination = None
        text = None

        def __init__(self, action, amount, destination, text):
            self.action = action
            self.amount = amount
            self.destination = destination
            self.text = text
