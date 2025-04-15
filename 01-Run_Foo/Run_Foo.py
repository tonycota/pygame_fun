import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Set up display - Increase screen size by 20%
WIDTH, HEIGHT = int(800 * 1.75), int(600 * 1.5)
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("RUN FROM THE OTHER FOOS")

# Colors
WHITE = (100, 100, 100)
BLUE = (255, 255, 255)
BLACK = (0, 0, 0)
ACTUAL_WHITE = (255, 255, 255)

# Fonts
font = pygame.font.SysFont("Arial", 50)
subfont = pygame.font.SysFont("Arial", 25)
time_font = pygame.font.SysFont("Arial", 30)
face_font = pygame.font.SysFont("Arial", 20)  # Font for the faces

# Player setup - Decrease player size by 20%
player_size = int(50 * 0.8)  # player is now 20% smaller
player_x = WIDTH // 2
player_y = HEIGHT // 2
player_speed = 11  # Initial player speed

# Enemy setup - Increase enemy size by 20%
enemy_size = int(50 * 1.2)  # enemies are now 20% bigger
enemies = []
spawn_interval = 7000  # 7 seconds in milliseconds
last_spawn_time = pygame.time.get_ticks()
enemy_speed = 8  # Initial enemy speed
spawned_enemy_count = 0  # Counter to track number of enemies spawned

# Function to render faces on the player and enemies
def render_face_on_square(square, x, y):
    # Render the face text on the square
    if square == 'player':
        face = face_font.render(":o", True, BLACK)  # Render the player's face
    elif square == 'enemy':
        face = face_font.render(">:(", True, ACTUAL_WHITE)  # Render the enemy's face

    # Draw the face onto the screen at the correct position
    win.blit(face, (x + (player_size // 2) - face.get_width() // 2, y + (player_size // 2) - face.get_height() // 2))

# Function to create a new enemy
def spawn_enemy():
    x = random.randint(0, WIDTH - enemy_size)  # random x position
    y = random.randint(0, HEIGHT - enemy_size)  # random y position
    speed_x = random.choice([-enemy_speed, enemy_speed])  # random speed in x direction
    speed_y = random.choice([-enemy_speed, enemy_speed])  # random speed in y direction
    enemies.append({'x': x, 'y': y, 'speed_x': speed_x, 'speed_y': speed_y})

# Function to check collision between player and enemy
def check_collision(player_x, player_y, enemy):
    # Check if player collides with enemy
    player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
    enemy_rect = pygame.Rect(enemy['x'], enemy['y'], enemy_size, enemy_size)
    return player_rect.colliderect(enemy_rect)  # Returns True if there is a collision

# Function to show instructions
def show_instructions():
    instructions_text = font.render("the party ran out of modelos!", True, BLACK)
    instructions_subtext = subfont.render("the foos are pissed! \n "
    "use arrow keys to run!", True, BLACK)
    
    win.fill(WHITE)
    win.blit(instructions_text, (WIDTH // 2 - instructions_text.get_width() // 2, HEIGHT // 2 - 50))
    win.blit(instructions_subtext, (WIDTH // 2 - instructions_subtext.get_width() // 2, HEIGHT // 2 + 50))
    pygame.display.update()
    
    # Wait for a key press to start the game
    waiting_for_input = True
    while waiting_for_input:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                waiting_for_input = False

# Spawn the first enemy
spawn_enemy()

# Game setup
show_instructions()  # Show instructions before starting the game

# Game loop
running = True
game_over = False
start_time = pygame.time.get_ticks()  # record the start time
elapsed_time = 0  # initialize elapsed time variable

while running:
    pygame.time.delay(30)  # delay to control the speed of the game

    if game_over:
        # Draw "You Lose" text when the game is over
        text = font.render("you died ese!", True, BLACK)
        time_text = time_font.render(f"Time Survived: {elapsed_time} seconds", True, BLACK)
        retry_text = subfont.render("Press 'f' to close the window", True, BLACK)
        
        win.fill(WHITE)
        win.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
        win.blit(time_text, (WIDTH // 2 - time_text.get_width() // 2, HEIGHT // 2 + 50))
        win.blit(retry_text, (WIDTH // 2 - retry_text.get_width() // 2, HEIGHT // 2 + 100))
        pygame.display.update()  # update the screen
        
        # Wait for player input to retry or quit
        waiting_for_input = True
        while waiting_for_input:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_y:  # 'Y' to restart
                        running = False
                        game_over = False
                    elif event.key == pygame.K_f:  # 'N' to quit
                        pygame.quit()
                        sys.exit()

    if not game_over:
        current_time = pygame.time.get_ticks()  # get the current time
        if current_time - last_spawn_time >= spawn_interval:  # check if 7 seconds have passed
            spawn_enemy()  # spawn a new enemy
            last_spawn_time = current_time  # update the last spawn time
            spawned_enemy_count += 1  # increase the count of spawned enemies

            # Every 3 enemies that spawn, increase speed for both player and enemies
            if spawned_enemy_count % 3 == 0:
                player_speed += 1  # increase player speed
                enemy_speed += 1  # increase enemy speed

        for event in pygame.event.get():  # check for events
            if event.type == pygame.QUIT:  # if the user quits, exit
                running = False

        # Move player
        keys = pygame.key.get_pressed()  # get the keys pressed by the player
        if keys[pygame.K_LEFT] and player_x > 0:  # move left
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:  # move right
            player_x += player_speed
        if keys[pygame.K_UP] and player_y > 0:  # move up
            player_y -= player_speed
        if keys[pygame.K_DOWN] and player_y < HEIGHT - player_size:  # move down
            player_y += player_speed

        # Move enemies and check for collisions with walls, player, and other enemies
        for i, enemy in enumerate(enemies):
            enemy['x'] += enemy['speed_x']  # move enemy in x direction
            enemy['y'] += enemy['speed_y']  # move enemy in y direction

            # Bounce off walls
            if enemy['x'] <= 0 or enemy['x'] >= WIDTH - enemy_size:  # bounce in x direction
                enemy['speed_x'] *= -1
            if enemy['y'] <= 0 or enemy['y'] >= HEIGHT - enemy_size:  # bounce in y direction
                enemy['speed_y'] *= -1

            # Check for collision with player
            if check_collision(player_x, player_y, enemy):  # if collision occurs, stop game
                game_over = True
                elapsed_time = (pygame.time.get_ticks() - start_time) // 1000  # capture the time when game is over

            # Check for collisions between enemies
            for j, other_enemy in enumerate(enemies):
                if i != j:  # Don't check the same enemy with itself
                    if check_collision(enemy['x'], enemy['y'], other_enemy):
                        # If enemies collide, reverse their directions
                        enemy['speed_x'] *= -1
                        enemy['speed_y'] *= -1
                        other_enemy['speed_x'] *= -1
                        other_enemy['speed_y'] *= -1

        # Drawing
        win.fill(WHITE)  # fill the screen with grey
        pygame.draw.rect(win, BLUE, (player_x, player_y, player_size, player_size))  # draw player

        # Draw the face on the player
        render_face_on_square('player', player_x, player_y)

        for enemy in enemies:
            pygame.draw.rect(win, BLACK, (enemy['x'], enemy['y'], enemy_size, enemy_size))  # draw enemies
            # Draw the face on each enemy
            render_face_on_square('enemy', enemy['x'], enemy['y'])

        pygame.display.update()  # update the screen

# Exit
pygame.quit()
sys.exit()
