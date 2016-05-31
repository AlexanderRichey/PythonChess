from pieces.king import King
from pieces.queen import Queen
from pieces.rook import Rook
from pieces.bishop import Bishop
from pieces.knight import Knight
from pieces.pawn import Pawn

class Board:
    def __init__(self):
        self.grid = [([None] * 8) for i in range(8)]
        self.pieces = []
        self.white_pieces = []
        self.black_pieces = []

    def make_move(self, start_pos, end_pos):
        start_tile_content = self.grid[start_pos[0]][start_pos[1]]
        self._validate(start_tile_content, end_pos)
        self._move(start_pos, start_tile_content, end_pos)

    def all_pieces(self):
        self._ensure_pieces()
        return self.pieces

    def _get_all_pieces(self):
        for tile in self.grid:
            if self.is_piece(tile): self._collect_piece(tile)

    def _collect_piece(self, piece):
        self.pieces.append(piece)
        if piece.color == "White":
            self.white_pieces.append(piece)
        else:
            self.black_pieces.append(piece)

    def _ensure_pieces(self):
        if not self.pieces: self._get_all_pieces()

    def pieces_for(self, color):
        self._ensure_pieces()
        if color == "White":
            return self.white_pieces
        else:
            return self.black_pieces

    def possible_moves_for(self, color):
        possible_moves = []
        for piece in self.pieces_for(color):
            possible_moves.extend(piece.possible_moves())

        return possible_moves

    def is_check(self, color):
        pass

    def is_check_for(self, color):
        pass

    def is_checkmate(self):
        pass

    def _validate(self, start_tile_content, end_pos):
        if not self.is_legal(start_tile_content, end_pos):
            raise Exception

    def _move(self, start_pos, start_tile_content, end_pos):
        self.grid[end_pos[0]][end_pos[1]] = start_tile_content
        start_tile_content.pos = end_pos
        self.grid[start_pos[0]][start_pos[1]] = None

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

    def is_capture(self, start_tile, end_tile):
        return self.is_piece(start_tile) and \
               self.is_piece(end_tile) and \
               end_tile.color != start_tile.color

    def is_in_bounds(self, pos):
        for coord in pos:
            if coord not in range(8):
                return False

        return True

    def is_capture_own_color(self, start_tile, end_tile):
       return self.is_piece(end_tile) and end_tile.color == start_tile.color

    def populate(self):
        self._populate_major_and_minor(0, "Black")
        self._populate_pawns(1, "Black",  1)
        self._populate_pawns(6, "White", -1)
        self._populate_major_and_minor(7, "White")

    def _populate_pawns(self, row, color, direction):
        for i in range(8):
            self.grid[row][i] = Pawn(self, [row, i], color, direction)

    def _populate_major_and_minor(self, row, color):
        self.grid[row][4] = King(self, [row, 4], color)
        self.grid[row][3] = Queen(self, [row, 3], color)
        self.grid[row][2] = Bishop(self, [row, 2], color)
        self.grid[row][5] = Bishop(self, [row, 5], color)
        self.grid[row][0] = Rook(self, [row,0], color)
        self.grid[row][7] = Rook(self, [row,7], color)
        self.grid[row][1] = Knight(self, [row, 1], color)
        self.grid[row][6] = Knight(self, [row, 6], color)
