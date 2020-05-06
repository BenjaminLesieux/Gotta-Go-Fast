from pygame.sprite import *

class Lava(Sprite):

    def __init__(self):
        super().__init__()
        self.moving = False
        self.position = (0,720)
        self.image = pygame.image.load("images/lave_1.png").convert_alpha()
        self.x = 0
        self.y = 720
        self.speed = 0.5
        self.rect = self.image.get_rect()

    def move(self, delta_y):

        if self.moving:
            self.y -= self.speed - delta_y
    
    def is_moving(self, state):

        if (self.y == 0 or state == False):
            self.moving = False
        else:
            self.moving = True

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))
