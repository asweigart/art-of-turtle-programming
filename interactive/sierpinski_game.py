# To play Sierpinski's Game, click three times in the window to select the three
# points of the triangle. Then click somewhere inside the triangle to begin.
# The animation speeds up over time.

from turtle import *
import random

setworldcoordinates(0, 0, 960, 810)
bgcolor('#4b4b6e')
pencolor('white')
penup()

click_num = 1

def setup_clicks(x, y):
    global click_num, point_A, point_B, point_C

    if click_num == 1:
        point_A = (x, y)
        goto(point_A)
        #dot(12, 'red') # (!) Try commenting this out to hide the red dot
    elif click_num == 2:
        point_B = (x, y)
        goto(point_B)
        #dot(12, 'green') # (!) Try commenting this out to hide the green dot
    elif click_num == 3:
        point_C = (x, y)
        goto(point_C)
        #dot(12, 'blue') # (!) Try commenting this out to hide the blue dot
    elif click_num == 4:
        goto(x, y)
        start_the_game()
    click_num +=  1
    
def start_the_game():
    global point_A, point_B, point_C    

    # start in the middle of the triangle
    left = min(point_A[0], point_B[0], point_C[0])
    right = max(point_A[0], point_B[0], point_C[0])
    bottom = min(point_A[1], point_B[1], point_C[1])
    top = max(point_A[1], point_B[1], point_C[1])
    goto(left + int((right - left) / 2), bottom + int((top - bottom) / 2))
    
    for i in range(25000):
        roll = random.randint(1, 3)
        if roll == 1:
            dest = point_A
        elif roll == 2:
            dest = point_B
        elif roll == 3:
            dest = point_C

        midx = int(abs(dest[0] - xcor()) / 2) + min(dest[0], xcor())
        midy = int(abs(dest[1] - ycor()) / 2) + min(dest[1], ycor())
        goto(midx, midy)
        dot(2)

        if i == 20:
            tracer(4, 0)
        elif i == 2000:
            tracer(100, 0)
        elif i == 4000:
            tracer(10000, 0)


onscreenclick(setup_clicks)
done()
