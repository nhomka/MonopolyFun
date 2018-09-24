class TransactionEvent:

    def __init__(self, tile, transaction_type, turn, payers, receivers, individual_cost, total_paid):
        self.tile = tile
        self.transaction_type = transaction_type
        self.turn = turn
        self.payers = payers
        self.receivers = receivers
        self.individual_cost = individual_cost
        self.total_paid = total_paid


def create_and_assign_event(tile, transaction_type, turn, payers, receivers, individual_cost, total_paid, assignees):
    event = TransactionEvent(tile, transaction_type, turn, payers, receivers, individual_cost, total_paid)
    assign_event(assignees, event)


def assign_event(assignees, event):
    for a in assignees:
        a.transaction_list.append(event)