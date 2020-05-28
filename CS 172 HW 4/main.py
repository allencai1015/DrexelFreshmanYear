# Allen Cai, ac3978 CS 172 Section 060
import pygame, sys
from Drawable import Drawable
from Ball import Ball
from Block import Block
from Text import Text

if __name__ == "__main__":
    WIDTH = 600
    HEIGHT = 450
    GROUND = 350

    pygame.init()
    surface = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Allen Cai - CS 172 HW 4')
    fpsClock = pygame.time.Clock()

    # COLORS
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)

    # PHYSICS VARIABLES
    dt = 0.1  # DELTA TIME
    g = 6.67  # GRAVITY
    R = 0.7  # REBOUND
    eta = 0.5 # FRICTION

    # OTHER VARIABLES INITIALIZED HERE SO THE WHILE LOOP DOESN'T BUG OUT BEFORE THE MOUSE HAS BEEN CLICKED OR BLOCKS HIT
    x_change = 0
    y_change = 0
    yv = 1
    blocks_hit = 0

    # DRAWABLE OBJECTS: 1 ball, 9 blocks, 2 text objects for score
    ball = Ball((100, 340), True, RED, 10)
    block1 = Block((400, 290), True, 20, 20, BLUE)
    block2 = Block((400, 310), True, 20, 20, BLUE)
    block3 = Block((400, 330), True, 20, 20, BLUE)
    block4 = Block((420, 290), True, 20, 20, BLUE)
    block5 = Block((420, 310), True, 20, 20, BLUE)
    block6 = Block((420, 330), True, 20, 20, BLUE)
    block7 = Block((440, 290), True, 20, 20, BLUE)
    block8 = Block((440, 310), True, 20, 20, BLUE)
    block9 = Block((440, 330), True, 20, 20, BLUE)
    scoretext = Text((50, 50), True, "Score: ", BLACK)
    scorenumber = Text((120, 50), True, str(blocks_hit), BLACK)
    drawables = [ball, block1, block2, block3, block4, block5, block6, block7, block8, block9, scoretext, scorenumber]

    # MAIN GAME LOOP
    while True:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                startloc = pygame.mouse.get_pos()
                x1 = float(startloc[0])
                y1 = float(startloc[1])
            if event.type == pygame.MOUSEBUTTONUP:
                endloc = pygame.mouse.get_pos()
                x2 = float(endloc[0])
                y2 = float(endloc[1])

                xv = x2 - x1
                yv = (y2 - y1) * -1

                x_change = dt * xv
                y_change = dt * yv

                if y1 >= GROUND - 10 :   # IF BALL IS ON OR BELOW THE GROUND
                    yv *= (R * -1)
                    xv *= eta
                else :           # IF BALL IS ABOVE THE GROUND
                    yv -= (g * dt)

        surface.fill((255, 255, 255))  # RESET BACKGROUND TO WHITE
        pygame.draw.line(surface, BLACK, (0, GROUND), (WIDTH, GROUND), 1)  # GROUND LINE

        ''' SCORE DOESN'T UPDATE PROPERLY FOR SOME REASON UNLESS I MANUALLY CHANGE IT HERE,
        USING A SETMESSAGE METHOD CORRECTLY CHANGES THE MESSAGE, BUT PYGAME STILL DRAWS A 0.'''
        num_blocks = str(blocks_hit)
        drawables[-1] = Text((120, 50), True, num_blocks, BLACK)

        for drawable in drawables:   # DRAW EACH DRAWABLE THAT IS VISIBLE
            if drawable.getVisibility() == True:
                drawable.draw(surface, drawable.getLocation())

        # INTERSECTION AND SETTING BLOCK VISIBILITY TO FALSE
        for drawable in drawables:
            for i in range(len(drawables)):
                for j in range(i + 1, len(drawables)):
                    if (isinstance(drawables[j], Block)) and (drawables[j].getVisibility() == True): # BALL INTERSECTS WITH VISIBLE BLOCKS ONLY
                        if (drawable.intersect(drawables[i].get_rect(), drawables[j].get_rect())):
                            drawables[j].setVisibility(False)
                            blocks_hit += 1

        # MOVES BALL, STILL HAS ISSUES WITH BALL OSCILLATING ON THE EDGES
        ball_location = ball.getLocation()
        if abs(yv) >= 0.0001:
            ball.setLocation(ball_location, int(x_change), int(y_change))
            if (ball_location[0] <= 0) or (ball_location[0] >= WIDTH):    # COVERS LEFT TO RIGHT OF SCREEN
                ball.setLocation(ball_location, int(x_change * -1), int(y_change))
                xv = 0
                yv = 0
            if (ball_location[1] <= 0) or (ball_location[1] >= GROUND):   # COVERS TOP TO GROUND
                ball.setLocation(ball_location, int(x_change), int(y_change * -1))
                xv = 0
                yv = 0

        pygame.display.update()
        fpsClock.tick(30)