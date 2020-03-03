import turtle
from random import randint
from time import sleep
import tkinter
"""
to do: 
"""
# ------------------parameters---------------------------

num_of_bombs = randint(5, 20) # from 5 up to 20 bombs, randomly generated
game_on = True
window_width = 300
window_height = 300
flag_count = 0
rows = 10
columns = 10

# --------------------------------------------------------


# ----------------creating random board-------------------
# field parameters would be [if_visible, if_flagged, has_bomb, number_of_bombs_surrounding, left_x_cor, lower_y_cor]
def give_coordinates(board):
    global window_height, window_width
    y = window_height / 2 - window_height / len(board)
    for i in range(len(board)):
        x = -window_width/2
        for j in range(len(board[0])):
            board[i][j].append(x)
            board[i][j].append(y)
            x += window_width/len(board[0])
        x = -window_width/2
        y -= window_height / len(board)


# creating single "empty" field
def single_field():
    return [False, False, False, 0]     # [if_visible, if_flagged, has_bomb, number_of_bombs_surrounding]


def plant_bombs(rows, columns, board):    # this function plants bombs and returns their coordinates
    global num_of_bombs
    bombs_cor = []
    i = 0   # control variable for while loop
    while i != num_of_bombs:
        r = randint(0, rows-1)  # which row_index would bomb be in
        c = randint(0, columns-1)   # which column_index would bomb be in
        cor = [r, c]
        if cor not in bombs_cor:
            board[r][c][2] = True
            i += 1
            bombs_cor.append(cor)
    return bombs_cor


def add_how_many_bombs_nearby(board, bombs_cor):
    for i in range(len(bombs_cor)):
        if bombs_cor[i][0] != 0:   # asserting the bomb is not in the highest row
            board[bombs_cor[i][0]-1][bombs_cor[i][1]][3] += 1
        if bombs_cor[i][0] < len(board)-1:   # asserting the bomb is not in the lowest row
            board[bombs_cor[i][0]+1][bombs_cor[i][1]][3] += 1
        if bombs_cor[i][1] != 0:     # asserting the bomb is not in the boarder left column
            board[bombs_cor[i][0]][bombs_cor[i][1]-1][3] += 1
        if bombs_cor[i][1] < len(board[0])-1:   # asserting the bomb is not in the boarder right column
            board[bombs_cor[i][0]][bombs_cor[i][1]+1][3] += 1
        if bombs_cor[i][0] != 0 and bombs_cor[i][1] < len(board[0])-1:
            board[bombs_cor[i][0]-1][bombs_cor[i][1]+1][3] += 1
        if bombs_cor[i][0] != 0 and bombs_cor[i][1] != 0:
            board[bombs_cor[i][0]-1][bombs_cor[i][1]-1][3] += 1
        if bombs_cor[i][0] < len(board)-1 and bombs_cor[i][1] != 0:
            board[bombs_cor[i][0]+1][bombs_cor[i][1]-1][3] += 1
        if bombs_cor[i][0] < len(board)-1 and bombs_cor[i][1] < len(board[0])-1:
            board[bombs_cor[i][0]+1][bombs_cor[i][1]+1][3] += 1


def create_board(rows, columns):
    global num_of_bombs
    assert num_of_bombs <= rows*columns
    board = []
    for i in range(rows):   # creating empty board (no bombs)
        row = []
        for j in range(columns):
            row.append(single_field())
        board.append(row)
    bombs_cor = plant_bombs(rows,columns, board)
    add_how_many_bombs_nearby(board, bombs_cor)
    give_coordinates(board)
    return board

# ------------------------------------------------------------

# ------------------flagging functions------------------------

def flag_field(board, i, j):
    global flag_count, num_of_bombs
    if board[i][j][1]:  # checking if flagged already
        board[i][j][1] = False
        flag_count -= 1
    elif (not board[i][j][1]) and (not board[i][j][0]) and flag_count != num_of_bombs:  # asserting the field is not already visible and user still has flag
        board[i][j][1] = True
        flag_count += 1

