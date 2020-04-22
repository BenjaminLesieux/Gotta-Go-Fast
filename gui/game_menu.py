import pygame
import sys
from gui.gui import Gui
from entities.player import Player
from entities.platform import Platform
from gui.button import Button


class GameMenu(Gui):

    def __init__(self, game):
        self.play = game.play
        self.game = game

    def loop(self):
        self.play.register_platform_by_file(self.game.level.location)
        self.play.register_player(Player([100, 600]))
        self.play.render_lava()

        while True:
            self.game.mode.blit(self.game.bg, [0, 0])
            self.game.draw_text(self.game.level.name, self.game.font, (255, 255, 255), self.game.mode, 20, 20)

            self.play.process()

            for event in pygame.event.get():
                if event.type == pygame.K_KP_ENTER:
                    break
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    self.play.register_platform(self.game.level.location, mouse_pos, False)
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    sys.exit(0)  # si echap ou bouton croix, quitter

            pygame.display.update()
            self.game.clock.tick(60)
