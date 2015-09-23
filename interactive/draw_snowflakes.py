from turtle import *
import random
import math

bgcolor('#1C2340')
pencolor('white')
tracer(10, 0)

def snowflake_side(length_side, levels):
    if levels == 0:
        forward(length_side)
        return
    length_side = length_side / 3.0
    snowflake_side(length_side, levels-1)
    left(60)
    snowflake_side(length_side, levels-1)
    right(120)
    snowflake_side(length_side, levels-1)
    left(60)
    snowflake_side(length_side, levels-1)

def draw_snowflake(length_side, levels):
    for i in range(6):
        snowflake_side(length_side, levels)
        right(60)

def draw_multi_snowflake(x, y):
    setheading(random.randint(0, 360))
    for length in range(1, 5):
        if random.randint(0, 2) == 0:
            continue
        pensize(random.randint(1, 4))
        length = length * random.randint(20, 40)
        penup()
        goto(x, y)
        backward(length / 2.0)
        right(90)
        backward(length * math.sqrt(3) / 2.0)
        left(90)
        pendown()
        draw_snowflake(length, random.randint(2, 4))
    update()
    
onscreenclick(draw_multi_snowflake)
done()
