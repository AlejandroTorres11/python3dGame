import pygame as pg
import math
from settings import *

class Prop:
    def __init__(self,game,pos,path,scale,altura): #altura sobre el nivel del suelo, podria haber objetos voladores
        self.game=game
        self.player=game.player
        self.x,self.y=pos
        self.image=pg.image.load(path).convert_alpha()
        self.IMAGE_WIDTH= self.image.get_width()
        self.IMAGE_HALF_WIDTH= self.IMAGE_WIDTH//2
        self.IMAGE_RATIO=self.IMAGE_WIDTH/self.image.get_height()
        self.dx,self.dy=0,0
        self.SPRITE_SCALE=scale 
        self.dist=0 #distancia al jugadorç
        self.fixedDist=0
        self.angle=0 #angulo con respecto al jugador
        self.visible=False
        self.screenX=0
        self.spriteHalfWidth=0
        self.SPRITE_ALTURA=altura

    def getSpriteProjection(self):
        proj=SCREEN_DIST/self.fixedDist* self.SPRITE_SCALE
        projWidth,projHeight=proj*self.IMAGE_RATIO,proj

        image=pg.transform.scale(self.image,(projWidth,projHeight))

        self.spriteHalfWidth=projWidth//2
        heightToFloor=projHeight * self.SPRITE_ALTURA
        pos= self.screenX - self.spriteHalfWidth, HALF_HEIGHT - projHeight//2+heightToFloor

        self.game.rayCasting.objectsToRender.append((self.fixedDist, image, pos))
    def getProp(self):
        dx=self.x-self.game.player.x
        dy=self.y-self.game.player.y
        angle=math.atan2(dy,dx)
        diffAngle=self.game.player.angle-angle #falta normalizar los angulos del player
        
        #cosas de pi con el circulo y tal
        if diffAngle<-math.pi:
            diffAngle+=2*math.pi
        if diffAngle>math.pi:
            diffAngle-=2*math.pi
        
        angleNumRaysDiff= -diffAngle/DELTA_ANGLE #La diferencia de ángulo entre el sprite y el centro de visión del jugador.
        self.screenX=((NUM_RAYS//2) + angleNumRaysDiff)*SCALE

        self.dist = math.sqrt((self.x - self.game.player.x)**2 + (self.y - self.game.player.y)**2)
        self.fixedDist=self.dist*math.cos(diffAngle)
        if -self.IMAGE_HALF_WIDTH<self.screenX<(WIDTH+self.IMAGE_HALF_WIDTH) and self.fixedDist>0.5:
            self.getSpriteProjection()
            return True
        if(diffAngle<HALF_FOV):
            self.visible=True
        else:
            self.visible=False

    def update(self):
        self.getProp()