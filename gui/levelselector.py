import pygame
import sys
from gui.button import Button
from gui.leveleditor import LevelEditor


class LevelSelector:

    def __init__(self, ggf):
        self.ggf = ggf
        self.mode = ggf.mode
        self.levels = []
        self.selected_level = None
        self.ggf.level = self.selected_level
        self.bg = self.ggf.bg
        self.buttons = []

    def register_level(self, level):
        registered = open("levels.txt", "a+")
        registered.write(level.name + "\n")

    def propose_levels(self):
        registered = open("levels.txt", "r")

        for line in registered.readlines():
            self.levels.append(Level(line[0:len(line) - 1]))

    def has_selected_level(self):
        return self.selected_level is not None

    def process(self):

        self.buttons.clear()
        self.mode.blit(self.bg, [0, 0])
        self.ggf.draw_text("Select Level", self.ggf.font, (255, 255, 255), self.mode, 450, 10)

        i = 0

        for level in self.levels:
            b = Button(level.name, 450, 70, (430, 300 + i), self.ggf)
            edit = Button("", 40, 40, (900, 300 + i), self.ggf).custom_image("images/ediiit.png", (50, 50))
            self.buttons.append((b, level, [430, 300 + i], edit))
            i += 80

        click = False
        highlight = "None"

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        for button in self.buttons:
            if button[0].collides():
                highlight = button[1].name
                if click:
                    self.selected_level = button[1]
                    self.ggf.level = self.selected_level
                    self.ggf.game_menu.loop()
            if button[3].collides():
                highlight = button[1].name
                if click:
                    self.selected_level = button[1]
                    self.ggf.level = self.selected_level
                    LevelEditor(button[1], self.ggf.game_menu.game_handler, self.mode, self).process()
                    print("yey")

            button[0].render(highlight)
            button[3].render(highlight)

        pygame.display.update()


class Level:

    def __init__(self, name):
        self.name = name
        self.location = name + ".txt"


