from turtle import *
import random
import time

tracer(1000, 0)

def branch(x, y, direction, branch_length):
    # if the branch is too small, just quit
    if branch_length < 5:
        return

    # draw the "trunk"
    pensize(max(branch_length / 7.0, 1))
    forward(branch_length)

    # draw the two branches, which are fractal trees
    left(LEFT_ANGLE)
    branch(xcor(), ycor(), heading(), branch_length - LEFT_DECREASE)
    right(LEFT_ANGLE + RIGHT_ANGLE)
    branch(xcor(), ycor(), heading(), branch_length - RIGHT_DECREASE)
    left(RIGHT_ANGLE)

    # return back to the starting point
    penup()
    goto(x, y)
    setheading(direction)
    pendown()

def draw_tree(x, y, direction, seed):
    global LEFT_ANGLE, RIGHT_ANGLE, LEFT_DECREASE, RIGHT_DECREASE

    # go to the starting point
    penup()
    goto(x, y)
    setheading(direction)
    pendown()
    
    # try changing these values and looking at the results
    random.seed(seed)
    LEFT_ANGLE     = random.randint(10,  30)
    RIGHT_ANGLE    = random.randint(10,  30)
    LEFT_DECREASE  = random.randint( 6,  15)
    RIGHT_DECREASE = random.randint( 6,  15)
    START_SIZE     = random.randint(80, 120)

    branch(x, y, direction, START_SIZE)
    update()

draw_tree(0, -310, 90, 123)
exitonclick()
