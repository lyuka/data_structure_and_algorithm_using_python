# solve the n-queens problem using recursive
from queenboard import QueenBoard

cnt = 0
def solveNQueens( board, col ):
    global cnt
    if board.numQueen() == board.size():
        cnt += 1
        print 'Placement %d: ' % cnt
        board.draw()
        #board.reset()
        return True
    else:
        flag = 0
        for row in range( board.size() ):
            if board.unguarded( row, col ):
                board.placeQueen( row, col )
                if solveNQueens( board, col+1 ):
                    flag = 1
                board.removeQueen( row, col )
        if flag:
            return True
        else:
            return False

myboard = QueenBoard( 8 )
solveNQueens( myboard, 0 )
