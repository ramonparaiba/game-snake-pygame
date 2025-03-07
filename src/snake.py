import pygame
from config import BLOCK_SIZE, GREEN


class Snake:
    def __init__(self):
        self.body = [(100, 100), (80, 100), (60, 100)]  # initial snake's body
        self.direction = (BLOCK_SIZE, 0)  # move to right.

    def move(self):
        # add a new head and remove the last part of tail
        head_x, head_y = self.body[0]
        new_head = (head_x + self.direction[0], head_y + self.direction[1])
        self.body.insert(0, new_head)
        self.body.pop()

    def grow(self):
        # add a new sement to body
        self.body.append(self.body[-1])

    def change_direction(self, new_direction):
        # Prevents the snake from moving back where it came from
        if (new_direction[0] * -1, new_direction[1] * -1) != self.direction:
            self.direction = new_direction

    def check_collision(self):
        # collision with borders
        head_x, head_y = self.body[0]
        if head_x < 0 or head_x >= 600 or head_y < 0 or head_y >= 400:
            return True
        # self collision
        if self.body[0] in self.body[1:]:
            return True
        return False

    def draw(self, screen):
        for segment in self.body:
            pygame.draw.rect(screen, GREEN, (*segment, BLOCK_SIZE, BLOCK_SIZE))
