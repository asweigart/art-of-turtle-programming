from turtle import *
tracer(100, 0)

mona_lisa_data = '0x54a9554ebaaab5555b776eeb56addebdb5db5b33fd9b6d5d6db55affcaeed576d559dd71576ab7a9a76ee32ceb59b556edd591df6b5aead5b265add256954aa52ad5aa55aa96ab55fd576d569d2b556affea992a955b4aa94effd4dd555496aa57f7feb45554a51534b9dfecb2aa36caa4a627ff14a49c254922d12ffd69345b54552c037f88a951423249a89ffe6905494892bc44bfda6689e74925a22bfd7125432a927800bff9d24bdeac83b5edfef6935fb7757fbbfff6d10adddd4ba9b5ffff4d5eeef37a913ff55255fabaff86aaffff92aafffd59103feafaadfb6fffc99fffe8ab5bff5ffc947ffffbdffd6f7f571ffffeeb6f7bfefe3d57eeffffffff77d9afbf7f5b7bbd7ffe5b7fff7efbff7fbff29fffafbffeffdebf97ffffdfedff6ffffdffffded7feffdd6fffffff7fd5fdb76ffedefffffffffffb7ff77fbb7dbbfef5b7feb57fdd6ddbf5efbdeb5bfffd6feeffdffe9afffdedefbb7fff8227fefafbfdfbefe5116bfcbbb7eeffde048fffe4dddfbbffca027ffbb6ff75f7fa090bf7fdd7bbabdfc0096fbee33ffdf7e2484ffbfbd1ddebff000170dffbef7fcfca910affffe9fb5ffe00897bffffdbdc7ff90017fffffefabffee805ffffeafefefefb757beefffb76ebf7fbfffffbffbf76ffbeedbfffffdffdbdffff7ffffffffffffffbbeff6bfefb76ffffdffffff7fbffb3fbfffffffbbfefd59efffdbefeffffbeafffffffffffffff7f7fefffffffffeedfbeffedfbffffffffeffffffbffeffffff7efdf7ffffffffff7fffefffffffffdfffeffffffbefffffbfbffdffffffff7bffff7ffffffffbfffffffbdfffbbdfffffffbdffebbffffffffffffff7efffffffffffff7feff5ffffff7f7ffbf76f05ffdffdfffff7bf892bffffffdfffffbe4a5fffffffefffffd50affffffffffffdf6a43fffffffffffffbb51f7fdfbfffffffd4baad57ffdfbfffd6b4f7ffffffffffff3ae7affffffffbff5be73f77effffeff7e8bbdffffffddffff5bfcefbf7ffffff7fd8def7fffefffffffeffffbfffffffffffb7fffffffffffffffefb77fffffffffffffffffffffffbffffffbfffffffffffffffffffffffffffffff7fffffffffffffffffffffff7ffffffffffffffffffffffff7ff7ffdfffffffeffffffffffffffffffffffff7fffffffffffffffffffffffffff'



def draw_from_data(image_data, image_width, image_height, left, top, pixel_size):
    penup()
    
    in_binary = bin(int(image_data, 16))
    in_binary = in_binary[2:] # remove '0b' from start

    in_binary = in_binary.rjust(image_width * image_height, '0') # add leading zeros
    # TODO: is this even needed?
    #assert not (len(in_binary) > image_width * image_height), 'Too much image data for the width x height size given.'

    for y in range(image_height):
        for x in range(image_width):
            goto(left + (x * pixel_size), top - (y * pixel_size))

            if in_binary[y * image_width + x] == '1': # (!) Try switching this to '0'.
                begin_fill()
                setheading(0)
                forward(pixel_size) # draw top of the box
                right(90)
                forward(pixel_size) # draw right edge of the box
                right(90)
                forward(pixel_size) # draw bottom of the box
                right(90)
                forward(pixel_size) # draw left edge of the box
                end_fill()          # fill in the box

bgcolor('#FFF7D0')
fillcolor('#FF0C6B')
draw_from_data(mona_lisa_data, 68, 100, -272, 400, 4)
fillcolor('#CE18FF')
draw_from_data(mona_lisa_data, 68, 100, 0, 400, 4)
fillcolor('#7C0BE8')
draw_from_data(mona_lisa_data, 68, 100, -272, 0, 4)
fillcolor('#460CFF')
draw_from_data(mona_lisa_data, 68, 100, 0, 0, 4)

update()
exitonclick()          
