from turtle import *
from math import pi, cos, sin

def dot_pos(x,m) :
    return((sin(x*(2*pi/m))*300,cos(x*(2*pi/m))*300))

def dot_modulo(m):
    for x in range(m):
        x += 1
        penup()
        goto(dot_pos(x,m))
        pendown()
        dot(4)

def draw(t,m):
    print(f"Table de {t} modulo {m}")
    hideturtle()
    speed(0)
    penup()
    goto(0,-300)
    pendown()
    circle(300)
    dot_modulo(m)
    for x in range(m):
        x += 1
        penup()
        goto(dot_pos(x,m))
        pendown()
        goto(dot_pos(x*t,m))
    exitonclick()
        
draw(7,100)
