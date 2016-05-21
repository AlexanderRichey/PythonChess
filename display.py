class Display:
    def __init__(self, board):
        self.board = board

    def decoder(*arg):
        if arg[1] == None:
            return " . "
        else:
            return arg[1].symbol()

    def render(self):
        for row in self.board.grid:
            print str().join(map(self.decoder, row))
