from turtle import *
import math
tracer(1000, 0)
setworldcoordinates(0, 0, 960, 810)
bgcolor(0.9, 0.9, 0.9)

BASE_SIZE = 13
BASE_HEIGHT = BASE_SIZE * math.sin(60 * (math.pi / 180))
START_X = 50
START_Y = 20

def draw_triangle(x, y, color):
    penup()
    pencolor(color)
    goto(x, y) # go to bottom-left corner
    pendown()
    setheading(60)
    forward(BASE_SIZE) # draw first side
    right(120)
    forward(BASE_SIZE) # draw second side
    right(120)
    forward(BASE_SIZE) # draw third side

def draw_sierpinski(x, y, level, color):
    if level == 0:
        draw_triangle(x, y, color)
        draw_triangle(x + (BASE_SIZE * 0.5), y + BASE_HEIGHT, color)
        draw_triangle(x + BASE_SIZE, y, color)
    else:
        draw_sierpinski(x, y, level - 1, color)
        draw_sierpinski(x + (BASE_SIZE * 0.5 * (2 ** level)), y + (BASE_HEIGHT * (2 ** level)), level - 1, color)
        draw_sierpinski(x + (BASE_SIZE * (2 ** level)), y, level - 1, color)

# loop from 5 to 0, drawing 5 sets of sierpinski triangles each with a different color
for i in range(5, -1, -1):
    red = 1 - (0.2 * i)
    green = 0.1 * i
    blue = 0.1 * i
    draw_sierpinski(START_X, START_Y, i, (red, green, blue))

hideturtle()
update()
exitonclick()
