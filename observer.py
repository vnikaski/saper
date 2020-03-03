def time_travel(board):
    board2 = board.copy()
    return board2

def note_changes(board, board2):
    changed = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] != board2[i][j]:
                changed.append([i,j])
    return changed
