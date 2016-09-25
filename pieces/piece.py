class Piece:
    def __init__(self, board, pos, color):
        self.board = board
        self.pos = pos
        self.color = color

    def is_valid(self, start_pos, end_pos):
        return self.board.is_in_bounds(end_pos) and \
               not self.board.is_capture_own_color(self.to_tile(start_pos),
                                                   self.to_tile(end_pos))

    def to_tile(self, pos):
        return self.board.grid[pos[0]][pos[1]]
