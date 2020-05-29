import pygame
import sys
from gui.button import Button
from gui.leveleditor import LevelEditor
from gui.text_box import TextBox


class LevelSelector:

    def __init__(self, ggf):
        self.ggf = ggf
        self.mode = ggf.mode
        self.levels = []
        self.selected_level = None
        self.ggf.level = self.selected_level
        self.bg = self.ggf.bg
        self.buttons = []
        self.box = TextBox(self.mode, 430, 600, 400, 50, 'Entrez le nom du niveau...')
        self.new_level_name = None
        self.text = self.box.active
        self.new_level = False

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
        self.ggf.draw_text("Select Level", self.ggf.font, (255, 255, 255), self.mode, 420, 10)

        i = 0

        for level in self.levels:
            b = Button(level.name, 450, 70, (430, 250 + i), self.ggf)
            edit = Button("", 40, 40, (900, 255 + i), self.ggf).custom_image("images/Edit.png", (50, 50))
            delete = Button("", 40, 40, (350, 260 + i), self.ggf).custom_image("images/RedCross.png", (50, 50))
            self.buttons.append((b, level, [430, 200 + i], edit, delete))
            i += 100

        add = Button("", 40, 40, (630, 250 + i), self.ggf).custom_image("images/AddCross.png", (50, 50))

        click = False
        highlight = "None"


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
                    self.box.verifClick(pygame.mouse.get_pos())
            if event.type == pygame.KEYDOWN and self.text:
                if self.box.active:
                    if event.key == pygame.K_LSHIFT:
                        self.box.caps = True
                    self.box.addText(event.key)
                    self.new_level_name = self.box.getText()
                    self.text = self.box.active
            if event.type == pygame.KEYUP and event.key == pygame.K_LSHIFT and self.text:
                self.box.caps = False

        self.new_level = not self.text and self.new_level_name is not None and self.new_level_name != ""

        for button in self.buttons:
            if button[0].collides():
                highlight = button[1].name
                if click:
                    self.selected_level = button[1]
                    self.ggf.level = self.selected_level
                    self.ggf.game_menu.loop(self.selected_level.name)
            if button[3].collides():
                highlight = button[1].name
                if click:
                    self.selected_level = button[1]
                    self.ggf.level = self.selected_level
                    LevelEditor(button[1], self.ggf.game_menu.game_handler, self.mode, self).process()
            if button[4].collides() and not self.has_selected_level():
                highlight = button[1].name
                if click and len(self.levels) > 1:
                    self.remove_level(button[1])
            if add.collides():

                if len(self.levels) == 4:
                    self.ggf.draw_text("Trop de niveaux",
                                       self.ggf.font, (255, 9, 28), self.mode, 350, 600)
                    break

                highlight = ""
                if click:
                    if self.new_level is True:
                        level = Level(self.new_level_name)
                        self.register_level(level)
                        self.levels.append(level)
                        self.box.text = ""
                        self.new_level_name = ""
                        self.new_level = False
                        break
                    self.text = True if not self.new_level else False

            button[0].render(highlight)
            button[3].render(highlight)
            button[4].render(highlight)
            add.render(highlight)

            if self.text:
                self.box.draw(self.mode)

        pygame.display.update()

    def remove_level(self, level):
        self.levels.remove(level)
        f = open("levels.txt", "w")

        for l in self.levels:
            f.write(l.name + "\n")

class Level:

    def __init__(self, name):
        self.name = name
        self.location = name
