from game_state import GameState
from game_token import GameToken
from drop_state import DropState
from game_logic_base import GameLogicBase
from display_console import DisplayConsole
import time


class GameLogicLocal(GameLogicBase):
    ROWS = 6
    COLS = 7

    def __init__(self):
        # Initialize the game board with empty spaces
        self._board = [[' ' for _ in range(self.COLS)] for _ in range(self.ROWS)]
        # Initialize the game state to RED's turn
        self._state = GameState.TURN_RED

    def _check_winner(self, player: GameToken) -> bool:
        for r in range(self.ROWS):
            for c in range(self.COLS - 3):
                if (self._board[r][c] == player and 
                    self._board[r][c+1] == player and 
                    self._board[r][c+2] == player and 
                    self._board[r][c+3] == player):
                    return True

        # vertical check
        for c in range(self.COLS):
            for r in range(self.ROWS - 3):
                if (self._board[r][c] == player and 
                    self._board[r+1][c] == player and 
                    self._board[r+2][c] == player and 
                    self._board[r+3][c] == player):
                    return True

        # positive diagonal check
        for r in range(self.ROWS - 3):
            for c in range(self.COLS - 3):
                if (self._board[r][c] == player and 
                    self._board[r+1][c+1] == player and 
                    self._board[r+2][c+2] == player and 
                    self._board[r+3][c+3] == player):
                    return True

        # negative diagonal check
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

    def get_board(self) -> list:
        return self._board

    def get_state(self) -> GameState:
        return self._state

    def drop_token(self, player: GameToken, column: int) -> DropState:
        if column < 0 or column >= self.COLS:
            return DropState.COLUMN_INVALID
        
        # checks the lowest empty row in column
        row = 5
        for r in range(self.ROWS):
            if self._board[r][column] == ' ':
                row = r
            else:
                r -= 1
                break
        
        if r == -1:
            return DropState.COLUMN_FULL

        # drop animation
        display = DisplayConsole()
        for y in range(row + 1):
            display.draw_grid()  # redraws the grid background
            # redraws dropped tokens
            for r in range(self.ROWS):
                for c in range(self.COLS):
                    token = self._board[r][c]
                    if token != ' ':
                        display.draw_token(c, r, token)
            # board with new token
            display.draw_token(column, y, player)
            time.sleep(0.075)

        # token in last row
        self._board[row][column] = player
            
        if self._check_winner(GameToken.RED):
            self._state = GameState.WON_RED
        elif self._check_winner(GameToken.YELLOW):
            self._state = GameState.WON_YELLOW
        elif self._check_draw():
            self._state = GameState.DRAW
        else:
            # switches turns only if game hasn't ended
            self._state = GameState.TURN_YELLOW if self._state == GameState.TURN_RED else GameState.TURN_RED

        return DropState.DROP_OK