# ---------------------------------------------------------


# ---------------------uncovering fields--------------------

def collect_empty(i, j, board, empties):
    if board[i][j][3] == 0 and (not board[i][j][0]): #if number of bombs nearby == 0 and field is not already uncovered
        empties.append([i, j])


def uncover_nearby(i, j, board, empties):
    if i != 0:                          # checking whether row is not the highest one
        collect_empty(i-1, j, board, empties)
        board[i-1][j][0] = True         # uncovering the field above
    if i != len(board)-1:               # checking  whether row is not the lowest one
        collect_empty(i+1, j, board, empties)
        board[i+1][j][0] = True         # uncovering the field below
    if j != 0:                          # checking whether column is not the one on the left end
        collect_empty(i, j-1, board, empties)
        board[i][j-1][0] = True         # uncovering the field on the left
    if j != len(board[0])-1:            # checking whether column is not the one on the right end
        collect_empty(i, j+1, board, empties)
        board[i][j+1][0] = True         # uncovering the field on the right
    if i != 0 and j != 0:
        collect_empty(i-1, j-1, board, empties)
        board[i-1][j-1][0] = True
    if i != 0 and j != len(board[0])-1:
        collect_empty(i-1, j+1, board, empties)
        board[i-1][j+1][0] = True
    if i != len(board)-1 and j != 0:
        collect_empty(i+1, j-1, board, empties)
        board[i+1][j-1][0] = True
    if i != len(board)-1 and j != len(board[0])-1:
        collect_empty(i+1, j+1, board, empties)
        board[i+1][j+1][0] = True


def uncover_field(board, i, j):
    global flag_count
    board[i][j][0] = True
    if board[i][j][1]: #if the field was flagged
        flag_count -= 1
    if board[i][j][3] == 0: #if there's zero bombs nearby
        empties = []
        empties.append([i, j])
        while len(empties) != 0:
            i, j = empties[0]
            uncover_nearby(i, j, board, empties)
            del empties[0]
# -------------------------------------------------------------

# ------------------drawing board--------------------------


def write_info(info, height, width):
    turtle.pencolor("Dark Slate Blue")   # setting pencolour
    turtle.fillcolor("Misty Rose")   # setting info background colour
    turtle.pendown()
    turtle.begin_fill()
    rectangle(height, width)     # drawing info background
    turtle.end_fill()
    turtle.right(90)    # going to the starting point of writing the info
    turtle.fd(width/2)
    turtle.left(90)
    turtle.penup()
    turtle.fd(height / 8)  # lower edge of the info will be in eighth of background height
    turtle.write(info, align="center", font=("Arial", int(height / 2), "normal"))
    turtle.backward(height / 8)    # going back to the left corner
    turtle.pendown()
    turtle.left(90)
    turtle.fd(width/2)
    turtle.right(90)


def rectangle(a, b):
    for i in range(2):
        turtle.fd(a)
        turtle.right(90)
        turtle.fd(b)
        turtle.right(90)


def draw_field(field_height, field_width, fillcolor):    # function to draw a single field
    turtle.pencolor("Dark Slate Blue")
    turtle.fillcolor(fillcolor)
    turtle.begin_fill()
    rectangle(field_height, field_width)
    turtle.end_fill()


def go_to_next_column(field_width):
    turtle.right(90)
    turtle.fd(field_width)
    turtle.left(90)


