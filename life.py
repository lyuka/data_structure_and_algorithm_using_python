# Implements the LifeGrid ADT for the use with the game of Life.
from myarray import myArray2D

class LifeGrid:
	# Defines constants to represent the cell states.
	DEAD_CELL = 0
	LIVE_CELL = 1

	# Creates the game grid and initializes the cells to dead.
	def __init__( self, numRows, numCols ):
		# Allocate the 2-D array for the grid.
		self._grid = myArray2D( numRows, numCols )
		# Clear the grid and set all cells to dead.
		self.configure( list() )

	# Returns the number of rows in the grid.
	def numRows( self ):
		return self._grid.numRows()

	# Returns the number of columns in the grid.
	def numCols( self ):
		return self._grid.numCols()

	# Configures the grid to contain the given live cells.
	def configure( self, coordList ):
		# Clear the game grid.
		for i in range( self.numRows() ):
			for j in range( self.numCols() ):
				self.clearCell(i, j)

		# Set the indicated cells to be alive
		for coord in coordList:
			self.setCell( coord[0], coord[1])

	# Does the indicated cell contain  a live organism?
	def isLiveCell( self, row, col ):
		return self._grid[row, col] == self.LIVE_CELL

	# Clears the indicated cell by setting it to dead.
	def clearCell( self, row, col ):
		self._grid[row, col] = self.DEAD_CELL

	def setCell( self, row, col ):
		self._grid[row, col] = self.LIVE_CELL

	# Returns the number of live neighbors for the given cell.
	def numLiveNeighbors( self, row, col ):
		#print str(row) + ' , ' + str(col)
		alive_cnt = 0
		for i in [-1, 0, 1]:
			for j in [-1, 0, 1]:
				if row + i >= 0 and row + i < self.numRows() and col + j >= 0 and col + j < self.numCols():
					if self.isLiveCell(row+i, col+j):
						alive_cnt += 1
						#print '( ' + str(row+i) + ', ' + str(col+j) + ' ): ' + 'YES' 
		return alive_cnt - self.isLiveCell(row, col)

	# Prints the current configure
	def print_config( self ):
		for i in range( self.numRows() ):
			for j in range( self.numCols() ):
				print self._grid[i, j], 
			print ""

if __name__ == '__main__':
	init_grid = LifeGrid(5, 5)
	init_grid.print_config()

	print ""

	#for i in range( init_config.numRows() ):
	#	for j in range( init_config.numRows() ):
	#		init_config.setCell(i, j)
	init_grid.configure([ (1, 2), (2, 1), (2, 2), (2, 3) ])
	init_grid.print_config()
	print init_grid.numLiveNeighbors(1, 2)
	#for i in range(5):
	#	for j in range(5):
	#		print '( ' + str(i) + ', ' + str(j)  + ' )',
	#		print init_grid.numLiveNeighbors(i, j)


