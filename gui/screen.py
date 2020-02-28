import pygame
from entities.player import Player
from entities.platform import Platform
from errors.error import GGFError


class Screen:

    def __init__(self, dimensions):

        self.sprites = pygame.sprite.Group()
        self.clock = pygame.time.Clock()
        self.player = None  # :)

        self.window = pygame.display
        self.window_mode = self.window.set_mode(dimensions)
        self.window_mode.blit(pygame.image.load("images/back pix.png").convert_alpha(), [0, 0])
        self.window.set_caption("Gotta Go Fast")
        self.window.set_icon(pygame.image.load("images/logo.png").convert_alpha())
        self.window.toggle_fullscreen()
        self.window.flip()
        self.playing = True

    def run(self):

        while self.playing:

            self.sprites.update()

            for sprite in self.sprites:
                if isinstance(sprite, Player):
                    sprite.move()
                    sprite.draw(self.window_mode)

            self.window_mode.blit(pygame.image.load("images/back pix.png").convert_alpha(), [0, 0])
            self.draw_sprites()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.playing = False

            self.window.flip()
            self.clock.tick(60)

    def stop(self):
        self.playing = False

    def draw_sprites(self):
        self.sprites.draw(self.window_mode)
        # self.sprites.update() //Optionnel
        self.window.flip()

    def get_sprites(self):
        return self.sprites

    def register_player(self, sprite):
        self.player = sprite

    def add_sprite(self, *sprite):
        self.sprites.add(sprite)

    def remove_sprite(self, *sprite):
        self.sprites.remove(sprite)
