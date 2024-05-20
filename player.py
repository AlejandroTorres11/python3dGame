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
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        dx, dy = 0, 0
        speed = PLAYER_SPEED * self.game.delta_time
        speed_sin = speed * sin_a
        speed_cos = speed * cos_a

        key = pg.key.get_pressed()
        if key[pg.K_w]:
            dx += speed_cos
            dy += speed_sin
        if key[pg.K_s]:
            dx += -speed_cos
            dy += -speed_sin
        if key[pg.K_a]:
            dx += speed_sin
            dy += -speed_cos
        if key[pg.K_d]:
            dx += -speed_sin
            dy += speed_cos
        
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
    def pos(self):  # saber coordenadas exactas del jugador
        return self.x, self.y
    
    @property
    def mapPos(self):  # saber en qué casilla está el jugador
        return int(self.x), int(self.y)
