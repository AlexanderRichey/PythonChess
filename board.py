from pieces.king import King
from pieces.queen import Queen
from pieces.rook import Rook
from pieces.bishop import Bishop
from pieces.knight import Knight
from pieces.pawn import Pawn

class Board:
    def __init__(self):
        self.grid = [([None] * 8) for i in range (8)]

    def make_move(self, start_pos, end_pos):
        piece = self.grid[start_pos[0]][start_pos[1]]
        self.grid[end_pos[0]][end_pos[1]] = piece
        self.grid[start_pos[0]][start_pos[1]] = None

    def populate(self):
        self.populate_major_and_minor(0, "Black")
        self.populate_pawns(1, "Black")
        self.populate_pawns(6, "White")
        self.populate_major_and_minor(7, "White")

    def populate_pawns(self, row, color):
        for i in range (8):
            self.grid[row][i] = Pawn(self, [row, i], color)

    def populate_major_and_minor(self, row, color):
        self.grid[row][4] = King(self, [row, 4], color)
        self.grid[row][3] = Queen(self, [row, 3], color)
        self.grid[row][2] = Bishop(self, [row, 2], color)
        self.grid[row][5] = Bishop(self, [row, 5], color)
        self.grid[row][0] = Rook(self, [row,0], color)
        self.grid[row][7] = Rook(self, [row,7], color)
        self.grid[row][1] = Knight(self, [row, 1], color)
        self.grid[row][6] = Knight(self, [row, 6], color)
