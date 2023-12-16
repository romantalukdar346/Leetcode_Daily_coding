def isValidSudoku(self, board):
    
    row=len(board)
    col=len(board[0])

    row_list=[[] for _ in range(9)]
    col_list=[[] for _ in range(9)]
    sub_box=[[] for _ in range(9)]

    for i in range(row):
        for j in range(col):
            if board[i][j]!='.':
                row_list[i].append(int(board[i][j]))
                col_list[j].append(int(board[i][j]))
                sub_box[((i//3)*3 + j//3)].append(int(board[i][j]))

    for i in range(row):
        rs=set(row_list[i])
        cs=set(col_list[i])
        ss=set(sub_box[i])
        if len(rs)==len(row_list[i]) and len(cs)==len(col_list[i]) and len(ss)==len(sub_box[i]):
            pass
        else:
            return False
    return True