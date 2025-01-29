import pygame as pg
from settings import *

class SpriteRenderer:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.wallTextures = self.loadWallTextures()
        #sky
        self.skyImage = self.getTexture('assets/sky/sky.png', (WIDTH, HEIGHT // 2)) 
        self.skyOffSet=0;
        

    def draw(self):
        self.drawBackground()
        self.renderGameSprites()

    def drawBackground(self):
        self.skyOffSet=(self.skyOffSet+400 *self.game.player.angleDiff)%WIDTH
        self.screen.blit(self.skyImage,(-self.skyOffSet,0))
        self.screen.blit(self.skyImage,(WIDTH-self.skyOffSet,0))
        #pg.draw.rect(self.screen, ROOF_COLOR, (0, 0, WIDTH, HALF_HEIGHT))
        pg.draw.rect(self.screen, FLOOR_COLOR, (0, HALF_HEIGHT, WIDTH, HALF_HEIGHT))

    def renderGameSprites(self, color=None):
        listaSprites = sorted(self.game.rayCasting.objectsToRender,key=lambda x:x[0],reverse=True)#segun depth
        self.color = color if color else (255, 255, 255)
        for sprite in listaSprites:
            depth, spriteSlice, spritePos = sprite
            color = ((255 / (1 + depth ** 5 * 0.00002)),) * 3  # Default color is white
            spriteSlice.fill(color, special_flags=pg.BLEND_MULT)
            self.screen.blit(spriteSlice, spritePos)
            
    @staticmethod
    def getTexture(path, res=(TEXTURE_WIDTH, TEXTURE_WIDTH)):
        texture = pg.image.load(path).convert_alpha()
        return pg.transform.scale(texture, res)
    
    def loadWallTextures(self):
        return {
            1: self.getTexture('assets/wall/wall_1.png'),
            2: self.getTexture('assets/wall/wall_2.png'),
            3: self.getTexture('assets/wall/wall_3.png'),
        }
