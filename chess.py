import board
import display
import game

board = board.Board()
display = display.Display(board)
new_game = game.Game(board, display)
new_game.play()
