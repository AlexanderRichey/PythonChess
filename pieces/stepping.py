from piece import Piece

class SteppingPiece(Piece):
    def __init__(self, board, pos, color):
        Piece.__init__(self, board, pos, color)
