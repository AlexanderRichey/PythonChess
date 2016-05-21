class Game:
    def __init__(self, board, display):
        self.board = board
        self.display = display

    def play(self):
        self.board.populate()
        print self.display.render()
