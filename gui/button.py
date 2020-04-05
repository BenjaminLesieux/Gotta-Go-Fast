import pygame
import sys


class Button:

    def __init__(self, width, height, position, function):
        self.width = width
        self.height = height
        self.position = position
        self.function = function
        self.x = position[0]
        self.y = position[1]
        self.mouse_pos = pygame.mouse.get_pos()
        self.value = pygame.Rect(430, 300, width, height)

    def on_click(self, function):

        click = False

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if self.value.collidepoint(self.mouse_pos[0], self.mouse_pos[1]):
                if click:
                    function()

    def render(self):
        pass
