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
        self.y_1 = self.y
        self.ground = self.rect.bottom
        self.falling = False
        self.landed = True
        self.power = 0.8
        self.alpha = 26  # 30 = vertical; 0 = horizontal
        self.angle = -self.alpha * pi / 60  # .................calcul de l'angle en RAD, selon alpha
        self.convert = (
                    (38.2 / 1920) / 100)  # ..........Pour un écran 17", 38.2 cm = 1920pix => 1 pix = (38.2/1920)/100 m
        self.g = 9.81  # .............................constante de gravitation
        self.sens = 1  # 1 : droite ; -1 : gauche
        self.i = 1  # variables itérative arbitraire (remplace la variable temporaire d'une vraie équation de trajectoire)
        self.d0 = self.x
        self.h0 = self.y
        self.dist_jump = 20
        self.dist_fall = 20
        self.frame = 0
        self.face = True
        self.dead = "None"
        self.speed = 0

    def get_position(self):
        return self.position

    def update(self):
        self.rect.topleft = self.x, self.y
        self.position = self.x, self.y

    def update_position(self):
        self.d0 = int(self.x)  # mise à jour des conditions initiales
        self.h0 = int(self.y)
        self.y = self.h0
        self.x = self.d0
        self.y_1 = self.y - 1
        self.i = 1
        self.update()
        self.new_rect()

    def move(self, decalage):
        """ Gestion des évènements """
        i = 0
        key = pygame.key.get_pressed()
        dist = 6  # la distance en 1 frame

        if (self.landed == False):
            self.angle = -self.alpha * pi / 60
            i = self.jump(self.power, self.angle)
            if self.can_defil():
                self.h0 += decalage

        else:
            self.rect.left += 5
            self.rect.right += 5
            self.face = False
            if key[pygame.K_RIGHT] or key[pygame.K_d]:  # right key
                self.x += dist  # right
                if (self.sens == 1 and self.speed < 6):
                    self.speed += 0.2
                elif (self.sens == -1):
                    self.speed = 0
                self.sens = 1

                if key[pygame.K_SPACE]:
                    self.update_position()
                    self.landed = False
                    i = self.dist_jump

                elif key[pygame.K_UP] or key[pygame.K_w]:
                    if self.alpha < 28:
                        self.alpha += 0.2
                        self.power += 0.004

                elif key[pygame.K_DOWN] or key[pygame.K_s]:
                    if self.alpha > 20:
                        self.alpha -= 0.2
                        self.power -= 0.004


            elif key[pygame.K_LEFT] or key[pygame.K_a]:  # left key
                self.x -= dist  # left
                if (self.sens == -1 and self.speed < 6):
                    self.speed += 0.2
                elif (self.sens == 1):
                    self.speed = 0
                self.sens = -1

                if key[pygame.K_SPACE]:
                    self.update_position()
                    self.landed = False
                    i = self.dist_jump

                elif key[pygame.K_UP] or key[pygame.K_w]:
                    if self.alpha < 28:
                        self.alpha += 0.2
                        self.power += 0.004
                    print(self.power)

                elif key[pygame.K_DOWN] or key[pygame.K_s]:
                    if self.alpha > 20:
                        self.alpha -= 0.2
                        self.power -= 0.004
                    print(self.power)


            elif key[pygame.K_SPACE]:  # space key
                self.update_position()
                self.landed = False
                i = self.dist_jump

            elif key[pygame.K_UP] or key[pygame.K_w]:
                if self.alpha < 28:
                    self.alpha += 0.2
                    self.power += 0.004
                print(self.power)

            elif key[pygame.K_DOWN] or key[pygame.K_s]:
                if self.alpha > 20:
                    self.alpha -= 0.2
                    self.power -= 0.004
                print(self.power)

            else:  # S'il ne se passe rien
                self.face = True
                self.sens = 0
                if self.landed == True:
                    self.speed = 0

        if self.y > 720:
            self.dead = "Lose"

        self.animation()
        return i

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

    def fall(self):
        self.y = self.convert * 0.5 * self.g * self.i * self.i + self.h0
        self.i += self.dist_fall

    def jump(self, power, angle):
        self.x = self.sens * self.i * power * cos(
            angle) + self.d0  # ...........................................equation horaire selon x
        self.y = self.convert * 0.5 * self.g * self.i * self.i + power * sin(
            angle) * self.i + self.h0  # .......equation horaire selon y
        self.i -= self.dist_jump
        self.y_1 = self.convert * 0.5 * self.g * self.i * self.i + power * sin(angle) * self.i + self.h0
        self.i += 2 * self.dist_jump
        self.new_rect()
        self.rect.bottomleft = int(self.x), int(self.y + self.image.get_height() + 5)
        self.rect.bottomright = int(self.x + self.image.get_width()), int(self.y + self.image.get_height() + 5)

        self.update()

        return self.i

    def new_rect(self):
        self.rect = self.image.get_rect(center=self.position)

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

    def can_lava_move(self):

        if self.y <= 500:  # Valeur à changer pour le début de montée de lave
            return True
        else:
            return False
    
    def can_defil(self):

        if self.y <= 300:  # Valeur à changer pour le début du fond d'écran
            return True
        else :
            return False

    def just_falling(self):

        if (self.falling == True):
            if self.sens == 1:
                self.x += self.speed
            else:
                self.x -= self.speed