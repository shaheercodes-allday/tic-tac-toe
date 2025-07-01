import pygame
import time
pygame.init()

SIZE: int = 600
WINDOW: pygame.Surface = pygame.display.set_mode((SIZE, SIZE))
FPS: int = 30
CLOCK: pygame.time.Clock = pygame.time.Clock()
SCREEN_COLOR: tuple = (230, 230, 230)
LINE_COLOR: tuple = (0, 0, 0)
LINE_WIDTH: int = 3

def draw_board(board, x_shape, o_shape) -> None:
    WINDOW.fill(SCREEN_COLOR)
    for _ in range(1, 3):
        pygame.draw.line(WINDOW, LINE_COLOR, (0, _ * (SIZE / 3)), (SIZE, _ * (SIZE / 3)), LINE_WIDTH)
    for _ in range(1, 3):
        pygame.draw.line(WINDOW, LINE_COLOR, (_ * (SIZE / 3), 0), (_ * (SIZE / 3), SIZE), LINE_WIDTH)

    for i in range(3):
        for j in range(3):
            if board[i][j] == 'x':
                WINDOW.blit(x_shape, (j * SIZE / 3 + 25, i * SIZE / 3 + 25))
            elif board[i][j] == 'o':
                WINDOW.blit(o_shape, (j * SIZE / 3 + 25, i * SIZE / 3 + 25))

def we_have_a_winner(board, shape) -> bool:
    for i in range(3):
        if board[i].count(shape) == 3:
            return True
        if board[0][i] == shape and board[1][i] == shape and board[2][i] == shape:
            return True
        
    if board[1][1] == shape:
        if board[0][0] == shape and board[2][2] == shape:
            return True
        if board[0][2] == shape and board[2][0] == shape:
            return True
        
    return False

def board_is_full(board) -> bool:
    return board[0].count(None) + board[1].count(None) + board[2].count(None) == 0

def main() -> None:
    running: bool = True
    board: list[list[str]] = [[None for _ in range(3)] for _ in range(3)]
    x_shape = pygame.image.load('assets/x.png').convert_alpha()
    o_shape = pygame.image.load('assets/o.png').convert_alpha()
    current_shape: str = 'x'

    while running:
        draw_board(board, x_shape, o_shape)
        pygame.display.update()
        CLOCK.tick(FPS)

        if board_is_full(board):
            time.sleep(1)
            board = [[None for _ in range(3)] for _ in range(3)]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x_pos, y_pos = event.pos[0] // int(SIZE / 3), event.pos[1] // int(SIZE / 3)
                board[y_pos][x_pos] = current_shape
                if we_have_a_winner(board, current_shape):
                    print(f'{current_shape} WON!!!')
                    running = False
                current_shape = 'o' if current_shape == 'x' else 'x'

    pygame.quit()

if __name__ == '__main__':
    main()