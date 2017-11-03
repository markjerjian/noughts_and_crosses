from classes.Player import Player
from classes.Round import Round
from classes.MatchResults import MatchResults
from strategies.RandomChoicesStrategy import RandomChoicesStrategy


class Match:
    def __init__(self, number_of_rounds=1, strategy_0=RandomChoicesStrategy(), strategy_1=RandomChoicesStrategy()):
        self.number_of_rounds = number_of_rounds
        self.round_counter = 0
        self.scores = [0, 0]

        self.players = []
        self.initialise_players()
        self.assign_player_names(['Player1', 'Player2'])
        self.assign_players_symbols([1, -1])
        self.assign_player_strategies([strategy_0, strategy_1])

        self.match_results = MatchResults()

    def initialise_players(self):
        self.players.append(Player())
        self.players.append(Player())

    def assign_player_names(self, names_list):
        assert len(names_list) == len(self.players)
        for player, name in zip(self.players, names_list):
            player.set_name(name)

    def assign_players_symbols(self, symbol_list):
        assert len(self.players) == 2, 'Trying to assign 2 symbols to players but found %d players' % len(self.players)
        for player, symbol in zip(self.players, symbol_list):
            player.set_symbol(symbol)

    def assign_player_strategies(self, strategy_list):
        assert len(strategy_list) == len(self.players)
        for idx, strategy in enumerate(strategy_list):
            self.players[idx].set_strategy(strategy)

    def play_match(self):
        print('Starting match')
        for i in range(self.number_of_rounds):
            print('Playing round number {}'.format(i))
            new_round = Round(self.players)
            round_results = new_round.play_round()
            self.update_match_results(self.round_counter, round_results)
            self.round_counter += 1

    def update_match_results(self, round_idx, round_results):
        pass
