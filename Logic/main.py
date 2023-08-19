import pygame, sys
from settings import *
from level import Level
# Pygame setup
pygame.init()
screen_width= 1200
screen_height= 700
screen= pygame.display.set_mode((screen_width, screen_height))
clock= pygame.time.Clock()
level= Level(level_map, screen)

while True:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # fill the screen with a color to wipe away anything from last frame
    screen.fill('black')
    level.run()
    pygame.display.update()
    clock.tick(60) # limits FPS to 60