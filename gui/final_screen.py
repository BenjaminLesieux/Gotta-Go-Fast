import pygame
import sys
from gui.button import Button


class FinalScreen:

    def __init__(self, ggf):
        self.ggf = ggf
        self.activated = False
        self.menu = None
        self.leave = None
        self.state = "None"

    def is_activated(self):
        return self.activated

    def process(self):
        running = True
        click = False
        choice = 0

        while running:

            highlight = "None"

            self.ggf.mode.blit(self.ggf.bg, [0, 0])
            self.ggf.draw_text(self.state, self.ggf.font, (255, 255, 255), self.ggf.mode, 500, 10)

            self.menu = Button("Menu", 450, 70, (430, 200), self.ggf)
            self.leave = Button("Quitter", 450, 70, (430, 300), self.ggf)

            if self.menu.collides():
                highlight = "Menu"
                if click:
                    running = False
                    self.activated = False

            elif self.leave.collides():
                highlight = "Quitter"
                if click:
                    sys.exit(0)
            else:
                click = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True

            self.menu.render(highlight)
            self.leave.render(highlight)
            pygame.display.update()
