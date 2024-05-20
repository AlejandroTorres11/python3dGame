import pygame as pg
import math as math
from settings import *

class Player:
    def __init__(self,game):
        self.game= game
        self.x, self.y= PLAYER_POS
        self.angle= PLAYER_ANGLE

    def update(self):
        self.movement()
        self.checkWall(self.x,self.y)

    def draw(self):                                                         #self.game.screen es la superficie
        #pg.draw.line(self.game.screen, 'yellow', (self.x *100, self.y *100 ), (self.x *100 + WIDTH * math.cos(self.angle),self.y *100 + WIDTH * math.sin(self.angle)),2)
        pg.draw.circle(self.game.screen,'green',(self.x*100,self.y*100 ),15)
    
    def movement(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        dx, dy = 0, 0
        speed = PLAYER_SPEED
        key = pg.key.get_pressed()
        
        if key[pg.K_w]:
            dx += speed * cos_a
            dy += speed * sin_a
        if key[pg.K_s]:
            dx -= speed * cos_a
            dy -= speed * sin_a
        if key[pg.K_a]:  # mueve a la izquierda
            dx += speed * sin_a
            dy -= speed * cos_a
        if key[pg.K_d]:  # mueve a la derecha
            dx -= speed * sin_a
            dy += speed * cos_a
        
        self.checkWallCollision(dx,dy)
        
        if key[pg.K_LEFT]:
            self.angle -= PLAYER_ROT_SPEED * self.game.delta_time
        if key[pg.K_RIGHT]:
            self.angle += PLAYER_ROT_SPEED * self.game.delta_time
            self.angle %= math.tau

    def checkWall(self,x,y):
        return (x,y) not in self.game.map.worldMap #chequea si coordenadas estan en las paredes

    def checkWallCollision(self,dx,dy):
        if self.checkWall(int(self.x+dx),int(self.y)): #se anticipa al movimiento, en x
            self.x += dx
        if self.checkWall(int(self.x),int(self.y + dy)):
            self.y +=dy
    @property
    def pos(self): #saber coordenadas exactas del jugador
        return self.x, self.y
    
    @property
    def mapPos(self): #saber en que casilla está el jugador
        return int(self.x), int(self.y)