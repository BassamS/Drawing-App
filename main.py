from utils import *

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
# Name on the top of the window
pygame.display.set_caption('Drawing App')


def init_grid(rows, cols, color):
    grid = []

    for i in range(rows):
        grid.append([])
        for _ in range(cols):
            grid[i].append(color)

    return grid


def draw(win):
    win.fill(BG_COLOR)
    pygame.display.update()


run = True
clock = pygame.time.Clock()

while run:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    draw(WIN)

pygame.quit()
