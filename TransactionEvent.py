class TransactionEvent:

    def __init__(self, tile, transaction_type, turn, payers, receivers, individual_cost, total_paid):
        self.tile = tile
        self.transaction_type = transaction_type
        self.turn = turn
        self.payers = payers
        self.receivers = receivers
        self.individual_cost = individual_cost
        self.total_paid = total_paid



