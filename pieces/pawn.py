from piece import Piece

class Pawn(Piece):
    def __init__(self):
        Piece.__init__(self)

    def move_directions(self):
        pass

    def symbol(self):
        return " P "
