import turtle
from flag import update_flagged

def write_info(info, hight, width):
    turtle.pencolor("Dark Slate Blue") #setting pencolour
    turtle.fillcolor("Misty Rose") #setting info background colour
    turtle.pendown()
    turtle.begin_fill()
    rectangle(hight, width) #drawing info background
    turtle.end_fill()
    turtle.right(90)    #going to the starting point of writing the info
    turtle.fd(width/2)
    turtle.left(90)
    turtle.penup()
    turtle.fd(hight/8)  #lower edge of the info will be in eighth of background hight
    turtle.write(info, align="center", font=("Arial", int(hight/2), "normal"))
    turtle.backward(hight/8)    #going back to the left corner
    turtle.pendown()
    turtle.left(90)
    turtle.fd(width/2)
    turtle.right(90)

def rectangle(a,b):
    for i in range(2):
        turtle.fd(a)
        turtle.right(90)
        turtle.fd(b)
        turtle.right(90)

def draw_field(field_hight,field_width, fillcolor): #function to draw a single field
    turtle.pencolor("Dark Slate Blue")
    turtle.fillcolor(fillcolor)
    turtle.begin_fill()
    rectangle(field_hight,field_width)
    turtle.end_fill()

def go_to_next_column(field_width):
    turtle.right(90)
    turtle.fd(field_width)
    turtle.left(90)

def draw_board(board, window_width, window_hight, num_of_bombs):
    field_hight = window_hight/len(board)
    field_width = window_width/len(board[0])
    for i in reversed(range(len(board))):
        x_cor1 = turtle.xcor()
        y_cor1 = turtle.ycor()
        for j in range(len(board[0])):
            if (not board[i][j][0]) and (not board[i][j][1]): #drawing empty field if (not visible and not flagged)
                draw_field(field_hight,field_width, "Lavender")
                go_to_next_column(field_width)
            elif (board[i][j][0] and board[i][j][3]==0 and (not board[i][j][2])): #drawing empty uncovered field
                draw_field(field_hight,field_width, "Azure")
                go_to_next_column(field_width)
            elif ((not board[i][j][0]) and board[i][j][1]):#drawing flagged field
                x_cor = turtle.xcor()
                y_cor = turtle.ycor()
                draw_field(field_hight,field_width, "Lavender")
                turtle.right(90)
                turtle.fd(field_width*(5/8))
                turtle.left(90)
                turtle.penup()
                turtle.fd(field_hight/2)
                turtle.fillcolor("Navy")
                turtle.begin_fill()
                turtle.circle((window_width/len(board[0]))*(1/8))
                turtle.end_fill()
                turtle.goto(x_cor,y_cor)
                go_to_next_column(field_width)
                turtle.pendown()
            elif board[i][j][0] and (not board[i][j][2]):#drawing field with information (if visible and doesn't have bomb)
                x_cor = turtle.xcor()
                y_cor = turtle.ycor()
                draw_field(field_hight,field_width, "Azure")
                turtle.right(90)
                turtle.fd(field_width/2)
                turtle.left(90)
                turtle.penup()
                turtle.fd(field_hight/8)
                turtle.pendown()
                turtle.write(board[i][j][3], align="center", font=("Arial", int(field_hight/2), "normal"))
                turtle.penup()
                turtle.goto(x_cor,y_cor)
                go_to_next_column(field_width)
                turtle.pendown()
            elif board[i][j][0] and board[i][j][2]: #drawing field with a bomb
                x_cor = turtle.xcor()
                y_cor = turtle.ycor()
                draw_field(field_hight,field_width, "Azure")
                turtle.right(90)
                turtle.fd(field_width*(6/8))
                turtle.left(90)
                turtle.penup()
                turtle.fd(field_hight/2)
                turtle.fillcolor("Tomato")
                turtle.begin_fill()
                turtle.circle((window_width/len(board[0]))*(1/4))
                turtle.end_fill()
                turtle.goto(x_cor,y_cor)
                go_to_next_column(field_width)
                turtle.pendown()
        turtle.goto(x_cor1,y_cor1)
        turtle.fd(field_hight)
    write_info(f"Flags left: {num_of_bombs - update_flagged(board)}", window_hight/10, window_width)
    turtle.backward(window_hight)
    turtle.update()

