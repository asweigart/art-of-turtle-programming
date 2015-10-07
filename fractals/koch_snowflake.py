from turtle import *
tracer(1, 0)

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


LENGTH = 300.0
penup()
backward(LENGTH / 2.0)
right(90)
backward(1.75 * LENGTH / 2.0)
left(90)
pendown()

for lev in range(5):
    draw_snowflake(LENGTH, lev)
exitonclick()
