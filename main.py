from enum import Enum
from random import randint

class Board:
    def __init__(self, size: tuple[int, int]):
        self.size = size
        self.snake = Snake(size)

        self.food = self.generate_food()

    def generate_food(self):
        self.food = (randint(randint(0, self.size[0]), randint(0, self.size[1])))

    def update(self):
        head = self.snake.move() # move, then do checks.
        # theres probably some game design course in college
        # that says this is a bad or good idea but i dont particularly care

        if head in self.snake.segments[1:]:
            print("this is a die situation")

        elif head == self.food:
            self.snake.eat()
            self.generate_food()

        elif head[0] < 0 or head[1] < 0 or head[0] > self.size[0] or head[1] > self.size[1]:
            print("wall is also a die situation")

        # likely will need pygame magic here for keyinput stuff
        self.snake.change_heading(Heading.NORTH)


class Heading(Enum):
    NORTH = 0
    EAST  = 0
    SOUTH = 0
    WEST  = 0

class Snake:
    def __init__(self, size: tuple[int, int]):
        self.heading: Heading = Heading.EAST
        self.head: tuple[int, int] = (0, 0)
        self.segments: list[tuple[int, int]] = [self.head]

        self.ate = False
    
    def eat(self):
        self.ate = True

    def change_heading(self, heading: Heading):
        self.heading = heading

    def move(self) -> tuple[int, int]:
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
                self.segments.remove(self.segments[-1])

            self.ate = False
            return self.head

def new_game(size: tuple[int, int]) -> Board:
    board = Board(size)

    return board
