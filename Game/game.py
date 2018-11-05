import pygame
from pygame.locals import *

pygame.init()

window = pygame.display.set_mode((500, 500))

clock = pygame.time.Clock()

class Player:

    def __init__(self, y, s, width, height,grav):
        self.y = y
        self.s = s
        self.g = grav
        self.w = width
        self.h = height

        self.y_vel = 0

    def graphics(self):
        pygame.draw.rect(window,(255,255,255),(150,self.y,self.w,self.h))

    def movement(self):
        dt = clock.tick(60) / 1000

        self.y_vel += self.g

        key = pygame.key.get_pressed()

        if key[K_SPACE]:
            self.y_vel -= 1

        self.y += self.y_vel




running = True

player = Player(250,3,50,100,0.5)

down = False

while running:

    window.fill(pygame.color.Color("BLACK"))

    for event in pygame.event.get():

        if event.type == QUIT:
            running = False

    player.movement()

    player.graphics()



    pygame.display.update()



