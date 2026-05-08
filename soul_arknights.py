import pygame
from scripts.tools.timer import timer
pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
running = True


@timer
def process_logical():
    return
@timer
def process_render():
    screen.fill((86,144,220))
    return


while running:
    #get user input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #logical
    process_logical()
    #render
    process_render()
    #display
    pygame.display.flip()
    clock.tick(60)

