# Implementation of the Set ADT container using a Python list
class mySet:
    # Creates an empty set instance
    def __init__( self ):
        self._theElements = list()

    # Returns the number of items in the set.
    def __len__( self ):
        return len( self._theElements )

    # Determines if an element is in the set.
    def __contains__( self, element ):
        return element in self._theElements

    # Adds a new unique element to the set.
    def add( self, element ):
        if element not in self:
            self._theElements.append( element )

    # Removes an element from the set.
    def remove( self, element ):
        assert element in self, "The element must be in the set."
        self._theElements.remove( item )

    # Determins if two sets are equal.
    def __eq__( self, setB):
        if len( self ) != len( setB ):
            return False
        else:
            return self.isSubsetOf( setB )

    # Determins if this set is a subset of setB.
    def isSubsetOf( self, setB ):
        for element in self:
            if element not in setB:
                return False
        return True

    # Creates a new set from the union of this set and setB
    def union( self, setB ):
        newSet = mySet()
        newSet._theElements.extend( self._theElements )
        for element in setB:
            if element not in self : 
                newSet._theElements.append( element )
        return newSet

    # Creates a new set from the intersection: self set and setB.
    def interset( self, setB ):
        newSet = mySet()
        for element in self:
            if element in setB:
                newSet._theElements.append( element )
        return newSet

    # Creates a new set from the difference: self set and setB.
    def difference( self, setB ):
        newSet = mySet()
        for element in self:
            if element not in setB:
                newSet._theElements.append( element )
        return newSet

    # Returns an iterator for traversing the list of items.
    def __iter__( self ):
        return _SetIterator( self._theElements )

# An iterator for the Set ADT.
class _SetIterator:
    def __init__( self, theSet ):
        self._setRef = theSet
        self._curNdx = 0

    def __iter__( self ):
        return self

    def next( self ):
        if self._curNdx < len( self._setRef ):
            entry = self._setRef[ self._curNdx ]
            self._curNdx += 1
            return entry
        else:
            raise StopIteration


if __name__ == '__main__':
    mySetA = mySet()
    mySetA.add(6)
    mySetA.add(3)
    mySetA.add(2)
    mySetA.add(1)
    mySetA.add(3)
    print "Set A: "
    for ele in mySetA:
        print ele, 
    print ""
    
    mySetB = mySet()
    mySetB.add(4)
    mySetB.add(1)
    mySetB.add(7)
    mySetB.add(2)
    print "Set B: "
    for ele in mySetB:
        print ele,
    print ""

    # Set Union
    mySetC = mySetA.union(mySetB)
    print "A + B: "
    for ele in mySetC:
        print ele,
    print ""

    # Set Interset
    mySetD = mySetA.interset(mySetB)
    print "interset(A, B)"
    for ele in mySetD:
        print ele,
    print ""

    mySetE = mySetB.interset(mySetA)
    print "interset(B, A)"
    for ele in mySetE:
        print ele,
    print ""

    # Set difference
    mySetF = mySetA.difference(mySetB)
    print "A - B: "
    for ele in mySetF:
        print ele,
    print ""

    mySetG = mySetB.difference(mySetA)
    print "B - A: "
    for ele in mySetG:
        print ele,
    print ""
