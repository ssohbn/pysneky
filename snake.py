from typing import Sequence
from heading import Heading
import pygame
from board import Board

class Snake:
    def __init__(self, size: tuple[int, int]):
        self.heading: Heading = Heading.EAST
        self.head: tuple[int, int] = (int(size[0]/2), int(size[1]/2))
        self.segments: list[tuple[int, int]] = [self.head, (-1,-1),(-1,-1),]

        self.ate = False

    def eat(self):
        self.ate = True

    def draw(self, screen, tile_dimensions: tuple[int, int]):
        # snake
        for segment in self.segments:
            pygame.draw.rect(screen, (0, 255, 0), pygame.Rect((segment[0]*tile_dimensions[0], segment[1]*tile_dimensions[1], tile_dimensions[0], tile_dimensions[1])))

    def change_heading(self, pressed_keys: Sequence[bool]):

        if pressed_keys[pygame.K_w] or pressed_keys[pygame.K_UP] and self.heading != Heading.SOUTH:
            self.heading = Heading.NORTH

        elif pressed_keys[pygame.K_d] or pressed_keys[pygame.K_RIGHT] and self.heading != Heading.WEST:
            self.heading = Heading.EAST

        elif pressed_keys[pygame.K_s] or pressed_keys[pygame.K_DOWN] and self.heading != Heading.NORTH:
            self.heading = Heading.SOUTH

        elif pressed_keys[pygame.K_a] or pressed_keys[pygame.K_LEFT] and self.heading != Heading.EAST:
            self.heading = Heading.WEST

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
    

    def update(self, board: Board) -> bool:
        self.move()

        if self.head in self.segments[:-1]:
            return False

        elif board.food in self.segments:
            self.eat()
            board.generate_food()

        # u can go into right and bottom walls. fix later or dont idk
        elif self.head[0] < 0 or self.head[1] < 0 or self.head[0] > board.size[0]-1 or self.head[1] > board.size[1]-1:
            return False

        return True
