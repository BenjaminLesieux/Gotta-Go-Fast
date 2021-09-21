import pygame
import sys


class Button:

    def __init__(self, title, width, height, position, ggf):
        self.title = title
        self.width = width
        self.height = height
        self.position = position
        self.x = position[0]
        self.y = position[1]
        self.image = pygame.image.load("images/menu button.png").convert_alpha()
        self.ggf = ggf
        (self.mouse_x, self.mouse_y) = pygame.mouse.get_pos()
        self.value = self.image.get_rect(topleft=(self.x, self.y))

    """
    :desc - Si la souris est sûr le bouton
    :return - True si oui False sinon
    :type - boolean
    """

    def collides(self):
        if self.x < self.mouse_x < self.x + self.image.get_width() and self.y < self.mouse_y < self.y + self.image.get_height():
            return True
        return False

    """
    desc - Change la position d'un bouton
    """

    def move_to(self, position):
        self.x = position[0]
        self.y = position[1]

    """
    :param link - le lien de l'image
    :param dimensions - les nouvelles dimensions
    :return self
    :type Button
    """

    def custom_image(self, link, dimensions):
        self.image = pygame.image.load(link).convert_alpha()
        self.title = ""

        if dimensions is not None:
            self.image = pygame.transform.scale(self.image, dimensions)

        return self

    """
    :param text, font, color 
    :param surface - Surface sur laquelle on dessine le texte
    :param x,y - la position
    """

    def draw_text(self, text, font, color, surface, x, y):
        self.ggf.draw_text(text, font, color, surface, x, y)

    """
    :param highlight - hover effect
    """

    def render(self, highlight):

        self.ggf.mode.blit(self.image, (self.x, self.y))

        if highlight == self.title:
            self.draw_text(self.title, pygame.font.Font("images/Fipps-Regular.otf", 26), (109, 0, 0), self.ggf.mode,
                           self.x + 5, self.y)

        else:
            self.draw_text(self.title, pygame.font.Font("images/Fipps-Regular.otf", 26), (0, 0, 0), self.ggf.mode,
                           self.x + 5, self.y)
