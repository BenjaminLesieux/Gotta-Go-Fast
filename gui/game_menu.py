import pygame
import sys
from gui.gui import Gui
from entities.player import Player
from entities.platform import Platform
from gui.button import Button
from gui.final_screen import FinalScreen

class GameMenu(Gui):

    def __init__(self, ggf):
        self.game_handler = ggf.play
        self.ggf = ggf
        self.end_menu = FinalScreen(ggf)
        self.game_handler.set_end_menu(end_menu=self.end_menu)
        self.player = None

    def loop(self):

        self.load()

        self.end_menu.activated = False
        self.end_menu.game = True

        while self.end_menu.game:
            self.player.dead = "None"

            if self.end_menu.is_activated():
                self.end_menu.process()
                if self.end_menu.game:
                    self.load()

            elif self.end_menu.game:
                self.ggf.mode.blit(self.ggf.bg, [0, 0])
                self.ggf.draw_text(self.ggf.level.name, self.ggf.font, (200, 0, 0), self.ggf.mode, 20, 20)
                self.game_handler.process()

                for event in pygame.event.get():
                    if event.type == pygame.K_KP_ENTER:
                        break
                    if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                        sys.exit(0)  # si echap ou bouton croix, quitter

                pygame.display.update()

    def load(self):

        self.game_handler.render_background()
        self.game_handler.platforms = []
        self.game_handler.register_platform_by_file(self.ggf.level.location)

        self.player = Player([100, 500])

        self.game_handler.register_player(self.player)
        self.ggf.player.add(self.player)
        self.game_handler.render_lava()
        