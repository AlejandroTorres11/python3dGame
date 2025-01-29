import pygame as pg
import math
from settings import *

class RayCasting:
    def __init__(self,game):
        self.game= game
        self.rayCastingResult= []
        self.objectsToRender=[]
        self.textures= self.game.spriteRenderer.wallTextures

    def getSpritesToRender(self):
        self.objectsToRender=[]
        for ray, values in enumerate(self.rayCastingResult):
            depth, projHeight, texture, offset = values
            if projHeight < HEIGHT:
                wallSlice = self.textures[texture].subsurface(offset * (TEXTURE_WIDTH - SCALE), 0, SCALE, TEXTURE_WIDTH)
                wallSlice = pg.transform.scale(wallSlice, (SCALE, projHeight))
                wallPos = (ray * SCALE, HALF_HEIGHT - projHeight // 2)
            else:
                textureHeight = TEXTURE_WIDTH * HEIGHT / projHeight
                wallSlice = self.textures[texture].subsurface(offset * (TEXTURE_WIDTH - SCALE), HALF_TEXTURE_WIDTH - textureHeight // 2, SCALE, textureHeight)
                wallSlice = pg.transform.scale(wallSlice, (SCALE, HEIGHT))
                wallPos = (ray * SCALE, 0)

            self.objectsToRender.append((depth, wallSlice, wallPos))

    def rayCast(self):
        self.rayCastingResult=[]
        textureHor,textureVer=1,1
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
                    textureHor= self.game.map.worldMap[tileHorizontal]
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
                    textureVer= self.game.map.worldMap[tileVertical]
                    break
                xVertical+=dx
                yVertical+=dy       
                depthVertical+= deltaDepth
            
            #depth, distancia al muro
            if(depthHorizontal>depthVertical):
                depth,texture=depthVertical, textureVer
                yVertical%=1
                offset= yVertical if cosA>0 else 1-yVertical
            else:
                depth, texture=depthHorizontal, textureHor
                xHorizontal%=1
                offset= xHorizontal if sinA<0 else (1-xHorizontal)

            #quitar efecto de ojo de pez
            depth*=math.cos(self.game.player.angle - rayAngle) #cuanto mas se aleja el rayo del centro, menor es el coseno de la diferencia 
                                                                #y menor el depth para compensar

            #projeccion
            projHeight= SCREEN_DIST/ (depth + 0.0001) #altura de la proyeccion de la pared

            #resultado raycasting
            self.rayCastingResult.append((depth,projHeight,texture,offset))
            #dibujar paredes blancas
            ''' 
            color=((255/(1+depth **5 * 0.00002)),) * 3
            pg.draw.rect(self.game.screen, color,
                        (ray*SCALE,HALF_HEIGHT - projHeight//2, SCALE, projHeight))
            '''
            #minimapa
            #pg.draw.line(self.game.screen,'yellow',(ox*100,oy*100), (100*ox+100*depth*cosA,100*oy +100*depth*sinA),2)

            rayAngle+=DELTA_ANGLE
            
    def update(self):
        self.rayCast()
        self.getSpritesToRender()