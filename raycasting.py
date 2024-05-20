import pygame as pg
import math
from settings import *

class RayCasting:
    def __init__(self,game):
        self.game= game
    
    def rayCast(self,player):
        ox,oy= self.game.player.pos
        xMap,yMap= self.game.player.mapPos
        rayAngle= self.game.player.angle - HALF_FOV +0.0001
        for ray in range(NUM_RAYS):
            sinA=math.sin(rayAngle)
            cosA=math.cos(rayAngle)

            #lineas verticales de la casilla
            if cosA>0: #significa que miramos a derecha
                xVert,dx=(xMap+1,1)
            else: #si miramos a izquierda
                xVert,dx=xMap-1e-6,-1 
            depthVert=(xVert -ox)/cosA #trigonometria
            yVert=oy + sinA* depthVert

            for i in range(MAX_DEPTH):
                tileVert= int(xVert),int(yVert)
                if tileVert in self.game.map.worldMap:
                    break
                xVert+=dx
                yVert+=dy
                depthVert+= deltaDepth
            deltaDepth= dx/cosA  #deltaDepth es la distancia al siguiente cuadrante
            dy= deltaDepth * sinA
            rayAngle+=DELTA_ANGLE
            pg.draw.line(self.game.screen,'yellow',(self.x *100, self.y *100 ), (ox+MAX_DEPTH*sinA,oy +MAX_DEPTH*cosA),2)    
    def update(self):
        self.rayCast()