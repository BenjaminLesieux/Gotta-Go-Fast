from gui.button import Button
from gui.gui import Gui
import pygame
import sys


class OptionMenu(Gui):

    def __init__(self, ggf):
        self.title = "Options"
        self.ggf = ggf
        self.back = None
        self.le_help = None
        self.game_help = None

    def loop(self):
        running = True

        while running:
            self.ggf.mode.blit(self.ggf.bg, [0, 0])
            self.draw_text("Options", self.ggf.font, (255, 255, 255), self.ggf.mode, 500, 10)

            self.back = Button("Retour", 450, 100, (450, 100), self.ggf)
            self.le_help = Button("Aide - Level Editor", 450, 100, (450, 200), self.ggf)
            self.game_help = Button("Aide - Jeu", 450, 100, (450, 300), self.ggf)

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
            if self.le_help.collides():
                self.le_help.custom_image("images/helple.png", (200, 200))
                self.le_help.move_to((800, 200))
            if self.game_help.collides():
                pass

            self.back.render(highlight)
            self.le_help.render(highlight)
            self.game_help.render(highlight)

            pygame.display.update()
            self.ggf.clock.tick(60)
