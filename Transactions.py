from TransactionEvent import TransactionEvent


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
                tile.transaction_list.append(TransactionEvent(tile, 'Buy Property', turn, player, "Bank", value, value))
                print(player.name, "has purchased", tile.name, "for", value, "and now has", player.bank, "dollars.")
            else:
                print("Player", player.name, "has opted not to purchase", tile.name)
        else:
            print("Player", player.name, "does not have sufficient funds to purchase", tile.name)


def mortgage_property(player, tile):
    if player == tile.owner:
        value = tile.mortgage_price
        print("Player", player.name, "has:", player.bank, "dollars.  Proceed to mortgage", tile.name, "for: ",
              value, "dollars?")
        get_input = input().capitalize()
        if get_input == "Y":
            if tile.mortgage():
                player.bank += value


def unmortgage_property(player, tile):
    if player == tile.owner:
        value = tile.mortgage_price
        if player.bank > value:
            print("Player", player.name, "has:", player.bank, "dollars.  Proceed to unmortgage", tile.name, "for: ",
                  value, "dollars?")
            get_input = input().capitalize()
            if get_input == "Y":
                if tile.unmortgage():
                    player.bank -= value


def pay_rent(player, tile):
    if not tile.owner or player == tile.owner:
        print("No rent is owed.")
        return
    else:
        owed_rent = tile.rents[tile.houses]
        print("Player", player.name, "owes:", tile.owner.name, owed_rent, "dollars.")
        if player.bank > owed_rent:
            player.bank -= owed_rent
            tile.owner.bank += owed_rent
        else:
            # player has to make money to pay.
            return


def pay_bank(player, amount):
    if player.bank > amount:
        player.bank -= amount
    else:
        # player has to make enough money to pay.
        return


def get_paid_from_bank(player, amount):
    player.bank += amount


def pay_income_tax(player):
    if player.bank > 999:
        player.bank -= 100
        return 100
    else:
        cost = int(player.bank * .1)
        player.bank -= cost
        return cost


def pay_each_player(player, amount, player_list):
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
    else:
        # player has to make money to pay.
        return


def all_players_pay(player, amount, player_list):
    for p in player_list:
        if p != player:
            if p.bank >= amount:
                p.bank -= amount
                player.bank += amount
            else:
                # player has to make money to pay.
                return


def pay_cc_house_tax(player):
    house_count = 0
    hotel_count = 0
    for p in player.get_properties_list():
        if p.houses == 5:
            hotel_count += 1
        else:
            house_count += p.houses

    total_owed = house_count * 40 + hotel_count * 115
    pay_bank(player, total_owed)
    print(player.name, "has paid the bank", total_owed)


def pay_chance_house_tax(player):
    house_count = 0
    hotel_count = 0
    for p in player.get_properties_list():
        if p.houses == 5:
            hotel_count += 1
        else:
            house_count += p.houses

    total_owed = house_count * 25 + hotel_count * 100
    pay_bank(player, total_owed)
    print(player.name, "has paid the bank", total_owed)
