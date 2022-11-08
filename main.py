import pygame
from pygame.event import wait
from board import Board
from snake import Snake

SCREEN_DIMENSIONS = (640, 640)
FPS = 60
GAME_SIZE = (10, 10)

def new_game(size: tuple[int, int]) -> Board:
    board = Board(size)

    return board

def draw_stuff(screen: pygame.surface.Surface, board: Board, snake: Snake):
    tile_dimensions = (int(screen.get_size()[0]/board.size[0]), int(screen.get_size()[1]/board.size[1]))
    board.draw(screen, tile_dimensions)
    snake.draw(screen, tile_dimensions)
# def cool_background(board: Board, screen: pygame.surface.Surface):
#     width = screen.get_size()[1] / board.size[1]
#     for y in board.size[1]:
#         pygame.draw.rect(screen, (200, 230, 200), pygame.Rect(screen, (y,0))) # do this later idk

if __name__ == "__main__":
    pygame.init()

    screen = pygame.display.set_mode(SCREEN_DIMENSIONS)
    clock = pygame.time.Clock()

    board = new_game(GAME_SIZE)
    snake = Snake(GAME_SIZE)

    i = 0
    living = True
    while living:
        i+= 1
        screen.fill((255,255,255))

        draw_stuff(screen, board, snake)
        if i%10 == 0:
            living = snake.update(board)

        pressed_keys = pygame.key.get_pressed()
        snake.change_heading(pressed_keys)


        clock.tick(FPS)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()


