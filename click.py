from mouse import daj_zdarzenie
from game_over import uncover_all_bombs, game_over
from draw_board import draw_board
from uncover_2nd_try import uncover_field
from flag import flag_field, update_flagged
import turtle

def click(board, window_width, window_hight, game_on, num_of_bombs):
    occurance, x, y = daj_zdarzenie()
    for i in range(len(board)): #checking where on the board user clicked
        for j in range(len(board[0])):
            if board[i][j][4] <= x < board[i][j][4]+window_width/len(board[0])\
                    and board[i][j][5] <= y < board[i][j][5]+window_hight/len(board):
                if occurance == "l_klik":
                    if board[i][j][2]: #user clicked on bomb
                        uncover_all_bombs(board)
                        draw_board(board, window_width, window_hight, num_of_bombs)
                        game_over(window_hight, window_width)
                        game_on = False
                    else: #uncovvering field
                        uncover_field(board, x, y, i, j)
                        draw_board(board, window_width, window_hight, num_of_bombs)
                        break
                elif occurance == "r_klik":
                    flag_field(board, x, y, i, j)
                    update_flagged(board)
                    draw_board(board, window_width, window_hight, num_of_bombs)
                    turtle.fd(window_hight)
                    #write_info()
                    turtle.backward(window_hight)
                    break


