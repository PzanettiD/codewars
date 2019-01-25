def done_or_not(board): #board[i][j]
    maX = len(board)
    Trows = []
    Tcolumns = []
    for i in range(maX):
        rows = []
        columns = []
        for j in range(maX):
            if board[i][j] in rows:
                return 'Try again!'
            else:
                rows.append(board[i][j])
            if board[j][i] in columns:
                return 'Try again!'
            else:
                columns.append(board[j][i])
        if rows in Trows:
            return 'Try again!'
        else:
            Trows.append(rows)
        if columns in Tcolumns:
            return 'Try again!'
        else:
            Tcolumns.append(columns)
    region1 = []
    region2 = []
    region3 = []
    for k in range(maX):
        if k == 3:
            region1 = []
            region2 = []
            region3 = []
        elif k == 3:
            region1 = []
            region2 = []
            region3 = []
        elif k == 6:
            region1 = []
            region2 = []
            region3 = []
        for m in range(maX):
            if m < 3:
                if board[k][m] in region1:
                    return 'Try again!'
                else:
                    region1.append(board[k][m])
            elif m < 6:
                if board[k][m] in region2:
                    return 'Try again!'
                else:
                    region2.append(board[k][m])
            else:
                if board[k][m] in region3:
                    return 'Try again!'
                else:
                    region3.append(board[k][m])
    return 'Finished!'
b = [[1, 3, 2, 5, 7, 9, 4, 6, 8],
     [4, 9, 8, 2, 6, 1, 3, 7, 5],
     [7, 5, 6, 3, 8, 4, 2, 1, 9],
     [6, 4, 3, 1, 5, 8, 7, 9, 2],
     [5, 2, 1, 7, 9, 3, 8, 4, 6],
     [9, 8, 7, 4, 2, 6, 5, 3, 1],
     [2, 1, 4, 9, 3, 5, 6, 8, 7],
     [3, 6, 5, 8, 1, 7, 9, 2, 4],
     [8, 7, 9, 6, 4, 2, 1, 5, 3]]

print(done_or_not(b))