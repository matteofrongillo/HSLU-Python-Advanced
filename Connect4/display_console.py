from ansi import Ansi
from game_token import GameToken
from display_base import DisplayBase


class DisplayConsole(DisplayBase):
    def __init__(self):
        Ansi.clear_screen()

    def draw_token(self, x: int, y: int, token: GameToken = GameToken.EMPTY) -> None:
        row = 3 + (y * 2)  # y-position inside the grid

        col = 3 + (x * 5) # x-position inside the grid

        if x < 0 or x >= 7 or y < -1 or y >= 6:
            raise ValueError("Invalid position for token.")
        
        Ansi.gotoXY(col, row)
        
        if token == GameToken.RED:
            Ansi.set_foreground(1, True)
            token_str = "██"
        elif token == GameToken.YELLOW:
            Ansi.set_foreground(3, True)
            token_str = "██"
        else:
            token_str = "  "
        
        print(token_str, end="")
        Ansi.reset()

    def draw_grid(self) -> None:
        # YOUR CODE HERE
        Ansi.reset()
        Ansi.gotoXY(1, 2)

        print(f"┌────┬────┬────┬────┬────┬────┬────┐\n│    │    │    │    │    │    │    │\n├────┼────┼────┼────┼────┼────┼────┤\n│    │    │    │    │    │    │    │\n├────┼────┼────┼────┼────┼────┼────┤\n│    │    │    │    │    │    │    │\n├────┼────┼────┼────┼────┼────┼────┤\n│    │    │    │    │    │    │    │\n├────┼────┼────┼────┼────┼────┼────┤\n│    │    │    │    │    │    │    │\n├────┼────┼────┼────┼────┼────┼────┤\n│    │    │    │    │    │    │    │\n└────┴────┴────┴────┴────┴────┴────┘")


if __name__ == '__main__':
    Ansi.clear_screen()
    Ansi.reset()
    fc = DisplayConsole()
    fc.draw_grid()
    fc.draw_token(0, 0, GameToken.RED)
    fc.draw_token(5, 2, GameToken.YELLOW)
    #print(type(GameToken.RED))
    #print(GameToken.RED)
    Ansi.gotoXY(0,15)
