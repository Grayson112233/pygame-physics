import pygame
import globals
import numpy
import random
from display import update_display_mode, toggle_fullscreen
from input import isKeyJustPressed, isKeyPressed
from ball import Ball

globals.width = 800
globals.height = 800
globals.fps = 60
globals.friction = 0.005
globals.gravity = 0.1

def main():

    pygame.init()
    update_display_mode()
    clock = pygame.time.Clock()

    entities = []
    for i in range(1000):
        entities.append(Ball(globals.width / 2, globals.height / 2, numpy.random.normal(-10, 10), numpy.random.normal(-10, 10), (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))))

    running = True

    globals.window.fill((255, 255, 255))

    while(running):

        # Set FPS limit
        clock.tick(globals.fps)

        # Fill window white
        globals.window.fill((255, 255, 255))

        globals.events = pygame.event.get()

        for entitiy in entities:
            entitiy.update()

        for entitiy in entities:
            entitiy.draw()

        if isKeyJustPressed(pygame.K_RETURN):
            toggle_fullscreen()

        if isKeyJustPressed(pygame.K_ESCAPE):
            globals.pygame.quit()
            loop = False

        # Flip the buffer
        pygame.display.flip()

main()
