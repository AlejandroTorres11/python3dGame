import math

# opciones generales

# pantalla
RES = WIDTH, HEIGHT = 1290, 720
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2

FPS = 60

# jugador
PLAYER_POS = 1.5, 5  # miniMap
PLAYER_ANGLE = 0
PLAYER_SPEED = 0.004
PLAYER_ROT_SPEED = 0.0025
PLAYER_SIZE_SCALE = 60

# ray cast
FOV = math.pi / 3  # equivale a 60°
HALF_FOV = FOV / 2
NUM_RAYS = WIDTH // 2  # si se modifica a un menor numero entonces hay bug visual
MAX_DEPTH = 800  # longitud maxima de un rayo
DELTA_ANGLE = FOV / NUM_RAYS  # diferencia de grados entre rayos

# proyectil
PROYECTILE_POS = PLAYER_POS  # miniMap
PROYECTILE_ANGLE = PLAYER_ANGLE
PROYECTILE_SPEED = 0.04

SCREEN_DIST = HALF_WIDTH / math.tan(HALF_FOV)  # distancia de la pantalla al jugador
SCALE = WIDTH // NUM_RAYS  # Ancho de cada columna de píxeles por rayo

# texturas
TEXTURE_WIDTH = 256
HALF_TEXTURE_WIDTH = TEXTURE_WIDTH // 2

# color del piso
#FLOOR_COLOR = (0, 80, 0)  # verde
FLOOR_COLOR = (112, 66, 20)  # marron grisaceo
ROOF_COLOR = (56, 33, 10)  # gris oscuro