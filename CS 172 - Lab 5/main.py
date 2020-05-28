import pygame, sys, random
from Drawable import Drawable

# COLORS
blue = (0, 0, 255)
green = (0, 255, 0)
white = (255, 255, 255)

class Rectangle(Drawable):
    def __init__(self, x= 0, y=0, width = 1, height = 1, color = (0, 0, 0)):
        super().__init__(x, y)
        self.__x = x
        self.__y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.__x, self.__y, self.width, self.height), 0)

class Snowflake(Drawable):
    def __init__(self, x= 0, y= 0):
        super().__init__(x, y)
        self.__x = x
        self.__y = y
        self.line1s = (self.__x - 5, self.__y) # s = start
        self.line1e = (self.__x + 5, self.__y) # e = end
        
        self.line2s = (self.__x, self.__y - 5)
        self.line2e = (self.__x, self.__y + 5)
        
        self.line3s = (self.__x - 5, self.__y - 5)
        self.line3e = (self.__x + 5, self.__y + 5)
        
        self.line4s = (self.__x - 5, self.__y + 5)
        self.line4e = (self.__x + 5, self.__y - 5)
        
    def draw(self, surface):
        pygame.draw.line(surface, white, self.line1s, self.line1e, 1)
        pygame.draw.line(surface, white, self.line2s, self.line2e, 1)
        pygame.draw.line(surface, white, self.line3s, self.line3e, 1)
        pygame.draw.line(surface, white, self.line4s, self.line4e, 1)
        
    def move_down(self):
        self.__y += 5

if __name__ == "__main__":
    x = Rectangle(0, 0, 1, 1, blue)
    print(x)
    pygame.init()
    surface = pygame.display.set_mode((600, 450))
    pygame.display.set_caption('Allen Cai - CS 172 Lab 5')
    fpsClock = pygame.time.Clock()
    
    sky = Rectangle(0, 0, 600, 300, blue)
    ground = Rectangle(0, 300, 600, 450, green)
    snow = Snowflake(300, 0)
    drawables = [sky, ground, snow]
       
    still = True
    
    while True:  # main game loop
        for event in pygame.event.get():
            if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.__dict__['key'] == pygame.K_q) :
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:      # toggle on
                if event.__dict__['key'] == pygame.K_SPACE:
                    still = not still     
        if not still : 
            surface.fill((0, 0, 0))
            for drawable in drawables:
                drawable.draw(surface)
            pygame.display.update()
            for drawable in drawables:
                if isinstance(drawable, Snowflake):
                    location = drawable.getLoc()
                    maxY = random.randint(300,350)
                    if location[1] >= maxY:     # Extra Credit: Stops it from moving below maxY
                        drawable.__init__(location[0], location[1])
                    else :
                        y = location[1] + 5
                        drawable.__init__(location[0], y)
                        drawable.move_down()

            temp = random.randint(0, 600)
            newSnowflake = Snowflake(temp)
            drawables.append(newSnowflake)
            
        pygame.display.update()
        fpsClock.tick(30)