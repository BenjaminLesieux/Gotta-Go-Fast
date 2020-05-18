import pygame
import sys
from game.background import *
from gui.button import Button

class LevelEditor:

    def __init__(self, level, game_handler, mode, level_selector):

        self.level = level
        self.game_handler = game_handler
        self.level_selector = level_selector
        self.mode = mode
        self.bg = None
        self.p_type = 1  # 1 type 1 - 2 type 2 - 3 type 3
        self.p1_button = None
        self.p2_button = None
        self.p3_button = None

    def process(self):
        print("Editing levels")
        pro = True
        self.game_handler.register_platform_by_file(self.level.location)
        self.render_background()

        click = False

        while pro:

            self.bg.draw(self.mode)

            self.p1_button = Button("Type 1", 200, 200, (1100, 100),
                                    self.game_handler.ggf).custom_image("images/plateforme 1.png", (40, 40))
            self.p2_button = Button("Type 2", 200, 200, (1100, 200),
                                    self.game_handler.ggf).custom_image("images/plateforme 2.png", (40, 40))
            self.p3_button = Button("Type 3", 200, 200, (1100, 300),
                                    self.game_handler.ggf).custom_image("images/plateforme 3.png", (40, 40))

            place = True

            if self.p1_button.collides():
                place = False
                if click: self.p_type = 1
            elif self.p2_button.collides():
                place = False
                if click: self.p_type = 2
            elif self.p3_button.collides():
                place = False
                if click: self.p_type = 3

            click = False

            for plat in self.game_handler.platforms:
                if plat.is_mobile():
                    plat.move()
                plat.draw(self.mode)

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if event.button == 1:
                        click = True
                        if place:
                            self.game_handler.register_platform(self.level.location, mouse_pos, False, self.bg.decalage,
                                                                self.p_type)
                    elif event.button == 3:
                        click = True
                        if place:
                            self.game_handler.register_platform(self.level.location, mouse_pos, True, self.bg.decalage,
                                                                self.p_type)
                elif event.type == pygame.QUIT:
                    pro = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.bg.defil()
                        if self.bg.count < self.bg.n_screen:
                            for plat in self.game_handler.platforms:
                                plat.move_y(self.bg.delta_y)

            self.p1_button.render("")
            self.p2_button.render("")
            self.p3_button.render("")
            pygame.display.update()
            self.game_handler.ggf.clock.tick(60)

        self.level_selector.selected_level = None
        self.game_handler.level = None
        self.game_handler.platforms = []

    def render_background(self):
        self.bg = Background()
        self.bg.surface = self.mode

    