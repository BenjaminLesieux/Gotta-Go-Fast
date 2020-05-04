from pygame.sprite import *
from math import *


class Player(Sprite):

    def __init__(self, position):
        super().__init__()
        self.position = position
        self.list_images = [pygame.image.load("images/face.png"),
                            pygame.image.load("images/right1.png"),
                            pygame.image.load("images/right2.png"),
                            pygame.image.load("images/left1.png"),
                            pygame.image.load("images/left2.png")]
        self.image = self.list_images[0]
        self.rect = self.image.get_rect()
        self.surface = None
        self.x = position[0]
        self.y = position[1]
        self.ground = self.rect.bottom
        self.falling = False
        self.landed = True
        self.power = 0.9
        self.alpha = 26
        self.angle = -self.alpha * pi / 60  # .................calcul de l'angle en RAD, selon alpha
        self.convert = ((38.2 / 1920) / 100)  # ..........Pour un écran 17", 38.2 cm = 1920pix => 1 pix = (38.2/1920)/100 m
        self.g = 9.81  # .............................constante de gravitation
        self.sens = 1  # 1 : droite ; -1 : gauche
        self.i = 1  # variables itérative arbitraire (remplace la variable temporaire d'une vraie équation de trajectoire)
        self.d0 = self.x
        self.h0 = self.y
        self.frame = 0
        self.face = True

    def get_position(self):
        return self.position

    def update(self):
        self.rect.topleft = self.x, self.y + 10
        self.position = self.x, self.y

    def update_position(self):
        self.d0 = int(self.x)  # mise à jour des conditions initiales
        self.h0 = int(self.y)
        self.y = self.h0
        self.x = self.d0
        self.position = self.x, self.y
        self.i = 1
        self.rect.topleft = self.x, self.y + 10

    def move(self):
        """ Gestion des évènements """
        key = pygame.key.get_pressed()
        dist = 6  # la distance en 1 frame

        if (self.landed == False):
            self.jump(self.power, self.angle)

        else:
            self.face = False
            if key[pygame.K_RIGHT]:  # right key
                self.x += dist  # right
                self.sens = 1

            elif key[pygame.K_LEFT]:  # left key
                self.x -= dist  # left
                self.sens = -1

            elif key[pygame.K_SPACE]:  # space key
                self.update_position()
                self.landed = False
            else:
                self.face = True

        self.animation()

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

    def fall(self, collide):
        if (collide == 0 or collide == 2):
            self.y = self.convert * 0.5 * self.g * self.i * self.i + self.h0
            self.i += 20
            return True
        self.update_position()
        return False

    def jump(self, power, angle):
        self.x = self.sens * self.i * power * cos(
            angle) + self.d0  # ...........................................equation horaire selon x
        self.y = self.convert * 0.5 * self.g * self.i * self.i + power * sin(
            angle) * self.i + self.h0  # .......equation horaire selon y
        self.i += 30
        #print("oh je saute", self.h0, self.y, self.i)
        self.draw(self.surface)

        return

    def animation(self):

        if (self.frame == 12):
            self.frame = 0

        if self.landed:

            if self.face:
                self.image = self.list_images[0]

            else:
                if (self.sens == 1):
                    if (self.frame//6 == 0):
                        self.image = self.list_images[1]
                    else:
                        self.image = self.list_images[2]
                    self.frame += 1
                
                elif (self.sens == -1):
                    if (self.frame//6 == 0):
                        self.image = self.list_images[3]
                    else:
                        self.image = self.list_images[4]
                    self.frame += 1

        else:

            if (self.sens == 1):
                self.image = self.list_images[1]
            elif (self.sens == -1):
                self.image = self.list_images[3]

        #print(self.frame)

    def can_lava_move(self):

        if self.y <= 475.5:             # Valeur à changer pour le début de montée de lave
            return True
        else :
            return False

