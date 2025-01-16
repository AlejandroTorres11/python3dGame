import pygame as pg
import math
from settings import *

class Player:
    def __init__(self, game):
        self.game = game
        self.x, self.y = PLAYER_POS
        self.angle = PLAYER_ANGLE

    def update(self):
        self.movement()
        self.checkWall(self.x, self.y)

    def draw(self):
        pg.draw.circle(self.game.screen, 'green', (int(self.x * 100), int(self.y * 100)), 15)
    
    def movement(self):
        sinA = math.sin(self.angle)
        cosA = math.cos(self.angle)
        dx, dy = 0, 0   #diferencia x
        speed = PLAYER_SPEED * self.game.delta_time
        speedSin = speed * sinA
        speedCos = speed * cosA

        key = pg.key.get_pressed()
        if key[pg.K_w]:
            dx += speedCos
            dy += speedSin
        if key[pg.K_s]:
            dx += -speedCos
            dy += -speedSin
        if key[pg.K_a]:
            dx += speedSin
            dy += -speedCos
        if key[pg.K_d]:
            dx += -speedSin
            dy += speedCos
        
        self.checkWallCollision(dx, dy)
        
        if key[pg.K_LEFT]:
            self.angle -= PLAYER_ROT_SPEED * self.game.delta_time
        if key[pg.K_RIGHT]:
            self.angle += PLAYER_ROT_SPEED * self.game.delta_time
            self.angle %= math.tau

    def checkWall(self, x, y):
        return (x, y) not in self.game.map.worldMap  # chequea si las coordenadas están en las paredes

    def checkWallCollision(self, dx, dy):
        if self.checkWall(int(self.x + dx), int(self.y)):  # se anticipa al movimiento en x
            self.x += dx
        if self.checkWall(int(self.x), int(self.y + dy)):  # se anticipa al movimiento en y
            self.y += dy

    @property
    def position(self):  # saber coordenadas exactas del jugador
        return self.x, self.y
    
    @property
    def mapPosition(self):  # saber en qué casilla está el jugador
        return int(self.x), int(self.y)
