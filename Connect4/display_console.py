from ansi import Ansi
from game_token import GameToken
from display_base import DisplayBase


class DisplayConsole(DisplayBase):
    def __init__(self):
        Ansi.clear_screen()

    def draw_token(self, x: int, y: int, token: GameToken = GameToken.EMPTY) -> None:
        # YOUR CODE HERE
        Ansi.gotoXY(1, 20)
        pass

    def draw_grid(self) -> None:
        # YOUR CODE HERE
        Ansi.reset()
        print("┌"+(("─")*4+"┬")*6+("─")*4+"┐")
        for _ in range(5):
            print("│"+((" ")*4+"│")*6+(" ")*4+"│")
            print("├"+(("─")*4+"┼")*6+("─")*4+"┤")
        print("│"+((" ")*4+"│")*6+(" ")*4+"│")
        print("└"+(("─")*4+"┴")*6+("─")*4+"┘")

        Ansi.reset()
        print(
"""
┌
┐
└
┘
├
┤
┼
─
│
┬
┴
█ 

https://de.wikipedia.org/wiki/Unicodeblock_Rahmenzeichnung
""")

if __name__ == '__main__':
    Ansi.clear_screen()
    Ansi.reset()
    fc = DisplayConsole()
    fc.draw_grid()
    fc.draw_token(0, 0, GameToken.RED)
    fc.draw_token(5, 2, GameToken.YELLOW)
    print(type(GameToken.RED))
    print(GameToken.RED)
