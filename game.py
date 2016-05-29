class Game:
    def __init__(self, board, display, player_one, player_two):
        self.board = board
        self.display = display
        self.player_one = player_one
        self.player_two = player_two
        self.current_player = self.player_one

    def switch_players(self):
        if self.current_player == self.player_one:
            self.current_player = self.player_two
        else:
            self.current_player = self.player_one

    def play(self):
        self.board.populate()
        while True:
            self.display.render()
            self.current_player.take_turn()
            self.switch_players()
