# added collisions


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

# Images ----------------------------------------------------- #
background_img = pygame.image.load('Assets/images/background.png').convert()
player_img = pygame.image.load('Assets/images/player.png')

# Variables -------------------------------------------------- #
FPS = 60

# movement
moving_right = False
moving_left = False

# gravity
player_location = [50, 50]
player_y_momentum = 0

# collisions
player_rect = pygame.Rect(player_location[0], player_location[1], player_img.get_width(), player_img.get_height()) #player hitbox
test_rect = pygame.Rect(100, 100, 100, 50)

# Main Loop -------------------------------------------------- #
while True: # game loop
    screen.fill((146, 244, 255)) # fill screen with color

    screen.blit(player_img, player_location) # render player at player coordinates

    # gravity
    if player_location[1] > WINDOW_SIZE[1]-player_img.get_height():
        player_y_momentum = -player_y_momentum
    else:
        player_y_momentum += 0.2
    player_location[1] += player_y_momentum
    
    # movement
    if moving_right == True:
        player_location[0] += 4
    if moving_left == True:
        player_location[0] -= 4

    # collisions
    player_rect.x = player_location[0]
    player_rect.y = player_location[1]

    if player_rect.colliderect(test_rect): # check if player collides with test_rect
        pygame.draw.rect(screen, (255, 0, 0), test_rect)
    else:
        pygame.draw.rect(screen, (0, 0, 0), test_rect)

    # event loop
    for event in pygame.event.get(): 
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
