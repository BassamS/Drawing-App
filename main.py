from utils import *

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
# Name on the top of the window
pygame.display.set_caption('Drawing App')

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()
