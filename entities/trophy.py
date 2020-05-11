from pygame.sprite import *


class Trophy(Sprite):

    def __init__(self, platform):
        self.x = platform.x + 1
        self.y = platform.y + platform.rect.center[1]
        self.image = pygame.image.load("images/trophy.png")
        self.platform = platform

    def draw(self, surface):
        print(self.x, ', ', self.y)
        surface.blit(self.image, (self.x, self.y))
