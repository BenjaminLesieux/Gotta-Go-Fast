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
                            pygame.image.load("images/left2.png")]  # toutes les images du personnages
        self.image = self.list_images[0]
        self.rect = self.image.get_rect()
        self.surface = None
        self.x = position[0]
        self.y = position[1]
        self.y_1 = self.y  # coordonee y 1 frame avant celle actuelle
        self.ground = self.rect.bottom
        self.falling = False  # True si le joueur chute, mais pas d'un saut
        self.landed = True  # True si le joueur a atteri après un saut ou une chute
        self.power = 0.8  # equivalent à la vitesse initiale, trouvé avec experimentations
        self.alpha = 26  # 30 = vertical; 0 = horizontal
        self.angle = -self.alpha * pi / 60  # calcul de l'angle en RAD, selon alpha
        self.convert = ((38.2 / 1920) / 100)  # Pour un écran 17", 38.2 cm = 1920pix => 1 pix = (38.2/1920)/100m
        self.g = 9.81  # constante de gravitation
        self.sens = 1  # 1 : droite ; -1 : gauche ; 0 verticale
        self.i = 1  # variables itérative arbitraire (remplace la variable temporaire d'une vraie équation de trajectoire)
        self.d0 = self.x
        self.h0 = self.y
        self.dist_jump = 20
        self.dist_fall = 20
        self.frame = 0
        self.face = True
        self.dead = "None"
        self.speed = 0

    """
    :return position - la position du joueur
    :type - un tuple d'integer correspondant à la position du joueur
    """
    def get_position(self):
        return self.position

    """
    :desc - Retrace la hitbox du personnage pendant le saut
    """
    def update(self):
        self.rect.topleft = self.x, self.y
        self.position = self.x, self.y

    """
    :desc - Remet à jour les conditions initiales du saut
    :call - self.update()
    :call - self.new_rect()
    """
    def update_position(self):
        """ Mise à jour des conditions initiales """
        self.d0 = int(self.x)
        self.h0 = int(self.y)
        self.y = self.h0
        self.x = self.d0
        self.y_1 = self.y - 1
        self.i = 1
        self.update()
        self.new_rect()

    """
    :param decalage - Le décalage correspond au delta lorsque l'écran de jeu bouge 
    :return i
    :type integer
    """
    def move(self, decalage):
        """ Gestion des évènements """
        i = 0
        key = pygame.key.get_pressed()
        dist = 6  # la distance en 1 frame

        if (self.landed == False):
            """ Tant que le joueur n'a pas attéri, il continue son saut """
            self.angle = -self.alpha * pi / 60
            i = self.jump(self.power, self.angle)
            if self.can_defil():
                self.h0 += decalage  # compense le décalage verticale de la montée d'écran

        else:
            self.rect.left += 5
            self.rect.right += 5
            self.face = False
            if key[pygame.K_RIGHT] or key[pygame.K_d]:  # fleche de droite ou touche 'd'
                self.x += dist
                if (self.sens == 1 and self.speed < 6):  # vitesse de chute de plateforme
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


            elif key[pygame.K_LEFT] or key[pygame.K_a]:  # fleche de droite ou touche 'q' ('a' en qwerty)
                self.x -= dist
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

                elif key[pygame.K_DOWN] or key[pygame.K_s]:
                    if self.alpha > 20:
                        self.alpha -= 0.2
                        self.power -= 0.004


            elif key[pygame.K_SPACE]:
                self.update_position()
                self.landed = False
                self.power = 0.8
                i = self.dist_jump

            elif key[pygame.K_UP] or key[pygame.K_w]:
                if self.alpha < 28:
                    self.alpha += 0.2
                    self.power += 0.004

            elif key[pygame.K_DOWN] or key[pygame.K_s]:
                if self.alpha > 20:
                    self.alpha -= 0.2
                    self.power -= 0.004

            else:  # S'il ne se passe rien
                self.face = True
                self.sens = 0
                if self.landed == True:
                    self.speed = 0

        if self.y > 720:
            self.dead = "Lose"

        self.animation()
        return i

    """
    :desc - Dessine le joueur sur l'écran
    """
    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

    """
    :desc - S'occupe de la trajectoire verticale lors d'une chute
    """
    def fall(self):
        """ Trajectoire selon y uniquement, pour une chute verticale """
        self.y = self.convert * 0.5 * self.g * self.i * self.i + self.h0
        self.i += self.dist_fall

    """
    :param power - la puissance du saut
    :param angle - l'angle initial du saut
    """
    def jump(self, power, angle):
        self.x = self.sens * self.i * power * cos(angle) + self.d0  # equation horaire selon x
        self.y = self.convert * 0.5 * self.g * self.i ** 2 + power * sin(
            angle) * self.i + self.h0  # equation horaire selon y
        self.i -= self.dist_jump
        self.y_1 = self.convert * 0.5 * self.g * self.i ** 2 + power * sin(angle) * self.i + self.h0
        self.i += 2 * self.dist_jump
        self.new_rect()
        self.rect.bottomleft = int(self.x), int(self.y + self.image.get_height() + 5)
        self.rect.bottomright = int(self.x + self.image.get_width()), int(self.y + self.image.get_height() + 5)

        self.update()

        return self.i

    """
    :desc - Remet à jour le rectangle du joueur
    """
    def new_rect(self):
        self.rect = self.image.get_rect(center=self.position)

    """
    :desc - Anime le joueur pendant le mouvement
    """
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

    """
    :return True si elle peut, False sinon
    :type boolean
    """
    def can_lava_move(self):
        if self.y <= 500:  # Valeur à changer pour le début de montée de lave
            return True
        else:
            return False

    """
    :return True si elle peut, False sinon
    :type boolean
    """
    def can_defil(self):
        if self.y <= 300:  # Valeur à changer pour le début du fond d'écran
            return True
        else :
            return False

    """
    :desc - Pour ne pas que le joueur tombe verticalement d'une plateforme
    """
    def just_falling(self):
        if (self.falling == True):
            if self.sens == 1:
                self.x += self.speed
            else:
                self.x -= self.speed