
def update_flagged(board):
    flag_count = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j][1] and board[i][j][0]:
                board[i][j][1] = False
            elif board[i][j][1]:
                flag_count += 1
    return flag_count

def flag_field(board,x,y,i,j):
    if board[i][j][1]: #checking if flagged already
        board[i][j][1] = False
    elif (not board[i][j][1]) and (not board[i][j][0]): #asserting the field is not already visible
        board[i][j][1] = True

