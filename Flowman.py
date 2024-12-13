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

pos = {
    x: 0,
    y: 0,
}


pygame.init()
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Creating Sprite")
 
exit = True
clock = pygame.time.Clock()

while exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                exit = False
    pygame.display.flip()
    clock.tick(60)

pygame.quit()