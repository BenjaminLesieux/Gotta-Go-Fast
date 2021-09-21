from pygame.sprite import *

pygame.mixer.init(44100, -16, 2, 2048)
trophy = pygame.mixer.Sound("images/fly.ogg")


class Trophy(Sprite):

    def __init__(self, platform, *groups):
        super().__init__(*groups)
        self.x = platform.x + 42
        self.y = int((platform.y + platform.rect.center[1]) / 2) - 29
        self.image = pygame.image.load("images/casque.png").convert_alpha()
        self.platform = platform
        self.rect = self.image.get_rect(center=(self.x, self.y))

    """
        Affiche le casque dans la fenêtre de jeu
    """

    def draw(self, surface):
        surface.blit(self.image, (self.x - 31.5, self.y - 25))

    """
        redéfinit le rectangle du casque
    """

    def new_rect(self):
        self.rect = self.image.get_rect(center=(self.x, self.y))

    """
        type string
        : return Win ou None - état de victoire du perso 
    """

    def collide_with(self, player):

        if (player.y - self.y + 51 < 10) and self.rect.colliderect(player.rect):
            trophy.play()
            return "Win"
        else:
            return "None"
