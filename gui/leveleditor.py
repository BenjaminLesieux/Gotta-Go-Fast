import pygame
import sys
from game.background import *

class LevelEditor:

    def __init__(self, level, game, mode, level_selector):

        self.level = level
        self.game = game
        self.level_selector = level_selector
        self.mode = mode
        self.bg = None

    def process(self):
               
        pro = True
        self.game.register_platform_by_file(self.level.location)
        self.render_background()

        while pro:
            
            self.bg.draw(self.mode)
            for plat in self.game.platforms:
                if plat.is_mobile():
                    plat.move()
                plat.draw(self.mode)

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if event.button == 1:
                        self.game.register_platform(self.level.location, mouse_pos, False, self.bg.decalage)
                    elif event.button == 3:
                        self.game.register_platform(self.level.location, mouse_pos, True, self.bg.decalage)
                elif event.type == pygame.QUIT:
                    pro = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.bg.defil()
                        if self.bg.count < self.bg.n_screen:
                            for plat in self.game.platforms:
                                plat.move_y(self.bg.delta_y)

            pygame.display.update()
            self.game.screen.clock.tick(60)

        self.level_selector.selected_level = None
        self.game.level = None

    def render_background(self):
        self.bg = Background()
        self.bg.surface = self.mode

    