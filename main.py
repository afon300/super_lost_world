import pygame
import button
import sys
import random
import time
from fonctions import *

# Initialisation de Pygame
pygame.init()

# Définir les paramètres de la fenêtre
WINDOW_SIZE, WINDOW_HEIGHT, WINDOW_WIDTH = resolutions_ecran()
pygame.display.set_caption("Super lost world")
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Main Menu")
state_main_menu = True
menu_state = "main"
font = pygame.font.SysFont("arialblack", 40)

TEXT_COL = (255, 255, 255)

################################# IMAGES BOUTTONS MENU #################################

menu_start_img = pygame.image.load("images_menu/menu_start.png").convert_alpha()
menu_end_img = pygame.image.load("images_menu/menu_end.png").convert_alpha()
menu_options_img = pygame.image.load("images_menu/menu_options.png").convert_alpha()
title_start_img = pygame.image.load("images_menu/title_start.png").convert_alpha()
title_end_img = pygame.image.load("images_menu/title_end.png").convert_alpha()
MENU_SIZE = (1240, 720)
endgame = False

if not endgame:
    background_img = pygame.transform.scale(menu_start_img, MENU_SIZE)
    title_img = pygame.transform.scale(title_start_img, (700, 100))
else:
    background_img = pygame.transform.scale(menu_end_img, MENU_SIZE)
    title_img = pygame.transform.scale(title_end_img, (700, 100))

background_options_img = pygame.transform.scale(menu_options_img, MENU_SIZE)

play_img = pygame.image.load("button/button_play.png").convert_alpha()
options_img = pygame.image.load("button/button_options.png").convert_alpha()
quit_img = pygame.image.load("button/button_quit.png").convert_alpha()
video_img = pygame.image.load("button/button_video.png").convert_alpha()
audio_img = pygame.image.load("button/button_audio.png").convert_alpha()
keys_img = pygame.image.load("button/button_keys.png").convert_alpha()
back_img = pygame.image.load("button/button_back.png").convert_alpha()

button_size = (200, 100)
play_img = pygame.transform.scale(play_img, button_size)
options_img = pygame.transform.scale(options_img, button_size)
quit_img = pygame.transform.scale(quit_img, button_size)
video_img = pygame.transform.scale(video_img, button_size)
audio_img = pygame.transform.scale(audio_img, button_size)
keys_img = pygame.transform.scale(keys_img, button_size)
back_img = pygame.transform.scale(back_img, button_size)

play_button = button.Button(300, 225, play_img, 1)
options_button = button.Button(300, 325, options_img, 1)
quit_button = button.Button(300, 425, quit_img, 1)
video_button = button.Button(300, 225, video_img, 1)
audio_button = button.Button(300, 325, audio_img, 1)
keys_button = button.Button(300, 425, keys_img, 1)
back_button = button.Button(300, 525, back_img, 1)

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

###################################### Experimental #######################################

CHARACTER_SIZE = (64, 64)
walk_down = [load_and_scale_image('main_character/marche/kadhafi_face_1.png', CHARACTER_SIZE), 
             load_and_scale_image('main_character/marche/kadhafi_face_2.png', CHARACTER_SIZE), 
             load_and_scale_image('main_character/marche/kadhafi_face_3.png', CHARACTER_SIZE)]
walk_up = [load_and_scale_image('main_character/marche/kadhafi_dos_1.png', CHARACTER_SIZE), 
           load_and_scale_image('main_character/marche/kadhafi_dos_2.png', CHARACTER_SIZE), 
           load_and_scale_image('main_character/marche/kadhafi_dos_3.png', CHARACTER_SIZE)]
walk_left = [load_and_scale_image('main_character/marche/kadhafi_gauche_1.png', CHARACTER_SIZE), 
             load_and_scale_image('main_character/marche/kadhafi_gauche_2.png', CHARACTER_SIZE), 
             load_and_scale_image('main_character/marche/kadhafi_gauche_3.png', CHARACTER_SIZE),
             load_and_scale_image('main_character/marche/kadhafi_gauche_4.png', CHARACTER_SIZE)]
walk_right = [load_and_scale_image('main_character/marche/kadhafi_droit_1.png', CHARACTER_SIZE), 
              load_and_scale_image('main_character/marche/kadhafi_droit_2.png', CHARACTER_SIZE), 
              load_and_scale_image('main_character/marche/kadhafi_droit_3.png', CHARACTER_SIZE),
              load_and_scale_image('main_character/marche/kadhafi_droit_4.png', CHARACTER_SIZE)]
