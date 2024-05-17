import pygame as pg
import sys
from settings import *
class Game:

    def __init__(self): #al iniciar un game
        pg.init()
        self.screen = pg.display.set_mode(RES)
        self.clock= pg.time.Clock()
        self.delta_time=1
        self.new_game()
    def new_game(self):
        self.player=Player(self)

    def update(self): #llamado cada frame
        pg.display.flip()
        self.clock.tick(FPS)
        pg.display.set_caption(f'{self.clock.get_fps() :.1f}') #actualiza el nombre de la ventana según los fps actuales

    def draw(self): #dibuja la pantalla
        self.screen.fill('black')
        self.player.draw()

    def checkEvents(self): #chequea si sales de la ventana para cerrar el programa
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type== pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                pg.exit()

    def run(self):
        while True:
            self.draw()
            self.update()
            self.checkEvents()

if __name__=='__main__':
    game=Game()
    game.run()
