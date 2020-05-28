# Allen Cai, ac3978 CS 172 Section 061
import abc

class Drawable(metaclass = abc.ABCMeta):
    def __init__(self, position = (0, 0), visible = True):
        self.__position = position
        self.__visible = visible

    @abc.abstractmethod
    def draw(self):
        pass

    @abc.abstractmethod
    def get_rect(self):
        pass

    def getLocation(self):
        return self.__position

    def getVisibility(self):
        return self.__visible

    def setVisibility(self, visibility = False):
        self.__visible = visibility

    def intersect(self, rect1, rect2):
        if (rect1.x < rect2.x + rect2.width) and (rect1.x + rect1.width > rect2.x) and (rect1.y < rect2.y + rect2.height) and (rect1.height + rect1.y > rect2.y):
            return True
        return False