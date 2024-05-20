import pygame as pg
import math
from settings import *

class RayCasting:
    def __init__(self,game):
        self.game= game
    
    def rayCast(self):
        ox,oy= self.game.player.pos
        xMap,yMap= self.game.player.mapPos
        rayAngle= self.game.player.angle - HALF_FOV +0.0001
        for ray in range(NUM_RAYS):
            sinA=math.sin(rayAngle)
            cosA=math.cos(rayAngle)
            #lineas horizontales de la casilla
            if sinA>0: #miramos arriba
                yHor,dy=(yMap +1,1)
            else:
               yHor,dy=(yMap-0.000001,-1)
            depthHor=(yHor-oy)/sinA      
            xHor=ox + cosA*depthHor

            deltaDepth=dy/sinA
            dx=deltaDepth * cosA

            for i in range(MAX_DEPTH):
                tileHor=int(xHor),int(yHor)
                if tileHor in self.game.map.worldMap:
                    break
                xHor+=dx
                yHor+=dy
                depthHor+= deltaDepth

            #lineas verticales de la casilla
            
            if cosA>0: #significa que miramos a derecha
                xVert,dx=(xMap+1,1)
            else: #si miramos a izquierda
                xVert,dx=(xMap-0.000001,-1)

            depthVert=(xVert -ox)/cosA #trigonometria para conocer la hipotenusa
            yVert=oy + sinA* depthVert #al conocer la hipotenusa y elseno del angulo podemos calcular la posicion del rayo en y
            deltaDepth= dx/cosA  #deltaDepth es la distancia al siguiente cuadrante
            dy= deltaDepth * sinA
            for i in range(MAX_DEPTH):
                tileVert= int(xVert),int(yVert)
                if tileVert in self.game.map.worldMap:
                    break
                xVert+=dx
                yVert+=dy       
                depthVert+= deltaDepth
            
            #depth
            if(depthHor>depthVert):
                depth=depthVert
            else:
                depth=depthHor

            pg.draw.line(self.game.screen,'yellow',(ox*100,oy*100), (100*ox+100*depth*cosA,100*oy +100*depth*sinA),2)
            rayAngle+=DELTA_ANGLE
    def update(self):
        self.rayCast()