class HumanPlayer:
    def __init__(self, board, color):
        self.board = board
        self.color = color

    def take_turn(self):
        start_pos = self.get_input("Start Position >> ")
        end_pos = self.get_input("End Position >> ")
        self.board.make_move(start_pos, end_pos)

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
