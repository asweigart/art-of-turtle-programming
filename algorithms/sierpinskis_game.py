from turtle import *
import random
tracer(1, 0)
setworldcoordinates(0, 0, 960, 810)
bgcolor(0.1, 0.1, 0.1)
pencolor(1.0, 0.0, 0.0)
penup()
DOT_SIZE = 3

# TODO - animate this and also have the colors cycle

def halfway(x1, y1, x2, y2):
    #print('halfway of %s, %s and %s, %s is %s, %s' % (x1, y1, x2, y2, int(abs(x1 - x2) / 2.0) + min(x1, x2), int(abs(y1 - y2) / 2.0) + min(y1, y2)))
    #return (int(abs(x1 - x2) / 2.0) + min(x1, x2), int(abs(y1 - y2) / 2.0) + min(y1, y2))

    # debug - more lines of code than the previous one-liner, but might be easier to read
    if x1 > x2:
        halfwayx = int(abs(x1 - x2) / 2.0) + x2
    else:
        halfwayx = int(abs(x2 - x1) / 2.0) + x1

    if y1 > y2:
        halfwayy = int(abs(y1 - y2) / 2.0) + y2
    else:
        halfwayy = int(abs(y2 - y1) / 2.0) + y1

    return (halfwayx, halfwayy)

def play_sierpinskis_game(ax, ay, bx, by, cx, cy):
    px = ax
    py = ay

    for i in range(1000):
        random_point = random.randint(1, 3)
        if random_point == 1:
            px, py = halfway(px, py, ax, ay)
            goto(px, py)
            dot(DOT_SIZE)
        elif random_point == 2:
            px, py = halfway(px, py, bx, by)
            goto(px, py)
            dot(DOT_SIZE)
        elif random_point == 3:
            px, py = halfway(px, py, cx, cy)
            goto(px, py)
            dot(DOT_SIZE)

play_sierpinskis_game(random.randint(0, 960), random.randint(0, 810),
                      random.randint(0, 960), random.randint(0, 810),
                      random.randint(0, 960), random.randint(0, 810))
update()
exitonclick()
