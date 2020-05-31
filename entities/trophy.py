from pygame.sprite import *


class Trophy(Sprite):

    def __init__(self, platform):
        self.x = platform.x + 42
        self.y = int((platform.y + platform.rect.center[1])/2)-29
        self.image = pygame.image.load("images/casque.png").convert_alpha()
        self.platform = platform
        self.rect = self.image.get_rect(center = (self.x,self.y))

    def draw(self, surface):
        surface.blit(self.image, (self.x-31.5, self.y-25))
    
    def new_rect(self):
        self.rect = self.image.get_rect(center = (self.x,self.y))

    def collide_with(self, player):

        if (player.y - self.y+51 < 10) and self.rect.colliderect(player.rect):
            return "Win"
        else:
            return "None"
