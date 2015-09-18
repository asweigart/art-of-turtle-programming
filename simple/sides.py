from turtle import *

#tracer(1, 0) # (!) Try uncommenting this line.

penup()
goto(-100, -300)
pendown()

#setheading(30) (!) Try uncommenting this line, and changing 30 to another number.

pensize(3) # (!) Try changing this line to other sizes.
pencolor('green') # (!) Try changing this line to other colors.

for sides in range(3, 21):
    begin_fill()
    for i in range(sides):
        forward(100)
        left(360 / sides)

        #if i == int(sides / 2.0): # (!) Try uncommenting these two lines.
        #    write(str(sides))
