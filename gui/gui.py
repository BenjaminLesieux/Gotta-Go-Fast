import pygame
from gui.button import Button


class Gui:

    def __int__(self, title, main):
        self.title = title
        self.font = pygame.font.SysFont(None, 100)
        self.draw_text(self.title, self.font, (255, 0, 0), main.mode, (430, 10))
        self.buttons = []

    def draw_text(self, text, font, color, surface, x, y):
        textobj = font.render(text, 1, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobj, textrect)

    """ A définir dans les classe héritantes"""

    def back_page(self):
        pass

    """ A définir dans les classe héritantes """

    def loop(self):
        pass

    def add_button(self, title, position, highlight_color, basic_color, function):
        button = Button(430, 70, position, function)
        self.buttons.append(button)