attack_down = [load_and_scale_image('main_character/attaque/kadhafi_face_1.png', CHARACTER_SIZE), 
             load_and_scale_image('main_character/attaque/kadhafi_face_2.png', CHARACTER_SIZE), 
             load_and_scale_image('main_character/attaque/kadhafi_face_3.png', CHARACTER_SIZE)]
attack_up = [load_and_scale_image('main_character/attaque/kadhafi_dos_1.png', CHARACTER_SIZE), 
           load_and_scale_image('main_character/attaque/kadhafi_dos_2.png', CHARACTER_SIZE), 
           load_and_scale_image('main_character/attaque/kadhafi_dos_3.png', CHARACTER_SIZE)]
attack_left = [load_and_scale_image('main_character/attaque/kadhafi_gauche_1.png', CHARACTER_SIZE), 
             load_and_scale_image('main_character/attaque/kadhafi_gauche_2.png', CHARACTER_SIZE), 
             load_and_scale_image('main_character/attaque/kadhafi_gauche_3.png', CHARACTER_SIZE)]
attack_right = [load_and_scale_image('main_character/attaque/kadhafi_droit_1.png', CHARACTER_SIZE), 
              load_and_scale_image('main_character/attaque/kadhafi_droit_2.png', CHARACTER_SIZE), 
              load_and_scale_image('main_character/attaque/kadhafi_droit_3.png', CHARACTER_SIZE)]

kadhafi_walk_animations = {
    'down': walk_down,
    'up': walk_up,
    'left': walk_left,
    'right': walk_right
}

kadhafi_attack_animations = {
    'down': attack_down,
    'up': attack_up,
    'left': attack_left,
    'right': attack_right
}

BLOB_SIZE = (32, 32)
blob_animation = [load_and_scale_image('PNJ/Mobs/blob/blob_1.png', CHARACTER_SIZE),
                   load_and_scale_image('PNJ/Mobs/blob/blob_2.png', CHARACTER_SIZE),
                   load_and_scale_image('PNJ/Mobs/blob/blob_3.png', CHARACTER_SIZE)]

character_x = 300
character_y = 200

blob_x = random.randint(100, 600)
blob_y = random.randint(100, 600)
blob_health = 2
clock = pygame.time.Clock()

frame_rate = 10
frame = 0
character_speed = 4
direction = "down"
is_moving = False
is_attack = False
is_attacking = False 

blob_frame = 0
blob_speed = 3
blob_direction = "down"
blob_is_moving = False
blob_alive = True

exemple_map = pygame.image.load("exemple.png").convert_alpha()
exemple_map_img = pygame.transform.scale(exemple_map, MENU_SIZE)

keyboard = True
controller = False

if pygame.joystick.get_count() > 0:
    controller = True
    keyboard = False
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
else:
    joystick = None

last_press = 0
input_delay = 750
last_hit_time = 0

def handle_joystick_events():
    global character_x, character_y, direction, is_moving, last_press, frame, is_attack, is_attacking, last_tick

    if controller:
        x_axis = joystick.get_axis(0)
        y_axis = joystick.get_axis(1)
        threshold = 0.1
    
    if joystick.get_button(0) or joystick.get_button(1):
        if last_press >= input_delay:
            if joystick.get_button(0):
                print("A")
                is_attack = True
                is_attacking = True
                is_moving = False
                frame = 0
            if joystick.get_button(1):
                print("B")
                is_moving = False
                frame = 0
            last_press = 0
        else:
            last_press += pygame.time.get_ticks() - last_tick
    else:
        if abs(x_axis) > threshold or abs(y_axis) > threshold:
            if x_axis < -threshold:
                character_x -= character_speed
                direction = 'left'
                is_moving = True
            elif x_axis > threshold:
                character_x += character_speed
                direction = 'right'
                is_moving = True
            if y_axis < -threshold:
                character_y -= character_speed
                direction = 'up'
                is_moving = True
            elif y_axis > threshold:
                character_y += character_speed
                direction = 'down'
                is_moving = True
        else:
            is_moving = False
            frame = 0
            
