import pygame
import sys
from gui.button import Button


class FinalScreen:

    def __init__(self, ggf):
        self.ggf = ggf
        self.activated = False
        self.menu = None
        self.leave = None
        self.retry = None
        self.game = False
        self.state = "None"
        self.time_font = pygame.font.Font("images/Fipps-Regular.otf", 30)
        self.times = []

    def is_activated(self):
        return self.activated

    def read_scores(self, level_name):
        file = open("high scores/" + level_name + ".txt", "r")
        lines = file.readlines()
        self.times = []
        for i in range(0, len(lines)):
            self.times.append(lines[i])
            if '\n' in self.times[i]:
                self.times[i] = self.times[i].replace('\n', '')
        file.close()

    def update_scores(self, new_score):
        for i in range(0, 3):
            self.times[i] = self.times[i].replace('\n', '')

            if new_score <= self.times[i]:
                if i == 0:
                    tmp = self.times[0]
                    self.times[0] = new_score
                    self.times[2] = self.times[1]
                    self.times[1] = tmp
                    break
                elif i == 1:
                    tmp = self.times[1]
                    self.times[1] = new_score
                    self.times[2] = tmp
                    break
                elif i == 2:
                    self.times[2] = new_score
                    break

    def save_scores(self, scores, level_name):
        file = open("high scores/" + level_name + ".txt", "w")
        for i in range(0, 3):
            file.write(scores[i] + '\n')
        file.close()

    def process(self, level_name):
        running = True
        click = False
        new = ['', '', '']
        self.time = str(self.ggf.timer)
        self.read_scores(level_name)

        if self.state == "Victoire":
            self.update_scores(self.time)

            for j in range(0, 3):
                i = 1
                if (self.time == self.times[j]):
                    new[j] = "New !"
                while (str(self.times[j][i]) != '.'):
                    i += 1
                self.times[j] = self.times[j].replace(self.times[j][i + 3:len(self.times[j])], "")

            self.save_scores(self.times, level_name)

        while running:

            highlight = "None"

            self.ggf.mode.blit(self.ggf.bg, [0, 0])
            if self.state == "Victoire":
                self.ggf.mode.blit(self.ggf.win, [448, 10])
            elif self.state == "Game over":
                self.ggf.mode.blit(self.ggf.lose, [448, 10])

            self.ggf.draw_text("Meilleurs scores : ", self.time_font, (255, 255, 255), self.ggf.mode, 430, 250)
            self.ggf.draw_text(self.times[0] + "s  " + new[0], self.time_font, (255, 255, 255), self.ggf.mode, 430, 300)
            self.ggf.draw_text(self.times[1] + "s  " + new[1], self.time_font, (255, 255, 255), self.ggf.mode, 430, 350)
            self.ggf.draw_text(self.times[2] + "s  " + new[2], self.time_font, (255, 255, 255), self.ggf.mode, 430, 400)
            self.retry = Button("Réessayer", 450, 70, (430, 500), self.ggf)
            self.menu = Button("Menu", 450, 70, (430, 600), self.ggf)

            if self.menu.collides():
                highlight = "Menu"
                if click:
                    running = False
                    self.activated = False
                    self.game = False
                    
            elif self.retry.collides():
                highlight = "Réessayer"
                if click:
                    self.activated = False
                    self.game = True
                    running = False

            else:
                click = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        click = True

            self.retry.render(highlight)
            self.menu.render(highlight)

            pygame.display.update()
