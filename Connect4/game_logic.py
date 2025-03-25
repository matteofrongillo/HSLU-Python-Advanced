from game_state import GameState
from game_token import GameToken
from drop_state import DropState
from game_logic_base import GameLogicBase


class GameLogicLocal(GameLogicBase):
    ROWS = 6
    COLS = 7

    def __init__(self):
        pass

    def get_board(self) -> list:
        return None

    def get_state(self) -> GameState:
        return GameState.TURN_RED

    def drop_token(self, player: GameToken, column: int) -> DropState:
        return DropState.COLUMN_INVALID
