from sliding import SlidingPiece

class Rook(SlidingPiece):
    def __init__(self):
        SlidingPiece.__init__(self)

    def move_directions(self):
        return [[-1, 0],
                [0, -1],
                [0, 1],
                [1, 0]]

    def symbol(self):
        return " R "
