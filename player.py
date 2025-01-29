import pygame as pg
import math
from settings import *

class Player:
    def __init__(self, game):
        self.game = game
        self.x, self.y = PLAYER_POS
        self.angle = PLAYER_ANGLE
        self.prevAngle=0;
        self.angleDiff = 0
    def update(self):
        self.movement()
        self.checkWall(self.x, self.y)
        #print(self.angle)
        print(self.angleDiff)
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
        
        self.prevAngle = self.angle
        if key[pg.K_LEFT]:
            self.angle -= PLAYER_ROT_SPEED * self.game.delta_time
        if key[pg.K_RIGHT]:
            self.angle += PLAYER_ROT_SPEED * self.game.delta_time
        
        
        # diferencia ajustada
        self.angleDiff = self.angle - self.prevAngle
        if self.angleDiff > math.pi:
            self.angleDiff -= 2 * math.pi
        elif self.angleDiff < -math.pi:
            self.angleDiff += 2 * math.pi
            

    def checkWall(self, x, y):
        return (x, y) not in self.game.map.worldMap  # chequea si las coordenadas están en las paredes

    def checkWallCollision(self, dx, dy):
        scale=PLAYER_SIZE_SCALE/self.game.delta_time
        if self.checkWall(int(self.x + dx * scale), int(self.y)):  # se anticipa al movimiento en x
            self.x += dx
        if self.checkWall(int(self.x), int(self.y + dy* scale)):  # se anticipa al movimiento en y
            self.y += dy

    @property
    def position(self):  # saber coordenadas exactas del jugador
        return self.x, self.y
    
    @property
    def mapPosition(self):  # saber en qué casilla está el jugador
        return int(self.x), int(self.y)
