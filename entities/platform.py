from pygame.sprite import *


class Platform(Sprite):

    def __init__(self, position, mobile, image_link):
        super().__init__()
        self.position = position
        self.mobile = mobile
        self.image = pygame.image.load(image_link).convert_alpha()
        self.rect = self.image.get_rect(center=position)
        
    def get_position(self):
        return self.position

    def is_mobile(self):
        return self.mobile

    def move(self):
        if self.mobile:
            print("I'm moving")
