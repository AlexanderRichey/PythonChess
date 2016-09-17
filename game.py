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
        while not self.board.is_checkmate():
            print self.board.possible_moves_for(self.current_player.color)
            self.display.render()
            self._render_check()
            self.current_player.take_turn()
            self.switch_players()

    def _render_check(self):
        if self.board.is_check_for(self.current_player.color):
            print self.current_player.color + " is in check"
