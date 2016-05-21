from stepping import SteppingPiece

class Knight(SteppingPiece):
    def __init__(self):
        SteppingPiece.__init__(self)

    def move_directions(self):
        return [[-1, 2],
                [1, 2],
                [1, -2],
                [-1, -2],
                [-2, -1],
                [2, 1],
                [-2, 1],
                [2, -1]]

    def symbol(self):
        return " k "
