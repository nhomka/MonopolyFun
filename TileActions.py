import Transactions
import Cards
import Dice


def perform_action(player, tile, game):
    # Check if passed go this roll
    if tile.position == 0 or player.last_roll > tile.position:
        Transactions.get_paid_from_bank(player, 200)
        print("Player", player.name, "has passed Go and collected $200.")

    # Community Chest
    elif tile.position in [2, 17, 33]:
        print("Player", player.name, "has landed on Community Chest.")
        community_chest_action(player, game)

    # Income Tax
    elif tile.position == 4:
        income_tax_cost = Transactions.pay_income_tax(player)
        print("Player", player.name, "has landed on income tax and paid", income_tax_cost, "dollars.")

    # Chance
    elif tile.position in [7, 22, 36]:
        print("Player", player.name, "has landed on Chance.")
        chance_action(player, game)

    # Jail/Just Visiting
    elif tile.position == 10:
        jail_or_visiting_action(player)

    # Free Parking
    elif tile.position == 20:
        Transactions.get_paid_from_bank(player, 500)
        print("Player", player.name, "has landed on free parking and received $500.")

    # Go To Jail
    elif tile.position == 30:
        go_to_jail_action(player)

    # Luxury Tax
    elif tile.position == 38:
        Transactions.pay_bank(player, 75)
        print("Player", player.name, "has landed on Luxury Tax and been charged $75")

    # Property
    else:
        # Buy if unowned
        if not tile.owner:
            purchase_cost = tile.purchase_price
            if player.bank >= purchase_cost:
                print("Purchase", tile.name, "for:", purchase_cost, "dollars?")
                get_input = input().capitalize()
                if get_input == "Y":
                    player.bank -= purchase_cost
                    player.owned_properties.append(tile)
                    tile.owner = player
                    print("Player", player.name, "has purchased", tile.name, "for", purchase_cost)
                    print("Player", player.name, "now has", player.bank, "dollars")
                elif get_input == "N":
                    print("Player", player.name, "has opted not to purchase", tile.name)
            else:
                print("Player", player.name, "does not have sufficient funds to purchase", tile.name)

        # Pay rent
        elif tile.owner and tile.owner != player:
            if len(tile.rents) == 6:
                total_owed = tile.rents[tile.houses]
                if player.bank >= total_owed:
                    player.bank -= total_owed
                    tile.owner.bank += total_owed
                    print("Player", player.name, "has paid", tile.owner.name, "$", total_owed)
                else:
                    print("Player", player.name, "cannot afford to pay", tile.owner.name, "$", total_owed)
            elif len(tile.rents) == 4:
                owned_rails = 0
                for item in tile.owner.owned_properties:
                    if len(item.rents) == 4:
                        owned_rails += 1
                if owned_rails >= 1:
                    total_owed = tile.rents[owned_rails-1]
                else:
                    total_owed = 0
                if player.bank >= total_owed:
                    player.bank -= total_owed
                    tile.owner.bank += total_owed
                    print("Player", player.name, "has paid", tile.owner.name, "$", total_owed)
                else:
                    print("Player", player.name, "cannot afford to pay", tile.owner.name, "$", total_owed)
            elif len(tile.rents) == 2:
                owned_utilities = 0
                for item in tile.owner.owned_properties:
                    if len(item.rents) == 2:
                        owned_utilities += 1
                if owned_utilities >= 1:
                    total_owed = tile.rents[owned_utilities-1]*player.last_roll
                else:
                    total_owed = 0
                if player.bank >= total_owed:
                    player.bank -= total_owed
                    tile.owner.bank += total_owed
                    print("Player", player.name, "has paid", tile.owner.name, "$", total_owed)
                else:
                    print("Player", player.name, "cannot afford to pay", tile.owner.name, "$", total_owed)

        # Do nothing
        return


def community_chest_action(player, game):
    # Implement
    card = game.cards.draw_cc_card(game)
    print(card.text)
    if card.action == 'AP':
        Transactions.all_players_pay(player, card.amount, game.player_list)
        print(player.name, "has been paid", card.amount, "by all players")
    elif card.action == 'BP':
        Transactions.get_paid_from_bank(player, card.amount)
        print(player.name, "has been paid", card.amount, "by the bank")
    elif card.action == 'JF':
        player.jail_passes += 1
        print(player.name, "has received a Get Out Of Jail Free card")
    elif card.action == 'M':
        move_to_card_destination(card, player)
        print(player.name, "has moved to", game.board.tile_dict[player.position])
    elif card.action == 'PA':
        Transactions.pay_each_player(player, card.amount, game.player_list)
        print(player.name, "has paid each player", card.amount)
    elif card.action == 'PB':
        Transactions.pay_bank(player, card.amount)
        print(player.name, "has paid the bank", card.amount)
    elif card.action == 'PH':
        Transactions.pay_cc_house_tax(player)

    return


def chance_action(player, game):
    card = game.cards.draw_chance_card(game)
    print(card.text)
    if card.action == 'AP':
        Transactions.all_players_pay(player, card.amount, game.player_list)
        print(player.name, "has been paid", card.amount, "by all players")
    elif card.action == 'BP':
        Transactions.get_paid_from_bank(player, card.amount)
        print(player.name, "has been paid", card.amount, "by the bank")
    elif card.action == 'JF':
        player.jail_passes += 1
        print(player.name, "has received a Get Out Of Jail Free card")
    elif card.action == 'M':
        move_to_card_destination(card, player)
        print(player.name, "has moved to", game.board.tile_dict[player.position])
    elif card.action == 'PA':
        Transactions.pay_each_player(player, card.amount, game.player_list)
        print(player.name, "has paid each player", card.amount)
    elif card.action == 'PB':
        Transactions.pay_bank(player, card.amount)
        print(player.name, "has paid the bank", card.amount)
    elif card.action == 'PH':
        Transactions.pay_cc_house_tax(player)

    return


def move_to_card_destination(card, player):
    old_position = player.position
    if card.destination == 'Jail':
        go_to_jail_action(player)
    elif card.destination == 'Boardwalk':
        player.position = 39
    elif card.destination == 'Go':
        player.position = 0
    elif card.destination == 'RR':
        if player.position <= 5:
            player.position = 5
        elif player.position <= 15:
            player.position = 15
        elif player.position <= 25:
            player.position = 25
        elif player.position <= 35:
            player.position = 35
        else:
            player.position = 5
    elif card.destination == 'Reading':
        player.position = 5
    elif card.destination == 'St. Charles':
        player.position = 11
    elif card.destination == 'Illinois':
        player.position = 24
    elif card.destination == 'Back3':
        if player.position >= 3:
            player.position = player.position - 3
        else:
            player.position = player.position + 37
    if player.position < old_position and not player.in_jail:
        player.bank += 200
        print(player.name, "has passed Go and collected $200.")


def jail_or_visiting_action(player):
    if not player.in_jail:
        print("Player", player.name, "is just visiting jail.")
    else:
        print("Player", player.name, "is still in jail.")
    return


def go_to_jail_action(player):
    print("Player: ", player.name, "is going directly to jail.  Do not pass go, do not collect any income")
    player.position = 10
    player.in_jail = True
    return
