import Transactions


def auction_property_from_bank(bidder_list, tile, turn):
    bidding_price = tile.purchase_price
    highest_bidder = None
    purchase_price = None
    while len(bidder_list) > 1:
        for p in bidder_list:
            if len(bidder_list) > 1:
                print(p.name, "would you like to bid on", tile.name, "for $", bidding_price)
                if input().capitalize() == "Y":
                    if p.bank > bidding_price:
                        highest_bidder = p
                        purchase_price = bidding_price
                        bidding_price += 10
                    else:
                        print(p.name, "cannot afford the bidding price and is out of the auction")
                        bidder_list.remove(p)
                else:
                    bidder_list.remove(p)
            else:
                if highest_bidder:
                    print(tile.name, "has been auctioned to", highest_bidder.name, "for $", purchase_price)
                    tile.owner = highest_bidder
                    Transactions.pay_bank(highest_bidder, purchase_price, tile, turn)
                else:
                    print("Nobody has bid on the tile and it has gone unsold")