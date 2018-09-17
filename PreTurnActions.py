# Manage any mortgage related action
def manage_mortgages(player):
    return


# Manage any house/hotel related action
def manage_houses(player):
    print("On which property set would you like to manage houses/hotels? (Access by index)")
    properties_list = player.get_properties_list()
    print([i.name for i in properties_list])
    get_input = int(input())
    if 0 <= get_input < len(properties_list):
        managed_property = properties_list[get_input]
        owned_count = player.verify_set_owned(managed_property)
        if not owned_count:
            print("Player does not own full property set")
            return
        print("Managing property:", managed_property.name, "Would you like to buy ('B') or sell ('S') houses/hotels?")
        get_input = input().capitalize()
        if get_input == "B":
            one_set_of_houses_cost = owned_count*managed_property.house_cost
            print("There are currently", managed_property.houses, "houses on each property in this set.")
            print("One set of houses on", managed_property.name, "costs", one_set_of_houses_cost, "Purchase how many?")
            count_input = int(input())
            if 1 <= count_input <= (5-managed_property.houses):
                if player.bank >= count_input*one_set_of_houses_cost:
                    player.bank -= count_input * one_set_of_houses_cost
                    for item in player.owned_properties:
                        if item.color == managed_property.color:
                            item.houses += count_input
                    print(count_input, "houses have been added to each of the", managed_property.color, "properties.")
                else:
                    print(player.name, "can not afford this purchase.")
            else:
                print("This is not a valid purchase.")

    return


# Manage any trade with other players
def request_trade(player):
    return


# If a Get Out Of Jail Free card is owned by the player, use it to leave jail.
def get_out_of_jail_free(player):
    return
