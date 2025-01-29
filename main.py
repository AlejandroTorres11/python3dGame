import pygame as pg
import sys
from settings import *
from map import *
from player import *
from raycasting import *
from spriteRenderer import *
from prop import *
class Game:

    def __init__(self): #al iniciar un game
        pg.init()
        self.screen = pg.display.set_mode(RES)
        self.clock= pg.time.Clock()
        self.delta_time=1
        self.new_game()

    def new_game(self):
        self.player=Player(self)
        self.map=Map(self)
        self.spriteRenderer=SpriteRenderer(self)
        self.rayCasting= RayCasting(self)
        self.prop=Prop(self,(10.5,3.5),'assets/weapons/crossbow.png',5)

    def update(self): #llamado cada frame
        self.player.update()
        self.rayCasting.update()
        self.prop.update()
        pg.display.flip()
        self.delta_time=self.clock.tick(FPS)
        #print(self.delta_time)
        pg.display.set_caption(f'{self.clock.get_fps() :.1f}') #actualiza el nombre de la ventana según los fps actuales

    def draw(self): #dibuja la pantalla
        #self.screen.fill('black')
        self.spriteRenderer.draw()
        self.player.draw()
        self.map.draw()
        
    def checkEvents(self): #chequea si sales de la ventana para cerrar el programa
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type== pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                pg.exit()

    def run(self):
        while True:
            self.checkEvents()
            self.update()
            self.draw()

if __name__=='__main__':
    game=Game()
    game.run()
