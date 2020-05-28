import pygame
import sys
from gui.button import Button


class FinalScreen:

    def __init__(self, ggf):
        self.ggf = ggf
        self.activated = False
        self.menu = None
        self.leave = None
        self.retry = None
        self.game = False
        self.state = "None"

    def is_activated(self):
        return self.activated

    def process(self):
        running = True
        click = False

        while running:

            highlight = "None"

            self.ggf.mode.blit(self.ggf.bg, [0, 0])
            if self.state == "Victoire":
                self.ggf.mode.blit(self.ggf.win, [448, 10])
            elif self.state == "Game over":
                self.ggf.mode.blit(self.ggf.lose, [448, 10])

            self.retry = Button("Réessayer", 450, 70, (430, 350), self.ggf)
            self.menu = Button("Menu", 450, 70, (430, 450), self.ggf)
            self.leave = Button("Quitter", 450, 70, (430, 550), self.ggf)

            if self.menu.collides():
                highlight = "Menu"
                if click:
                    running = False
                    self.activated = False
                    self.game = False
                    
            elif self.retry.collides():
                highlight = "Réessayer"
                if click:
                    self.activated = False
                    self.game = True
                    running = False

            elif self.leave.collides():
                highlight = "Quitter"
                if click:
                    sys.exit(0)
            else:
                click = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        click = True

            self.retry.render(highlight)
            self.menu.render(highlight)
            self.leave.render(highlight)
            pygame.display.update()
