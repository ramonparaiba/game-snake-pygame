import pygame
from config import BLOCK_SIZE, WIDTH, HEIGHT, SPEED, BLACK
from snake import Snake
from food import Food


class Game:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()
        self.snake = Snake()
        self.food = Food()
        self.running = True
        self.score = 0

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.snake.change_direction((0, -BLOCK_SIZE))
                elif event.key == pygame.K_DOWN:
                    self.snake.change_direction((0, BLOCK_SIZE))
                elif event.key == pygame.K_LEFT:
                    self.snake.change_direction((-BLOCK_SIZE, 0))
                elif event.key == pygame.K_RIGHT:
                    self.snake.change_direction((BLOCK_SIZE, 0))

    def update(self):
        self.snake.move()
        if self.snake.body[0] == self.food.position:
            self.snake.grow()
            self.food.respawn()
            self.score += 10

        if self.snake.check_collision():
            self.running = False

    def draw(self):
        self.screen.fill(BLACK)
        self.snake.draw(self.screen)
        self.food.draw(self.screen)

        pygame.display.flip()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(SPEED)
        
        pygame.quit()
