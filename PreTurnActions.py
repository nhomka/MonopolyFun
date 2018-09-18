def choose_preturn_action(player):
    print("Manage: Mortgages ('M'), Houses/Hotels ('H'), or Trades ('T')?")
    get_input = input().capitalize()
    if get_input == 'M':
        manage_mortgages(player)
    elif get_input == 'H':
        manage_houses(player)
    elif get_input == 'T':
        return


# Manage any mortgage related action
def manage_mortgages(player):
    mortgaged_properties_list = player.get_mortgaged_properties_list()
    unmortgaged_properties_list = player.get_unmortgaged_properties_list()
    print("The following properties are mortgaged:")
    print([i.name for i in mortgaged_properties_list])
    print("The following properties are unmortgaged:")
    print([i.name for i in unmortgaged_properties_list])
    print("Would you like to mortgage ('M') or unmortgage ('U') a property?")
    get_input = input().capitalize()
    if get_input == "M":
        print("Which property would you like to mortgage? (Access by index)")
        print([i.name for i in unmortgaged_properties_list])
        property_input = int(input())
        if 0 <= property_input < len(unmortgaged_properties_list):
            selected_property = unmortgaged_properties_list[property_input]
            selected_property.is_mortgaged = True
            player.bank += selected_property.mortgage_price
            print("Property:", selected_property.name, "has been mortgaged for $", selected_property.mortgage_price)
    elif get_input == "U":
        print("Which property would you like to unmortgage? (Access by index)")
        print([i.name for i in mortgaged_properties_list])
        property_input = int(input())
        if 0 <= property_input < len(mortgaged_properties_list):
            selected_property = mortgaged_properties_list[property_input]
            selected_property.is_mortgaged = False
            player.bank -= selected_property.mortgage_price
            print("Property:", selected_property.name, "has been unmortgaged for $", selected_property.mortgage_price)
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
            print("Player does not own full property set or has mortgaged at least one property.")
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
        elif get_input == "S":
            if managed_property.houses >= 1:
                one_set_of_houses_cost = int((owned_count*managed_property.houses_cost)/2)
                print("There are currently", managed_property.houses, "houses on each property in this set.")
                print("One set of", managed_property.color, "houses is worth", one_set_of_houses_cost, "Sell how many?")
                count_input = int(input())
                if 1 <= count_input <= managed_property.houses:
                    player.bank += count_input * one_set_of_houses_cost
                    for item in player.owned_properties:
                        if item.color == managed_property.color:
                            item.houses -= count_input
                    print(count_input, "houses have been sold from each of the", managed_property.color, "properties.")
                else:
                    print("This is not a valid purchase")
            else:
                print("There are no houses on the", managed_property.color, "properties.")

    return


# Manage any trade with other players
def request_trade(player):
    return


# If a Get Out Of Jail Free card is owned by the player, use it to leave jail.
def get_out_of_jail_free(player):
    return
