from pygame.sprite import *
import time
from entities.trophy import Trophy


class Platform(Sprite):

    def __init__(self, position, mobile, image_link):
        super().__init__()
        self.position = position
        self.mobile = mobile
        self.image = pygame.image.load(image_link)
        self.rect = self.image.get_rect(center=position)
        self.loop = 0
        self.sens = False
        self.winnable = False
        self.x = position[0]
        self.y = position[1]
        self.trophy = None

    def is_winnable(self):
        return self.winnable

    def set_winnable(self, boolean, surface):
        self.winnable = boolean
        self.trophy = Trophy(self)
        self.trophy.draw(surface)

        
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
        if pygame.sprite.spritecollideany(player, platforms, None) != None and player.y_1 < player.y:
            # print("yes", end=" ")
            # print(player.rect.left, self.rect.left - 2/3 * player.image.get_height(), player.rect.right, self.rect.right + 2/3 * player.image.get_height(), player.rect.bottom, self.rect.bottom + 5, player.rect.bottom, self.rect.top - 5)
            if player.rect.left > self.rect.left - 2 / 3 * player.image.get_height() and player.rect.right < self.rect.right + 2 / 3 * player.image.get_height() and player.rect.bottom < self.rect.bottom + 5 and player.rect.bottom > self.rect.top - 5:
                #print("yes")
                """if player.rect.collidepoint(self.rect.topleft) == 1 and self.rect.collidepoint(player.rect.bottomright) == 1:
                    if (player.y != self.rect.top - player.image.get_height() + 1):
                        player.y = self.rect.top - player.image.get_height() + 1
                        player.update_position()
                if player.rect.collidepoint(self.rect.midtop) == 1 and self.rect.collidepoint(player.rect.midbottom) == 1:
                    if (player.y != self.rect.top - player.image.get_height() + 1):
                        player.y = self.rect.top - player.image.get_height() + 1
                        player.update_position()
                if player.rect.collidepoint(self.rect.topright) == 1 and self.rect.collidepoint(player.rect.bottomleft) == 1:
                    if (player.y != self.rect.top - player.image.get_height() + 1):
                        player.y = self.rect.top - player.image.get_height() + 1
                        player.update_position()"""
                if (player.y != self.rect.top - player.image.get_height() + 1):
                    player.y = self.rect.top - player.image.get_height() + 1
                    player.update_position()
                return 1
        return 0

"""
            elif player.rect.collidepoint(self.rect.bottomright) == 1 or player.rect.collidepoint(self.rect.bottomleft) == 1 or player.rect.collidepoint(self.rect.midbottom) == 1:
                player.y -= 20
                player.landed = True
"""