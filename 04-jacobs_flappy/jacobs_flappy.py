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
large_font = pygame.font.SysFont("Arial", 48)

def draw_bird(x, y):
    pygame.draw.circle(screen, RED, (int(x), int(y)), bird_radius)

def draw_pipe(x, top_height):
    pygame.draw.rect(screen, GREEN, (x, 0, pipe_width, top_height))
    pygame.draw.rect(screen, GREEN, (x, top_height + pipe_gap, pipe_width, HEIGHT - top_height - pipe_gap))

def check_collision(bird_x, bird_y, pipes):
    if bird_y - bird_radius < 0 or bird_y + bird_radius > HEIGHT:
        return True
    for pipe_x, top, _ in pipes:
        if pipe_x < bird_x + bird_radius < pipe_x + pipe_width:
            if bird_y - bird_radius < top or bird_y + bird_radius > top + pipe_gap:
                return True
    return False

def start_screen():
    while True:
        screen.fill(BLUE)
        title = large_font.render("Jacob's Flappy", True, WHITE)
        instruction = font.render("Press SPACE to start", True, WHITE)
        controls = font.render("Flap = SPACE | Quit = ESC", True, WHITE)

        screen.blit(title, (WIDTH//2 - title.get_width()//2, HEIGHT//2 - 100))
        screen.blit(instruction, (WIDTH//2 - instruction.get_width()//2, HEIGHT//2))
        screen.blit(controls, (WIDTH//2 - controls.get_width()//2, HEIGHT//2 + 40))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

def game_over_screen(score):
    while True:
        screen.fill(BLUE)
        msg = large_font.render("Game Over!", True, WHITE)
        score_msg = font.render(f"Final Score: {score}", True, WHITE)
        retry = font.render("Press R to Retry or Q to Quit", True, WHITE)

        screen.blit(msg, (WIDTH//2 - msg.get_width()//2, HEIGHT//2 - 100))
        screen.blit(score_msg, (WIDTH//2 - score_msg.get_width()//2, HEIGHT//2 - 30))
        screen.blit(retry, (WIDTH//2 - retry.get_width()//2, HEIGHT//2 + 30))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return True  # Restart game
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

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
            pipes.append([WIDTH, top_height, False])  # False = not yet scored

        # Move pipes
        for pipe in pipes:
            pipe[0] -= pipe_speed

        # Remove offscreen pipes
        pipes = [pipe for pipe in pipes if pipe[0] + pipe_width > 0]

        # Score
        for pipe in pipes:
            if not pipe[2] and pipe[0] + pipe_width < bird_x:
                score += 1
                pipe[2] = True

        # Check collision
        if check_collision(bird_x, bird_y, pipes):
            break

        # Draw everything
        draw_bird(bird_x, bird_y)
        for pipe in pipes:
            draw_pipe(pipe[0], pipe[1])

        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()

    if game_over_screen(score):
        main()

if __name__ == "__main__":
    start_screen()
    main()
