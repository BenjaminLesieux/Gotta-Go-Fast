from pygame.sprite import *


class Player(Sprite):

    def __init__(self, position, image_link):
        super().__init__()
        self.position = position
        self.image = pygame.image.load(image_link).convert_alpha()
        self.rect = self.image.get_rect(center=position)
        self.x = position[0]
        self.y = position[1]

    def get_position(self):
        return self.position

    def move(self):
        """ Gestion des évènements """
        key = pygame.key.get_pressed()
        dist = 5  # la distance en 1 frame
        if key[pygame.K_DOWN]:  # down key
            self.y += dist  # down
        elif key[pygame.K_UP]:  # up key
            self.y -= dist  # up
        if key[pygame.K_RIGHT]:  # right key
            self.x += dist  # right
        elif key[pygame.K_LEFT]:  # left key
            self.x -= dist  # left

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

    def jump(self, power, angle):
        pass
