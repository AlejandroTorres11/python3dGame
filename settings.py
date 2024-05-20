import math

#opciones generales

#pantalla
RES = WIDTH, HEIGHT = 1600,900
FPS=60

#jugador
PLAYER_POS=1.5 , 5 #miniMap
PLAYER_ANGLE= 0
PLAYER_SPEED= 0.04
PLAYER_ROT_SPEED = 0.05
#ray cast
FOV = math.pi/3 
HALF_FOV= FOV/2
NUM_RAYS=120
MAX_DEPTH= 800  #longitud maxima de un rayo
DELTA_ANGLE= FOV/NUM_RAYS #diferencia de grados entre rayos
#proyectil
PROYECTILE_POS=PLAYER_POS #miniMap
PROYECTILE_ANGLE= PLAYER_ANGLE
PROYECTILE_SPEED= 0.04
