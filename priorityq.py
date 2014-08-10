# Implemenetion of the unbounded Priority Queue ADT using a Python list
# with new items appended to the end..

class PriorityQueue:
    # Create an empty unbounded priority queue.
    def __init__( self ):
        self._qList = list()

    # Returns True if the queue is empty.
    def isEmpty( self ):
        return len( self ) == 0

    # Returns the number of items in the queue.
    def __len__( self ):
        return len( self._qList )

    # Adds the given item to the queue.
    def enqueue( self, item, priority ):
        # Create a new instance of the storage class and append it to the list.
        entry = _PriorityQEntry( item, priority)
        self._qList.append( entry )

    # Removes and returns the first item in the queue.
    def dequeue( self ):
        assert not self.isEmpty(), "Cannot dequeue from an empty queue."

        # Find the entry with the highest priority.
        highest = self._qList[0].priority
        h_ndx = 0
        for i in range( len(self) ):
            if self._qList[i].priority < highest:
                highest = self._qList[i].priority
                h_ndx = i
                
        entry = self._qList.pop( h_ndx )
        return entry.item

# Private storage class for associating queue items with their priority.
class _PriorityQEntry( object ):
    def __init__( self, item, priority ):
        self.item = item
        self.priority = priority

if __name__ == '__main__':
    Q = PriorityQueue()
    Q.enqueue( 'purple', 5 )
    Q.enqueue( 'black', 1 )
    Q.enqueue( 'orange', 3 )
    Q.enqueue( 'white', 0 )
    Q.enqueue( 'green', 1 )
    Q.enqueue( 'yellow', 5)

    while not Q.isEmpty():
        item = Q.dequeue()
        print item
