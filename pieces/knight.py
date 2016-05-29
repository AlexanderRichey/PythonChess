# This Python file uses the following encoding: utf-8
import os, sys

from stepping import SteppingPiece

class Knight(SteppingPiece):
    def __init__(self, board, pos, color):
        SteppingPiece.__init__(self, board, pos, color)

    def move_directions(self):
        return [[-1, 2],
                [1, 2],
                [1, -2],
                [-1, -2],
                [-2, -1],
                [2, 1],
                [-2, 1],
                [2, -1]]

    def symbol(self):
        if self.color == "White":
            return u" ♘ "
        else:
            return u" ♞ "
