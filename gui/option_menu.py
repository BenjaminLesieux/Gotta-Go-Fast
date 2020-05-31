from gui.button import Button
from gui.gui import Gui
import pygame
import sys

pygame.mixer.init(44100, -16,2,2048)
clic = pygame.mixer.Sound("images/clic.ogg")

class OptionMenu(Gui):

    def __init__(self, ggf):
        self.title = "Options"
        self.ggf = ggf
        self.back = None
        self.le_help = None
        self.game_help = None

    def loop(self):
        running = True

        while running:
            self.ggf.mode.blit(self.ggf.bg, [0, 0])
            self.draw_text("Options", self.ggf.font, (255, 255, 255), self.ggf.mode, 530, 10)

            self.back = Button("Retour", 450, 100, (450, 200), self.ggf)
            self.le_help = Button("Aide - Level Editor", 450, 100, (450, 300), self.ggf)
            self.game_help = Button("Aide - Jeu", 450, 100, (450, 400), self.ggf)

            lhelp = False
            ghelp = False

            click = False
            highlight = "None"

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True
                        clic.play()

            if self.back.collides():
                highlight = "Retour"

                if click:
                    running = False
            if self.le_help.collides():
                lhelp = True
                self.le_help.custom_image("images/leveleditorhelp.png", (700, 700))
                self.le_help.move_to((300, 95))
            if self.game_help.collides():
                ghelp = True
                self.game_help.custom_image("images/gamehelp.png", (700, 700))
                self.game_help.move_to((300, 150))

            self.back.render(highlight)

            if not ghelp and not lhelp:
                self.le_help.render(highlight)
                self.game_help.render(highlight)
            elif ghelp:
                self.game_help.render(highlight)
            elif lhelp:
                self.le_help.render(highlight)

            pygame.display.update()
