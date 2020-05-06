import pygame
import sys


class LevelEditor:

    def __init__(self, level, game, mode, level_selector):

        self.level = level
        self.game = game
        self.level_selector = level_selector
        self.mode = mode
        self.bg = pygame.image.load("images/back.png")

    def process(self):

        pro = True
        self.game.register_platform_by_file(self.level.location)

        while pro:
            self.mode.blit(self.bg, [0, 0])
            self.game.render_background()
            for plat in self.game.platforms:
                if plat.is_mobile():
                    plat.move()
                plat.draw(self.mode)

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if event.button == 1:
                        self.game.register_platform(self.level.location, mouse_pos, False)
                    elif event.button == 3:
                        self.game.register_platform(self.level.location, mouse_pos, True)
                if event.type == pygame.QUIT:
                    pro = False

            pygame.display.update()
            self.game.screen.clock.tick(60)

        self.level_selector.selected_level = None

        while not self.level_selector.has_selected_level():
            self.level_selector.process()
