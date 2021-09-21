import pygame


class Lava():

    def __init__(self):
        super().__init__()
        self.moving = False
        self.position = (0, 700)
        self.image = pygame.image.load("images/lave_2.png").convert_alpha()
        self.x = -1 / 3 * self.image.get_width()
        self.y = 700
        self.speed = 0.6
        self.rect = self.image.get_rect()

    """
  Change la position verticale de la lave
    : Si elle peut monter (dépend du joueur)
        : Si elle est en dessous de 700 pixels, alors elle subit le décalage du fond d'écran
        : Sinon, elle ne fait que monter
    """

    def move(self, delta_y):
        if self.moving:
            if self.y < 700:
                self.y -= (self.speed - delta_y)
            else:
                self.y -= self.speed

    """
        Change l'état de la lave de ammovible à movible.
        Elle prend en paramètre l'état retourné par can_lava_move() et change l'état de la lave en fonction.
    """

    def is_moving(self, state):
        if not state:
            self.moving = False
        else:
            self.moving = True

    """
        Affiche la lave dans la fenêtre
    """

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

    """
        Redéfini la hitbox de la lave en fonction de sa position
    """

    def new_rect(self):
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    """
        Vérifie que le joueur rentre en collision avec la lave
        Si oui, 
            retourne le string "lose"
        sinon,
            retourne un string
    """

    def collide_with(self, player):
        if self.rect.colliderect(player.rect):
            return "Lose"
        else:
            return "None"
