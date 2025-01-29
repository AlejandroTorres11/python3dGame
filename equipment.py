import pygame as pg
from settings import *

class Equipment:
    def __init__(self, game, path, scale):
        self.game = game
        self.player = game.player
        self.image = pg.image.load(path).convert_alpha()
        
        # Escalado de la imagen
        self.SPRITE_SCALE = scale
        new_width = int(self.image.get_width() * scale)
        new_height = int(self.image.get_height() * scale)
        self.imageScaled = pg.transform.smoothscale(self.image, (new_width, new_height))

        # Posición centrada
        self.pos = (HALF_WIDTH - new_width // 2, HEIGHT - new_height)

    def draw(self):
        self.game.screen.blit(self.imageScaled, self.pos)

    def update(self):
        pass
