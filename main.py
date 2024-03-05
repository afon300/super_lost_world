import pygame
from fonctions import *

pygame.init()

WINDOW_SIZE = resolutions_ecran()
# screen = pygame.display.set_mode(WINDOW_SIZE, pygame.FULLSCREEN)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Accepter des entrées en Pygame")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
pygame.display.set_caption("Menu de sélection")
font = pygame.font.Font(None, 36)

main_menu(BLACK, WHITE, font, screen)