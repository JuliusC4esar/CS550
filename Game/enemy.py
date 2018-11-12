import pygame
from pygame.locals import *

from player import Player


class Enemy:

    def __init__(self,xpos,ypos,speed,size):
        self.x = xpos
        self.y = ypos
        self.speed = speed
        self.size = size
        self.delay = 1
        self.color = (255, 0, 0)
        self.run = True

    def graphics(self, screen_size: tuple, window: pygame.Surface):
        """Draws the enemy on the screen.

        Keyword arguments:
        screen_size -- the size of the display window
        window -- the window to draw to
        """

        pygame.draw.circle(window, self.color, (self.x, self.y), self.size)

    def collidesWith(self, player: Player):
        player_x = player.x + (player.w/2)
        player_y = player.y + (player.h/2)

        player_vector = complex(player_x, player_y)
        self_vector = complex(self.x, self.y)

        return abs(player_vector - self_vector) < self.size + player.w / 2


    def movement(self, screen_size: tuple, dt: float, player: Player):
        """Draws the player on the screen.
        
        Keyword arguments:
        screen_size -- the size of the display window
        dt -- a multiplier for movement amount based on fps (60 / fps)
        """

        # Collision detection
        if self.collidesWith(player):
            self.color = (0, 255, 0)
            self.run = False
        else:
            self.color = (255, 0, 0)

        # Enemy AI movement
        if self.y != player.y:
            self.y += int(self.speed * ((player.y-self.y)/(abs(player.y-self.y))) * dt)
        if self.x != player.x:
            self.x += int(self.speed * ((player.x-self.x)/(abs(player.x-self.x))) * dt)



        # await asyncio.sleep(self.delay)

        if self.y != player.y:
            self.y += int(self.speed * ((player.y - self.y) / (abs(player.y - self.y))) * dt)
        if self.x != player.x:
            self.x += int(self.speed * ((player.x - self.x) / (abs(player.x - self.x))) * dt)