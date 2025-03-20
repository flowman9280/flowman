# Importing librarys
import random, time, config, pygame
from map import map
from spritesheet import spritesheet
from ennemies import Enemy
config.init()
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

gameoverScreen = spritesheet("nouveauflow-man\\bouton-menu.png").image_at((0,0,1280,736))

# Initial stats
pface = 0
newPos = 0
face = 1
animationIndexX = 0
animationIndexY = 0
score = 0

# Flowman functions
def move_up():
    newPos = (config.posY - 1)
    if map[config.posY - 1][config.posX] != 3:
        config.posY = newPos



def move_down():
    global face
    global pface
    newPos = (config.posY + 1)
    if map[config.posY + 1][config.posX] != 3:
        config.posY = newPos
    


def move_left():
    newPos = (config.posX - 1)
    if map[config.posY][config.posX - 1] != 3:
        config.posX = newPos



def move_right():
    newPos = (config.posX + 1)
    if map[config.posY][config.posX + 1] != 3:
        config.posX = newPos



def rage():
    config.rag = True


def rot_center(image, rect, angle):
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = rot_image.get_rect(center=rect.center)
    return rot_image,rot_rect

def gameover():
    print("detected")
    pygame.QUIT()


def win():
    pass

ennemys = []
ennemyNb = 4
for i in range(ennemyNb):
    ennemys.append(Enemy(18,11))

# CELLS : 1-PACGUM 0-PELLET 3-MUR
running = True
p = 0
temps = 0
cycle = 0
while running:
    cycle += 1
    score += 69
    print(score)
    if cycle%30 == 0:
        ennemys.append(Enemy(18,11))
    time.sleep(GAMECLOCK)
    screen.fill(BACKGROUND_COLOR)

    char_images = flowman.image_at((animationIndexX*32, animationIndexY*32, 32, 32))

    for i in ennemys:
        i.step(config.posX, config.posY, config.rag)

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
                if map[config.posY][config.posX - 1] != 3:
                    face = 1

            if event.key == pygame.K_RIGHT:
                pface = face
                if map[config.posY][config.posX + 1]  != 3:
                    face = 3

            if event.key == pygame.K_UP:
                pface = face
                if map[config.posY - 1][config.posX] != 3:
                    face = 4

            if event.key == pygame.K_DOWN:
                pface = face
                if map[config.posY + 1][config.posX] != 3:
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
            if (x == config.posX) and (y == config.posY):
                screen.blit(char_images, (x*32, y*32))
            for i in ennemys:
                if (x == i.eposX) and (y == i.eposY):
                    screen.blit(eye, (x*32, y*32))

                if config.posX == config.eposX and config.posY == config.eposY and not config.rag:
                    gameover()

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

    if config.posX == 5 and config.posY == -1:
        config.posX = 5
        config.posY = 22

    if config.posX == 5 and config.posY == 23:
        config.posX = 5
        config.posY = 0

    if config.posX == 34 and config.posY==-1:
        config.posX = 34
        config.posY = 22

    if config.posX == 34 and config.posY == 23:
        config.posX = 34
        config.posY = 0

    if map[config.posY][config.posX] == 0:
        map[config.posY][config.posX] = 8
        p += 1
    if p == 452:
        win()

    if map[config.posY][config.posX] == 2:
        map[config.posY][config.posX] = 8
        rage()
    if config.rag == 1:
        temps= temps + 1
    if temps == 60:
        config.rag = 0
    
    pygame.display.flip()
    clock.tick(60)
    print(config.eposX)
pygame.quit()