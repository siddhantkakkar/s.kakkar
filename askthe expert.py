import random

import turtle as t

t.bgcolor('yellow')

caterpiller = t.Turtle()

caterpiller.shape('square')

caterpiller.color('red')

caterpiller.speed(0)

caterpiller.penup()

caterpiller.hideturtle()

leaf = t.Turtle()

leaf_shape = ((0, 0), (14, 2), (18, 16), (20, 20), (6, 18), (2, 14))

t.register_shape('leaf', leaf_shape)

leaf.shape('leaf')

leaf.color('green')

leaf.penup()

leaf.hideturtle()

leaf.speed(0)

game_started = False

text_turtle = t.Turtle()

text_turtle.write('Press SPACE to start', align='center', font=('Arial', 16, 'bold'))

text_turtle.hideturtle()

score_turtle = t.Turtle()

score_turtle.hideturtle()

score_turtle.speed(0)


def outside_window():

    left_wall = t.window_width() / 2

    right_wall = t.window_width() / 2

    top_wall = t.window_height() / 2

    bottum_wall = t.window_height() / 2

    (x, y) = caterpiller.pos()

    # outside = \
    #
    #     x <












































































































































































