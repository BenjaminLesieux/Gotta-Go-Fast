import pygame
import sys
from gui.gui import Gui
from entities.player import Player
from entities.platform import Platform
from gui.button import Button
from gui.final_screen import FinalScreen

class GameMenu(Gui):

    def __init__(self, game):
        self.play = game.play
        self.game = game
        self.end_menu = FinalScreen(game)
        self.play.set_end_menu(end_menu=self.end_menu)

    def loop(self):

        self.play.render_background()
        self.play.register_platform_by_file(self.game.level.location)

        player = Player([100, 500])

        self.play.register_player(player)
        self.game.player.add(player)
        self.play.render_lava()

        self.end_menu.activated = False

        playing = True

        while playing:

            player.dead = "None"

            if self.end_menu.is_activated():
                self.end_menu.process()
                playing = False
            else:
                self.game.mode.blit(self.game.bg, [0, 0])
                self.game.draw_text(self.game.level.name, self.game.font, (109, 0, 0), self.game.mode, 20, 20)
                self.play.process()

                for event in pygame.event.get():
                    if event.type == pygame.K_KP_ENTER:
                        break
                    if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                        sys.exit(0)  # si echap ou bouton croix, quitter

                pygame.display.update()
