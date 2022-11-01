import pygame

from enum import Enum
from random import randint

class Board:
    def __init__(self, size: tuple[int, int]):
        self.size = size

        self.generate_food()

    def generate_food(self):
        self.food = (
                randint(0, self.size[0]),
                randint(0, self.size[1]),
            )

    def draw(self, screen: pygame.surface.Surface, tile_dimensions: tuple[int, int]):
        screen_size = screen.get_size()


        # food
        pygame.draw.rect(screen, (255,0,0), pygame.Rect((self.food[0]*tile_dimensions[0], self.food[1]*tile_dimensions[1], tile_dimensions[0], tile_dimensions[1])))

class Heading(Enum):
    NORTH = 0
    EAST  = 1
    SOUTH = 2
    WEST  = 3

class Snake:
    def __init__(self, size: tuple[int, int]):
        self.heading: Heading = Heading.EAST
        self.head: tuple[int, int] = (0, 0)
        self.segments: list[tuple[int, int]] = [self.head, (1,1),(1,1),]

        self.ate = False

    def eat(self):
        self.ate = True

    def draw(self, screen, tile_dimensions: tuple[int, int]):
        # snake
        for segment in self.segments:
            pygame.draw.rect(screen, (0, 255, 0), pygame.Rect((segment[0]*tile_dimensions[0], segment[1]*tile_dimensions[1], tile_dimensions[0], tile_dimensions[1])))

    def change_heading(self, heading: Heading):
        self.heading = heading

    def move(self):
            x, y = self.head
            match self.heading:
                case Heading.NORTH:
                    y -= 1
                case Heading.EAST:
                    x += 1
                case Heading.SOUTH:
                    y +=1
                case Heading.WEST:
                    x -= 1

            # add new head and remove tail depending on ate
            self.segments.append((x, y))
            self.head = (x, y)

            if not self.ate:
                self.segments.remove(self.segments[0])

            self.ate = False
    

    def update(self, board: Board):
        self.move()

        if self.head in self.segments[:-1]:
            print("snake eating itself")

        elif self.head == board.food:
            self.eat()
            board.generate_food()

        elif self.head[0] < 0 or self.head[1] < 0 or self.head[0] > board.size[0] or self.head[1] > board.size[1]:
            print("wall is also a die situation")
# likely will need pygame magic here for keyinput stuff

def new_game(size: tuple[int, int]) -> Board:
    board = Board(size)

    return board

def draw_stuff(screen: pygame.surface.Surface, board: Board, snake: Snake):
    tile_dimensions = (int(screen.get_size()[0]/board.size[0]), int(screen.get_size()[1]/board.size[1]))
    board.draw(screen, tile_dimensions)
    snake.draw(screen, tile_dimensions)

def cool_background(board: Board, screen: pygame.surface.Surface):
    width = screen.get_size()[1] / board.size[1]
    for y in board.size[1]:
        pygame.draw.rect(screen, (200, 230, 200), pygame.Rect()) # do this later idk

SCREEN_DIMENSIONS = (640, 640)
FPS = 50

if __name__ == "__main__":
    pygame.init()

    screen = pygame.display.set_mode(SCREEN_DIMENSIONS)
    clock = pygame.time.Clock()

    board = new_game((16, 16))
    snake = Snake((16, 16))

    i = 0
    while True:
        i+= 1
        screen.fill((255,255,255))

        draw_stuff(screen, board, snake)
        if i%10 == 0:
            snake.update(board)

        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[pygame.K_w]:
            snake.change_heading(Heading.NORTH)

        if pressed_keys[pygame.K_d]:
            snake.change_heading(Heading.EAST)

        if pressed_keys[pygame.K_s]:
            snake.change_heading(Heading.SOUTH)

        if pressed_keys[pygame.K_a]:
            snake.change_heading(Heading.WEST)

        clock.tick(FPS)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

