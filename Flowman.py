# Importing librarys
import random, pygame, time
from map import map
from spritesheet import spritesheet
from ennemy import Enemy

# CONSTANTS
GAMECLOCK = 0.15
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
eye = pygame.image.load("Sprite\Skelette2.png")
skelette = pygame.image.load("Sprite\squelette.png")
mur = pygame.image.load("flow_man sprite\decor\pac-mur.png")
flowman = spritesheet("flow_man sprite\\flowman.png")
char_images = flowman.image_at((0, 0, 32, 32))
pellet = pygame.image.load("louis\pelette.png")
pacgum = pygame.image.load("louis\\arduino.png")

# Initial stats
pface = 0
posX = 20
posY = 14
newPos = 0
face = 1
animationIndexX = 0
animationIndexY = 0

# Flowman functions
def move_up():
    global posY
    newPos = (posY - 1)
    if map[posY - 1][posX] != 3:
        posY = newPos



def move_down():
    global posY
    global face
    global pface
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
    global rag
    rag=1


def rot_center(image, rect, angle):
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = rot_image.get_rect(center=rect.center)
    return rot_image,rot_rect


def win():
    pass


one = Enemy(1, 1)

# CELLS : 1-PACGUM 0-PELLET 3-MUR
running = True
p = 0
while running:
    time.sleep(GAMECLOCK)
    screen.fill(BACKGROUND_COLOR)

    char_images = flowman.image_at((animationIndexX*32, animationIndexY*32, 32, 32))

    one.step(posX, posY)

    animationIndexX += 1

    if animationIndexX == 2:
        animationIndexY += 1
        animationIndexX = 0

    if animationIndexY == 2:
        animationIndexY = 0
        animationIndexX = 0

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pface = face
                if map[posY][posX - 1] != 3:
                    face = 1

            if event.key == pygame.K_RIGHT:
                pface = face
                if map[posY][posX + 1]  != 3:
                    face = 3

            if event.key == pygame.K_UP:
                pface = face
                if map[posY - 1][posX] != 3:
                    face = 4

            if event.key == pygame.K_DOWN:
                pface = face
                if map[posY + 1][posX] != 3:
                    face = 2

    match face:
        case 1:
            char_images = rot_center(char_images, pygame.Rect(0, 0, 32, 32), 180)[0]
            move_left()
        case 2:
            char_images = rot_center(char_images, pygame.Rect(0, 0, 32, 32), -90)[0]
            move_down()
        case 3:
            char_images = rot_center(char_images, pygame.Rect(0, 0, 32, 32), 0)[0]
            move_right()
        case 4:
            char_images = rot_center(char_images, pygame.Rect(0, 0, 32, 32), 90)[0]
            move_up()

    y = -1
    for columns in map:
        y += 1
        x = -1
        for cell in columns:
            x += 1
            if (x == posX) and (y == posY):
                screen.blit(char_images, (x*32, y*32))
            if (x == one.eposX) and (y == one.eposY):
                screen.blit(eye, (x*32, y*32))
                pygame.quit
            else:
                match cell:
                    case 2:
                        screen.blit(pacgum, (x*32, y*32))
                    case 3:
                        screen.blit(mur, (x*32, y*32))
                    case 0:
                        screen.blit(pellet, (x*32, y*32))
                    case 9:
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
        p += 1
    if p == 452:
        win()

    if map[posY][posX] == 2:
        map[posY][posX] = 8
        rage()

    

    pygame.display.flip()
    clock.tick(60)

pygame.quit()