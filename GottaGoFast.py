import pygame
import sys
from game.Game import Game
from gui.levelselector import LevelSelector
from gui.game_menu import GameMenu
from gui.option_menu import OptionMenu
from gui.button import Button

class GGf:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Gotta go fast")
        self.mode = pygame.display.set_mode((1280, 720))
        self.font = pygame.font.SysFont(None, 100)
        self.clock = pygame.time.Clock()
        self.bg = pygame.image.load("images/back.png").convert_alpha()
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
        # pygame.mixer.music.load('pioneer-to-the-falls.mp3')
        # pygame.mixer.music.set_volume(0.5)
        # pygame.mixer.music.play(-1)

        self.level_selector.propose_levels()

        while True:

            self.mode.blit(self.bg, [0, 0])
            self.draw_text("Gotta go fast", self.font, (109, 7, 26), self.mode, 430, 10)

            play = Button("Jouer", 450, 70, (430, 300), self)
            rules = Button("Règles", 450, 70, (430, 400), self)
            editor = Button("Editeur", 450, 70, (430, 500), self)
            highlight = "None"
            click = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True

            if play.collides():
                highlight = play.title
                if click:

                    while not self.level_selector.has_selected_level():
                        self.level_selector.process()

            elif rules.collides():
                highlight = rules.title
                if click:
                    self.option_menu.loop()

            elif editor.collides():
                highlight = editor.title
                if click:
                    pass

            play.render(highlight)
            rules.render(highlight)
            editor.render(highlight)

            pygame.display.update()
            self.clock.tick(60)

    def level_maker(self):
        pass

ggf = GGf()
