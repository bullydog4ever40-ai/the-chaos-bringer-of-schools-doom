import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display in 4K resolution (3840x2160)
WIDTH, HEIGHT = 3840, 2160
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("Chaos Game - 4K Quality")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Ball properties
ball_radius = 50
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_dx = 10
ball_dy = 10

# Paddle properties
paddle_width = 200
paddle_height = 20
paddle_x = (WIDTH - paddle_width) // 2
paddle_y = HEIGHT - 50
paddle_speed = 15

# Clock for FPS
clock = pygame.time.Clock()
FPS = 60

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # Get keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_x > 0:
        paddle_x -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle_x < WIDTH - paddle_width:
        paddle_x += paddle_speed

    # Update ball
    ball_x += ball_dx
    ball_y += ball_dy

    # Bounce off walls
    if ball_x - ball_radius <= 0 or ball_x + ball_radius >= WIDTH:
        ball_dx = -ball_dx
    if ball_y - ball_radius <= 0:
        ball_dy = -ball_dy

    # Bounce off paddle
    if (ball_y + ball_radius >= paddle_y and
        paddle_x <= ball_x <= paddle_x + paddle_width and
        ball_dy > 0):
        ball_dy = -ball_dy

    # If ball falls off screen, reset
    if ball_y > HEIGHT:
        ball_x = WIDTH // 2
        ball_y = HEIGHT // 2
        ball_dy = -abs(ball_dy)

    # Draw everything
    screen.fill(BLACK)
    pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)
    pygame.draw.rect(screen, WHITE, (paddle_x, paddle_y, paddle_width, paddle_height))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()