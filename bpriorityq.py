# Implementation of the bounded Priority Queue ADT using an array of
# queues in which the queues are implemented using a linked list.
from myarray import myArray
from llistqueue import Queue

class BPriorityQueue:
    # Creates an empty bounded priority queue.
    def __init__( self, numLevels ):
        self._qSize = 0
        self._qLevels = myArray( numLevels )
        for i in range( numLevels ):
            self._qLevels[i] = Queue()

    # Returns True if the queue is empty.
    def isEmpty( self ):
        return len( self ) == 0

    # Returns the number of items in the queue.
    def __len__( self ):
        return self._qSize

    # Adds the given item to the queue.
    def enqueue( self, item, priority ):
        assert priority >= 0 and priority < len(self._qLevels), \
               "Invalid priority level."
        self._qLevels[priority].enqueue(item)
        self._qSize += 1

    # Removes and returns the next item in the queue
    def dequeue( self ):
        assert not self.isEmpty(), "cannot dequeue from an empty queue."
        i = 0
        p = len(self._qLevels)
        while i < p and self._qLevels[i].isEmpty():
            i += 1
        self._qSize -= 1
        return self._qLevels[i].dequeue()


if __name__ == '__main__':
    Q = BPriorityQueue(6)
    Q.enqueue( 'purple', 5 )
    Q.enqueue( 'black', 1 )
    Q.enqueue( 'orange', 3 )
    Q.enqueue( 'white', 0 )
    Q.enqueue( 'green', 1 )
    Q.enqueue( 'yellow', 5)

    #print len(Q)

    while not Q.isEmpty():
        item = Q.dequeue()
        print item
        #print len(Q)
