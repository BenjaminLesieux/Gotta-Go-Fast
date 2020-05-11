import pygame
from gui.button import Button


class Gui:

    def __int__(self, name, ggf):
        self.title = name
        self.ggf = ggf
        self.font = pygame.font.SysFont(None, 100)
        self.draw_text(self.title, self.font, (255, 0, 0), self.ggf.mode, (430, 10))

    def draw_text(self, text, font, color, surface, x, y):
        textobj = font.render(text, 1, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobj, textrect)

    """ A définir dans les classe héritantes """

    def loop(self):
        pass
