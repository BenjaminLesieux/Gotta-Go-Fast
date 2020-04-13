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
        self.game = game
        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
        self.value = pygame.Rect(self.x, self.y, width, height)

    def collides(self):
        if self.value.collidepoint(self.mouse_x, self.mouse_y):
            return True

        return False

    def draw_text(self, text, font, color, surface, x, y):
        self.game.draw_text(text, font, color, surface, x, y)

    def render(self, highlight):
        if highlight == self.title:
            pygame.draw.rect(self.game.mode, (109, 7, 26), self.value)
        else:
            pygame.draw.rect(self.game.mode, (255, 0, 0), self.value)

        self.draw_text(self.title, self.game.font, (109, 7, 26), self.game.mode, self.x, self.y)
