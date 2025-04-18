from display_base import DisplayBase
from input_sensehat import InputSenseHat, Keys
from player_base import PlayerBase
from game_state import GameState
from game_token import GameToken
from display_sensehat import DisplaySenseHat
from ansi import Ansi

class PlayerSenseHat(PlayerBase):  # Renamed from PlayerConsole
    def __init__(self, player: GameToken):
        super().__init__(player)
        self._display = DisplaySenseHat()
        self._input = InputSenseHat()
        self._current_column = 0

    def play_turn(self) -> int:
        self._current_column = 0
        self._display.draw_token(self._current_column, -1, self._player)

        while True:
            key = self._input.read_key()
            
            if key == Keys.RIGHT and self._current_column > 0:
                self._display.draw_token(self._current_column, -1, GameToken.EMPTY)
                self._current_column -= 1
                self._display.draw_token(self._current_column, -1, self._player)
            
            elif key == Keys.LEFT and self._current_column < 6:
                self._display.draw_token(self._current_column, -1, GameToken.EMPTY)
                self._current_column += 1
                self._display.draw_token(self._current_column, -1, self._player)
            
            elif key == Keys.SELECT:  # Changed from ENTER
                self._display.draw_token(self._current_column, -1, GameToken.EMPTY)
                return self._current_column

    def draw_board(self, board: list, state: GameState):
        self._display.draw_grid()
        for y in range(6):
            for x in range(7):
                if board[y][x] != ' ':
                    self._display.draw_token(x, y, board[y][x])

if __name__ == '__main__':

    board = [[' ' for _ in range(7)] for _ in range(6)]
    board[5][0] = GameToken.RED  # [Y][X]
    p = PlayerSenseHat(GameToken.YELLOW)

    Ansi.clear_screen()
    Ansi.reset()
    p.draw_board(board, GameState.TURN_YELLOW)
    pos = p.play_turn()
    Ansi.reset()
    Ansi.gotoXY(1, 20)
    print(f"Position: {pos}")
