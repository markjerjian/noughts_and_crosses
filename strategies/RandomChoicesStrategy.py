import random
from strategies.BaseStrategy import BaseStrategy


class RandomChoicesStrategy:
    def __init__(self):
        pass

    def decide_where_to_go(self, board, symbol=1):
        available_spots = [idx for idx, val in enumerate(board.state) if val == 0]
        return random.choice(available_spots)
