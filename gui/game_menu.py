import pygame
import sys
from gui.gui import Gui
from entities.player import Player
from entities.platform import Platform
from gui.button import Button


class GameMenu(Gui):

    def __init__(self, level_title, main, game):
        super(level_title, main)
        self.play = game

    def loop(self):
        super().loop()

        self.play.add_sprite(Platform((500, 100), True, "images/plateforme 1 V2.png"))
        self.play.register_player(Player([100, 300]))

        while True:
            self.mode.blit(self.bg, [0, 0])
            self.draw_text('Level 1', self.font, (255, 255, 255), self.mode, 20, 20)

            self.play.process()

            for button in self.buttons:
                button.on_click()

            for event in pygame.event.get():
                if event.type == pygame.K_KP_ENTER:
                    break
                if event.type == pygame.QUIT:
                    sys.exit(0)

            pygame.display.update()
            self.clock.tick(30)
