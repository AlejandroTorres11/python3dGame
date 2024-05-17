from settings import *
class Player:
    def __init__(self,game):
        self.game= game
        self.x, self.y= PLAYER_POS
        self.angle= PLAYER_ANGLE

    def __update__(self):
        self.draw

    def draw(self):                                                         #self.game.screen es la superficie
        pg.draw.line(self.game.screen, 'yellow', (self.x *100, self.y *100), (self.x *100 + WITDH * math.cos(self.angle),self.y *100 + WITDH * math.sin(self.angle)),2)
        pg.draw.circle(self.game.screen,'green',(self.x*100,self.y *100),15)