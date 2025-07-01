import pygame
pygame.init()

SIZE: int = 600
WINDOW: pygame.Surface = pygame.display.set_mode((SIZE, SIZE))
FPS = 30
CLOCK = pygame.time.Clock()
SCREEN_COLOR = (255, 255, 255)
LINE_COLOR = (0, 0, 0)
LINE_WIDTH = 3

def draw_board():
    WINDOW.fill(SCREEN_COLOR)
    for _ in range(1, 3):
        pygame.draw.line(WINDOW, LINE_COLOR, (0, _ * (SIZE / 3)), (SIZE, _ * (SIZE / 3)), LINE_WIDTH)
    for _ in range(1, 3):
        pygame.draw.line(WINDOW, LINE_COLOR, (_ * (SIZE / 3), 0), (_ * (SIZE / 3), SIZE), LINE_WIDTH)

def main() -> None:
    running: bool = True
    board: list[list[str]] = [[None for _ in range(3)] for _ in range(3)]
    current: str = 'x'

    draw_board()
    pygame.display.update()
    CLOCK.tick(FPS)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()

if __name__ == '__main__':
    main()