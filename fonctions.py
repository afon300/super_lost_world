import os
import pygame
import sys

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def resolutions_ecran():
    x = 1 #résolution de base de 1240px : 720px (720p / HD)
    if x == 0:
        WINDOW_WIDTH = 800
        WINDOW_HEIGHT = 600
    if x == 1:
        WINDOW_WIDTH = 1240
        WINDOW_HEIGHT = 720
    if x == 2:
        WINDOW_WIDTH = 1920
        WINDOW_HEIGHT = 1080
    if x == 3:
        WINDOW_WIDTH = 2560
        WINDOW_HEIGHT = 1440
    if x == 4:
        WINDOW_WIDTH = 3840
        WINDOW_HEIGHT = 2160
    WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)
    return WINDOW_SIZE, WINDOW_HEIGHT, WINDOW_WIDTH


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def main_menu(BLACK, WHITE, font, screen):
    while True:
        screen.fill(BLACK)
        draw_text('Menu principal', font, WHITE, screen, 20, 20)

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(50, 100, 200, 50)
        button_2 = pygame.Rect(50, 200, 200, 50)
        button_3 = pygame.Rect(50, 300, 200, 50)

        pygame.draw.rect(screen, WHITE, button_1)
        pygame.draw.rect(screen, WHITE, button_2)
        pygame.draw.rect(screen, WHITE, button_3)

        draw_text('Jouer', font, BLACK, screen, 70, 110)
        draw_text('Option', font, BLACK, screen, 70, 210)
        draw_text('Quitter', font, BLACK, screen, 70, 310)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_1.collidepoint((mx, my)):
                    print('Jouer')
                if button_2.collidepoint((mx, my)):
                    print('Option')
                if button_3.collidepoint((mx, my)):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
        
def load_and_scale_image(file, size):
    image = pygame.image.load(file).convert_alpha()
    return pygame.transform.scale(image, size)