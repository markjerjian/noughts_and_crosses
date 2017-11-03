from classes.Board import Board
from classes.RoundResults import RoundResults


class Round:
    def __init__(self, players_list):
        self.board = Board()

        self.players = players_list

        self.turn_counter = 0
        self.player_turn_idx = self.turn_counter % len(self.players)

        self.finished = False
        self.results = RoundResults()

    def play_round(self):
        for i in range(self.board.dimension**2):
            self.play_turn()
            if self.finished:
                break

        return self.results

    def play_turn(self):
        player = self.players[self.player_turn_idx]
        print('{} is playing turn number {}'.format(player.name, self.turn_counter))

        position = player.strategy.decide_where_to_go(board=self.board, symbol=player.symbol)
        self.board.update_with_move(symbol=player.symbol, position=position)
        self.turn_counter += 1
        self.player_turn_idx = (self.player_turn_idx + 1) % len(self.players)

        print(self.board)
        print('--------')

        if self.board.check_for_winner() != 0 or self.turn_counter >= self.board.dimension**2:
            print('Game over')
            self.finished = True
