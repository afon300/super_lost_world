import pygame
import button
import sys
import random
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

menu_start_img = pygame.image.load("images/menu/menu_start.png").convert_alpha()
menu_end_img = pygame.image.load("images/menu/menu_end.png").convert_alpha()
menu_options_img = pygame.image.load("images/menu/menu_options.png").convert_alpha()
title_start_img = pygame.image.load("images/menu/title_start.png").convert_alpha()
title_end_img = pygame.image.load("images/menu/title_end.png").convert_alpha()
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

FOUDRE_SIZE = (32, 32)
foudre_animation = [load_and_scale_image('PNJ/Mobs/monstre_de_foudre/foudre_1.png', CHARACTER_SIZE),
                   load_and_scale_image('PNJ/Mobs/monstre_de_foudre/foudre_2.png', CHARACTER_SIZE),
                   load_and_scale_image('PNJ/Mobs/monstre_de_foudre/foudre_3.png', CHARACTER_SIZE)]

character_x = 300
character_y = 200

blob_x = random.randint(100, 600)
blob_y = random.randint(100, 600)

foudre_x = random.randint(100, 600)
foudre_y = random.randint(100, 600)

blob_health = 2
foudre_health = 4

clock = pygame.time.Clock()

frame_rate = 10
frame = 0
character_speed = 4
direction = "down"
is_moving = False
is_attack = False
is_attacking = False 

blob_frame = 0
blob_speed = 1
blob_direction = "down"
blob_is_moving = False
blob_alive = True

foudre_frame = 0
foudre_speed = 2
foudre_direction = "down"
foudre_is_moving = False
foudre_alive = True

background_map = pygame.image.load("images/maps/background.bmp")
background_map_img = pygame.transform.scale(background_map, MENU_SIZE)
collision_map = pygame.image.load("images/collisions/collision_img.bmp")
collision_map_img = pygame.transform.scale(collision_map, MENU_SIZE)

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

def change_map(new_background_path, new_collision_path):
    global background_map, background_map_img, collision_map, collision_map_img, character_x, character_y

    # Vérifier si la position actuelle du joueur touche la couleur bleue
    current_player_x, current_player_y = character_x, character_y
    if collision_map_img.get_at((current_player_x, current_player_y)) == (0, 0, 255):
        # Charger les nouvelles images de fond et de collision
        background_map = pygame.image.load(new_background_path)
        background_map_img = pygame.transform.scale(background_map, MENU_SIZE)

        collision_map = pygame.image.load(new_collision_path)
        collision_map_img = pygame.transform.scale(collision_map, MENU_SIZE)

        character_x, character_y = start_x, start_y

actual_map = 1

def check_player_position():
    global actual_map, start_x, start_y

    current_player_x, current_player_y = character_x, character_y
    if collision_map_img.get_at((current_player_x, current_player_y)) == (0, 0, 255):
        if actual_map == 1 and current_player_x < 10:  # Exemple de condition pour la zone bleue sur la carte 1
            start_x = 1100
            start_y = 450
            change_map("images/maps/background_2.bmp", "images/collisions/collision_img_2.bmp")
            actual_map = 2
        elif actual_map == 2 and current_player_x > WINDOW_WIDTH - 10:  # Exemple de condition pour la zone bleue sur la carte 2
            start_x = 50
            start_y = 450
            change_map("images/maps/background.bmp", "images/collisions/collision_img.bmp")
            actual_map = 1

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
                new_x, new_y = character_x, character_y
                if x_axis < -threshold:
                    new_x -= character_speed
                    direction = 'left'
                elif x_axis > threshold:
                    new_x += character_speed
                    direction = 'right'
                if y_axis < -threshold:
                    new_y -= character_speed
                    direction = 'up'
                elif y_axis > threshold:
                    new_y += character_speed
                    direction = 'down'

                if not check_collision_with_obstacles(new_x, new_y):
                    character_x, character_y = new_x, new_y
                    is_moving = True
                else:
                    is_moving = False
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
        new_x, new_y = character_x, character_y
        if keys[pygame.K_LEFT]:
            new_x -= character_speed
            direction = 'left'
        elif keys[pygame.K_RIGHT]:
            new_x += character_speed
            direction = 'right'
        elif keys[pygame.K_UP]:
            new_y -= character_speed
            direction = 'up'
        elif keys[pygame.K_DOWN]:
            new_y += character_speed
            direction = 'down'

        if not check_collision_with_obstacles(new_x, new_y):
            character_x, character_y = new_x, new_y
            is_moving = True
        else:
            is_moving = False
        frame = 0

