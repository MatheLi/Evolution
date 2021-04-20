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

# Images ----------------------------------------------------- #
background_img = pygame.image.load('Assets/images/background.png').convert()

# Main Loop -------------------------------------------------- #
while True: # game loop

    for event in pygame.event.get(): # event loop
        if event.type == QUIT: # check for window quit
            pygame.quit() # stop pygame
            sys.exit() # stop script


    pygame.display.update() # update display
    clock.tick(FPS) # maintain fps
