import pygame
import sys
from game.game_handler import Game
from gui.levelselector import LevelSelector
from gui.game_menu import GameMenu
from gui.option_menu import OptionMenu
from gui.button import Button
from pygame.locals import *

pygame.mixer.init(44100, -16,2,2048)
clic = pygame.mixer.Sound("images/clic.ogg")

class GGf:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Gotta go fast")
        pygame.display.set_icon(pygame.image.load("images/logo.png"))
        self.title = pygame.image.load("images/Gotta Go Fast.png")
        self.py_sprite = pygame.sprite.Group()
        self.player = pygame.sprite.Group()
        self.mode = pygame.display.set_mode((1280, 720))
        self.font = pygame.font.Font("images/Fipps-Regular.otf", 45)
        self.font_title = pygame.font.Font("images/Fipps-Regular.otf", 70)
        self.clock = pygame.time.Clock()
        self.bg = pygame.image.load("images/GGf.jpg")
        self.win = pygame.transform.scale(pygame.image.load("images/You Win !.png"), (384, 216))
        self.lose = pygame.transform.scale(pygame.image.load("images/game over.png"), (384, 216))
        self.play = Game(self)
        self.level = None
        self.level_selector = LevelSelector(self)
        self.game_menu = GameMenu(self)
        self.option_menu = OptionMenu(self)
        self.timer = 0
        self.menu()

    def draw_text(self, text, font, color, surface, x, y):
        textobj = font.render(text, 1, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobj, textrect)

    def menu(self):
        pygame.mixer.music.load('images/idée-menu-non-mixée.ogg')
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.play(-1)

        self.level_selector.propose_levels()
        while True:

            self.mode.blit(self.bg, [0, 0])
            self.mode.blit(self.title, [30, 20])
            self.level_selector.selected_level = None
            self.play.platforms = []

            play = Button("Jouer", 450, 70, (430, 300), self)
            rules = Button("Règles", 450, 70, (430, 400), self)
            leave = Button("Quitter", 450, 70, (430, 500), self)

            highlight = "None"
            click = False

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit(0)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True
                        clic.play()
            if play.collides():
                highlight = play.title
                if click:
                    back = True
                    while not self.level_selector.has_selected_level() and back:
                        back = self.level_selector.process()

            elif rules.collides():
                highlight = rules.title
                if click:
                    self.option_menu.loop()

            elif leave.collides():
                highlight = leave.title
                if click:
                    pygame.quit()
                    sys.exit(0)

            play.render(highlight)
            rules.render(highlight)
            leave.render(highlight)

            pygame.display.update()
            self.clock.tick(60)


ggf = GGf()