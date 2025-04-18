from sense_hat import SenseHat
import time

sense = SenseHat()
sense.set_rotation(180)

#text = input("Enter text to display: ")
#sense.show_message(text, text_colour=(64,64,64))

# for letter in "delia":
#     sense.show_letter(letter, text_colour=(64,64,64))
#     time.sleep(0.3)

X = (0,64,0)
O = (0,0,0)
creeper = [
    X, X, X, X, X, X, X, X,
    X, O, O, X, X, O, O, X,
    X, O, O, X, X, O, O, X,
    X, X, X, O, O, X, X, X,
    X, X, O, O, O, O, X, X,
    X, X, O, O, O, O, X, X,
    X, X, O, X, X, O, X, X,
    X, X, X, X, X, X, X, X
]

P = (64,0,64)
enderman = [
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    P, P, P, O, O, P, P, P,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O
]

H = (102,51,0)
S = (255,204,204)
W = (64,64,64)
B = (0,0,64)
N = (204,153,0)
steve = [
    H, H, H, H, H, H, H, H,
    H, H, H, H, H, H, H, H,
    H, S, S, S, S, S, S, H,
    S, S, S, S, S, S, S, S,
    S, W, B, S, S, B, W, S,
    S, S, S, N, N, S, S, S,
    S, S, H, S, S, H, S, S,
    S, S, H, H, H, H, S, S
]

R = (255,102,153)
pig = [
    R, R, R, R, R, R, R, R,
    R, R, R, R, R, R, R, R,
    R, R, R, R, R, R, R, R,
    O, W, R, R, R, R, W, O,
    R, R, R, R, R, R, R, R,
    R, R, O, R, R, O, R, R,
    R, R, R, R, R, R, R, R,
    R, R, R, R, R, R, R, R
]

minecraft_list = [creeper, enderman, steve, pig]

try:
    while True:
        for i in minecraft_list:
            sense.set_pixels(i)
            time.sleep(1)
except KeyboardInterrupt:
    sense.show_message("bye", text_colour=(64,64,64), scroll_speed=0.05)
    sense.clear()
