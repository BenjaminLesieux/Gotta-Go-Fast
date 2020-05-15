from pygame.sprite import *


class Trophy(Sprite):

    def __init__(self, platform):
        self.x = platform.x + 42
        self.y = int((platform.y + platform.rect.center[1])/2)-29
        self.image = pygame.image.load("images/trophy.png").convert_alpha()
        self.platform = platform
        self.rect = self.image.get_rect(center = (self.x,self.y))

    def draw(self, surface):
        #print(self.x, ', ', self.y)
        #pygame.draw.rect(surface, pygame.Color('blue'), self.rect)
        surface.blit(self.image, (self.x-31.5, self.y-25))
    
    def new_rect(self):
        self.rect = self.image.get_rect(center = (self.x,self.y))

    def collide_with(self, player):

        if self.rect.colliderect(player.rect):
            return "Win"
        else:
            return "None"
