from pieces.piece import Piece
from pieces.king import King
from pieces.queen import Queen
from pieces.rook import Rook
from pieces.bishop import Bishop
from pieces.knight import Knight
from pieces.pawn import Pawn

class Board:
    def __init__(self):
        self.grid = [([None] * 8) for i in range(8)]
        self.pieces = set()
        self.white_pieces = set()
        self.black_pieces = set()

    def make_move(self, start_pos, end_pos):
        start_tile_content = self.grid[start_pos[0]][start_pos[1]]
        if not self.is_legal(start_tile_content, end_pos): raise Exception
        self._move(start_pos, start_tile_content, end_pos)

    def all_pieces(self):
        self._ensure_pieces()
        return self.pieces

    def pieces_for(self, color):
        self._ensure_pieces()
        if color == "White":
            return self.white_pieces
        else:
            return self.black_pieces

    def possible_moves_for(self, color):
        return set(coord for sublist in
                tuple(piece.possible_moves() for piece in self.pieces_for(color))
                for coord in sublist)

    def is_check_for(self, color):
        return tuple(self._king_for(color).pos) in self.possible_moves_for(
                                                    self._opponent(color))

    def is_check(self):
        return self.is_check_for("White") or self.is_check_for("Black")

    def is_checkmate(self):
        return self.is_checkmate_for("White") or self.is_checkmate_for("Black")

    def is_checkmate_for(self, color):
        checkmate = True
        for piece in self.pieces_for(color):
            for end_pos in piece.possible_moves():
                end_tile_content = self.grid[end_pos[0]][end_pos[1]]
                if self.is_capture_own_color(piece, end_tile_content): continue
                start_pos = piece.pos
                self._move(start_pos, piece, end_pos)
                if not self.is_check_for(color): checkmate = False
                self._undo_move(start_pos, piece, end_pos, end_tile_content)
                if not checkmate: return False
        return True

    def is_legal(self, start_tile_content, end_pos):
        return end_pos in start_tile_content.possible_moves()

    def is_piece(self, tile_content):
        return isinstance(tile_content, Piece)

    def is_empty(self, tile_content):
        return tile_content == None

    def is_capture(self, start_tile, end_tile):
        return self.is_piece(start_tile) and \
               self.is_piece(end_tile) and \
               end_tile.color != start_tile.color

    def is_in_bounds(self, pos):
        for coord in pos:
            if coord not in range(8): return False
        return True

    def is_capture_own_color(self, start_tile, end_tile):
       return self.is_piece(end_tile) and end_tile.color == start_tile.color

    def populate(self):
        self._populate_major_and_minor(0, "Black")
        self._populate_pawns(1, "Black",  1)
        self._populate_pawns(6, "White", -1)
        self._populate_major_and_minor(7, "White")

    def _opponent(self, color):
        if color == "White":
            return "Black"
        else:
            return "White"

    def _move(self, start_pos, start_tile_content, end_pos):
        end_tile_content = self.grid[end_pos[0]][end_pos[1]]
        try:
            self.pieces.discard(end_tile_content)
            self.pieces_for(end_tile_content.color).discard(end_tile_content)
        except: pass
        self.grid[end_pos[0]][end_pos[1]] = start_tile_content
        start_tile_content.pos = end_pos
        self.grid[start_pos[0]][start_pos[1]] = None

    def _undo_move(self, start_pos, start_tile_content,
                   end_pos, end_tile_content):
        try:
            self.pieces.add(end_tile_content)
            self.pieces_for(end_tile_content.color).add(end_tile_content)
        except: pass
        self.grid[start_pos[0]][start_pos[1]] = start_tile_content
        start_tile_content.pos = start_pos
        self.grid[end_pos[0]][end_pos[1]] = end_tile_content

    def _get_all_pieces(self):
        for row in self.grid:
            for tile in row:
                if self.is_piece(tile): self._collect_piece(tile)

    def _collect_piece(self, piece):
        self.pieces.add(piece)
        if piece.color == "White":
            self.white_pieces.add(piece)
        else:
            self.black_pieces.add(piece)

    def _ensure_pieces(self):
        if not self.pieces: self._get_all_pieces()

    def _king_for(self, color):
        for piece in self.pieces_for(color):
            if isinstance(piece, King): return piece

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
