from sliding import SlidingPiece

class Bishop(SlidingPiece):
    def __init__(self):
        SlidingPiece.__init__(self)

    def move_directions(self):
        return [[-1, -1],
                [-1, 1],
                [1, -1],
                [1, 1]]

    def symbol(self):
        return " B "
