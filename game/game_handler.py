import pygame, time
from entities.player import Player
from entities.platform import Platform
from entities.lava import Lava
from game.background import Background
import os.path


class Game:

    def __init__(self, ggf):
        self.ggf = ggf
        self.platforms = []
        self.player = None
        self.lava = None
        self.state = False
        self.stop = False
        self.background = None
        self.i = 0
        self.lava_delta = 0
        self.end_menu = None
        self.w_pos = (-100,0)
        self.trophy = None

    def set_end_menu(self, end_menu):
        self.end_menu = end_menu

    def process(self):

        if not self.stop:

            collide = 0
            self.lava.new_rect()
            self.player.update()

            if self.player.can_defil():
                self.lava_delta = self.background.delta_y
                self.background.defil()

                for sprite in self.platforms:
                    self.ggf.py_sprite.remove(sprite)
                    if self.background.count < self.background.n_screen:
                        sprite.move_y(self.background.delta_y)
                    sprite.move()
                    self.ggf.py_sprite.add(sprite)
                    sprite.draw(self.ggf.mode)
            else:
                self.lava_delta = 0

            self.background.draw(self.ggf.mode)
            # pygame.draw.rect(self.ggf.mode, pygame.Color('green'), (self.player.x, sprite.rect.left - self.player.image.get_width()), 0)
            for sprite in self.platforms:
                # pygame.draw.rect(self.ggf.mode, pygame.Color('blue'), sprite.rect)
                # pygame.draw.line(self.ggf.mode, pygame.Color('blue'), (self.player.x, self.player.rect.y) , (self.player.rect.right, self.player.rect.top))
                # pygame.draw.line(self.ggf.mode, pygame.Color('green'), (sprite.rect.left, sprite.rect.top - 10) , (sprite.rect.right, sprite.rect.top - 10))
                # pygame.draw.line(self.ggf.mode, pygame.Color('green'), (sprite.rect.left, sprite.rect.top + 10) , (sprite.rect.right, sprite.rect.top + 10))
                sprite.move()
                sprite.draw(self.ggf.mode)
                """pygame.draw.circle(self.ggf.mode, pygame.Color('red'), self.player.rect.midbottom, 3)
                pygame.draw.circle(self.ggf.mode, pygame.Color('red'), self.player.rect.bottomleft, 3)
                pygame.draw.circle(self.ggf.mode, pygame.Color('red'), self.player.rect.bottomright, 3)
                pygame.draw.circle(self.ggf.mode, pygame.Color('blue'), sprite.rect.midtop, 3)
                pygame.draw.circle(self.ggf.mode, pygame.Color('blue'), sprite.rect.topleft, 3)
                pygame.draw.circle(self.ggf.mode, pygame.Color('blue'), sprite.rect.topright, 3)"""

                if self.i < self.player.dist_jump or self.i > 100:
                    collide += sprite.collides_with(player=self.player, platforms=self.platforms)
            if collide >= 1:
                self.player.landed = True
                self.player.falling = False
                self.player.update_position()
            elif self.player.landed == True:
                self.player.falling = True

            if self.player.falling == True:
                self.player.fall()
            else:
                self.i = self.player.move()
            self.player.just_falling()

            self.player.new_rect()
            if self.state is False:
                self.state = self.player.can_lava_move()  # Vérification de la hauteur à partir de laquelle la lave monte

            self.lava.is_moving(self.state)
            self.lava.move(self.lava_delta)
            self.player.dead = self.lava.collide_with(self.player)

            self.player.draw(self.ggf.mode)
            self.trophy.set_winnable(True, self.ggf.mode)
            self.lava.draw(self.ggf.mode)  # Lave en dernier !
            self.end()


        # self.screen.clock.tick(60)

    def register_platform(self, level_name, position, mobile, decalage):

        file = open(level_name, "a")  # Si non existant, le fichier sera créé

        file.write("{" + str(position[0]) + "/" + str(position[1]-decalage) + "/" + str(mobile) + "}\n")
        file.write("")

        file.close()

        plat = Platform(position, mobile, "images/plateforme 1.png")

        self.platforms.append(plat)

        return plat

    def register_platform_by_file(self, level_name):

        ymax = 10000
        

        level = open(level_name, "r") if os.path.exists(level_name + ".txt") else open(level_name, "a+")
        level = open(level_name, "r")  # Pour être sûr de mettre en mode 'read' après la possible création

        lines = level.readlines()

        for j in range(0, len(lines)):
            i = 1

            while lines[j][i] != "/":
                i += 1

            last = i
            x = int(lines[j][1:i])

            i += 1

            while lines[j][i] != "/":
                i += 1
            # s
            y = int(lines[j][last + 1:i])

            if (y < ymax):
                ymax = y
                self.w_pos = j

            position = (x, y)
            mobile = True if lines[j][i + 1:len(lines[j]) - 2] == "True" else False

            self.platforms.append(Platform(position, mobile, "images/plateforme 1.png"))

        self.trophy = self.platforms[self.w_pos]

    def remove_platform(self, *sprite):
        self.platforms.remove(sprite)

    def register_player(self, player):
        self.player = player
        self.player.surface = self.ggf.mode

    def render_lava(self):
        self.lava = Lava()
        self.player.surface = self.ggf.mode

    def render_background(self):
        self.background = Background()
        self.background.surface = self.ggf.mode

    def end(self):

        if self.player.dead != "None":
            if (self.player.dead == "Win"):
                self.end_menu.state = "Victoire"
                self.end_menu.activated = True
            else:
                self.end_menu.state = "Game over"
                self.end_menu.activated = True
