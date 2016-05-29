class HumanPlayer:
    def __init__(self, board, color):
        self.board = board
        self.color = color

    def take_turn(self):
        while True:
            print "\n..." + self.color + " Player's Turn..."
            start_pos = self.get_input("Start Position >> ")
            end_pos = self.get_input("End Position   >> ")
            try:
                self.validate_color(start_pos, end_pos)
                self.board.make_move(start_pos, end_pos)
                break
            except Exception as e:
                print "Invalid Move"
                print e #for debugging

    def parse_input(self, pos):
        return [(8 - int(pos[1])), self.parse_letter(pos[0].lower())]

    def parse_letter(arg, letter):
        return ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'].index(letter)

    def get_input(self, instruction):
        while True:
            try:
                return self.parse_input(raw_input(instruction))
            except:
                print "Invalid Input"

    def validate_color(self, start_pos, end_pos):
        if self.board.grid[start_pos[0]][start_pos[1]].color != self.color:
            raise Exception