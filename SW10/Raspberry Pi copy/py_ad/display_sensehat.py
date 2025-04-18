from sense_hat import SenseHat
from display_base import DisplayBase
from game_token import GameToken

class DisplaySenseHat(DisplayBase):
    def __init__(self):
        self.sense = SenseHat()
        self.sense.set_rotation(180)
        self.sense.clear()
        self.RED = (255, 0, 0)
        self.YELLOW = (255, 255, 0)
        self.EMPTY = (0, 0, 0)
        self.GRID = (48, 48, 48)  # Blue color for grid

    def draw_grid(self) -> None:
        # Draw the game grid background
        pixels = []
        for y in range(8):
            for x in range(8):
                if y < 2 or x > 6:  # Top rows for dropping tokens
                    pixels.append(self.EMPTY)
                else:
                    pixels.append(self.GRID)
        self.sense.set_pixels(pixels)

    def draw_token(self, x: int, y: int, token: GameToken) -> None:
        if x < 0 or x >= 7 or y < -1 or y >= 6:
            return
            
        # Adjust y position to account for top 2 rows
        display_y = y + 2 if y >= 0 else y + 2
        
        color = {
            GameToken.RED: self.RED,
            GameToken.YELLOW: self.YELLOW,
            GameToken.EMPTY: self.EMPTY
        }.get(token, self.EMPTY)
        
        self.sense.set_pixel(x, display_y, color)

if __name__ == "__main__":
    display = DisplaySenseHat()
    display.draw_grid()
    # Example of drawing tokens
    display.draw_token(3, 5, GameToken.RED)
    display.draw_token(4, 5, GameToken.YELLOW)
    display.draw_token(2, -1, GameToken.RED)  # Example of dropping token
