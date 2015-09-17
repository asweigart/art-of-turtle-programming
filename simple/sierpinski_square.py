from turtle import *

tracer(100, 0)

FG_COLOR = ('#FFD78E')
BG_COLOR = ('#517DB2')

bgcolor(BG_COLOR)
pencolor(FG_COLOR)

def draw_rectangle(left, top, width, height):
    if width < 5 or height < 5:
        return
    
    # draw outer rectangle
    penup()
    goto(left, top)
    pendown()
    fillcolor(FG_COLOR)
    
    begin_fill()
    setheading(0)
    forward(width)
    right(90)
    forward(height)
    right(90)
    forward(width)
    right(90)
    forward(height)
    end_fill()

    www = width / 3.0
    hhh = height / 3.0

    # draw inner rectangle
    penup()
    goto(left + www, top - hhh)
    pendown()
    fillcolor(BG_COLOR)

    begin_fill()
    setheading(0)
    forward(www)
    right(90)
    forward(hhh)
    right(90)
    forward(www)
    right(90)
    forward(hhh)
    end_fill()

    # recursive calls
    draw_rectangle(left, top, www, hhh)                         # top-left
    draw_rectangle(left + www, top, www, hhh)                   # top
    draw_rectangle(left + (www * 2), top, www, hhh)             # top-right
    draw_rectangle(left, top - hhh, www, hhh)                   # left
    draw_rectangle(left + (www * 2), top - hhh, www, hhh)       # right
    draw_rectangle(left, top - (hhh * 2), www, hhh)             # bottom-left
    draw_rectangle(left + www, top - (hhh * 2), www, hhh)       # bottom
    draw_rectangle(left + (www * 2), top - (hhh * 2), www, hhh) # bottom-right
    
draw_rectangle(-350, 350, 700, 700)
update()
exitonclick()
