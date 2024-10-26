import pygame as pg
from settings import *

class SpriteRenderer:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.wallTextures = self.loadWallTextures()

    def draw(self):
        self.renderGameSprites()

    def renderGameSprites(self, color=None):
        # Use self.game instead of passing 'game' as a parameter
        self.color = color if color else (255, 255, 255)
        for sprite in self.game.rayCasting.objectsToRender:
            depth, wallColumn, wallPos = sprite
            color = ((255 / (1 + depth ** 5 * 0.00002)),) * 3  # Default color is white
            wallColumn.fill(color, special_flags=pg.BLEND_MULT)
            self.screen.blit(wallColumn, wallPos)

    @staticmethod
    def getTexture(path, res=(TEXTURE_WIDTH, TEXTURE_WIDTH)):
        texture = pg.image.load(path).convert_alpha()
        return pg.transform.scale(texture, res)
    
    def loadWallTextures(self):
        return {
            1: self.getTexture('assets/wall/wall1.png'),
            2: self.getTexture('assets/wall/wall2.png'),
            3: self.getTexture('assets/wall/wall3.png'),
        }
