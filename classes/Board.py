import random


class Board:
    def __init__(self, dimension=3):
        self.dimension = dimension
        self.state = [0] * (self.dimension ** 2)

    def __repr__(self):
        dim = self.dimension
        output = '\n'.join(
            ['\t'.join([str(x) for x in self.state[row_idx * dim:row_idx * dim + dim]])
             for row_idx in range(dim)]
        )
        return output

    def check_for_winner(self):
        dim = self.dimension

        # Horizontal Winner
        for row in range(dim):
            if abs(sum(self.state[row*dim:row*dim + dim])) >= dim:
                return self.state[row * dim]

        # Vertical winner
        for column in range(dim):
            if abs(sum(self.state[column::dim])) >= dim:
                return self.state[column]

        # Diagonal winner
        if abs(sum(self.state[0::dim+1])) >= dim:
            return self.state[0]
        if abs(sum(self.state[2::dim-1])) >= dim:
            return self.state[2]

        else:
            return 0

    def update_with_move(self, symbol, position):
        assert self.state[position] == 0
        self.state[position] = symbol

if __name__ == "__main__":
    board = Board()

    for i in range(10):
        for idx, entry in enumerate(board.state):
            board.state[idx] = random.randint(-1, 1)
        print(board)
        print(board.check_for_winner())
