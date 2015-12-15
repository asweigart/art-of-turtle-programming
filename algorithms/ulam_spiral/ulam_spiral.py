from turtle import *
import math

tracer(1000, 0)

SPACING = 5

bgcolor('#353337')
pencolor('#CCCCCC')

def amount_of_divisors(number):
    total = 0
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            total += 1
    return total

penup() # (!) Try commenting this line out.
forward(SPACING) # 1 is not prime, so skip
left(90)
dot(2) # 2 is prime, so make a dot
forward(SPACING)
left(90)

current_number = 3
length = 3
while current_number < 40000:
    for i in range(2):
        for j in range(length):
            divs = amount_of_divisors(current_number)
            current_number += 1

            if divs == 0: # (!) Try changing > to == so that primes are marked.
                dot((int(math.sqrt(divs)) + 1) * 2, '#76b7eb')
            #else: # (!) Try uncommenting these two lines.
            #    dot(4, '#ffa25e')
            forward(SPACING)
        left(90)
    length += 1

update()
exitonclick()
