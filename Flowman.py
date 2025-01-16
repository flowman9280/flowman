import random
import pygame
COLOR = (255, 100, 98)
RED = (255, 0, 0)
WHITE = (255, 255 ,255)
BLUE = (0 , 255 ,0 )
SURFACE_COLOR = (167, 255, 100)
WIDTH = 512
HEIGHT = 512
size = (WIDTH, HEIGHT)
pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Creating Sprite")
exit = True
clock = pygame.time.Clock()

skelette = pygame.image.load("Sprite\squelette.png")
flowman = pygame.image.load("Sprite\pac-man original.png")

posX = 1
posY = 1
newPos = 0

map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

def move_up():
    global posY
    newPos = (posY - 1)
    if map[posY-1][posX] != 1:
        posY = newPos
def move_down():
    global posY
    newPos = (posY + 1)
    if map[posY+1][posX] != 1:
        posY = newPos
def move_left():
    global posX
    newPos = (posX - 1)
    if map[posY][posX-1] != 1:
        posX = newPos
def move_right():
    global posX
    newPos = (posX + 1)
    if map[posY][posX+1] != 1:
        posX = newPos

while exit:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                exit = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                move_left()
            if event.key == pygame.K_RIGHT:
                move_right()
            if event.key == pygame.K_UP:
                move_up()
            if event.key == pygame.K_DOWN:
                move_down()

    newMap = map
    newMap[posY][posX] = 8

    x: int = 0
    y: int = 0
    for columns in map:
        y+=1
        x=0
        for cell in columns:
            x+=1
            match cell:
                case 1:
                    screen.blit(skelette, (x*30, y*30))
                case 2:
                    pass
                case 8:
                    screen.blit(flowman, (x*30, y*30))

    

    pygame.display.flip()
    clock.tick(60)

pygame.quit()