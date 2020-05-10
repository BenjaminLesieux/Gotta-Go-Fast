from gui.button import Button
from gui.gui import Gui
from gui.levelselector import *
import pygame

class FinalScreen():

    def __init__(self, game):
        self.state = "None"
        self.game = game
        self.bg = None
        self.menu = None
        self.second = None
        self.leave = None

        self.levelselector = None
        self.menu = None
    
    def loop(self):

        running = True
        click = False
        choice = 0

        while running :

            highlight_m = "None"
            highlight_s = "None"
            highlight_l = "None"

            self.game.mode.blit(self.game.bg, [0, 0])
            # self.game.draw_text(self.state, self.game.font, (255, 255, 255), self.game.mode, 500, 10)

            self.menu = Button("Menu", 450, 70, (430, 400), self.game)
            self.second = Button("Sélection de niveau", 450, 70, (430, 200), self.game)
            self.leave = Button("Quitter", 450, 70, (430, 600), self.game)
            
            if self.menu.collides():
                highlight_m = "Menu"
                if click:
                    running = False

            elif self.second.collides():
                highlight_s = "Sélection de niveau"
                if click == True:
                    choice = 1
                    running = False
                    
            elif self.leave.collides():
                highlight_l = "Quitter"
                if click:
                    sys.exit(0)
                    running = False
            
            else:
                click = False
                    

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True

            self.menu.render(highlight_m)
            self.second.render(highlight_s)
            self.leave.render(highlight_l)

            pygame.display.update()

        if choice == 1:
            self.level_selector_process()
        
        else:
            self.menu_process()
    
    def level_selector_process(self):

        self.levelselector = LevelSelector(self.game)
        self.levelselector.propose_levels()
        while not self.levelselector.has_selected_level():
            self.levelselector.process()

    def menu_process(self):
        self.game.menu()