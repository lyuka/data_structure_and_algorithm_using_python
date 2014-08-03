# Implementation of the Sparse Matrix ADT using a list.

class SparseMatrix:
    # Create a sparse matrix of size numRows * numCols initialized to 0.
    def __init__( self, numRows, numCols ):
        self._numRows = numRows
        self._numCols = numCols
        self._elementList = list()

    # Return the number of rows in the matrix
    def numRows( self ):
        return self._numRows

    # Return the number of colums in the matrix.
    def numCols( self ):
        return self._numCols

    # Return the value of element (i, j): x[i, j]
    def __getitem__( self, ndxTuple ):
        row = ndxTuple[0]
        col = ndxTuple[1]
        assert row >=0 and row < self.numRows() and col >=0 and col < self.numCols(), \
               "subscript out of range"
        ndx = self._findPosition( row, col )
        if ndx is not None:
            return self._elementList[ndx].value
        else:
            return 0
    
    # Set the value of element (i,j) to the value s: x[i,j] = s
    def __setitem__( self, ndxTuple, scalar ):
        ndx = self._findPosition( ndxTuple[0], ndxTuple[1] )
        if ndx is not None:
            if scalar != 0.0:
                self._elementList[ndx].value = scalar
            else:
                self._elementList.pop( ndx )
        else:
            if scalar != 0.0:
                element = _MatrixElement( ndxTuple[0], ndxTuple[1], scalar )
                self._elementList.append( element )

    # Scalar the matrix by the given scalar.
    def scaleBy( self, scalar ):
        for element in self._elementList:
            element.value *= scalar

    # add
    def __add__( self, rhsMatrix ):
        assert rhsMatrix.numRows() == self.numRows() and \
               rhsMatrix.numCols() == self.numCols(), \
               "Matrix sizes not compatible for the add operation."

        # Create the new matrix
        newMatrix = SparseMatrix( self.numRows(), self.numCols() )

        # Duplicate the lhsmatrix. The elements are mutable, thus we must
        # create new objects and not simply copy the reference.
        for element in self._elementList:
            dupElement = _MatrixElement( element.row, element.col, element.value)
            newMatrix._elementList.append( dupElement )

        # Iterate through each non-zero element of the rhsMatrix.
        for element in rhsMatrix._elementList:
            value = newMatrix[ element.row, element.col ]
            value += element.value
            newMatrix[ element.row, element.col ] = value

        # Return the new matrix
        return newMatrix
            

    # sub
    def __sub__( self, rhsMatrix ):
        assert rhsMatrix.numRows() == self.numRows() and \
               rhsMatrix.numCols() == self.numCols(), \
               "Matrix sizes not compatible for the sub operation."

        # Create the new matrix
        newMatrix = SparseMatrix( self.numRows(), self.numCols() )

        # Duplicate the lhsMatrix.
        for element in self._elementList:
            dupElement = _MatrixElement( element.row, element.col, element.value )
            newMatrix._elementList.append( dupElement )

        # Iterator through each non-zero element of the rhsMatrix.
        for element in rhsMatrix._elementList:
            value = newMatrix[ element.row, element.col ]
            value -= element.value
            newMatrix[ element.row, element.col ] = value

        # Return the new matrix
        return newMatrix

    # multiply
    def __mul__( self, rhsMatrix ):
        assert rhsMatrix.numRows() == self.numCols(), \
               "Marix sizes not compatible for the multiply operation."

        # Create the new matrix
        newMatrix = SparseMatrix( self.numRows(), rhsMatrix.numCols() )

        for row in range( self.numRows() ):
            for col in range( rhsMatrix.numCols() ):
                tmp_sum = 0
                for kk in range( self.numCols() ):
                    if self[ row, kk ] != 0 and rhsMatrix[ kk, col ] != 0:
                        tmp_sum += self[ row, kk ] * rhsMatrix[ kk, col ]
                newMatrix[ row, col ] = tmp_sum

        return newMatrix

    # Helper method used to find a specific matrix element (row, col) in the
    # list of non-zero entries. None is returned if the element is not found.
    def _findPosition( self, row, col ):
        n = len( self._elementList )
        for i in range( n ):
            if row == self._elementList[i].row and \
               col == self._elementList[i].col:
                return i
        return None

# Storage class for holding the non-zero matrix elements.
class _MatrixElement:
    def __init__( self, row, col, value ):
        self.row = row
        self.col = col
        self.value = value


if __name__ == '__main__':
    sparse_mat_A = SparseMatrix( 3, 4 )
    sparse_mat_B = SparseMatrix( 3, 4 )
    sparse_mat_C = SparseMatrix( 4, 2 )

    sparse_mat_A[0, 0] = 1
    sparse_mat_A[2, 3] = 3

    sparse_mat_B[1, 2] = 4
    sparse_mat_B[2, 3] = -3
    sparse_mat_B[2, 2] = 1

    sparse_mat_C[0, 0] = 5
    sparse_mat_C[2, 1] = 2
    sparse_mat_C[3, 1] = 11

    print 'mat A: '
    for i in range(3):
        for j in range(4):
            print sparse_mat_A[i, j],
        print ''

    print 'mat B: '
    for i in range(3):
        for j in range(4):
            print sparse_mat_B[i, j],
        print ''

    print 'mat C: '
    for i in range(4):
        for j in range(2):
            print sparse_mat_C[i, j],
        print ''

    add_mat_01 = sparse_mat_A + sparse_mat_B
    print 'A + B: '
    for i in range( add_mat_01.numRows() ):
        for j in range( add_mat_01.numCols() ):
            print add_mat_01[i, j],
        print ''

    sub_mat_02 = sparse_mat_A - sparse_mat_B
    print 'A - B: '
    for i in range( sub_mat_02.numRows() ):
        for j in range( sub_mat_02.numCols() ):
            print sub_mat_02[i, j],
        print ''

    mul_mat_03 = sparse_mat_A * sparse_mat_C
    print ' A * C: '
    for i in range( mul_mat_03.numRows() ):
        for j in range( mul_mat_03.numCols() ):
            print mul_mat_03[i, j],
        print ''
