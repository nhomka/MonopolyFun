from TransactionEvent import TransactionEvent, create_and_assign_event, assign_event
import Auctions


def buy_property(player, tile, turn):
    if not tile.owner:
        value = tile.purchase_price
        if player.bank > value:
            print("Player", player.name, "has:", player.bank, "dollars.  Proceed to buy", tile.name, "for: ",
                  value, "dollars?")
            if input().capitalize() == "Y":
                player.bank -= value
                player.owned_properties.append(tile)
                tile.owner = player
                create_and_assign_event(tile, 'Buy Property', turn, player, "Bank", value, value, [tile, player])
                print(player.name, "has purchased", tile.name, "for", value, "and now has", player.bank, "dollars.")
            else:
                print("Player", player.name, "has opted not to purchase", tile.name)
        else:
            print("Player", player.name, "does not have sufficient funds to purchase", tile.name)


def mortgage_property(player, tile, turn):
    if player == tile.owner:
        value = tile.mortgage_price
        print("Player", player.name, "has:", player.bank, "dollars.  Proceed to mortgage", tile.name, "for: ",
              value, "dollars?")
        get_input = input().capitalize()
        if get_input == "Y":
            if tile.mortgage():
                player.bank += value
                create_and_assign_event(tile, 'Mortgage', turn, "Bank", player, value, value, [tile, player])


def unmortgage_property(player, tile, turn):
    if player == tile.owner:
        value = int(tile.mortgage_price * 1.1)
        if player.bank > value:
            print("Player", player.name, "has:", player.bank, "dollars.  Proceed to unmortgage", tile.name, "for: ",
                  value, "dollars?")
            get_input = input().capitalize()
            if get_input == "Y":
                if tile.unmortgage():
                    player.bank -= value
                    create_and_assign_event(tile, 'Unmortgage', turn, player, "Bank", value, value, [tile, player])
        else:
            print("Player", player.name, "does not have sufficient funds to unmortgage", tile.name)


def pay_double_rr_rent(player, tile, turn):
    transaction_event = None
    owned_rails = 0
    for item in tile.owner.owned_properties:
        if len(item.rents) == 4:
            owned_rails += 1
    if owned_rails >= 1:
        total_owed = tile.rents[owned_rails - 1] * 2
    else:
        total_owed = 0
    if player.bank >= total_owed:
        player.bank -= total_owed
        tile.owner.bank += total_owed
        transaction_event = TransactionEvent(tile, 'Rent', turn, player, tile.owner, total_owed, total_owed)
        print("Player", player.name, "has paid", tile.owner.name, "$", total_owed)
    else:
        print("Player", player.name, "cannot afford to pay", tile.owner.name, "$", total_owed)
        player.increase_bank(total_owed)
    assign_event([player, tile.owner], transaction_event)


def pay_rent(player, tile, turn):
    transaction_event = None
    if tile.is_mortgaged:
        print(tile.name, "is mortgaged,", player.name, "owes no rent")
        return
    if len(tile.rents) == 6:
        total_owed = tile.rents[tile.houses]
        if tile.houses == 0 and player.verify_set_owned(tile):
            total_owed *= 2
        if player.bank >= total_owed:
            player.bank -= total_owed
            tile.owner.bank += total_owed
            transaction_event = TransactionEvent(tile, 'Rent', turn, player, tile.owner, total_owed, total_owed)
            print("Player", player.name, "has paid", tile.owner.name, "$", total_owed)
        else:
            print("Player", player.name, "cannot afford to pay", tile.owner.name, "$", total_owed)
            player.increase_bank(total_owed)
    elif len(tile.rents) == 4:
        owned_rails = 0
        for item in tile.owner.owned_properties:
            if len(item.rents) == 4:
                owned_rails += 1
        if owned_rails >= 1:
            total_owed = tile.rents[owned_rails - 1]
        else:
            total_owed = 0
        if player.bank >= total_owed:
            player.bank -= total_owed
            tile.owner.bank += total_owed
            transaction_event = TransactionEvent(tile, 'Rent', turn, player, tile.owner, total_owed, total_owed)
            print("Player", player.name, "has paid", tile.owner.name, "$", total_owed)
        else:
            print("Player", player.name, "cannot afford to pay", tile.owner.name, "$", total_owed)
            player.increase_bank(total_owed)
    elif len(tile.rents) == 2:
        owned_utilities = 0
        for item in tile.owner.owned_properties:
            if len(item.rents) == 2:
                owned_utilities += 1
        if owned_utilities >= 1:
            total_owed = tile.rents[owned_utilities - 1] * player.last_roll
        else:
            total_owed = 0
        if player.bank >= total_owed:
            player.bank -= total_owed
            tile.owner.bank += total_owed
            transaction_event = TransactionEvent(tile, 'Rent', turn, player, tile.owner, total_owed, total_owed)
            print("Player", player.name, "has paid", tile.owner.name, "$", total_owed)
        else:
            print("Player", player.name, "cannot afford to pay", tile.owner.name, "$", total_owed)
            player.increase_bank(total_owed)
    assign_event([player, tile, tile.owner], transaction_event)


