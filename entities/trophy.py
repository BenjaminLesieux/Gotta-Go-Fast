from pygame.sprite import *


class Trophy(Sprite):

    def __init__(self, platform):
        self.x = platform.x + 1
        self.y = platform.y + platform.rect.center
        self.image = pygame.image.load("images/trophy.png").convert_alpha()
        self.platform = platform

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))
