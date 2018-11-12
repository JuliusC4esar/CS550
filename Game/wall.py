import pygame
from pygame.locals import *

class Wall:
    def __init__(self, x: float, y: float, w: float, h: float, one_way: bool, rgb=None):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

        self.one_way = one_way  # Can you jump and fall through the platform or not

        self.rgb = ((255, 255, 255) if one_way else (0, 0, 255)) if rgb is None else rgb  # Platform coloring
    
    def graphics(self, screen_size: tuple, window: pygame.Surface):
        pygame.draw.rect(window, self.rgb, (self.x, self.y, self.w, self.h))   # Platform graphics