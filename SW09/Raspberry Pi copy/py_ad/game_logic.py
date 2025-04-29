from game_state import GameState
from game_token import GameToken
from drop_state import DropState
from game_logic_base import GameLogicBase
from display_sensehat import DisplaySenseHat
import time


class GameLogicSenseHat(GameLogicBase):
    # Standard Connect4 dimensions
    ROWS = 6
    COLS = 7

    def __init__(self):
        self._board = [[' ' for _ in range(self.COLS)] for _ in range(self.ROWS)]
        self._state = GameState.TURN_RED
        self._display = DisplaySenseHat()

    def _check_winner(self, player: GameToken) -> bool:
        # Horizontal check
        for r in range(self.ROWS):
            for c in range(self.COLS - 3):
                if (self._board[r][c] == player and 
                    self._board[r][c+1] == player and 
                    self._board[r][c+2] == player and 
                    self._board[r][c+3] == player):
                    return True

        # Vertical check
        for c in range(self.COLS):
            for r in range(self.ROWS - 3):
                if (self._board[r][c] == player and 
                    self._board[r+1][c] == player and 
                    self._board[r+2][c] == player and 
                    self._board[r+3][c] == player):
                    return True

        # Positive diagonal check
        for r in range(self.ROWS - 3):
            for c in range(self.COLS - 3):
                if (self._board[r][c] == player and 
                    self._board[r+1][c+1] == player and 
                    self._board[r+2][c+2] == player and 
                    self._board[r+3][c+3] == player):
                    return True

        # Negative diagonal check
        for r in range(3, self.ROWS):
            for c in range(self.COLS - 3):
                if (self._board[r][c] == player and 
                    self._board[r-1][c+1] == player and 
                    self._board[r-2][c+2] == player and 
                    self._board[r-3][c+3] == player):
                    return True

        return False

    def _check_draw(self) -> bool:
        return all(self._board[self.ROWS-1][c] != ' ' for c in range(self.COLS))

    def drop_token(self, player: GameToken, column: int) -> DropState:
        if column < 0 or column >= self.COLS:
            return DropState.COLUMN_INVALID
        
        # Find the lowest empty row
        row = 5
        for r in range(self.ROWS):
            if self._board[r][column] == ' ':
                row = r
            else:
                r -= 1
                break
        
        if r == -1:
            return DropState.COLUMN_FULL

        # Animate token drop
        # Note: In SenseHAT display, game board starts at row 2 (0-based)
        for y in range(row + 1):
            self._display.draw_grid()  # Draw the game grid
            
            # Draw existing tokens (offset by 2 rows for SenseHAT display)
            for r in range(self.ROWS):
                for c in range(self.COLS):
                    if self._board[r][c] != ' ':
                        self._display.draw_token(c, r + 2, self._board[r][c])
            
            # Draw falling token (offset by 2 rows)
            self._display.draw_token(column, y + 2, player)
            time.sleep(0.1)

        # board state
        self._board[row][column] = player

        if self._check_winner(GameToken.RED):
            self._state = GameState.WON_RED
        elif self._check_winner(GameToken.YELLOW):
            self._state = GameState.WON_YELLOW
        elif self._check_draw():
            self._state = GameState.DRAW
        else:
            self._state = GameState.TURN_YELLOW if self._state == GameState.TURN_RED else GameState.TURN_RED

        return DropState.DROP_OK

    def get_board(self) -> list:
        return self._board

    def get_state(self) -> GameState:
        return self._state
