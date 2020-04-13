import pygame
import sys


class LevelSelector:

    def __init__(self, game):
        self.game = game
        self.mode = game.mode
        self.levels = []
        self.selected_level = None
        self.game.level = self.selected_level
        self.bg = self.game.bg
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

        self.mode.blit(self.bg, [0, 0])
        self.game.draw_text("Select Level", self.game.font, (255, 255, 255), self.mode, 450, 10)

        i = 0

        for level in self.levels:
            self.buttons.append((pygame.Rect(430, 300 + i, 450, 70), level, [430, 300 + i]))
            i += 80

        click = False
        mouse_x, mouse_y = pygame.mouse.get_pos()
        highlight = "None"

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        for button in self.buttons:
            if button[0].collidepoint((mouse_x, mouse_y)):
                highlight = button[1].name
                if click:
                    self.selected_level = button[1]
                    self.game.level = self.selected_level
                    self.game.game_menu.loop()

            if highlight == button[1].name:
                pygame.draw.rect(self.mode, (109, 7, 26), button[0])
            if highlight != button[1].name:
                pygame.draw.rect(self.mode, (255, 0, 0), button[0])

            x = button[2][0] + 50
            y = button[2][1]

            self.game.draw_text(button[1].name, self.game.font, (100, 7, 26), self.mode, x, y)

        pygame.display.update()
        self.game.clock.tick(25)


class Level:

    def __init__(self, name):
        self.name = name
        self.location = name + ".txt"


class LevelEditor:

    def __init(self, name, game):
        self.name = name
        self.game = game
        self.mode = self.game.mode

    def process(self):
        pass
