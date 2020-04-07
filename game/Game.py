import pygame
from entities.player import Player
from entities.platform import Platform


class Game:

    def __init__(self, screen):
        self.screen = screen
        self.platforms = []
        self.player = None

    def process(self):
        for sprite in self.platforms:
            sprite.move()
            sprite.draw(self.screen.mode)
        falling = self.player.fall()
        if (falling == False):  # s'il ne tombe pas, il peut bouger
            self.player.move()
        self.player.draw(self.screen.mode)
        self.screen.clock.tick(60)

    def render_level(self, link):
        pass

    def register_platform(self, *sprite):
        self.platforms.append(*sprite)

    def remove_platform(self, *sprite):
        self.platforms.remove(sprite)

    def register_player(self, player):
        self.player = player
        self.player.surface = self.screen.mode
