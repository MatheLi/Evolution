# added animation

# Setup Python ----------------------------------------------- #
import pygame, sys, os # import pygame, sys and os

# Setup pygame ----------------------------------------------- #
clock = pygame.time.Clock() # setup the clock

from pygame.locals import * # import pygame modules
pygame.init() # inititates pygame

# Setup window ----------------------------------------------- #
pygame.display.set_caption('Evolution 1.0.0') # set window name

WINDOW_SIZE = (720, 405) # set up window size

screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32) # initiate screen

display = pygame.Surface((240, 135)) # Surface

# Images ----------------------------------------------------- #
background_img = pygame.image.load('Assets/images/background.png').convert()
player_img = pygame.image.load('Assets/images/player.png')
player_img.set_colorkey((255, 255, 255)) # set this color transparent
next_arrow_img = pygame.image.load('Assets/images/arrow.png').convert()
next_arrow_img.set_colorkey((255,255,255))

# Animations ------------------------------------------------- #
animation_timings = {}
animation_database = {}
for anim in os.listdir('Assets/animations'):
    f = open('Assets/animations/' + anim + '/timings.txt','r')
    t = f.read()
    f.close()
    timings = t.split(';')
    n = 0
    for val in timings:
        timings[n] = int(val)
        n += 1
    animation_timings[anim] = timings.copy()
    images = []
    for i in range(len(timings)):
        img = pygame.image.load('Assets/animations/' + anim + '/' + anim + '_' + str(i) + '.png').convert()
        img.set_colorkey((255,255,255))
        images.append(img.copy())
    animation_database[anim] = images.copy()

# Functions -------------------------------------------------- #
def collision_test(rect, tiles):
    hit_list = []
    for tile in tiles:
        if rect.colliderect(tile):
            hit_list.append(tile)
    return hit_list

# check for colissions
def move(rect, movement, tiles):
    collision_types = {'top': False, 'bottom': False, 'right': False, 'left': False}

    rect.x += movement[0]
    hit_list = collision_test(rect, tiles)
    for tile in hit_list:
        if movement[0] > 0:
            rect.right = tile.left 
            collision_types['right'] = True
        if movement[0] < 0:
            rect.left = tile.right
            collision_types['left'] = True

    rect.y += movement[1]
    hit_list = collision_test(rect, tiles)
    for tile in hit_list:
        if movement[1] > 0:
            rect.bottom = tile.top 
            collision_types['bottom'] = True
        if movement[1] < 0:
            rect.top = tile.bottom 
            collision_types['top'] = True

    return rect, collision_types

# Variables -------------------------------------------------- #
FPS = 60

# movement
up = False
down = False
right = False
left = False

# gravity
player_y_momentum = 0

# collisions
player_rect = pygame.Rect(50, 50, player_img.get_width(), player_img.get_height()) #player hitbox

# scroll
scroll = [0, 0]
true_scroll = [0,0]


# Main Loop -------------------------------------------------- #
while True: # game loop
    display.fill((0,0,0)) # fill screen with color

    # background 
    tile_rects = []

    true_scroll[0] += (player_rect.x - true_scroll[0] - 120) / 10
    true_scroll[1] += (player_rect.y - true_scroll[1] - 68) / 10
    scroll = [int(true_scroll[0]), int(true_scroll[1])]
    
    if scroll[1] > 5:
        scroll[1] = 5
    if scroll[1] < -69:
        scroll[1] = -69
    if scroll[0] < -62:
        scroll[0] = -62
    if scroll[0] > 67:
        scroll[0] = 67

    display.blit(background_img,(-scroll[0]-62, -scroll[1]-69)) # fill screen with background

    # Handle Movement ---------------------------------------- #
    player_movement = [0,0]
    if up == True:
        player_movement[1] -= 1.4
    if down == True:
        player_movement[1] += 1.4
    if right == True:
        player_movement[0] += 1.4
    if left == True:
        player_movement[0] -= 1.4

    player_movement[1] += player_y_momentum
    
    player_rect, collisions = move(player_rect, player_movement, tile_rects)


    # collisions
    if collisions['bottom']:
        player_y_momentum = 0

    display.blit(player_img, (player_rect.x, player_rect.y)) # render player at player coordinates

    # event loop
    for event in pygame.event.get(): 
        if event.type == QUIT: # check for window quit)
            pygame.quit() # stop pygame
            sys.exit() # stop script

        if event.type == KEYDOWN: # check for key pressed
            if event.key == K_d:
                right = True
            if event.key == K_a:
                left = True
            if event.key == K_w:
                up = True
            if event.key == K_s:
                down = True

        if event.type == KEYUP: # check for key released
            if event.key == K_d:
                right = False
            if event.key == K_a:
                left = False
            if event.key == K_w:
                up = False
            if event.key == K_s:
                down = False

    # Update ------------------------------------------------- #
    surf = pygame.transform.scale(display, WINDOW_SIZE) # define Surface
    screen.blit(surf, (0,0)) # display Surface
    pygame.display.update() # update display
    clock.tick(FPS) # maintain 60 fps

