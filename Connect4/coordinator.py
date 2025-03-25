
from player_console import PlayerConsoleSimple
from player_console import PlayerConsole
from game_token import GameToken
from game_logic import GameLogic
from game_logic_base import GameLogicBase
from game_state import GameState
from drop_state import DropState
import time, sys

from util import Util 
if Util.isRaspberry():
    pass

class Coordinator:
    def __init__(self):
        # YOUR CODE HERE
        # for a local game
        # - create 2 Player objects
        # - create a GameLogic object as self._game
        pass

    def run(self):

        # play game until won or draw
        while (True):

            # YOUR CODE HERE
            # forever
            # - get game state
            state = self._game.get_state()
            # - if game over: end game
            # - else: determine current_player
            # - current_player.draw_board(...)
            # - column = current_player.play_turn()
            # - self._game.drop_token( player, column )
            # repeat



# start a local game
if __name__ == '__main__':

    print("Welcome to  Connect 4, starting game")

    coordinator = Coordinator()
    coordinator.run()
