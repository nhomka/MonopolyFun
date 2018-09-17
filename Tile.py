class Tile:
    purchase_price = None
    rents = None
    mortgage_price = None
    owner = None
    houses = None
    is_mortgaged = None
    name = None
    position = None
    color = None
    house_cost = None

    def __init__(self, purchase_price=0, rents=None, mortgage_price=0):
        self.purchase_price = purchase_price
        self.rents = rents
        self.mortgage_price = mortgage_price
        self.houses = 0
        self.is_mortgaged = False
        self.house_cost = 0

    def mortgage(self):
        if not self.is_mortgaged:
            self.is_mortgaged = True
            return True
        else:
            print("property is already mortgaged")
            return False

    def unmortgage(self):
        if self.is_mortgaged:
            self.is_mortgaged = False
            return True
        else:
            print("property is not mortgaged")
            return False


    def create_all_properties(self, edition):
        if edition == 0:
            tile_rents={}
            tile_rents["1"] = Tile(60, [2, 10, 30, 90, 160, 250], 30)
            tile_rents["3"] = Tile(60, [4, 20, 60, 180, 320, 450], 30)
            tile_rents["5"] = Tile(200, [25, 50, 100, 200], 100)
            tile_rents["6"] = Tile(100, [6, 30, 90, 270, 400, 550], 50)
            tile_rents["8"] = Tile(100, [6, 30, 90, 270, 400, 550], 50)
            tile_rents["9"] = Tile(120, [8, 40, 100, 300, 450, 600], 60)
            tile_rents["11"] = Tile(140, [10, 50, 150, 450, 625, 750], 70)
            tile_rents["12"] = Tile(150, [4, 10], 75)
            tile_rents["13"] = Tile(140, [10, 50, 150, 450, 625, 750], 70)
            tile_rents["14"] = Tile(160, [12, 60, 180, 500, 700, 900], 80)
            tile_rents["15"] = Tile(200, [25, 50, 100, 200], 100)
            tile_rents["16"] = Tile(180, [14, 70, 200, 550, 750, 950], 90)
            tile_rents["17"] = Tile(180, [14, 70, 200, 550, 750, 950], 90)
            tile_rents["19"] = Tile(200, [16, 80, 220, 600, 800, 1000], 100)
            tile_rents["21"] = Tile(220, [18, 90, 250, 700, 875, 1050], 110)
            tile_rents["23"] = Tile(220, [18, 90, 250, 700, 875, 1050], 110)
            tile_rents["24"] = Tile(240, [20, 100, 300, 750, 925, 1100], 120)
            tile_rents["25"] = Tile(200, [25, 50, 100, 200], 100)
            tile_rents["26"] = Tile(260, [22, 110, 330, 800, 975, 1150], 130)
            tile_rents["27"] = Tile(260, [22, 110, 330, 800, 975, 1150], 130)
            tile_rents["28"] = Tile(150, [4, 10], 75)
            tile_rents["29"] = Tile(280, [24, 120, 360, 850, 1025, 1200], 140)
            tile_rents["31"] = Tile(300, [26, 130, 390, 900, 1100, 1275], 150)
            tile_rents["33"] = Tile(300, [26, 130, 390, 900, 1100, 1275], 150)
            tile_rents["34"] = Tile(320, [28, 150, 450, 1000, 1200, 1400], 160)
            tile_rents["35"] = Tile(200, [25, 50, 100, 200], 100)
            tile_rents["37"] = Tile(350, [35, 175, 500, 1100, 1300, 1500], 175)
            tile_rents["39"] = Tile(400, [50, 200, 600, 1400, 1700, 2000], 200)
            return tile_rents