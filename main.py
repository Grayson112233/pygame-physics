import pygame
import globals
from display import update_display_mode, toggle_fullscreen
from input import isKeyJustPressed, isKeyPressed
from ball import Ball

globals.width = 640
globals.height = 480
globals.fps = 60


def main():

    pygame.init()
    update_display_mode()
    clock = pygame.time.Clock()

    entities = []
    entities.append(Ball(globals.width / 2, globals.height / 2, 5, 5))

    running = True

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
