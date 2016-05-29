from piece import Piece

class SteppingPiece(Piece):
    def __init__(self, board, pos, color):
        Piece.__init__(self, board, pos, color)

    def possible_moves(self):
        possible_moves = []

        for direction in self.move_directions():
            start_pos = self.pos
            end_pos = [start_pos[0] + direction[0],
                       start_pos[1] + direction[1]]
            if self.is_valid_and_is_in_bounds(start_pos, end_pos):
                possible_moves.append(end_pos)

        return possible_moves
