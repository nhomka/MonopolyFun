from Tile import Tile

class Board:

    edition = None
    name = None
    banner = None
    tile_dict = None
    tile_rents = None

    def __init__(self, edition=0):
        self.edition = edition

    def create(self):
        self.tile_rents = {}
        if self.edition == 0:
            self.name = "Atlantic City Edition"
            # self.banner = ""

            self.tile_dict = {
                        0: "Go",
                        1: "Mediterranean Avenue",
                        2: "Community Chest",
                        3: "Baltic Avenue",
                        4: "Income Tax",
                        5: "Reading Railroad",
                        6: "Oriental Avenue",
                        7: "Chance",
                        8: "Vermont Avenue",
                        9: "Connecticut Avenue",
                        10: "Jail / Just Visiting",
                        11: "St. Charles Place",
                        12: "Electric Works",
                        13: "States Avenue",
                        14: "Virginia Avenue",
                        15: "Pennsylvania Railroad",
                        16: "St. James Place",
                        17: "Community Chest",
                        18: "Tennessee Avenue",
                        19: "New York Avenue",
                        20: "Free Parking",
                        21: "Kentucky Avenue",
                        22: "Chance",
                        23: "Indiana Avenue",
                        24: "Illinois Avenue",
                        25: "B & O Railroad",
                        26: "Atlantic Avenue",
                        27: "Ventnor Avenue",
                        28: "Water Works",
                        29: "Marvin Gardens",
                        30: "Go To Jail",
                        31: "Pacific Avenue",
                        32: "North Carolina Avenue",
                        33: "Community Chest",
                        34: "Pennsylvania Avenue",
                        35: "Short Line",
                        36: "Chance",
                        37: "Park Place",
                        38: "Luxury Tax",
                        39: "Boardwalk"}

            self.tile_rents["0"] = Tile()
            self.tile_rents["1"] = Tile(60, [2, 10, 30, 90, 160, 250], 30)
            self.tile_rents["2"] = Tile()
            self.tile_rents["3"] = Tile(60, [4, 20, 60, 180, 320, 450], 30)
            self.tile_rents["4"] = Tile()
            self.tile_rents["5"] = Tile(200, [25, 50, 100, 200], 100)
            self.tile_rents["6"] = Tile(100, [6, 30, 90, 270, 400, 550], 50)
            self.tile_rents["7"] = Tile()
            self.tile_rents["8"] = Tile(100, [6, 30, 90, 270, 400, 550], 50)
            self.tile_rents["9"] = Tile(120, [8, 40, 100, 300, 450, 600], 60)
            self.tile_rents["10"] = Tile()
            self.tile_rents["11"] = Tile(140, [10, 50, 150, 450, 625, 750], 70)
            self.tile_rents["12"] = Tile(150, [4, 10], 75)
            self.tile_rents["13"] = Tile(140, [10, 50, 150, 450, 625, 750], 70)
            self.tile_rents["14"] = Tile(160, [12, 60, 180, 500, 700, 900], 80)
            self.tile_rents["15"] = Tile(200, [25, 50, 100, 200], 100)
            self.tile_rents["16"] = Tile(180, [14, 70, 200, 550, 750, 950], 90)
            self.tile_rents["17"] = Tile()
            self.tile_rents["18"] = Tile(180, [14, 70, 200, 550, 750, 950], 90)
            self.tile_rents["19"] = Tile(200, [16, 80, 220, 600, 800, 1000], 100)
            self.tile_rents["20"] = Tile()
            self.tile_rents["21"] = Tile(220, [18, 90, 250, 700, 875, 1050], 110)
            self.tile_rents["22"] = Tile()
            self.tile_rents["23"] = Tile(220, [18, 90, 250, 700, 875, 1050], 110)
            self.tile_rents["24"] = Tile(240, [20, 100, 300, 750, 925, 1100], 120)
            self.tile_rents["25"] = Tile(200, [25, 50, 100, 200], 100)
            self.tile_rents["26"] = Tile(260, [22, 110, 330, 800, 975, 1150], 130)
            self.tile_rents["27"] = Tile(260, [22, 110, 330, 800, 975, 1150], 130)
            self.tile_rents["28"] = Tile(150, [4, 10], 75)
            self.tile_rents["29"] = Tile(280, [24, 120, 360, 850, 1025, 1200], 140)
            self.tile_rents["30"] = Tile()
            self.tile_rents["31"] = Tile(300, [26, 130, 390, 900, 1100, 1275], 150)
            self.tile_rents["32"] = Tile(300, [26, 130, 390, 900, 1100, 1275], 150)
            self.tile_rents["33"] = Tile()
            self.tile_rents["34"] = Tile(320, [28, 150, 450, 1000, 1200, 1400], 160)
            self.tile_rents["35"] = Tile(200, [25, 50, 100, 200], 100)
            self.tile_rents["36"] = Tile()
            self.tile_rents["37"] = Tile(350, [35, 175, 500, 1100, 1300, 1500], 175)
            self.tile_rents["38"] = Tile()
            self.tile_rents["39"] = Tile(400, [50, 200, 600, 1400, 1700, 2000], 200)
            for key in self.tile_rents:
                pair = self.tile_rents[key]
                pair.name = self.tile_dict[int(key)]
                pair.position = int(key)
                if pair.position < 5 and pair.rents and len(pair.rents) == 6:
                    pair.color = "purple"
                    pair.house_cost = 50
                elif pair.position < 10 and pair.rents and len(pair.rents) == 6:
                    pair.color = "light blue"
                    pair.house_cost = 50
                elif pair.position < 15 and pair.rents and len(pair.rents) == 6:
                    pair.color = "magenta"
                    pair.house_cost = 100
                elif pair.position < 20 and pair.rents and len(pair.rents) == 6:
                    pair.color = "orange"
                    pair.house_cost = 100
                elif pair.position < 25 and pair.rents and len(pair.rents) == 6:
                    pair.color = "red"
                    pair.house_cost = 150
                elif pair.position < 30 and pair.rents and len(pair.rents) == 6:
                    pair.color = "yellow"
                    pair.house_cost = 150
                elif pair.position < 35 and pair.rents and len(pair.rents) == 6:
                    pair.color = "green"
                    pair.house_cost = 200
                elif pair.position < 40 and pair.rents and len(pair.rents) == 6:
                    pair.color = "dark blue"
                    pair.house_cost = 200
                elif len(pair.rents) == 4:
                    pair.color = "black"
                elif len(pair.rents) == 2:
                    pair.color = "white"

        else:
            tile_dict = None
