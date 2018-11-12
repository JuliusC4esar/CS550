import pygame
from pygame.locals import *

from typing import List

from wall import Wall


class Player:
    y_vel: float
    jumps: int
    jumped_already: bool

    def __init__(self, x: float, y: float, w: float, h: float, color=(255, 255, 255)):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

        self.gravity = 0.5  # Amount subtracted from velocity each time

        self.jump_strength = 8  # Amount added to velocity when space is pressed
        self.jump_num = 3  # The number of jumps allowed before touching the ground (or a platform)

        self.x_speed = 3  # The x velocity when left or right is pressed

        self.x_vel = 0  # The current x velocity
        self.y_vel = 0  # The current y velocity

        self.jumps = 0  # The current number of jumps since the ground was touched

        # Jumped already on the current press of the space key (to prevent multiple jumps in one press)
        self.jumped_already = False

        self.color = color  # The color of the player

    def graphics(self, screen_size: tuple, window: pygame.Surface):
        """Draws the player on the screen (a rectangle at (x, y) with dimensions (w, h))

        Keyword arguments:
        screen_size -- the size of the display window
        window -- the window to draw to
        """

        pygame.draw.rect(window, self.color, (self.x, self.y, self.w, self.h))

    def movement(self, screen_size: tuple, dt: float, walls: List[Wall]):
        """Calculates the movement of the player.

        Keyword arguments:
        screen_size -- the size of the display window
        dt -- a multiplier for movement amount based on fps (60 / fps)
        walls -- a list of the walls in the display window
        """

        dt = round(dt)  # Make dt an int

        # Call movement dt times per frame (to help with consistency across platforms)
        if dt > 1:
            self.movement(screen_size, dt - 1, walls)

        width, height = screen_size  # Split screen size into w and h
        key = pygame.key.get_pressed()  # Get the keys pressed

        # Add the velocities to the positions
        self.x += self.x_vel
        self.y += self.y_vel

        # Make sure the x is in range
        self.x = max(0, self.x)
        self.x = min(width - self.w, self.x)

        # Set the x velocity based on the keys pressed
        self.x_vel = self.x_speed * (int(key[K_RIGHT]) - int(key[K_LEFT]))

        if self.y >= height - self.h:  # If at the bottom (or below):
            self.y = height - self.h  # Set the player to the exact bottom
            self.y_vel = 0  # Set velocity
            self.jumps = 0

        if key[K_SPACE]:  # If space is pressed
            if (self.y >= height - self.h or self.jumps < self.jump_num) and not(self.jumped_already):  # Check if player wants to jump
                self.y_vel = -self.jump_strength  # Jump
                self.jumped_already = True  # Already jumped on this press of space
                self.jumps += 1  # Add jump
        else:
            self.jumped_already = False  # Haven't jumped already (because key is released)

        self.y_vel += self.gravity  # Factor in gravity

        [self.collision(w, key) for w in walls]  # Call collision for each wall

    def collision(self, wall: Wall, key: tuple):
        """Calculates the changes in x, y, x_vel, and y_vel because of a certain wall.

        Keyword arguments:
        wall -- the wall that changes coordinates and velocity
        key -- an array of keys that are pressed
        """

        # Checks if player is going to land on the top of the wall and updates the coordinates and
        # velocities so that the player doesn't fall through the wall
        if not(wall.one_way and key[K_DOWN]):  # Allows the player to fall through one-way walls
            if self.y_vel >= 0:  # If the player is falling down
                p_y_vel = self.y_vel  # Previous y velocity

                # If the player is above the wall
                if wall.y >= self.y + self.h and self.x < wall.x + wall.w and self.x + self.w > wall.x:
                    if self.y_vel > wall.y - (self.y + self.h):  # If the player is going to fall through the wall
                        self.y = wall.y - self.h  # Set the player's y to the top of the wall
                        self.y_vel = 0  # Set the player's y velocity to 0 (landed on the wall)

                if self.y_vel == 0 and self.y_vel != p_y_vel:  # If the velocity changed and is 0 (landed on the wall)
                    self.jumps = 0  # Reset jumps

        if not(wall.one_way):  # If the wall isn't one-way (need to check sides and bottom)
            if self.y_vel <= 0:  # If the player is going up
                # If the player is below the wall
                if wall.y + wall.h <= self.y and self.x < wall.x + wall.w and self.x + self.w > wall.x:
                    if self.y_vel < (wall.y + wall.h) - self.y:  # If the player is going to hit the wall
                        self.y = wall.y + wall.h  # Set the player's y to the bottom of the wall
                        self.y_vel = 0  # Set the player's y velocity to 0 (hit the wall)

            # If the player's and the wall's y positions overlap (need to check sides)
            if self.y < wall.y + wall.h and self.y + self.h > wall.y:
                if self.x_vel >= 0 and self.x + self.w <= wall.x:  # If the player is to the left of the wall
                    if self.x_vel >= wall.x - (self.x + self.w):  # If the player is going to hit the left edge
                        self.x = wall.x - self.w  # Set the player's x to the left of the wall
                        self.x_vel = 0  # Set the player's x velocity to 0 (hit side of the the wall)

                if self.x_vel <= 0 and self.x >= wall.x + wall.w:  # If the player is to the right of the wall
                    if self.x_vel <= (wall.x + wall.w) - self.x:  # If the player is going to hit the right edge
                        self.x = wall.x + wall.w  # Set the player's x to the right of the wall
                        self.x_vel = 0  # Set the player's x velocity to 0 (hit side of the the wall)
