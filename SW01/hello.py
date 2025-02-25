import tkinter as tk
from tkinter import messagebox
import random
import math

# -------------------------------
# Game Constants and Global Variables
# -------------------------------
ROW_COUNT = 6
COLUMN_COUNT = 7
PLAYER = 1      # Human coin (red)
AI = 2          # Computer coin (blue)
EMPTY = 0

CELL_SIZE = 100   # Size of each board cell (in pixels)
MARGIN = 8        # Margin inside each cell

# Game state globals
board = None
game_over = False
turn = None       # 0 = human, 1 = computer
difficulty = None # "easy", "normal", "hard"
animating = False # Flag to prevent moves during animation

# -------------------------------
# Game Logic Functions
# -------------------------------
def create_board():
    """Create and return an empty board."""
    return [[EMPTY for _ in range(COLUMN_COUNT)] for _ in range(ROW_COUNT)]

def is_valid_location(board, col):
    """Return True if the top cell in the given column is empty."""
    return board[ROW_COUNT - 1][col] == EMPTY

def get_valid_locations(board):
    """Return a list of column indices that are not full."""
    return [col for col in range(COLUMN_COUNT) if is_valid_location(board, col)]

def get_next_open_row(board, col):
    """Return the lowest available row index in the given column."""
    for r in range(ROW_COUNT):
        if board[r][col] == EMPTY:
            return r

def drop_piece(board, row, col, piece):
    """Place a piece (PLAYER or AI) into the board at the given row and column."""
    board[row][col] = piece

def winning_move(board, piece):
    """Return True if the given piece has four connected in a row."""
    # Horizontal check
    for r in range(ROW_COUNT):
        for c in range(COLUMN_COUNT - 3):
            if board[r][c] == piece and board[r][c+1] == piece and \
               board[r][c+2] == piece and board[r][c+3] == piece:
                return True

    # Vertical check
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r+1][c] == piece and \
               board[r+2][c] == piece and board[r+3][c] == piece:
                return True

    # Positive diagonal check
    for r in range(ROW_COUNT - 3):
        for c in range(COLUMN_COUNT - 3):
            if board[r][c] == piece and board[r+1][c+1] == piece and \
               board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True

    # Negative diagonal check
    for r in range(3, ROW_COUNT):
        for c in range(COLUMN_COUNT - 3):
            if board[r][c] == piece and board[r-1][c+1] == piece and \
               board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True

    return False

def is_terminal_node(board):
    """Return True if the game is over (win or draw)."""
    return winning_move(board, PLAYER) or winning_move(board, AI) or len(get_valid_locations(board)) == 0

def evaluate_window(window, piece):
    """Score a list of 4 cells (a window) for the given piece."""
    score = 0
    opp_piece = PLAYER if piece == AI else AI

    if window.count(piece) == 4:
        score += 100
    elif window.count(piece) == 3 and window.count(EMPTY) == 1:
        score += 5
    elif window.count(piece) == 2 and window.count(EMPTY) == 2:
        score += 2

    if window.count(opp_piece) == 3 and window.count(EMPTY) == 1:
        score -= 4

    return score

def score_position(board, piece):
    """Evaluate the board and return a score from the perspective of the given piece."""
    score = 0

    # Score center column
    center_col = COLUMN_COUNT // 2
    center_array = [board[r][center_col] for r in range(ROW_COUNT)]
    score += center_array.count(piece) * 3

    # Score horizontal windows
    for r in range(ROW_COUNT):
        row_array = board[r]
        for c in range(COLUMN_COUNT - 3):
            window = row_array[c:c+4]
            score += evaluate_window(window, piece)

    # Score vertical windows
    for c in range(COLUMN_COUNT):
        col_array = [board[r][c] for r in range(ROW_COUNT)]
        for r in range(ROW_COUNT - 3):
            window = col_array[r:r+4]
            score += evaluate_window(window, piece)

    # Score positive sloped diagonals
    for r in range(ROW_COUNT - 3):
        for c in range(COLUMN_COUNT - 3):
            window = [board[r+i][c+i] for i in range(4)]
            score += evaluate_window(window, piece)

    # Score negative sloped diagonals
    for r in range(3, ROW_COUNT):
        for c in range(COLUMN_COUNT - 3):
            window = [board[r-i][c+i] for i in range(4)]
            score += evaluate_window(window, piece)

    return score

