from pygame.sprite import *
import time
import pygame
from entities.trophy import Trophy


class Platform(Sprite):

    def __init__(self, position, mobile, image_link):
        super().__init__()
        self.position = position
        self.mobile = mobile
        self.image = pygame.image.load(image_link)
        self.rect = self.image.get_rect(center=position)
        self.loop = 0
        self.sens = False
        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
        self.x = position[0]
        self.y = position[1]
        self.trophy = None

    """
        Paramètre : surface
        Défini la platforme de type casque
    """
    def set_winnable(self, surface):
        self.trophy = Trophy(self)

    """
        Retourne la position de la plateforme
    """   
    def get_position(self):
        return self.position

    """
        Retourne l'état de la plateforme
    """
    def is_mobile(self):
        return self.mobile

    """
        Mouvement horizontal des plateformes
    """
    def move(self):
        if self.mobile:
            if self.sens:
                self.x += 2
            else:
                self.x -= 2

            if self.x == self.position[0] + 40:
                self.sens = False
            if self.x == self.position[0] - 40:
                self.sens = True

        self.rect.topleft = self.x, self.y

    """
        Affiche la plateforme dans la fenêtre
    """
    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

    """
        Mouvement vertical des platformes, dépend de la valeur donnée par Background()
    """
    def move_y(self, delta_y):
        self.y += delta_y

    """
        Fonction de collision de la plateforme avec un joueur.
        Vérifie si plus de 2/3 de la taille du joueur dépasse la plateforme lors d'un saut. 
        Si oui
            le joueur est téléporté au dessus de la plateforme
        : return Booléen
    """

    def collides_with(self, player, platforms):
        if pygame.sprite.spritecollideany(player, platforms, None) is not None and player.y_1 < player.y:
            if player.rect.left > self.rect.left - 2 / 3 * player.image.get_width() and player.rect.right < self.rect.right + 2 / 3 * player.image.get_width() and self.rect.bottom + 5 > player.rect.bottom > self.rect.top - 5:
                if player.y != self.rect.top - player.image.get_height() + 1:
                    player.y = self.rect.top - player.image.get_height() + 1
                    player.landed = True
                    player.update_position()
                return 1
        return 0

    """
        : collision entre souris et plateforme
        : return booléen
    """
    def collides(self):
        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
        return self.x < self.mouse_x < self.x + self.image.get_width() and self.y < self.mouse_y < self.y + self.image.get_height()
