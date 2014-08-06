# Implementation of the Sparse Matrix ADT using an array of linked lists.
from myarray import myArray

class SparseMatrix:
    # Creates a sparse matrix of size numRows * numCols initialized to 0
    def __init__( self, numRows, numCols ):
        self._numCols = numCols
        self._listOfRows = myArray( numRows )

    # Returns the number of rows in the matrix.
    def numRows( self ):
        return len( self._listOfRows )

    # Returns the number of columns in the matrix.
    def numCols( self ):
        return self._numCols

    # Returns the value of element (i,j): x[i, j]
    def __getitem__( self, ndxTuple ):
        row = ndxTuple[0]
        col = ndxTuple[1]
        
        assert row >= 0 and row < self.numRows() and col >= 0 and col < self.numCols(),\
               "subsripts out of range"

        curNode = self._listOfRows[row]
        while curNode is not None and curNode.col != col:
            curNode = curNode.next

        if curNode:
            return curNode.value
        else:
            return 0

    # Sets the value of element (i, j) to the value s: x[i, j] = s
    def __setitem__( self, ndxTuple, value ):
        row = ndxTuple[0]
        col = ndxTuple[1]

        assert row >= 0 and row < self.numRows() and col >= 0 and col < self.numCols(),\
               "subsripts out of range"
        
        preNode = None
        curNode = self._listOfRows[row]
        while curNode is not None and curNode.col != col:
            preNode = curNode
            curNode = curNode.next

        # See if the element is in the list.
        if curNode is not None and curNode.col == col:
            if value == 0.0: # remove the node
                if curNode == self._listOfRows[row]:
                    self._listOfRows[row] = curNode.next
                else:
                    preNode.next = curNode.next
            else:   # change the node's value.
                curNode.value = value
        # Otherwise, the element is not in the list
        elif value != 0.0:
            newNode = _MatrixElementNode( col, value )
            newNode.next = curNode
            if curNode == self._listOfRows[row]:
                self._listOfRows[row] = newNode
            else:
                preNode.next = newNode

    # Scales the matrix by the given scalar
    def scaleBy( self, scalar ):
        for row in range( self.numRows() ):
            curNode = self._listOfRows[row]
            while curNode is not None:
                self[row, curNode.col] = curNode.value * scalar
                curNode = curNode.next

    # Creates and returns a new matrix that is the transpose of this matrix.
    def transpose( self ):
        newMatrix = SparseMatrix( self.numCols(), self.numRows() )
        for row in range( self.numRows() ):
            curNode = self._listOfRows[row]
            while curNode is not None:
                newMatrix[curNode.col, row] = curNode.value
                curNode = curNode.next
        return newMatrix

    # Matrix addition: newMatrix = self + rhsMatrix.
    def __add__( self, rhsMatrix ):
        # Make sure the two matrices have the correct size.
        assert rhsMatrix.numRows() == self.numRows() and \
               rhsMatrix.numCols() == self.numCols(), \
               "Matrix sizes not compatable for adding."

        # Create a new sparse matrix of the same size.
        newMatrix = SparseMatrix( self.numRows(), self.numCols() )

        # Duplicate the element of this matrix to the new matrix.
        for row in range( self.numRows() ):
            curNode = self._listOfRows[row]
            while curNode is not None:
                newMatrix[row, curNode.col] = curNode.value
                curNode = curNode.next

        # Add the elements of the rhsMatrix to the new matrix.
        for row in range( rhsMatrix.numRows() ):
            curNode = rhsMatrix._listOfRows[row]
            while curNode is not None:
                value = newMatrix[row, curNode.col]
                value += curNode.value
                newMatrix[row, curNode.col] = value
                curNode = curNode.next

        return newMatrix

    # Matrix subtraction: newMatrix = self - rhsMatrix
    def __sub__( self, rhsMatrix ):
        # Make sure the two matrices have the correct size.
        assert rhsMatrix.numRows() == self.numRows() and \
               rhsMatrix.numCols() == self.numCols(), \
               "Matrix sizes not compatable for subtract."

        # Create a new sparse matrix of the same size.
        newMatrix = SparseMatrix( self.numRows(), self.numCols() )

        # Duplicate the element of this matrix to the new matrix.
        for row in range( self.numRows() ):
            curNode = self._listOfRows[row]
            while curNode is not None:
                newMatrix[row, curNode.col] = curNode.value
                curNode = curNode.next

        # Sub the elements of the rhsMatrix to the new matrix.
        for row in range( rhsMatrix.numRows() ):
            curNode = rhsMatrix._listOfRows[row]
            while curNode is not None:
                value = newMatrix[row, curNode.col]
                value -= curNode.value
                newMatrix[row, curNode.col] = value
                curNode = curNode.next

        return newMatrix

    # Matrix multiplication: newMatrix = self * rhsMatrix
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

# Storage class for creating matrix element nodes.
class _MatrixElementNode:
    def __init__( self, col, value ):
        self.col = col
        self.value = value
        self.next = None


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
    print 'A * C: '
    for i in range( mul_mat_03.numRows() ):
        for j in range( mul_mat_03.numCols() ):
            print mul_mat_03[i, j],
        print ''

    transpos_mat = sparse_mat_A.transpose()
    print 'A.T: '
    for i in range( transpos_mat.numRows() ):
        for j in range( transpos_mat.numCols() ):
            print transpos_mat[i, j],
        print ''

    sparse_mat_B.scaleBy(3)
    print 'B * 3: '
    for i in range( sparse_mat_B.numRows() ):
        for j in range( sparse_mat_B.numCols() ):
            print sparse_mat_B[i, j],
        print ''
