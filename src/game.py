import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()

size = (512, 512)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Flow-man")

done = False

clock = pygame.time.Clock()

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(GREEN)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()