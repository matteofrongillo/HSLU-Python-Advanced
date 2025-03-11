import random
import pygame
import sys

# List of valid 5-letter words
WORD_LIST = [
    "apple", "brave", "cigar", "delta", "eagle", "fable", "grape", "hound", 
    "ivory", "joker", "koala", "lemon", "mango", "noble", "ocean", "pearl",
    "queen", "river", "smile", "tiger", "ultra", "vivid", "whale", "xenon",
    "yield", "zebra"
]

def choose_secret_word():
    return random.choice(WORD_LIST)

def get_feedback(guess, solution):
    feedback = [''] * len(solution)
    solution_letter_counts = {}
    # Count letters not correct for yellow detection
    for i, s_char in enumerate(solution):
        if guess[i] != s_char:
            solution_letter_counts[s_char] = solution_letter_counts.get(s_char, 0) + 1
    # Green letters
    for i, g_char in enumerate(guess):
        if g_char == solution[i]:
            feedback[i] = 'G'
        else:
            feedback[i] = None
    # Yellow letters
    for i, g_char in enumerate(guess):
        if feedback[i] is None:
            if g_char in solution_letter_counts and solution_letter_counts[g_char] > 0:
                feedback[i] = 'Y'
                solution_letter_counts[g_char] -= 1
            else:
                feedback[i] = 'B'
    return feedback

# Pygame colors (using colors similar to Wordle)
BACKGROUND_COLOR = (18, 18, 19)
EMPTY_TILE_COLOR = (58, 58, 60)
GREEN_COLOR = (83, 141, 78)
YELLOW_COLOR = (181, 159, 59)
TEXT_COLOR = (255, 255, 255)
BORDER_COLOR = (0,0,0)

# Board settings
ROWS = 6
COLS = 5
TILE_SIZE = 80
TILE_MARGIN = 10

WIDTH = COLS * (TILE_SIZE + TILE_MARGIN) + TILE_MARGIN
HEIGHT = ROWS * (TILE_SIZE + TILE_MARGIN) + TILE_MARGIN + 100  # extra space for messages

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Wordle")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 48)
small_font = pygame.font.Font(None, 32)

def draw_board(board, feedbacks):
    screen.fill(BACKGROUND_COLOR)
    for row in range(ROWS):
        for col in range(COLS):
            x = TILE_MARGIN + col * (TILE_SIZE + TILE_MARGIN)
            y = TILE_MARGIN + row * (TILE_SIZE + TILE_MARGIN)
            tile_rect = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)
            letter = board[row][col]
            cell_feedback = None
            if feedbacks is not None and row < len(feedbacks):
                cell_feedback = feedbacks[row][col]
            # Choose tile color
            if cell_feedback == 'G':
                color = GREEN_COLOR
            elif cell_feedback == 'Y':
                color = YELLOW_COLOR
            elif cell_feedback == 'B':
                color = EMPTY_TILE_COLOR
            else:
                color = EMPTY_TILE_COLOR

            pygame.draw.rect(screen, color, tile_rect)
            pygame.draw.rect(screen, BORDER_COLOR, tile_rect, 2)
            if letter != "":
                text_surface = font.render(letter.upper(), True, TEXT_COLOR)
                text_rect = text_surface.get_rect(center=tile_rect.center)
                screen.blit(text_surface, text_rect)

def show_message(text):
    # Display a message below the board
    text_surface = small_font.render(text, True, TEXT_COLOR)
    text_rect = text_surface.get_rect(center=(WIDTH//2, HEIGHT-50))
    screen.blit(text_surface, text_rect)

def main():
    secret_word = choose_secret_word()
    attempts_allowed = ROWS

    board = [["" for _ in range(COLS)] for _ in range(ROWS)]
    feedbacks = []
    current_guess = ""
    current_row = 0
    message = "Type your guess."
    game_over = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and not game_over:
                if event.key == pygame.K_RETURN:
                    if len(current_guess) != COLS:
                        message = "Not enough letters."
                    elif current_guess not in WORD_LIST:
                        message = "Word not in list."
                    else:
                        # Process guess
                        feedback = get_feedback(current_guess, secret_word)
                        feedbacks.append(feedback)
                        # Update board row with the guess letters
                        for idx, letter in enumerate(current_guess):
                            board[current_row][idx] = letter
                        if current_guess == secret_word:
                            message = "Congratulations! You guessed it!"
                            game_over = True
                        else:
                            current_row += 1
                            if current_row >= attempts_allowed:
                                message = f"Game over! Word was: {secret_word.upper()}"
                                game_over = True
                            else:
                                message = "Type your guess."
                        current_guess = ""
                elif event.key == pygame.K_BACKSPACE:
                    current_guess = current_guess[:-1]
                else:
                    # Accept only alphabetic keys and ignore further if already full
                    if len(current_guess) < COLS and event.unicode.isalpha():
                        current_guess += event.unicode.lower()

        # Draw board
        draw_board(board, feedbacks)
        # Draw current guess letters in the appropriate row
        if current_row < ROWS:
            for i, letter in enumerate(current_guess):
                x = TILE_MARGIN + i * (TILE_SIZE + TILE_MARGIN)
                y = TILE_MARGIN + current_row * (TILE_SIZE + TILE_MARGIN)
                tile_rect = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)
                text_surface = font.render(letter.upper(), True, TEXT_COLOR)
                text_rect = text_surface.get_rect(center=tile_rect.center)
                screen.blit(text_surface, text_rect)

        # Show message
        show_message(message)
        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    main()