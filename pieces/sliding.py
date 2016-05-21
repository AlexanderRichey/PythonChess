from piece import Piece

class SlidingPiece(Piece):
    def __init__(self, board, pos, color):
        Piece.__init__(self, board, pos, color)
