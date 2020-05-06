import pygame
from pygame.sprite import *

class Background:

    #Classe de défillement du fond d'écran, uniquement verticalement

    def __init__(self):
        
        self.bck_ground = [pygame.transform.scale(pygame.image.load("images/back.png"),(1280, 1200)), pygame.transform.scale(pygame.image.load("images/back.png"),(1280, 1200))]

        self.pos_1 = -300
        self.pos_2 = -1500
        self.limit = [900, -300]     # bas, haut
        self.vitesse = 2
        self.delta_y = 5
        self.decalage = 0

    def defil(self):
            
        self.pos_1 += 25
        self.pos_2 += 25
        self.decalage += self.delta_y

        if self.pos_1 > self.pos_2:
            if self.pos_1 >= 900:
                    self.pos_1 = -1500
            
        else:
            if self.pos_2 >= 900:
                self.pos_2 = -1500
    
    def draw(self, surface):
        surface.blit(self.bck_ground[0], (0, self.pos_1))
        surface.blit(self.bck_ground[1], (0, self.pos_2))