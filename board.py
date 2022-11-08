from random import randint
import pygame

class Board:
    def __init__(self, size: tuple[int, int]):
        self.size = size

        self.generate_food()

    def generate_food(self):
        self.food = (
                randint(0, self.size[0]-1),
                randint(0, self.size[1]-1),
            )

    def draw(self, screen: pygame.surface.Surface, tile_dimensions: tuple[int, int]):
        for y in range(self.size[1]):

            x1 = 0
            y1 = y/tile_dimensions[1] * screen.get_size()[1]

            x2 = screen.get_size()[1]
            y2 = y + tile_dimensions[1]

            rect = pygame.Rect(
                        0,
                        y*tile_dimensions[1],
                        screen.get_size()[0],
                        y*tile_dimensions[1] + tile_dimensions[1])

            # background bars
            if y % 2 == 0:
                pygame.draw.rect(screen,
                        (150,200,150),
                        rect,
                    )
            else:
                pygame.draw.rect(screen,
                        (150,190,150),
                        rect,
                    )



        # food
        pygame.draw.rect(screen, (255,0,0), pygame.Rect((self.food[0]*tile_dimensions[0], self.food[1]*tile_dimensions[1], tile_dimensions[0], tile_dimensions[1])))