def handle_keyboard_input():
    global character_x, character_y, direction, is_moving, last_press, frame, is_attack, is_attacking, last_tick

    keys = pygame.key.get_pressed()
    current_time = pygame.time.get_ticks()
    if keys[pygame.K_a] or keys[pygame.K_z]:
        if current_time - last_press >= input_delay:
            if keys[pygame.K_a]:
                print("A")
                is_attack = True
                is_attacking = True
                is_moving = False
                frame = 0
            if keys[pygame.K_z]:
                print("Z")
                is_moving = False
                frame = 0
            last_press = current_time
    else:
        if keys[pygame.K_LEFT]:
            character_x -= character_speed
            direction = 'left'
            is_moving = True
        elif keys[pygame.K_RIGHT]:
            character_x += character_speed
            direction = 'right'
            is_moving = True
        elif keys[pygame.K_UP]:
            character_y -= character_speed
            direction = 'up'
            is_moving = True
        elif keys[pygame.K_DOWN]:
            character_y += character_speed
            direction = 'down'
            is_moving = True
        else:
            is_moving = False
            frame = 0

def handle_input():
    if controller:
        handle_joystick_events()
    if keyboard:
        handle_keyboard_input()

def check_collision(x1, y1, size1, x2, y2, size2):
    return (x1 < x2 + size2[0] and x1 + size1[0] > x2 and 
            y1 < y2 + size2[1] and y1 + size1[1] > y2)

def handle_blob_movement():
    global blob_x, blob_y, blob_direction, blob_is_moving, blob_frame

    if random.randint(1, 20) == 1:
        direction = random.choice(['left', 'right', 'up', 'down'])
        blob_direction = direction
        blob_is_moving = True

    if blob_is_moving:
        if blob_direction == 'left':
            blob_x -= blob_speed
        elif blob_direction == 'right':
            blob_x += blob_speed
        elif blob_direction == 'up':
            blob_y -= blob_speed
        elif blob_direction == 'down':
            blob_y += blob_speed

    if blob_x < 0:
        blob_x = 0
    elif blob_x > WINDOW_WIDTH - BLOB_SIZE[0]:
        blob_x = WINDOW_WIDTH - BLOB_SIZE[0]

    if blob_y < 0:
        blob_y = 0
    elif blob_y > WINDOW_HEIGHT - BLOB_SIZE[1]:
        blob_y = WINDOW_HEIGHT - BLOB_SIZE[1]

world_map = False

run = True
while run:
    last_tick = pygame.time.get_ticks()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                state_main_menu = True
        if event.type == pygame.QUIT:
            run = False
    if state_main_menu:
        screen.fill((52, 78, 91))
        screen.blit(background_img, (0, 0))
        screen.blit(title_img, (0, 0))

        if menu_state == "main":
            if play_button.draw(screen):
                state_main_menu = False
                world_map = True
            if options_button.draw(screen):
                menu_state = "options"
            if quit_button.draw(screen):
                run = False
        if menu_state == "options":
            screen.blit(background_options_img, (0, 0))
            if video_button.draw(screen):
                print("Video Settings")
            if audio_button.draw(screen):
                print("Audio Settings")
            if keys_button.draw(screen):
                print("Change Key Bindings")
            if back_button.draw(screen):
                menu_state = "main"
    if world_map:
        screen.fill((0, 0, 0))
        screen.blit(exemple_map_img, (0, 0))
        
        handle_input()
        handle_blob_movement()
        
        # marche
        if is_moving and not is_attack:
            frame += 1
            if frame >= len(kadhafi_walk_animations[direction]) * frame_rate:
                frame = 0
            image = kadhafi_walk_animations[direction][frame // frame_rate]
            screen.blit(image, (character_x, character_y))

        # attaque
        if is_attack:
            is_moving = False
            frame += 1
            if frame >= len(kadhafi_attack_animations[direction]) * frame_rate:
                frame = 0
                is_attack = False
            image = kadhafi_attack_animations[direction][frame // frame_rate]
            screen.blit(image, (character_x, character_y))

            # Collision
            current_time = pygame.time.get_ticks()
            if check_collision(character_x, character_y, CHARACTER_SIZE, blob_x, blob_y, BLOB_SIZE):
                if current_time - last_hit_time >= 500:
                    blob_health -= 1
                    last_hit_time = current_time
                    if blob_health <= 0:
                        blob_alive = False
                    print(f"Blob health: {blob_health}")

        if not is_moving and not is_attack:
            image = kadhafi_walk_animations[direction][0]
            screen.blit(image, (character_x, character_y))
        
        if blob_alive:
            blob_frame += 1
            if blob_frame >= len(blob_animation) * frame_rate:
                blob_frame = 0
            blob_img = blob_animation[blob_frame // frame_rate]
            screen.blit(blob_img, (blob_x, blob_y))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()

#Aventure, exploration, polution , réfléchir, découvrir