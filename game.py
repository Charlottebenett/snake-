import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Snake
SNAKE_SIZE = 20
SNAKE_SPEED = 15
snake_x, snake_y = WIDTH // 2, HEIGHT // 2
snake_x_change, snake_y_change = 0, 0
snake = [(snake_x, snake_y)]

# Apples
apple_x, apple_y = random.randrange(0, WIDTH - SNAKE_SIZE, SNAKE_SIZE), random.randrange(0, HEIGHT - SNAKE_SIZE, SNAKE_SIZE)

# Score
score = 0
font = pygame.font.Font(None, 36)

# Function to display the score
def show_score():
    score_text = font.render(f"Score: {score}", True, GREEN)
    screen.blit(score_text, (10, 10))

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        snake_x_change = -SNAKE_SIZE
        snake_y_change = 0
    elif keys[pygame.K_RIGHT]:
        snake_x_change = SNAKE_SIZE
        snake_y_change = 0
    elif keys[pygame.K_UP]:
        snake_x_change = 0
        snake_y_change = -SNAKE_SIZE
    elif keys[pygame.K_DOWN]:
        snake_x_change = 0
        snake_y_change = SNAKE_SIZE

    snake_x += snake_x_change
    snake_y += snake_y_change
    snake.append((snake_x, snake_y))

    if snake_x == apple_x and snake_y == apple_y:
        apple_x, apple_y = random.randrange(0, WIDTH - SNAKE_SIZE, SNAKE_SIZE), random.randrange(0, HEIGHT - SNAKE_SIZE, SNAKE_SIZE)
        score += 1

    if len(snake) > score + 1:
        del snake[0]

    screen.fill(WHITE)
    pygame.draw.rect(screen, GREEN, [apple_x, apple_y, SNAKE_SIZE, SNAKE_SIZE])

    for segment in snake:
        pygame.draw.rect(screen, GREEN, [segment[0], segment[1], SNAKE_SIZE, SNAKE_SIZE])

    show_score()
    pygame.display.update()
    pygame.time.delay(100)
