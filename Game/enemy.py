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
        playerxpos = player.x + (player.w/2)
        playerypos = player.y + (player.h/2)
        
        playerVector = complex(playerxpos, playerypos)
        selfVector = complex(self.x, self.y)

        return abs(playerVector - selfVector) < self.size + player.w / 2


    def movement(self, screen_size: tuple, dt: float, player: Player):
        """Draws the player on the screen.
        
        Keyword arguments:
        screen_size -- the size of the display window
        dt -- a multiplier for movement amount based on fps (60 / fps)
        """

        if self.collidesWith(player):
            self.color = (0, 255, 0)
            self.run = False
        else:
            self.color = (255, 0, 0)

        if self.y != player.y:

            self.y += int(self.speed * ((player.y-self.y)/(abs(player.y-self.y))) * dt)
        if self.x != player.x:

            self.x += int(self.speed * ((player.x-self.x)/(abs(player.x-self.x))) * dt)



        # await asyncio.sleep(self.delay)

        if self.y != player.y:
            self.y += int(self.speed * ((player.y - self.y) / (abs(player.y - self.y))) * dt)
        if self.x != player.x:
            self.x += int(self.speed * ((player.x - self.x) / (abs(player.x - self.x))) * dt)