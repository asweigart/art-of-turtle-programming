# Koch Snowflake Drawer, by Al Sweigart al@inventwithpython.com
# Click in the window to draw koch snowflakes with turtle graphics.

import turtle
import random
import math

PURPLISH_BLUE = '#1C2340'
turtle.bgcolor(PURPLISH_BLUE)
turtle.pencolor('white')
turtle.tracer(10, 0) # Make the turtle draw faster.

def snowflakeSide(length_side, levels):
    # Draw a "koch curve" for one of the six sides of the snowflake.
    if levels == 0:
        turtle.forward(length_side)
        return
    length_side = length_side / 3.0
    snowflakeSide(length_side, levels-1)
    turtle.left(60)
    snowflakeSide(length_side, levels-1)
    turtle.right(120)
    snowflakeSide(length_side, levels-1)
    turtle.left(60)
    snowflakeSide(length_side, levels-1)

def drawSnowflake(length_side, levels):
    # Draw a snowflake by drawing six "koch curves".
    for i in range(6):
        snowflakeSide(length_side, levels)
        turtle.right(60)

def drawMultiSnowflake(x, y):
    # The turtle module passes the XY coordinates of where the mouse
    # clicked in the window when it calls this function.

    # The snowflakes are drawn at a random angle.
    turtle.setheading(random.randint(0, 360))
    for length in range(1, 5): # Draw snowflakes of varying lengths.
        if random.randint(0, 2) == 0:
            # In 1 in 3 times, we skip the snowflake of this length.
            continue

        # Set a random line thickness (pensize) and length of each
        # side of the snowflake:
        turtle.pensize(random.randint(1, 4))
        length = length * random.randint(20, 40)

        # Move the turtle to the starting position:
        turtle.penup()
        turtle.goto(x, y)
        turtle.backward(length / 2.0)
        turtle.right(90)
        turtle.backward(length * math.sqrt(3) / 2.0)
        turtle.left(90)
        turtle.pendown()

        # Draw a snowflake.
        drawSnowflake(length, random.randint(2, 4))
    turtle.update() # Finish drawing the screen.

# Call drawMultiSnowflake() when screen is clicked:
turtle.onscreenclick(drawMultiSnowflake)
turtle.mainloop() # Start the program, and run until the window is closed.
