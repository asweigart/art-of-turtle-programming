from turtle import *
import random
tracer(100, 0)

GAP = 10
THICKNESS = 20

def draw_head(length):
    begin_fill()
    final_position = position()
    left(90)
    forward(length - THICKNESS)
    left(90)
    forward(THICKNESS * 3)
    left(90)
    forward(THICKNESS / 2.0)
    right(90) # draw tongue
    forward(THICKNESS)
    right(45)
    forward(THICKNESS / 3.0)
    backward(THICKNESS / 3.0)
    left(90)
    forward(THICKNESS / 3.0)
    backward(THICKNESS / 3.0)
    right(45)
    backward(THICKNESS)
    left(90) # end tongue
    forward(THICKNESS / 2.0)
    left(90)
    forward(THICKNESS * 2)
    right(90)
    forward(length - THICKNESS)
    left(90)
    forward(THICKNESS)
    penup()
    goto(final_position)
    left(90)
    forward(length - THICKNESS * 1.3)
    left(90)
    forward(THICKNESS * 1.5)
    dot(8, 'black')
    backward(THICKNESS * 1.5)
    right(90)
    backward(length - THICKNESS * 1.3)
    right(90)
    pendown()
    end_fill()

def twist_up(length):
    begin_fill()
    forward(GAP)
    left(90)
    forward(length - THICKNESS)
    right(90)
    forward(THICKNESS)
    final_position = position()
    right(90)
    penup()
    forward(THICKNESS)
    pendown()
    forward(length - THICKNESS)
    right(90)
    forward(THICKNESS + GAP)
    end_fill()
    penup()
    goto(final_position)
    pendown()
    right(180)
    
    
def twist_down(length):
    begin_fill()
    forward(GAP + THICKNESS)
    right(90)
    forward(length - THICKNESS)
    final_position = position()
    penup()
    forward(THICKNESS)
    pendown()
    right(90)
    forward(THICKNESS)
    right(90)
    forward(length - THICKNESS)
    left(90)
    forward(GAP)
    end_fill()
    penup()
    goto(final_position)
    pendown()
    right(180)
    

def draw_tail(length):
    begin_fill()
    forward(GAP)
    left(90)
    forward(length - THICKNESS)
    right(90)
    forward(THICKNESS / 2.0)
    right(90)
    forward(length)
    right(90)
    forward(THICKNESS / 2.0 + GAP)
    right(180)
    end_fill()

def draw_snake(lengths):
    draw_head(lengths[0])
    for i in range(1, len(lengths) - 1, 2):
        twist_up(lengths[i])
        twist_down(lengths[i + 1])
    draw_tail(lengths[-1])

pensize(4)
for i in range(50):
    penup()
    goto(random.randint(-400, 400), random.randint(-400, 400))
    pendown()
    setheading(random.randint(0, 360))
    #pencolor(random.randint(0, 100) / 100.0, random.randint(0, 100) / 100.0, random.randint(0, 100) / 100.0)
    #pencolor(random.choice(['#BFAC2C', '#7F731D', '#FFE53A', '#40390F', '#E5CE34']))
    pencolor(random.choice(['#71BF2E', '#4C7F1E', '#97FF3D', '#26400F', '#88E537']))
    fillcolor(pencolor())
    lengths = []
    for j in range(random.randint(3, 6) * 2):
             lengths.append(random.randint(40, 150))
    draw_snake(lengths)
    print(i)
    
