import pygame, time
from entities.player import Player
from entities.platform import Platform
from entities.lava import Lava
from game.background import Background
from gui.ecran_fin import FinalScreen
import os.path


class Game:

    def __init__(self, screen):
        self.screen = screen
        self.platforms = []
        self.player = None
        self.end_screen = FinalScreen(self.screen)
        self.lava = None
        self.state = False
        self.stop = False
        self.background = None
        self.i = 0

    def process(self):

        if not self.stop:

            collide = 0
            self.player.update()

            if self.player.can_defil():
                self.background.defil()

                for sprite in self.platforms:
                    self.screen.py_sprite.remove(sprite)
                    sprite.move_y(self.background.delta_y)
                    sprite.move()
                    self.screen.py_sprite.add(sprite)
                    sprite.draw(self.screen.mode)

            self.background.draw(self.screen.mode)
            # pygame.draw.rect(self.screen.mode, pygame.Color('green'), (self.player.x, sprite.rect.left - self.player.image.get_width()), 0)
            k = 1
            for sprite in self.platforms:
                print(k)
                k += 1
                # pygame.draw.rect(self.screen.mode, pygame.Color('blue'), sprite.rect)
                # pygame.draw.line(self.screen.mode, pygame.Color('blue'), (self.player.x, self.player.rect.y) , (self.player.rect.right, self.player.rect.top))
                # pygame.draw.line(self.screen.mode, pygame.Color('green'), (sprite.rect.left, sprite.rect.top - 10) , (sprite.rect.right, sprite.rect.top - 10))
                # pygame.draw.line(self.screen.mode, pygame.Color('green'), (sprite.rect.left, sprite.rect.top + 10) , (sprite.rect.right, sprite.rect.top + 10))
                sprite.move()
                sprite.draw(self.screen.mode)
                if collide == 0 and (self.i < self.player.dist_jump or self.i > 100):
                    collide = sprite.collides_with(player=self.player, platforms=self.platforms)
                    if collide == 1:
                        self.player.landed = True
                        self.player.falling = False
                        self.player.update_position()
                    elif self.player.landed == True:
                        self.player.falling = True

            if self.player.falling == True:
                self.player.fall()
            else:
                self.i = self.player.move()

            self.player.new_rect()
            if self.state is False:
                self.state = self.player.can_lava_move()  # Vérification de la hauteur à partir de laquelle la lave monte

            self.lava.is_moving(self.state)
            self.lava.move(self.background.delta_y)

            self.player.draw(self.screen.mode)
            self.lava.draw(self.screen.mode)  # Lave en dernier !
            self.end()
            
        else:
            self.screen.level_selector.selected_level = None
            self.type_end()
            self.stop = False
            self.end_screen.loop()

        self.screen.clock.tick(60)

    def register_platform(self, level_name, position, mobile):

        file = open(level_name, "a")  # Si non existant, le fichier sera créé

        file.write("{" + str(position[0]) + "/" + str(position[1]-self.background.decalage) + "/" + str(mobile) + "}\n")
        file.write("")

        file.close()

        self.platforms.append(Platform(position, mobile, "images/plateforme 1.png"))

    def register_platform_by_file(self, level_name):
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
            position = (x, y)
            mobile = True if lines[j][i + 1:len(lines[j]) - 2] == "True" else False

            self.platforms.append(Platform(position, mobile, "images/plateforme 1.png"))

    def remove_platform(self, *sprite):
        self.platforms.remove(sprite)

    def register_player(self, player):
        self.player = player
        self.player.surface = self.screen.mode

    def render_lava(self):
        self.lava = Lava()
        self.player.surface = self.screen.mode

    def render_background(self):
        self.background = Background()
        self.background.surface = self.screen.mode

    def end(self):

        if (self.player.dead == "Win") or (self.player.dead == "Lose"):
            self.stop = True
    
    def type_end(self):

        if (self.player.dead == "Win"):
            self.state == "Victoire"
        else:
            self.state == "Game Over"