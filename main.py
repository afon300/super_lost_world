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

#load button images
button_play = os.path.join(os.getcwd(), "button", "button_play.png")
button_option = os.path.join(os.getcwd(), "button", "button_option.png")
button_quit = os.path.join(os.getcwd(), "button", "button_play.png")
button_video = os.path.join(os.getcwd(), "button", "button_play.png")
button_audio = os.path.join(os.getcwd(), "button", "button_play.png")
button_keys = os.path.join(os.getcwd(), "button", "button_play.png")
button_back = os.path.join(os.getcwd(), "button", "button_play.png")

resume_img = pygame.image.load(button_play).convert_alpha()
options_img = pygame.image.load(button_option).convert_alpha()
quit_img = pygame.image.load(button_quit).convert_alpha()
video_img = pygame.image.load(button_video).convert_alpha()
audio_img = pygame.image.load(button_audio).convert_alpha()
keys_img = pygame.image.load(button_keys).convert_alpha()
back_img = pygame.image.load(button_back).convert_alpha()
print(resume_img)

#create button instances
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

#game loop
run = True
while run:

  screen.fill((52, 78, 91))

  #check if game is paused
  if game_paused == True:
    #check menu state
    if menu_state == "main":
      #draw pause screen buttons
      if resume_button.draw(screen):
        game_paused = False
      if options_button.draw(screen):
        menu_state = "options"
      if quit_button.draw(screen):
        run = False
    #check if the options menu is open
    if menu_state == "options":
      #draw the different options buttons
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