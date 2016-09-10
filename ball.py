import globals
import pygame


class Ball():

    def __init__(self, x, y, vx=0, vy=0):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.width = 10
        self.height = 10
        self.color = (0, 0, 0)

    # Bounce off of walls with inelastic collisions
    def collide_walls(self):
        if self.x < 0:
            self.x = 0
            self.vx = -self.vx
        if self.x > globals.width - self.width:
            self.x = globals.width - self.width
            self.vx = -self.vx
        if self.y < 0:
            self.y = 0
            self.vy = -self.vy
        if self.y > globals.height - self.height:
            self.y = globals.height - self.height
            self.vy = -self.vy

    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.collide_walls()

    def draw(self):
        rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(globals.window, self.color, rect)
