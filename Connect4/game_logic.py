from game_state import GameState
from game_token import GameToken
from drop_state import DropState
from game_logic_base import GameLogicBase


class GameLogicLocal(GameLogicBase):
    ROWS = 6
    COLS = 7

    def __init__(self):
        # Initialize the game board with empty spaces
        self._board = [[' ' for _ in range(self.COLS)] for _ in range(self.ROWS)]
        # Initialize the game state to RED's turn
        self._state = GameState.TURN_RED

    def get_board(self) -> list:
        return self._board

    def get_state(self) -> GameState:
        return self._state

    def drop_token(self, player: GameToken, column: int) -> DropState:
        if column < 0 or column >= self.COLS:
            return DropState.COLUMN_INVALID
        
        # Find the lowest empty row
        row = -1
        for r in range(self.ROWS):
            if self._board[r][column] == ' ':
                row = r
                break
        
        if row == -1:
            return DropState.COLUMN_FULL

        # Place the token
        self._board[row][column] = player
        
        # Switch turns
        self._state = GameState.TURN_YELLOW if self._state == GameState.TURN_RED else GameState.TURN_RED
        
        return DropState.DROP_OK
