import pygame as pygame

from entities.player import Player
from entities.platform import Platform
from gui.screen import Screen

screen = Screen((1600, 900))

player = Player((500, 500), "images/left.png")
platform = Platform((400, 400), True, "images/platforme V1.png")
platform2 = Platform((600, 400), True, "images/platforme V1.png")

screen.add_sprite(platform, platform2)
screen.register_player(player)

screen.run()
