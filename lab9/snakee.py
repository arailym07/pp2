import pygame
import random
import time
from pygame.locals import *

# Initialize pygame
pygame.init()

# Game settings
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE
FPS = 10

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)

# Directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Setup display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Snake Game with Timed Food')
clock = pygame.time.Clock()

class Snake:
    def __init__(self):
        self.positions = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.length = 1
        self.direction = RIGHT
        self.score = 0
        self.color = GREEN
    
    def get_head_position(self):
        return self.positions[0]
    
    def update(self):
        head = self.get_head_position()
        x, y = self.direction
        new_head = ((head[0] + x) % GRID_WIDTH, (head[1] + y) % GRID_HEIGHT)
        
        if new_head in self.positions[1:]:
            return False
        
        self.positions.insert(0, new_head)
        if len(self.positions) > self.length:
            self.positions.pop()
        return True
    
    def reset(self):
        self.__init__()
    
    def render(self, surface):
        for i, p in enumerate(self.positions):
            rect = pygame.Rect((p[0] * GRID_SIZE, p[1] * GRID_SIZE), (GRID_SIZE, GRID_SIZE))
            color = ORANGE if i == 0 else self.color
            pygame.draw.rect(surface, color, rect)
            pygame.draw.rect(surface, BLACK, rect, 1)

class Food:
    def __init__(self):
        self.randomize_type()
        self.randomize_position()
    
    def randomize_position(self):
        while True:
            self.position = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
            if self.position not in snake.positions:
                break
    
    def randomize_type(self):
        food_types = [
            ("normal", 70, RED, 1, None),
            ("bonus", 20, YELLOW, 3, None),
            ("special", 5, BLUE, 5, None),
            ("timed", 5, PURPLE, 2, 3)  # Disappears after 3 seconds
        ]
        
        self.type, _, self.color, self.weight, self.lifetime = random.choices(
            food_types,
            weights=[t[1] for t in food_types],
            k=1
        )[0]
        
        self.spawn_time = time.time()
    
    def is_expired(self):
        if self.lifetime is not None:
            return time.time() - self.spawn_time > self.lifetime
        return False
    
    def time_remaining(self):
        if self.lifetime is None:
            return 1
        return max(0, (self.lifetime - (time.time() - self.spawn_time)) / self.lifetime)
    
    def render(self, surface):
        rect = pygame.Rect((self.position[0] * GRID_SIZE, self.position[1] * GRID_SIZE), (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(surface, self.color, rect)
        pygame.draw.rect(surface, BLACK, rect, 1)
        
        if self.type == "timed":
            remaining = self.time_remaining()
            radius = int((GRID_SIZE // 2 - 2) * remaining)
            center = (rect.centerx, rect.centery)
            pygame.draw.circle(surface, WHITE, center, radius)

def draw_grid(surface):
    for y in range(0, SCREEN_HEIGHT, GRID_SIZE):
        for x in range(0, SCREEN_WIDTH, GRID_SIZE):
            rect = pygame.Rect((x, y), (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(surface, (50, 50, 50), rect, 1)

def show_hud(surface, score, food_time_left):
    font = pygame.font.SysFont('Arial', 20)
    score_text = font.render(f"Score: {score}", True, WHITE)
    surface.blit(score_text, (10, 10))
    
    if food_time_left is not None:
        time_text = font.render(f"Food: {food_time_left:.1f}s", True, WHITE)
        surface.blit(time_text, (10, 40))

def main():
    global snake
    
    snake = Snake()
    food = Food()
    game_over = False
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_UP and snake.direction != DOWN:
                    snake.direction = UP
                elif event.key == K_DOWN and snake.direction != UP:
                    snake.direction = DOWN
                elif event.key == K_LEFT and snake.direction != RIGHT:
                    snake.direction = LEFT
                elif event.key == K_RIGHT and snake.direction != LEFT:
                    snake.direction = RIGHT
        
        if not game_over:
            if not snake.update():
                game_over = True
            
            if snake.get_head_position() == food.position:
                snake.length += food.weight
                snake.score += food.weight
                food = Food()
            
            if food.is_expired():
                food = Food()
            
            food_time_left = food.time_remaining() if food.lifetime is not None else None
            
            screen.fill(BLACK)
            draw_grid(screen)
            snake.render(screen)
            food.render(screen)
            show_hud(screen, snake.score, food_time_left)
            
            pygame.display.update()
            clock.tick(FPS)
    
    pygame.quit()

if __name__ == "__main__":
    main()