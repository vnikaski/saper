import turtle
from draw_board import draw_board, write_info, rectangle
#-----------------drawing parameters-------------------------

#------------------------------------------------------------


#every painted element will start and end from the left bottom corner, seth 90
#every written element begins set at the centre of the writing




def ini_graphics(board, window_width, window_hight, num_of_bombs):
    turtle.hideturtle()
    turtle.tracer(0,0)
    #turtle.speed(10)
    turtle.seth(90)
    turtle.penup()
    turtle.goto(-window_width/2, -window_width/2)
    turtle.pendown()
    draw_board(board, window_width, window_hight, num_of_bombs)
    turtle.fd(window_hight)
    write_info("Click any field to start the game", window_hight/10, window_width)
    turtle.backward(window_hight)
    turtle.update()
