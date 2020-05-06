from pygame.sprite import *


class Platform(Sprite):

    def __init__(self, position, mobile, image_link):
        super().__init__()
        self.position = position
        self.mobile = mobile
        self.image = pygame.image.load(image_link)
        self.rect = self.image.get_rect(center=position)
        self.loop = 0
        self.sens = False
        self.x = position[0]
        self.y = position[1]
        
    def get_position(self):
        return self.position

    def is_mobile(self):
        return self.mobile

    def move(self):

        if self.mobile:

            if self.sens:
                self.x += 5
            else:
                self.x -= 5

            if self.x == self.position[0] + 40:
                self.sens = False
            if self.x == self.position[0] - 40:
                self.sens = True

        self.rect.topleft = self.x, self.y

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

    def move_y(self, delta_y):
        self.y += delta_y

    def collides_with(self, player, platforms):
        if pygame.sprite.spritecollideany(player, platforms, None) != None:
            if player.rect.collidepoint(self.rect.bottomleft) == 1:
                return 0
            elif player.rect.collidepoint(self.rect.midbottom) == 1:
                return 0
            elif player.rect.collidepoint(self.rect.bottomright) == 1:
                return 0
            """else:
                print("top")"""
            return 1
        return 0
