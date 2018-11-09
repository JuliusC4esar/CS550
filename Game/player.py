import pygame
from pygame.locals import *

from typing import List

from wall import Wall


class Player:
    GRAVITY = 0.5  # Amount subtracted from velocity each time

    y_vel: float
    jumps: int
    jumped_already: bool

    def __init__(self, x: float, y: float, w: float, h: float, j: float, rgb=(255, 255, 255)):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

        self.jump_strength = j
        self.jump_num = 3

        self.x_speed = 3

        self.x_vel = 0
        self.y_vel = 0

        self.jumps = 0
        self.jumped_already = False

        self.rgb = rgb

    def graphics(self, screen_size: tuple, window: pygame.Surface):
        """Draws the player on the screen.

        Keyword arguments:
        screen_size -- the size of the display window
        window -- the window to draw to
        """

        pygame.draw.rect(window, self.rgb, (self.x, self.y, self.w, self.h))

    def movement(self, screen_size: tuple, dt: float, walls: List[Wall]):
        """Draws the player on the screen.

        Keyword arguments:
        screen_size -- the size of the display window
        dt -- a multiplier for movement amount based on fps (60 / fps)
        """

        dt = round(dt)

        if dt > 1:
            self.movement(screen_size, dt - 1, walls)

        width, height = screen_size
        key = pygame.key.get_pressed()  # Get the keys pressed

        # Add the velocities
        self.x += self.x_vel
        self.y += self.y_vel

        self.x = max(0, self.x)
        self.x = min(width - self.w, self.x)

        self.x_vel = self.x_speed * (int(key[K_RIGHT]) - int(key[K_LEFT]))

        if self.y >= height - self.h:  # If at the bottom (or below):
            self.y = height - self.h  # Set the player to the exact bottom
            self.y_vel = 0  # Set velocity
            self.jumps = 0

        if key[K_SPACE]:
            if (self.y >= height - self.h or self.jumps < self.jump_num) and not(self.jumped_already):  # Check if player wants to jump
                self.y_vel = -self.jump_strength  # Jump
                self.jumped_already = True
                self.jumps += 1
        else:
            self.jumped_already = False

        self.y_vel += Player.GRAVITY  # Factor in gravity

        [self.collision(w, key) for w in walls]

    def collision(self, wall: Wall, key: tuple):
        if self.y_vel >= 0 and not(wall.one_way and key[K_DOWN]):
            p_y_vel = self.y_vel

            if wall.y >= self.y + self.h and self.x < wall.x + wall.w and self.x + self.w > wall.x:
                self.y_vel = min(self.y_vel, wall.y - (self.y + self.h))

            if self.y_vel == 0 and self.y_vel != p_y_vel:
                self.jumps = 0

        if not(wall.one_way):
            if self.y_vel <= 0:
                if wall.y + wall.h <= self.y and self.x < wall.x + wall.w and self.x + self.w > wall.x:
                    self.y_vel = max(self.y_vel, (wall.y + wall.h) - self.y)

            if self.y < wall.y + wall.h and self.y + self.h > wall.y:
                if self.x_vel >= 0 and self.x + self.w <= wall.x:
                    if self.x_vel >= wall.x - (self.x + self.w):
                        self.x = wall.x - self.w
                        self.x_vel = 0

                if self.x_vel <= 0 and self.x >= wall.x + wall.w:
                    if self.x_vel <= (wall.x + wall.w) - self.x:
                        self.x = wall.x + wall.w
                        self.x_vel = 0
