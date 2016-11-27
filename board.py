from pieces.piece import Piece
from pieces.king import King
from pieces.queen import Queen
from pieces.rook import Rook
from pieces.bishop import Bishop
from pieces.knight import Knight
from pieces.pawn import Pawn
from pieces.pieces_store import PiecesStore


class Board:
    def __init__(self):
        self.grid = [([None] * 8) for i in range(8)]
        self.white_has_castled = False
        self.black_has_castled = False
        self.store = PiecesStore(self.grid)

    def make_move(self, start_pos, end_pos):
        start_tile_content = self.get_tile_content(start_pos)
        if not self.is_legal(start_tile_content, end_pos):
            raise Exception
        self._move(start_pos, start_tile_content, end_pos)

    def possible_moves_for(self, color):
        return set(coord for sublist in
                   tuple(piece.possible_moves() for piece in
                         self.store.pieces_for(color))
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
        for piece in self.store.pieces_for(color):
            for end_pos in piece.possible_moves():
                end_tile_content = self.get_tile_content(end_pos)
                if self.is_capture_own_color(piece, end_tile_content):
                    continue
                start_pos = piece.pos
                self._move(start_pos, piece, end_pos)
                if not self.is_check_for(color):
                    checkmate = False
                self._undo_move(start_pos, piece, end_pos, end_tile_content)
                if not checkmate:
                    return False
        return True

    def is_legal(self, start_tile_content, end_pos):
        return end_pos in start_tile_content.possible_moves()

    def is_piece(self, tile_content):
        return isinstance(tile_content, Piece)

    def is_empty(self, tile_content):
        return tile_content is None

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
        return self.is_piece(end_tile) and \
               self.is_piece(start_tile) and \
               end_tile.color == start_tile.color

    def populate(self):
        self._populate_major_and_minor(0, "Black")
        self._populate_pawns(1, "Black",  1)
        self._populate_pawns(6, "White", -1)
        self._populate_major_and_minor(7, "White")

    def can_castle(self, color):
        if color is "White":
            return self.white_can_castle()
        else:
            return self.black_can_castle()

    def white_can_castle(self):
        if isinstance(self.grid[7][0], Rook) \
                and isinstance(self.grid[7][4], King):
            return not self.grid[7][0].has_moved() \
                and not self.grid[7][4].has_moved() \
                and self.is_empty(self.grid[7][1]) \
                and self.is_empty(self.grid[7][2]) \
                and self.is_empty(self.grid[7][3])
        elif isinstance(self.grid[7][7], Rook) \
                and isinstance(self.grid[7][4], King):
            return not self.grid[7][7].has_moved() \
                and not self.grid[7][4].has_moved() \
                and self.is_empty(self.grid[7][5]) \
                and self.is_empty(self.grid[7][6])

    def black_can_castle(self):
        if isinstance(self.grid[0][0], Rook) \
                and isinstance(self.grid[0][4], King):
            return not self.grid[0][0].has_moved() \
                and not self.grid[0][4].has_moved() \
                and self.is_empty(self.grid[0][1]) \
                and self.is_empty(self.grid[0][2]) \
                and self.is_empty(self.grid[0][3])
        elif isinstance(self.grid[0][7], Rook) \
                and isinstance(self.grid[0][4], King):
            return not self.grid[0][7].has_moved() \
                and not self.grid[0][4].has_moved() \
                and self.is_empty(self.grid[0][5]) \
                and self.is_empty(self.grid[0][6])

    def get_tile_content(self, coord):
        return self.grid[coord[0]][coord[1]]

    def _set_tile_content(self, coord, content):
        self.grid[coord[0]][coord[1]] = content
        if isinstance(content, Piece):
            content.pos = coord

    def _opponent(self, color):
        if color == "White":
            return "Black"
        else:
            return "White"

    def _move(self, start_pos, start_tile_content, end_pos):
        end_tile_content = self.get_tile_content(end_pos)
        self.store.unstore_piece(end_tile_content)
        self._set_tile_content(end_pos, start_tile_content)
        start_tile_content.move_count += 1
        self._set_tile_content(start_pos, None)

    def _undo_move(self, start_pos, start_tile_content,
                   end_pos, end_tile_content):
        self._set_tile_content(start_pos, start_tile_content)
        self.store.store_piece(start_tile_content)
        start_tile_content.move_count -= 1
        self._set_tile_content(end_pos, end_tile_content)

    def _castle(self, color, direction):
        if color == "White":
            self._castle_white(direction)
        else:
            self._castle_black(direction)

    def _castle_white(self, direction):
        king = self.get_tile_content([7, 4])
        if direction == 'Queen':
            rook = self.get_tile_content([7, 0])
            self._set_tile_content([7, 3], rook)
            self._set_tile_content([7, 2], king)
        else:
            rook = self.get_tile_content([7, 7])
            self._set_tile_content([7, 5], rook)
            self._set_tile_content([7, 6], king)
        king.move_count += 1
        rook.move_count += 1
        self.white_has_castled = True

    def _castle_black(self, direction):
        king = self.get_tile_content([0, 4])
        if direction == 'Queen':
            rook = self.get_tile_content([0, 0])
            self._set_tile_content([0, 3], rook)
            self._set_tile_content([0, 2], king)
        else:
            rook = self.get_tile_content([0, 7])
            self._set_tile_content([0, 5], rook)
            self._set_tile_content([0, 6], king)
        king.move_count += 1
        rook.move_count += 1
        self.black_has_castled = True

    def _is_promotion(self):
        pass

    def _promote(self):
        pass

    def _king_for(self, color):
        for piece in self.store.pieces_for(color):
            if isinstance(piece, King):
                return piece

    def _populate_pawns(self, row, color, direction):
        for i in range(8):
            self.grid[row][i] = Pawn(self, [row, i], color, direction)

    def _populate_major_and_minor(self, row, color):
        self.grid[row][4] = King(self, [row, 4], color)
        self.grid[row][3] = Queen(self, [row, 3], color)
        self.grid[row][2] = Bishop(self, [row, 2], color)
        self.grid[row][5] = Bishop(self, [row, 5], color)
        self.grid[row][0] = Rook(self, [row, 0], color)
        self.grid[row][7] = Rook(self, [row, 7], color)
        self.grid[row][1] = Knight(self, [row, 1], color)
        self.grid[row][6] = Knight(self, [row, 6], color)
