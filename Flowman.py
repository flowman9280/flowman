import random
import pygame
COLOR = (255, 100, 98)
RED = (255, 0, 0)
WHITE = (255, 255 ,255)
BLUE = (0 , 255 ,0 )
SURFACE_COLOR = (167, 255, 100)
WIDTH = 500
HEIGHT = 500
size = (WIDTH, HEIGHT)
pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Creating Sprite")
exit = True
clock = pygame.time.Clock()


posX: int = 0
posY: int = 0

map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

def move_up():
    newPos: int = posY - 1
    if map[posY][posX] != 1:
        posY = newPos
def move_down():
    newPos: int = posY + 1
    if map[posY][posX] != 1:
        posY = newPos
def move_left():
    newPos: int = posX - 1
    if map[posY][posX] != 1:
        posX = newPos
def move_right():
    newPos: int = posX + 1
    if map[posY][posX] != 1:
        posX = newPos

while exit:
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
    
    for rows in map:
        for cell in rows:
            match cell:
                pass

    

    pygame.display.flip()
    clock.tick(60)

pygame.quit()