def minimax(board, depth, alpha, beta, maximizingPlayer):
    """
    Use minimax with alpha-beta pruning to evaluate the best move.
    Returns a tuple (best_column, score).
    """
    valid_locations = get_valid_locations(board)
    terminal = is_terminal_node(board)
    if depth == 0 or terminal:
        if terminal:
            if winning_move(board, AI):
                return (None, 100000000000000)
            elif winning_move(board, PLAYER):
                return (None, -100000000000000)
            else:
                return (None, 0)
        else:
            return (None, score_position(board, AI))

    if maximizingPlayer:
        value = -math.inf
        best_col = random.choice(valid_locations)
        for col in valid_locations:
            row = get_next_open_row(board, col)
            board_copy = [r.copy() for r in board]
            drop_piece(board_copy, row, col, AI)
            new_score = minimax(board_copy, depth - 1, alpha, beta, False)[1]
            if new_score > value:
                value = new_score
                best_col = col
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return best_col, value
    else:
        value = math.inf
        best_col = random.choice(valid_locations)
        for col in valid_locations:
            row = get_next_open_row(board, col)
            board_copy = [r.copy() for r in board]
            drop_piece(board_copy, row, col, PLAYER)
            new_score = minimax(board_copy, depth - 1, alpha, beta, True)[1]
            if new_score < value:
                value = new_score
                best_col = col
            beta = min(beta, value)
            if alpha >= beta:
                break
        return best_col, value

# -------------------------------
# GUI and Animation Functions
# -------------------------------
def draw_board():
    """Redraw the board on the canvas from the current board state."""
    canvas.delete("all")
    # Draw board background (a royal blue rectangle)
    canvas.create_rectangle(0, 0, COLUMN_COUNT * CELL_SIZE, ROW_COUNT * CELL_SIZE,
                            fill="royalblue", outline="")

    # Draw each cell as a circular "hole"
    for r in range(ROW_COUNT):
        for c in range(COLUMN_COUNT):
            display_row = ROW_COUNT - 1 - r  # because row 0 is at bottom
            x1 = c * CELL_SIZE + MARGIN
            y1 = display_row * CELL_SIZE + MARGIN
            x2 = (c + 1) * CELL_SIZE - MARGIN
            y2 = (display_row + 1) * CELL_SIZE - MARGIN
            if board[r][c] == PLAYER:
                color = "red"
            elif board[r][c] == AI:
                color = "blue"
            else:
                color = "white"
            canvas.create_oval(x1, y1, x2, y2, fill=color, outline="black")

def animate_drop(col, target_row, piece, callback):
    """
    Animate a coin drop into the specified column and target row.
    When the animation finishes, the callback is invoked.
    """
    global animating
    animating = True

    coin_diameter = CELL_SIZE - 2 * MARGIN
    x1 = col * CELL_SIZE + MARGIN
    x2 = (col + 1) * CELL_SIZE - MARGIN
    final_y = (ROW_COUNT - 1 - target_row) * CELL_SIZE + MARGIN
    current_y = -coin_diameter
    color = "red" if piece == PLAYER else "blue"
    coin = canvas.create_oval(x1, current_y, x2, current_y + coin_diameter,
                              fill=color, outline="black")
    step = 20
    delay = 20

    def fall():
        nonlocal current_y
        global animating  # Ensure we update the global variable
        if current_y < final_y:
            current_y = min(current_y + step, final_y)
            canvas.coords(coin, x1, current_y, x2, current_y + coin_diameter)
            canvas.after(delay, fall)
        else:
            canvas.delete(coin)
            animating = False
            callback()

    fall()

def perform_move(col, piece, move_callback):
    """
    Animate the coin drop for the move.
    When the coin finishes dropping, update the board state, redraw,
    and then invoke move_callback().
    """
    row = get_next_open_row(board, col)
    def finish_move():
        drop_piece(board, row, col, piece)
        draw_board()
        move_callback()
    animate_drop(col, row, piece, finish_move)

# -------------------------------
# Event Handlers and Game Flow
# -------------------------------
def player_click(event):
    """Handle player's click on the canvas (to drop a coin)."""
    global turn, game_over
    if game_over or animating or turn != 0:
        return

    col = event.x // CELL_SIZE
    if col < 0 or col >= COLUMN_COUNT or not is_valid_location(board, col):
        return

    def after_player_move():
        if winning_move(board, PLAYER):
            messagebox.showinfo("Game Over", "Congratulations, you win!")
            end_game()
            return
        if len(get_valid_locations(board)) == 0:
            messagebox.showinfo("Game Over", "Draw!")
            end_game()
            return
        turn_switch()
        root.after(300, computer_move)

    perform_move(col, PLAYER, after_player_move)

