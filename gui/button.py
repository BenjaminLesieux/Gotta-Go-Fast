import pygame
import sys


class Button:

    def __init__(self, title, width, height, position, game):
        self.title = title
        self.width = width
        self.height = height
        self.position = position
        self.x = position[0]
        self.y = position[1]
        self.image = pygame.image.load("images/menu button.png").convert_alpha()
        self.game = game
        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
        self.value = self.image.get_rect(topleft=(self.x, self.y))

    def collides(self):
        if self.value.collidepoint(self.mouse_x, self.mouse_y):
            return True

        return False

    def custom_image(self, link, dimensions):
        self.image = pygame.image.load(link).convert_alpha()

        if dimensions is not None:
            self.image = pygame.transform.scale(self.image, dimensions)

        return self

    def draw_text(self, text, font, color, surface, x, y):
        self.game.draw_text(text, font, color, surface, x, y)

    def render(self, highlight):

        self.game.mode.blit(self.image, (self.x, self.y))

        if highlight == self.title:
            self.draw_text(self.title, pygame.font.Font("images/Fipps-Regular.otf", 26), (109, 0, 0), self.game.mode,
                           self.x + 5, self.y)

        else:
            self.draw_text(self.title, pygame.font.Font("images/Fipps-Regular.otf", 26), (0, 0, 0), self.game.mode,
                           self.x + 5, self.y)
