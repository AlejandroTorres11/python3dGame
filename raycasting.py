import pygame as pg
import math
from settings import *

class RayCasting:
    def __init__(self,game):
        self.game= game
    
    def rayCast(self):
        ox,oy= self.game.player.position
        xMap,yMap= self.game.player.mapPosition
        rayAngle= self.game.player.angle - HALF_FOV +0.0001
        for ray in range(NUM_RAYS):
            sinA=math.sin(rayAngle)
            cosA=math.cos(rayAngle)
            #lineas horizontales de la casilla
            if sinA>0: #miramos arriba
                yHorizontal,dy=(yMap +1,1)
            else:
               yHorizontal,dy=(yMap-0.000001,-1)
            depthHorizontal=(yHorizontal-oy)/sinA      
            xHorizontal=ox + cosA*depthHorizontal

            deltaDepth=dy/sinA
            dx=deltaDepth * cosA

            for i in range(MAX_DEPTH):
                tileHorizontal=int(xHorizontal),int(yHorizontal)
                if tileHorizontal in self.game.map.worldMap:
                    break
                xHorizontal+=dx
                yHorizontal+=dy
                depthHorizontal+= deltaDepth

            #lineas verticales de la casilla
            
            if cosA>0: #significa que miramos a derecha
                xVertical,dx=(xMap+1,1)
            else: #si miramos a izquierda
                xVertical,dx=(xMap-0.000001,-1)

            depthVertical=(xVertical -ox)/cosA #trigonometria para conocer la hipotenusa
            yVertical=oy + sinA* depthVertical #al conocer la hipotenusa y elseno del angulo podemos calcular la posicion del rayo en y
            deltaDepth= dx/cosA  #deltaDepth es la distancia al siguiente cuadrante
            dy= deltaDepth * sinA
            for i in range(MAX_DEPTH):
                tileVertical= int(xVertical),int(yVertical)
                if tileVertical in self.game.map.worldMap:
                    break
                xVertical+=dx
                yVertical+=dy       
                depthVertical+= deltaDepth
            
            #depth
            if(depthHorizontal>depthVertical):
                depth=depthVertical
            else:
                depth=depthHorizontal

            pg.draw.line(self.game.screen,'yellow',(ox*100,oy*100), (100*ox+100*depth*cosA,100*oy +100*depth*sinA),2)
            rayAngle+=DELTA_ANGLE
    def update(self):
        self.rayCast()