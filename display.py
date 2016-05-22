class Display:
    def __init__(self, board):
        self.board = board

    def decoder(*arg):
        if arg[1] == None:
            return " . "
        else:
            return arg[1].symbol()

    def build_board(self):
        for idx, row in enumerate(self.board.grid):
            print str(8 - idx) + str().join(map(self.decoder, row))

        print "  A  B  C  D  E  F  G  H "

    def render(self):
        print self.build_board()
