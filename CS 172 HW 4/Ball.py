# Allen Cai, ac3978 CS 172 Section 061
import pygame
from Drawable import Drawable

class Ball(Drawable):
    def __init__(self, position = (0, 0), visible = True, color = (0, 0, 0), radius = 1):
        super().__init__(position, visible)
        self.__color = color
        self.__radius = radius

    def draw(self, surface, position):
        pygame.draw.circle(surface, self.__color, position, self.__radius)

    def get_rect(self):
        loc = self.getLocation()
        return pygame.Rect(loc[0], loc[1], 5, 5)

    def setLocation(self, position, x_change, y_change):  #
        x = position[0]
        y = position[1]
        x += x_change
        y -= y_change
        self._Drawable__position = (x,y)