# An array-based implementation of the max-heap.
from myarray import myArray

class MaxHeap:
    # Create a max-heap with maximum capacity of maxSize.
    def __init__( self, maxSize ):
        self._elements = myArray( maxSize )
        self._count = 0

    # Returns the number of items in the heap.
    def __len__( self ):
        return self._count

    # Return the maximum capacity of the heap.
    def capacity( self ):
        return len( self._elements )

    # Traversal the heap
    def traversal( self ):
        for i in range( len( self ) ):
            print self._elements[i],
        print ''
        
    # Add a new value to the heap.
    def add( self, value ):
        assert len( self ) < self.capacity(), "Cannot add to a full heap."
        self._elements[ self._count ] = value
        self._count += 1
        # Sift the new value up the tree.
        self._siftUp( self._count - 1 )

    # Extract the maximum value from the heap.
    def extract( self ):
        assert len( self ) > 0, "Cannot extract from an empty heap."
        value = self._elements[0]
        self._count -= 1
        self._elements[0] = self._elements[ self._count ]
        # Sift the root value down the tree.
        self._siftDown( 0 )
        return value

    # Sift the value at the ndx element up the tree.
    def _siftUp( self, ndx ):
        if ndx > 0:
            parent = (ndx-1) // 2
            if self._elements[ndx] > self._elements[parent]:
                tmp = self._elements[ndx]
                self._elements[ndx] = self._elements[parent]
                self._elements[parent] = tmp
                #print 'swap ', self._elements[ndx], self._elements[parent]
                #self.traversal()
                self._siftUp( parent )

    # Sift the value at the ndx element down the tree.
    def _siftDown( self, ndx ):
        left = 2 * ndx + 1
        right = 2 * ndx + 2
        # Determine which node contains the larger value.
        largest = ndx
        if left < len( self ) and self._elements[left] >= self._elements[largest]:
            largest = left
        if right < len( self ) and self._elements[right] >= self._elements[largest]:
            largest = right
        if largest != ndx:
            #print 'swap: ', self._elements[ndx], self._elements[largest]
            tmp = self._elements[ndx]
            self._elements[ndx] = self._elements[largest]
            self._elements[largest] = tmp
            self._siftDown( largest )

if __name__ == '__main__':
    one_max_heap = MaxHeap(11)
    one_max_heap.add(100)
    one_max_heap.add(84)
    one_max_heap.add(71)
    one_max_heap.add(60)
    one_max_heap.add(23)
    one_max_heap.add(12)
    one_max_heap.add(29)
    one_max_heap.add(1)
    one_max_heap.traversal()
    
    print 'add 37: '
    one_max_heap.add(37)
    one_max_heap.traversal()
    
    one_max_heap.add(4)
    print 'add 4: '
    one_max_heap.traversal()

    print 'add 90: '
    one_max_heap.add(90)
    one_max_heap.traversal()

    print 'remove ', one_max_heap.extract()
    one_max_heap.traversal()
