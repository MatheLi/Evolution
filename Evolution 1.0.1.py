# added player image
# added player movement


# Setup Python ----------------------------------------------- #
import pygame, sys # import pygame and sys

# Setup pygame ----------------------------------------------- #
clock = pygame.time.Clock() # setup the clock

from pygame.locals import * # import pygame modules
pygame.init() # inititates pygame

# Setup window ----------------------------------------------- #
pygame.display.set_caption('Evolution 1.0.0') # set window name

WINDOW_SIZE = (400, 400) # set up window size

screen = pygame.display.set_mode(WINDOW_SIZE) # initiate screen

# Variables -------------------------------------------------- #
FPS = 60
moving_right = False
moving_left = False

player_location = [50, 50]
# Images ----------------------------------------------------- #
background_img = pygame.image.load('Assets/images/background.png').convert()
player_img = pygame.image.load('Assets/images/player.png')

# Main Loop -------------------------------------------------- #
while True: # game loop
    screen.fill((146, 244, 255)) # fill screen with color
    screen.blit(player_img, player_location) # render player at player coordinates

    if moving_right == True:
        player_location[0] += 4
    if moving_left == True:
        player_location[0] -= 4

    for event in pygame.event.get(): # event loop
        if event.type == QUIT: # check for window quit
            pygame.quit() # stop pygame
            sys.exit() # stop script

        if event.type == KEYDOWN: # check for key pressed
            if event.key == K_RIGHT:
                moving_right = True
            if event.key == K_LEFT:
                moving_left = True
        if event.type == KEYUP: # check for key pressed
            if event.key == K_RIGHT:
                moving_right = False
            if event.key == K_LEFT:
                moving_left = False

    pygame.display.update() # update display
    clock.tick(FPS) # maintain fps
