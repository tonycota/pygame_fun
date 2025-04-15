# This is an attempt to create a tic tac toe game in python

# Ensuring the file is working properly in the window
print(f"I like some of the gaga songs wtf does she know about cameras??")
# Okay we're good

# Import libraries
import pygame
import sys

# Initialize the game
pygame.init()

# Set up the parameters of the game

Width, Height = 600, 600 #Square window
Line_width = 15
board_rows = 3
board_columns = 3
square_size = Width // board_columns # Equals 200
circle_radius = square_size // board_rows # Equals 66
circle_width = 15
cross_width = 25
space = square_size // 4

# Set up the colors
background_color = (28,170,156)
line_color = (23, 145, 135)
circle_color = (239, 231, 200)
cross_color = (66, 66, 66)

#Set up the screen parameters
screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Tic Tac Toe Mother Fucker")
screen.fill(background_color)

# use a list comprehension to set up the board
# shouts out stack overflow
board = [[0 for _ in range(board_columns)] for _ in range(board_rows)]

# create a function to draw the grid
def draw_lines():
    # x_axis lines
    for i in range(1, board_rows):
        pygame.draw.line(screen, line_color, (0, i * square_size), (Width, i * square_size), Line_width)
    for i in range(1, board_columns):
        pygame.draw.line(screen, line_color, (i * square_size, 0), (i * square_size, Height), Line_width)

# draw the x's and o's using another function

def draw_figures():
    for row in range(board_rows):
        for col in range(board_columns):
            if board[row][col] == 1:
                # draw x
                pygame.draw.line(screen, cross_color, (col * square_size + space, row * square_size + space),
                                 (col * square_size + square_size - space, row * square_size + square_size - space), cross_width)
                pygame.draw.line(screen, cross_color, (col * square_size + space, row * square_size + square_size - space),
                                 (col * square_size + square_size - space, row * square_size + space), cross_width)
            elif board[row][col] == 2:
                # draw o
                pygame.draw.circle(screen, circle_color,
                                   (col * square_size +square_size // 2, row * square_size + square_size // 2),
                                   circle_radius, circle_width)

# create a function to check the win
def check_win(player):
    # vertical win
    for col in range(board_columns):
        if all(board[row][col] == player for row in range(board_rows)):
            return True

    # horizontal win
    for row in range(board_rows):
        if all (board[row][col] == player for col in range(board_columns)):
            return True
        
    # diagonal wins
    if all(board[i][i] == player for i in range(board_rows)):
        return True
    if all (board[i][board_columns - 1 - i] == player for i in range(board_rows)):
        return True
    return False

# create a function to restart the game
def restart_game():
    screen.fill(background_color)
    draw_lines()
    for row in range(board_rows):
        for col in range(board_columns):
            board[row][col] = 0

# draw the initial lines
draw_lines()

# set up the game variables
player = 1
game_over = False

# game loop
while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0]
            mouseY = event.pos[1]

            clicked_row = mouseY // square_size
            clicked_col = mouseX // square_size
        
            if board[clicked_row][clicked_col] == 0:
                board[clicked_row][clicked_col] = player
                if check_win(player):
                    game_over = True
                player = 2 if player == 1 else 1
                draw_figures()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart_game()
                game_over = False
                player = 1

    pygame.display.update()


