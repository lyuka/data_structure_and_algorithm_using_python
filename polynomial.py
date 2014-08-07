# Implementation of the Polynomial ADT using a sorted linked list.
class Polynomial:
    # Create a new polynomial object.
    def __init__( self, degree = None, cofficient = None ):
        if degree is None:
            self._polyHead = None
        else:
            self._polyHead = _PolyTermNode(degree, cofficient)
        self._polyTail = self._polyHead

    # Return the degree of the polynomial.
    def degree( self ):
        if self._polyHead is None:
            return -1
        else:
            return self._polyHead.degree

    # Return the cofficient for the term of the given degree
    def __getitem__( self, degree ):
        assert self.degree() >= 0,\
               "Operation not permitted on an empty polynomial."
        curNode = self._polyHead
        while curNode is not None and curNode.degree > degree:
            curNode = curNode.next

        if curNode is None or curNode.degree != degree:
            return 0.0
        else:
            return curNode.coefficient

    # Evaluate the polynomial at the given scalar value.
    def evaluate( self, scalar ):
        assert self.degree() >= 0,\
               "Only non-empty polynomials can be evaluated."
        result = 0.0
        curNode = self._polyHead
        while curNode is not None:
            result += curNode.coefficient * (scalar ** curNode.degree)
            curNode = curNode.next
        return result

    # Polynomial addition: newPoly = self + rhsPoly.
    def __add__( self, rhsPoly ):
        assert self.degree() >= 0 and rhsPoly.degree() >= 0, \
               "Addition only allowed on non-empty polynomials."

        newPoly = Polynomial()
        nodeA = self._polyHead
        nodeB = rhsPoly._polyHead

        # Add corresponding terms until one list is empty.
        while nodeA is not None and nodeB is not None:
            if nodeA.degree > nodeB.degree:
                degree = nodeA.degree
                value = nodeA.coefficient
                nodeA = nodeA.next
            elif nodeA.degree < nodeB.degree:
                degree = nodeB.degree
                value = nodeB.coefficient
                nodeB = nodeB.next
            else:
                degree = nodeA.degree
                value = nodeA.coefficient + nodeB.coefficient
                nodeA = nodeA.next
                nodeB = nodeB.next
            newPoly._appendTerm( degree, value )

        # If self List contains more terms
        while nodeA is not None:
            newPoly._appendTerm( nodeA.degree, nodeA.coefficient )
            nodeA = nodeA.next

        # Or rhs List contains more terms
        while nodeB is not None:
            newPoly._appendTerm( nodeB.degree, nodeB.coefficient )
            nodeB = nodeB.next

        return newPoly

    # Polynomial subtraction: newPoly = self - rhsPoly.
    def __sub__( self, rhsPoly ):
        newPoly = Polynomial()
        nodeA = self._polyHead
        nodeB = rhsPoly._polyHead

        # Add corresponding terms until one list is empty.
        while nodeA is not None and nodeB is not None:
            if nodeA.degree > nodeB.degree:
                degree = nodeA.degree
                value = nodeA.coefficient
                nodeA = nodeA.next
            elif nodeA.degree < nodeB.degree:
                degree = nodeB.degree
                value = nodeB.coefficient
                nodeB = nodeB.next
            else:
                degree = nodeA.degree
                value = nodeA.coefficent - nodeB.coefficient
                nodeA = nodeA.next
                nodeB = nodeB.next
            newPoly._appendTerm( degree, value )

        # If self List contains more terms
        while nodeA is not None:
            newPoly._appendTerm( nodeA.degree, nodeA.coefficient )
            nodeA = nodeA.next

        # Or rhs List contains more terms
        while nodeB is not None:
            newPoly._appendTerm( nodeB.degree, nodeB.coefficient )
            nodeB = nodeB.next

        return newPoly

    # Polynomial multiplication: newPoly = self * rhsPoly.
    def __mul__( self, rhsPoly ):
        assert self.degree() >= 0 and rhsPoly.degree() >= 0, \
               "Multiplication only allowed on non-empty polynomials."

        # Create a new polynomial by multiplying rhsPoly by the first term.
        node = self._polyHead
        newPoly = rhsPoly._termMultiply( node )

        # Iterate through the remaining terms of the poly computing the
        # product of the rhsPoly by each term.
        node = node.next
        while node is not None:
            tempPoly = rhsPoly._termMultiply( node )
            newPoly = newPoly + tempPoly
            node = node.next

        return newPoly

    # Helper method for creating a new polynomial from multiplying an
    # exsiting polynomial by another term.
    def _termMultiply( self, termNode ):
        newPoly = Polynomial()

        # Iterate through the terms and compute the product of each term and
        # the term in termNode.
        curr = self._polyHead
        while curr is not None:
            newDegree = curr.degree + termNode.degree
            newCoeff = curr.coefficient * termNode.coefficient

            newPoly._appendTerm( newDegree, newCoeff )
            curr = curr.next
        return newPoly

    # Helper method for appending terms to the polynomial.
    def _appendTerm( self, degree, coefficient ):
        if coefficient != 0.0:
            newTerm = _PolyTermNode( degree, coefficient )
            if self._polyHead is None:
                self._polyHead = newTerm
            else:
                self._polyTail.next = newTerm
            self._polyTail = newTerm

# Class for creating polynomial term nodes used with the linked list.
class _PolyTermNode( object ):
    def __init__( self, degree, coefficient ):
        self.degree = degree
        self.coefficient = coefficient
        self.next = None


if __name__ == '__main__':
    poly_A = Polynomial(3, +5.0)
    poly_B = Polynomial(2, +3.0)
    poly_C = Polynomial(0, +7.0)   
    poly_D = poly_A + poly_B + poly_C
    print 'Polynomial D: '
    for i in range(poly_D.degree()+1)[:1:-1]:
        if poly_D[i] != 0.0:
            print '( ' + str(poly_D[i]) + ' * x ^ ' + str(i) + ' )' + ' + ',
    print str(poly_D[0])

    poly_A = Polynomial(4, +2.0)
    poly_B = Polynomial(2, -3.0)
    poly_C = Polynomial(5, -1.0)
    poly_E = poly_A + poly_B + poly_C
    print 'Polynomial E: '
    for i in range(poly_E.degree()+1)[:1:-1]:
        if poly_E[i] != 0.0:
            print '( ' + str(poly_E[i]) + ' * x ^ ' + str(i) + ' )' + ' + ',
    print str(poly_E[0])

    poly_F = poly_D * poly_E
    print 'Polynomial F = D * E: '
    for i in range(poly_F.degree()+1)[:1:-1]:
        if poly_F[i] != 0.0:
            print '( ' + str(poly_F[i]) + ' * x ^ ' + str(i) + ' )' + ' + ',
    print str(poly_F[0])
