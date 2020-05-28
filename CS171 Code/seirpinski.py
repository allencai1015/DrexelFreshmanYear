import turtle
import math
def equalTri(x,y,length) :
    turtle.penup()
    turtle.setpos(x,y)
    turtle.pendown()
    i = 0
    side = 360/3
    while i < 3 :
        turtle.forward(length)
        turtle.left(side)
        i += 1

def seirpinski(x,y,s) :
    z = 0
    if s > 10:   
        equalTri(x,y,s)
        seirpinski(x,y,s/2)
        seirpinski(x+(s/2),y,s/2)
        seirpinski(x+(s/4),y+(s * math.sqrt(3) / 4),s/2)
        
seirpinski(0,0,200)
        