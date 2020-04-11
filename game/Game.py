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

        if not falling:  # s'il ne tombe pas, il peut bouger
            self.player.move()
        self.player.draw(self.screen.mode)
        self.screen.clock.tick(60)

    def render_level(self, link):
        pass

    def register_platform(self, level_name, position, mobile):
        file = open(level_name, "a")
        file.write("{" + str(position[0]) + "-" + str(position[1]) + "-" + str(mobile) + "}\n")
        file.write("")

        file.close()

        self.platforms.append(Platform(position, mobile, "images/plateforme 1 V2.png"))

    def register_platform_by_file(self, level_name):
        level = open(level_name, "r")
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

            # Commentaire pour commit

            y = int(lines[j][last + 1:i])
            position = (x, y)
            mobile = True if lines[j][i + 1:] == "True" else False

            print(str(x) + " " + str(y) + " " + str(mobile))

            self.platforms.append(Platform(position, mobile, "images/plateforme 1 V2.png"))

    def remove_platform(self, *sprite):
        self.platforms.remove(sprite)

    def register_player(self, player):
        self.player = player
        self.player.surface = self.screen.mode
