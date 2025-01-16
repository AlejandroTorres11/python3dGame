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
            lado=""
            sinA=math.sin(rayAngle)
            cosA=math.cos(rayAngle)
            wallHeight=1
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
                    valor = self.game.map.worldMap[tileHorizontal]  # Accede al valor en esa posición
                    digitoAltura= str(valor)[1] 
                    wallHeight= int(digitoAltura)
                    lado="H"
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
                    valor = self.game.map.worldMap[tileVertical]  # Accede al valor en esa posición
                    digitoAltura= str(valor)[1] 
                    wallHeight= int(digitoAltura)
                    lado="V"
                    break
                xVertical+=dx
                yVertical+=dy       
                depthVertical+= deltaDepth
            
            #depth
            if abs(depthHorizontal - depthVertical) < 0.0001:
                depth = depthVertical
                lado = "V"
            elif depthHorizontal > depthVertical:
                depth = depthVertical
                lado = "V"
            else:
                depth = depthHorizontal
                lado = "H"

            #remove fishbowl effect
            depth*=math.cos(self.game.player.angle - rayAngle)

            offset=0
            for i in range(0, wallHeight):
                # Calcula la altura de la proyección
                proj_height = SCREEN_DIST / (depth + 0.0001)
                # Dibuja las paredes
                color_intensity = 255 / (1 + depth ** 5 * 0.00002)
                if lado == "H":
                    color = [0, color_intensity * 0.5, 0]  # Verde oscuro para H (mitad de intensidad)
                elif lado == "V":
                    color = [0, color_intensity, 0]# Verde claro para V (intensidad completa)
                if i == 1:
                    if lado == "H":
                        color = [color_intensity * 0.5, 0, 0]  # Rojo oscuro para H
                    elif lado == "V":
                        color = [color_intensity, 0, 0]  # Rojo claro para 

                pg.draw.rect(self.game.screen, color,
                            (ray*SCALE,HALF_HEIGHT - proj_height//2 - offset, SCALE, proj_height))                
                offset += proj_height
            
            #minimap
            '''
            pg.draw.line(self.game.screen,'yellow',(ox*100,oy*100), (100*ox+100*depth*cosA,100*oy +100*depth*sinA),2)

            '''
            rayAngle+=DELTA_ANGLE
    def update(self):
        self.rayCast()