import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 600, 900
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jacob's Flappy")

# Clock
clock = pygame.time.Clock()
FPS = 60

# Game variables
gravity = 0.5
flap_strength = -10
pipe_gap = 150
pipe_width = 70
pipe_speed = 4
bird_radius = 15

# Colors
WHITE = (255, 255, 255)
BLUE = (50, 150, 255)
GREEN = (0, 200, 0)
RED = (255, 0, 0)

font = pygame.font.SysFont("Arial", 32)

def draw_bird(x, y):
    pygame.draw.circle(screen, RED, (int(x), int(y)), bird_radius)

def draw_pipe(x, top_height):
    pygame.draw.rect(screen, GREEN, (x, 0, pipe_width, top_height))
    pygame.draw.rect(screen, GREEN, (x, top_height + pipe_gap, pipe_width, HEIGHT - top_height - pipe_gap))

def check_collision(bird_x, bird_y, pipes):
    if bird_y - bird_radius < 0 or bird_y + bird_radius > HEIGHT:
        return True
    for pipe_x, top in pipes:
        if pipe_x < bird_x + bird_radius < pipe_x + pipe_width:
            if bird_y - bird_radius < top or bird_y + bird_radius > top + pipe_gap:
                return True
    return False

def main():
    bird_x = 100
    bird_y = HEIGHT // 2
    bird_velocity = 0

    pipes = []
    pipe_timer = 0
    score = 0

    running = True
    while running:
        clock.tick(FPS)
        screen.fill(BLUE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird_velocity = flap_strength

        # Update bird
        bird_velocity += gravity
        bird_y += bird_velocity

        # Add new pipes
        pipe_timer += 1
        if pipe_timer >= 90:
            pipe_timer = 0
            top_height = random.randint(50, HEIGHT - pipe_gap - 50)
            pipes.append([WIDTH, top_height])

        # Move pipes
        for pipe in pipes:
            pipe[0] -= pipe_speed

        # Remove offscreen pipes
        pipes = [pipe for pipe in pipes if pipe[0] + pipe_width > 0]

        # Check collision
        if check_collision(bird_x, bird_y, pipes):
            break  # Game over

        # Score
        for pipe in pipes:
            if pipe[0] + pipe_width == bird_x:
                score += 1

        # Draw everything
        draw_bird(bird_x, bird_y)
        for pipe in pipes:
            draw_pipe(pipe[0], pipe[1])

        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()

    pygame.quit()
    print("Game Over! Final score:", score)

if __name__ == "__main__":
    main()
