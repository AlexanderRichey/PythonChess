import board
import display
from players.human_player import HumanPlayer
import game

board = board.Board()
display = display.Display(board)
player_one = HumanPlayer(board, "White")
player_two = HumanPlayer(board, "Black")
new_game = game.Game(board, display, player_one, player_two)
new_game.play()
