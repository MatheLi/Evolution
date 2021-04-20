# added player animation
# added boundaries
# added jump

# Setup Python ----------------------------------------------- #
import pygame, sys, os # import pygame, sys and os
import Assets.entities as e
# Setup pygame ----------------------------------------------- #
clock = pygame.time.Clock() # setup the clock

from pygame.locals import * # import pygame modules
pygame.init() # inititates pygame

# Setup window ----------------------------------------------- #
pygame.display.set_caption('Evolution 1.0.0') # set window name

WINDOW_SIZE = (720, 405) # set up window size
DISPLAY_SIZE = (240, 135)# set up surface size

screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32) # initiate screen

display = pygame.Surface(DISPLAY_SIZE) # Surface

# Images ----------------------------------------------------- #
background_img = pygame.image.load('Assets/images/background.png').convert()
player_img = pygame.image.load('Assets/images/player.png')
player_img.set_colorkey((255, 255, 255)) # set this color transparent
next_arrow_img = pygame.image.load('Assets/images/arrow.png').convert()
next_arrow_img.set_colorkey((255,255,255))
L1_img = pygame.image.load('Assets/animations/green_monster/L1.png')
L1_img.set_colorkey((255, 255, 255))
L2_img = pygame.image.load('Assets/animations/green_monster/L2.png')
L2_img.set_colorkey((255, 255, 255))
L3_img = pygame.image.load('Assets/animations/green_monster/L3.png')
L3_img.set_colorkey((255, 255, 255))
L4_img = pygame.image.load('Assets/animations/green_monster/L4.png')
L4_img.set_colorkey((255, 255, 255))
L5_img = pygame.image.load('Assets/animations/green_monster/L5.png')
L5_img.set_colorkey((255, 255, 255))
L6_img = pygame.image.load('Assets/animations/green_monster/L6.png')
L6_img.set_colorkey((255, 255, 255))

R1_img = pygame.image.load('Assets/animations/green_monster/R1.png')
R1_img.set_colorkey((255, 255, 255))
R2_img = pygame.image.load('Assets/animations/green_monster/R2.png')
R2_img.set_colorkey((255, 255, 255))
R3_img = pygame.image.load('Assets/animations/green_monster/R3.png')
R3_img.set_colorkey((255, 255, 255))
R4_img = pygame.image.load('Assets/animations/green_monster/R4.png')
R4_img.set_colorkey((255, 255, 255))
R5_img = pygame.image.load('Assets/animations/green_monster/R5.png')
R5_img.set_colorkey((255, 255, 255))
R6_img = pygame.image.load('Assets/animations/green_monster/R6.png')
R6_img.set_colorkey((255, 255, 255))

# Functions -------------------------------------------------- #
def collision_test(rect, tiles):
    hit_list = []
    for tile in tiles:
        if rect.colliderect(tile):
            hit_list.append(tile)
    return hit_list
    

# Initialization --------------------------------------------- #
e.load_animations('Assets/images/entities/')

# Player Class ----------------------------------------------- #
class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.move_animation_right = False
        self.move_animation_left = False
        self.walk_left = [L1_img, L2_img, L3_img, L4_img, L5_img, L6_img]
        self.walk_right = [R1_img, R2_img, R3_img, R4_img, R5_img, R6_img]
        self.current_sprite = 0
        self.image = self.walk_left[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x,pos_y]

    def move(self, movement, tiles):
        collision_types = {'top': False, 'bottom': False, 'right': False, 'left': False}

        self.rect.x += movement[0]
        hit_list = collision_test(self.rect, tiles)
        for tile in hit_list:
            if movement[0] > 0:
                self.rect.right = tile.left 
                collision_types['right'] = True
            if movement[0] < 0:
                self.rect.left = tile.right
                collision_types['left'] = True

        self.rect.y += movement[1]
        hit_list = collision_test(self.rect, tiles)
        for tile in hit_list:
            if movement[1] > 0:
                self.rect.bottom = tile.top 
                collision_types['bottom'] = True
            if movement[1] < 0:
                self.rect.top = tile.bottom 
                collision_types['top'] = True

        return self.rect, collision_types


    def update(self,speed):
        if self.move_animation_left == True:
            self.current_sprite += speed
            if int(self.current_sprite) >= len(self.walk_left):
                self.current_sprite = 0
            self.image = self.walk_left[int(self.current_sprite)]

        if self.move_animation_right == True:
            self.current_sprite += speed
            if int(self.current_sprite) >= len(self.walk_right):
                self.current_sprite = 0
            self.image = self.walk_right[int(self.current_sprite)]

