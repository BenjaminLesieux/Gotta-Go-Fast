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
        self.p_trophy = None
        self.start_time = 0
        self.count = ""

    def set_end_menu(self, end_menu):
        self.end_menu = end_menu

    def process(self):
        if self.start_time == 0:
            self.start_time = time.time()
            self.ggf.timer = 0
            pygame.mixer.music.load("images/Run.ogg")
            pygame.mixer.music.set_volume(0.1)
            pygame.mixer.music.play(-1)

        if not self.stop:

            collide = 0
            self.lava.new_rect()
            self.player.update()

            if self.p_trophy is not None:
                self.p_trophy.set_winnable(self.ggf.mode)
                self.trophy = self.p_trophy.trophy

            if self.player.can_defil():
                self.lava_delta = self.background.delta_y
                self.background.defil("up")

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

            for sprite in self.platforms:
                sprite.move()
                sprite.draw(self.ggf.mode)

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
                self.i = self.player.move(self.background.delta_y)
            self.player.just_falling()
            self.player.new_rect()

            if self.state is False:
                self.state = self.player.can_lava_move()  # Vérification de la hauteur à partir de laquelle la lave monte

            self.lava.is_moving(self.state)
            self.lava.move(self.lava_delta)
            self.type_end()

            if self.p_trophy is not None:
                self.trophy.draw(self.ggf.mode)
            self.player.draw(self.ggf.mode)
            self.lava.draw(self.ggf.mode)  # Lave en dernier !
            self.count = str(time.time() - self.start_time)
            self.count = self.count.replace(self.count[6:len(self.count)], "")

            self.ggf.draw_text(self.count + "s", pygame.font.Font("images/Fipps-Regular.otf", 35), (255, 255, 255),
                               self.ggf.mode, 30, 20)
            self.end()


    def register_platform(self, level_name, position, mobile, decalage, ptype):

        file = open(level_name, "a")  # Si non existant, le fichier sera créé

        file.write(
            "{" + str(position[0]) + "/" + str(position[1] - decalage) + "/" + str(ptype) + "/" + str(mobile) + "}\n")
        file.write("")

        file.close()

        plat = None

        if ptype == 1:
            plat = Platform(position, mobile, "images/plateforme 1.png")
        elif ptype == 2:
            plat = Platform(position, mobile, "images/plateforme 2.png")
        elif ptype == 3:
            plat = Platform(position, mobile, "images/plateforme 3.png")

        self.platforms.append(plat)

        return plat

    def register_platform_by_file(self, level_name):

        ymax = 10000

        level = open(level_name + ".txt", "r") if os.path.exists(level_name + ".txt") else open(level_name + ".txt",
                                                                                                "a+")
        if os.path.exists("high scores/" + level_name + ".txt"):
            level_hs = open("high scores/" + level_name + ".txt", "r")
        else:
            level_hs = open("high scores/" + level_name + ".txt", "w+")
            for i in range(0, 3):
                level_hs.write("999.99\n")
        level_hs.close()
        level = open(level_name + ".txt", "r")  # Pour être sûr de mettre en mode 'read' après la possible création

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

            y = int(lines[j][last + 1:i])

            while lines[j][i] != "/":
                i += 1

            ptype = int(lines[j][i + 1])

            if (y < ymax):
                ymax = y
                self.w_pos = j

            position = (x, y)
            mobile = True if lines[j][i + 3:len(lines[j]) - 2] == "True" else False

            plat = None

            if ptype == 1:
                plat = Platform(position, mobile, "images/plateforme 1.png")
            elif ptype == 2:
                plat = Platform(position, mobile, "images/plateforme 2.png")
            elif ptype == 3:
                plat = Platform(position, mobile, "images/plateforme 3.png")

            self.platforms.append(plat)

        if len(self.platforms) > 0:
            self.p_trophy = self.platforms[self.w_pos]

    def rewrite_file(self, level_name, platform):

        level = open(level_name.name + ".txt", "r")  # Pour être sûr de mettre en mode 'read' après la possible création
        lines = level.readlines()
        num_line = 0
        ymax = 0

        for j in range(0, len(lines)):
            i = 1
            while lines[j][i] != "/":
                i += 1

            last = i
            x = int(lines[j][1:i])

            i += 1
            while lines[j][i] != "/":
                i += 1

            y = int(lines[j][last + 1:i])
            while lines[j][i] != "/":
                i += 1

            ptype = int(lines[j][i + 1])
            if y < ymax:
                ymax = y
                self.w_pos = j

            position = (x, y)
            mobile = True if lines[j][i + 3:len(lines[j]) - 2] == "True" else False
            if position == platform.position:
                num_line = j
                break

        level.close()
        lines.pop(num_line)
        level = open(level_name.name + ".txt", "w+")

        for line in lines:
            level.write(line)

        level.close()

    def remove_platform(self, *sprite):
        self.platforms.remove(sprite)
    """
        Fonctions permettant d'initialiser les classes.
    """
    def register_player(self, player):
        self.player = player
        self.player.surface = self.ggf.mode

    def render_lava(self):
        self.lava = Lava()
        self.player.surface = self.ggf.mode

    def render_background(self):
        self.background = Background()
        self.background.surface = self.ggf.mode

    """
        Vérifie si le joueur a gagné ou perdu
    """
    def type_end(self):

        if self.trophy is not None:
            if self.trophy.collide_with(self.player) == "Win":
                self.player.dead = "Win"
        if self.lava.collide_with(self.player) == "Lose":
            self.player.dead = "Lose"

    """
        Remet les conditions à zéro en cas de victoire/défaite
        Donne des paramètres différents au menu.
    """
    def end(self):

        if self.player.dead != "None":
            if self.ggf.timer == 0:
                self.ggf.timer = time.time() - self.start_time
                self.start_time = 0
            self.state = False
            self.lava.moving = False
            if (self.player.dead == "Win"):
                self.end_menu.state = "Victoire"
                self.end_menu.activated = True
            else:
                self.end_menu.state = "Game over"
                self.end_menu.activated = True
                pygame.mixer.music.load('images/idée-menu-non-mixée.ogg')
                pygame.mixer.music.set_volume(0.3)
                pygame.mixer.music.play(-1)
