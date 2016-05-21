from pieces.king import King
from pieces.queen import Queen
from pieces.rook import Rook
from pieces.bishop import Bishop
from pieces.knight import Knight
from pieces.pawn import Pawn

class Board:
    def __init__(self):
        self.grid = [([None] * 8) for i in range (8)]

    def populate(self):
        self.grid[7][0] = King(self, [0, 0], "White")
        self.grid[6][1] = Queen(self, [0, 0], "White")