# Variables -------------------------------------------------- #
FPS = 60
VEL = 1.4
JUMP_VEL = 6
# Creating the sprites and groups
moving_sprites = pygame.sprite.Group()
player = Player(50, 50)
moving_sprites.add(player)

# movement
up = False
down = False
right = False
left = False
isJump = False
jump_count = 10

# gravity
player_y_momentum = 0

# scroll
scroll = [0, 0]
true_scroll = [0,0]

# animations
active_animations = []
# Main Loop -------------------------------------------------- #
while True: # game loop
    # background + camera moving
    tile_rects = []

    true_scroll[0] += (player.rect.x - true_scroll[0] - 120) / 10
    true_scroll[1] += (player.rect.y - true_scroll[1] - 68) / 10
    scroll = [int(true_scroll[0]), int(true_scroll[1])]
    
    if scroll[1] > 5:
        scroll[1] = 5
    if scroll[1] < -69:
        scroll[1] = -69
    if scroll[0] < -62:
        scroll[0] = -62
    if scroll[0] > 67:
        scroll[0] = 67

    # Handle Movement ---------------------------------------- #
    player_movement = [0,0]
    if up == True:
        player_movement[1] -= VEL
    if down == True:
        player_movement[1] += VEL
    if left == True:
        player_movement[0] -= VEL
        player.move_animation_left = True
    if right == True:
        player_movement[0] += VEL
        player.move_animation_right = True
    if isJump == True:
        if jump_count >= -10:
            neg = 1
            if jump_count < 5:
                neg = -1
            player_movement[1] -= (jump_count ** 2) * 0.09 * neg
            jump_count -= 1
        else:
            isJump = False
            jump_count = 10

    if up == False:
        pass
    if down == False:
        pass
    if left == False:
        player.move_animation_left = False
    if right == False:
        player.move_animation_right = False

    
    player_movement[1] += player_y_momentum # gravity (aktuell 0)
    
    player.rect, collisions = player.move(player_movement, tile_rects) # neue pos von player & check for collisions


    # collisions
    if collisions['bottom']:
        player_y_momentum = 0

    # Animations
    entities = []
    entities.append(e.entity(50,50,6,6,'player'))
    for entity in entities:
        if entity.type == 'player':
            if player_movement != [0,0]:
                entity.change_frame(1)
            if player_movement[1] > 0:
                entity.set_action('walk_down')
            if player_movement[1] < 0:
                entity.set_action('walk_up')
            if player_movement[0] > 0:
                entity.set_action('walk_side')
                entity.set_flip(False)
            if player_movement[0] < 0:
                entity.set_action('walk_side')
                entity.set_flip(True)
            entity.move(player_movement,[],[])

 
    # event loop
    for event in pygame.event.get(): 
        if event.type == QUIT: # check for window quit)
            pygame.quit() # stop pygame
            sys.exit() # stop script

        if event.type == KEYDOWN: # check for key pressed
            if event.key == K_a and player.rect.x > VEL:
                left = True
            if event.key == K_d and player.rect.x < DISPLAY_SIZE[0] - player.rect.width:
                right = True

            if not (isJump):
                if event.key == K_w and player.rect.y > VEL:
                    up = True
                if event.key == K_s and player.rect.y < DISPLAY_SIZE[1] - player.rect.height:
                    down = True
                if event.key == K_SPACE:
                    isJump = True
           
            
           
        if event.type == KEYUP: # check for key released
            if event.key == K_d:
                right = False
            if event.key == K_a:
                left = False
            if event.key == K_w:
                up = False
            if event.key == K_s:
                down = False

    # Drawing ------------------------------------------------- #
    screen.fill((0,0,0)) # fill screen with color
    surf = pygame.transform.scale(display, WINDOW_SIZE) # define Surface
    screen.blit(surf, (0,0)) # display Surface
    display.blit(background_img,(-scroll[0]-62, -scroll[1]-69)) # fill screen with background
    moving_sprites.draw(display) # draw sprites on surface
    moving_sprites.update(0.2) # update sprites animation
    pygame.display.update() # update display
    clock.tick(FPS) # maintain 60 fps

