import pygame
import button
from fonctions import *

pygame.init()

WINDOW_SIZE = resolutions_ecran()

import pygame
import button
pygame.display.set_caption("Super lost world")
#pygame.display.set_icon(x)
pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Main Menu")
game_paused = True
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

resume_img = pygame.image.load("button/button_play.png").convert_alpha()
options_img = pygame.image.load("button/button_option.png").convert_alpha()
quit_img = pygame.image.load("button/button_quit.png").convert_alpha()
video_img = pygame.image.load("button/button_video.png").convert_alpha()
audio_img = pygame.image.load("button/button_audio.png").convert_alpha()
keys_img = pygame.image.load("button/button_keys.png").convert_alpha()
back_img = pygame.image.load("button/button_back.png").convert_alpha()

button_size = (200, 100)
resume_img = pygame.transform.scale(resume_img, button_size)
options_img = pygame.transform.scale(options_img, button_size)
quit_img = pygame.transform.scale(quit_img, button_size)
video_img = pygame.transform.scale(video_img, button_size)
audio_img = pygame.transform.scale(audio_img, button_size)
keys_img = pygame.transform.scale(keys_img, button_size)
back_img = pygame.transform.scale(back_img, button_size)

resume_button = button.Button(300, 225, resume_img, 1)
options_button = button.Button(300, 325, options_img, 1)
quit_button = button.Button(300, 425, quit_img, 1)
video_button = button.Button(300, 225, video_img, 1)
audio_button = button.Button(300, 325, audio_img, 1)
keys_button = button.Button(300, 425, keys_img, 1)
back_button = button.Button(300, 525, back_img, 1)

def draw_text(text, font, text_col, x, y):
  img = font.render(text, True, text_col)
  screen.blit(img, (x, y))


################################## BOUCLE PRINCIPALE ###################################

run = True
while run:

  screen.fill((52, 78, 91))
  screen.blit(background_img, (0, 0))
  screen.blit(title_img, (0, 0))
  
  if game_paused == True:
    if menu_state == "main":
      if resume_button.draw(screen):
        game_paused = False
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
    draw_text("Press SPACE to pause", font, TEXT_COL, 160, 250)


  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE:
        game_paused = True
    if event.type == pygame.QUIT:
      run = False
  pygame.display.update()

pygame.quit()