def draw_board(board):
    global window_height, window_width, num_of_bombs, game_on
    field_height = window_height / len(board)
    field_width = window_width/len(board[0])
    for i in reversed(range(len(board))):   # reversed, because drawing starts from the bottom left corner
        x_cor1 = turtle.xcor()
        y_cor1 = turtle.ycor()  # marking the begining of the row
        for j in range(len(board[0])):
            if (not board[i][j][0]) and (not board[i][j][1]):   # drawing an empty covered field (not visible and not flagged)
                draw_field(field_height, field_width, "Lavender")
                go_to_next_column(field_width)
            elif board[i][j][0] and board[i][j][3]==0 and (not board[i][j][2]):    # drawing empty uncovered field
                draw_field(field_height, field_width, "Azure")
                go_to_next_column(field_width)
            elif (not board[i][j][0]) and board[i][j][1] and game_on:     # drawing flagged field
                x_cor = turtle.xcor()
                y_cor = turtle.ycor()
                turtle.right(90)    # going to the starting point to draw the "flag"
                turtle.fd(field_width*(5/8))
                turtle.left(90)
                turtle.penup()
                turtle.fd(field_height/2)
                turtle.fillcolor("Navy")
                turtle.begin_fill()
                turtle.circle((window_width/len(board[0]))*(1/8))   # than drawing the "flag"
                turtle.end_fill()
                turtle.goto(x_cor, y_cor)
                go_to_next_column(field_width)
                turtle.pendown()
            elif board[i][j][0] and (not board[i][j][2]):   # drawing field with information (if visible and doesn't have bomb)
                x_cor = turtle.xcor()
                y_cor = turtle.ycor()
                draw_field(field_height, field_width, "Azure")
                turtle.right(90)
                turtle.fd(field_width/2)
                turtle.left(90)
                turtle.penup()
                turtle.fd(field_height/8)
                turtle.pendown()
                turtle.write(board[i][j][3], align="center", font=("Arial", int(field_height/2), "normal"))
                turtle.penup()
                turtle.goto(x_cor, y_cor)
                go_to_next_column(field_width)
                turtle.pendown()
            elif board[i][j][0] and board[i][j][2] and (not board[i][j][1]):   # drawing field with a bomb
                x_cor = turtle.xcor()
                y_cor = turtle.ycor()
                draw_field(field_height, field_width, "Azure")  # first drawing an empty field
                turtle.right(90)
                turtle.fd(field_width*(6/8))
                turtle.left(90)
                turtle.penup()
                turtle.fd(field_height/2)
                turtle.fillcolor("Tomato")
                turtle.begin_fill()
                turtle.circle((window_width/len(board[0]))*(1/4))  # then drawing the bomb
                turtle.end_fill()
                turtle.goto(x_cor, y_cor)
                go_to_next_column(field_width)
                turtle.pendown()
            elif (not game_on) and board[i][j][2] and board[i][j][1]: # the game has ended: drawing flagged bomb
                x_cor = turtle.xcor()
                y_cor = turtle.ycor()
                draw_field(field_height, field_width, "Azure")  # first drawing an empty field
                turtle.right(90)
                turtle.fd(field_width*(6/8))
                turtle.left(90)
                turtle.penup()
                turtle.fd(field_height/2)
                turtle.fillcolor("Tomato")
                turtle.begin_fill()
                turtle.circle((window_width/len(board[0]))*(1/4))  # then drawing the bomb
                turtle.end_fill()
                turtle.left(90)
                turtle.fd(field_width*(1/8))
                turtle.right(90)
                turtle.fillcolor("Navy")
                turtle.begin_fill()
                turtle.circle((window_width/len(board[0]))*(1/8))   # than drawing the "flag"
                turtle.end_fill()
                turtle.goto(x_cor, y_cor)
                go_to_next_column(field_width)
                turtle.pendown()
            elif (not game_on) and board[i][j][1] and (not board[i][j][2]): # the game has ended: drawing falsely flagged field
                x_cor = turtle.xcor()
                y_cor = turtle.ycor()
                turtle.pendown()
                turtle.pencolor("Tomato")
                turtle.goto(x_cor + field_width, y_cor + field_height)
                turtle.penup()
                turtle.goto(x_cor, y_cor + field_width)
                turtle.pendown()
                turtle.goto(x_cor + field_width, y_cor)
                turtle.pencolor("Dark Slate Blue")


        turtle.goto(x_cor1, y_cor1)
        turtle.fd(field_height)
    write_info(f"Flags left: {num_of_bombs - flag_count}", window_height / 10, window_width)
    turtle.backward(window_height)
    turtle.update


