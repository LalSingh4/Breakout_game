import pygame
from ball import create_ball, update_ball
from scoreboard import Scoreboard
import time

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Define screen dimensions
WIDTH = 800
HEIGHT = 600

# Define paddle and ball properties
paddle_width = 75
paddle_height = 15
ball_radius = 10

# Initialize Pygame
pygame.init()

# Creating the game screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Breakout")

# Define the paddle as a rectangle
paddle = pygame.Rect(WIDTH // 2 - paddle_width // 2, HEIGHT - paddle_height, paddle_width, paddle_height)

# Create the ball object
ball = create_ball(WIDTH, HEIGHT, ball_radius)

# Initialize the scoreboard
scoreboard = Scoreboard(32)  # Font size for score and lives

# Define some bricks
bricks = []
for row in range(3):
    for col in range(5):
        x = col * (paddle_width + 10) + 10
        y = row * (paddle_height + 5) + 50
        brick = pygame.Rect(x, y, paddle_width, paddle_height)
        bricks.append(brick)

# Game loop
running = True
while running:
    time.sleep(0.01)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Handle keyboard controls for the paddle
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                paddle.x -= 5
            if event.key == pygame.K_RIGHT:
                paddle.x += 5

    # Check for collisions
    ball = update_ball(ball, WIDTH, HEIGHT)

    # Check for paddle collision
    if paddle.colliderect(ball["pos"][0] - ball_radius, ball["pos"][1] - ball_radius, 2 * ball_radius, 2 * ball_radius):
        ball["y_change"] *= -1

    # Check for brick collisions (similar logic as before, update score on hit)
    for brick in bricks:
        if brick.colliderect(ball["pos"][0] - ball_radius, ball["pos"][1] - ball_radius, 2 * ball_radius, 2 * ball_radius):
            bricks.remove(brick)
            ball["y_change"] *= -1
            scoreboard.update_score(10)

    # Check for game over (ball hits bottom)
    if ball["pos"][1] >= HEIGHT:
        scoreboard.lose_life()
        if scoreboard.lives == 0:
            print("Game Over")
            running = False
        # Reset ball position and direction on life loss
        ball = create_ball(WIDTH, HEIGHT, ball_radius)

    # Fill the screen with black
    screen.fill(BLACK)

    # Draw the paddle
    pygame.draw.rect(screen, WHITE, paddle)

    # Draw the ball using ball object's position
    pygame.draw.circle(screen, WHITE, ball["pos"], ball_radius)

    # Draw the bricks
    for brick in bricks:
        pygame.draw.rect(screen, RED, brick)

    # Draw the scoreboard using scoreboard object
    scoreboard.draw(screen, 10, 10)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()

