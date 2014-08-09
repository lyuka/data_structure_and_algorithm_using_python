# Implements the Maze ADT using a 2-D array.
from myarray import myArray2D
from lliststack import Stack

class Maze:
    # Define constants to represent contents of the maze cells.
    MAZE_WALL   = '*'
    PATH_TOKEN  = 'X'
    TRIED_TOKEN = 'o'

    # Creates a maze object with all cells marked as open.
    def __init__( self, numRows, numCols ):
        self._mazeCells = myArray2D( numRows, numCols )
        self._startCell = None
        self._exitCell  = None

    # Returns the number of rows in the maze.
    def numRows( self ):
        return self._mazeCells.numRows()

    # Returns the number of columns in the maze.
    def numCols( self ):
        return self._mazeCells.numCols()

    # Fills the indicated cell with a "wall" marker.
    def setWall( self, row, col ):
        assert row >=0 and row < self.numRows() and \
               col >=0 and col < self.numCols(), \
               "Cell index out of range."
        self._mazeCells[row, col] = self.MAZE_WALL

    # Sets the starting cell position.
    def setStart( self, row, col ):
        assert row >= 0 and row < self.numRows() and \
               col >= 0 and col < self.numCols(), \
               "Cell index out of range."
        self._startCell = _CellPosition( row, col )

    # Sets the exit cell position.
    def setExit( self, row, col ):
        assert row >= 0 and row < self.numRows() and \
               col >= 0 and col < self.numCols(), \
               "Cell index out of range."
        self._exitCell = _CellPosition( row, col )

    # Attempts to solve the maze by finding a path from the starting cell
    # to the exit. Returns True if a path is found and False otherwise.
    def findPath( self ):
        path_stack = Stack()
        cur_cell = self._startCell
        path_stack.push(cur_cell)
        self._markPath( cur_cell.row, cur_cell.col )
        
        while len( path_stack ) != 0:
            flag_valid = 0
            for (v, h) in [(1, 0), (-1, 0), (0, -1), (0 ,1)]:
                cur_row = cur_cell.row + v
                cur_col = cur_cell.col + h
                if self._validMove( cur_row, cur_col ):
                    path_stack.push( _CellPosition(cur_row, cur_col) )
                    self._markPath( cur_row, cur_col )
                    #print "( " + str(cur_row) + ", " + str(cur_col) + " ) is valid Path Point"
                    flag_valid = 1
                    break
            if flag_valid == 0:
                pop_cell = path_stack.pop()
                self._markTried( pop_cell.row, pop_cell.col )
                #print "( " + str(pop_cell.row) + ", " + str(pop_cell.col) + " ) is Invalid Path Point"
                if len(path_stack) == 0:
                    return False
            cur_cell = path_stack.peek()
            #print "( " + str(cur_cell.row) + ", " + str(cur_cell.col) + " ) is on the top."
            if self._exitFound( cur_cell.row, cur_cell.col ):
                #print len(path_stack)
                return True
        #return False

    # Resets the maze by removing all "path" and "tried" tokens
    def reset( self ):
        for row in range( self.numRows() ):
            for col in range( self.numCols() ):
                cur_cell = self._mazeCells[row, col]
                if cur_cell == self.TRIED_TOKEN or cur_cell == self.PATH_TOKEN:
                    self._mazeCells[row, col] = '.'

    # Prints a text-based representation of the maze.
    def draw( self ):
        for row in range( self.numRows() ):
            for col in range( self.numCols() ):
                cur_cell = self._mazeCells[row, col]
                if cur_cell is None:
                    print '.',
                else:
                    print cur_cell,
            print ''

    # Returns True if the given cell position is a valid move.
    def _validMove( self, row, col ):
        return row >= 0 and row < self.numRows() and \
               col >= 0 and col < self.numCols() and \
               self._mazeCells[row, col] is None

    # Helper method to determin if the exit was found.
    def _exitFound( self, row, col ):
        return row == self._exitCell.row and \
               col == self._exitCell.col

    # Drops a "tried" token at the given cell.
    def _markTried( self, row, col ):
        self._mazeCells[row, col] = self.TRIED_TOKEN
        
    # Drops a "path" token at the given cell.
    def _markPath( self, row, col ):
        self._mazeCells[row, col] = self.PATH_TOKEN

# Private storage class for holding a cell position.
class _CellPosition( object ):
    def __init__( self, row, col ):
        self.row = row
        self.col = col
