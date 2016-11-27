from piece import Piece


class PiecesStore:
    def __init__(self, grid):
        self.pieces = set()
        self.white_pieces = set()
        self.black_pieces = set()
        self.grid = grid

    def all_pieces(self):
        self._ensure_pieces()
        return self.pieces

    def pieces_for(self, color):
        self._ensure_pieces()
        if color == "White":
            return self.white_pieces
        else:
            return self.black_pieces

    def store_piece(self, end_tile_content):
        try:
            self.pieces.add(end_tile_content)
            self.pieces_for(end_tile_content.color).add(end_tile_content)
        except:
            pass

    def unstore_piece(self, end_tile_content):
        try:
            self.pieces.discard(end_tile_content)
            self.pieces_for(end_tile_content.color).discard(end_tile_content)
        except:
            pass

    def _get_all_pieces(self):
        for row in self.grid:
            for tile in row:
                if isinstance(tile, Piece):
                    self._collect_piece(tile)

    def _collect_piece(self, piece):
        self.pieces.add(piece)
        if piece.color == "White":
            self.white_pieces.add(piece)
        else:
            self.black_pieces.add(piece)

    def _ensure_pieces(self):
        if not self.pieces:
            self._get_all_pieces()