# -------------------------------------------------------------

# ----------------begining of the graphics---------------------

# drawing the covered board with initial info
def ini_graphics(board):
    global window_width, window_height, num_of_bombs
    turtle.hideturtle()
    turtle.tracer(0,0)
    turtle.seth(90)
    turtle.penup()
    turtle.goto(-window_width/2, -window_width/2)  # going to the bottom left corner
    turtle.pendown()
    draw_board(board)
    turtle.fd(window_height)
    write_info("Click any field to start the game", window_height / 10, window_width)
    turtle.backward(window_height)

# ------------------------------------------------------------

# ------------------game over scenario------------------------


def uncover_all_bombs(board):
    for i in range(len(board)):
        for j in range(len(board[0])):  # uncovering all bombs
            if board[i][j][2]:
                board[i][j][0] = True


def game_over():
    global window_height, window_width

    turtle.fd(window_width)
    write_info('GAME OVER', window_height / 10, window_width)
    turtle.done()


# ------------------------------------------------------------

# -------------------winning scenario------------------------
def you_won(board):
    global window_height, window_width
    sleep(1)
    draw_board(board)
    turtle.fd(window_width)
    write_info('YOU WON :)', window_height / 10, window_width)
    turtle.done()


def check_flags(board):
    global window_width, window_height, num_of_bombs, flag_count, game_on
    if flag_count == num_of_bombs:
        check = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j][1] and board[i][j][2]:
                    check += 1
        game_on = False
        if check == num_of_bombs:
            you_won(board)
        else:
            uncover_all_bombs(board)
            draw_board(board)
            game_over()

# --------------------------------------------------------

# -----------------this part is not my code---------------------
# ------------- Obsługa myszki - początek-------------
zdarzenie_myszki = ""
x_myszki = 0
y_myszki = 0


def ustaw_guziki_myszy(guzik):
    def result(x, y):
        global zdarzenie_myszki, x_myszki, y_myszki
        zdarzenie_myszki, x_myszki, y_myszki = guzik, x, y

    return result


def daj_zdarzenie():
    global zdarzenie_myszki, x_myszki, y_myszki
    while zdarzenie_myszki == "":
        tkinter._default_root.update()
        sleep(0.01)
    pom, zdarzenie_myszki = zdarzenie_myszki, ""
    return pom, x_myszki, y_myszki


def ini_myszki():
    for guzik, numer in zip(["l_klik", "m_klik", "r_klik"], range(1, 4)):
        turtle.onscreenclick(ustaw_guziki_myszy(guzik.lower()), numer)


# ------------- Obsługa myszki - koniec-------------
# --------------------------------------------------

# --------what happens when user clicks---------------


def click(board):
    global window_width, window_height, num_of_bombs, game_on
    occurrence, x, y = daj_zdarzenie()
    for i in range(len(board)):  # checking where on the board user clicked
        for j in range(len(board[0])):
            if board[i][j][4] <= x < board[i][j][4]+window_width/len(board[0])\
                    and board[i][j][5] <= y < board[i][j][5]+window_height/len(board):
                if occurrence == "l_klik":
                    if board[i][j][2]:  # user clicked on bomb
                        game_on = False
                        uncover_all_bombs(board)
                        draw_board(board)
                        game_over()
                    else:   # uncovvering field
                        uncover_field(board, i, j)
                        draw_board(board)
                        break
                elif occurrence == "r_klik":  # flagging/unflagging field
                    flag_field(board, i, j)
                    draw_board(board)
                    turtle.fd(window_height)
                    turtle.backward(window_height)
                break  # we've already found the field user clicked on, so it isn't needed to look further


# ------------------------------------------------------------

def main():
    global num_of_bombs, game_on, flag_count, rows, columns
    ini_myszki()
    board = create_board(rows, columns)
    ini_graphics(board)
    while game_on:
        click(board)
        check_flags(board)



main()
