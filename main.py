import pygame
import button
import sys
from fonctions import *

pygame.init()

WINDOW_SIZE = resolutions_ecran()
pygame.display.set_caption("Super lost world")
#pygame.display.set_icon(x)
pygame.init()
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
  
###################################### TEST MAP #######################################
  
exemple_map = pygame.image.load("exemple.png").convert_alpha()
exemple_map_img =  pygame.transform.scale(exemple_map, MENU_SIZE)
# collision_map = pygame.image.load("collision_map.png").convert_alpha()


CHARACTER_SIZE = (64, 64)
walk_down = [load_and_scale_image('main_character/kadafi_face1.png', CHARACTER_SIZE), 
             load_and_scale_image('main_character/kadafi_face2.png', CHARACTER_SIZE), 
             load_and_scale_image('main_character/kadafi_face3.png', CHARACTER_SIZE)]
walk_up = [load_and_scale_image('main_character/kadafi_dos1.png', CHARACTER_SIZE), 
           load_and_scale_image('main_character/kadafi_dos2.png', CHARACTER_SIZE), 
           load_and_scale_image('main_character/kadafi_dos3.png', CHARACTER_SIZE)]
walk_left = [load_and_scale_image('main_character/kadafi_profile_gauche1.png', CHARACTER_SIZE), 
             load_and_scale_image('main_character/kadafi_profile_gauche2.png', CHARACTER_SIZE), 
             load_and_scale_image('main_character/kadafi_profile_gauche3.png', CHARACTER_SIZE)]
walk_right = [load_and_scale_image('main_character/kadafi_profile_droit1.png', CHARACTER_SIZE), 
              load_and_scale_image('main_character/kadafi_profile_droit2.png', CHARACTER_SIZE), 
              load_and_scale_image('main_character/kadafi_profile_droit3.png', CHARACTER_SIZE)]
animations = {'down': walk_down, 'up': walk_up, 'left': walk_left, 'right': walk_right}

character_x = 300
character_y = 200
clock = pygame.time.Clock()

character_speed = 5
frame_rate = 10
frame = 0
direction = "down"
is_moving = False

################################## BOUCLE PRINCIPALE ###################################

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                state_main_menu = True
            else:
                is_moving = True
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYUP:
            is_moving = False

    if state_main_menu:
        screen.fill((52, 78, 91))
        screen.blit(background_img, (0, 0))
        screen.blit(title_img, (0, 0))

        if menu_state == "main":
            if play_button.draw(screen):
                state_main_menu = False
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
    else:
        screen.fill((0, 0, 0))
        screen.blit(exemple_map_img, (0, 0))
        
        if is_moving:
            frame += 1
            if frame >= len(animations[direction]) * frame_rate:
                frame = 0

        for i in range(pygame.joystick.get_count()):
          joystick = pygame.joystick.Joystick(i)
          joystick.init()
          axis = joystick.get_axis(0), joystick.get_axis(1)

        if axis[0] < -0.5:
            character_x -= character_speed
            direction = 'left'
        elif axis[0] > 0.5:
            character_x += character_speed
            direction = 'right'
        elif axis[1] < -0.5:
            character_y -= character_speed
            direction = 'up'
        elif axis[1] > 0.5:
            character_y += character_speed
            direction = 'down'

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            character_x -= character_speed
            direction = 'left'
        elif keys[pygame.K_RIGHT]:
            character_x += character_speed
            direction = 'right'
        elif keys[pygame.K_UP]:
            character_y -= character_speed
            direction = 'up'
        elif keys[pygame.K_DOWN]:
            character_y += character_speed
            direction = 'down'

        else:
            frame = 0

        image = animations[direction][frame // frame_rate]
        screen.blit(image, (character_x, character_y))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()