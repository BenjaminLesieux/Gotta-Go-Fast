from pygame.sprite import *
from math import *


class Player(Sprite):

    def __init__(self, position):
        super().__init__()
        self.position = position
        self.image = pygame.image.load("images/face.png").convert_alpha()
        self.rect = self.image.get_rect(center=position)
        self.x = position[0]
        self.y = position[1]
        self.ground = self.rect.bottom
        self.falling = False
        self.landed = True
        self.power = 0.9
        self.alpha = -27
        self.angle = -self.alpha * pi / 60  # .................calcul de l'angle en RAD, selon alpha
        self.convert = (
                    (38.2 / 1920) / 100)  # ..........Pour un écran 17", 38.2 cm = 1920pix => 1 pix = (38.2/1920)/100 m
        self.g = 9.81  # .............................constante de gravitation
        self.sens = 1  # 1 : droite ; -1 : gauche
        self.i = 1
        self.d0 = self.x
        self.h0 = self.y

    def get_position(self):
        return self.position

    def update_position(self):
        self.position[0] = self.x
        self.position[1] = self.y

    def move(self):
        """ Gestion des évènements """
        key = pygame.key.get_pressed()
        dist = 6  # la distance en 1 frame

        if key[pygame.K_RIGHT]:  # right key
            self.x += dist  # right
        elif key[pygame.K_LEFT]:  # left key
            self.x -= dist  # left
        elif key[pygame.K_SPACE]:  # space key
            self.landed = False
            self.i = 1
            while (self.landed == False and self.i == 1):
                self.jump(self.power, self.angle)

        self.update_position()


    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

    def jump(self, power, angle):
        if self.landed == True:
            self.d0 = int(self.x)  # mise à jour des conditions initiales
            self.h0 = int(self.y)  # """
            self.y = self.h0
            self.x = self.d0
            self.i = 1
            self.falling = False
            return
        else:
            while (self.i < 20):
                self.x = self.sens * self.i * power * cos(
                    angle) + self.d0  # ..........................equation horaire selon x, avec les differentes variables
                self.y = self.convert * 0.5 * self.g * self.i * self.i + power * sin(
                    angle) * self.i + self.h0  # .......equation horaire selon y
                self.i += 1
                print("oh je saute")
                self.update_position()
            self.landed = True
