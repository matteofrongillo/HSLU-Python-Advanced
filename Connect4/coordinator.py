
# from player_console import PlayerConsoleSimple
from player_console import PlayerConsole
from game_token import GameToken
from game_logic import GameLogicLocal
from game_logic_base import GameLogicBase
from game_state import GameState
from drop_state import DropState
import time, sys

from util import Util 
if Util.isRaspberry():
    pass

class Coordinator:
    def __init__(self):
        # red and yellow player
        self._player_red = PlayerConsole(GameToken.RED)
        self._player_yellow = PlayerConsole(GameToken.YELLOW)
        self._game = GameLogicLocal()

    def run(self): # plays game until won or draw
        while True:
            # checks the game state
            state = self._game.get_state()
            
            # checks if game is over
            if state in [GameState.WON_RED, GameState.WON_YELLOW, GameState.DRAW]:
                if state == GameState.WON_RED:
                    print("Red is the winner")
                elif state == GameState.WON_YELLOW:
                    print("Yellow is the winner")
                else:
                    print("Draw")
                break
            
            # determines which player is playing
            current_player = self._player_red if state == GameState.TURN_RED else self._player_yellow
            current_token = GameToken.RED if state == GameState.TURN_RED else GameToken.YELLOW
            
            # board
            current_player.draw_board(self._game.get_board(), state)
            
            # moves player
            try:
                column = current_player.play_turn()
                # drops token
                drop_result = self._game.drop_token(current_token, column)
                if drop_result != DropState.DROP_OK:
                    print(f"Invalid move: {drop_result}")
            except KeyboardInterrupt:
                print("\nGame interrupted by player")
                break

# start a local game
if __name__ == '__main__':

    print("Welcome to Connect 4, starting game")

    coordinator = Coordinator()
    coordinator.run()
