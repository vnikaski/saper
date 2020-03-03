from draw_board import write_info
import turtle

def you_won(window_hight, window_width):
    turtle.fd(window_width)
    write_info('YOU WON :)', window_hight/10, window_width)
    turtle.done()

def check_flags(board, flag_count, num_of_bombs, window_hight, window_width, game_on):
    if flag_count == num_of_bombs:
        check = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j][1] and board[i][j][2]:
                    check += 1
        if check == num_of_bombs:
            game_on = False
            you_won(window_hight, window_width)