def handle_input():
    if controller:
        handle_joystick_events()
    if keyboard:
        handle_keyboard_input()

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
        
def handle_foudre_movement():
    global foudre_x, foudre_y, foudre_direction, foudre_is_moving, foudre_frame

    if random.randint(1, 20) == 1:
        direction = random.choice(['left', 'right', 'up', 'down'])
        foudre_direction = direction
        foudre_is_moving = True

    if foudre_is_moving:
        if foudre_direction == 'left':
            foudre_x -= foudre_speed
        elif foudre_direction == 'right':
            foudre_x += foudre_speed
        elif foudre_direction == 'up':
            foudre_y -= foudre_speed
        elif foudre_direction == 'down':
            foudre_y += foudre_speed

    if foudre_x < 0:
        foudre_x = 0
    elif foudre_x > WINDOW_WIDTH - FOUDRE_SIZE[0]:
        foudre_x = WINDOW_WIDTH - FOUDRE_SIZE[0]

    if foudre_y < 0:
        foudre_y = 0
    elif foudre_y > WINDOW_HEIGHT - FOUDRE_SIZE[1]:
        foudre_y = WINDOW_HEIGHT - FOUDRE_SIZE[1]

def check_collision(x1, y1, size1, x2, y2, size2):
    return (x1 < x2 + size2[0] and x1 + size1[0] > x2 and 
            y1 < y2 + size2[1] and y1 + size1[1] > y2)
    
def check_collision_with_obstacles(x, y):
    collision_color = (163, 73, 164)
    x = int(x)
    y = int(y)
    if 0 <= x < collision_map_img.get_width() and 0 <= y < collision_map_img.get_height():
        if collision_map_img.get_at((x, y)) == collision_color:
            return True
    return False

pygame.mixer.music.load("musiques/musique_de_fond.mp3")
pygame.mixer.music.set_volume(0.2)
music_playing = False 
world_map = False
actual_map = 1

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
        if not music_playing:  # Jouer la musique une seule fois
             pygame.mixer.music.play(-1)
             music_playing = True
            
        screen.fill((0, 0, 0))
        screen.blit(background_map_img, (0, 0))
        
        handle_input()
        handle_blob_movement()
        handle_foudre_movement()
        
        # marche
        if is_moving and not is_attack:
            frame += 1
            if frame >= 30:
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

            # Collision avec le blob
            current_time = pygame.time.get_ticks()
            if check_collision(character_x, character_y, CHARACTER_SIZE, blob_x, blob_y, BLOB_SIZE):
                if current_time - last_hit_time >= 500:
                    blob_health -= 1
                    last_hit_time = current_time
                    if blob_health <= 0:
                        blob_alive = False
                    print(f"Blob health: {blob_health}")
                    
            if check_collision(character_x, character_y, CHARACTER_SIZE, foudre_x, foudre_y, FOUDRE_SIZE):
                if current_time - last_hit_time >= 500:
                    foudre_health -= 1
                    last_hit_time = current_time
                    if foudre_health <= 0:
                        foudre_alive = False
                    print(f"foudre health: {foudre_health}")

        if not is_moving and not is_attack:
            image = kadhafi_walk_animations[direction][0]
            screen.blit(image, (character_x, character_y))
        
        if blob_alive:
            blob_frame += 1
            if blob_frame >= len(blob_animation) * frame_rate:
                blob_frame = 0
            blob_img = blob_animation[blob_frame // frame_rate]
            screen.blit(blob_img, (blob_x, blob_y))
            
        if foudre_alive:
            foudre_frame += 1
            if foudre_frame >= len(foudre_animation) * frame_rate:
                foudre_frame = 0
            foudre_img = foudre_animation[foudre_frame // frame_rate]
            screen.blit(foudre_img, (foudre_x, foudre_y))
        
        check_player_position()
        
        
    pygame.display.flip()
    clock.tick(60)

pygame.mixer.music.stop()
pygame.quit()
sys.exit()