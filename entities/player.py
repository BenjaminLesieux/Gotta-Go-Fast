from pygame.sprite import *
from math import *


class Player(Sprite):

    def __init__(self, position):
        super().__init__()
        self.position = position
        self.list_images = [pygame.image.load("images/face.png").convert_alpha(),pygame.image.load("images/right1.png").convert_alpha(),pygame.image.load("images/right2.png").convert_alpha(),pygame.image.load("images/left1.png").convert_alpha(),pygame.image.load("images/left2.png").convert_alpha()]
        self.image = self.list_images[0]
        self.rect = self.image.get_rect(center=position)
        self.surface = None
        self.x = position[0]
        self.y = position[1]
        self.ground = self.rect.bottom
        self.falling = False
        self.landed = True
        self.power = 0.8
        self.alpha = 25
        self.angle = -self.alpha * pi / 60  # .................calcul de l'angle en RAD, selon alpha
        self.convert = (
                    (38.2 / 1920) / 100)  # ..........Pour un écran 17", 38.2 cm = 1920pix => 1 pix = (38.2/1920)/100 m
        self.g = 9.81  # .............................constante de gravitation
        self.sens = 1  # 1 : droite ; -1 : gauche
        self.i = 1  # variables itérative arbitraire (remplace la variable temporaire d'une vraie équation de trajectoire)
        self.d0 = self.x
        self.h0 = self.y
        self.frame = 0
        self.face = True

    def get_position(self):
        return self.position

    def update_position(self):
        self.d0 = int(self.x)  # mise à jour des conditions initiales
        self.h0 = int(self.y)
        self.y = self.h0
        self.x = self.d0
        self.position[0] = self.x
        self.position[1] = self.y
        self.i = 1

    def move(self):
        """ Gestion des évènements """
        key = pygame.key.get_pressed()
        nb_key = 0
        dist = 6  # la distance en 1 frame

        for i in range(0,len(key)):
            if (key[i] == 1):
                nb_key += 1

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

        if (nb_key == 0):
            self.face = True
        
        self.animation()    

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

    def fall(self):
        if (self.y < 620 and self.landed == True):
            self.y = self.convert * 0.5 * self.g * self.i * self.i + self.h0
            self.i += 30
            return True
        return False

    def jump(self, power, angle):
        self.x = self.sens * self.i * power * cos(
            angle) + self.d0  # ...........................................equation horaire selon x
        self.y = self.convert * 0.5 * self.g * self.i * self.i + power * sin(
            angle) * self.i + self.h0  # .......equation horaire selon y
        self.i += 20
        #print("oh je saute", self.h0, self.y, self.i)
        self.draw(self.surface)

        if (self.i > 800):
            self.landed = True
            self.update_position()
        """
        diplay all things 
        """
        return

    def animation(self):

        if (self.frame == 12):
            self.frame = 0

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

        #print(self.frame)
