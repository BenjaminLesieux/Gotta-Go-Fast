import pygame
import sys
from game.game_handler import Game
from gui.levelselector import LevelSelector
from gui.game_menu import GameMenu
from gui.option_menu import OptionMenu
from gui.button import Button
from gui.text_box import TextBox
from pygame.locals import *


class GGf:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Gotta go fast")
        pygame.display.set_icon(pygame.image.load("images/logo.png"))
        self.py_sprite = pygame.sprite.Group()
        self.player = pygame.sprite.Group()
        self.mode = pygame.display.set_mode((1280, 720))
        self.font = pygame.font.Font("images/Fipps-Regular.otf", 45)
        self.clock = pygame.time.Clock()
        self.bg = pygame.image.load("images/back.png")
        self.play = Game(self)
        self.level = None
        self.level_selector = LevelSelector(self)
        self.game_menu = GameMenu(self)
        self.option_menu = OptionMenu(self)
        self.menu()

    def draw_text(self, text, font, color, surface, x, y):
        textobj = font.render(text, 1, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobj, textrect)

    def menu(self):
        pygame.mixer.music.load('images/idée-menu-non-mixée.ogg')
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(-1)

        self.level_selector.propose_levels()
        # box = TextBox(self.mode, 100, 100, 400, 50, 'enter text here...')
        while True:

            self.mode.blit(self.bg, [0, 0])
            self.draw_text("Gotta go fast", self.font, (109, 7, 26), self.mode, 430, 10)
            self.level_selector.selected_level = None
            self.play.platforms = []

            play = Button("Jouer", 450, 70, (430, 300), self)
            rules = Button("Règles", 450, 70, (430, 400), self)
            highlight = "None"
            click = False

            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    #box.verifClick(pygame.mouse.get_pos())
                    if event.button == 1:
                        click = True
                """if event.type == pygame.KEYDOWN:
                    if box.active:
                        if event.key == K_LSHIFT:
                            box.caps = True
                        box.addText(event.key)
                if  event.type == pygame.KEYUP and event.key == K_LSHIFT and box.active:
                    box.caps = False
            box.draw(self.mode)"""
            if play.collides():
                highlight = play.title
                if click:

                    while not self.level_selector.has_selected_level():
                        self.level_selector.process()

            elif rules.collides():
                highlight = rules.title
                if click:
                    self.option_menu.loop()

            play.render(highlight)
            rules.render(highlight)

            pygame.display.update()
            self.clock.tick(60)

    def level_maker(self):
        pass

ggf = GGf()