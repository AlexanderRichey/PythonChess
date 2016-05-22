from piece import Piece

class Pawn(Piece):
    def __init__(self, board, pos, color):
        Piece.__init__(self, board, pos, color)

    def move_directions(self):
        pass

    def symbol(self):
        return " P "
