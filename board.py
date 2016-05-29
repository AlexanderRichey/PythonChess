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
        start_tile_content = self.grid[start_pos[0]][start_pos[1]]
        self.validate(start_tile_content, end_pos)
        self.move(start_pos, start_tile_content, end_pos)

    def validate(self, start_tile_content, end_pos):
        if not self.is_legal(start_tile_content, end_pos):
            raise Exception

    def is_legal(self, start_tile_content, end_pos):
        return end_pos in start_tile_content.possible_moves()

    def is_valid(self, start_tile_content, end_tile_content):
        if not self.is_piece(start_tile_content):
            return False
        elif self.is_capture_own_color(start_tile_content, end_tile_content):
            return False
        else:
            return True

    def is_piece(self, tile_content):
        return not self.is_empty(tile_content)

    def is_empty(self, tile_content):
        return tile_content == None

    def is_capture_own_color(self, start_tile, end_tile):
        return self.is_piece(end_tile) and end_tile.color == start_tile.color

    def is_capture(self, start_tile, end_tile):
        return self.is_piece(start_tile) and \
               self.is_piece(end_tile) and \
               end_tile.color != start_tile.color

    def is_in_bounds(self, pos):
        for coord in pos:
            if coord not in range(8):
                return False

        return True

    def move(self, start_pos, start_tile_content, end_pos):
        self.grid[end_pos[0]][end_pos[1]] = start_tile_content
        start_tile_content.pos = end_pos
        self.grid[start_pos[0]][start_pos[1]] = None

    def populate(self):
        self.populate_major_and_minor(0, "Black")
        self.populate_pawns(1, "Black",  1)
        self.populate_pawns(6, "White", -1)
        self.populate_major_and_minor(7, "White")

    def populate_pawns(self, row, color, direction):
        for i in range(8):
            self.grid[row][i] = Pawn(self, [row, i], color, direction)

    def populate_major_and_minor(self, row, color):
        self.grid[row][4] = King(self, [row, 4], color)
        self.grid[row][3] = Queen(self, [row, 3], color)
        self.grid[row][2] = Bishop(self, [row, 2], color)
        self.grid[row][5] = Bishop(self, [row, 5], color)
        self.grid[row][0] = Rook(self, [row,0], color)
        self.grid[row][7] = Rook(self, [row,7], color)
        self.grid[row][1] = Knight(self, [row, 1], color)
        self.grid[row][6] = Knight(self, [row, 6], color)
