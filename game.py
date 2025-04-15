# #Well let's try to make a video game I guess

# #test file to ensure it's working
# print('shabba labba ding dong call my peepee king kong')

#okay we're good

#import dependencies
import pygame
import sys

#initialize pygame
pygame.init()

#set up display
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("first try at this game")

#set up colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

#set up player
player_size = 50
player_x = WIDTH // 2
player_y = HEIGHT // 2
player_speed = 7

#game loop
running = True
while running:
    pygame.time.delay(30)  #this is the delay to control game speed

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #movement keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    #drawing
    win.fill(WHITE)
    pygame.draw.rect(win, BLACK, (player_x, player_y, player_size, player_size))
    pygame.display.update()

#exit
pygame.quit()
sys.exit()
