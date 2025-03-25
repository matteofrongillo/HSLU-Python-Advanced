from display_base import DisplayBase  # base class for output methods
from input_console import InputConsole
from player_base import PlayerBase
from game_state import GameState
from game_token import GameToken
from ansi import Ansi


class PlayerConsole(PlayerBase):
    def __init__(self, player: GameToken):  # Red or Yellow player
        super().__init__(player)

        # YOUR CODE HERE
        # self._display = DisplayConsole() # use this class for console output
        self._input = InputConsole() # use this class for console input

    def play_turn(self) -> int:
        # YOUR CODE HERE
        # TODO: return desired column from user input (0..6) using
        # use self._input to read keys, use self._output to draw current token position
        pass

    def draw_board(self, board: list, state: GameState):
        # YOUR CODE HERE
        # TODO: draw grid with tokens using self._display
        pass


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
