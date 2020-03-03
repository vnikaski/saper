
#field parameters would be [if_visible, if_flagged, has_bomb, number_of_bombs_surrounding, left_x_cor, lower_y_cor]
def give_coordinates(board, window_hight, window_width):
    y = window_hight/2 - window_hight/len(board)
    for i in range(len(board)):
        x = -window_width/2
        for j in range(len(board[0])):
            board[i][j].append(x)
            board[i][j].append(y)
            x += window_width/len(board[0])
        x = -window_width/2
        y -= window_hight/len(board)


