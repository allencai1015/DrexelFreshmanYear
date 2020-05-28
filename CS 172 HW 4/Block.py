# Allen Cai, ac3978 CS 172 Section 061
import pygame
from Drawable import Drawable

class Block(Drawable):
    def __init__(self, position = (0, 0), visible = True, width = 1, length = 1, color = (0, 0, 0)):
        super().__init__(position, visible)
        self.__width = width
        self.__length = length
        self.__color = color

    def draw(self, surface, position):
        x = position[0]
        y = position[1]
        pygame.draw.rect(surface, self.__color, (int(x), int(y), self.getWidth(), self.getLength()), 5)

    def get_rect(self):
        loc = self.getLocation()
        return pygame.Rect(loc[0], loc[1], 20, 20)

    def getLocation(self):
        return super().getLocation()

    def getWidth(self):
        return self.__width

    def getLength(self):
        return self.__length