import pygame

class Button:
    def __init__(self, x, y, image, scale):
        """
        Initialise un bouton avec une image, une position et une échelle données.

        Arguments :
        x, y -- coordonnées du coin supérieur gauche du bouton.
        image -- image du bouton.
        scale -- échelle à laquelle l'image du bouton doit être redimensionnée.
        """
        self.original_image = image  # Garde une copie de l'image originale
        width = image.get_width()  # Largeur originale de l'image
        height = image.get_height()  # Hauteur originale de l'image
        # Redimensionne l'image selon l'échelle donnée
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        # Crée un rectangle autour de l'image pour gérer les collisions et la position
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)  # Place le coin supérieur gauche du rectangle aux coordonnées (x, y)
        self.clicked = False  # Indique si le bouton a été cliqué

    def draw(self, surface):
        """
        Dessine le bouton sur la surface donnée et vérifie s'il a été cliqué.

        Arguments :
        surface -- surface sur laquelle le bouton doit être dessiné.

        Retourne :
        True si le bouton a été cliqué, False sinon.
        """
        action = False  # Action indiquant si le bouton a été cliqué

        pos = pygame.mouse.get_pos()  # Obtient la position actuelle de la souris

        # Vérifie si la souris est sur le bouton et si un clic gauche est effectué
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True  # Marque le bouton comme cliqué
                action = True  # Indique qu'une action a eu lieu

        # Réinitialise l'état cliqué lorsque le bouton gauche de la souris est relâché
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # Dessine l'image du bouton sur la surface
        surface.blit(self.image, (self.rect.x, self.rect.y))

        return action  # Retourne si le bouton a été cliqué

    def resize_image(self, scale):
        """
        Redimensionne l'image du bouton selon l'échelle donnée.

        Arguments :
        scale -- nouvelle échelle à appliquer à l'image du bouton.
        """
        width = self.original_image.get_width()  # Largeur originale de l'image
        height = self.original_image.get_height()  # Hauteur originale de l'image
        # Redimensionne l'image selon la nouvelle échelle
        self.image = pygame.transform.scale(self.original_image, (int(width * scale), int(height * scale)))
