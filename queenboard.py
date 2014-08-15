# NQueens Board ADT Class
from myarray import myArray2D

class QueenBoard():
    QUEEN_CELL = 1
    NON_QUEEN_CELL = 0
    
    def __init__( self, n ):
        # Creates an n*n empty board.
        self._board = myArray2D( n, n )
        self._clear( self.NON_QUEEN_CELL )

    def _clear( self, value ):
        self._board.clear( value )

    
    # Returns the size of the board
    def size( self ):
        return self._board.numRows()

    # Returns the number of queens currently positioned on the board.
    def numQueen( self ):
        queen_cnt = 0
        for i in range( self.size() ):
            for j in range( self.size() ):
                if self._board[i, j] == self.QUEEN_CELL:
                    queen_cnt += 1
        return queen_cnt

    # Returns a boolean value indicating if the given square is currently unguarded.
    def unguarded( self, row, col ):
        for i in range( self.size() ):  # vertical direction
            if i != row and self._board[i, col] == self.QUEEN_CELL:
                return False
        for j in range( self.size() ):  # horizontal direction
            if j != col and self._board[row, j] == self.QUEEN_CELL:
                return False
        for i in range( 1, self.size() ):   # left-up direction
            if row - i < 0 or col - i < 0:
                break
            if self._board[row - i, col - i] == self.QUEEN_CELL:
                return False
        for i in range( 1, self.size() ):   # right-down direction
            if row + i >= self.size() or col + i >= self.size():
                break
            if self._board[row + i, col + i] == self.QUEEN_CELL:
                return False
        for i in range( 1, self.size() ):   # left-down direction
            if row - i < 0 or col + i >= self.size():
                break
            if self._board[row - i, col + i] == self.QUEEN_CELL:
                return False
        for i in range( 1, self.size() ):   # right-up direction
            if row + i >= self.size() or col - i < 0:
                break
            if self._board[row + i, col - i] == self.QUEEN_CELL:
                return False
        return True

    # Places a queen on the board at position (row, col)
    def placeQueen( self, row, col ):
        self._board[row, col] = self.QUEEN_CELL

    # Removes the queen from position (row, col)
    def removeQueen( self, row, col ):
        self._board[row, col] = self.NON_QUEEN_CELL

    # Resets the board to its original state
    def reset( self ):
        self._clear( self.NON_QUEEN_CELL )

    # Prints the board
    def draw( self ):
        for i in range( self.size() ):
            for j in range( self.size() ):
                print self._board[i, j],
            print ''
    
                

    
