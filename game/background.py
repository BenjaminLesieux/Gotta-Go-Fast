import pygame
from pygame.sprite import *


class Background():

    # Classe de défillement du fond d'écran, uniquement verticalement

    def __init__(self):

        self.bck_ground = [pygame.transform.scale(pygame.image.load("images/Background1.jpg"), (1280, 1200)),
                           pygame.transform.scale(pygame.image.load("images/Background2.jpg"), (1280, 1200))]
        # Les fonds d'écrans sont plus longs que la fenêtre pour donner un véritable effet de longueur.
        self.pos_1 = -300
        self.pos_2 = -1500
        self.limit = [900, -300]  # bas, haut
        self.delta_y = 5
        self.decalage = 0
        self.count = 1
        self.n_screen = 3
        self.sens = 1

    """
        Deux directions up et down pour le leveleditor
        n_screen est le nombre maximal d'écrans pouvant défiler
        Si écran 1 sort de l'écran, il passe en dessous d'écran 2.
        Même chose pour écran 2.
    """

    def defil(self, direction):
        if direction == "up":
            self.sens = 1
        else:
            self.sens = -1

        if self.count < self.n_screen:
            self.pos_1 += self.sens * 2
            self.pos_2 += self.sens * 2
            self.decalage += self.sens * self.delta_y

            if self.pos_1 > self.pos_2:
                if self.pos_1 >= 900:
                    self.pos_1 = -1500
                    self.count += 1
            else:
                if self.pos_2 >= 900:
                    self.pos_2 = -1500
                    self.count += 1

    """
        Affiche les deux background dans la fenêtre
    """

    def draw(self, surface):
        surface.blit(self.bck_ground[0], (0, self.pos_1))
        surface.blit(self.bck_ground[1], (0, self.pos_2))
