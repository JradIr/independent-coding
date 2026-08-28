import pygame

pygame.init()

WIDTH, HEIGHT = 300, 300
CELL_SIZE = 100
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")
font = pygame.font.SysFont(None, 36)

board = [" "] * 9
current_player = "X"
winner = None


def draw_board(screen):
    screen.fill((255, 255, 255))

    pygame.draw.line(screen, (0, 0, 0), (100, 0), (100, 300), 5)
    pygame.draw.line(screen, (0, 0, 0), (200, 0), (200, 300), 5)

    pygame.draw.line(screen, (0, 0, 0), (0, 100), (300, 100), 5)
    pygame.draw.line(screen, (0, 0, 0), (0, 200), (300, 200), 5)


def get_cell_from_click(x, y):
    col = x // CELL_SIZE
    row = y // CELL_SIZE
    return row * 3 + col


def draw_marks(screen, board):
    for i, mark in enumerate(board):
        row = i // 3
        col = i % 3
        x = col * CELL_SIZE + 50
        y = row * CELL_SIZE + 50

        if mark == "X":
            pygame.draw.line(screen, (255, 0, 0), (x - 30, y - 30), (x + 30, y + 30), 5)
            pygame.draw.line(screen, (255, 0, 0), (x + 30, y - 30), (x - 30, y + 30), 5)
        elif mark == "O":
            pygame.draw.circle(screen, (0, 0, 255), (x, y), 30, 5)


def check_winner(board):
    wins = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6),
    ]
    for a, b, c in wins:
        if board[a] == board[b] == board[c] != " ":
            return board[a]
    return None


def board_is_full(board):
    return " " not in board


def draw_message(screen, text):
    label = font.render(text, True, (0, 128, 0))
    rect = label.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(label, rect)


def play_again():
    global board, current_player, winner
    board = [" "] * 9
    current_player = "X"
    winner = None


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if winner is not None or board_is_full(board):
                play_again()
            else:
                x, y = event.pos
                cell = get_cell_from_click(x, y)

                if board[cell] == " ":
                    board[cell] = current_player
                    winner = check_winner(board)
                    if winner is None and not board_is_full(board):
                        current_player = "O" if current_player == "X" else "X"

    draw_board(screen)
    draw_marks(screen, board)

    if winner is not None:
        draw_message(screen, winner + " wins! Click to restart")
    elif board_is_full(board):
        draw_message(screen, "Tie! Click to restart")

    pygame.display.flip()

pygame.quit()
