from player_sensehat import PlayerSenseHat
from game_token import GameToken
from game_logic import GameLogicSenseHat
from game_state import GameState
from drop_state import DropState
from sense_hat import SenseHat
import time

class Coordinator:
    def __init__(self):
        self.sense = SenseHat()
        self.sense.set_rotation(180)
        # Initialize players with SenseHat display
        self._player_red = PlayerSenseHat(GameToken.RED)
        self._player_yellow = PlayerSenseHat(GameToken.YELLOW)
        self._game = GameLogicSenseHat()

    def show_game_message(self, message: str, color=(255, 255, 0)):
        self.sense.show_message(message, text_colour=color, scroll_speed=0.0375)

    def run(self):
        self.show_game_message("Connect 4", (0, 255, 0))
        
        while True:
            state = self._game.get_state()
            
            if state in [GameState.WON_RED, GameState.WON_YELLOW, GameState.DRAW]:
                if state == GameState.WON_RED:
                    self.show_game_message("Red Wins!", (255, 0, 0))
                elif state == GameState.WON_YELLOW:
                    self.show_game_message("Yellow Wins!", (255, 255, 0))
                else:
                    self.show_game_message("Draw!", (0, 255, 255))
                break
            
            current_player = self._player_red if state == GameState.TURN_RED else self._player_yellow
            current_token = GameToken.RED if state == GameState.TURN_RED else GameToken.YELLOW
            
            try:
                current_player.draw_board(self._game.get_board(), state)
                column = current_player.play_turn()
                drop_result = self._game.drop_token(current_token, column)
                
                if drop_result != DropState.DROP_OK:
                    continue
                    
            except KeyboardInterrupt:
                self.show_game_message("Game Over")
                self.sense.clear()
                break

if __name__ == '__main__':
    coordinator = Coordinator()
    try:
        coordinator.run()
    finally:
        coordinator.sense.clear()
