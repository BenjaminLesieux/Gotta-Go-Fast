import pygame


class TextBox:
    def __init__(self, surface, x, y, width, height, passive_text=''):
        self.surface = surface
        self.x = x
        self.y = y
        self.pos = (self.x, self.y)
        self.width = width
        self.height = height
        self.image = pygame.Surface((width, height))
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)
        self.color = (255, 255, 255)
        self.black = (0, 0, 0)
        self.active_color = (220, 220, 220)
        self.active = False
        self.passive_text = passive_text
        self.text = ''
        self.caps = False
        self.font = pygame.font.Font('images/Fipps-Regular.otf', height // 2)
        self.passive_font = pygame.font.Font('images/Fipps-Regular.otf', height // 3)

    """
    :param window - une surface sur laquelle dessiner 
    :desc - dessine la textbox à l'écran
    """

    def draw(self, window):
        if not self.active:
            self.image.fill(self.black)
            pygame.draw.rect(self.image, self.color, (1, 1, self.width - 2, self.height - 2))
            text = self.font.render(self.text, False, (109, 0, 0))
            if len(self.text) == 0:
                passive_text = self.passive_font.render(self.passive_text, False, (220, 220, 220))
                self.image.blit(passive_text, (4, 10))
            self.image.blit(text, (4, -5))
        else:
            self.image.fill(self.black)
            pygame.draw.rect(self.image, self.active_color, (1, 1, self.width - 2, self.height - 2))
            text = self.font.render(self.text, False, (109, 0, 0))
            text_width = text.get_width()
            if text_width < self.width - 2:
                self.image.blit(text, (4, -5))
            else:
                self.image.blit(text, ((4 + (self.width - text_width - 6)), -5))

        window.blit(self.image, self.pos)

    """
    :param pos - position du clic
    :desc - vérifie si l'on clique sur la textbox 
    """

    def verifClick(self, pos):
        if self.x < pos[0] < self.x + self.width and self.y < pos[1] < self.y + self.height:
            self.active = True
        else:
            self.active = False

    """
    :param key - la touche pressée 
    :desc - Ajoute du texte dans la textbox 
    """

    def addText(self, key):
        if (47 < key < 58) or (255 < key < 266):
            self.caps = False
            if 255 < key < 266:
                key = key - 208
        if self.caps:
            key = key - 32
        elif key == 13:
            self.active = False

        try:
            if key != 109 and key != 77:
                if key == 59 or key == 27 or (64 < key < 91) or (96 < key < 123) or (47 < key < 58):
                    letter = chr(key)
                    if letter == 'q':
                        letter = 'a'
                    elif letter == 'w':
                        letter = 'z'
                    elif key == 59:
                        letter = 'm'
                    elif letter == 'a':
                        letter = 'q'
                    elif letter == 'z':
                        letter = 'w'
                    elif letter == 'Q':
                        letter = 'A'
                    elif letter == 'W':
                        letter = 'Z'
                    elif key == 27:
                        letter = 'M'
                    elif letter == 'A':
                        letter = 'Q'
                    elif letter == 'Z':
                        letter = 'W'
                    text = list(self.text)
                    text.append(letter)
                    self.text = "".join(text)

                elif key == 8:  # backspace
                    text = list(self.text)
                    text.pop()
                    self.text = "".join(text)

                elif key == 32:  # space
                    text = list(self.text)
                    text.append(' ')
                    self.text = "".join(text)
        except ValueError:
            print("Error")

    def getText(self):
        return self.text
