from stepping import SteppingPiece

class King(SteppingPiece):
    def __init__(self, board, pos, color):
        SteppingPiece.__init__(self, board, pos, color)

    def move_directions(self):
        return [[-1, -1],
                [-1, 0],
                [-1, 1],
                [0, -1],
                [0, 1],
                [1, -1],
                [1, 0],
                [1, 1]]

    def symbol(self):
        return " K "
