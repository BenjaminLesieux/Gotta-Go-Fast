from pygame.sprite import *


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
        self.v = 0

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
            self.jump()

        self.update_position()

    def jump(self):

        if self.falling:
            return
        else:
            pass

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

    def jump(self, power, angle):
        pass
