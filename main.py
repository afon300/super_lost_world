import pygame
from fonctions import *

pygame.init()


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
WINDOW_WIDTH = 1920
WINDOW_HEIGHT = 1080
WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)

screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Accepter des entrées en Pygame")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Taille de la fenêtre
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Menu de sélection")
font = pygame.font.Font(None, 36)

main_menu(BLACK, WHITE, font, screen)