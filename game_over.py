import turtle
from draw_board import write_info

def uncover_all_bombs(board):
    for i in range(len(board)):
        for j in range(len(board[0])): #uncovering all bombs
            if board[i][j][2]:
                board[i][j][0] = True

def game_over(window_hight, window_width):
    turtle.fd(window_width)
    write_info('GAME OVER', window_hight/10, window_width)
    turtle.done()