def pay_bank(player, amount, tile, turn):
    if player.bank > amount:
        player.bank -= amount
        create_and_assign_event(tile, 'Pay Bank', turn, player, 'Bank', amount, amount, [player, tile])
    else:
        player.increase_bank(amount)
        if player.in_game:
            player.bank -= amount
            create_and_assign_event(tile, 'Pay Bank', turn, player, 'Bank', amount, amount, [player, tile])
        else:
            player.liquidate_all_assets()
            player.bank = 0


def get_paid_from_bank(player, amount, tile, turn):
    player.bank += amount
    create_and_assign_event(tile, 'Bank Pays', turn, 'Bank', player, amount, amount, [player, tile])


def pay_income_tax(player, tile, turn):
    if player.get_total_assets() > 1999:
        cost = 200
        pay_bank(player, cost, tile, turn)
    else:
        cost = int(player.get_total_assets()*.1)
        pay_bank(player, cost, tile, turn)
    return cost


def pay_each_player(player, amount, player_list, tile, turn):
    player_count = 0
    for p in player_list:
        if p != player:
            player_count += 1

    total_owed = amount*player_count

    if player.bank > total_owed:
        player.bank -= total_owed
        for p in player_list:
            if p != player:
                p.bank += amount
        receivers = [a for a in player_list if a != player]
        assignees = [tile]
        assignees.extend(player_list)
        create_and_assign_event(tile, 'Pay All Players', turn, player, receivers, amount, total_owed, assignees)
    else:
        # player has to make money to pay.
        return


def all_players_pay(player, amount, player_list, tile, turn):
    for p in player_list:
        if p != player:
            if p.bank >= amount:
                p.bank -= amount
                player.bank += amount
            else:
                p.increase_bank(amount)
                return
    payers = [a for a in player_list if a != player]
    assignees = [tile]
    assignees.extend(player_list)
    create_and_assign_event(tile, 'Pay All Players', turn, payers, player, amount, amount*len(payers), assignees)


def pay_cc_house_tax(player, tile, turn):
    house_count = 0
    hotel_count = 0
    for p in player.get_properties_list():
        if p.houses == 5:
            hotel_count += 1
        else:
            house_count += p.houses

    total_owed = house_count * 40 + hotel_count * 115
    pay_bank(player, total_owed, tile, turn)
    print(player.name, "has paid the bank", total_owed)


def pay_chance_house_tax(player, tile, turn):
    house_count = 0
    hotel_count = 0
    for p in player.get_properties_list():
        if p.houses == 5:
            hotel_count += 1
        else:
            house_count += p.houses

    total_owed = house_count * 25 + hotel_count * 100
    pay_bank(player, total_owed, tile, turn)
    print(player.name, "has paid the bank", total_owed)

def transfer_assets_to_player(giver, receiver):
    for item in giver.owned_properties:
        giver.owned_properties.remove(item)
        receiver.owned_properties.append(item)
    bank_value = giver.bank
    giver.bank = 0
    receiver.bank += bank_value
    if giver.jail_passes >= 1:
        jail_passes_count = giver.jail_passes
        giver.jail_passes = 0
        receiver.jail_passes += jail_passes_count