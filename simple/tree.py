from turtle import *

tracer(1, 0)

# try changing these values and looking at the results
LEFT_ANGLE = 30
RIGHT_ANGLE = 20
LEFT_DECREASE = 7
RIGHT_DECREASE = 11

def tree(x, y, direction, branch_length):
    # if the branch is too small, just quit
    if branch_length < 5:
        return

    # draw the trunk
    pensize(max(branch_length / 8.0, 1))
    forward(branch_length)

    # draw the two branches, which are fractal trees
    left(LEFT_ANGLE)
    tree(xcor(), ycor(), heading(), branch_length - LEFT_DECREASE)
    right(LEFT_ANGLE + RIGHT_ANGLE)
    tree(xcor(), ycor(), heading(), branch_length - RIGHT_DECREASE)
    left(RIGHT_ANGLE)

    # return back to the starting point
    penup()
    goto(x, y)
    setheading(direction)
    pendown()
        
# move the turtle to the starting point at the root
penup()
goto(0, -310)
setheading(90)
pendown()

# draw the first branch
tree(xcor(), ycor(), heading(), 100)
update()
exitonclick()
