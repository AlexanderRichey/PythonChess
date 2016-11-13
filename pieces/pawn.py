# This Python file uses the following encoding: utf-8
import os
import sys

from piece import Piece


class Pawn(Piece):
    def __init__(self, board, pos, color, direction):
        Piece.__init__(self, board, pos, color)
        self.direction = direction
        self.original_position = pos

    def symbol(self):
        if self.color == "White":
            return u" ♙ "
        else:
            return u" ♟ "

    def move_directions(self):
        move_directions = [[self.direction,  0],
                           [self.direction, -1],
                           [self.direction,  1]]
        if self.pos == self.original_position:
            move_directions.append([(self.direction * 2), 0])
        return move_directions

    def possible_moves(self):
        possible_moves = set()
        for direction in self.move_directions():
            start_pos = self.pos
            end_pos = [start_pos[0] + direction[0],
                       start_pos[1] + direction[1]]
            if self.is_valid_pawn_move(start_pos, end_pos):
                possible_moves.add(tuple(end_pos))
        return possible_moves

    def is_valid_pawn_move(self, start_pos, end_pos):
        if self.is_valid(start_pos, end_pos):
            if self.is_pawn_capture(start_pos, end_pos):
                return self.board.is_capture(self.to_tile(start_pos),
                                             self.to_tile(end_pos))
            elif self.is_en_passant(start_pos, end_pos):
                return self.is_valid_en_passant(start_pos)
            else:
                return not self.board.is_capture(self.to_tile(start_pos),
                                                 self.to_tile(end_pos))
        else:
            return False

    def is_pawn_capture(self, start_pos, end_pos):
        return abs(start_pos[0] - end_pos[0]) == 1 and \
               abs(start_pos[1] - end_pos[1]) == 1

    def is_en_passant(self, start_pos, end_pos):
        return abs(start_pos[0] - end_pos[0]) == 2

    def is_valid_en_passant(self, start_pos):
        return self.board.is_empty(self.to_tile([start_pos[0] + self.direction,
                                                start_pos[1]]))
