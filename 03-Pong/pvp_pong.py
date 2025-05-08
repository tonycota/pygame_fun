#!/usr/bin/env python
# coding: utf-8

# In[5]:


print(f"just wanting to make sure this kernel is connecting correctly.")


# In[6]:


import pygame
import sys


# In[7]:


print(f'dependencies imported successfully')


# In[8]:


import pygame
import sys

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Baby")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Game objects
PADDLE_WIDTH, PADDLE_HEIGHT = 15, 100
BALL_RADIUS = 10
PADDLE_SPEED = 7
BALL_SPEED_X, BALL_SPEED_Y = 5, 5

# Create paddles and ball
left_paddle = pygame.Rect(50, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
right_paddle = pygame.Rect(WIDTH - 50 - PADDLE_WIDTH, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(WIDTH//2 - BALL_RADIUS, HEIGHT//2 - BALL_RADIUS, BALL_RADIUS*2, BALL_RADIUS*2)

# Score
left_score = 0
right_score = 0
font = pygame.font.SysFont("Arial", 36)

# Game loop
clock = pygame.time.Clock()
running = True
while running:
    clock.tick(60)
    SCREEN.fill(BLACK)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get key states
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and left_paddle.top > 0:
        left_paddle.y -= PADDLE_SPEED
    if keys[pygame.K_s] and left_paddle.bottom < HEIGHT:
        left_paddle.y += PADDLE_SPEED
    if keys[pygame.K_UP] and right_paddle.top > 0:
        right_paddle.y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and right_paddle.bottom < HEIGHT:
        right_paddle.y += PADDLE_SPEED

    # Ball movement
    ball.x += BALL_SPEED_X
    ball.y += BALL_SPEED_Y

    # Ball collisions with walls
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        BALL_SPEED_Y *= -1

    # Ball collisions with paddles
    if ball.colliderect(left_paddle) or ball.colliderect(right_paddle):
        BALL_SPEED_X *= -1

    # Scoring
    if ball.left <= 0:
        right_score += 1
        ball.center = (WIDTH//2, HEIGHT//2)
        BALL_SPEED_X *= -1
    if ball.right >= WIDTH:
        left_score += 1
        ball.center = (WIDTH//2, HEIGHT//2)
        BALL_SPEED_X *= -1

    # Draw paddles, ball, score
    pygame.draw.rect(SCREEN, WHITE, left_paddle)
    pygame.draw.rect(SCREEN, WHITE, right_paddle)
    pygame.draw.ellipse(SCREEN, WHITE, ball)
    pygame.draw.aaline(SCREEN, WHITE, (WIDTH//2, 0), (WIDTH//2, HEIGHT))

    left_text = font.render(str(left_score), True, WHITE)
    right_text = font.render(str(right_score), True, WHITE)
    SCREEN.blit(left_text, (WIDTH//4, 20))
    SCREEN.blit(right_text, (WIDTH * 3//4, 20))

    pygame.display.flip()

pygame.quit()
sys.exit()


# In[ ]:




