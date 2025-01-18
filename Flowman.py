# Importing librarys
import random, pygame, time
from map import map
from spritesheet import spritesheet

# CONSTANTS
GAMECLOCK = 0.1
COLOR = (255, 100, 98)
RED = (255, 0, 0)
WHITE = (255, 255 ,255)
BLUE = (0 , 255 ,0 )
SURFACE_COLOR = (167, 255, 100)
BACKGROUND_COLOR = (0, 0, 0)
WIDTH = 1280
HEIGHT = 736
size = (WIDTH, HEIGHT)

# Pygame initialisation
pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Creating Sprite")
clock = pygame.time.Clock()

# Content loading
skelette = pygame.image.load("Sprite\squelette.png")
mur = pygame.image.load("flow_man sprite\decor\pac-mur.png")
flowman = spritesheet("flow_man sprite\\flowman.png")
char_images = flowman.image_at((0, 0, 32, 32))

# Initial stats
posX = 20
posY = 14
newPos = 0
face = 1

# Flowman functions
def move_up():
    global posY
    newPos = (posY - 1)
    if map[posY - 1][posX] != 3:
        posY = newPos


def move_down():
    global posY
    newPos = (posY + 1)
    if map[posY + 1][posX] != 3:
        posY = newPos


def move_left():
    global posX
    newPos = (posX - 1)
    if map[posY][posX - 1] != 3:
        posX = newPos


def move_right():
    global posX
    newPos = (posX + 1)
    if map[posY][posX + 1] != 3:
        posX = newPos


def rage():
    print("ok")


# CELLS : 0-PELLET 3-MUR
running = True
while running:
    time.sleep(GAMECLOCK)
    screen.fill(BACKGROUND_COLOR)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                face = 1

            if event.key == pygame.K_RIGHT:
                face = 3

            if event.key == pygame.K_UP:
                face = 4

            if event.key == pygame.K_DOWN:
                face = 2

    match face:
        case 1:
            move_left()
        case 2:
            move_down()
        case 3:
            move_right()
        case 4:
            move_up()

    y = -1
    for columns in map:
        y += 1
        x = -1
        for cell in columns:
            x += 1
            if (x == posX) and (y == posY):
                screen.blit(char_images, (x*32, y*32))
            else:
                match cell:
                    case 3:
                        screen.blit(mur, (x*32, y*32))
                    case 0:
                        screen.blit(skelette, (x*32, y*32))

    if posX == 5 and posY == -1:
        posX = 5
        posY = 22

    if posX == 5 and posY == 23:
        posX = 5
        posY = 0

    if posX == 34 and posY==-1:
        posX = 34
        posY = 22

    if posX == 34 and posY == 23:
        posX = 34
        posY = 0

    if map[posY][posX] == 0:
        map[posY][posX] = 8

    if map[posY][posX] == 0:
        rage()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()