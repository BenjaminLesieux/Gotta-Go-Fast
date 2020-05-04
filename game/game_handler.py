import pygame
from entities.player import Player
from entities.platform import Platform
from entities.lava import Lava
import os.path


class Game:

    def __init__(self, screen):
        self.screen = screen
        self.platforms = []
        self.player = None
        self.lava = None
        self.state = False

    def process(self):

        self.player.update()

        for sprite in self.platforms:
            self.screen.py_sprite.remove(sprite)
            self.screen.py_sprite.add(sprite)
            sprite.move()
            sprite.draw(self.screen.mode)
            sprite.collides_with(player=self.player)

        falling = self.player.fall()

        if falling is False:  # s'il ne tombe pas, il peut bouger
            self.player.move()

        if self.state is False:
            self.state = self.player.can_lava_move()  # Vérification de la hauteur à partir de laquelle la lave monte
        self.lava.is_moving(self.state)
        # self.lava.move()

        self.player.draw(self.screen.mode)
        self.player.update()
        self.lava.draw(self.screen.mode)  # Lave en dernier !
        self.screen.clock.tick(60)

    def register_platform(self, level_name, position, mobile):

        file = open(level_name, "a")  # Si non existant, le fichier sera créé

        file.write("{" + str(position[0]) + "-" + str(position[1]) + "-" + str(mobile) + "}\n")
        file.write("")

        file.close()

        plat = Platform(position, mobile, "images/plateforme 1.png")

        self.platforms.append(plat)
        self.screen.py_sprite.add(plat)

    def register_platform_by_file(self, level_name):
        level = open(level_name, "r") if os.path.exists(level_name + ".txt") else open(level_name, "a+")
        level = open(level_name, "r")  # Pour être sûr de mettre en mode 'read' après la possible création

        lines = level.readlines()

        for j in range(0, len(lines)):
            i = 1

            while lines[j][i] != "-":
                i += 1

            last = i
            x = int(lines[j][1:i])

            i += 1

            while lines[j][i] != "-":
                i += 1
            # s
            y = int(lines[j][last + 1:i])
            position = (x, y)
            mobile = True if lines[j][i + 1:len(lines[j]) - 2] == "True" else False

            plat = Platform(position, mobile, "images/plateforme 1.png")

            self.platforms.append(plat)
            self.screen.py_sprite.add(plat)

    def remove_platform(self, *sprite):
        self.platforms.remove(sprite)

    def register_player(self, player):
        self.player = player
        self.player.surface = self.screen.mode

    def render_lava(self):
        self.lava = Lava()
        self.player.surface = self.screen.mode
