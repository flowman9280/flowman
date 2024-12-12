
import random
import pygame
 
# Global Variables
WHITE= (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0 0,)
COLOR = (255, 100, 98)
SURFACE_COLOR = (167, 255, 100)
WIDTH = 500
HEIGHT = 500
 
# Object class
class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()
 
        self.image = pygame.Surface([width, height])
        self.image.fill(SURFACE_COLOR)
        self.image.set_colorkey(COLOR)
 
        pygame.draw.rect(self.image,
                         color,
                         pygame.Rect(0, 0, width, height))
 
        self.rect = self.image.get_rect()
        self.image = pygame.image.load("Sprite\pac-man original.png")
 
    def moveRight(self, pixels):
        self.rect.x += pixels
 
    def moveLeft(self, pixels):
        self.rect.x -= pixels
 
    def moveForward(self, speed):
        self.rect.y += speed * speed/10
 
    def moveBack(self, speed):
        self.rect.y -= speed * speed/10

pygame.display.set_caption("Creating Sprite")
 
all_sprites_list = pygame.sprite.Group()
 
playerCar = Sprite(RED, 20, 30)
playerCar.rect.x = 200
playerCar.rect.y = 300
 
all_sprites_list.add(playerCar)
 
exit = True
clock = pygame.time.Clock()
 
class Jewel(object):
    """Class to hold Jewel sprite properties"""

    def __init__(self, pos):
        jewels.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)
        
class Wall(object):
    """Class to hold Wall sprite properties"""

    def __init__(self, pos):
        walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)

walls = [] #List to contain walls
jewels = []#List to contain Jewels

#!-----------------------Maze Layout----------------------!

#Table used to create the level, where W = wall
level = [
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"W       J               W          JJJ           W",
"W                       W     W                  W",
"W    WWWW   WWWWW   WWWWW     W      WWWWWWWWWW  W",
"W    W          W       W     W           W      W",
"W    W      JJJJ        W   WWWWWWW       W      W",
"W    W   WW                    W          W      W",
"W    W    W     WWWW           W          W      W",
"W    WWW  W     W  W           W  W   WWWWW      W",
"W         W                    W  W              W",
"WWWW      WWWWWWWWWWWWWWWWWWWWWW                 W",
"W  W     WW                    W                 W",
"W       WW                     W WWWWWWWWWWWWWWWWW",
"W             WWW              W                 W",
"W   WW               WW  WWW   W                 W",
"W    W  WWW          WWWWWWW   WWWWWWWWWWWWWWWW  W",
"W    W    W   WWW       WW         W          W  W",
"W    WW   W                            W      W  W",
"W     W   W          WWWWWWWWWWWWWWWWWWWWWWWW W  W",
"WWWW      WWWWW      WW  WWW                  W  W",
"W  W      W                W  WWWWWWWWWWWWWWWWW  W",
"W  W   WWWW     W  W       W     W               W",
"W      W           W  WWW  W            W        W",
"W      WWWW        W  W    WWWWWWWWWWWWWWWWWWWWWWW",
"W  WW     W   WWW  W  W      JJJ                 W",
"W   W     W        W  W                     J    W",
"W   W   WWW           W    WWW                   W",
"W  WWW       WWWWWWWWWW      WWWW                W",
"W    W       W                  WWWWWWW    W     W",
"WW   W    WWWW        WWWWWW          WWWW WWWW  W",
"WJ   W                   W            W    W     W",
"W     W  J    WWW           WWWWW    W    W  WWWW",
"WWW   W        W      W               W WWWW     W",
"W W       WWWWWW   WWWW               W    W     W",
"W WWW     W        W         WWWWW    WWWW WWWWW W",
"W       WWW        W     W               W       W",
"W       W                W               W       W",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
]

#Draw the wall rects as shown in the table above
x = y = 0
for row in level:
    for column in row:
        if column == "W":
            Wall((x, y))
        if column == "J":
            Jewel((x, y))
        x += 16
    y += 16
    x = 0

#Draw walls and jewels

while exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                exit = False
 
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        playerCar.moveLeft(10)
    if keys[pygame.K_RIGHT]:
        playerCar.moveRight(10)
    if keys[pygame.K_DOWN]:
        playerCar.moveForward(10)
    if keys[pygame.K_UP]:
        playerCar.moveBack(10)
    for wall in walls:
        pygame.draw.rect(screen, (WHITE), wall.rect)

    for jewel in jewels:
        pygame.draw.rect(screen, (BLUE), jewel.rect)
    all_sprites_list.update()
    screen.fill(SURFACE_COLOR)
    all_sprites_list.draw(screen)
    pygame.display.flip()
    clock.tick(60)