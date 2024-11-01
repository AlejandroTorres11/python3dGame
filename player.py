import pygame as pg
import math
from settings import *

class Player:
    def __init__(self, game):
        self.game = game
        self.x, self.y = PLAYER_POS
        self.angle = PLAYER_ANGLE
        self.angleDelta = 0  # Cambios en el ángulo

    def update(self):
        self.movement()
        self.checkWall(self.x, self.y)

    def movement(self):
        sinA = math.sin(self.angle)
        cosA = math.cos(self.angle)
        dx, dy = 0, 0
        speed = PLAYER_SPEED * self.game.delta_time
        speedSin = speed * sinA
        speedCos = speed * cosA

        key = pg.key.get_pressed()

        # Inicializa el cambio en el ángulo en cero
        self.angleDelta = 0
        
        # Movimiento adelante y atrás
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
        
        # Rotación con flechas
        if key[pg.K_LEFT]:
            self.angleDelta = -PLAYER_ROT_SPEED * self.game.delta_time
        if key[pg.K_RIGHT]:
            self.angleDelta = PLAYER_ROT_SPEED * self.game.delta_time
        
        # Actualiza el ángulo usando el cambio
        self.angle += self.angleDelta
        self.angle %= math.tau

        # Detectar colisiones con paredes
        self.checkWallCollision(dx, dy)
        
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
