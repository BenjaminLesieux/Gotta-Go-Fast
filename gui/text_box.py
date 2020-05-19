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

    def draw(self, window):
        if self.active == False:
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

    def verifClick(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width and pos[1] > self.y and pos[1] < self.y + self.height:
            self.active = True
        else:
            self.active = False

    def addText(self, key):
        if self.caps == True:
            key = key - 32
        try:
            if (64 < key and key < 91) or (96 < key and key < 123) or (47 < key and key < 58):
                letter = chr(key)
                if letter == 'q':
                    letter = 'a'
                elif letter == 'w':
                    letter = 'z'
                elif letter == ';':
                    letter = 'm'
                elif letter == 'a':
                    letter = 'q'
                elif letter == 'z':
                    letter = 'w'
                elif letter == 'Q':
                    letter = 'A'
                elif letter == 'W':
                    letter = 'Z'
                elif letter == ':':
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

            elif key == 32:
                text = list(self.text)
                text.append(' ')
                self.text = "".join(text)


        except:
            print("oui")

    def getText(self):
        return self.text
