from strategies.RandomChoicesStrategy import RandomChoicesStrategy


class Player:
    def __init__(self, name='Default name'):
        self.name = name if name else None
        self.strategy = None
        self.symbol = None

    def set_name(self, name):
        self.name = name

    def set_symbol(self, symbol):
        self.symbol = symbol

    def set_strategy(self, strategy):
        self.strategy = strategy
