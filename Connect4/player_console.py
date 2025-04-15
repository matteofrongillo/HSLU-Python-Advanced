from display_base import DisplayBase  # base class for output methods
from input_console import InputConsole
from player_base import PlayerBase
from game_state import GameState
from game_token import GameToken
from ansi import Ansi
from display_console import DisplayConsole
from input_console import Keys

class PlayerConsole(PlayerBase):
    def __init__(self, player: GameToken):
        super().__init__(player)

        self._display = DisplayConsole()
        self._input = InputConsole()
        self._current_column = 0

    def play_turn(self) -> int:
        self._current_column = 0

        # draws token
        self._display.draw_token(self._current_column, -1, self._player)

        while True:
            key = self._input.read_key()
            
            if key == Keys.LEFT and self._current_column > 0:
                # clears position
                self._display.draw_token(self._current_column, -1, GameToken.EMPTY)
                self._current_column -= 1
                # draws at now position
                self._display.draw_token(self._current_column, -1, self._player)
            
            elif key == Keys.RIGHT and self._current_column < 6:
                # clears position
                self._display.draw_token(self._current_column, -1, GameToken.EMPTY)
                self._current_column += 1
                # draws at now position
                self._display.draw_token(self._current_column, -1, self._player)
            
            elif key == Keys.ENTER:
                # clears top token
                self._display.draw_token(self._current_column, -1, GameToken.EMPTY)
                return self._current_column
            
            # emergency exit
            elif key == Keys.ESC:
                raise KeyboardInterrupt()

    def draw_board(self, board: list, state: GameState):
        self._display.draw_grid() # draws the grid
        
        # draws tokens
        for y in range(6):
            for x in range(7):
                if board[y][x] != ' ':
                    self._display.draw_token(x, y, board[y][x])

if __name__ == '__main__':

    board = [[' ' for _ in range(7)] for _ in range(6)]
    board[5][0] = GameToken.RED  # [Y][X]
    p = PlayerConsole(GameToken.YELLOW)

    Ansi.clear_screen()
    Ansi.reset()
    p.draw_board(board, GameState.TURN_YELLOW)
    pos = p.play_turn()
    Ansi.reset()
    Ansi.gotoXY(1, 20)
    print(f"Position: {pos}")
