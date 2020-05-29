import pygame

class Lava():

    def __init__(self):
        super().__init__()
        self.moving = False
        self.position = (0, 700)
        self.image = pygame.image.load("images/lave_2.png").convert_alpha()
        self.x = -1 / 3 * self.image.get_width()
        self.y = 700
        self.speed = 0.5
        self.rect = self.image.get_rect()

    def move(self, delta_y):
        if self.moving:
            if self.y < 700:
                self.y -= (self.speed - 0.20*delta_y)
            else :
                self.y -= self.speed
    
    def is_moving(self, state):
        if (self.y == 0 or state == False):
            self.moving = False
        else:
            self.moving = True

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

    def new_rect(self):
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
    
    def collide_with(self, player):
        if self.rect.colliderect(player.rect):
            return "Lose"
        else:
            return "None"