def computer_move():
    """Compute and perform the computer's move."""
    global turn, game_over
    if game_over or animating or turn != 1:
        return

    valid_locations = get_valid_locations(board)
    if not valid_locations:
        messagebox.showinfo("Game Over", "Draw!")
        end_game()
        return

    if difficulty == "easy":
        col = random.choice(valid_locations)
    elif difficulty == "normal":
        col, _ = minimax(board, 3, -math.inf, math.inf, True)
        if col is None:
            col = random.choice(valid_locations)
    elif difficulty == "hard":
        col, _ = minimax(board, 5, -math.inf, math.inf, True)
        if col is None:
            col = random.choice(valid_locations)
    else:
        col = random.choice(valid_locations)

    def after_computer_move():
        if winning_move(board, AI):
            messagebox.showinfo("Game Over", "Computer wins!")
            end_game()
            return
        if len(get_valid_locations(board)) == 0:
            messagebox.showinfo("Game Over", "Draw!")
            end_game()
            return
        turn_switch()

    perform_move(col, AI, after_computer_move)

def turn_switch():
    """Switch turn between player (0) and computer (1)."""
    global turn
    turn = 0 if turn == 1 else 1

def end_game():
    """Mark the game as over."""
    global game_over
    game_over = True

# -------------------------------
# Control Buttons: Restart and Menu
# -------------------------------
def restart_game():
    """Restart the game with the same difficulty."""
    global board, game_over, turn, animating
    if animating:
        return
    board = create_board()
    game_over = False
    turn = random.choice([0, 1])
    draw_board()
    if turn == 1:
        root.after(500, computer_move)

def go_to_menu():
    """Return to the main menu (difficulty selection)."""
    global board, game_over, animating
    if animating:
        return
    game_frame.pack_forget()
    menu_frame.pack(pady=20)

# -------------------------------
# Difficulty Menu and Game Setup
# -------------------------------
def set_difficulty(diff):
    """Set the difficulty level and start a new game."""
    global difficulty, board, game_over, turn
    difficulty = diff
    menu_frame.pack_forget()
    game_frame.pack()
    board = create_board()
    game_over = False
    turn = random.choice([0, 1])
    draw_board()
    if turn == 1:
        root.after(500, computer_move)

# -------------------------------
# Setting Up the Tkinter GUI
# -------------------------------
root = tk.Tk()
root.title("Connect 4")
root.resizable(False, False)

# --- Menu Frame (Difficulty Selection) ---
menu_frame = tk.Frame(root)
menu_frame.pack(pady=20)

menu_label = tk.Label(menu_frame, text="Select Difficulty", font=("Helvetica", 20, "bold"))
menu_label.pack(pady=10)

button_frame = tk.Frame(menu_frame)
button_frame.pack()

easy_button = tk.Button(button_frame, text="Easy", width=10, font=("Helvetica", 14),
                        command=lambda: set_difficulty("easy"))
easy_button.grid(row=0, column=0, padx=5, pady=5)

normal_button = tk.Button(button_frame, text="Normal", width=10, font=("Helvetica", 14),
                          command=lambda: set_difficulty("normal"))
normal_button.grid(row=0, column=1, padx=5, pady=5)

hard_button = tk.Button(button_frame, text="Hard", width=10, font=("Helvetica", 14),
                        command=lambda: set_difficulty("hard"))
hard_button.grid(row=0, column=2, padx=5, pady=5)

# --- Game Frame (Board + Control Buttons) ---
game_frame = tk.Frame(root)

canvas_width = COLUMN_COUNT * CELL_SIZE
canvas_height = ROW_COUNT * CELL_SIZE
canvas = tk.Canvas(game_frame, width=canvas_width, height=canvas_height, bg="white")
canvas.pack()

canvas.bind("<Button-1>", player_click)

control_frame = tk.Frame(game_frame)
control_frame.pack(pady=10)

restart_button = tk.Button(control_frame, text="Restart", width=12, font=("Helvetica", 12),
                           command=restart_game)
restart_button.pack(side=tk.LEFT, padx=10)

menu_button = tk.Button(control_frame, text="Menu", width=12, font=("Helvetica", 12),
                        command=go_to_menu)
menu_button.pack(side=tk.LEFT, padx=10)

root.mainloop()
