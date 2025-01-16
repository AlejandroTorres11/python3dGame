import pygame as pg

_= False

miniMap = [
    [11, 11, 11, 11, 11, 11, 11, 11, 12, 12, 11, 11, 11, 11, 11, 11],
    [11,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _, 11],
    [11,  _,  _, 11, 11, 11, 11,  _,  _,  _,  _,  _,  _,  _,  _, 11],
    [11,  _,  _,  _,  _,  _, 11,  _,  _,  _,  _,  _,  _,  _,  _, 11],
    [11,  _,  _,  _,  _,  _, 11,  _,  _,  _,  _,  _,  _,  _,  _, 11],
    [11,  _,  _, 11, 11, 11, 11,  _,  _,  _,  _, 12, 12,  _,  _, 11],
    [11,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _, 12,  _,  _,  _, 11],
    [11,  _,  _, 11,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _,  _, 11],
    [11, 11, 11, 11, 11, 11, 11, 11, 12, 12, 11, 11, 11, 11, 11, 11],
]


class Map:
    def __init__(self, game):
        self.game= game
        self.miniMap= miniMap
        self.worldMap= {}
        self.getMap()

    def getMap(self):
        for j,row in enumerate(self.miniMap):#row es el valor [1,_,1] y j es el indice (0), por ejemplo 
            for i, value in enumerate(row):#value es el valor [1] e i es el indice [0]
                if value:
                    self.worldMap[(i,j)]= value

    def draw(self):
        for pos in self.worldMap:
            pg.draw.rect(self.game.screen, 'darkgray',(pos[0]*100,pos[1]*100,100,100),2)
        
