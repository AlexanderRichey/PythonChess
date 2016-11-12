from board import Board
from display import Display
from players.human_player import HumanPlayer
from game import Game

board = Board()
display = Display(board)
player_one = HumanPlayer(board, "White")
player_two = HumanPlayer(board, "Black")
new_game = Game(board, display, player_one, player_two)
new_game.play()
