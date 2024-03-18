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
game_paused = False
menu_state = "main"
font = pygame.font.SysFont("arialblack", 40)

TEXT_COL = (255, 255, 255)

################################# IMAGES BOUTTONS MENU #################################

resume_img = pygame.image.load("button/button_play.png").convert_alpha()
options_img = pygame.image.load("button/button_option.png").convert_alpha()
quit_img = pygame.image.load("button/button_quit.png").convert_alpha()
video_img = pygame.image.load("button/button_video.png").convert_alpha()
audio_img = pygame.image.load("button/button_audio.png").convert_alpha()
keys_img = pygame.image.load("button/button_keys.png").convert_alpha()
back_img = pygame.image.load("button/button_back.png").convert_alpha()

resume_img = pygame.transform.scale(resume_img, (200, 100))
options_img = pygame.transform.scale(options_img, (200, 100))
quit_img = pygame.transform.scale(quit_img, (200, 100))
video_img = pygame.transform.scale(video_img, (200, 100))
audio_img = pygame.transform.scale(audio_img, (200, 100))
keys_img = pygame.transform.scale(keys_img, (200, 100))
back_img = pygame.transform.scale(back_img, (200, 100))

resume_button = button.Button(304, 125, resume_img, 1)
options_button = button.Button(297, 250, options_img, 1)
quit_button = button.Button(336, 375, quit_img, 1)
video_button = button.Button(226, 75, video_img, 1)
audio_button = button.Button(225, 200, audio_img, 1)
keys_button = button.Button(246, 325, keys_img, 1)
back_button = button.Button(332, 450, back_img, 1)

def draw_text(text, font, text_col, x, y):
  img = font.render(text, True, text_col)
  screen.blit(img, (x, y))


################################## BOUCLE PRINCIPALE ###################################

run = True
while run:

  screen.fill((52, 78, 91))


  if game_paused == True:
    if menu_state == "main":
      if resume_button.draw(screen):
        game_paused = False
      if options_button.draw(screen):
        menu_state = "options"
      if quit_button.draw(screen):
        run = False
    if menu_state == "options":
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