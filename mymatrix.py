#Implementation of the Matrix ADT using a 2-D array
from myarray import myArray2D

class myMatrix:
    # Creates a matrix of size numRows * numCols initialized to 0
    def __init__( self, numRows, numCols ):
        self._theGrid = myArray2D( numRows, numCols )
        self._theGrid.clear( 0 )

    # Returns the number of rows in the matrix
    def numRows( self ):
        return self._theGrid.numRows()

    # Returns the number of columns in the matrix
    def numCols( self ):
        return self._theGrid.numCols()

    # Returns the value of element (i, j): x[i,j]
    def __getitem__( self, ndxTuple ):
        return self._theGrid[ ndxTuple[0], ndxTuple[1] ]

    # Sets the value of element (i, j) to the value s: x[i, j] = s
    def __setitem__( self, ndxTuple, scalar ):
        self._theGrid[ ndxTuple[0], ndxTuple[1] ] = scalar

    # Scales the matrix by the given scalar
    def scaleBy( self, scalar ):
        for r in range( self.numRows() ):
            for  c in range( self.numCols() ):
                self[ r, c ] *= scalar

    # Creates and returns a new matrix that is the transpose of this matrix
    def tranpos( self ):
        # Create the new Matrix
        newMatrix = myMatrix( self.numCols(), self.numRows() )

        for r in range( self.numCols() ):
            for c in range( self.numRows() ):
                newMatrix[r, c] = self[c, r]
        return newMatrix

    # Creates and returns a new matrix that results from matrix addition
    def __add__( self, rhsMatrix):
        assert rhsMatrix.numRows() == self.numRows() and \
            rhsMatrix.numCols() == self.numCols(), \
            "Matrix sizes not compatible for the add operation."
        # Create the new matrix
        newMatrix = myMatrix( self.numRows(), self.numCols() )
        # Add the corresponding elements in the two matrices
        for r in range( self.numRows() ):
            for c in range( self.numCols() ):
                newMatrix[r, c] = self[r, c] + rhsMatrix[r, c]
        return newMatrix

    # Creates and returns a new matrix that results from matrix subtraction
    def __sub__( self, rhsMatrix ):
        #pass
        assert rhsMatrix.numRows() == self.numRows() and \
               rhsMatrix.numCols() == self.numCols(), \
               "Matrix sizes not compatible for the subtraction."
        # Create the new matrix
        newMatrix = myMatrix( self.numRows(), self.numCols() )
        # Sub the corresponding elements in the two matrices
        for r in range( self.numRows() ):
            for c in range( self.numCols() ):
                newMatrix[r, c] = self[r, c] - rhsMatrix[r, c]
        return newMatrix

    # Creates and returns a new matrix and results from matrix multiplication
    def __mul__( self, rhsMatrix ):
        #pass
        assert rhsMatrix.numRows() == self.numCols(), \
               "Matrix size not compatible for the multiplication."
        # Create the new matrix
        newMatrix = myMatrix( self.numRows(), rhsMatrix.numCols() )
        # Multiply the corresponding elements in the two matrices
        for r in range( self.numRows() ):
            for c in range( rhsMatrix.numCols() ):
                newMatrix[r, c] = 0
                for j in range( self.numCols() ):
                    newMatrix[r, c] += self[r, j] * rhsMatrix[j, c]
        return newMatrix

    # Print the matrix
    def printMat( self ):
        for i in range( self.numRows() ):
            for j in range( self.numCols() ):
                print self[i, j],
            print ""
            

if __name__ == '__main__':
    mat_a = myMatrix(3, 4)
    print "Matrix a: "
    for i in range(mat_a.numRows()):
        for j in range(mat_a.numCols()):
            mat_a[i, j] = 3
    mat_a.printMat()

    mat_b = myMatrix(3, 4)
    print "Matrix b: "
    for i in range(mat_b.numRows()):
        for j in range(mat_b.numCols()):
            mat_b[i, j] = 5
    mat_b.printMat()

    print "a + b: "
    mat_c = mat_a + mat_b
    mat_c.printMat()

    print "a.T: "
    mat_a_t = mat_a.tranpos()
    mat_a_t.printMat()

    print "a - b: "
    mat_d = mat_a - mat_b
    mat_d.printMat()

    print "a * a.T: "
    mat_e = mat_a * mat_a_t
    mat_e.printMat()

    print "a * 3: "
    mat_a.scaleBy(3)
    mat_a.printMat()

    print "a * b: "
    mat_f = mat_a * mat_b
    mat.f.printMat()
