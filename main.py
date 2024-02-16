import pygame

pygame.init()

pygame.display.set_caption("yeet")
pygame.display.set_mode((500,300))
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Corrected the event type comparison
            running = False
            pygame.quit()
            print("fermeture du jeu")
