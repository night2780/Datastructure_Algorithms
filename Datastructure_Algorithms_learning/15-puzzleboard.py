board = ([[1,2,3,4],
  [5,6,7,8],
  [9,10,None,12],
  [13,14,11,15,]])
def up(a):
    for i in range(len(board)):
        row = board[i]
        for j in range(len(row)):
            if row[j] == None:
                row[j],row[j-1] == row[j-1],row[j]
            print(row[j])
print(up(board))
