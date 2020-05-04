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
        self.rect.center = self.x, self.y

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

    def collides_with(self, player):

        if player.rect.collidepoint(self.rect.topleft) == 1:
            print("topleft it is")
        elif player.rect.collidepoint(self.rect.topright) == 1:
            print("topright it is")
        elif player.rect.collidepoint(self.rect.bottomleft) == 1:
            print("bottomleft it is")
        elif player.rect.collidepoint(self.rect.bottomright) == 1:
            print("bottomright it is")
        elif player.rect.collidepoint(self.rect.midleft) == 1:
            print("midleft it is")
        elif player.rect.collidepoint(self.rect.midright) == 1:
            print("midright it is")
        elif player.rect.collidepoint(self.rect.midtop) == 1:
            print("midtop it is")
        elif player.rect.collidepoint(self.rect.midbottom) == 1:
            print("midbottom it is")

        return True
