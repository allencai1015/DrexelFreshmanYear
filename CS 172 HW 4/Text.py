# Allen Cai, ac3978 CS 172 Section 061
import pygame
from Drawable import Drawable

class Text(Drawable):
    def __init__(self, position = (0, 0), visible = True, message = "Score: ", color = (0, 0, 0)):
        super().__init__(position, visible)
        self.__message = message
        self.__color = color
        fontObj = pygame.font.Font("freesansbold.ttf", 20)
        self.__surface = fontObj.render(message, True, self.__color)

    def draw(self, surface, position):
        surface.blit(self.__surface, position)

    def get_rect(self):
        loc = self.getLocation()
        return pygame.Rect(loc[0], loc[1], 20, 20)

    def getLocation(self):
        return super().getLocation()

    def getMessage(self):
        return self.__message

    def setMessage(self, new_message):
        self.__message =  new_message