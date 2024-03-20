import pygame

class Button():
    def __init__(self, x, y, image, scale):
        self.original_image = image
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self, surface):
        action = False

        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        surface.blit(self.image, (self.rect.x, self.rect.y))

        return action

    def resize_image(self, scale):
        width = self.original_image.get_width()
        height = self.original_image.get_height()
        self.image = pygame.transform.scale(self.original_image, (int(width * scale), int(height * scale)))