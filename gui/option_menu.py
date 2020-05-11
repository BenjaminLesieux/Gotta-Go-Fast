from gui.button import Button
from gui.gui import Gui
import pygame
import sys


class OptionMenu(Gui):

    def __init__(self, ggf):
        self.title = "Options"
        self.ggf = ggf
        self.back = None

    def loop(self):
        running = True

        while running:
            self.ggf.mode.blit(self.ggf.bg, [0, 0])
            self.draw_text("Options", self.ggf.font, (255, 255, 255), self.ggf.mode, 500, 10)

            self.back = Button("Retour", 450, 70, (450, 100), self.ggf)

            click = False
            mouse_x, mouse_y = pygame.mouse.get_pos()
            highlight = "None"

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True

            if self.back.collides():
                highlight = "Retour"

                if click:
                    running = False

            self.back.render(highlight)

            pygame.display.update()
            self.ggf.clock.tick(60)
