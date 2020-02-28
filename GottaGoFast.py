import pygame as pygame

from entities.player import Player
from entities.platform import Platform
from gui.screen import Screen

screen = Screen((1600, 900))

player = Player((300, 300), "images/face.png")
plat1 = Platform((400, 400), True, "images/plateforme 1 V2.png")
plat2 = Platform((400, 500), True, "images/plateforme 2 V2.png")

screen.add_sprite(player, plat1, plat2)

screen.run()
