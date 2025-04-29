from game_state import GameState
from game_token import GameToken
from drop_state import DropState
from display_sensehat import DisplaySenseHat
import time


class GameLogicBase:
    """
        GameLogicBase provides basic methods for interacting with the game's logic.
    """

    def __init__(self):
        # print("GameLogicBase initialized")
        pass

    def get_board(self) -> list:
        """
        Returns the board as a list of lists. The board positions are displayed as a string. They can contain one of 3 values:
        - 'X' or '0': the game position is occupied by player 'X' or '0', respectively
        - ' ': the game position is still unoccupied
        """
        return self._board

    def get_state(self) -> GameState:
        raise NotImplementedError("")

    def drop_token(self, player: GameToken, column: int) -> DropState:
        """
        The current player (identified by either 'X' or 'Y') makes their move by dropping their token into the specified column. 
        Parameters:
        - player: The token representing the player (i.e., RED or YELLOW).
        - column: The column (0..6) into which to drop the token.
        Returns:
        DropState: The state of the drop (e.g., okay, invalid position, column full).

        """
        if column < 0 or column >= self.COLS:
            return DropState.COLUMN_INVALID
        
        # Find the lowest empty row
        row = -1
        for r in range(self.ROWS):
            if self._board[r][column] == GameToken.EMPTY:
                row = r
                break
        
        if row == -1:
            return DropState.COLUMN_FULL

        # Animate the drop
        display = DisplaySenseHat()  # You might want to pass this as a parameter instead
        for y in range(row + 1):
            if y > 0:
                display.draw_token(column, y-1, GameToken.EMPTY)  # Clear previous position
            display.draw_token(column, y, player)  # Draw current position
            time.sleep(0.1)  # Add a small delay for animation
        
        self._board[row][column] = player
        return DropState.OK

        raise NotImplementedError("You need to subclass GameLogicBase to use move().")
