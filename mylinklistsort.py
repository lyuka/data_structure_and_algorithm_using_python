# Sorts a linked list
from mylinklist import ListNode, traversal, append_node, insert_sorted

# ===================Insertion Sort==============
def llistInsertonSort( origList ):
    if origList is None:
        return None

    newList = None
    while origList is not None:
        curNode = origList
        origList = origList.next
        curNode.next = None
        newList = _addToSortedList( newList, curNode)
    return newList

def _addToSortedList( newList, curNode ):
    newList = insert_sorted( newList, curNode.data )
    return newList

if __name__ == '__main__':
    head = None
    tail = None
    ( head, tail ) = append_node( head, tail, 23 )
    ( head, tail ) = append_node( head, tail, 2 )
    ( head, tail ) = append_node( head, tail, 51 )
    ( head, tail ) = append_node( head, tail, 18 )
    ( head, tail ) = append_node( head, tail, 4 )
    ( head, tail ) = append_node( head, tail, 31 )
    traversal( head )
    print '=======Insertion Sort======='
    origList = head
    sortedList = llistInsertonSort( origList )
    traversal( sortedList )
